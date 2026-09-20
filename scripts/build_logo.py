#!/usr/bin/env python3
"""Plan step 2.2: clean master drawing of the chosen G1 roundel logo. No fonts needed: the 4 is drawn as a path."""
import os
from build import BASE_FLAME, BASE_CORE
from build_c import BODY, FIN_L, FIN_R, NOZZLE, CFIN, SIL
from build_d import PALETTES

L, D = PALETTES[0]["light"], PALETTES[0]["dark"]
OUTS = ["out/logo"]
FOUR = "M207 225 V185 L185 213 H216"          # numeral 4, drawn with round caps and joins
PLACE = "translate(256 268) scale(1.02) translate(-200 -242)"

def head(title, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512" role="img" aria-labelledby="t d">'
            f'<title id="t">{title}</title><desc id="d">{desc}</desc>')

def full(P, name, small=False):
    o = [head(f"4th Try Tech logo ({name})", "A rounded rocket with a 4 on its hull, launching in front of a sun disc and stripe band, inside a ring.")]
    o.append('<defs><clipPath id="disc-clip"><circle cx="256" cy="256" r="232"/></clipPath><clipPath id="body-clip"><path d="' + BODY + '"/></clipPath></defs>')
    o.append(f'<circle id="disc" cx="256" cy="256" r="232" fill="{P["sun"]}"/>')
    o.append('<g id="stripes" clip-path="url(#disc-clip)">' + "".join(
        f'<rect x="0" y="{300 + i * 18}" width="512" height="18" fill="{c}"/>' for i, c in enumerate([P["flame"], P["fin"], P["body"]])) + "</g>")
    o.append(f'<g id="rocket" clip-path="url(#disc-clip)"><g transform="{PLACE}">')
    o.append(f'<g id="gap" fill="{P["sun"]}" stroke="{P["sun"]}" stroke-width="{18 if small else 14}" stroke-linejoin="round">' + "".join(f'<path d="{d}"/>' for d in (BODY, FIN_L, FIN_R, NOZZLE, BASE_FLAME)) + "</g>")
    o.append(f'<g id="flame"><path d="{BASE_FLAME}" fill="{P["flame"]}"/>' + ("" if small else f'<path d="{BASE_CORE}" fill="{P["sun"]}"/>') + "</g>")
    o.append(f'<g id="fins"><path d="{FIN_L}" fill="{P["fin"]}"/><path d="{FIN_R}" fill="{P["fin"]}"/></g>')
    o.append(f'<path id="nozzle" d="{NOZZLE}" fill="{P["nozzle"]}"/>')
    o.append(f'<path id="body" d="{BODY}" fill="{P["body"]}"/><g clip-path="url(#body-clip)"><rect id="body-shade" x="200" y="0" width="70" height="340" fill="#000" opacity=".16"/>')
    if not small:
        o.append(f'<g id="bands"><rect x="140" y="110" width="120" height="9" fill="{P["sun"]}"/><rect x="140" y="296" width="120" height="7" fill="{P["sun"]}"/></g>')
    o.append("</g>")
    if small:
        o.append(f'<circle id="porthole" cx="200" cy="200" r="30" fill="{P["ground"]}" stroke="{P["success"]}" stroke-width="12"/>')
    else:
        o.append(f'<path id="center-fin" d="{CFIN}" fill="{P["flame"]}"/>')
        o.append(f'<g id="badge"><circle id="badge-ring" cx="200" cy="205" r="35" fill="{P["ground"]}" stroke="{P["success"]}" stroke-width="6"/>'
                 f'<path id="numeral" d="{FOUR}" fill="none" stroke="{P["success"]}" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"/></g>')
    o.append("</g></g>")
    o.append(f'<circle id="ring" cx="256" cy="256" r="240" fill="none" stroke="{P["body"]}" stroke-width="{22 if small else 16}"/></svg>')
    return "".join(o)

def mono(color, name):
    parts = [BODY, FIN_L, FIN_R, NOZZLE, BASE_FLAME]
    sil = "".join(f'<path d="{d}"/>' for d in parts)
    o = [head(f"4th Try Tech logo ({name})", "One-color version of the 4th Try Tech rocket roundel.")]
    o.append('<defs><clipPath id="disc-clip"><circle cx="256" cy="256" r="232"/></clipPath><clipPath id="body-clip"><path d="' + BODY + '"/></clipPath>'
             f'<mask id="knock" maskUnits="userSpaceOnUse" x="0" y="0" width="512" height="512"><rect width="512" height="512" fill="#fff"/>'
             f'<g transform="{PLACE}" fill="#000" stroke="#000" stroke-width="16" stroke-linejoin="round">{sil}</g></mask>'
             f'<mask id="badge-knock" maskUnits="userSpaceOnUse" x="0" y="0" width="512" height="512"><rect width="512" height="512" fill="#fff"/>'
             f'<g transform="{PLACE}" fill="#000"><circle cx="200" cy="205" r="35"/><g clip-path="url(#body-clip)"><rect x="140" y="110" width="120" height="8"/><rect x="140" y="296" width="120" height="7"/></g></g></mask></defs>')
    o.append('<g id="stripes" mask="url(#knock)"><g clip-path="url(#disc-clip)">' + "".join(
        f'<rect x="0" y="{302 + i * 18}" width="512" height="10" fill="{color}"/>' for i in range(3)) + "</g></g>")
    o.append(f'<g id="rocket" mask="url(#badge-knock)"><g transform="{PLACE}" fill="{color}">{sil}</g></g>')
    o.append(f'<g id="badge" transform="{PLACE}"><circle cx="200" cy="205" r="29" fill="none" stroke="{color}" stroke-width="5"/>'
             f'<path d="{FOUR}" fill="none" stroke="{color}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" transform="translate(200 205) scale(.8) translate(-200 -205)"/></g>')
    o.append(f'<circle id="ring" cx="256" cy="256" r="240" fill="none" stroke="{color}" stroke-width="16"/></svg>')
    return "".join(o)

FILES = {
    "logo-roundel-light.svg": full(L, "light"),
    "logo-roundel-dark.svg": full(D, "dark"),
    "logo-roundel-small.svg": full(L, "small sizes", small=True),
    "logo-roundel-mono-ink.svg": mono(L["ink"], "one color, ink"),
    "logo-roundel-mono-reversed.svg": mono("#FFFFFF", "one color, reversed"),
}

if __name__ == "__main__":
    for d in OUTS:
        os.makedirs(d, exist_ok=True)
        for n, s in FILES.items():
            open(os.path.join(d, n), "w").write(s)
    # contact sheet for a visual check
    cells = []
    for n, s in FILES.items():
        bg = D["ground"] if ("dark" in n or "reversed" in n) else L["ground"]
        inner = s.replace('width="512" height="512"', "")
        sizes = "".join(f'<div style="width:{px}px">{inner}</div>' for px in (220, 64, 32, 16))
        cells.append(f'<div style="background:{bg};padding:16px;display:flex;gap:16px;align-items:flex-end;color:#888;font:12px monospace">{sizes}<span>{n}</span></div>')
    open("out/logo/sheet.html", "w").write("<!doctype html><meta charset=utf-8><body style='margin:0;display:grid;gap:4px'>" + "".join(cells))
    print("wrote", list(FILES))
