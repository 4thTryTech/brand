#!/usr/bin/env python3
"""Round F (plan step 1.5): paragraph face beside the locked display face Fredoka, on the D1 palette."""
from build import CSS
from build_d import PALETTES

OUT = "out/round-f-text.html"
L, D = PALETTES[0]["light"], PALETTES[0]["dark"]
OPTIONS = [
    dict(tag="F1", name="Source Sans 3", fam="'Source Sans 3'", gf="Source+Sans+3:wght@400;600",
         line="Neutral and crisp. Lets Fredoka carry the personality while long technical text stays businesslike."),
    dict(tag="F2", name="Nunito Sans", fam="'Nunito Sans'", gf="Nunito+Sans:wght@400;600",
         line="Slightly rounder and warmer, closer to Fredoka's shapes. The whole page feels friendlier."),
]

EXTRA = """
.pairgrid{display:grid;gap:40px 28px;grid-template-columns:1fr}
@media (min-width:860px){.pairgrid{grid-template-columns:1fr 1fr}}
.spec{padding:22px 18px 24px;display:flex;flex-direction:column;gap:14px}
.spec h3{margin:0;font-family:Fredoka,'Trebuchet MS',sans-serif;font-weight:600;font-size:clamp(24px,5.4vw,32px);line-height:1.12;text-wrap:balance}
.spec h4{margin:6px 0 0;font-family:Fredoka,'Trebuchet MS',sans-serif;font-weight:600;font-size:18px}
.spec p,.spec li{margin:0;font-size:16px;line-height:1.6;max-width:62ch}
.spec ul{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:4px}
.spec small{font-size:13px;opacity:.8}
.row{display:flex;flex-wrap:wrap;align-items:center;gap:12px}
.btn{display:inline-block;padding:9px 18px;border-radius:999px;font-family:Fredoka,'Trebuchet MS',sans-serif;font-weight:600;font-size:15px;color:#fff}
.spec code{font-family:"JetBrains Mono",ui-monospace,Menlo,monospace;font-size:13px;padding:3px 8px;border-radius:5px}
.fontflag{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:12px;color:var(--muted)}
.fontflag.bad{color:#C23B22}
"""

def spec(o, P, dark):
    code_bg = "rgba(255,255,255,.09)" if dark else "rgba(0,0,0,.07)"
    f = f"font-family:{o['fam']},system-ui,sans-serif"
    return (f'<div class="spec" style="background:{P["ground"]};color:{P["ink"]}">'
            f'<h3 style="color:{P["body"]}">When the 3rd try wasn&rsquo;t enough, keep going.</h3>'
            f'<p style="{f}">Most of what I know about infrastructure I learned by getting it wrong first. The storage pool that would not import, the alert rule that paged me 400 times in one night, the automation that quietly automated the wrong thing.</p>'
            f'<h4 style="color:{P["body"]}">What you will find here</h4>'
            f'<ul style="{f}"><li>Build logs from the homelab, failures included</li><li>Notes on monitoring, automation and <strong style="font-weight:600">what actually held up</strong></li><li>Small tools, shared as they are</li></ul>'
            f'<p style="{f}"><small>Posted 20 September 2026 &middot; 6 min read &middot; Attempt 4 of 4 &middot; 0123456789</small></p>'
            f'<div class="row"><span class="btn" style="background:{P["fin"]}">Read the log</span><code style="background:{code_bg}">$ retry --attempt 4</code></div></div>')

def build():
    fams = ["IBM+Plex+Mono:wght@400;500", "IBM+Plex+Sans:wght@400;600", "JetBrains+Mono", "Fredoka:wght@600"] + [o["gf"] for o in OPTIONS]
    links = "".join(f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={f}&display=swap">' for f in fams)
    parts = ['<title>4th Try Tech Text Face Round F</title>', '<link rel="preconnect" href="https://fonts.googleapis.com">', links,
             f"<style>{CSS}{EXTRA}</style>", '<div class="wrap">']
    parts.append('<header class="top"><span class="eyebrow">4th Try Tech &middot; Phase 1.5 &middot; Round F</span>'
                 '<h1>Two paragraph faces beside Fredoka</h1>'
                 '<p>Headlines and buttons are Fredoka in both. Only the paragraph, list and caption text changes. '
                 'Open this page in a regular browser: the Claude app&rsquo;s viewer does not load the fonts.</p>'
                 '<p class="fontflag" data-font="Fredoka">Checking Fredoka&hellip;</p></header>')
    parts.append('<main class="pairgrid">')
    for o in OPTIONS:
        parts.append(f'<section class="style"><div class="style-head"><h2><span class="tag">{o["tag"]}</span>{o["name"]}</h2><p>{o["line"]}</p></div>'
                     f'<div class="panel">{spec(o, L, False)}{spec(o, D, True)}</div>'
                     f'<span class="fontflag" data-font="{o["fam"].strip(chr(39))}">Checking font&hellip;</span></section>')
    parts.append("</main>")
    parts.append("""<script>
(function(){
  function run(){
    document.querySelectorAll('.fontflag[data-font]').forEach(function(el){
      var want = el.dataset.font.toLowerCase(), ok = false;
      try { document.fonts.forEach(function(f){ if (f.family.replace(/['"]/g, '').toLowerCase() === want && f.status === 'loaded') ok = true; }); } catch (e) {}
      el.textContent = el.dataset.font + (ok ? ': loaded on this device' : ': did NOT load here; you are seeing a fallback. Open in a regular browser.');
      el.classList.toggle('bad', !ok);
    });
  }
  if (document.fonts && document.fonts.ready) { document.fonts.ready.then(function(){ setTimeout(run, 300); }); setTimeout(run, 4000); } else { run(); }
})();
</script>""")
    parts.append('<footer>Sample copy is placeholder; the brand voice is written in step 1.6.</footer></div>')
    open(OUT, "w").write("\n".join(parts))
    print("wrote", OUT)

if __name__ == "__main__":
    build()
