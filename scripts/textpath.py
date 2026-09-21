#!/usr/bin/env python3
"""Turn a line of text into SVG path data, so brand lettering needs no font at view time.

Needs the fonttools package (pip install fonttools) and the font files under ../fonts/.
Applies the font's pair kerning (GPOS 'kern', pair adjustment), which is all this Latin lettering needs.
"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.varLib import instancer

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "..", "fonts")
_cache = {}


def font(name):
    """name: 'fredoka-600', 'nunito-400', 'nunito-600'."""
    if name not in _cache:
        if name == "fredoka-600":
            f = TTFont(os.path.join(FONTS, "Fredoka", "static", "Fredoka-SemiBold.ttf"))
        else:
            wght = int(name.split("-")[1])
            vf = TTFont(os.path.join(FONTS, "Nunito_Sans", "NunitoSans-VariableFont_YTLC,opsz,wdth,wght.ttf"))
            f = instancer.instantiateVariableFont(vf, {"wght": wght, "wdth": 100, "opsz": 12, "YTLC": 500})
        _cache[name] = (f, _kern_pairs(f))
    return _cache[name]


def _kern_pairs(f):
    """Return a function (left glyph, right glyph) -> x advance adjustment in font units."""
    if "GPOS" not in f:
        return lambda a, b: 0
    t = f["GPOS"].table
    idx = {i for fr in t.FeatureList.FeatureRecord if fr.FeatureTag == "kern" for i in fr.Feature.LookupListIndex}
    subs = []
    for i in sorted(idx):
        for st in t.LookupList.Lookup[i].SubTable:
            if st.LookupType == 9:
                st = st.ExtSubTable
            if st.LookupType == 2:
                subs.append(st)

    def kern(a, b):
        for st in subs:
            if a not in st.Coverage.glyphs:
                continue
            if st.Format == 1:
                ps = st.PairSet[st.Coverage.glyphs.index(a)]
                for r in ps.PairValueRecord:
                    if r.SecondGlyph == b:
                        return (r.Value1.XAdvance or 0) if r.Value1 else 0
            else:
                c1 = st.ClassDef1.classDefs.get(a, 0)
                c2 = st.ClassDef2.classDefs.get(b, 0)
                v = st.Class1Record[c1].Class2Record[c2].Value1
                if v and (v.XAdvance or 0):
                    return v.XAdvance
                if c2:          # a matching subtable stops the search, as in OpenType
                    return 0
        return 0
    return kern


def text_path(text, fontname, size, x=0, y=0, anchor="start", tracking=0):
    """Return (path data, width). y is the baseline; tracking is extra space per letter in output units."""
    f, kern = font(fontname)
    gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f["hmtx"]
    s = size / f["head"].unitsPerEm
    names = [cmap[ord(c)] for c in text]
    adv, pos = 0.0, []
    for i, g in enumerate(names):
        pos.append(adv)
        adv += hmtx[g][0] * s + tracking + (kern(g, names[i + 1]) * s if i + 1 < len(names) else 0)
    width = adv - tracking
    x0 = x - (width / 2 if anchor == "middle" else width if anchor == "end" else 0)
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    for g, p in zip(names, pos):
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x0 + p, y)))
    return pen.getCommands(), width


if __name__ == "__main__":
    d, w = text_path("4th Try Tech", "fredoka-600", 124, tracking=2)
    print(round(w, 1), len(d))
