# Context for Claude sessions working in this repo

This repo holds the core brand assets for 4th Try Tech, shared across projects. Read `GUIDELINES.md` first: it records every brand decision (logo, style rules, colors, type, voice) and the repo layout.

- Colors and type come only from `tokens/`. Do not introduce new colors; green is reserved for success.
- The logo is the roundel in `logo/`. The splash art in `splash/` is hero artwork, not a logo.
- Regenerate logo or splash files by editing and running `scripts/build_logo.py` or `scripts/build_h.py`, then copy the results from `scripts/out/` into `logo/` or `splash/`.
- Reusable pieces are in `elements/`, the favicon and app-icon set in `icons/`, PNG copies in `exports/`. Regenerate with `scripts/build_elements.py` then `scripts/export_icons.py` and copy from `scripts/out/`.
- When running git here from a Claude session, use `git --no-optional-locks` for read commands: the session cannot delete files, so a plain `git status` can leave a stale `.git/index.lock` behind.
- Copy follows `voice/brand-voice.md`: candid, practical, wry; the journey is the subject.
- Fonts are self-hosted: sites use `fonts/web/` (WOFF2 subsets plus `fonts.css`). Brand lettering in SVGs is always outlined with `scripts/textpath.py`, never live text, so files need no font. Those scripts need `fonttools` (and `brotli` for `build_webfonts.py`).
- The website lives in the separate `4thTryTech/website` repo and should consume these assets.
