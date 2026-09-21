#!/usr/bin/env python3
"""Plan step 3.3: the diagrams used by GUIDELINES.md (clear space, size ladder, backgrounds, misuse).

Writes SVGs to out/guidelines/. Plain Python, no dependencies. Labels use the system sans so the
diagrams read correctly anywhere, including GitHub, without the brand fonts.
"""
import os
from build_d import PALETTES
from build_logo import full, mono
from build_elements import micro

L, D = PALETTES[0]["light"], PALETTES[0]["dark"]
SANS = "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
CLEAR = 1 / 8           # clear space on every side, as a fraction of the logo's diameter
_n = [0]


def place(svg, x, y, size, extra=""):
    """Nest a finished 512-unit drawing at x, y. Ids are made unique so several can share one file."""
    _n[0] += 1
    u = f"u{_n[0]}-"
    inner = svg[svg.index(">") + 1:-len("</svg>")]
    inner = inner[inner.index("</title>") + 8:] if "</title>" in inner else inner
    if inner.startswith("<desc"):
        inner = inner[inner.index("</desc>") + 7:]
    for i in ("disc-clip", "body-clip", "badge-knock", "knock", '"c"', "#c)"):
        if i == '"c"':
            inner = inner.replace('id="c"', f'id="{u}c"')
        elif i == "#c)":
            inner = inner.replace("url(#c)", f"url(#{u}c)")
        else:
            inner = inner.replace(f'id="{i}"', f'id="{u}{i}"').replace(f"url(#{i})", f"url(#{u}{i})")
    import re
    inner = re.sub(r' id="(?!u\d+-)[^"]*"', "", inner)
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 512 512" {extra}>{inner}</svg>'


def doc(w, h, title, body, bg=None):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t" font-family="{SANS}">'
            f'<title id="t">{title}</title><rect width="{w}" height="{h}" fill="{bg or L["ground"]}"/>{body}</svg>')


def label(x, y, s, size=14, anchor="middle", color=None, weight=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color or L["ink"]}" font-weight="{weight}">{s}</text>'


def clear_space():
    S = 320; x = S * CLEAR; W = H = S + 4 * x
    o0 = 2 * x                                   # logo origin
    g = f'stroke="{L["fin"]}" stroke-width="1.5" stroke-dasharray="6 5" fill="none"'
    b = [f'<rect x="{x}" y="{x}" width="{S + 2 * x}" height="{S + 2 * x}" fill="{L["fin"]}" opacity=".10"/>',
         f'<rect x="{o0}" y="{o0}" width="{S}" height="{S}" fill="{L["ground"]}"/>',
         f'<rect x="{x}" y="{x}" width="{S + 2 * x}" height="{S + 2 * x}" {g}/>', f'<rect x="{o0}" y="{o0}" width="{S}" height="{S}" {g}/>',
         place(full(L, "x"), o0, o0, S)]
    for cx, cy in ((W / 2, x * 1.5), (W / 2, H - x * 1.5), (x * 1.5, H / 2), (W - x * 1.5, H / 2)):
        b.append(f'<rect x="{cx - x / 2}" y="{cy - x / 2}" width="{x}" height="{x}" fill="{L["fin"]}" opacity=".25"/>' + label(cx, cy + 6, "x", 17, color=L["fin2"], weight=600))
    b.append(label(W / 2, H - 14, "x = one eighth of the logo's diameter", 14))
    return doc(W, H, "Clear space around the 4th Try Tech logo", "".join(b))


def size_ladder():
    rows = [("Roundel, full color", full(L, "x"), 64, "64 px / 20 mm and up"), ("Roundel, one color", mono(L["ink"], "x"), 80, "80 px / 25 mm and up"),
            ("Small roundel", full(L, "x", small=True), 32, "32 to 63 px / 10 to 19 mm"), ("Micro icon", micro(L), 16, "16 to 31 px, screens only")]
    W, rh = 640, 104
    b = []
    for i, (name, svg, s, rule) in enumerate(rows):
        y = i * rh
        if i:
            b.append(f'<line x1="24" y1="{y}" x2="{W - 24}" y2="{y}" stroke="{L["ink"]}" opacity=".15"/>')
        b.append(place(svg, 24 + (80 - s) / 2, y + (rh - s) / 2, s))
        b.append(label(136, y + rh / 2 - 4, name, 16, "start", weight=600) + label(136, y + rh / 2 + 18, rule, 14, "start"))
        b.append(label(W - 24, y + rh / 2 + 5, f"shown at {s} px", 12, "end", color="#6B6E85"))
    return doc(W, rh * len(rows), "Minimum sizes for each version of the logo", "".join(b))


def backgrounds():
    cells = [(L["ground"], full(L, "x"), "Light logo on ground", L["ink"]), ("#FFFFFF", full(L, "x"), "Light logo on white", L["ink"]),
             (D["ground"], full(D, "x"), "Dark logo on dark ground", D["ink"]), (L["body"], mono("#FFFFFF", "x"), "Reversed on brand slate", "#FFFFFF"),
             (L["fin"], mono("#FFFFFF", "x"), "Reversed on coral", "#FFFFFF"), (L["sun"], mono(L["ink"], "x"), "Ink on sun", L["ink"])]
    cw, ch = 220, 230
    b = []
    for i, (bg, svg, name, ink) in enumerate(cells):
        x, y = (i % 3) * cw, (i // 3) * ch
        b.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="{bg}"/>' + place(svg, x + 45, y + 28, 130) + label(x + cw / 2, y + ch - 28, name, 13, color=ink))
    return doc(cw * 3, ch * 2, "Approved backgrounds for the logo", "".join(b), bg="#FFFFFF")


def misuse():
    base = full(L, "x")
    hue = base
    for a, c in ((L["body"], "#7A4FA3"), (L["fin"], "#2FA36B"), (L["sun"], "#F7E04A")):
        hue = hue.replace(a, c)
    noring = base[:base.rindex('<circle id="ring"')] + "</svg>"
    cells = [("Do not stretch or squash", lambda x, y: f'<g transform="translate({x + 20} {y + 45}) scale(1.38 .74)">{place(base, 0, 0, 130)}</g>'),
             ("Do not tilt or rotate", lambda x, y: f'<g transform="rotate(-24 {x + 110} {y + 93})">{place(base, x + 45, y + 28, 130)}</g>'),
             ("Do not recolor", lambda x, y: place(hue, x + 45, y + 28, 130)),
             ("Do not add shadows or effects", lambda x, y: f'<g filter="url(#sh)">{place(base, x + 45, y + 28, 130)}</g>'),
             ("Do not remove the ring or parts", lambda x, y: place(noring, x + 45, y + 28, 130)),
             ("Do not place color on color", lambda x, y: f'<rect x="{x + 16}" y="{y + 14}" width="188" height="158" fill="{L["flame"]}"/>' + place(base, x + 45, y + 28, 130))]
    cw, ch = 220, 230
    b = ['<defs><filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="7" dy="9" stdDeviation="6" flood-color="#000" flood-opacity=".5"/></filter></defs>']
    for i, (name, fn) in enumerate(cells):
        x, y = (i % 3) * cw, (i // 3) * ch
        b.append(fn(x, y))
        b.append(f'<g transform="translate({x + 186} {y + 34})"><circle r="14" fill="{L["fin2"]}"/><path d="M-6 -6 L6 6 M6 -6 L-6 6" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/></g>')
        b.append(label(x + cw / 2, y + ch - 28, name, 13))
        if i % 3:
            b.append(f'<line x1="{x}" y1="{y + 16}" x2="{x}" y2="{y + ch - 16}" stroke="{L["ink"]}" opacity=".12"/>')
    return doc(cw * 3, ch * 2, "Ways the logo must not be used", "".join(b))


FILES = {"clear-space.svg": clear_space, "minimum-sizes.svg": size_ladder, "backgrounds.svg": backgrounds, "misuse.svg": misuse}

if __name__ == "__main__":
    os.makedirs("out/guidelines", exist_ok=True)
    for n, fn in FILES.items():
        open(os.path.join("out/guidelines", n), "w").write(fn())
    print("wrote", sorted(FILES))
