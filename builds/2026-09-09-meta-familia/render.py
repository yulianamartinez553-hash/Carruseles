# -*- coding: utf-8 -*-
from __future__ import annotations

from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent


def main() -> None:
    html = B / "carrusel.html"
    png_dir = B / "png"
    png4k = B / "png-4k"
    png_fhd = B / "png-fhd"
    for d in (png_dir, png4k, png_fhd):
        d.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = br.new_page(viewport={"width": 1180, "height": 1450}, device_scale_factor=2)
        pg.goto(html.as_uri())
        pg.wait_for_function("document.fonts.ready")
        pg.wait_for_timeout(4000)
        el = pg.query_selector(".slide")
        raw = png_dir / "slide-01-raw.png"
        el.screenshot(path=str(raw))
        br.close()

    im = Image.open(raw).convert("RGB")
    # lienzo lógico 1080×1350 → retina 2160×2700
    im4k = im.resize((2160, 2700), Image.Resampling.LANCZOS)
    im_fhd = im.resize((1080, 1350), Image.Resampling.LANCZOS)
    dest = png_dir / "slide-01.png"
    im4k.save(dest, optimize=True)
    im4k.save(png4k / "slide-01.png", optimize=True)
    im_fhd.save(png_fhd / "slide-01.png", optimize=True)
    raw.unlink(missing_ok=True)
    print("OK", dest, im4k.size)


if __name__ == "__main__":
    main()
