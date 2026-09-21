# Elements

Reusable pieces of the logo, each a standalone SVG drawn from the same shapes and tokens as `logo/`. Assemble new artwork from these instead of redrawing.

| File | Use |
| --- | --- |
| `rocket-light.svg`, `rocket-dark.svg` | The rocket alone: success states, call-to-action accents, illustrations |
| `rocket-mono-ink.svg`, `rocket-mono-reversed.svg` | One-color rocket |
| `badge-4-light.svg`, `badge-4-dark.svg`, `badge-4-mono-*.svg` | Circle with the 4: bullets, progress markers, section markers. The colored badge is success green, so use it only where success is meant; use a mono badge elsewhere |
| `sun-stripes-light.svg`, `sun-stripes-dark.svg` | Sun disc with the stripe band, no rocket or ring: backgrounds and empty states |
| `stripe-band-light.svg`, `stripe-band-dark.svg` | The three-stripe band as a rule or divider. Stretches sideways to any width |
| `hairline-star.svg`, `hairline-planet.svg` | Scene icons. They draw in `currentColor`; use them at about 45% opacity |

| `wordmark-*.svg` | "4th Try Tech" in Fredoka 600: headers, footers, documents. Light, dark, mono-ink, mono-reversed |
| `tagline-lockup-*.svg` | Wordmark with the tagline beneath: hero sections, slides. Same four versions |

The icon mark is the roundel itself, in `logo/`. The lettering in the wordmark and lockup is outlined, so no font is needed.

Regenerate with `scripts/build_elements.py` and `scripts/build_wordmark.py`.
