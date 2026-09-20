#!/usr/bin/env python3
"""Round G (plan step 2.1): simple primary logo options in the locked C5 / D1 / Fredoka system."""
import html
from build import CSS, BASE_FLAME, BASE_CORE
from build_c import BODY, FIN_L, FIN_R, NOZZLE, CFIN, SIL
from build_d import PALETTES

OUT = "out/round-g-logos.html"
L, D = PALETTES[0]["light"], PALETTES[0]["dark"]
FRED = "Fredoka, 'Trebuchet MS', sans-serif"

def rocket(P, uid, halo, badge=None):
    """Rocket in native coordinates (x 104-296, y 38-446). badge: None or the text for a circle on the body."""
    o = [f'<clipPath id="{uid}b"><path d="{BODY}"/></clipPath>']
    o.append(f'<path d="{SIL} {BASE_FLAME}" fill="{halo}" stroke="{halo}" stroke-width="14" stroke-linejoin="round"/>')
    o.append(f'<path d="{BASE_FLAME}" fill="{P["flame"]}"/><path d="{BASE_CORE}" fill="{P["sun"]}"/>'
             f'<path d="{FIN_L}" fill="{P["fin"]}"/><path d="{FIN_R}" fill="{P["fin2"]}"/><path d="{NOZZLE}" fill="{P["nozzle"]}"/>'
             f'<path d="{BODY}" fill="{P["body"]}"/><g clip-path="url(#{uid}b)"><rect x="200" y="0" width="70" height="340" fill="#000" opacity=".16"/>'
             f'<rect x="140" y="110" width="120" height="9" fill="{P["sun"]}"/><rect x="140" y="296" width="120" height="7" fill="{P["sun"]}"/></g>'
             f'<path d="{CFIN}" fill="{P["flame"]}"/>')
    if badge:
        size = 46 if len(badge) == 1 else 28
        o.append(f'<circle cx="200" cy="205" r="34" fill="{P["ground"]}" stroke="{P["success"]}" stroke-width="5"/>'
                 f'<text x="200" y="207" text-anchor="middle" dominant-baseline="central" font-family="{FRED}" font-weight="600" font-size="{size}" fill="{P["success"]}">{badge}</text>')
    else:
        o.append(f'<circle cx="200" cy="192" r="24" fill="{P["sun"]}"/><circle cx="200" cy="192" r="15" fill="{P["ground"]}"/>')
    return "".join(o)

def stripes(P, y, clip):
    cols = [P["flame"], P["fin"], P["body"]]
    return f'<g clip-path="url(#{clip})">' + "".join(f'<rect x="0" y="{y + i * 14}" width="400" height="14" fill="{c}"/>' for i, c in enumerate(cols)) + "</g>"

def g1(P, uid):
    """Roundel: upright rocket with a 4 on the hull, inside a sun disc."""
    return (f'<defs><clipPath id="{uid}c"><circle cx="200" cy="200" r="178"/></clipPath></defs>'
            f'<circle cx="200" cy="200" r="178" fill="{P["sun"]}"/>' + stripes(P, 232, uid + "c") +
            f'<g clip-path="url(#{uid}c)"><g transform="translate(200 214) scale(.84) translate(-200 -242)">{rocket(P, uid, P["sun"], "4")}</g></g>'
            f'<circle cx="200" cy="200" r="184" fill="none" stroke="{P["body"]}" stroke-width="12"/>')

def g2(P, uid):
    """Breakout: angled rocket leaving the ring, 4TH TRY set on the curve."""
    return (f'<defs><clipPath id="{uid}c"><circle cx="190" cy="212" r="160"/></clipPath><path id="{uid}arc" d="M 58 212 A 132 132 0 0 0 322 212"/></defs>'
            f'<circle cx="190" cy="212" r="166" fill="{P["sun"]}" stroke="{P["body"]}" stroke-width="12"/>'
            f'<text font-family="{FRED}" font-weight="600" font-size="40" letter-spacing="3" fill="{P["body"]}"><textPath href="#{uid}arc" startOffset="66%" text-anchor="middle">4TH TRY</textPath></text>'
            f'<g transform="translate(226 172) rotate(40) scale(.74) translate(-200 -242)">{rocket(P, uid, P["ground"])}</g>')

def g3(P, uid):
    """Numeral: a big 4 in the success ring, small rocket launching off the edge."""
    return (f'<circle cx="190" cy="212" r="160" fill="{P["ground"]}" stroke="{P["success"]}" stroke-width="16"/>'
            f'<text x="182" y="222" text-anchor="middle" dominant-baseline="central" font-family="{FRED}" font-weight="600" font-size="270" fill="{P["success"]}">4</text>'
            f'<g transform="translate(316 92) rotate(40) scale(.44) translate(-200 -242)">{rocket(P, uid, P["ground"])}</g>')

def g4(P, uid):
    """Liftoff: upright rocket rising out of the top of the ring, 4th on the hull."""
    return (f'<defs><clipPath id="{uid}c"><circle cx="200" cy="238" r="142"/></clipPath></defs>'
            f'<circle cx="200" cy="238" r="148" fill="{P["sun"]}" stroke="{P["body"]}" stroke-width="12"/>' + stripes(P, 262, uid + "c") +
            f'<g transform="translate(200 206) scale(.86) translate(-200 -242)">{rocket(P, uid, P["ground"], "4th")}</g>')

OPTIONS = [
    dict(tag="G1", name="Roundel", fn=g1, line="Upright rocket with a 4 on the hull, fully inside a sun disc with the stripe band. Self-contained, like a mission patch.",
         facts=[("Says", "4 (numeral only)"), ("Strength", "One closed shape; drops into any square or circle slot"), ("Watch", "The 4 on the hull gets small below about 48 px")]),
    dict(tag="G2", name="Breakout", fn=g2, line="Angled rocket breaking out of the ring, with 4TH TRY set along the curve.",
         facts=[("Says", "4TH TRY (words)"), ("Strength", "The most motion; the name is in the mark itself"), ("Watch", "Curved text disappears at favicon size, so it needs a simplified small version")]),
    dict(tag="G3", name="Numeral", fn=g3, line="A big 4 inside the green success ring, with a small rocket launching off the edge.",
         facts=[("Says", "4 (numeral leads)"), ("Strength", "Reads at any size; the 4 is unmistakable"), ("Watch", "The rocket becomes a supporting detail; most green of the four")]),
    dict(tag="G4", name="Liftoff", fn=g4, line="Upright rocket rising out of the top of the ring, 4th on the hull, stripes behind.",
         facts=[("Says", "4th"), ("Strength", "Closest to the test image you have been judging; rocket stays the hero"), ("Watch", "Taller than it is wide, so it sits less neatly in a circle avatar")]),
]

EXTRA = """
.logo-panel{display:grid;grid-template-columns:1fr 1fr}
.logo-panel figure{margin:0;padding:18px;display:grid;place-items:center}
.logo-panel svg{display:block;width:100%;max-width:280px;height:auto}
.sizes{display:flex;align-items:center;justify-content:center;gap:18px;padding:14px 12px;flex-wrap:wrap;border-top:1px solid rgba(128,128,128,.25)}
.sizes svg{display:block;flex:none}
.sizes span{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:11px;opacity:.7}
.lockup{display:flex;align-items:center;gap:12px;padding:14px 18px;border-top:1px solid rgba(128,128,128,.25)}
.lockup svg{width:52px;height:52px;flex:none;display:block}
.lockup b{font-family:Fredoka,'Trebuchet MS',sans-serif;font-weight:600;font-size:clamp(20px,5vw,28px);letter-spacing:.02em}
.fontflag{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:12px;color:var(--muted)}
.fontflag.bad{color:#C23B22}
"""

def svg(fn, P, uid, px=None, label=""):
    size = f' width="{px}" height="{px}"' if px else ""
    aria = f' role="img" aria-label="{html.escape(label)}"' if label else ' aria-hidden="true"'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 420"{size}{aria}>{fn(P, uid)}</svg>'

def build():
    fams = ["IBM+Plex+Mono:wght@400;500", "IBM+Plex+Sans:wght@400;600", "Fredoka:wght@600"]
    links = "".join(f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={f}&display=swap">' for f in fams)
    parts = ['<title>4th Try Tech Logo Round G</title>', '<link rel="preconnect" href="https://fonts.googleapis.com">', links,
             f"<style>{CSS}{EXTRA}</style>", '<div class="wrap">']
    parts.append('<header class="top"><span class="eyebrow">4th Try Tech &middot; Phase 2.1 &middot; Round G</span>'
                 '<h1>Four ways to build the simple logo</h1>'
                 '<p>Same rocket, palette and typeface in all four. They differ in what the mark says (4, 4th or 4TH TRY), how the circle is used, and whether the rocket or the numeral leads. '
                 'These are rough compositions to choose a direction, not finished drawings.</p>'
                 '<p class="fontflag" data-font="Fredoka">Checking Fredoka&hellip;</p></header>')
    parts.append('<dl class="how"><div><dt>Top</dt><dd>The mark on light and dark</dd></div>'
                 '<div><dt>Middle</dt><dd>Shrunk to 96, 48 and 24 pixels, the favicon test</dd></div>'
                 '<div><dt>Bottom</dt><dd>Beside the wordmark, as a site header</dd></div></dl>')
    parts.append('<main class="grid">')
    for i, o in enumerate(OPTIONS, 1):
        facts = "".join(f"<dt>{html.escape(k)}</dt><dd>{html.escape(v)}</dd>" for k, v in o["facts"])
        sizes = "".join(f'{svg(o["fn"], L, f"g{i}s{px}", px)}<span>{px}</span>' for px in (96, 48, 24))
        parts.append(
            f'<section class="style" id="{o["tag"].lower()}"><div class="style-head"><h2><span class="tag">{o["tag"]}</span>{o["name"]}</h2><p>{html.escape(o["line"])}</p></div>'
            f'<div class="panel"><div class="logo-panel"><figure style="background:{L["ground"]}">{svg(o["fn"], L, f"g{i}l", label=o["name"] + " on light")}</figure>'
            f'<figure style="background:{D["ground"]}">{svg(o["fn"], D, f"g{i}d", label=o["name"] + " on dark")}</figure></div>'
            f'<div class="sizes" style="background:{L["ground"]};color:{L["ink"]}">{sizes}</div>'
            f'<div class="lockup" style="background:{L["ground"]};color:{L["body"]}">{svg(o["fn"], L, f"g{i}k")}<b>4th Try Tech</b></div></div>'
            f'<div class="meta"><dl class="facts">{facts}</dl></div></section>')
    parts.append("</main>")
    parts.append("""<script>
(function(){
  function run(){
    document.querySelectorAll('.fontflag[data-font]').forEach(function(el){
      var want = el.dataset.font.toLowerCase(), ok = false;
      try { document.fonts.forEach(function(f){ if (f.family.replace(/['"]/g, '').toLowerCase() === want && f.status === 'loaded') ok = true; }); } catch (e) {}
      el.textContent = ok ? 'Fredoka loaded: lettering is shown correctly.' : 'Fredoka did NOT load here, so the 4 and the wordmark are in a fallback font. Open this page in a regular browser.';
      el.classList.toggle('bad', !ok);
    });
  }
  if (document.fonts && document.fonts.ready) { document.fonts.ready.then(function(){ setTimeout(run, 300); }); setTimeout(run, 4000); } else { run(); }
})();
</script>""")
    parts.append('<footer>Next after a direction is chosen: redraw it cleanly on a grid (2.2), then compose the full phone screen (2.4).</footer></div>')
    open(OUT, "w").write("\n".join(parts))
    print("wrote", OUT)

if __name__ == "__main__":
    build()
