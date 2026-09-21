#!/usr/bin/env python3
"""Plan step 3.2: PNG and ICO exports of the icon masters. Run build_logo.py and build_elements.py first.

Unlike the other scripts this one needs two packages: playwright (with Chromium) to rasterize, and Pillow for the .ico.
  pip install playwright pillow && playwright install chromium
Sizes 16 and 24 come from icon-micro.svg, 32 and 48 from the small roundel, larger from the full logo or the app icon.
"""
import asyncio, base64, os
from PIL import Image
from playwright.async_api import async_playwright

I, LOGO, OUT, EXP = "out/icons/", "out/logo/", "out/icons/", "out/exports/"
JOBS = [(I + "icon-micro.svg", OUT + "favicon-16.png", 16, None), (I + "icon-micro.svg", OUT + "favicon-24.png", 24, None),
        (LOGO + "logo-roundel-small.svg", OUT + "favicon-32.png", 32, None), (LOGO + "logo-roundel-small.svg", OUT + "favicon-48.png", 48, None),
        (I + "app-icon-light.svg", OUT + "apple-touch-icon.png", 180, "#F2CC8F"),
        (I + "app-icon-light.svg", OUT + "icon-192.png", 192, "#F2CC8F"), (I + "app-icon-light.svg", OUT + "icon-512.png", 512, "#F2CC8F"),
        (I + "app-icon-light.svg", OUT + "icon-maskable-512.png", 512, "#F2CC8F"),
        (I + "app-icon-light.svg", EXP + "avatar-light-1024.png", 1024, "#F2CC8F"), (I + "app-icon-dark.svg", EXP + "avatar-dark-1024.png", 1024, "#E8C07D")]
for v in ("light", "dark", "mono-ink", "mono-reversed"):
    JOBS += [(LOGO + f"logo-roundel-{v}.svg", EXP + f"logo-roundel-{v}-{s}.png", s, None) for s in (512, 1024)]


async def main():
    os.makedirs(OUT, exist_ok=True); os.makedirs(EXP, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for src, out, s, bg in JOBS:
            pg = await b.new_page(viewport={"width": s, "height": s}, device_scale_factor=1)
            uri = "data:image/svg+xml;base64," + base64.b64encode(open(src, "rb").read()).decode()
            await pg.set_content(f'<body style="margin:0;background:{bg or "transparent"}"><img src="{uri}" style="display:block;width:{s}px;height:{s}px">')
            await pg.screenshot(path=out, omit_background=bg is None, clip={"x": 0, "y": 0, "width": s, "height": s})
            await pg.close()
        await b.close()
    frames = [Image.open(OUT + f"favicon-{s}.png").convert("RGBA") for s in (16, 24, 32, 48)]
    frames[-1].save(OUT + "favicon.ico", format="ICO", append_images=frames[:-1], sizes=[(f.width, f.height) for f in frames])
    print("wrote", len(JOBS), "PNG files and favicon.ico")

if __name__ == "__main__":
    asyncio.run(main())
