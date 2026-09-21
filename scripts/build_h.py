#!/usr/bin/env python3
"""Round H (plan step 2.4): full phone-screen compositions, 1170 x 2532, light and dark."""
import os
from build import CSS, BASE_FLAME, BASE_CORE
from build_c import BODY, FIN_L, FIN_R, NOZZLE, CFIN
from build_d import PALETTES
from build_logo import full, FOUR

OUT = "out/round-h-phone.html"
L, D = PALETTES[0]["light"], PALETTES[0]["dark"]
W, H = 1170, 2532
SAFE_TOP, SAFE_BOTTOM = 141, 102
FRED = "Fredoka, 'Trebuchet MS', sans-serif"
NUN = "'Nunito Sans', system-ui, sans-serif"
TAG = "When the 3rd try wasn&#8217;t enough, keep going."

def icons(P, pts):
    ln = f'fill="none" stroke="{P["ink"]}" stroke-width="6" stroke-linecap="round" opacity=".45"'
    o = []
    for kind, x, y, s in pts:
        if kind == "plus":
            o.append(f'<path d="M{x} {y - s} V{y + s} M{x - s} {y} H{x + s}" {ln}/>')
        else:
            o.append(f'<circle cx="{x}" cy="{y}" r="{s}" {ln}/><path d="M{x - s * 1.5} {y + s * .3} C{x - s * .4} {y + s} {x + s} {y + s * .3} {x + s * 1.6} {y - s * .6}" {ln}/>')
    return "".join(o)

OUTLINE = [False]   # True while writing the standalone splash files: lettering becomes shapes, no font needed

def words(P, y, size=124):
    if OUTLINE[0]:
        from textpath import text_path
        d1, _ = text_path("4th Try Tech", "fredoka-600", size, W / 2, y, "middle", tracking=2)
        d2, _ = text_path("When the 3rd try wasn\u2019t enough, keep going.", "nunito-400", 46, W / 2, y + 96, "middle")
        return f'<g id="wordmark"><path d="{d1}" fill="{P["body"]}"/></g><g id="tagline"><path d="{d2}" fill="{P["ink"]}"/></g>'
    return (f'<text x="{W / 2}" y="{y}" text-anchor="middle" font-family="{FRED}" font-weight="600" font-size="{size}" letter-spacing="2" fill="{P["body"]}">4th Try Tech</text>'
            f'<text x="{W / 2}" y="{y + 96}" text-anchor="middle" font-family="{NUN}" font-weight="400" font-size="46" fill="{P["ink"]}">{TAG}</text>')

def guides(P):
    g = f'stroke="{P["ink"]}" stroke-width="3" stroke-dasharray="14 12" opacity=".35"'
    return (f'<g class="guides"><line x1="0" y1="{SAFE_TOP}" x2="{W}" y2="{SAFE_TOP}" {g}/><line x1="0" y1="{H - SAFE_BOTTOM}" x2="{W}" y2="{H - SAFE_BOTTOM}" {g}/>'
            f'<rect x="{W / 2 - 190}" y="36" width="380" height="76" rx="38" fill="{P["ink"]}" opacity=".18"/>'
            f'<rect x="{W / 2 - 210}" y="{H - 52}" width="420" height="16" rx="8" fill="{P["ink"]}" opacity=".3"/></g>')

def h1(P, uid, show_guides=True):
    inner = full(P, "inline")
    inner = inner[inner.index("<defs>"):-len("</svg>")].replace("disc-clip", uid + "dc").replace("body-clip", uid + "bc")
    o = [f'<rect width="{W}" height="{H}" fill="{P["ground"]}"/>']
    o.append(icons(P, [("planet", 210, 470, 34), ("plus", 960, 380, 24), ("plus", 190, 1960, 18), ("plus", 1000, 560, 18), ("plus", 880, 2180, 16), ("planet", 930, 2000, 22)]))
    o.append(f'<g transform="translate(195 600) scale({780 / 512:.5f})">{inner}</g>')
    o.append(words(P, 1640))
    if show_guides: o.append(guides(P))
    return "".join(o)

def h2(P, uid, show_guides=True):
    place = "translate(585 1010) scale(3.3) translate(-200 -242)"
    o = [f'<defs><clipPath id="{uid}bc"><path d="{BODY}"/></clipPath></defs><rect width="{W}" height="{H}" fill="{P["ground"]}"/>']
    o.append(f'<circle cx="585" cy="930" r="500" fill="{P["sun"]}"/>')
    for i, c in enumerate([P["flame"], P["fin"], P["body"]]):
        o.append(f'<rect x="0" y="{1150 + i * 58}" width="{W}" height="58" fill="{c}"/>')
    o.append(icons(P, [("planet", 170, 330, 34), ("plus", 1000, 290, 24), ("plus", 110, 1560, 18), ("plus", 1060, 1600, 20)]))
    o.append(f'<g transform="{place}">')
    o.append(f'<g fill="{P["ground"]}" stroke="{P["ground"]}" stroke-width="14" stroke-linejoin="round">' + "".join(f'<path d="{d}"/>' for d in (BODY, FIN_L, FIN_R, NOZZLE, BASE_FLAME)) + "</g>")
    o.append(f'<path d="{BASE_FLAME}" fill="{P["flame"]}"/><path d="{BASE_CORE}" fill="{P["sun"]}"/><path d="{FIN_L}" fill="{P["fin"]}"/><path d="{FIN_R}" fill="{P["fin"]}"/>'
             f'<path d="{NOZZLE}" fill="{P["nozzle"]}"/><path d="{BODY}" fill="{P["body"]}"/><g clip-path="url(#{uid}bc)"><rect x="200" y="0" width="70" height="340" fill="#000" opacity=".16"/>'
             f'<rect x="140" y="110" width="120" height="9" fill="{P["sun"]}"/><rect x="140" y="296" width="120" height="7" fill="{P["sun"]}"/></g>'
             f'<path d="{CFIN}" fill="{P["flame"]}"/><circle cx="200" cy="205" r="35" fill="{P["ground"]}" stroke="{P["success"]}" stroke-width="6"/>'
             f'<path d="{FOUR}" fill="none" stroke="{P["success"]}" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"/></g>')
    o.append(words(P, 2010))
    if show_guides: o.append(guides(P))
    return "".join(o)

def phone(fn, P, uid, show_guides=True, standalone=False):
    """standalone=True writes a finished file: needs fonttools and ../fonts/, and the text is outlined."""
    size = f' width="{W}" height="{H}"' if standalone else ""
    OUTLINE[0] = standalone
    try:
        body = fn(P, uid, show_guides)
    finally:
        OUTLINE[0] = False
    label = "4th Try Tech. When the 3rd try wasn&#8217;t enough, keep going."
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"{size} role="img" aria-label="{label}">{body}</svg>'

OPTIONS = [
    dict(tag="H1", name="Centered roundel", fn=h1, line="The finished roundel in the middle of a calm screen, wordmark and tagline beneath it. The logo exactly as it appears everywhere else."),
    dict(tag="H2", name="Full-bleed launch", fn=h2, line="The roundel's scene opened up to fill the screen: big sun, stripes edge to edge, a large rocket, no ring. Closer to the G4 liftoff you liked."),
]

EXTRA = """
.phones{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.phones figure{margin:0;display:flex;flex-direction:column;gap:6px}
.phones svg{display:block;width:100%;height:auto;border-radius:22px;border:1px solid var(--line)}
.phones figcaption{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:11px;color:var(--muted);letter-spacing:.06em}
.fontflag{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:12px;color:var(--muted)}
.fontflag.bad{color:#C23B22}
"""

def build():
    fams = ["IBM+Plex+Mono:wght@400;500", "IBM+Plex+Sans:wght@400;600", "Fredoka:wght@600", "Nunito+Sans:wght@400"]
    links = "".join(f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={f}&display=swap">' for f in fams)
    parts = ['<title>4th Try Tech Phone Screen Round H</title>', '<link rel="preconnect" href="https://fonts.googleapis.com">', links,
             f"<style>{CSS}{EXTRA}</style>", '<div class="wrap">']
    parts.append('<header class="top"><span class="eyebrow">4th Try Tech &middot; Phase 2.4 &middot; Round H</span>'
                 '<h1>Two full-screen phone layouts</h1>'
                 '<p>Each is drawn at 1170 &times; 2532 pixels, the 9:19.5 portrait reference, in light and dark. Dashed lines mark the safe area: '
                 'nothing important sits above the top line (status bar and camera cutout) or below the bottom line (home indicator).</p>'
                 '<p class="fontflag" data-font="Fredoka">Checking Fredoka&hellip;</p></header>')
    parts.append('<main class="grid">')
    for i, o in enumerate(OPTIONS, 1):
        parts.append(f'<section class="style"><div class="style-head"><h2><span class="tag">{o["tag"]}</span>{o["name"]}</h2><p>{o["line"]}</p></div>'
                     f'<div class="phones"><figure>{phone(o["fn"], L, f"h{i}l")}<figcaption>{o["tag"]} &middot; LIGHT</figcaption></figure>'
                     f'<figure>{phone(o["fn"], D, f"h{i}d")}<figcaption>{o["tag"]} &middot; DARK</figcaption></figure></div></section>')
    parts.append("</main>")
    parts.append("""<script>
(function(){
  function run(){
    document.querySelectorAll('.fontflag[data-font]').forEach(function(el){
      var want = el.dataset.font.toLowerCase(), ok = false;
      try { document.fonts.forEach(function(f){ if (f.family.replace(/['"]/g, '').toLowerCase() === want && f.status === 'loaded') ok = true; }); } catch (e) {}
      el.textContent = ok ? 'Fredoka loaded: the wordmark is shown correctly.' : 'Fredoka did NOT load here, so the wordmark and tagline are in fallback fonts. Open this page in a regular browser.';
      el.classList.toggle('bad', !ok);
    });
  }
  if (document.fonts && document.fonts.ready) { document.fonts.ready.then(function(){ setTimeout(run, 300); }); setTimeout(run, 4000); } else { run(); }
})();
</script>""")
    parts.append('<footer>The safe-area guides, camera cutout and home bar are drawn only on this review page; the exported files leave them out.</footer></div>')
    open(OUT, "w").write("\n".join(parts))
    os.makedirs("out/phone", exist_ok=True)
    for o in OPTIONS:
        for mode, P in (("light", L), ("dark", D)):
            name = f'phone-{o["tag"].lower()}-{mode}.svg'
            open("out/phone/" + name, "w").write(phone(o["fn"], P, "p", show_guides=False, standalone=True))
    print("wrote", OUT)

if __name__ == "__main__":
    build()
