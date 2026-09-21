#!/usr/bin/env python3
"""Plan phase 4: horizontal versions. Header lockups (roundel + wordmark), a stacked lockup, and the
tablet and desktop hero artwork. Needs fonttools and ../fonts/ (lettering is outlined via textpath.py).

Writes to out/lockups/ and out/hero/.
"""
import os
from build import BASE_FLAME, BASE_CORE
from build_c import BODY, FIN_L, FIN_R, NOZZLE, CFIN
from build_d import PALETTES
from build_logo import full, mono, FOUR
from build_guides import place
from build_h import icons
from textpath import text_path

L, D = PALETTES[0]["light"], PALETTES[0]["dark"]
NAME, TAG = "4th Try Tech", "When the 3rd try wasn’t enough, keep going."
CAP = 0.70   # Fredoka cap height as a share of the type size, close enough for centering


def doc(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" role="img" aria-labelledby="t">'
            f'<title id="t">{title}</title>{body}</svg>')


def horizontal(mark, c_name, name):
    """Roundel left, wordmark right, centered on the roundel. Gap = one eighth of the roundel (the clear-space unit)."""
    S = 200; size = S * 0.56; gap = S / 8
    d, w = text_path(NAME, "fredoka-600", size, S + gap, S / 2 + size * CAP / 2, "start", tracking=size * 2 / 124)
    return doc(S + gap + w + 4, S, f"4th Try Tech logo with wordmark ({name})", place(mark, 0, 0, S) + f'<g id="wordmark"><path d="{d}" fill="{c_name}"/></g>')


def stacked(mark, c_name, c_tag, name, tagline=True):
    """Roundel above the wordmark, tagline beneath. For square-ish spaces: title slides, covers, about pages."""
    S = 320; size = 96
    d1, w1 = text_path(NAME, "fredoka-600", size, 0, 0, "middle", tracking=size * 2 / 124)
    d2, w2 = text_path(TAG, "nunito-400", size * 46 / 124, 0, size * 96 / 124, "middle")
    W = max(w1, w2 if tagline else 0, S) + 8
    y = S + S / 8 + size * CAP
    body = place(mark, (W - S) / 2, 0, S) + f'<g transform="translate({W / 2:.1f} {y:.1f})"><g id="wordmark"><path d="{d1}" fill="{c_name}"/></g>'
    if tagline:
        body += f'<g id="tagline"><path d="{d2}" fill="{c_tag}"/></g>'
    return doc(W, y + (size * 96 / 124 + 16 if tagline else 12), f"4th Try Tech stacked logo ({name})", body + "</g>")


def hero(W, H, P, name):
    """The H2 launch scene turned sideways: words on the left, sun and rocket on the right, stripes edge to edge."""
    k = H / 1440                                    # everything scales from the 1440-high desktop layout
    wide = W / H > 1.5
    cx, cy, r = W * (0.70 if wide else 0.75), H * 0.47, (470 if wide else 440) * k
    sy, sh = cy + 215 * k, 56 * k
    s = 2.95 * k
    o = [f'<defs><clipPath id="bc"><path d="{BODY}"/></clipPath></defs><rect width="{W}" height="{H}" fill="{P["ground"]}"/>',
         f'<circle id="sun" cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{P["sun"]}"/>', '<g id="stripes">']
    for i, c in enumerate([P["flame"], P["fin"], P["body"]]):
        o.append(f'<rect x="0" y="{sy + i * sh:.1f}" width="{W}" height="{sh:.1f}" fill="{c}"/>')
    o.append("</g>")
    pts = [("planet", W * .08, H * .16, 30 * k), ("plus", W * .40, H * .12, 22 * k), ("plus", W * .93, H * .20, 20 * k), ("plus", W * .04, H * .94, 16 * k), ("plus", W * .46, H * .90, 18 * k), ("planet", W * .95, H * .91, 20 * k)]
    o.append(f'<g id="icons">{icons(P, pts)}</g>')
    o.append(f'<g id="rocket" transform="translate({cx:.1f} {cy + 75 * k:.1f}) scale({s:.4f}) translate(-200 -242)">')
    o.append(f'<g fill="{P["ground"]}" stroke="{P["ground"]}" stroke-width="14" stroke-linejoin="round">' + "".join(f'<path d="{d}"/>' for d in (BODY, FIN_L, FIN_R, NOZZLE, BASE_FLAME)) + "</g>")
    o.append(f'<g id="flame"><path d="{BASE_FLAME}" fill="{P["flame"]}"/><path d="{BASE_CORE}" fill="{P["sun"]}"/></g><g id="fins"><path d="{FIN_L}" fill="{P["fin"]}"/><path d="{FIN_R}" fill="{P["fin"]}"/></g>'
             f'<path d="{NOZZLE}" fill="{P["nozzle"]}"/><path id="body" d="{BODY}" fill="{P["body"]}"/><g clip-path="url(#bc)"><rect x="200" y="0" width="70" height="340" fill="#000" opacity=".16"/>'
             f'<rect x="140" y="110" width="120" height="9" fill="{P["sun"]}"/><rect x="140" y="296" width="120" height="7" fill="{P["sun"]}"/></g>'
             f'<path d="{CFIN}" fill="{P["flame"]}"/><g id="badge"><circle cx="200" cy="205" r="35" fill="{P["ground"]}" stroke="{P["success"]}" stroke-width="6"/>'
             f'<path d="{FOUR}" fill="none" stroke="{P["success"]}" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"/></g></g>')
    x = W * 0.07; y = sy - 120 * k
    size = min(150 * k, ((cx - r) - x - 50 * k) / 717.4 * 124)     # the wordmark never reaches the sun
    d1, w1 = text_path(NAME, "fredoka-600", size, x, y, "start", tracking=size * 2 / 124)
    d2, _ = text_path("When the 3rd try wasn’t enough,", "nunito-400", size * .40, x, sy + 3 * sh + 110 * k, "start")
    d3, _ = text_path("keep going.", "nunito-400", size * .40, x, sy + 3 * sh + 110 * k + size * .54, "start")
    o.append(f'<g id="wordmark"><path d="{d1}" fill="{P["body"]}"/></g><g id="tagline"><path d="{d2}" fill="{P["ink"]}"/><path d="{d3}" fill="{P["ink"]}"/></g>')
    return doc(W, H, f"4th Try Tech hero artwork ({name})", "".join(o))


LOCKUPS, HEROES = {}, {}
for mode, (mark, small, cn, ct) in {"light": (full(L, "x"), full(L, "x", small=True), L["body"], L["ink"]), "dark": (full(D, "x"), None, D["body"], D["ink"]),
                                    "mono-ink": (mono(L["ink"], "x"), None, L["ink"], L["ink"]), "mono-reversed": (mono("#FFFFFF", "x"), None, "#FFFFFF", "#FFFFFF")}.items():
    LOCKUPS[f"lockup-horizontal-{mode}.svg"] = horizontal(mark, cn, mode)
    LOCKUPS[f"lockup-stacked-{mode}.svg"] = stacked(mark, cn, ct, mode)
LOCKUPS["lockup-horizontal-small-light.svg"] = horizontal(full(L, "x", small=True), L["body"], "small sizes, light")
for mode, P in (("light", L), ("dark", D)):
    HEROES[f"hero-desktop-{mode}.svg"] = hero(2560, 1440, P, f"desktop 16:9, {mode}")
    HEROES[f"hero-tablet-{mode}.svg"] = hero(2048, 1536, P, f"tablet 4:3, {mode}")

if __name__ == "__main__":
    for d, files in (("out/lockups", LOCKUPS), ("out/hero", HEROES)):
        os.makedirs(d, exist_ok=True)
        for n, s in files.items():
            open(os.path.join(d, n), "w").write(s)
        print(d, sorted(files))
