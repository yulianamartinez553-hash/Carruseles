# -*- coding: utf-8 -*-
"""Render 4K HQ — captura nativa 4x, entrega 4320×5400 + derivados."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageEnhance
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
TOTAL = 8
CSS_W, CSS_H = 1080, 1350
DSF = 4
OUT_W, OUT_H = CSS_W * 2, CSS_H * 2
FHD = (1920, 2400)


def polish(im: Image.Image) -> Image.Image:
    im = ImageEnhance.Contrast(im).enhance(1.02)
    im = ImageEnhance.Sharpness(im).enhance(1.08)
    return im


def main() -> None:
    png = B / "png"
    png4k = B / "png-4k"
    fhd = B / "png-fhd"
    jpg = B / "jpg"
    for d in (png, png4k, fhd, jpg):
        d.mkdir(exist_ok=True)
    html = B / "carrusel.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            args=["--no-sandbox", "--disable-dev-shm-usage", "--font-render-hinting=none"]
        )
        page = browser.new_page(viewport={"width": CSS_W, "height": CSS_H}, device_scale_factor=DSF)
        page.goto(html.resolve().as_uri(), wait_until="networkidle")
        page.evaluate(
            """async () => {
              await document.fonts.ready;
              for (const f of [
                '400 72px \"Bebas Neue\"',
                '700 28px \"Barlow Condensed\"',
                '500 14px \"IBM Plex Mono\"'
              ])
                await document.fonts.load(f).catch(()=>null);
              await document.fonts.ready;
            }"""
        )
        page.wait_for_timeout(900)
        slides = page.query_selector_all(".slide")
        assert len(slides) == TOTAL, f"expected {TOTAL}, got {len(slides)}"
        for i, el in enumerate(slides, 1):
            raw = png4k / f"slide-{i:02d}-raw.png"
            el.screenshot(path=str(raw), type="png", animations="disabled", scale="device")
            im = Image.open(raw).convert("RGB")
            target = (CSS_W * DSF, CSS_H * DSF)
            if im.size != target:
                im = im.resize(target, Image.Resampling.LANCZOS)
            im = polish(im)
            im.save(png4k / f"slide-{i:02d}.png", "PNG", compress_level=1)
            retina = im.resize((OUT_W, OUT_H), Image.Resampling.LANCZOS)
            retina = polish(retina)
            retina.save(png / f"slide-{i:02d}.png", "PNG", compress_level=1)
            hd = im.resize(FHD, Image.Resampling.LANCZOS)
            hd = polish(hd)
            hd.save(fhd / f"slide-{i:02d}.png", "PNG", compress_level=1)
            im.save(jpg / f"slide-{i:02d}@4k.jpg", "JPEG", quality=97, subsampling=0)
            retina.save(jpg / f"slide-{i:02d}@2x.jpg", "JPEG", quality=96, subsampling=0)
            hd.save(jpg / f"slide-{i:02d}@fhd.jpg", "JPEG", quality=97, subsampling=0)
            hd.resize((CSS_W, CSS_H), Image.Resampling.LANCZOS).save(
                jpg / f"slide-{i:02d}.jpg", "JPEG", quality=98, subsampling=0
            )
            raw.unlink(missing_ok=True)
            print("OK", f"slide-{i:02d}", im.size)
        browser.close()


if __name__ == "__main__":
    main()
