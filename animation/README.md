# Animated logo

Three tries that do not take, a fourth that does. The dot hops from node to node leaving a trail that fades; nodes 1 to 3 flash coral, get a retry arrow and dim; node 4 turns green and becomes the badge on the hull while the sun grows, the stripes wipe in, the rocket rises and the ring draws. About 5.3 seconds, ending on exactly the static artwork.

| File | What it is |
| --- | --- |
| `logo-animated-light.svg`, `-dark.svg` | The roundel, 512 x 512. Its last frame matches `logo/logo-roundel-*.svg` |
| `logo-animated-compact-light.svg`, `-dark.svg` | Compact version for tight spaces, 512 x 512. Nothing leaves the roundel: the rocket lifts and drops back three times while the badge counts 1, 2, 3 in coral, then a green 4 and liftoff. About 5.1 s. Same last frame |
| `splash-animated-*.svg` | Phone splash, 1170 x 2532. Last frame matches `splash/` |
| `hero-desktop-animated-*.svg`, `hero-tablet-animated-*.svg` | Landscape heroes. Last frame matches `hero/` |
| `video/*.mp4`, `video/logo-animated-*.gif` (compact included) | Rendered copies for social posts and Canva, 6.5 s with a hold at the end |

Plain SVG and CSS inside each file: no libraries and no script. The animation plays once when the file loads. It never loops.

## On a web page

As an image it plays once on load:

```html
<img src="/brand/logo-animated-light.svg" alt="4th Try Tech" width="160" height="160">
```

To let people replay it by clicking or tapping, put the SVG inline and swap it for a fresh copy:

```html
<div class="logo"><!-- paste the contents of logo-animated-light.svg here --></div>
<script>
  document.querySelector('.logo').addEventListener('click', function () {
    var svg = this.querySelector('svg'); svg.replaceWith(svg.cloneNode(true));
  });
</script>
```

People who have asked their device to reduce motion get the finished still frame and nothing moves; this is built into each file.

Which roundel: use the full version where it has room to breathe, at about 240 px and up, since the nodes are small inside it. Use the compact version below that, down to 64 px, or wherever the layout cannot give the nodes space.

Play it once per visit, on the home page hero or the splash. Everywhere else (headers on inner pages, documents, email) use the static logo.

Regenerate with `scripts/build_animation.py`, then `scripts/export_animation.py` for the video copies.
