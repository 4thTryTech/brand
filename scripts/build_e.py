#!/usr/bin/env python3
"""Round E (plan step 1.5): typeface options on the locked D1 palette."""
import html
from build import CSS
from build_d import rocket, PALETTES

OUT = "out/round-e-type.html"
L, D = PALETTES[0]["light"], PALETTES[0]["dark"]
MONT = "Montserrat, 'Helvetica Neue', sans-serif"

OPTIONS = [
    dict(tag="E1", name="Jost", disp="Jost", gf="Jost:wght@500", dw=500, hw=500, ls=".2em",
         line="Clean 1920s-style geometric sans, the quiet option. Closest to what you have been seeing.",
         facts=[("Character", "Precise, understated, quietly space-age"), ("Risk", "The least distinctive of the six")]),
    dict(tag="E2", name="Syncopate", disp="Syncopate", gf="Syncopate:wght@700", dw=700, hw=700, ls=".12em",
         line="Very wide, flat-sided capitals. Reads as spacecraft hull lettering.",
         facts=[("Character", "Technical, futuristic, wide"), ("Risk", "Capitals only in feel; long headlines get very wide")]),
    dict(tag="E3", name="Righteous", disp="Righteous", gf="Righteous", dw=400, hw=400, ls=".06em",
         line="Rounded deco display face with distinctive cut-in letter shapes. Mid-century signage.",
         facts=[("Character", "Retro, confident, a little playful"), ("Risk", "Strong personality; needs a plain text face beside it")]),
    dict(tag="E4", name="Bowlby One", disp="'Bowlby One'", gf="Bowlby+One", dw=400, hw=400, ls=".03em",
         line="The fat rounded face from the 1970s style you liked. Heavy poster lettering.",
         facts=[("Character", "Bold, warm, 1970s paperback"), ("Risk", "Too heavy for anything but the wordmark and big headlines")]),
    dict(tag="E5", name="Fredoka", disp="Fredoka", gf="Fredoka:wght@600", dw=600, hw=600, ls=".04em",
         line="Soft, fully rounded letters that echo the rounded rocket.",
         facts=[("Character", "Friendly, approachable, personal"), ("Risk", "Can read as less serious for technical writing")]),
    dict(tag="E6", name="Space Mono", disp="'Space Mono'", gf="Space+Mono:wght@700", dw=700, hw=700, ls=".02em",
         line="Bold monospace with quirky retro-computing shapes. A nod to the terminal style you liked.",
         facts=[("Character", "Technical, tinkerer, code-first"), ("Risk", "Monospace headlines take a lot of room")]),
]

EXTRA = """
.spec{display:flex;flex-direction:column}
.lock{display:flex;align-items:center;gap:16px;padding:18px}
  .lock svg{width:72px;height:auto;flex:none;border-radius:6px;display:block}
.lock .wm{display:flex;flex-direction:column;gap:6px;min-width:0;line-height:1.1;overflow-wrap:anywhere}
.lock .wm b{font-weight:inherit;font-size:clamp(20px,5.4vw,34px)}
.lock .wm i{font-style:normal;font-size:clamp(17px,4.4vw,26px);letter-spacing:0;opacity:.85}
.fontflag{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:12px;color:var(--muted)}
.fontflag.bad{color:#C23B22}
.sample{padding:20px 18px 22px;display:flex;flex-direction:column;gap:12px;border-top:1px solid rgba(128,128,128,.25)}
.sample h3{margin:0;font-size:clamp(22px,5vw,30px);line-height:1.15;text-wrap:balance}
.sample p{margin:0;font-size:16px;line-height:1.55;max-width:60ch}
.row{display:flex;flex-wrap:wrap;align-items:center;gap:12px}
.btn{display:inline-block;padding:9px 18px;border-radius:999px;font-size:14px;letter-spacing:.04em;color:#fff}
.badge{width:64px;height:64px;border-radius:50%;display:grid;place-items:center;font-size:22px;flex:none}
.sample code{font-family:"JetBrains Mono",ui-monospace,Menlo,monospace;font-size:13px;padding:3px 8px;border-radius:5px}
"""

def spec(o, P, idx, mode):
    mark = rocket("B", P, f"e{idx}{mode}").replace(MONT, f"{o['disp']}, sans-serif")
    disp, body = o["disp"], "'Source Sans 3'"
    code_bg = "rgba(0,0,0,.07)" if mode == "l" else "rgba(255,255,255,.09)"
    return (f'<div class="spec" style="background:{P["ground"]};color:{P["ink"]}">'
            f'<div class="lock">{mark}<div class="wm" style="font-family:{disp},sans-serif;font-weight:{o["dw"]};letter-spacing:{o["ls"]}"><b>4TH TRY TECH</b><i>4th Try Tech</i></div></div>'
            f'<div class="sample"><h3 style="font-family:{disp},sans-serif;font-weight:{o["hw"]};color:{P["body"]}">When the 3rd try wasn&rsquo;t enough, keep going.</h3>'
            f'<p style="font-family:{body},sans-serif">Notes from a homelab and a day job in infrastructure: what I built, what broke, and what finally worked on the fourth attempt. 0123456789</p>'
            f'<div class="row"><span class="btn" style="font-family:{disp},sans-serif;font-weight:{o["hw"]};background:{P["fin"]}">Read the log</span>'
            f'<span class="badge" style="font-family:{disp},sans-serif;font-weight:{o["hw"]};color:{P["success"]};border:3px solid {P["success"]}">4th</span>'
            f'<code style="background:{code_bg}">$ retry --attempt 4</code></div></div></div>')

def build():
    fams = ["IBM+Plex+Mono:wght@400;500", "IBM+Plex+Sans:wght@400;600", "JetBrains+Mono", "Source+Sans+3:wght@400;600"] + [o["gf"] for o in OPTIONS]
    links = "".join(f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={f}&display=swap">' for f in fams)
    early = ("<script>window.__csp=[];document.addEventListener('securitypolicyviolation',function(e){window.__csp.push(e.violatedDirective+' blocked '+e.blockedURI);});</script>"
             "<style>@import url('https://fonts.googleapis.com/css2?family=Bowlby+One&display=swap');</style>")
    parts = ['<title>4th Try Tech Type Round E</title>', early, '<link rel="preconnect" href="https://fonts.googleapis.com">',
             links, f"<style>{CSS}{EXTRA}</style>", '<div class="wrap">']
    parts.append('<header class="top"><span class="eyebrow">4th Try Tech &middot; Phase 1.5 &middot; Round E</span>'
                 '<h1>Six wordmark typefaces on the D1 palette</h1>'
                 '<p>Second pass: six faces that differ clearly from one another, each shown as the wordmark in capitals and mixed case, a headline, a button and the 4th badge, in light and dark. '
                 'The paragraph face (Source Sans 3) and code face (JetBrains Mono) are the same everywhere, so only the display face changes.</p></header>')
    parts.append('<dl class="how"><div><dt>Judge first</dt><dd>The wordmark next to the rocket</dd></div>'
                 '<div><dt>Check</dt><dd>Each option says below whether its font loaded on your device</dd></div>'
                 '<div><dt>Sample copy</dt><dd>Placeholder; the voice is written in step 1.6</dd></div></dl>')
    parts.append('<p class="fontflag" id="diag">Font diagnostics: checking&hellip;</p>')
    parts.append('<main class="grid">')
    for i, o in enumerate(OPTIONS, 1):
        facts = "".join(f"<dt>{html.escape(k)}</dt><dd>{html.escape(v)}</dd>" for k, v in o["facts"])
        parts.append(f'<section class="style" id="{o["tag"].lower()}"><div class="style-head"><h2><span class="tag">{o["tag"]}</span>{html.escape(o["name"])}</h2>'
                     f'<p>{html.escape(o["line"])}</p></div><div class="panel">{spec(o, L, i, "l")}{spec(o, D, i, "d")}</div>'
                     f'<div class="meta"><dl class="facts">{facts}</dl><span class="fontflag" data-font="{html.escape(o["disp"])}" data-weight="{o["dw"]}">Checking font&hellip;</span></div></section>')
    parts.append("</main>")
    parts.append("""<script>
(function(){
  function run(){
    var sheets = 0, faces = 0, loaded = 0, failed = 0;
    try { for (var k = 0; k < document.styleSheets.length; k++) { var h = document.styleSheets[k].href || ''; if (h.indexOf('fonts.googleapis.com') > -1) sheets++; } } catch (e) {}
    try { document.fonts.forEach(function(f){ faces++; if (f.status === 'loaded') loaded++; if (f.status === 'error') failed++; }); } catch (e) {}
    var d = document.getElementById('diag');
    if (d) d.textContent = 'Font diagnostics: ' + sheets + ' of ' + document.querySelectorAll('link[rel=stylesheet][href*="fonts.googleapis"]').length + ' stylesheets attached, ' + faces + ' font faces registered, ' + loaded + ' loaded, ' + failed + ' failed. ' + ((window.__csp && window.__csp.length) ? 'Blocked by page policy: ' + window.__csp.slice(0, 3).join('; ') : 'No policy blocks reported.');
    document.querySelectorAll('.fontflag[data-font]').forEach(function(el){
      var want = el.dataset.font.replace(/['"]/g, '').toLowerCase(), ok = false;
      try { document.fonts.forEach(function(f){ if (f.family.replace(/['"]/g, '').toLowerCase() === want && f.status === 'loaded') ok = true; }); } catch (e) {}
      el.textContent = ok ? 'Font loaded on this device' : 'Font did NOT load here; you are seeing a fallback';
      el.classList.toggle('bad', !ok);
    });
  }
  if (document.fonts && document.fonts.ready) { document.fonts.ready.then(function(){ setTimeout(run, 300); }); setTimeout(run, 4000); } else { run(); }
})();
</script>""")
    parts.append('<footer>I have not checked these against Canva&rsquo;s font list. Before locking, confirm the chosen families appear in your Canva account.</footer></div>')
    open(OUT, "w").write("\n".join(parts))
    print("wrote", OUT, sum(len(x) for x in parts), "bytes")

if __name__ == "__main__":
    build()
