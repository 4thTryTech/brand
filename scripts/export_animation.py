#!/usr/bin/env python3
"""Plan step 5.5: MP4 and GIF copies of the animated logo for social posts and Canva.
Steps each SVG's animations frame by frame in headless Chromium, then encodes with ffmpeg.
Needs playwright (with Chromium) and ffmpeg. Run build_animation.py first. Writes to out/animation/video/.
"""
import asyncio, os, shutil, subprocess, tempfile
from playwright.async_api import async_playwright

FPS, SECONDS = 30, 6.5          # 5.3 s of motion, then a hold on the finished logo
JOBS = [("logo-animated-light", 720, 720, "#F0E9DC"), ("logo-animated-dark", 720, 720, "#1F2430"),
        ("logo-animated-compact-light", 720, 720, "#F0E9DC"), ("logo-animated-compact-dark", 720, 720, "#1F2430"),
        ("hero-desktop-animated-light", 1280, 720, None), ("hero-desktop-animated-dark", 1280, 720, None),
        ("splash-animated-light", 720, 1558, None), ("splash-animated-dark", 720, 1558, None)]


async def frames(name, w, h, bg, folder):
    svg = open(f"out/animation/{name}.svg").read()
    pad = "padding:12%;box-sizing:border-box;" if bg else ""
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": w, "height": h})
        await pg.set_content(f'<body style="margin:0;background:{bg or "#000"}"><div style="width:{w}px;height:{h}px;{pad}"><style>svg{{width:100%;height:100%;display:block}}</style>{svg}</div>')
        await pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        for i in range(int(FPS * SECONDS)):
            await pg.evaluate(f"document.getAnimations().forEach(a=>{{a.currentTime={i * 1000 / FPS}}})")
            await pg.screenshot(path=os.path.join(folder, f"f{i:04d}.png"))
        await b.close()


def main():
    out = "out/animation/video"
    os.makedirs(out, exist_ok=True)
    for name, w, h, bg in JOBS:
        tmp = tempfile.mkdtemp()
        asyncio.run(frames(name, w, h, bg, tmp))
        src = ["-framerate", str(FPS), "-i", os.path.join(tmp, "f%04d.png")]
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *src, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", f"{out}/{name}.mp4"], check=True)
        if name.startswith("logo"):
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *src, "-vf", "fps=20,scale=480:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=64[p];[b][p]paletteuse=dither=none",
                            "-loop", "0", f"{out}/{name}.gif"], check=True)
        shutil.rmtree(tmp)
        print("wrote", name)


if __name__ == "__main__":
    main()
