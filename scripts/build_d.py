#!/usr/bin/env python3
"""Round D (plan step 1.4): palette options on the chosen C5 art direction, light and dark, with WCAG contrast."""
import html
from build import geo, svg_open, text, CSS, BASE_FLAME, BASE_CORE
from build_c import BODY, FIN_L, FIN_R, NOZZLE, CFIN, SIL

OUT = "out/round-d-palettes.html"

def lum(hx):
    hx = hx.lstrip("#")
    out = []
    for i in (0, 2, 4):
        c = int(hx[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4)
    return .2126 * out[0] + .7152 * out[1] + .0722 * out[2]

def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + .05) / (lb + .05)

def rocket(v, P, pid):
    g = geo(v); H = g["H"]; p = f"d{pid}{v}"
    bg = P["ground"]
    o = [svg_open(H, f"Palette {pid}, variation {v}")]
    o.append(f'<defs><clipPath id="{p}b"><path d="{BODY}"/></clipPath></defs><rect width="400" height="{H}" fill="{bg}"/>')
    o.append(f'<circle cx="200" cy="182" r="124" fill="{P["sun"]}"/>')
    for i, c in enumerate([P["sun"], P["flame"], P["fin"], P["body"]]):
        o.append(f'<rect x="0" y="{264 + i * 11}" width="400" height="11" fill="{c}"/>')
    ln = f'fill="none" stroke="{P["ink"]}" stroke-width="2" stroke-linecap="round" opacity=".55"'
    o.append(f'<circle cx="62" cy="96" r="13" {ln}/><path d="M44 100 C58 108 74 100 82 88" {ln}/>'
             f'<path d="M330 70 V86 M322 78 H338 M70 420 V432 M64 426 H76 M352 236 V246 M347 241 H357" {ln}/>')
    o.append(f'<path d="{SIL} {BASE_FLAME}" fill="{bg}" stroke="{bg}" stroke-width="12" stroke-linejoin="round"/>')
    o.append(f'<path d="{BASE_FLAME}" fill="{P["flame"]}"/><path d="{BASE_CORE}" fill="{P["sun"]}"/>'
             f'<path d="{FIN_L}" fill="{P["fin"]}"/><path d="{FIN_R}" fill="{P["fin2"]}"/><path d="{NOZZLE}" fill="{P["nozzle"]}"/>'
             f'<path d="{BODY}" fill="{P["body"]}"/><g clip-path="url(#{p}b)"><rect x="200" y="0" width="70" height="340" fill="#000" opacity=".16"/>'
             f'<rect x="140" y="110" width="120" height="9" fill="{P["sun"]}"/><rect x="140" y="296" width="120" height="7" fill="{P["sun"]}"/></g>')
    o.append(f'<path d="{CFIN}" fill="{P["flame"]}"/>')
    if g["window"]:
        o.append(f'<circle cx="200" cy="192" r="24" fill="{P["sun"]}"/><circle cx="200" cy="192" r="15" fill="{bg}"/><path d="M200 177 A15 15 0 0 1 200 207 Z" fill="#000" opacity=".1"/>')
    cx, cy, r = g["cx"], g["cy"], g["r"]
    fam = "Montserrat, 'Helvetica Neue', sans-serif"
    if v == "A":
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 3}" fill="{bg}" stroke="{P["success"]}" stroke-width="5"/>')
        o.append(text(cx, cy + 3, "4th", 70, P["success"], fam, 300, 'letter-spacing="1"'))
    else:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{bg}" stroke="{P["success"]}" stroke-width="4"/>')
        o.append(text(cx, cy + 1.5, "4th", 27, P["success"], fam, 600))
    o.append("</svg>")
    return "".join(o)

PALETTES = [
    dict(tag="D1", name="Slate and coral", line="C5 exactly as you chose it, with a dark mode added. Muted and calm; the least saturated of the four.",
         light=dict(ground="#F0E9DC", body="#46607A", fin="#C44E33", fin2="#A23C26", flame="#E07A5F", sun="#F2CC8F", success="#4E8A6D", ink="#3D405B", nozzle="#3D405B"),
         dark=dict(ground="#1F2430", body="#7E9CBC", fin="#E0694C", fin2="#C44E33", flame="#F08A6C", sun="#E8C07D", success="#7FC29F", ink="#E6E1D6", nozzle="#3D4558")),
    dict(tag="D2", name="Navy and amber", line="Deeper navy body, amber fins and flame. Higher contrast, more classic aerospace.",
         light=dict(ground="#F4EFE6", body="#1F3A5F", fin="#C4650B", fin2="#A35307", flame="#F2A541", sun="#F7D488", success="#23855A", ink="#1B2A41", nozzle="#1B2A41"),
         dark=dict(ground="#0F1B2D", body="#5C86B8", fin="#F29A38", fin2="#D67F1E", flame="#F7B75C", sun="#F2CB78", success="#4CC38A", ink="#EAE6DC", nozzle="#2A3A55")),
    dict(tag="D3", name="Teal and terracotta", line="Teal body, terracotta fins, olive-green success. Warmest and most 1970s of the four.",
         light=dict(ground="#F3EBDD", body="#2F6F73", fin="#C8553D", fin2="#A4422E", flame="#E58A5A", sun="#F0C987", success="#5F8A1F", ink="#2B3A3A", nozzle="#2B3A3A"),
         dark=dict(ground="#142626", body="#5FA8A6", fin="#E06F55", fin2="#C8553D", flame="#F09A70", sun="#E9C17C", success="#A3CF5A", ink="#EDE7DA", nozzle="#2C4444")),
    dict(tag="D4", name="Plum and gold", line="Plum body, red-orange fins, gold sun, teal-green success. The most distinctive; least like other tech brands.",
         light=dict(ground="#F3EEEA", body="#4A3B6B", fin="#D14B40", fin2="#AE3A31", flame="#EE8A5F", sun="#F4CF7A", success="#2B8A72", ink="#2E2742", nozzle="#2E2742"),
         dark=dict(ground="#1B1628", body="#8E7CC0", fin="#EE6F62", fin2="#D14B40", flame="#F59C78", sun="#EEC66C", success="#5CC7AA", ink="#EEE9F2", nozzle="#392F55")),
]

EXTRA_CSS = """
.panel .wm2{display:flex}
.panel .wm2 div{flex:1 1 0;min-width:0;padding:14px 8px 16px;text-align:center;font-family:Montserrat,sans-serif;font-weight:300;letter-spacing:.22em;font-size:clamp(11px,2.6vw,16px);overflow-wrap:anywhere}
.modes{display:grid;gap:14px;grid-template-columns:1fr}
@media (min-width:520px){.modes{grid-template-columns:1fr 1fr}}
.modes h3{margin:0 0 6px;font-size:12px;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace}
.cr{width:100%;border-collapse:collapse;font-size:13px;font-variant-numeric:tabular-nums}
.cr td{padding:3px 0;border-top:1px solid var(--line)}
.cr td:nth-child(2){text-align:right;padding-right:10px;font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:12px}
.cr td:last-child{text-align:right;width:3.2em;font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:11px;color:var(--muted)}
.cr .ok{color:var(--text)} .cr .no{color:#C23B22}
"""

def grade(r, need):
    return ('<span class="ok">pass</span>' if r >= need else '<span class="no">low</span>')

def contrast_table(P):
    rows = [("Text (ink) on ground", P["ink"], 4.5), ("Success on ground", P["success"], 3.0), ("Body on ground", P["body"], 3.0), ("Fins on ground", P["fin"], 3.0)]
    out = ['<table class="cr"><tbody>']
    for label, col, need in rows:
        r = ratio(col, P["ground"])
        out.append(f"<tr><td>{label}</td><td>{r:.1f}:1</td><td>{grade(r, need)}</td></tr>")
    out.append("</tbody></table>")
    return "".join(out)

def build():
    fonts = ("https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;600&family=Montserrat:wght@300;600&display=swap")
    parts = ['<title>4th Try Tech Palette Round D</title>', '<link rel="preconnect" href="https://fonts.googleapis.com">',
             f'<link rel="stylesheet" href="{fonts}">', f"<style>{CSS}{EXTRA_CSS}</style>", '<div class="wrap">']
    parts.append('<header class="top"><span class="eyebrow">4th Try Tech &middot; Phase 1.4 &middot; Round D</span>'
                 '<h1>Four palettes on the C5 rocket</h1>'
                 '<p>Same artwork, four color sets, each in light and dark mode. The numbers under each are WCAG contrast ratios against the background: '
                 'text needs 4.5:1, shapes and large type need 3:1.</p></header>')
    parts.append('<dl class="how"><div><dt>Left</dt><dd>Light mode, variation A</dd></div>'
                 '<div><dt>Right</dt><dd>Dark mode, variation B</dd></div>'
                 '<div><dt>Fixed rule</dt><dd>Green means success and is used for nothing else</dd></div></dl>')
    parts.append('<main class="grid">')
    for i, s in enumerate(PALETTES, 1):
        L, D = s["light"], s["dark"]
        def sw(P):
            items = [("Body", P["body"]), ("Fins", P["fin"]), ("Flame", P["flame"]), ("Sun", P["sun"]), ("Success", P["success"]), ("Ink", P["ink"]), ("Ground", P["ground"])]
            return '<ul class="swatches">' + "".join(f'<li><i style="background:{h}"></i>{n} <code>{h}</code></li>' for n, h in items) + "</ul>"
        parts.append(
            f'<section class="style" id="{s["tag"].lower()}"><div class="style-head"><h2><span class="tag">{s["tag"]}</span>{html.escape(s["name"])}</h2>'
            f'<p>{html.escape(s["line"])}</p></div>'
            f'<div class="panel" style="background:{D["ground"]}"><div class="pair">'
            f'<figure>{rocket("A", L, f"{i}l")}<figcaption>{s["tag"]} &middot; light</figcaption></figure>'
            f'<figure>{rocket("B", D, f"{i}d")}<figcaption>{s["tag"]} &middot; dark</figcaption></figure></div>'
            f'<div class="wm2"><div style="background:{L["ground"]};color:{L["ink"]}">4TH TRY TECH</div><div style="background:{D["ground"]};color:{D["ink"]}">4TH TRY TECH</div></div></div>'
            f'<div class="modes"><div><h3>Light</h3>{sw(L)}{contrast_table(L)}</div><div><h3>Dark</h3>{sw(D)}{contrast_table(D)}</div></div></section>')
    parts.append("</main>")
    parts.append('<footer>Typeface is still the Montserrat placeholder; step 1.5 tests alternatives once the palette is locked.</footer></div>')
    open(OUT, "w").write("\n".join(parts))
    print("wrote", OUT, sum(len(x) for x in parts), "bytes")
    for s in PALETTES:
        for m in ("light", "dark"):
            P = s[m]
            print(s["tag"], m, {k: round(ratio(P[k], P["ground"]), 1) for k in ("ink", "success", "body", "fin")})

if __name__ == "__main__":
    build()
