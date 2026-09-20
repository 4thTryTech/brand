# Context for Claude sessions working in this repo

This repo holds the core brand assets for 4th Try Tech, shared across projects. Read `GUIDELINES.md` first: it records every brand decision (logo, style rules, colors, type, voice) and the repo layout.

- Colors and type come only from `tokens/`. Do not introduce new colors; green is reserved for success.
- The logo is the roundel in `logo/`. The splash art in `splash/` is hero artwork, not a logo.
- Regenerate logo or splash files by editing and running `scripts/build_logo.py` or `scripts/build_h.py`, then copy the results from `scripts/out/` into `logo/` or `splash/`.
- Copy follows `voice/brand-voice.md`: candid, practical, wry; the journey is the subject.
- Fonts must be self-hosted. Font files are not in the repo yet; adding Fredoka 600, Nunito Sans 400/600 and JetBrains Mono 400 (all SIL OFL) under `fonts/` is an open task, after which the splash text should be converted to outlines.
- The website lives in the separate `4thTryTech/website` repo and should consume these assets.
