#!/usr/bin/env python3
"""Plan steps 3.1 and 3.2: standalone brand elements and the icon masters.

Writes SVGs to out/elements/ and out/icons/. Plain Python, no dependencies.
PNG and ICO files are made from these by export_icons.py.
Text-based elements (wordmark, tagline lockup) are not built here yet: they need
the font files under fonts/ so the lettering can be converted to outlines.
"""
import os
from build import BASE_FLAME, BASE_CORE
from build_c import BODY, FIN_L, FIN_R, NOZZLE, CFIN
from build_d import PALETTES
from build_logo import FOUR

L, D = PALETTES[0]["light"], PALETTES[0]["dark"]
MODES = {"light": L, "dark": D}
NS = 'xmlns="http://www.w3.org/2000/svg"'


def head(vb, title, w=None, h=None):
    size = f' width="{w}" height="{h}"' if w else ""
    return f'<svg {NS} viewBox="{vb}"{size} role="img" aria-labelledby="t"><title id="t">{title}</title>'


def rocket_parts(P, badge=True, detail=True, clip="body-clip"):
    """The rocket in its own coordinate space (x 104-296, y 38-446). Same groups as the logo."""
    o = [f'<g id="flame"><path d="{BASE_FLAME}" fill="{P["flame"]}"/>' + (f'<path d="{BASE_CORE}" fill="{P["sun"]}"/>' if detail else "") + "</g>",
         f'<g id="fins"><path d="{FIN_L}" fill="{P["fin"]}"/><path d="{FIN_R}" fill="{P["fin"]}"/></g>',
         f'<path id="nozzle" d="{NOZZLE}" fill="{P["nozzle"]}"/>',
         f'<path id="body" d="{BODY}" fill="{P["body"]}"/>',
         f'<g clip-path="url(#{clip})"><rect id="body-shade" x="200" y="0" width="70" height="340" fill="#000" opacity=".16"/>']
    if detail:
        o.append(f'<g id="bands"><rect x="140" y="110" width="120" height="9" fill="{P["sun"]}"/><rect x="140" y="296" width="120" height="7" fill="{P["sun"]}"/></g>')
    o.append("</g>")
    if detail:
        o.append(f'<path id="center-fin" d="{CFIN}" fill="{P["flame"]}"/>')
    if badge:
        o.append(badge_parts(P))
    return "".join(o)


def badge_parts(P):
    return (f'<g id="badge"><circle id="badge-ring" cx="200" cy="205" r="35" fill="{P["ground"]}" stroke="{P["success"]}" stroke-width="6"/>'
            f'<path id="numeral" d="{FOUR}" fill="none" stroke="{P["success"]}" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"/></g>')


def gap(color, width):
    return (f'<g id="gap" fill="{color}" stroke="{color}" stroke-width="{width}" stroke-linejoin="round">'
            + "".join(f'<path d="{d}"/>' for d in (BODY, FIN_L, FIN_R, NOZZLE, BASE_FLAME)) + "</g>")


def body_clip(cid="body-clip"):
    return f'<clipPath id="{cid}"><path d="{BODY}"/></clipPath>'


# ---------- 3.1 elements ----------

def rocket(P, mode):
    return (head("92 26 216 432", f"4th Try Tech rocket ({mode})", 216, 432) + f"<defs>{body_clip()}</defs>"
            + f'<g id="rocket">{rocket_parts(P)}</g></svg>')


def rocket_mono(color, name):
    sil = "".join(f'<path d="{d}"/>' for d in (BODY, FIN_L, FIN_R, NOZZLE, BASE_FLAME))
    return (head("92 26 216 432", f"4th Try Tech rocket ({name})", 216, 432)
            + f'<defs><mask id="k" maskUnits="userSpaceOnUse" x="92" y="26" width="216" height="432"><rect x="92" y="26" width="216" height="432" fill="#fff"/>'
              f'<circle cx="200" cy="205" r="35" fill="#000"/></mask></defs>'
            + f'<g id="rocket" fill="{color}" mask="url(#k)">{sil}</g>'
            + f'<g id="badge"><circle cx="200" cy="205" r="29" fill="none" stroke="{color}" stroke-width="5"/>'
              f'<path d="{FOUR}" fill="none" stroke="{color}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" transform="translate(200 205) scale(.8) translate(-200 -205)"/></g></svg>')


def badge(P, mode):
    return head("160 165 80 80", f"4th Try Tech numeral badge ({mode})", 80, 80) + badge_parts(P) + "</svg>"


def badge_mono(color, name):
    return (head("160 165 80 80", f"4th Try Tech numeral badge ({name})", 80, 80)
            + f'<g id="badge"><circle cx="200" cy="205" r="35" fill="none" stroke="{color}" stroke-width="6"/>'
              f'<path d="{FOUR}" fill="none" stroke="{color}" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"/></g></svg>')


def sun_stripes(P, mode):
    """The scene behind the rocket: sun disc and three-stripe band, no ring, no rocket."""
    return (head("24 24 464 464", f"4th Try Tech sun and stripes ({mode})", 464, 464)
            + '<defs><clipPath id="disc-clip"><circle cx="256" cy="256" r="232"/></clipPath></defs>'
            + f'<circle id="disc" cx="256" cy="256" r="232" fill="{P["sun"]}"/><g id="stripes" clip-path="url(#disc-clip)">'
            + "".join(f'<rect x="0" y="{300 + i * 18}" width="512" height="18" fill="{c}"/>' for i, c in enumerate([P["flame"], P["fin"], P["body"]]))
            + "</g></svg>")


def stripe_band(P, mode):
    """The three-stripe band on its own, as a rule or section divider. Stretch it sideways freely."""
    return (head("0 0 512 54", f"4th Try Tech stripe band ({mode})", 512, 54).replace("<svg ", '<svg preserveAspectRatio="none" ')
            + '<g id="stripes">' + "".join(f'<rect x="0" y="{i * 18}" width="512" height="18" fill="{c}"/>' for i, c in enumerate([P["flame"], P["fin"], P["body"]])) + "</g></svg>")


def hairline(kind):
    """Hairline scene icons. They use currentColor, so they take the text color of wherever they sit."""
    ln = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"'
    if kind == "star":
        return head("0 0 24 24", "Plus-sign star", 24, 24) + f'<path d="M12 4 V20 M4 12 H20" {ln}/></svg>'
    return (head("0 0 48 32", "Ringed planet", 48, 32)
            + f'<circle cx="24" cy="16" r="9" {ln}/><path d="M10.5 18.7 C20.4 25 33 18.7 38.4 10.6" {ln}/></svg>')


# ---------- 3.2 icon masters ----------

def micro(P):
    """16 to 24 px. The roundel cannot survive here, so this keeps only what reads: sun disc, a wider rocket, a porthole."""
    sx, sy = 1.5, 1.18
    return (head("0 0 512 512", "4th Try Tech icon (micro)", 512, 512)
            + '<defs><clipPath id="c"><circle cx="256" cy="256" r="256"/></clipPath></defs>'
            + f'<circle id="disc" cx="256" cy="256" r="256" fill="{P["sun"]}"/><g id="rocket" clip-path="url(#c)">'
            + f'<g transform="translate(256 262) scale({sx} {sy}) translate(-200 -242)">{gap(P["sun"], 22)}'
            + f'<path d="{BASE_FLAME}" fill="{P["flame"]}"/><path d="{FIN_L}" fill="{P["fin"]}"/><path d="{FIN_R}" fill="{P["fin"]}"/>'
            + f'<path d="{NOZZLE}" fill="{P["nozzle"]}"/><path d="{BODY}" fill="{P["body"]}"/>'
            + f'<ellipse id="porthole" cx="200" cy="190" rx="{30 / sx:.1f}" ry="{30 / sy:.1f}" fill="{P["ground"]}"/></g></g></svg>')


def app_icon(P, mode):
    """Square, full-bleed, for home screens and avatars. Everything that matters sits inside the central 80% circle,
    so it survives the rounded-square, squircle and circle masks that phones and social sites apply."""
    s = 0.9
    return (head("0 0 512 512", f"4th Try Tech app icon ({mode})", 512, 512) + f"<defs>{body_clip()}</defs>"
            + f'<rect id="ground" width="512" height="512" fill="{P["sun"]}"/>'
            + '<g id="stripes">' + "".join(f'<rect x="0" y="{306 + i * 20}" width="512" height="20" fill="{c}"/>' for i, c in enumerate([P["flame"], P["fin"], P["body"]])) + "</g>"
            + f'<g id="rocket" transform="translate(256 262) scale({s}) translate(-200 -242)">{gap(P["sun"], 16)}{rocket_parts(P)}</g></svg>')


def favicon_svg():
    """One SVG favicon: the small roundel, switching to dark-mode colors with the browser theme."""
    from build_logo import full
    s = full(L, "favicon", small=True)
    css = "<style>@media (prefers-color-scheme: dark){" + "".join(
        f'[fill="{L[k]}"]{{fill:{D[k]}}}[stroke="{L[k]}"]{{stroke:{D[k]}}}' for k in ("sun", "body", "fin", "flame", "success", "ground")) + "}</style>"
    return s.replace("<defs>", css + "<defs>", 1)


MANIFEST = """{
  "name": "4th Try Tech",
  "short_name": "4th Try",
  "icons": [
    { "src": "icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ],
  "theme_color": "#46607A",
  "background_color": "#F0E9DC",
  "display": "standalone"
}
"""

ELEMENTS = {"hairline-star.svg": hairline("star"), "hairline-planet.svg": hairline("planet"),
            "rocket-mono-ink.svg": rocket_mono(L["ink"], "one color, ink"), "rocket-mono-reversed.svg": rocket_mono("#FFFFFF", "one color, reversed"),
            "badge-4-mono-ink.svg": badge_mono(L["ink"], "one color, ink"), "badge-4-mono-reversed.svg": badge_mono("#FFFFFF", "one color, reversed")}
for m, P in MODES.items():
    ELEMENTS.update({f"rocket-{m}.svg": rocket(P, m), f"badge-4-{m}.svg": badge(P, m),
                     f"sun-stripes-{m}.svg": sun_stripes(P, m), f"stripe-band-{m}.svg": stripe_band(P, m)})

ICONS = {"favicon.svg": favicon_svg(), "icon-micro.svg": micro(L), "app-icon-light.svg": app_icon(L, "light"), "app-icon-dark.svg": app_icon(D, "dark"),
         "site.webmanifest": MANIFEST}

if __name__ == "__main__":
    for d, files in (("out/elements", ELEMENTS), ("out/icons", ICONS)):
        os.makedirs(d, exist_ok=True)
        for n, s in files.items():
            open(os.path.join(d, n), "w").write(s)
        print(d, sorted(files))
