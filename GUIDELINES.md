# 4th Try Tech brand guidelines

Version 0.1, 20 September 2026. Decisions made by Michael Lehman; drawn and documented with Claude.

4th Try Tech is a working log of technology projects, experiments, and misadventures.

## Logo

The logo is the **roundel**: a rounded rocket with a 4 on its hull, launching in front of a sun disc and a three-stripe band, inside a ring.

| File | Use |
| --- | --- |
| `logo/logo-roundel-light.svg` | Default, on light backgrounds |
| `logo/logo-roundel-dark.svg` | On dark backgrounds |
| `logo/logo-roundel-small.svg` | 48 px and below (favicons, tiny avatars). Simplified: no numeral, bands or center fin; thicker ring; plain green porthole |
| `logo/logo-roundel-mono-ink.svg` | One color on light: stamps, watermarks, clashing backgrounds |
| `logo/logo-roundel-mono-reversed.svg` | One color, white, transparent background, for dark surfaces |
| `logo/logo-roundel-mono-reversed-preview.svg` | Viewing only. Has a dark square built in; do not place in designs |

The 4 is drawn as a shape, so the logo needs no font. Every part is a named group (`ring`, `disc`, `stripes`, `rocket`, `flame`, `fins`, `body`, `bands`, `badge`, `numeral`) so it can be animated part by part.

**Splash and hero artwork** is a separate piece: `splash/splash-light.svg` and `splash/splash-dark.svg` (1170 x 2532, 9:19.5 portrait). It is the roundel's scene opened to full screen with no ring, plus the wordmark and tagline. Use it for splash screens and hero sections; use the roundel in headers, icons and anywhere a logo is expected. The splash files set their text in Fredoka and Nunito Sans through a web import, so they need a browser; outline the text once font files are added to this repo.

Still to define: clear space, minimum sizes, and misuse examples (plan phase 3).

## Style rules

| Rule | Detail |
| --- | --- |
| Base | Flat design: solid shapes, no gradients, no long shadows |
| Rocket | Rounded torpedo body, swept fins, thin center fin, two hull bands |
| Depth | Right half of the body is one shade darker. Fins are one flat color, never shaded |
| Separation | A background-colored gap surrounds the rocket wherever it crosses other shapes |
| Scene | Large flat sun disc behind the rocket; warm three-stripe band (flame, fin, body colors); a few hairline icons (ringed planet, plus-sign stars) |
| Texture | None on the web. Paper grain and ink outlines are reserved for print pieces |
| Green | Means success and is used for nothing else: the 4 badge, confirmations |

## Color

Palette "slate and coral". Source of truth: `tokens/colors.json` and `tokens/colors.css` (CSS custom properties prefixed `--ftt-`, with automatic dark mode and a `data-theme` override).

| Role | Light | Dark | Use |
| --- | --- | --- | --- |
| ground | `#F0E9DC` | `#1F2430` | Page background |
| body | `#46607A` | `#7E9CBC` | Primary brand color; rocket body, headings, links |
| fin | `#C44E33` | `#E0694C` | Accent; fins, calls to action |
| finShade | `#A23C26` | `#C44E33` | Accent shade; hover states |
| flame | `#E07A5F` | `#F08A6C` | Secondary accent; flame, stripes |
| sun | `#F2CC8F` | `#E8C07D` | Warm neutral; sun disc, hull bands, soft fills |
| success | `#4E8A6D` | `#7FC29F` | Success only |
| ink | `#3D405B` | `#E6E1D6` | Text and hairline icons |

Contrast against the ground, WCAG 2: ink 8.4:1 light and 11.9:1 dark (passes 4.5:1 for text); body, fin and success all pass 3:1 for shapes and large type in both modes. The light-mode success green is 3.4:1, so do not use it for small body text.

## Typography

Source of truth: `tokens/typography.json`. All three families are under the SIL Open Font License and are available in Canva.

| Role | Family | Weights | Use |
| --- | --- | --- | --- |
| Display | Fredoka | 600 | Wordmark, headlines, buttons, badges |
| Text | Nunito Sans | 400, 600 | Paragraphs, lists, captions, interface |
| Code | JetBrains Mono | 400 | Code and console snippets |

Self-host the font files from this repo. Do not load them from Google at view time: some viewers and privacy filters block it, and the brand then falls back to system fonts.

## Voice

Full text: `voice/brand-voice.md`.

- **Tagline:** When the 3rd try wasn't enough, keep going.
- **Tone:** candid, practical, wry.
- The journey is the subject; setbacks are part of the route, not the headline. Plain words, first person. Specifics over adjectives. Persistence is shown, not preached.

## Future theme variants

Three explored styles were liked and set aside to return as theme variants of the same brand: terminal / pixel, technical blueprint, and 1970s airbrush. They can be regenerated from `scripts/` (styles A6, A5 and B1).

## Repository layout

| Path | Contents |
| --- | --- |
| `tokens/` | Color and typography design tokens |
| `logo/` | Roundel logo, all versions |
| `splash/` | Full-screen splash and hero artwork |
| `voice/` | Brand voice |
| `reference/` | Original concept (v0) and the chosen art-direction reference images |
| `scripts/` | Python generators for every review page and for the logo and splash files. See `scripts/README.md` |
