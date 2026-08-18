# -*- coding: utf-8 -*-
"""Renderiza el reloj STLabs a MP4 6:7 con agujas en loop exacto."""
from pathlib import Path
import shutil
import subprocess
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
W, H = 1080, 1260  # 6:7
DURATION = 8.0
FPS = 30
FRAMES = int(DURATION * FPS)


def main():
    frames = B / "frames"
    if frames.exists():
        shutil.rmtree(frames)
    frames.mkdir()
    out_mp4 = B / "reloj.mp4"

    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto((B / "reloj.html").as_uri() + "?still=1")
        pg.wait_for_function("document.fonts.ready")
        pg.wait_for_timeout(400)
        for i in range(FRAMES):
            t = (i / FRAMES) * DURATION
            pg.evaluate("t => window.setClock(t)", t)
            pg.locator("#stage").screenshot(path=str(frames / f"f{i:04d}.png"))
            if i % 30 == 0:
                print(f"frame {i}/{FRAMES}")
        br.close()

    poster = B / "poster.jpg"
    subprocess.run(
        [
            "ffmpeg", "-y", "-i", str(frames / "f0000.png"),
            "-q:v", "3", str(poster),
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-framerate", str(FPS),
            "-i", str(frames / "f%04d.png"),
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-crf", "18",
            "-preset", "medium",
            "-movflags", "+faststart",
            "-t", str(DURATION),
            str(out_mp4),
        ],
        check=True,
    )
    print(f"OK {out_mp4} · {FRAMES} frames")


if __name__ == "__main__":
    main()
