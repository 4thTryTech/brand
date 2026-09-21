# Generator scripts

Plain Python 3, no dependencies, except where the table says otherwise. Each script writes into `scripts/out/` (ignored by git). Run them from this folder; later scripts import earlier ones, so keep the file names.

| Script | Produces |
| --- | --- |
| `build.py` | Art-direction round A: six general styles (A1 pulp, A2 mid-century, A3 ultra modern, A4 flat, A5 blueprint, A6 pixel) |
| `build_b.py` | Round B: space sci-fi by decade, 1970s to 2020s |
| `build_c.py` | Round C: the flat 2010s look with the rounded rocket; C5 was chosen |
| `build_d.py` | Round D: four palettes with contrast ratios; D1 was chosen. Holds the palette values other scripts import |
| `build_e.py` | Round E: six display typefaces; Fredoka was chosen |
| `build_f.py` | Round F: text face beside Fredoka; Nunito Sans was chosen |
| `build_g.py` | Round G: four logo compositions; G1 roundel was chosen |
| `build_logo.py` | The finished roundel logo files in `logo/` |
| `build_h.py` | Round H: phone-screen layouts and the splash files in `splash/` (H2). The splash files have outlined lettering, so this one also needs `fonttools` |
| `build_elements.py` | The standalone pieces in `elements/` and the icon masters in `icons/` |
| `textpath.py` | Helper: turns a line of text into outlined SVG path data with the font's kerning. Needs `fonttools` and the families in `fonts/` |
| `build_wordmark.py` | The wordmark and tagline lockup in `elements/`. Needs `fonttools` |
| `build_webfonts.py` | The WOFF2 subsets in `fonts/web/`. Needs `fonttools` and `brotli` |
| `build_lockups.py` | Phase 4: the lockups in `logo/` and the tablet and desktop artwork in `hero/`. Needs `fonttools` |
| `build_storyboard.py` | Phase 5.1: the five animation sketches that were compared; option C was chosen |
| `build_animation.py` | Phase 5: the animated files in `animation/`. Needs `fonttools` |
| `export_animation.py` | MP4 and GIF copies in `animation/video/`. Needs `playwright` (with Chromium) and `ffmpeg` |
| `build_guides.py` | The diagrams in `guidelines/`: clear space, minimum sizes, backgrounds, misuse |
| `export_icons.py` | PNG and ICO files in `icons/` and `exports/`. The one script with dependencies: needs `playwright` (with Chromium) and `pillow`. Run `build_logo.py` and `build_elements.py` first |

The review pages load fonts from Google Fonts, so open them in a regular browser.
