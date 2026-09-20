#!/usr/bin/env python3
"""Round C: B5 (2010s flat + long shadow) as the primary theme, with the rounded rocket shape from A1/B1."""
import html
from build import geo, svg_open, text, CSS, BASE_FLAME, BASE_CORE

OUT = "out/round-c-styles.html"

BODY = "M200 38 C244 92 254 170 246 258 C243 298 234 322 226 332 H174 C166 322 157 298 154 258 C146 170 156 92 200 38 Z"
FIN_L = "M160 232 C118 256 100 310 104 368 C118 342 138 330 164 322 Z"
FIN_R = "M240 232 C282 256 300 310 296 368 C282 342 262 330 236 322 Z"
NOZZLE = "M176 330 H224 L229 346 H171 Z"
CFIN = "M197 252 H203 L205 352 H195 Z"
SIL = " ".join([BODY, FIN_L, FIN_R, NOZZLE])

BG, SLATE, CORAL, CORAL_D, SAGE, SAND, INK = "#F0EDE6", "#46607A", "#E07A5F", "#C9634A", "#5E9C7E", "#F2CC8F", "#3D405B"

def rocket(v, mode):
    g = geo(v); H = g["H"]; p = f"c{mode}{v}"
    bg = "#F0E9DC" if mode in (2, 4, 5) else BG
    fin_l, fin_r = (("#C44E33", "#A23C26") if mode == 5 else (CORAL, CORAL_D))
    o = [svg_open(H, f"Round C option {mode}, variation {v}")]
    defs = f'<clipPath id="{p}b"><path d="{BODY}"/></clipPath>'
    if mode == 3:
        defs += (f'<filter id="{p}g" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="5"/>'
                 f'<feColorMatrix type="matrix" values="0 0 0 0 .2  0 0 0 0 .2  0 0 0 0 .3  0 0 0 .8 -.36"/></filter>')
    o.append(f"<defs>{defs}</defs><rect width=\"400\" height=\"{H}\" fill=\"{bg}\"/>")
    if mode in (2, 4, 5):
        o.append(f'<circle cx="200" cy="182" r="124" fill="{SAND}"/>')
        stripes = [SAND, "#9FB3C8", "#6F8CA8", SLATE] if mode == 4 else [SAND, CORAL, CORAL_D, SLATE]
        for i, c in enumerate(stripes):
            o.append(f'<rect x="0" y="{264 + i * 11}" width="400" height="11" fill="{c}"/>')
    # long shadow, flattened through group opacity
    if mode in (1, 2, 3):
        o.append('<g opacity=".13" fill="#1B1B2F" stroke="#1B1B2F" stroke-width="3">' +
                 "".join(f'<path d="{SIL}" transform="translate({i} {i})"/>' for i in range(3, 330, 3)) + "</g>")
    ln = f'fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round" opacity=".55"'
    if mode in (1, 3):
        o.append(f'<ellipse cx="200" cy="200" rx="176" ry="54" {ln} transform="rotate(-24 200 200)" stroke-dasharray="2 9"/>')
    o.append(f'<circle cx="62" cy="96" r="13" {ln}/><path d="M44 100 C58 108 74 100 82 88" {ln}/>'
             f'<path d="M330 70 V86 M322 78 H338 M70 420 V432 M64 426 H76 M352 236 V246 M347 241 H357" {ln}/>')
    st = f'stroke="{INK}" stroke-width="3" stroke-linejoin="round"' if mode == 3 else ""
    if mode == 5:
        o.append(f'<path d="{SIL} {BASE_FLAME}" fill="{bg}" stroke="{bg}" stroke-width="12" stroke-linejoin="round"/>')
    o.append(f'<path d="{BASE_FLAME}" fill="{CORAL}" {st}/><path d="{BASE_CORE}" fill="{SAND}"/>'
             f'<path d="{FIN_L}" fill="{fin_l}" {st}/><path d="{FIN_R}" fill="{fin_r}" {st}/><path d="{NOZZLE}" fill="{INK}"/>'
             f'<path d="{BODY}" fill="{SLATE}"/><g clip-path="url(#{p}b)"><rect x="200" y="0" width="70" height="340" fill="#000" opacity=".14"/>'
             f'<rect x="140" y="110" width="120" height="9" fill="{SAND}"/><rect x="140" y="296" width="120" height="7" fill="{SAND}"/></g>')
    if mode == 3:
        o.append(f'<path d="{BODY}" fill="none" {st}/>')
    o.append(f'<path d="{CFIN}" fill="{CORAL}" {st}/>')
    if g["window"]:
        o.append(f'<circle cx="200" cy="192" r="24" fill="{SAND}" {st}/><circle cx="200" cy="192" r="15" fill="{bg}"/><path d="M200 177 A15 15 0 0 1 200 207 Z" fill="#000" opacity=".1"/>')
    cx, cy, r = g["cx"], g["cy"], g["r"]
    fam = "Montserrat, 'Helvetica Neue', sans-serif"
    if v == "A":
        if mode == 3:
            o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{bg}" stroke="{INK}" stroke-width="15"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{SAGE}" stroke-width="9"/>')
            o.append(text(cx, cy + 3, "4th", 70, SAGE, fam, 600))
        else:
            o.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 3}" fill="{bg}" stroke="{SAGE}" stroke-width="5"/>')
            o.append(text(cx, cy + 3, "4th", 70, SAGE, fam, 300, 'letter-spacing="1"'))
    else:
        if mode == 3:
            o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{bg}" stroke="{INK}" stroke-width="9"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{SAGE}" stroke-width="5"/>')
        else:
            o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{bg}" stroke="{SAGE}" stroke-width="4"/>')
        o.append(text(cx, cy + 1.5, "4th", 27, SAGE, fam, 600))
    if mode == 3:
        o.append(f'<rect width="400" height="{H}" filter="url(#{p}g)"/>')
    o.append("</svg>")
    return "".join(o)

SW = [("Body", SLATE), ("Fins / flame", CORAL), ("Success", SAGE), ("Sand", SAND), ("Ink", INK)]
STYLES = [
    dict(tag="C1", name="B5 with the rounded rocket", mode=1, bg=BG,
         line="The 2010s look unchanged, only the rocket swapped for the rounded A1/B1 shape, center fin and hull bands included.",
         wm="font-weight:300;letter-spacing:.3em;color:#3D405B;font-size:clamp(16px,4.2vw,24px)",
         facts=[("Kept from B5", "Long shadow, muted palette, hairline orbit and icons, light type"), ("Borrowed", "Rocket silhouette, center fin, hull bands"), ("Left out", "Grain, outlines, sun, stripes")]),
    dict(tag="C2", name="C1 plus the 1970s sun and stripes", mode=2, bg="#F0E9DC",
         line="Adds B1's big sun and stripe band, redrawn flat in B5's muted colors.",
         wm="font-weight:300;letter-spacing:.3em;color:#3D405B;font-size:clamp(16px,4.2vw,24px)",
         facts=[("Kept from B5", "Long shadow, muted palette, line icons, light type"), ("Borrowed", "Rocket shape; sun disc and stripe band from B1"), ("Left out", "Airbrush gradients, grain, orbit line")]),
    dict(tag="C4", name="C2, no shadow, cool stripes", mode=4, bg="#F0E9DC",
         sw=[("Body", SLATE), ("Fins / flame", CORAL), ("Success", SAGE), ("Sand", SAND), ("Stripe blue", "#6F8CA8")],
         line="Long shadow removed. The stripe band shifts to blue-greys so the warm fins stand clear of it.",
         wm="font-weight:300;letter-spacing:.3em;color:#3D405B;font-size:clamp(16px,4.2vw,24px)",
         facts=[("Changed", "No long shadow; stripes recolored sand to slate"), ("Fins", "Same coral as before; contrast comes from the stripes"), ("Trade-off", "Loses the warm 1970s stripe colors")]),
    dict(tag="C5", name="C2, no shadow, outlined rocket", mode=5, bg="#F0E9DC",
         sw=[("Body", SLATE), ("Fins", "#C44E33"), ("Flame / stripes", CORAL), ("Success", SAGE), ("Sand", SAND)],
         line="Long shadow removed. Warm stripes stay; the rocket gets a background-colored gap around it and deeper red fins.",
         wm="font-weight:300;letter-spacing:.3em;color:#3D405B;font-size:clamp(16px,4.2vw,24px)",
         facts=[("Changed", "No long shadow; gap around the rocket; fins darkened to #C44E33"), ("Stripes", "Same warm band as C2"), ("Trade-off", "The gap cuts a notch out of the sun and stripes")]),
]

FONTS = ("https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;600"
         "&family=Montserrat:wght@300;600&display=swap")

def build():
    parts = ['<title>4th Try Tech Style Round C</title>', '<link rel="preconnect" href="https://fonts.googleapis.com">',
             f'<link rel="stylesheet" href="{FONTS}">', f"<style>{CSS}</style>", '<div class="wrap">']
    parts.append('<header class="top"><span class="eyebrow">4th Try Tech &middot; Phase 1.3 &middot; Round C</span>'
                 '<h1>B5 as the base, with the rocket you liked</h1>'
                 '<p>B5&rsquo;s flat 2010s look is the primary theme. Every option uses the rounded rocket from A1 and B1. C1 and C2 are the first pass; '
                 'C4 and C5 are C2 without the long shadow, with two ways to separate the fins from the stripes. C3 (pulp ink lines) was dropped.</p></header>')
    parts.append('<dl class="how"><div><dt>Left</dt><dd>Variation A, circle below the rocket</dd></div>'
                 '<div><dt>Right</dt><dd>Variation B, circle on the rocket body</dd></div>'
                 '<div><dt>New this pass</dt><dd>C4 and C5</dd></div></dl>')
    parts.append('<main class="grid">')
    for s in STYLES:
        sw = "".join(f'<li><i style="background:{h}"></i>{html.escape(n)} <code>{h}</code></li>' for n, h in s.get("sw", SW))
        facts = "".join(f"<dt>{html.escape(k)}</dt><dd>{html.escape(val)}</dd>" for k, val in s["facts"])
        parts.append(
            f'<section class="style" id="{s["tag"].lower()}"><div class="style-head"><h2><span class="tag">{s["tag"]}</span>{html.escape(s["name"])}</h2>'
            f'<p>{html.escape(s["line"])}</p></div>'
            f'<div class="panel" style="background:{s["bg"]}"><div class="pair">'
            f'<figure>{rocket("A", s["mode"])}<figcaption>{s["tag"]} &middot; A</figcaption></figure>'
            f'<figure>{rocket("B", s["mode"])}<figcaption>{s["tag"]} &middot; B</figcaption></figure></div>'
            f'<div class="wordmark" style="font-family:Montserrat,sans-serif;{s["wm"]}">4TH TRY TECH</div></div>'
            f'<div class="meta"><ul class="swatches">{sw}</ul><dl class="facts">{facts}</dl></div></section>')
    parts.append("</main>")
    parts.append('<footer>Colors and type are still B5&rsquo;s placeholders; they get tuned in steps 1.4 and 1.5 once the style is chosen.</footer></div>')
    open(OUT, "w").write("\n".join(parts))
    print("wrote", OUT, sum(len(x) for x in parts), "bytes")

if __name__ == "__main__":
    build()
