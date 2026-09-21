#!/usr/bin/env python3
"""Plan step 5.1: animation storyboard. Five live SVG + CSS sketches of the four-tries story, to choose from.
Writes out/storyboard.html (page content only; the publisher adds the html skeleton). No dependencies.
"""
import os
from build import BASE_FLAME, BASE_CORE
from build_c import BODY, FIN_L, FIN_R, NOZZLE, CFIN
from build_d import PALETTES
from build_logo import FOUR, PLACE

P = PALETTES[0]["light"]
NUM = {1: "M-5 -9 L2 -15 V15", 2: "M-8 -8 C-8 -19 9 -19 8 -7 C8 1 -8 5 -8 15 H9", 3: "M-8 -12 C-3 -18 9 -16 8 -8 C8 -2 2 0 -2 0 C4 0 10 3 9 9 C8 17 -3 19 -9 12",
       4: "M7 20 V-20 L-15 8 H16"}
XS, NY, R = [140, 260, 380, 500], 196, 26
STEP = 120


def arcs():
    """One path through all four hops, each hop an arc of equal length, starting one step to the left of node 1."""
    d = f"M{XS[0] - STEP} {NY - R}"
    for x in XS:
        d += f" Q{x - STEP / 2} {NY - R - 92} {x} {NY - R}"
    return d


def seg(i):
    x = XS[i]
    return f"M{x - STEP} {NY - R} Q{x - STEP / 2} {NY - R - 92} {x} {NY - R}"


def node(i, x):
    n = i + 1
    t0 = 0.4 + i * 0.8                      # this try starts
    land = t0 + 0.55
    num = f'<path d="{NUM[n]}" fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" transform="scale(.62)"/>'
    if n < 4:
        retry = (f'<g class="retry" style="--d:{land}s"><path d="M0 -36 A36 36 0 1 1 -31 -18" fill="none" stroke="{P["flame"]}" stroke-width="4" stroke-linecap="round"/>'
                 f'<path d="M-40 -24 L-31 -18 L-27 -29" fill="none" stroke="{P["flame"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>')
        return (f'<g transform="translate({x} {NY})"><g class="node fail" style="--d:{land}s;--out:3.5s" stroke="{P["ink"]}">'
                f'<circle r="{R}" fill="{P["ground"]}" stroke-width="3"/>{num}</g>{retry}</g>')
    return (f'<g transform="translate({x} {NY})"><g class="tobadge"><g class="node win" style="--d:{land}s" stroke="{P["ink"]}">'
            f'<circle r="{R}" fill="{P["ground"]}" stroke-width="4.7"/>{num}</g></g></g>')


def roundel(with_badge=False, extra=""):
    """The finished logo, in animatable parts, nested at 240 px in the middle of the 640 x 300 stage."""
    o = [f'<svg x="200" y="30" width="240" height="240" viewBox="0 0 512 512" overflow="visible"><defs><clipPath id="DC"><circle cx="256" cy="256" r="232"/></clipPath><clipPath id="BC"><path d="{BODY}"/></clipPath></defs>',
         f'<circle class="disc" cx="256" cy="256" r="232" fill="{P["sun"]}"/><g clip-path="url(#DC)"><g class="stripes">']
    o += [f'<rect x="0" y="{300 + i * 18}" width="512" height="18" fill="{c}"/>' for i, c in enumerate([P["flame"], P["fin"], P["body"]])]
    o.append(f'</g><g class="rise"><g transform="{PLACE}">'
             f'<g fill="{P["sun"]}" stroke="{P["sun"]}" stroke-width="14" stroke-linejoin="round">' + "".join(f'<path d="{d}"/>' for d in (BODY, FIN_L, FIN_R, NOZZLE)) + "</g>"
             f'<g class="flame"><path d="{BASE_FLAME}" fill="{P["flame"]}"/><path d="{BASE_CORE}" fill="{P["sun"]}"/></g>'
             f'<path d="{FIN_L}" fill="{P["fin"]}"/><path d="{FIN_R}" fill="{P["fin"]}"/><path d="{NOZZLE}" fill="{P["nozzle"]}"/><path d="{BODY}" fill="{P["body"]}"/>'
             f'<g clip-path="url(#BC)"><rect x="200" y="0" width="70" height="340" fill="#000" opacity=".16"/><rect x="140" y="110" width="120" height="9" fill="{P["sun"]}"/><rect x="140" y="296" width="120" height="7" fill="{P["sun"]}"/></g>'
             f'<path d="{CFIN}" fill="{P["flame"]}"/>{extra}</g></g></g>'
             f'<g transform="rotate(-90 256 256)"><circle class="ring" cx="256" cy="256" r="240" fill="none" stroke="{P["body"]}" stroke-width="16" pathLength="100"/></g></svg>')
    return "".join(o)


def nodes_variant(kind):
    hair = f'fill="none" stroke="{P["ink"]}" stroke-width="2.5" stroke-linecap="round" opacity=".55"'
    line = ""
    if kind == "drawn":
        line = f'<g class="gone"><path class="trace" d="{arcs()}" pathLength="100" {hair}/></g>'
    elif kind == "fading":
        line = "".join(f'<path class="trail" style="--d:{0.4 + i * 0.8}s" d="{seg(i)}" pathLength="100" {hair}/>' for i in range(4))
    elif kind == "moving":
        line = f'<g class="gone"><path class="march" d="{arcs()}" {hair} stroke-dasharray="7 9"/></g>'
    dot = f'<circle class="dot" r="7" fill="{P["fin"]}" style="offset-path:path(\'{arcs()}\')"/>'
    return (f'<svg class="stage" viewBox="0 0 640 300" role="img" aria-label="Storyboard sketch: {kind} line">{roundel()}'
            f'{line}<g class="gone3">{"".join(node(i, x) for i, x in enumerate(XS[:3]))}</g>{node(3, XS[3])}{dot}</svg>')


def hull_variant():
    nums = "".join(f'<path class="n n{n}" d="{NUM[n]}" fill="none" stroke="{P["flame"] if n < 4 else P["success"]}" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round" '
                   f'/>' for n in (1, 2, 3, 4))
    nums = f'<g transform="translate(200 205) scale(.92)">{nums}</g>'
    badge = f'<circle class="bring" cx="200" cy="205" r="35" fill="{P["ground"]}" stroke="{P["flame"]}" stroke-width="6"/>{nums}'
    return f'<svg class="stage hull" viewBox="0 0 640 300" role="img" aria-label="Storyboard sketch: countdown on the hull">{roundel(extra=badge)}</svg>'


CSS = """
.stage{width:100%;height:auto;display:block;background:%(ground)s}
.node,.retry,.tobadge,.disc,.stripes,.rise,.n,.flame{transform-box:fill-box;transform-origin:center}
.play .node{animation:fadein .4s both}
.play .fail{animation:fadein .4s both,flash .5s var(--d) both,dim .4s calc(var(--d) + .5s) forwards}
.play .win{animation:fadein .4s both,win .01s var(--d) forwards,pop .45s var(--d) both}
.play .retry{opacity:0;animation:spin .7s var(--d) both}
.play .dot{animation:travel 3.2s .4s both}
.play .trace{stroke-dasharray:100;animation:trace 3.2s .4s both}
.play .trail{stroke-dasharray:100;animation:draw .55s var(--d) both ease-in-out,fadeout .45s calc(var(--d) + .75s) forwards}
.play .march{animation:fadein .4s both,march 1s linear infinite}
.play .gone,.play .gone3{animation:fadeout .4s 3.6s forwards}
.play .tobadge{animation:tobadge .6s 3.7s both cubic-bezier(.5,0,.2,1)}
.play .disc{animation:grow .55s 3.6s both cubic-bezier(.3,1.3,.5,1)}
.play .stripes{animation:wipe .45s 4s both ease-out}
.play .rise{animation:rise .75s 4.05s both cubic-bezier(.2,1.25,.4,1)}
.play .ring{stroke-dasharray:100;animation:draw .6s 4.7s both ease-in-out}
.hull.play .disc{animation:grow .5s 0s both cubic-bezier(.3,1.3,.5,1)}
.hull.play .stripes{animation:wipe .4s .3s both ease-out}
.hull.play .rise{animation:hulltries 4.3s .5s both}
.hull.play .flame{transform-origin:50% 0;animation:sputter 4.3s .5s both}
.hull.play .ring{animation:draw .6s 4.5s both ease-in-out}
.hull.play .n{opacity:0}
.hull.play .n1{animation:show 1.1s .5s both}.hull.play .n2{animation:show 1.1s 1.6s both}.hull.play .n3{animation:show 1.1s 2.7s both}
.hull.play .n4{animation:fadein .2s 3.8s both,pop .45s 3.8s both}
.hull.play .bring{animation:green .01s 3.8s forwards}
@keyframes fadein{from{opacity:0}to{opacity:1}}
@keyframes fadeout{to{opacity:0}}
@keyframes dim{to{opacity:.28}}
@keyframes flash{0%%,100%%{stroke:%(ink)s}30%%,70%%{stroke:%(fin)s}}
@keyframes win{to{stroke:%(success)s}}
@keyframes green{to{stroke:%(success)s}}
@keyframes pop{0%%{transform:scale(1)}45%%{transform:scale(1.28)}100%%{transform:scale(1)}}
@keyframes spin{0%%{opacity:0;transform:rotate(0)}15%%,80%%{opacity:1}100%%{opacity:0;transform:rotate(360deg)}}
@keyframes travel{0%%{offset-distance:0%%;opacity:1;animation-timing-function:ease-in-out}17%%,25%%{offset-distance:25%%;animation-timing-function:ease-in-out}42%%,50%%{offset-distance:50%%;animation-timing-function:ease-in-out}67%%,75%%{offset-distance:75%%;animation-timing-function:ease-in-out}92%%{offset-distance:100%%;opacity:1}100%%{offset-distance:100%%;opacity:0}}
@keyframes trace{0%%{stroke-dashoffset:100;animation-timing-function:ease-in-out}17%%,25%%{stroke-dashoffset:75;animation-timing-function:ease-in-out}42%%,50%%{stroke-dashoffset:50;animation-timing-function:ease-in-out}67%%,75%%{stroke-dashoffset:25;animation-timing-function:ease-in-out}92%%,100%%{stroke-dashoffset:0}}
@keyframes draw{from{stroke-dashoffset:100}to{stroke-dashoffset:0}}
@keyframes march{to{stroke-dashoffset:-16}}
@keyframes tobadge{to{transform:translate(-180px,-58.1px) scale(.643)}}
@keyframes grow{from{transform:scale(0)}to{transform:scale(1)}}
@keyframes wipe{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes rise{from{transform:translateY(470px)}to{transform:translateY(0)}}
@keyframes hulltries{0%%{transform:translateY(70px)}8%%{transform:translateY(38px)}14%%,26%%{transform:translateY(70px)}34%%{transform:translateY(30px)}40%%,52%%{transform:translateY(70px)}60%%{transform:translateY(22px)}66%%,78%%{transform:translateY(70px);animation-timing-function:cubic-bezier(.2,1.25,.4,1)}100%%{transform:translateY(0)}}
@keyframes sputter{0%%{transform:scaleY(0)}8%%{transform:scaleY(.8)}14%%,26%%{transform:scaleY(0)}34%%{transform:scaleY(.9)}40%%,52%%{transform:scaleY(0)}60%%{transform:scaleY(1)}66%%,78%%{transform:scaleY(0)}90%%,100%%{transform:scaleY(1)}}
@keyframes show{0%%{opacity:0}10%%,90%%{opacity:1}100%%{opacity:0}}
@media (prefers-reduced-motion:reduce){.play *{animation:none!important}.stage .dot,.stage .gone,.stage .gone3,.stage .trail,.stage .retry,.stage .n1,.stage .n2,.stage .n3{opacity:0!important}.stage .tobadge{transform:translate(-180px,-58.1px) scale(.643)}.stage .win,.stage .bring{stroke:%(success)s}.stage .n4{opacity:1!important}}
""".replace("%%", "%")
for _k in ("ground", "ink", "fin", "success"):
    CSS = CSS.replace("%(" + _k + ")s", P[_k])

VARIANTS = [("A", "Drawn line", "A hairline draws behind the dot and stays until launch. Closest to your original concept.", nodes_variant("drawn")),
            ("B", "No line", "Only the dot hops. Cleanest; the nodes carry the story.", nodes_variant("none")),
            ("C", "Fading trail", "Each hop leaves a trail that fades once the dot lands.", nodes_variant("fading")),
            ("D", "Moving line", "The whole path is there from the start, dashes marching toward node 4.", nodes_variant("moving")),
            ("E", "Countdown on the hull", "No nodes or line. The rocket itself tries three times, the badge counting 1, 2, 3 in coral, then a green 4 and liftoff.", hull_variant())]

if __name__ == "__main__":
    os.makedirs("out", exist_ok=True)
    import json
    json.dump({"css": CSS, "variants": [[t, n, s, v] for t, n, s, v in VARIANTS]}, open("out/storyboard.json", "w"))
    print("wrote out/storyboard.json", sum(len(v[3]) for v in VARIANTS))
