#!/usr/bin/env python3
"""Plan steps 5.2 to 5.4: the animated logo, storyboard option C (fading trail).

Three tries that do not take, a fourth that does: node 4 turns green and becomes the badge on the hull while the
scene assembles around it. Plain SVG + CSS inside each file, no libraries, no script. Plays once when loaded, ends on
exactly the static artwork, and shows only that still frame to people who ask for reduced motion.

Writes out/animation/: the roundel (512), the phone splash (1170 x 2532), and the tablet and desktop heroes.
Needs fonttools and ../fonts/ for the outlined lettering in the splash and heroes.
"""
import os
from build import BASE_FLAME, BASE_CORE
from build_c import BODY, FIN_L, FIN_R, NOZZLE, CFIN
from build_d import PALETTES
from build_logo import FOUR
from build_h import icons
from textpath import text_path

L, D = PALETTES[0]["light"], PALETTES[0]["dark"]
TAG = "When the 3rd try wasn’t enough, keep going."
NUM = {1: "M-5 -9 L2 -15 V15", 2: "M-8 -8 C-8 -19 9 -19 8 -7 C8 1 -8 5 -8 15 H9", 3: "M-8 -12 C-3 -18 9 -16 8 -8 C8 -2 2 0 -2 0 C4 0 10 3 9 9 C8 17 -3 19 -9 12"}
FOUR0 = "M7 20 V-20 L-15 8 H16"            # the logo's 4, moved so the badge center is 0,0
T_TRY, T_HOP = 0.8, 0.55                   # seconds per try; seconds the dot is in the air
T_LAUNCH = 0.4 + 4 * T_TRY                 # 3.6 s: the scene starts to assemble

CSS = """
.node,.retry path,.tobadge,.sun,.stripes,.rise,.flame,.words{transform-box:fill-box;transform-origin:center}
.node{animation:fadein .4s both}
.fail{animation:fadein .4s both,flash .5s var(--d) both,dim .4s calc(var(--d) + .5s) forwards,fadeout .4s 3.6s forwards}
.win{animation:fadein .4s both,win .01s var(--d) forwards,pop .45s var(--d) both}
.retry{opacity:0;animation:blink .7s var(--d) both}
.retry path{animation:turn .7s var(--d) both}
.dot{animation:travel 3.2s .4s both}
.trail{stroke-dasharray:100;animation:draw .55s var(--d) both ease-in-out,fadeout .45s calc(var(--d) + .75s) forwards}
.tobadge{animation:tobadge .6s 3.7s both cubic-bezier(.5,0,.2,1)}
.sun{animation:grow .55s 3.6s both cubic-bezier(.3,1.3,.5,1)}
.stripes{animation:wipe .45s 4s both ease-out}
.rise{animation:rise .75s 4.05s both cubic-bezier(.2,1.25,.4,1)}
.flame{transform-origin:50% 0;animation:burn .9s 4.05s both ease-out}
.ring{stroke-dasharray:100;animation:draw .6s 4.7s both ease-in-out}
.icons{animation:fadein .6s 4.5s both}
.words{animation:fadeup .6s 4.7s both ease-out}
.tagline{animation-delay:4.9s}
@keyframes fadein{from{opacity:0}to{opacity:1}}
@keyframes fadeout{to{opacity:0}}
@keyframes fadeup{from{opacity:0;transform:translateY(var(--up))}to{opacity:1;transform:translateY(0)}}
@keyframes dim{to{opacity:.28}}
@keyframes flash{0%,100%{stroke:INK}30%,70%{stroke:FIN}}
@keyframes win{to{stroke:SUCCESS}}
@keyframes pop{0%{transform:scale(1)}45%{transform:scale(1.28)}100%{transform:scale(1)}}
@keyframes blink{0%,100%{opacity:0}15%,80%{opacity:1}}
@keyframes turn{to{transform:rotate(360deg)}}
@keyframes travel{0%{offset-distance:0%;opacity:0;animation-timing-function:ease-in-out}3%{opacity:1}17%,25%{offset-distance:25%;animation-timing-function:ease-in-out}42%,50%{offset-distance:50%;animation-timing-function:ease-in-out}67%,75%{offset-distance:75%;animation-timing-function:ease-in-out}92%{offset-distance:100%;opacity:1}100%{offset-distance:100%;opacity:0}}
@keyframes draw{from{stroke-dashoffset:100}to{stroke-dashoffset:0}}
@keyframes tobadge{to{transform:translate(var(--bx),var(--by)) scale(var(--bs))}}
@keyframes grow{0%{transform:scale(.001);opacity:0}4%{opacity:1}100%{transform:scale(1);opacity:1}}
@keyframes wipe{0%{transform:scaleX(.001);opacity:0}4%{opacity:1}100%{transform:scaleX(1);opacity:1}}
@keyframes rise{from{transform:translateY(var(--rise))}to{transform:translateY(0)}}
@keyframes burn{0%{transform:scaleY(.2)}40%{transform:scaleY(1.25)}100%{transform:scaleY(1)}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}.dot,.fail,.trail,.retry{opacity:0}.tobadge{transform:translate(var(--bx),var(--by)) scale(var(--bs))}.win{stroke:SUCCESS}}
/* compact version: the rocket itself tries three times, inside the roundel */
.c .sun{animation:grow .5s 0s both cubic-bezier(.3,1.3,.5,1)}
.c .stripes{animation:wipe .4s .3s both ease-out}
.c .rise{animation:hulltries 4.3s .5s both,fadein .3s .25s both}
.c .flame{animation:sputter 4.3s .5s both}
.c .ring{animation:draw .6s 4.5s both ease-in-out}
.c .n{opacity:0}
.c .n4{transform-box:fill-box;transform-origin:center}
.c .n1{animation:show 1.1s .5s both}.c .n2{animation:show 1.1s 1.6s both}.c .n3{animation:show 1.1s 2.7s both}
.c .n4{animation:fadein .2s 3.8s both,pop .45s 3.8s both}
.c .bring{animation:win .01s 3.8s forwards}
@keyframes hulltries{0%{transform:translateY(70px)}8%{transform:translateY(38px)}14%,26%{transform:translateY(70px)}34%{transform:translateY(30px)}40%,52%{transform:translateY(70px)}60%{transform:translateY(22px)}66%,78%{transform:translateY(70px);animation-timing-function:cubic-bezier(.2,1.25,.4,1)}100%{transform:translateY(0)}}
@keyframes sputter{0%{transform:scaleY(0)}8%{transform:scaleY(.8)}14%,26%{transform:scaleY(0)}34%{transform:scaleY(.9)}40%,52%{transform:scaleY(0)}60%{transform:scaleY(1)}66%,78%{transform:scaleY(0)}90%,100%{transform:scaleY(1)}}
@keyframes show{0%{opacity:0}10%,90%{opacity:1}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){.c .n4{opacity:1}.c .bring{stroke:SUCCESS}}
"""


def rocket(P, place, gap, clip, extra=""):
    """The rocket without its badge (node 4 becomes the badge). `rise` has no transform of its own, so CSS can move it."""
    return (f'<g class="rise" id="rocket"><g transform="{place}">'
            f'<g fill="{gap}" stroke="{gap}" stroke-width="14" stroke-linejoin="round">' + "".join(f'<path d="{d}"/>' for d in (BODY, FIN_L, FIN_R, NOZZLE, BASE_FLAME)) + "</g>"
            f'<g class="flame" id="flame"><path d="{BASE_FLAME}" fill="{P["flame"]}"/><path d="{BASE_CORE}" fill="{P["sun"]}"/></g>'
            f'<g id="fins"><path d="{FIN_L}" fill="{P["fin"]}"/><path d="{FIN_R}" fill="{P["fin"]}"/></g><path d="{NOZZLE}" fill="{P["nozzle"]}"/><path id="body" d="{BODY}" fill="{P["body"]}"/>'
            f'<g clip-path="url(#{clip})"><rect x="200" y="0" width="70" height="340" fill="#000" opacity=".16"/><rect x="140" y="110" width="120" height="9" fill="{P["sun"]}"/><rect x="140" y="296" width="120" height="7" fill="{P["sun"]}"/></g>'
            f'<path d="{CFIN}" fill="{P["flame"]}"/>{extra}</g></g>')


def tries(P, xs, ny, r, badge, k):
    """Nodes, trails and the hopping dot. badge = (x, y, radius) of the 4 on the finished hull; k = rocket scale there."""
    step = xs[1] - xs[0]
    bs = badge[2] / r
    sw = 6 * k / bs                                    # so the ring of node 4 ends at the badge's stroke width
    hop = lambda x: f"M{x - step} {ny - r} Q{x - step / 2} {ny - r - step * .77} {x} {ny - r}"
    path = f"M{xs[0] - step} {ny - r}" + "".join(f" Q{x - step / 2} {ny - r - step * .77} {x} {ny - r}" for x in xs)
    o = ['<g id="tries">']
    for i, x in enumerate(xs):
        o.append(f'<path class="trail" style="--d:{0.4 + i * T_TRY}s" d="{hop(x)}" pathLength="100" fill="none" stroke="{P["ink"]}" stroke-width="{r * .1:.1f}" stroke-linecap="round" opacity=".55"/>')
    for i, x in enumerate(xs):
        land = 0.4 + i * T_TRY + T_HOP
        if i < 3:
            num = f'<path d="{NUM[i + 1]}" fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" transform="scale({r / 42:.3f})"/>'
            o.append(f'<g transform="translate({x} {ny})"><g class="node fail" style="--d:{land}s" stroke="{P["ink"]}"><circle r="{r}" fill="{P["ground"]}" stroke-width="{r * .115:.1f}"/>{num}</g>'
                     f'<g class="retry" style="--d:{land}s" transform="scale({r / 26:.3f})"><path d="M0 -36 A36 36 0 1 1 -31 -18 M-40 -24 L-31 -18 L-27 -29" fill="none" stroke="{P["flame"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g></g>')
        else:
            num = f'<path d="{FOUR0}" fill="none" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round" transform="scale({k / bs:.4f})"/>'
            o.append(f'<g transform="translate({x} {ny})"><g class="tobadge" id="badge"><g class="node win" style="--d:{land}s" stroke="{P["ink"]}"><circle r="{r}" fill="{P["ground"]}" stroke-width="{sw:.2f}"/>{num}</g></g></g>')
    o.append(f'<circle class="dot" r="{r * .27:.1f}" fill="{P["fin"]}" style="offset-path:path(\'{path}\')"/></g>')
    var = f"--bx:{badge[0] - xs[3]:.1f}px;--by:{badge[1] - ny:.1f}px;--bs:{bs:.4f}"
    return "".join(o), var


def wrap(W, H, P, title, body, var, rise, up=0, cls=""):
    css = CSS.replace("INK", "var(--ink)").replace("FIN", "var(--fin)").replace("SUCCESS", "var(--ok)")     # colors ride on the root, so light and dark files can share a page
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t"{cls} style="{var};--rise:{rise}px;--up:{up}px;--ink:{P["ink"]};--fin:{P["fin"]};--ok:{P["success"]}">'
            f'<title id="t">{title}</title><style>{css}</style>{body}</svg>')


def roundel(P, mode):
    place = "translate(256 268) scale(1.02) translate(-200 -242)"
    badge = (256, 268 + 1.02 * (205 - 242), 35 * 1.02)
    t, var = tries(P, [100, 204, 308, 412], 262, 30, badge, 1.02)
    body = (f'<defs><clipPath id="dc"><circle cx="256" cy="256" r="232"/></clipPath><clipPath id="bc"><path d="{BODY}"/></clipPath></defs>'
            f'<circle class="sun" id="disc" cx="256" cy="256" r="232" fill="{P["sun"]}"/><g clip-path="url(#dc)"><g class="stripes" id="stripes">'
            + "".join(f'<rect x="0" y="{300 + i * 18}" width="512" height="18" fill="{c}"/>' for i, c in enumerate([P["flame"], P["fin"], P["body"]]))
            + f'</g>{rocket(P, place, P["sun"], "bc")}</g>'
            f'<g transform="rotate(-90 256 256)"><circle class="ring" id="ring" cx="256" cy="256" r="240" fill="none" stroke="{P["body"]}" stroke-width="16" pathLength="100"/></g>{t}')
    return wrap(512, 512, P, f"4th Try Tech animated logo ({mode})", body, var, 470)



def compact(P, mode):
    """Storyboard option E, for tight spaces: nothing leaves the roundel. The badge counts 1, 2, 3 in coral while the
    rocket lifts and drops back, then shows a green 4 and the rocket climbs to its place."""
    place = "translate(256 268) scale(1.02) translate(-200 -242)"
    nums = "".join(f'<path class="n n{n}" d="{NUM[n]}" fill="none" stroke="{P["flame"]}" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round" transform="scale(.92)"/>' for n in (1, 2, 3))
    badge = (f'<g id="badge"><circle class="bring" cx="200" cy="205" r="35" fill="{P["ground"]}" stroke="{P["flame"]}" stroke-width="6"/><g transform="translate(200 205)">{nums}</g>'
             f'<path class="n n4" d="{FOUR}" fill="none" stroke="{P["success"]}" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"/></g>')
    body = (f'<defs><clipPath id="dc"><circle cx="256" cy="256" r="232"/></clipPath><clipPath id="bc"><path d="{BODY}"/></clipPath></defs>'
            f'<circle class="sun" id="disc" cx="256" cy="256" r="232" fill="{P["sun"]}"/><g clip-path="url(#dc)"><g class="stripes" id="stripes">'
            + "".join(f'<rect x="0" y="{300 + i * 18}" width="512" height="18" fill="{c}"/>' for i, c in enumerate([P["flame"], P["fin"], P["body"]]))
            + f'</g>{rocket(P, place, P["sun"], "bc", badge)}</g>'
            f'<g transform="rotate(-90 256 256)"><circle class="ring" id="ring" cx="256" cy="256" r="240" fill="none" stroke="{P["body"]}" stroke-width="16" pathLength="100"/></g>')
    return wrap(512, 512, P, f"4th Try Tech animated logo, compact ({mode})", body, "--bx:0px;--by:0px;--bs:1", 470, cls=' class="c"')


def scene(W, H, P, title, sun, stripe_y, stripe_h, k, rocket_xy, icon_pts, words, nodes):
    """Shared by the splash and the heroes. sun = (cx, cy, r); words = list of (class, path data, fill)."""
    place = f"translate({rocket_xy[0]:.1f} {rocket_xy[1]:.1f}) scale({k:.4f}) translate(-200 -242)"
    badge = (rocket_xy[0], rocket_xy[1] + k * (205 - 242), 35 * k)
    t, var = tries(P, *nodes, badge, k)
    body = (f'<defs><clipPath id="bc"><path d="{BODY}"/></clipPath></defs><rect width="{W}" height="{H}" fill="{P["ground"]}"/>'
            f'<circle class="sun" id="sun" cx="{sun[0]:.1f}" cy="{sun[1]:.1f}" r="{sun[2]:.1f}" fill="{P["sun"]}"/><g class="stripes" id="stripes" style="transform-origin:0 50%">'
            + "".join(f'<rect x="0" y="{stripe_y + i * stripe_h:.1f}" width="{W}" height="{stripe_h:.1f}" fill="{c}"/>' for i, c in enumerate([P["flame"], P["fin"], P["body"]]))
            + f'</g><g class="icons" id="icons">{icons(P, icon_pts)}</g>{rocket(P, place, P["ground"], "bc")}'
            + "".join(f'<g class="words {c}" id="{c}"><path d="{d}" fill="{f}"/></g>' for c, d, f in words) + t)
    return wrap(W, H, P, title, body, var, H, up=H * .012)


def splash(P, mode):
    W, H = 1170, 2532
    d1, _ = text_path("4th Try Tech", "fredoka-600", 124, W / 2, 2010, "middle", tracking=2)
    d2, _ = text_path(TAG, "nunito-400", 46, W / 2, 2106, "middle")
    pts = [("planet", 170, 330, 34), ("plus", 1000, 290, 24), ("plus", 110, 1560, 18), ("plus", 1060, 1600, 20)]
    return scene(W, H, P, f"4th Try Tech animated splash ({mode})", (585, 930, 500), 1150, 58, 3.3, (585, 1010), pts,
                 [("wordmark", d1, P["body"]), ("tagline", d2, P["ink"])], ([210, 460, 710, 960], 1240, 72))


def hero(W, H, P, mode, name):
    k = H / 1440
    wide = W / H > 1.5
    cx, cy, r = W * (0.70 if wide else 0.75), H * 0.47, (470 if wide else 440) * k
    sy, sh = cy + 215 * k, 56 * k
    x, y = W * 0.07, sy - 120 * k
    size = min(150 * k, ((cx - r) - x - 50 * k) / 717.4 * 124)
    d1, _ = text_path("4th Try Tech", "fredoka-600", size, x, y, "start", tracking=size * 2 / 124)
    d2, _ = text_path("When the 3rd try wasn’t enough,", "nunito-400", size * .40, x, sy + 3 * sh + 110 * k, "start")
    d3, _ = text_path("keep going.", "nunito-400", size * .40, x, sy + 3 * sh + 110 * k + size * .54, "start")
    pts = [("planet", W * .08, H * .16, 30 * k), ("plus", W * .40, H * .12, 22 * k), ("plus", W * .93, H * .20, 20 * k), ("plus", W * .04, H * .94, 16 * k), ("plus", W * .46, H * .90, 18 * k), ("planet", W * .95, H * .91, 20 * k)]
    step = W * .17
    xs = [W / 2 - 1.5 * step + i * step for i in range(4)]
    return scene(W, H, P, f"4th Try Tech animated hero ({name}, {mode})", (cx, cy, r), sy, sh, 2.95 * k, (cx, cy + 75 * k), pts,
                 [("wordmark", d1, P["body"]), ("tagline", d2 + d3, P["ink"])], (xs, H * .52, 64 * k))


FILES = {}
for mode, P in (("light", L), ("dark", D)):
    FILES[f"logo-animated-{mode}.svg"] = roundel(P, mode)
    FILES[f"logo-animated-compact-{mode}.svg"] = compact(P, mode)
    FILES[f"splash-animated-{mode}.svg"] = splash(P, mode)
    FILES[f"hero-desktop-animated-{mode}.svg"] = hero(2560, 1440, P, mode, "desktop")
    FILES[f"hero-tablet-animated-{mode}.svg"] = hero(2048, 1536, P, mode, "tablet")

if __name__ == "__main__":
    os.makedirs("out/animation", exist_ok=True)
    for n, s in FILES.items():
        open(os.path.join("out/animation", n), "w").write(s)
    print("wrote", sorted(FILES))
