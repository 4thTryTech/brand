#!/usr/bin/env python3
"""Plan steps 3.1 and 3.4 (lettering): the wordmark and the tagline lockup as outlined SVGs.

Needs fonttools and the font files under ../fonts/ (see textpath.py). Writes to out/elements/.
The lettering is converted to shapes, so these files look the same everywhere and need no font.
"""
import os
from fontTools.pens.boundsPen import BoundsPen
from fontTools.svgLib.path import parse_path
from build_d import PALETTES
from textpath import text_path

L, D = PALETTES[0]["light"], PALETTES[0]["dark"]
NAME, TAG = "4th Try Tech", "When the 3rd try wasn’t enough, keep going."
SIZE, TRACK = 124, 2            # same proportions as the splash: tagline 46 on a 124 wordmark, 96 below


def bounds(d):
    pen = BoundsPen(None)
    parse_path(d, pen)
    return pen.bounds


def svg(paths, box, title):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    body = "".join(f'<g id="{gid}"><path d="{d}" fill="{fill}"/></g>' for gid, d, fill in paths)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.1f} {y0:.1f} {w:.1f} {h:.1f}" width="{w:.0f}" height="{h:.0f}" role="img" aria-labelledby="t">'
            f'<title id="t">{title}</title>{body}</svg>')


def wordmark(color, name):
    d, _ = text_path(NAME, "fredoka-600", SIZE, 0, 0, "middle", TRACK)
    b = bounds(d)
    return svg([("wordmark", d, color)], (b[0] - 4, b[1] - 4, b[2] + 4, b[3] + 4), f"4th Try Tech wordmark ({name})")


def lockup(c_name, c_tag, name):
    d1, _ = text_path(NAME, "fredoka-600", SIZE, 0, 0, "middle", TRACK)
    d2, _ = text_path(TAG, "nunito-400", 46, 0, 96, "middle")
    b1, b2 = bounds(d1), bounds(d2)
    box = (min(b1[0], b2[0]) - 4, b1[1] - 4, max(b1[2], b2[2]) + 4, b2[3] + 4)
    return svg([("wordmark", d1, c_name), ("tagline", d2, c_tag)], box, f"4th Try Tech. {TAG} ({name})")


FILES = {}
for mode, (cn, ct) in {"light": (L["body"], L["ink"]), "dark": (D["body"], D["ink"]), "mono-ink": (L["ink"], L["ink"]), "mono-reversed": ("#FFFFFF", "#FFFFFF")}.items():
    FILES[f"wordmark-{mode}.svg"] = wordmark(cn, mode)
    FILES[f"tagline-lockup-{mode}.svg"] = lockup(cn, ct, mode)

if __name__ == "__main__":
    os.makedirs("out/elements", exist_ok=True)
    for n, s in FILES.items():
        open(os.path.join("out/elements", n), "w").write(s)
    print("wrote", sorted(FILES))
