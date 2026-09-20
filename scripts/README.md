# Generator scripts

Plain Python 3, no dependencies. Each script writes into `scripts/out/` (ignored by git). Run them from this folder; later scripts import earlier ones, so keep the file names.

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
| `build_h.py` | Round H: phone-screen layouts and the splash files in `splash/` (H2) |

The review pages load fonts from Google Fonts, so open them in a regular browser.
