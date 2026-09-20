#!/usr/bin/env python3
"""Builds the Batch B art-direction review page: space sci-fi by decade, 1970s to 2020s."""
import math, html
from build import geo, svg_open, text, star4, CSS, BASE_BODY, BASE_FIN_L, BASE_FIN_R, BASE_NOZZLE, BASE_FLAME, BASE_CORE

OUT = "out/batch-b-styles.html"

def stars(pts, col, op=.8):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" opacity="{op}"/>' for x, y, r in pts)

def grain(pid, H, strength="1.0 -.40", freq=".8"):
    d = (f'<filter id="{pid}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="{freq}" numOctaves="2" seed="11"/>'
         f'<feColorMatrix type="matrix" values="0 0 0 0 .1  0 0 0 0 .08  0 0 0 0 .1  0 0 0 {strength}"/></filter>')
    return d, f'<rect width="400" height="{H}" filter="url(#{pid})"/>'

# ---------- B1. 1970s ----------
def s70(v):
    g = geo(v); H = g["H"]; p = f"s70{v}"
    OLIVE = "#B7C34A"
    body = "M200 38 C244 92 254 170 246 258 C243 298 234 322 226 332 H174 C166 322 157 298 154 258 C146 170 156 92 200 38 Z"
    finL = "M160 232 C118 256 100 310 104 368 C118 342 138 330 164 322 Z"
    finR = "M240 232 C282 256 300 310 296 368 C282 342 262 330 236 322 Z"
    gd, gr = grain(p + "g", H, ".9 -.38")
    o = [svg_open(H, f"1970s sci-fi style, variation {v}")]
    o.append(f'<defs><linearGradient id="{p}bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1E0F0A"/><stop offset="1" stop-color="#5A2A14"/></linearGradient>'
             f'<linearGradient id="{p}sun" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F8CE5E"/><stop offset="1" stop-color="#E4582A"/></linearGradient>'
             f'<linearGradient id="{p}bd" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#C79A6A"/><stop offset=".3" stop-color="#FFF6E0"/><stop offset=".62" stop-color="#E6C294"/><stop offset="1" stop-color="#8A5A36"/></linearGradient>'
             f'<linearGradient id="{p}fn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EE7A35"/><stop offset="1" stop-color="#A9301C"/></linearGradient>'
             f'<linearGradient id="{p}fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF3C4"/><stop offset=".45" stop-color="#F6B13C"/><stop offset="1" stop-color="#E4582A" stop-opacity="0"/></linearGradient>'
             f'<filter id="{p}bl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>'
             f'<filter id="{p}sf" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2"/></filter>{gd}</defs>')
    o.append(f'<rect width="400" height="{H}" fill="url(#{p}bg)"/>')
    o.append(stars([(44, 60, 1.6), (92, 130, 1.2), (352, 52, 1.8), (330, 200, 1.2), (60, 236, 1.4), (366, 360, 1.4), (30, 400, 1.2)], "#F3E2B8"))
    o.append(f'<circle cx="200" cy="176" r="128" fill="url(#{p}sun)" filter="url(#{p}sf)"/>')
    for i, c in enumerate(["#F3E2B8", "#F6C453", "#EE8A2F", "#D5452B", "#7A2E1A"]):
        o.append(f'<rect x="0" y="{262 + i * 11}" width="400" height="11" fill="{c}"/>')
    o.append(f'<path d="M180 340 C168 392 190 420 200 452 C210 420 232 392 220 340 Z" fill="url(#{p}fl)" filter="url(#{p}bl)"/>')
    o.append(f'<path d="M186 340 C180 380 194 404 200 436 C206 404 220 380 214 340 Z" fill="url(#{p}fl)"/>')
    o.append(f'<path d="{finL}" fill="url(#{p}fn)"/><path d="{finR}" fill="url(#{p}fn)"/>')
    o.append(f'<path d="M176 330 H224 L229 346 H171 Z" fill="#3A1D12"/>')
    o.append(f'<path d="{body}" fill="url(#{p}bd)"/>')
    o.append(f'<path d="M171 120 C166 170 166 230 172 290" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round" opacity=".55" filter="url(#{p}sf)"/>')
    o.append(f'<path d="M163 300 H237" stroke="#8A5A36" stroke-width="2" opacity=".6"/><path d="M168 112 H232" stroke="#D5452B" stroke-width="7"/>')
    if g["window"]:
        o.append(f'<circle cx="200" cy="192" r="23" fill="#D5452B"/><circle cx="200" cy="192" r="16" fill="#2A1710"/>'
                 f'<ellipse cx="194" cy="186" rx="6" ry="4" fill="#FFFFFF" opacity=".55" transform="rotate(-30 194 186)" filter="url(#{p}sf)"/>')
    cx, cy, r = g["cx"], g["cy"], g["r"]
    fam = "'Bowlby One', 'Arial Black', sans-serif"
    if v == "A":
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#2A1710" fill-opacity=".55" stroke="{OLIVE}" stroke-width="12"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="{r - 14}" fill="none" stroke="{OLIVE}" stroke-width="2.5" opacity=".7"/>')
        o.append(text(cx, cy + 3, "4th", 66, OLIVE, fam))
    else:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#2A1710" stroke="{OLIVE}" stroke-width="6"/>')
        o.append(text(cx, cy + 1.5, "4th", 23, OLIVE, fam))
    o.append(gr + "</svg>")
    return "".join(o)

# ---------- B2. 1980s ----------
def s80(v):
    g = geo(v); H = g["H"]; p = f"s80{v}"
    CY, MG, GR = "#22E6FF", "#FF2BD6", "#2CFFB3"
    hz = H - 210
    o = [svg_open(H, f"1980s sci-fi style, variation {v}")]
    o.append(f'<defs><linearGradient id="{p}bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05010F"/><stop offset="1" stop-color="#2A0845"/></linearGradient>'
             f'<linearGradient id="{p}sun" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE14D"/><stop offset="1" stop-color="#FF2B8A"/></linearGradient>'
             f'<linearGradient id="{p}fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF3A6"/><stop offset="1" stop-color="{MG}"/></linearGradient>'
             f'<clipPath id="{p}sc"><rect x="0" y="0" width="400" height="{hz}"/></clipPath>'
             f'<clipPath id="{p}gc"><rect x="0" y="{hz}" width="400" height="{H - hz}"/></clipPath>'
             f'<filter id="{p}gl" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>')
    o.append(f'<rect width="400" height="{H}" fill="url(#{p}bg)"/>')
    o.append(stars([(40, 40, 1.4), (110, 90, 1), (340, 60, 1.6), (364, 170, 1), (60, 190, 1.2), (300, 130, 1)], "#FFFFFF"))
    # striped sun
    o.append(f'<g clip-path="url(#{p}sc)"><circle cx="200" cy="{hz - 40}" r="120" fill="url(#{p}sun)"/>')
    for i in range(6):
        y = hz - 66 + i * 12
        o.append(f'<rect x="60" y="{y}" width="280" height="{2.5 + i * 1.1:.1f}" fill="#160530"/>')
    o.append("</g>")
    # grid floor
    o.append(f'<rect x="0" y="{hz}" width="400" height="{H - hz}" fill="#0D0222"/><g clip-path="url(#{p}gc)" stroke="{MG}" stroke-width="1.4" opacity=".85">')
    for k in range(-10, 11):
        o.append(f'<line x1="{200 + k * 14}" y1="{hz}" x2="{200 + k * 110}" y2="{H}"/>')
    for i in range(1, 9):
        y = hz + (H - hz) * (i / 8) ** 2
        o.append(f'<line x1="0" y1="{y:.1f}" x2="400" y2="{y:.1f}"/>')
    o.append(f'</g><line x1="0" y1="{hz}" x2="400" y2="{hz}" stroke="{CY}" stroke-width="2" filter="url(#{p}gl)"/>')
    sw = 'stroke-width="3" stroke-linejoin="round"'
    o.append(f'<g filter="url(#{p}gl)"><path d="{BASE_FLAME}" fill="url(#{p}fl)"/>'
             f'<path d="{BASE_FIN_L}" fill="#1A0530" stroke="{MG}" {sw}/><path d="{BASE_FIN_R}" fill="#1A0530" stroke="{MG}" {sw}/>'
             f'<path d="{BASE_NOZZLE}" fill="#0B0221" stroke="{CY}" stroke-width="2"/>'
             f'<path d="{BASE_BODY}" fill="#0B0221" stroke="{CY}" {sw}/>'
             f'<path d="M150 182 H250 M150 300 H250" stroke="{CY}" stroke-width="1.5" opacity=".7"/>'
             f'<path d="M166 120 L166 320" stroke="{CY}" stroke-width="1.5" opacity=".5"/>')
    if g["window"]:
        o.append(f'<circle cx="200" cy="230" r="20" fill="#1A0530" stroke="{MG}" stroke-width="3"/><path d="M190 224 A12 12 0 0 1 204 218" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round"/>')
    o.append("</g>")
    cx, cy, r = g["cx"], g["cy"], g["r"]
    fam = "Orbitron, 'Arial Black', sans-serif"
    if v == "A":
        o.append(f'<g filter="url(#{p}gl)"><circle cx="{cx}" cy="{cy}" r="{r + 2}" fill="#0B0221" stroke="{GR}" stroke-width="5"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="{r - 10}" fill="none" stroke="{GR}" stroke-width="1.5" opacity=".8"/>')
        o.append(text(cx, cy + 3, "4th", 60, GR, fam, 800, 'font-style="italic"') + "</g>")
    else:
        o.append(f'<g filter="url(#{p}gl)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="#0B0221" stroke="{GR}" stroke-width="3.5"/>')
        o.append(text(cx, cy + 1.5, "4th", 22, GR, fam, 800, 'font-style="italic"') + "</g>")
    o.append("</svg>")
    return "".join(o)

# ---------- B3. 1990s ----------
def s90(v):
    g = geo(v); H = g["H"]; p = f"s90{v}"
    o = [svg_open(H, f"1990s sci-fi style, variation {v}")]
    o.append(f'<defs><linearGradient id="{p}bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#062A33"/><stop offset=".55" stop-color="#14203F"/><stop offset="1" stop-color="#2E1147"/></linearGradient>'
             f'<linearGradient id="{p}mt" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2B3A44"/><stop offset=".22" stop-color="#9FB4C0"/><stop offset=".38" stop-color="#F2F8FB"/><stop offset=".6" stop-color="#8296A3"/><stop offset="1" stop-color="#1F2A33"/></linearGradient>'
             f'<linearGradient id="{p}pm" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C9A6FF"/><stop offset=".45" stop-color="#7A45C4"/><stop offset="1" stop-color="#2C0F57"/></linearGradient>'
             f'<linearGradient id="{p}bv" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".5" stop-color="#FFFFFF" stop-opacity="0"/><stop offset="1" stop-color="#000000"/></linearGradient>'
             f'<linearGradient id="{p}sc" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C8FFF0"/><stop offset=".45" stop-color="#2EE6A6"/><stop offset="1" stop-color="#075A44"/></linearGradient>'
             f'<radialGradient id="{p}pl" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#B8FFF6"/><stop offset=".4" stop-color="#1FA6A0"/><stop offset="1" stop-color="#05262D"/></radialGradient>'
             f'<radialGradient id="{p}gs" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".3" stop-color="#5FE3D6"/><stop offset="1" stop-color="#083A44"/></radialGradient>'
             f'<radialGradient id="{p}fl" cx="50%" cy="10%" r="90%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".35" stop-color="#D59BFF"/><stop offset="1" stop-color="#7A45C4" stop-opacity="0"/></radialGradient>'
             f'<filter id="{p}bl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter></defs>')
    o.append(f'<rect width="400" height="{H}" fill="url(#{p}bg)"/>')
    o.append(stars([(36, 50, 1.2), (70, 150, 1.6), (120, 60, 1), (300, 40, 1.4), (370, 250, 1.2), (330, 330, 1.6), (40, 330, 1), (84, 420, 1.2), (356, 440, 1)], "#DFF7FF"))
    o.append(f'<ellipse cx="322" cy="126" rx="50" ry="11" fill="none" stroke="#B59BE6" stroke-width="4" opacity=".55" transform="rotate(-24 322 126)"/>'
             f'<circle cx="322" cy="126" r="27" fill="url(#{p}pl)"/>'
             f'<path d="M274.5 143 A50 11 -24 0 0 369.5 109" fill="none" stroke="#D9C8FF" stroke-width="4" opacity=".9"/>')
    o.append(f'<path d="{BASE_FLAME}" fill="url(#{p}fl)" filter="url(#{p}bl)" transform="translate(0 6) scale(1 1.05)"/><path d="{BASE_CORE}" fill="#FFFFFF" opacity=".9"/>')
    for d in (BASE_FIN_L, BASE_FIN_R):
        o.append(f'<path d="{d}" fill="url(#{p}pm)"/><path d="{d}" fill="none" stroke="url(#{p}bv)" stroke-width="2.5" opacity=".7"/>')
    o.append(f'<path d="{BASE_NOZZLE}" fill="#1B242C" stroke="#8296A3" stroke-width="1.5"/>')
    o.append(f'<path d="{BASE_BODY}" fill="url(#{p}mt)"/><path d="{BASE_BODY}" fill="none" stroke="url(#{p}bv)" stroke-width="3.5" opacity=".75"/>')
    for y in (150, 262, 304):
        o.append(f'<path d="M151 {y} H249" stroke="#1F2A33" stroke-width="1.6" opacity=".8"/><path d="M151 {y + 1.8} H249" stroke="#FFFFFF" stroke-width="1" opacity=".5"/>')
    o.append("".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#1F2A33" opacity=".7"/>' for x in (160, 240) for y in (270, 284, 296)))
    if g["window"]:
        o.append(f'<circle cx="200" cy="200" r="25" fill="url(#{p}mt)" stroke="#1F2A33" stroke-width="1.5"/><circle cx="200" cy="200" r="17" fill="url(#{p}gs)" stroke="#0A1A20" stroke-width="2"/>')
    cx, cy, r = g["cx"], g["cy"], g["r"]
    fam = "'Saira Extra Condensed', 'Arial Narrow', sans-serif"
    if v == "A":
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#06181F" fill-opacity=".6" stroke="url(#{p}sc)" stroke-width="13"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="{r + 7}" fill="none" stroke="#03241C" stroke-width="1.5"/><circle cx="{cx}" cy="{cy}" r="{r - 7}" fill="none" stroke="#03241C" stroke-width="1.5"/>')
        o.append(text(cx, cy + 4, "4TH", 90, f"url(#{p}sc)", fam, 800, 'font-style="italic" stroke="#03241C" stroke-width="1.5"'))
    else:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#06181F" stroke="url(#{p}sc)" stroke-width="7"/><circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="none" stroke="#03241C" stroke-width="1.2"/>')
        o.append(text(cx, cy + 2, "4TH", 33, f"url(#{p}sc)", fam, 800, 'font-style="italic"'))
    o.append("</svg>")
    return "".join(o)

# ---------- B4. 2000s ----------
def s00(v):
    g = geo(v); H = g["H"]; p = f"s00{v}"
    o = [svg_open(H, f"2000s sci-fi style, variation {v}")]
    o.append(f'<defs><linearGradient id="{p}bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#B9DAFB"/><stop offset=".55" stop-color="#FFFFFF"/><stop offset="1" stop-color="#D6EAFD"/></linearGradient>'
             f'<linearGradient id="{p}bd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7CCBFF"/><stop offset="1" stop-color="#1259CC"/></linearGradient>'
             f'<linearGradient id="{p}gls" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".85"/><stop offset="1" stop-color="#FFFFFF" stop-opacity=".05"/></linearGradient>'
             f'<linearGradient id="{p}fn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD071"/><stop offset="1" stop-color="#FF7400"/></linearGradient>'
             f'<linearGradient id="{p}gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C9F56F"/><stop offset="1" stop-color="#4C9A12"/></linearGradient>'
             f'<linearGradient id="{p}sv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".5" stop-color="#AEB9C4"/><stop offset="1" stop-color="#E9EEF3"/></linearGradient>'
             f'<radialGradient id="{p}lf"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".25" stop-color="#FFFFFF" stop-opacity=".7"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>'
             f'<clipPath id="{p}b"><path d="{BASE_BODY}"/></clipPath>'
             f'<filter id="{p}sh" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="9" stdDeviation="8" flood-color="#1259CC" flood-opacity=".3"/></filter></defs>')
    o.append(f'<rect width="400" height="{H}" fill="url(#{p}bg)"/>')
    for x, y, r, op in [(60, 110, 34, .5), (340, 300, 44, .45), (78, 380, 22, .5), (330, 60, 16, .5)]:
        o.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" opacity="{op}"/>')
    o.append(f'<g filter="url(#{p}sh)"><path d="{BASE_FLAME}" fill="url(#{p}fn)" stroke="#D96200" stroke-width="1.5"/><path d="{BASE_CORE}" fill="#FFF6C9"/>'
             f'<path d="{BASE_FIN_L}" fill="url(#{p}fn)" stroke="#C25A00" stroke-width="1.8"/><path d="{BASE_FIN_R}" fill="url(#{p}fn)" stroke="#C25A00" stroke-width="1.8"/>'
             f'<path d="{BASE_NOZZLE}" fill="url(#{p}sv)" stroke="#7D8A96" stroke-width="1.5"/>'
             f'<path d="{BASE_BODY}" fill="url(#{p}bd)" stroke="#0E4AA8" stroke-width="2"/></g>')
    o.append(f'<g clip-path="url(#{p}b)"><path d="M150 40 H250 V150 C222 172 178 172 150 150 Z" fill="url(#{p}gls)"/>'
             f'<rect x="150" y="306" width="100" height="24" fill="#FFFFFF" opacity=".14"/></g>')
    o.append(f'<path d="M110 348 C108 318 120 286 146 252" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" opacity=".55"/>'
             f'<path d="M290 348 C292 318 280 286 254 252" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" opacity=".35"/>')
    if g["window"]:
        o.append(f'<circle cx="200" cy="212" r="24" fill="url(#{p}sv)" stroke="#7D8A96" stroke-width="1.5"/><circle cx="200" cy="212" r="16.5" fill="#0E4AA8"/>'
                 f'<path d="M185.5 206 A16 16 0 0 1 214.5 206 C206 212 194 212 185.5 206 Z" fill="#FFFFFF" opacity=".6"/>')
    # lens flare
    o.append(f'<circle cx="258" cy="92" r="70" fill="url(#{p}lf)"/><path d="M178 92 H338 M258 32 V152" stroke="#FFFFFF" stroke-width="1.6" opacity=".9"/>'
             f'<circle cx="304" cy="54" r="9" fill="none" stroke="#FFFFFF" stroke-width="1.5" opacity=".7"/><circle cx="330" cy="32" r="5" fill="#FFFFFF" opacity=".6"/>'
             f'<circle cx="214" cy="128" r="6" fill="none" stroke="#FFFFFF" stroke-width="1.2" opacity=".6"/>')
    cx, cy, r = g["cx"], g["cy"], g["r"]
    fam = "'Varela Round', 'Trebuchet MS', sans-serif"
    if v == "A":
        o.append(f'<g filter="url(#{p}sh)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF" fill-opacity=".7" stroke="url(#{p}gr)" stroke-width="14"/></g>'
                 f'<circle cx="{cx}" cy="{cy}" r="{r + 7}" fill="none" stroke="#3C7F0C" stroke-width="1.5"/><circle cx="{cx}" cy="{cy}" r="{r - 7}" fill="none" stroke="#3C7F0C" stroke-width="1.5"/>'
                 f'<path d="M{cx - 78} {cy - 48} A92 92 0 0 1 {cx + 78} {cy - 48}" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" opacity=".6"/>')
        o.append(text(cx, cy + 3, "4th", 80, f"url(#{p}gr)", fam, 400, 'stroke="#3C7F0C" stroke-width="1.2"'))
    else:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF" stroke="url(#{p}gr)" stroke-width="8"/><circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="none" stroke="#3C7F0C" stroke-width="1.2"/>'
                 f'<path d="M{cx - 29} {cy - 18} A35 35 0 0 1 {cx + 29} {cy - 18}" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity=".7"/>')
        o.append(text(cx, cy + 1.5, "4th", 29, "#4C9A12", fam))
    o.append("</svg>")
    return "".join(o)

# ---------- B5. 2010s ----------
def s10(v):
    g = geo(v); H = g["H"]; p = f"s10{v}"
    BG, SHADE, SLATE, CORAL, SAGE, SAND, INK = "#F0EDE6", "#DCD6C9", "#46607A", "#E07A5F", "#5E9C7E", "#F2CC8F", "#3D405B"
    sil = BASE_BODY + " " + BASE_FIN_L + " " + BASE_FIN_R + " " + BASE_NOZZLE
    o = [svg_open(H, f"2010s sci-fi style, variation {v}")]
    o.append(f'<defs><clipPath id="{p}b"><path d="{BASE_BODY}"/></clipPath></defs><rect width="400" height="{H}" fill="{BG}"/>')
    o.append(f'<g fill="{SHADE}" stroke="{SHADE}" stroke-width="3">' + "".join(f'<path d="{sil}" transform="translate({i} {i})"/>' for i in range(3, 330, 3)) + "</g>")
    ln = f'fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round" opacity=".55"'
    o.append(f'<ellipse cx="200" cy="200" rx="176" ry="54" {ln} transform="rotate(-24 200 200)" stroke-dasharray="2 9"/>'
             f'<circle cx="62" cy="96" r="13" {ln}/><path d="M44 100 C58 108 74 100 82 88" {ln}/>'
             f'<path d="M330 70 V86 M322 78 H338 M70 300 V312 M64 306 H76 M352 236 V246 M347 241 H357" {ln}/>')
    o.append(f'<path d="{BASE_FLAME}" fill="{CORAL}"/><path d="{BASE_CORE}" fill="{SAND}"/>'
             f'<path d="{BASE_FIN_L}" fill="{CORAL}"/><path d="{BASE_FIN_R}" fill="#C9634A"/><path d="{BASE_NOZZLE}" fill="{INK}"/>'
             f'<path d="{BASE_BODY}" fill="{SLATE}"/><g clip-path="url(#{p}b)"><rect x="200" y="0" width="60" height="340" fill="#000" opacity=".14"/>'
             f'<rect x="150" y="290" width="100" height="8" fill="{SAND}"/></g>')
    if g["window"]:
        o.append(f'<circle cx="200" cy="192" r="24" fill="{SAND}"/><circle cx="200" cy="192" r="15" fill="{BG}"/><path d="M200 177 A15 15 0 0 1 200 207 Z" fill="#000" opacity=".1"/>')
    cx, cy, r = g["cx"], g["cy"], g["r"]
    fam = "Montserrat, 'Helvetica Neue', sans-serif"
    if v == "A":
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 3}" fill="{BG}" stroke="{SAGE}" stroke-width="5"/>')
        o.append(text(cx, cy + 3, "4th", 70, SAGE, fam, 300, 'letter-spacing="1"'))
    else:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BG}" stroke="{SAGE}" stroke-width="4"/>')
        o.append(text(cx, cy + 1.5, "4th", 27, SAGE, fam, 600))
    o.append("</svg>")
    return "".join(o)

# ---------- B6. 2020s ----------
def s20(v):
    g = geo(v); H = g["H"]; p = f"s20{v}"
    CORAL, GREEN, INK = "#FF5A3C", "#0B6B4B", "#191522"
    body = "M200 40 C220 52 232 76 232 104 V150 L228 162 V330 H172 V162 L168 150 V104 C168 76 180 52 200 40 Z"
    legL = "M176 292 L104 390 L117 394 L178 324 Z"
    legR = "M224 292 L296 390 L283 394 L222 324 Z"
    gd, gr = grain(p + "g", H, "1.2 -.46", ".9")
    o = [svg_open(H, f"2020s sci-fi style, variation {v}")]
    o.append(f'<defs><linearGradient id="{p}bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2B2250"/><stop offset=".45" stop-color="#9C7BE0"/><stop offset=".75" stop-color="#FF9E86"/><stop offset="1" stop-color="#FFD7A8"/></linearGradient>'
             f'<radialGradient id="{p}orb" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#FFE3B8"/><stop offset="1" stop-color="#FFE3B8" stop-opacity="0"/></radialGradient>'
             f'<linearGradient id="{p}bd" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#CFCBD6"/><stop offset=".35" stop-color="#FFFFFF"/><stop offset="1" stop-color="#A9A3B8"/></linearGradient>'
             f'<linearGradient id="{p}fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".3" stop-color="#FFD36B"/><stop offset=".7" stop-color="{CORAL}"/><stop offset="1" stop-color="{CORAL}" stop-opacity="0"/></linearGradient>'
             f'<clipPath id="{p}b"><path d="{body}"/></clipPath>'
             f'<filter id="{p}bl" x="-60%" y="-30%" width="220%" height="160%"><feGaussianBlur stdDeviation="5"/></filter>{gd}</defs>')
    o.append(f'<rect width="400" height="{H}" fill="url(#{p}bg)"/><circle cx="90" cy="{H - 250}" r="190" fill="url(#{p}orb)" opacity=".8"/>')
    o.append(stars([(48, 50, 1.4), (120, 96, 1), (330, 44, 1.6), (360, 140, 1), (290, 90, 1.2)], "#FFFFFF"))
    o.append(f'<path d="M186 344 C176 388 190 420 200 450 C210 420 224 388 214 344 Z" fill="url(#{p}fl)" filter="url(#{p}bl)"/>'
             f'<path d="M191 344 C187 380 195 402 200 426 C205 402 213 380 209 344 Z" fill="url(#{p}fl)"/>')
    o.append(f'<path d="{legL}" fill="{CORAL}"/><path d="{legR}" fill="#D9462B"/><rect x="96" y="390" width="26" height="6" rx="3" fill="{INK}"/><rect x="278" y="390" width="26" height="6" rx="3" fill="{INK}"/>')
    o.append(f'<path d="M186 328 H214 L218 346 H182 Z" fill="{INK}"/><path d="{body}" fill="url(#{p}bd)"/>')
    o.append(f'<g clip-path="url(#{p}b)"><rect x="160" y="162" width="80" height="20" fill="{INK}"/><rect x="160" y="312" width="80" height="18" fill="{INK}"/></g>')
    for x in (152, 230):
        o.append(f'<rect x="{x}" y="188" width="18" height="13" fill="{INK}"/><path d="M{x + 6} 188 V201 M{x + 12} 188 V201 M{x} 194.5 H{x + 18}" stroke="#8E88A0" stroke-width="1"/>')
    if g["window"]:
        o.append(f'<path d="M188 230 H212 M188 238 H212 M188 246 H204" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    fam = "Unbounded, 'Arial Black', sans-serif"
    if v == "A":
        cx, cy, r = g["cx"], g["cy"], g["r"]
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFF4E4" fill-opacity=".55" stroke="{GREEN}" stroke-width="12"/>')
        o.append(text(cx, cy + 3, "4th", 62, GREEN, fam, 700))
    else:
        cx, cy, r = 200, 106, 24
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFF4E4" stroke="{GREEN}" stroke-width="5.5"/>')
        o.append(text(cx, cy + 1, "4th", 16.5, GREEN, fam, 700))
    o.append(gr + "</svg>")
    return "".join(o)

STYLES = [
    dict(tag="B1", name="1970s", fn=s70, bg="#3A1D12",
         line="Airbrushed paperback cover: a huge sun, a stripe band, soft highlights on a rounded rocket.",
         wm_family="'Bowlby One', sans-serif", wm_style="letter-spacing:.03em;color:#F6C453;font-size:clamp(18px,4.8vw,27px)",
         sw=[("Body", "#E6C294"), ("Fins / flame", "#D5452B"), ("Success", "#B7C34A"), ("Sun", "#F6C453"), ("Ground", "#2A1710")],
         facts=[("Shapes", "Rounded and heavy; no outlines"), ("Texture", "Airbrush gradients, soft glow, grain, rainbow stripes"), ("Type", "Bowlby One, fat rounded display")]),
    dict(tag="B2", name="1980s", fn=s80, bg="#0B0221",
         line="Neon tubes on black: laser-grid floor, striped sunset, chrome lettering.",
         wm_family="Orbitron, sans-serif",
         wm_style="font-weight:800;font-style:italic;letter-spacing:.08em;font-size:clamp(18px,4.8vw,27px);color:#9fdcff;background:linear-gradient(#fff 0%,#7fd0ff 38%,#1b2a6b 52%,#ff8a3c 56%,#ffe29a 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent",
         sw=[("Body", "#22E6FF"), ("Fins / flame", "#FF2BD6"), ("Success", "#2CFFB3"), ("Sun", "#FFE14D"), ("Ground", "#0B0221")],
         facts=[("Shapes", "Glowing outlines over dark fills; perspective grid"), ("Texture", "Neon bloom, banded sun"), ("Type", "Orbitron extra bold italic, chrome gradient")]),
    dict(tag="B3", name="1990s", fn=s90, bg="#0C2230",
         line="Early-CGI sheen: brushed-metal hull with bevels, glassy spheres, teal and purple space.",
         wm_family="'Saira Extra Condensed', sans-serif", wm_style="font-weight:800;font-style:italic;letter-spacing:.12em;color:#9FE8DA;font-size:clamp(24px,6.4vw,36px)",
         sw=[("Body", "#9FB4C0"), ("Fins / flame", "#7A45C4"), ("Success", "#2EE6A6"), ("Teal", "#1FA6A0"), ("Ground", "#14203F")],
         facts=[("Shapes", "Same simple solids, given bevels, panel lines and rivets"), ("Texture", "Metallic gradients, specular highlights"), ("Type", "Saira Extra Condensed, heavy italic caps")]),
    dict(tag="B4", name="2000s", fn=s00, bg="#D6EAFD",
         line="Glossy gel surfaces on cool blue-white, a lens flare off the nose, soft rounded type.",
         wm_family="'Varela Round', sans-serif", wm_style="letter-spacing:.02em;color:#1259CC;font-size:clamp(20px,5.2vw,30px)",
         sw=[("Body", "#1259CC"), ("Fins / flame", "#FF7400"), ("Success", "#4C9A12"), ("Silver", "#AEB9C4"), ("Ground", "#D6EAFD")],
         facts=[("Shapes", "Soft solids with dark outlines one shade deeper"), ("Texture", "Gloss highlights, tinted drop shadows, lens flare"), ("Type", "Varela Round, soft rounded sans")]),
    dict(tag="B5", name="2010s", fn=s10, bg="#F0EDE6",
         line="Flat design with a long diagonal shadow, muted colors and thin line icons.",
         wm_family="Montserrat, sans-serif", wm_style="font-weight:300;letter-spacing:.3em;color:#3D405B;font-size:clamp(16px,4.2vw,24px)",
         sw=[("Body", "#46607A"), ("Fins / flame", "#E07A5F"), ("Success", "#5E9C7E"), ("Sand", "#F2CC8F"), ("Ground", "#F0EDE6")],
         facts=[("Shapes", "Flat solids with a half-tone split; hairline icons"), ("Texture", "None; one long shadow"), ("Type", "Montserrat light, widely spaced")]),
    dict(tag="B6", name="2020s", fn=s20, bg="#2B2250",
         line="Retro-future revival: grainy sunset gradient, bold type, a slim reusable booster on landing legs.",
         wm_family="Unbounded, sans-serif", wm_style="font-weight:700;letter-spacing:.01em;color:#FFE3B8;font-size:clamp(16px,4.3vw,25px)",
         sw=[("Body", "#F5F2EC"), ("Legs / flame", "#FF5A3C"), ("Success", "#0B6B4B"), ("Lilac", "#9C7BE0"), ("Ink", "#191522")],
         facts=[("Shapes", "Real-spaceflight proportions: fairing, grid fins, legs"), ("Texture", "Soft gradients under heavy film grain"), ("Type", "Unbounded bold, wide and rounded")]),
]

FONTS = ("https://fonts.googleapis.com/css2?family=Bowlby+One&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;600"
         "&family=Montserrat:wght@300;600&family=Orbitron:wght@800&family=Saira+Extra+Condensed:wght@800&family=Unbounded:wght@700"
         "&family=Varela+Round&display=swap")

def build():
    parts = ['<title>4th Try Tech Style Round B</title>',
             '<link rel="preconnect" href="https://fonts.googleapis.com">',
             f'<link rel="stylesheet" href="{FONTS}">', f"<style>{CSS}</style>", '<div class="wrap">']
    parts.append('<header class="top"><span class="eyebrow">4th Try Tech &middot; Phase 1.2 &middot; Batch B</span>'
                 '<h1>Space sci-fi, decade by decade</h1>'
                 '<p>The same test layout in the general look of each decade&rsquo;s space art, 1970s to today. '
                 'Each is the era&rsquo;s overall feel, not modeled on any one film, show or game.</p></header>')
    parts.append('<dl class="how"><div><dt>Left</dt><dd>Variation A, circle below the rocket</dd></div>'
                 '<div><dt>Right</dt><dd>Variation B, circle on the rocket body</dd></div>'
                 '<div><dt>Still in play from Batch A</dt><dd>A1 pulp, A2 mid-century, A5 blueprint, A6 pixel</dd></div></dl>')
    parts.append('<main class="grid">')
    for s in STYLES:
        sw = "".join(f'<li><i style="background:{h}"></i>{html.escape(n)} <code>{h}</code></li>' for n, h in s["sw"])
        facts = "".join(f"<dt>{html.escape(k)}</dt><dd>{html.escape(val)}</dd>" for k, val in s["facts"])
        parts.append(
            f'<section class="style" id="{s["tag"].lower()}"><div class="style-head"><h2><span class="tag">{s["tag"]}</span>{html.escape(s["name"])}</h2>'
            f'<p>{html.escape(s["line"])}</p></div>'
            f'<div class="panel" style="background:{s["bg"]}"><div class="pair">'
            f'<figure>{s["fn"]("A")}<figcaption>{s["tag"]} &middot; A</figcaption></figure>'
            f'<figure>{s["fn"]("B")}<figcaption>{s["tag"]} &middot; B</figcaption></figure></div>'
            f'<div class="wordmark" style="font-family:{s["wm_family"]};{s["wm_style"]}">4TH TRY TECH</div></div>'
            f'<div class="meta"><ul class="swatches">{sw}</ul><dl class="facts">{facts}</dl></div></section>')
    parts.append("</main>")
    parts.append('<footer>Colors, fonts and shapes here are exploration only. Reply with the tags you like from either batch, plus anything worth borrowing from the rest.</footer>')
    parts.append("</div>")
    open(OUT, "w").write("\n".join(parts))
    print("wrote", OUT, sum(len(x) for x in parts), "bytes")

if __name__ == "__main__":
    build()
