#!/usr/bin/env python3
"""The self-hosted web fonts in fonts/web/: Latin-subset WOFF2 files of the four faces the brand uses.

Needs fonttools and brotli (pip install fonttools brotli) and the downloaded families under ../fonts/.
Writes to out/webfonts/; copy the results into fonts/web/.
"""
import os
from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fonts")
LATIN = ("U+0020-007E,U+00A0-00FF,U+0131,U+0152-0153,U+02C6,U+02DA,U+02DC,U+2013-2014,U+2018-201A,U+201C-201E,"
         "U+2022,U+2026,U+2039-203A,U+20AC,U+2122,U+2190-2193,U+2212")


def make(font, out):
    opt = subset.Options()
    opt.flavor, opt.layout_features, opt.name_IDs, opt.notdef_outline = "woff2", ["*"], ["*"], True
    s = subset.Subsetter(opt)
    s.populate(unicodes=subset.parse_unicodes(LATIN))
    s.subset(font)
    subset.save_font(font, out, opt)


if __name__ == "__main__":
    os.makedirs("out/webfonts", exist_ok=True)
    make(TTFont(os.path.join(F, "Fredoka", "static", "Fredoka-SemiBold.ttf")), "out/webfonts/fredoka-600.woff2")
    make(TTFont(os.path.join(F, "JetBrains_Mono", "static", "JetBrainsMono-Regular.ttf")), "out/webfonts/jetbrains-mono-400.woff2")
    for w in (400, 600):
        vf = TTFont(os.path.join(F, "Nunito_Sans", "NunitoSans-VariableFont_YTLC,opsz,wdth,wght.ttf"))
        make(instancer.instantiateVariableFont(vf, {"wght": w, "wdth": 100, "opsz": 12, "YTLC": 500}, updateFontNames=True), f"out/webfonts/nunito-sans-{w}.woff2")
    print("wrote out/webfonts/")
