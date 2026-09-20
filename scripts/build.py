#!/usr/bin/env python3
"""Builds the Batch A art-direction review page: six styles x two test-image variations."""
import math, html, os
os.makedirs("out", exist_ok=True)

OUT = "out/batch-a-styles.html"

# ---------- shared geometry ----------
def geo(v):
    if v == "A":
        return dict(H=700, cx=200, cy=566, r=90, sw=12, fs=78, window=True)
    return dict(H=500, cx=200, cy=205, r=34, sw=7, fs=29, window=False)

def svg_open(H, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 {H}" role="img" '
            f'aria-label="{html.escape(label)}">')

def mirror(d_points):
    """mirror a list of (x,y) around x=200"""
    return [(400 - x, y) for x, y in d_points]

def star4(x, y, s, fill):
    k = s * 0.22
    pts = [(x, y - s), (x + k, y - k), (x + s, y), (x + k, y + k), (x, y + s), (x - k, y + k), (x - s, y), (x - k, y - k)]
    return '<polygon points="' + " ".join(f"{a:.1f},{b:.1f}" for a, b in pts) + f'" fill="{fill}"/>'

def text(x, y, s, size, fill, family, weight=400, extra=""):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{s}</text>')

BASE_BODY = "M200 40 C236 82 250 132 250 182 V330 H150 V182 C150 132 164 82 200 40 Z"
BASE_FIN_L = "M150 236 C118 268 102 312 104 356 L150 326 Z"
BASE_FIN_R = "M250 236 C282 268 298 312 296 356 L250 326 Z"
BASE_NOZZLE = "M172 328 H228 L234 348 H166 Z"
BASE_FLAME = "M176 346 C166 388 188 412 200 446 C212 412 234 388 224 346 Z"
BASE_CORE = "M189 346 C185 372 195 388 200 408 C205 388 215 372 211 346 Z"

# ---------- 1. 1930s pulp ----------
def pulp(v):
    g = geo(v); H = g["H"]; p = f"pulp{v}"
    INK, CREAM, CREAM2, RED, MUST, TEAL, PAPER = "#2B2320", "#EFE3C8", "#E5D4AE", "#C8402B", "#E2A72E", "#1F6F78", "#F7EED9"
    body = "M200 36 C250 90 262 170 250 260 C246 300 236 322 228 332 H172 C164 322 154 300 150 260 C138 170 150 90 200 36 Z"
    finL = "M158 226 C112 248 92 308 96 372 C112 342 134 328 162 320 Z"
    finR = "M242 226 C288 248 308 308 304 372 C288 342 266 328 238 320 Z"
    flame = "176,334 168,374 182,364 178,406 194,390 200,446 206,390 222,406 218,364 232,374 224,334"
    core = "188,334 186,362 194,356 200,400 206,356 214,362 212,334"
    o = [svg_open(H, f"1930s pulp style, variation {v}")]
    o.append(f'<defs><clipPath id="{p}b"><path d="{body}"/></clipPath>'
             f'<filter id="{p}g" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="7"/>'
             f'<feColorMatrix type="matrix" values="0 0 0 0 .17  0 0 0 0 .13  0 0 0 0 .12  0 0 0 1.1 -.42"/></filter></defs>')
    o.append(f'<rect width="400" height="{H}" fill="{CREAM}"/>')
    # sunburst
    rays = []
    for i in range(0, 24, 2):
        a0, a1 = math.radians(i * 15 - 90), math.radians((i + 1) * 15 - 90)
        rays.append(f'<path d="M200 250 L{200 + 900 * math.cos(a0):.0f} {250 + 900 * math.sin(a0):.0f} L{200 + 900 * math.cos(a1):.0f} {250 + 900 * math.sin(a1):.0f} Z" fill="{CREAM2}"/>')
    o.append("".join(rays))
    # planet and stars
    o.append(f'<g stroke="{INK}" stroke-width="2.5"><circle cx="334" cy="120" r="20" fill="{TEAL}"/>'
             f'<ellipse cx="334" cy="120" rx="34" ry="8" fill="none" transform="rotate(-20 334 120)"/></g>')
    for x, y, s in [(58, 84, 11), (84, 300, 7), (330, 262, 9), (46, 196, 5), (356, 400, 6)]:
        o.append(star4(x, y, s, INK))
    # offset ink shadow
    o.append(f'<g transform="translate(7 7)" fill="{INK}" opacity=".28"><path d="{body}"/><path d="{finL}"/><path d="{finR}"/></g>')
    st = f'stroke="{INK}" stroke-width="3" stroke-linejoin="round"'
    o.append(f'<polygon points="{flame}" fill="{MUST}" {st}/><polygon points="{core}" fill="{PAPER}"/>')
    o.append(f'<path d="{finL}" fill="{MUST}" {st}/><path d="{finR}" fill="{MUST}" {st}/>')
    o.append(f'<path d="M172 330 H228 L234 346 H166 Z" fill="{INK}"/>')
    o.append(f'<path d="{body}" fill="{RED}"/>')
    o.append(f'<g clip-path="url(#{p}b)"><rect x="200" y="0" width="100" height="400" fill="#000" opacity=".16"/>'
             f'<rect x="120" y="112" width="160" height="11" fill="{PAPER}"/><rect x="120" y="130" width="160" height="5" fill="{PAPER}"/>'
             f'<rect x="120" y="296" width="160" height="6" fill="{INK}" opacity=".55"/></g>')
    o.append(f'<path d="{body}" fill="none" {st}/>')
    o.append(f'<path d="M197 240 H203 L205 352 H195 Z" fill="{MUST}" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>')
    if g["window"]:
        o.append(f'<circle cx="200" cy="190" r="24" fill="{MUST}" {st}/><circle cx="200" cy="190" r="15" fill="{INK}"/>'
                 f'<path d="M191 184 A11 11 0 0 1 203 179" fill="none" stroke="{PAPER}" stroke-width="3" stroke-linecap="round"/>')
    cx, cy, r = g["cx"], g["cy"], g["r"]
    if v == "A":
        o.append(f'<circle cx="{cx + 6}" cy="{cy + 6}" r="{r + 4}" fill="{INK}" opacity=".28"/>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{PAPER}" stroke="{INK}" stroke-width="18"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{TEAL}" stroke-width="11"/>')
        o.append(text(cx, cy + 2, "4th", 82, TEAL, "Limelight, 'Poiret One', serif"))
    else:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{PAPER}" stroke="{INK}" stroke-width="11"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{TEAL}" stroke-width="6"/>')
        o.append(text(cx, cy + 1, "4th", 29, TEAL, "Limelight, 'Poiret One', serif"))
    o.append(f'<rect width="400" height="{H}" filter="url(#{p}g)"/>')
    o.append("</svg>")
    return "".join(o)

# ---------- 2. Mid-century space age ----------
def midcentury(v):
    g = geo(v); H = g["H"]; p = f"mc{v}"
    BG, TURQ, ORANGE, MUST, CHAR, SAGE, CREAM = "#F3EEE3", "#2FA7A0", "#E4572E", "#E9B949", "#2D3142", "#4F8A5B", "#FBF8F1"
    body = "M200 30 C224 92 234 172 228 252 L222 330 H178 L172 252 C166 172 176 92 200 30 Z"
    legL = "M181 262 C146 290 112 340 104 392 L117 392 C132 352 158 328 183 316 Z"
    legR = "M219 262 C254 290 288 340 296 392 L283 392 C268 352 242 328 217 316 Z"
    flame = "M186 346 C180 384 193 410 200 446 C207 410 220 384 214 346 Z"
    core = "M194 346 C192 370 197 386 200 404 C203 386 208 370 206 346 Z"
    o = [svg_open(H, f"Mid-century space age style, variation {v}")]
    o.append(f'<defs><clipPath id="{p}b"><path d="{body}"/></clipPath></defs>')
    o.append(f'<rect width="400" height="{H}" fill="{BG}"/>')
    # boomerangs
    o.append(f'<path d="M36 140 C70 96 118 96 138 128 C112 116 78 124 58 160 Z" fill="{MUST}" opacity=".75"/>')
    o.append(f'<path d="M372 300 C340 340 296 338 280 308 C304 320 334 312 352 280 Z" fill="{TURQ}" opacity=".35"/>')
    # atomic starbursts
    def burst(x, y, R, col):
        s = []
        for i in range(4):
            a = math.radians(i * 45)
            dx, dy = R * math.cos(a), R * math.sin(a)
            s.append(f'<line x1="{x - dx:.1f}" y1="{y - dy:.1f}" x2="{x + dx:.1f}" y2="{y + dy:.1f}" stroke="{col}" stroke-width="1.8"/>')
            s.append(f'<circle cx="{x + dx:.1f}" cy="{y + dy:.1f}" r="2.6" fill="{col}"/><circle cx="{x - dx:.1f}" cy="{y - dy:.1f}" r="2.6" fill="{col}"/>')
        return "".join(s)
    o.append(burst(318, 96, 24, CHAR)); o.append(burst(70, 258, 15, ORANGE)); o.append(burst(336, 214, 10, CHAR))
    o.append(f'<circle cx="92" cy="70" r="5" fill="{ORANGE}"/><circle cx="350" cy="396" r="4" fill="{CHAR}"/>')
    # rocket fills
    o.append(f'<path d="{flame}" fill="{ORANGE}"/><path d="{core}" fill="{MUST}"/>')
    o.append(f'<path d="{legL}" fill="{ORANGE}"/><path d="{legR}" fill="{ORANGE}"/>')
    o.append(f'<circle cx="110" cy="395" r="7" fill="{CHAR}"/><circle cx="290" cy="395" r="7" fill="{CHAR}"/>')
    o.append(f'<path d="M186 328 H214 L219 346 H181 Z" fill="{CHAR}"/>')
    o.append(f'<path d="{body}" fill="{TURQ}"/>')
    o.append(f'<g clip-path="url(#{p}b)"><rect x="150" y="0" width="100" height="112" fill="{ORANGE}"/>'
             f'<rect x="150" y="112" width="100" height="7" fill="{CREAM}"/>'
             f'<rect x="150" y="286" width="100" height="5" fill="{CHAR}"/><rect x="150" y="297" width="100" height="2.5" fill="{CHAR}"/></g>')
    # misregistered keyline
    o.append(f'<g transform="translate(-4 -3)" fill="none" stroke="{CHAR}" stroke-width="1.8" stroke-linejoin="round">'
             f'<path d="{body}"/><path d="{legL}"/><path d="{legR}"/><path d="{flame}"/></g>')
    if g["window"]:
        o.append(f'<circle cx="200" cy="190" r="19" fill="{CHAR}"/><circle cx="200" cy="190" r="12.5" fill="{CREAM}"/>'
                 f'<circle cx="196" cy="186" r="19" fill="none" stroke="{CHAR}" stroke-width="1.8"/>')
    cx, cy, r = g["cx"], g["cy"], g["r"]
    fam = "Righteous, 'Trebuchet MS', sans-serif"
    if v == "A":
        o.append(f'<circle cx="{cx + 8}" cy="{cy + 7}" r="{r - 8}" fill="{MUST}" opacity=".8"/>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{SAGE}" stroke-width="11"/>')
        o.append(f'<circle cx="{cx - 4}" cy="{cy - 3}" r="{r + 5.5}" fill="none" stroke="{CHAR}" stroke-width="1.8"/>')
        o.append(text(cx, cy + 3, "4th", 80, "#2F5E3A", fam))
    else:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{CREAM}" stroke="{SAGE}" stroke-width="7"/>')
        o.append(f'<circle cx="{cx - 3}" cy="{cy - 2}" r="{r + 3.5}" fill="none" stroke="{CHAR}" stroke-width="1.6"/>')
        o.append(text(cx, cy + 1.5, "4th", 29, "#2F5E3A", fam))
    o.append("</svg>")
    return "".join(o)

# ---------- 3. Ultra modern ----------
def modern(v):
    g = geo(v); H = g["H"]; p = f"um{v}"
    MINT = "#5CFFB1"
    body = "M200 40 C232 86 246 136 246 190 V330 H154 V190 C154 136 168 86 200 40 Z"
    finL = "M154 250 C126 276 106 316 104 360 L154 330"
    finR = "M246 250 C274 276 294 316 296 360 L246 330"
    o = [svg_open(H, f"Ultra modern style, variation {v}")]
    o.append(f'<defs><radialGradient id="{p}bg" cx="50%" cy="38%" r="75%"><stop offset="0" stop-color="#18203A"/><stop offset="1" stop-color="#070912"/></radialGradient>'
             f'<linearGradient id="{p}pr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6FE9FF"/><stop offset="1" stop-color="#7C6BFF"/></linearGradient>'
             f'<linearGradient id="{p}ac" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF8A5C"/><stop offset="1" stop-color="#FF4FD8"/></linearGradient>'
             f'<linearGradient id="{p}fl" gradientUnits="userSpaceOnUse" x1="0" y1="340" x2="0" y2="450"><stop offset="0" stop-color="#FF8A5C"/><stop offset="1" stop-color="#FF4FD8" stop-opacity="0"/></linearGradient>'
             f'<filter id="{p}gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="7"/></filter></defs>')
    o.append(f'<rect width="400" height="{H}" fill="url(#{p}bg)"/>')
    for rx, ry in [(150, 46), (210, 66), (280, 90)]:
        o.append(f'<ellipse cx="200" cy="250" rx="{rx}" ry="{ry}" fill="none" stroke="#FFFFFF" stroke-opacity=".07" stroke-width="1" transform="rotate(-18 200 250)"/>')
    o.append('<circle cx="326" cy="168" r="2" fill="#FFFFFF" opacity=".7"/><circle cx="74" cy="118" r="1.4" fill="#FFFFFF" opacity=".5"/><circle cx="60" cy="330" r="1.6" fill="#FFFFFF" opacity=".5"/>')
    def rocket(w, extra=""):
        s = f'<g fill="none" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {extra}>'
        s += f'<path d="{body}" stroke="url(#{p}pr)"/>'
        s += f'<path d="{finL}" stroke="url(#{p}ac)"/><path d="{finR}" stroke="url(#{p}ac)"/>'
        s += f'<path d="M178 330 L172 344 H228 L222 330" stroke="url(#{p}pr)" stroke-opacity=".6"/>'
        for x, y2 in [(186, 400), (200, 446), (214, 400), (193, 424), (207, 424)]:
            s += f'<line x1="{x}" y1="352" x2="{x}" y2="{y2}" stroke="url(#{p}fl)"/>'
        return s + "</g>"
    o.append(rocket(5, f'filter="url(#{p}gl)" opacity=".75"'))
    o.append(f'<path d="{body}" fill="url(#{p}pr)" opacity=".1"/>')
    o.append(rocket(2.4))
    if g["window"]:
        o.append(f'<circle cx="200" cy="190" r="18" fill="none" stroke="url(#{p}pr)" stroke-width="2"/><circle cx="200" cy="190" r="3" fill="#6FE9FF"/>')
    cx, cy, r = g["cx"], g["cy"], g["r"]
    fam = "Outfit, 'Helvetica Neue', sans-serif"
    if v == "A":
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="none" stroke="{MINT}" stroke-width="5" filter="url(#{p}gl)" opacity=".7"/>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="none" stroke="{MINT}" stroke-width="2.4"/>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r - 8}" fill="none" stroke="{MINT}" stroke-width=".8" stroke-opacity=".5" stroke-dasharray="2 7"/>')
        o.append(text(cx, cy + 2, "4th", 74, MINT, fam, 200, 'letter-spacing="2"'))
    else:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0B1020" stroke="{MINT}" stroke-width="4" filter="url(#{p}gl)" opacity=".7"/>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0B1020" stroke="{MINT}" stroke-width="2"/>')
        o.append(text(cx, cy + 1, "4th", 27, MINT, fam, 300, 'letter-spacing="1"'))
    o.append("</svg>")
    return "".join(o)

# ---------- 4. Simple flat (baseline) ----------
def flat(v):
    g = geo(v); H = g["H"]; p = f"fl{v}"
    BG, PRI, ACC, SUC, NEU, DARK = "#F4F5F7", "#3B5B92", "#F28C28", "#2FBF71", "#E9EDF3", "#2A2F3A"
    o = [svg_open(H, f"Simple flat style, variation {v}")]
    o.append(f'<defs><filter id="{p}s" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="5" stdDeviation="5" flood-color="#000" flood-opacity=".22"/></filter></defs>')
    o.append(f'<rect width="400" height="{H}" fill="{BG}"/>')
    o.append(f'<g filter="url(#{p}s)"><path d="{BASE_FLAME}" fill="{ACC}"/><path d="{BASE_CORE}" fill="{BG}" opacity=".55"/>'
             f'<path d="{BASE_FIN_L}" fill="{ACC}"/><path d="{BASE_FIN_R}" fill="{ACC}"/><path d="{BASE_NOZZLE}" fill="{DARK}"/>'
             f'<path d="{BASE_BODY}" fill="{PRI}"/>')
    if g["window"]:
        o.append(f'<circle cx="200" cy="188" r="27" fill="{DARK}" opacity=".35"/><circle cx="200" cy="188" r="20" fill="{NEU}"/>')
    cx, cy, r = g["cx"], g["cy"], g["r"]
    fam = "Poppins, 'Helvetica Neue', Arial, sans-serif"
    if v == "A":
        o.append("</g>")
        o.append(f'<g filter="url(#{p}s)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{SUC}" stroke-width="12"/>')
        o.append(text(cx, cy + 3, "4th", 76, SUC, fam, 700) + "</g>")
    else:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{NEU}" stroke="{SUC}" stroke-width="7"/>')
        o.append(text(cx, cy + 1.5, "4th", 28, SUC, fam, 700) + "</g>")
    o.append("</svg>")
    return "".join(o)

# ---------- 5. Technical blueprint ----------
def blueprint(v):
    g = geo(v); H = g["H"]; p = f"bp{v}"
    BG, LINE, AMBER, MINT = "#0F3D73", "#E4F0FF", "#FFD166", "#8CF2C0"
    fam = "'Share Tech Mono', 'Courier New', monospace"
    o = [svg_open(H, f"Technical blueprint style, variation {v}")]
    o.append(f'<defs><pattern id="{p}g" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0 H0 V20" fill="none" stroke="#FFFFFF" stroke-opacity=".09" stroke-width="1"/></pattern>'
             f'<pattern id="{p}G" width="100" height="100" patternUnits="userSpaceOnUse"><path d="M100 0 H0 V100" fill="none" stroke="#FFFFFF" stroke-opacity=".16" stroke-width="1"/></pattern>'
             f'<marker id="{p}a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1 L9 5 L0 9" fill="none" stroke="{LINE}" stroke-width="1.4"/></marker></defs>')
    o.append(f'<rect width="400" height="{H}" fill="{BG}"/><rect width="400" height="{H}" fill="url(#{p}g)"/><rect width="400" height="{H}" fill="url(#{p}G)"/>')
    o.append(f'<rect x="10" y="10" width="380" height="{H - 20}" fill="none" stroke="{LINE}" stroke-opacity=".5" stroke-width="1.2"/>')
    def note(x, y, s, anchor="start", col=LINE):
        return f'<text x="{x}" y="{y}" font-family="{fam}" font-size="11" fill="{col}" fill-opacity=".85" text-anchor="{anchor}" letter-spacing="1">{s}</text>'
    o.append(note(22, 30, "4TT-001") + note(22, 44, "REV A  1:1"))
    # centerline
    o.append(f'<line x1="200" y1="22" x2="200" y2="{H - 22}" stroke="{LINE}" stroke-opacity=".45" stroke-width="1" stroke-dasharray="14 4 3 4"/>')
    sw = 'stroke-width="2" stroke-linejoin="round" stroke-linecap="round"'
    o.append(f'<path d="{BASE_FLAME}" fill="none" stroke="{AMBER}" {sw} stroke-dasharray="6 4"/>')
    o.append(f'<path d="{BASE_FIN_L}" fill="{AMBER}" fill-opacity=".08" stroke="{AMBER}" {sw}/><path d="{BASE_FIN_R}" fill="{AMBER}" fill-opacity=".08" stroke="{AMBER}" {sw}/>')
    o.append(f'<path d="{BASE_NOZZLE}" fill="{BG}" stroke="{LINE}" {sw}/>')
    o.append(f'<path d="{BASE_BODY}" fill="{BG}" stroke="none"/><path d="{BASE_BODY}" fill="#FFFFFF" fill-opacity=".05" stroke="{LINE}" {sw}/>')
    o.append(f'<line x1="150" y1="182" x2="250" y2="182" stroke="{LINE}" stroke-opacity=".5" stroke-width="1"/><line x1="150" y1="300" x2="250" y2="300" stroke="{LINE}" stroke-opacity=".5" stroke-width="1"/>')
    if g["window"]:
        o.append(f'<circle cx="200" cy="230" r="20" fill="none" stroke="{LINE}" stroke-width="2"/><circle cx="200" cy="230" r="14" fill="none" stroke="{LINE}" stroke-width="1" stroke-opacity=".6"/>'
                 f'<path d="M172 230 H228 M200 202 V258" stroke="{LINE}" stroke-opacity=".6" stroke-width="1"/>')
    # height dimension (right)
    o.append(f'<path d="M256 40 H352 M256 330 H352" stroke="{LINE}" stroke-opacity=".5" stroke-width="1"/>'
             f'<line x1="344" y1="42" x2="344" y2="328" stroke="{LINE}" stroke-width="1.2" marker-start="url(#{p}a)" marker-end="url(#{p}a)"/>')
    o.append(f'<text transform="translate(362 185) rotate(90)" font-family="{fam}" font-size="11" fill="{LINE}" fill-opacity=".85" text-anchor="middle" letter-spacing="1">BODY 290</text>')
    # leaders (left)
    o.append(f'<path d="M122 300 L70 262 H24" fill="none" stroke="{LINE}" stroke-opacity=".7" stroke-width="1"/><circle cx="122" cy="300" r="2.2" fill="{LINE}"/>' + note(24, 256, "FIN x2", col=AMBER))
    o.append(f'<path d="M188 396 L90 430 H24" fill="none" stroke="{LINE}" stroke-opacity=".7" stroke-width="1"/><circle cx="188" cy="396" r="2.2" fill="{LINE}"/>' + note(24, 424, "EXHAUST", col=AMBER))
    cx, cy, r = g["cx"], g["cy"], g["r"]
    if v == "A":
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 5}" fill="none" stroke="{MINT}" stroke-width="2"/><circle cx="{cx}" cy="{cy}" r="{r - 6}" fill="none" stroke="{MINT}" stroke-width="2"/>')
        o.append(f'<path d="M{cx - r - 22} {cy} H{cx + r + 22}" stroke="{LINE}" stroke-opacity=".35" stroke-width="1" stroke-dasharray="14 4 3 4"/>')
        o.append(text(cx, cy + 2, "4th", 70, MINT, fam))
        y = cy + r + 22
        o.append(f'<path d="M104 {cy + 30} V{y + 6} M296 {cy + 30} V{y + 6}" stroke="{LINE}" stroke-opacity=".5" stroke-width="1"/>'
                 f'<line x1="106" y1="{y}" x2="294" y2="{y}" stroke="{LINE}" stroke-width="1.2" marker-start="url(#{p}a)" marker-end="url(#{p}a)"/>')
        o.append(f'<rect x="150" y="{y - 8}" width="100" height="16" fill="{BG}"/>' + note(200, y + 4, "&#216;192 = FIN SPAN", "middle"))
    else:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 2}" fill="{BG}" stroke="{MINT}" stroke-width="2"/><circle cx="{cx}" cy="{cy}" r="{r - 4}" fill="none" stroke="{MINT}" stroke-width="1.4"/>')
        o.append(text(cx, cy + 1, "4th", 27, MINT, fam))
        y = 470
        o.append(f'<path d="M104 362 V{y + 6} M296 362 V{y + 6}" stroke="{LINE}" stroke-opacity=".5" stroke-width="1"/>'
                 f'<line x1="106" y1="{y}" x2="294" y2="{y}" stroke="{LINE}" stroke-width="1.2" marker-start="url(#{p}a)" marker-end="url(#{p}a)"/>')
        o.append(f'<rect x="158" y="{y - 8}" width="84" height="16" fill="{BG}"/>' + note(200, y + 4, "FIN SPAN 192", "middle"))
    o.append("</svg>")
    return "".join(o)

# ---------- 6. Terminal / pixel ----------
def pixel(v):
    g = geo(v); H = g["H"]; p = f"px{v}"
    BG, BODY, AMBER, GREEN, NOZ, HOT = "#07110A", "#B8F5C4", "#FFB000", "#39FF6A", "#4A6B52", "#FFE9A8"
    PX, X0, Y0 = 8, 200, 40
    cells = {}
    def put(c, r, col): cells[(c, r)] = col
    for r in range(0, 37):
        hw = 6 if r >= 14 else max(1, round(6 * math.sqrt((r + 1) / 14)))
        for c in range(-hw, hw): put(c, r, BODY)
    for r in range(24, 40):
        outer = min(12, 7 + (r - 24) // 2)
        inner = 6 if r <= 36 else 6 + (r - 36) * 2 - 1
        for c in range(inner, outer):
            put(c, r, AMBER); put(-c - 1, r, AMBER)
    for r in (37, 38):
        for c in range(-4, 4): put(c, r, NOZ)
    fl = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]
    for i, hw in enumerate(fl):
        r = 39 + i
        for c in range(-hw, hw): put(c, r, AMBER)
        if i < 6:
            for c in range(-1, 1): put(c, r, HOT)
    if g["window"]:
        for r in range(17, 21):
            for c in range(-2, 2): put(c, r, BG)
        put(-2, 17, GREEN)
    # body shading column
    for r in range(14, 37):
        if (5, r) in cells and cells[(5, r)] == BODY: put(5, r, "#7FCF92")
    # badge ring
    cx, cy = 200, (568 if v == "A" else 208)
    ro, ri = (12.0, 10.4) if v == "A" else (5.7, 4.5)
    ring = {}
    n = int(ro) + 1
    for rr in range(-n, n):
        for cc in range(-n, n):
            d = math.hypot(cc + .5, rr + .5)
            if d <= ro:
                ring[(cc, rr)] = GREEN if d >= ri else (BG if v == "B" else None)
    def runs(cellmap, x0, y0):
        out = []
        rows = {}
        for (c, r), col in cellmap.items():
            if col: rows.setdefault(r, []).append((c, col))
        for r, lst in rows.items():
            lst.sort()
            start, prev, col = lst[0][0], lst[0][0], lst[0][1]
            for c, k in lst[1:] + [(None, None)]:
                if c is not None and c == prev + 1 and k == col:
                    prev = c; continue
                out.append(f'<rect x="{x0 + start * PX}" y="{y0 + r * PX}" width="{(prev - start + 1) * PX}" height="{PX}" fill="{col}"/>')
                if c is not None: start, prev, col = c, c, k
        return "".join(out)
    o = [svg_open(H, f"Terminal pixel style, variation {v}")]
    o.append(f'<defs><pattern id="{p}s" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="2" fill="#000" opacity=".28"/></pattern>'
             f'<filter id="{p}gl" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
             f'<radialGradient id="{p}v" cx="50%" cy="45%" r="75%"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient></defs>')
    o.append(f'<rect width="400" height="{H}" fill="{BG}"/>')
    tf = "VT323, 'Courier New', monospace"
    o.append(f'<g font-family="{tf}" font-size="19" fill="{GREEN}" filter="url(#{p}gl)"><text x="18" y="32">&gt; launch --try 4</text>'
             f'<text x="18" y="52" fill="{AMBER}">try 1..3 [FAIL]</text><text x="18" y="72">try 4    [ OK ]</text></g>')
    for x, y in [(328, 120), (344, 264), (52, 196), (72, 380), (312, 396)]:
        o.append(f'<rect x="{x}" y="{y}" width="4" height="4" fill="{BODY}" opacity=".7"/>')
    o.append(f'<g shape-rendering="crispEdges" filter="url(#{p}gl)">' + runs(cells, X0, Y0) + runs(ring, cx, cy) + "</g>")
    pf = "'Press Start 2P', 'Courier New', monospace"
    if v == "A":
        o.append(f'<g filter="url(#{p}gl)">' + text(cx + 3, cy + 3, "4th", 42, GREEN, pf) + "</g>")
    else:
        o.append(text(cx + 1, cy + 1, "4th", 17, GREEN, pf))
    o.append(f'<rect width="400" height="{H}" fill="url(#{p}s)"/><rect width="400" height="{H}" fill="url(#{p}v)"/>')
    o.append("</svg>")
    return "".join(o)

# ---------- page ----------
STYLES = [
    dict(tag="A1", name="1930s pulp sci-fi", fn=pulp, bg="#EFE3C8", ink="#2B2320",
         line="Raygun-era adventure: a fat torpedo rocket, heavy ink outlines, printed on rough paper.",
         wm_family="Limelight, serif", wm_style="letter-spacing:.08em;color:#C8402B;font-size:clamp(20px,5.2vw,30px)",
         sw=[("Body", "#C8402B"), ("Fins / flame", "#E2A72E"), ("Success", "#1F6F78"), ("Ink", "#2B2320"), ("Paper", "#EFE3C8")],
         facts=[("Shapes", "Bulbous, swept, exaggerated; thick black keylines"), ("Texture", "Paper grain, sunburst rays, offset ink shadow"), ("Type", "Limelight, an art-deco display face")]),
    dict(tag="A2", name="Mid-century space age", fn=midcentury, bg="#F3EEE3", ink="#2D3142",
         line="Atomic-era optimism: a needle rocket on tripod legs, starbursts, slightly misaligned print.",
         wm_family="Righteous, sans-serif", wm_style="letter-spacing:.06em;color:#2D3142;font-size:clamp(20px,5.2vw,30px)",
         sw=[("Body", "#2FA7A0"), ("Fins / flame", "#E4572E"), ("Success", "#4F8A5B"), ("Charcoal", "#2D3142"), ("Mustard", "#E9B949")],
         facts=[("Shapes", "Slender, tapered, playful; boomerangs and atom bursts"), ("Texture", "Flat ink with keylines printed off-register"), ("Type", "Righteous, rounded geometric display")]),
    dict(tag="A3", name="Ultra modern", fn=modern, bg="#0A0D18", ink="#E8ECFF",
         line="Thin luminous line work on deep space; gradients and glow do the talking.",
         wm_family="Outfit, sans-serif", wm_style="font-weight:200;letter-spacing:.34em;color:#E8ECFF;font-size:clamp(17px,4.4vw,25px)",
         sw=[("Body", "#6FE9FF"), ("Body end", "#7C6BFF"), ("Fins / flame", "#FF4FD8"), ("Success", "#5CFFB1"), ("Ground", "#070912")],
         facts=[("Shapes", "Outlines only, hairline weight, lots of empty space"), ("Texture", "Gradient strokes with soft glow; no fills"), ("Type", "Outfit at its lightest weight, widely spaced")]),
    dict(tag="A4", name="Simple flat (baseline)", fn=flat, bg="#F4F5F7", ink="#2A2F3A",
         line="Your approved test image as-is: solid shapes, slight drop shadow, nothing extra.",
         wm_family="Poppins, sans-serif", wm_style="font-weight:700;letter-spacing:.02em;color:#3B5B92;font-size:clamp(20px,5.2vw,30px)",
         sw=[("Body", "#3B5B92"), ("Fins / flame", "#F28C28"), ("Success", "#2FBF71"), ("Dark", "#2A2F3A"), ("Ground", "#F4F5F7")],
         facts=[("Shapes", "Clean geometric solids, no outlines"), ("Texture", "None; one soft drop shadow"), ("Type", "Poppins bold, friendly geometric sans")]),
    dict(tag="A5", name="Technical blueprint", fn=blueprint, bg="#0F3D73", ink="#E4F0FF",
         line="The rocket as an engineering drawing: grid, centerline, dimensions and callouts.",
         wm_family="'Share Tech Mono', monospace", wm_style="letter-spacing:.22em;color:#E4F0FF;font-size:clamp(17px,4.4vw,25px)",
         sw=[("Body line", "#E4F0FF"), ("Fins / flame", "#FFD166"), ("Success", "#8CF2C0"), ("Sheet", "#0F3D73"), ("Grid", "#2A5590")],
         facts=[("Shapes", "Line drawing only; dashed hidden lines, arrows"), ("Texture", "Drafting grid and sheet border"), ("Type", "Share Tech Mono, all caps annotations")]),
    dict(tag="A6", name="Terminal / pixel", fn=pixel, bg="#07110A", ink="#B8F5C4",
         line="8-pixel blocks on a phosphor screen, with the four tries told as console output.",
         wm_family="'Press Start 2P', monospace", wm_style="letter-spacing:.04em;color:#39FF6A;font-size:clamp(12px,3.3vw,18px);line-height:1.6",
         sw=[("Body", "#B8F5C4"), ("Fins / flame", "#FFB000"), ("Success", "#39FF6A"), ("Shade", "#4A6B52"), ("Screen", "#07110A")],
         facts=[("Shapes", "Everything snapped to an 8-pixel grid"), ("Texture", "Scanlines, phosphor glow, screen vignette"), ("Type", "Press Start 2P for the mark, VT323 for console text")]),
]

CSS = """
:root{
  --bg:#F1F2F6; --surface:#FFFFFF; --text:#1A1D2B; --muted:#5A607A; --line:#D7DAE6; --accent:#3646C4; --chip:#E6E8F2;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){ --bg:#11131B; --surface:#191C28; --text:#E9EBF5; --muted:#9BA1BA; --line:#2B2F40; --accent:#93A0FF; --chip:#232738; }
}
:root[data-theme="dark"]{ --bg:#11131B; --surface:#191C28; --text:#E9EBF5; --muted:#9BA1BA; --line:#2B2F40; --accent:#93A0FF; --chip:#232738; }
*{box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;font-size:15px;line-height:1.5;padding-inline:16px;padding-block:28px 56px}
.wrap{max-width:1120px;margin-inline:auto;display:flex;flex-direction:column;gap:32px}
header.top{display:flex;flex-direction:column;gap:10px;max-width:68ch}
.eyebrow{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
h1{font-size:clamp(26px,5vw,38px);line-height:1.12;margin:0;font-weight:600;letter-spacing:-.01em;text-wrap:balance}
header.top p{margin:0;color:var(--muted)}
.how{display:grid;gap:6px 20px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding-block:14px;margin:0}
.how div{display:flex;gap:10px;align-items:baseline}
.how dt{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:12px;color:var(--accent);white-space:nowrap}
.how dd{margin:0;color:var(--text)}
.grid{display:grid;gap:40px 28px;grid-template-columns:1fr}
@media (min-width:860px){.grid{grid-template-columns:1fr 1fr}}
.style{display:flex;flex-direction:column;gap:14px;min-width:0}
.style-head{display:flex;flex-direction:column;gap:4px}
.style-head h2{margin:0;font-size:20px;font-weight:600;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.tag{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:13px;font-weight:500;color:var(--accent);border:1px solid var(--accent);border-radius:4px;padding:1px 7px}
.style-head p{margin:0;color:var(--muted)}
.panel{border-radius:10px;overflow:hidden;border:1px solid var(--line);display:flex;flex-direction:column}
.pair{display:flex;align-items:flex-end;gap:0}
.pair figure{margin:0;flex:1 1 0;min-width:0;position:relative}
.pair svg{display:block;width:100%;height:auto}
.pair figcaption{position:absolute;left:10px;bottom:8px;font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:11px;letter-spacing:.08em;padding:2px 6px;border-radius:3px;background:rgba(0,0,0,.45);color:#fff}
.wordmark{padding:16px 14px 18px;text-align:center;border-top:1px solid rgba(128,128,128,.25);overflow-wrap:anywhere}
.meta{display:flex;flex-direction:column;gap:12px}
.swatches{display:flex;flex-wrap:wrap;gap:8px;list-style:none;margin:0;padding:0}
.swatches li{display:flex;align-items:center;gap:7px;background:var(--chip);border-radius:999px;padding:3px 10px 3px 4px;font-size:12px}
.swatches i{width:18px;height:18px;border-radius:50%;border:1px solid rgba(128,128,128,.45);display:block;flex:none}
.swatches code{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:11px;color:var(--muted)}
.facts{margin:0;display:grid;grid-template-columns:auto 1fr;gap:4px 14px;font-size:14px}
.facts dt{color:var(--muted)}
.facts dd{margin:0}
footer{border-top:1px solid var(--line);padding-top:16px;color:var(--muted);max-width:68ch;font-size:14px}
"""

FONTS = ("https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;600"
         "&family=Limelight&family=Outfit:wght@200;300&family=Poppins:wght@700&family=Press+Start+2P&family=Righteous"
         "&family=Share+Tech+Mono&family=VT323&display=swap")

def build():
    parts = ['<title>4th Try Tech Style Round A</title>',
             '<link rel="preconnect" href="https://fonts.googleapis.com">',
             f'<link rel="stylesheet" href="{FONTS}">', f"<style>{CSS}</style>", '<div class="wrap">']
    parts.append('<header class="top"><span class="eyebrow">4th Try Tech &middot; Phase 1.2 &middot; Batch A</span>'
                 '<h1>Six art directions, one rocket</h1>'
                 '<p>The same test layout drawn six ways. Each style brings its own rocket shape, palette and typeface. '
                 'None of this is final artwork; it exists so you can react to the overall feel.</p></header>')
    parts.append('<dl class="how"><div><dt>Left</dt><dd>Variation A, circle below the rocket</dd></div>'
                 '<div><dt>Right</dt><dd>Variation B, circle in place of the porthole</dd></div>'
                 '<div><dt>Reply with</dt><dd>Tags you like, plus anything worth stealing from the rest</dd></div></dl>')
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
    parts.append('<footer>Colors, fonts and shapes here are exploration only. Batch B follows with space sci-fi by decade, 1970s to today, on the same layout.</footer>')
    parts.append("</div>")
    open(OUT, "w").write("\n".join(parts))
    print("wrote", OUT, sum(len(p) for p in parts), "bytes")

if __name__ == "__main__":
    build()
