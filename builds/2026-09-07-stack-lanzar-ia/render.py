# -*- coding: utf-8 -*-
"""Render retina 2× → 2160×2700 (+ FHD opcional)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageEnhance
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
TOTAL = 12
CSS_W, CSS_H = 1080, 1350
DSF = 2
CAPTURE = (CSS_W * DSF, CSS_H * DSF)
SIZE_4K = (CSS_W * 4, CSS_H * 4)
FHD = (1920, 2400)


def polish(im: Image.Image, sharp: float = 1.05) -> Image.Image:
    im = ImageEnhance.Contrast(im).enhance(1.01)
    return ImageEnhance.Sharpness(im).enhance(sharp)


def save_png(im: Image.Image, path: Path) -> None:
    im.save(path, "PNG", compress_level=1, optimize=False)


def main() -> None:
    png = B / "png"
    png4k = B / "png-4k"
    fhd_dir = B / "png-fhd"
    jpg = B / "jpg"
    for d in (png, png4k, fhd_dir, jpg):
        d.mkdir(exist_ok=True)
    html = B / "carrusel.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--disable-web-security", "--font-render-hinting=none"])
        page = browser.new_page(
            viewport={"width": 1180, "height": 1600},
            device_scale_factor=DSF,
        )
        page.goto(html.as_uri(), wait_until="networkidle")
        page.evaluate(
            """async () => {
              const loads = [
                '800 72px Poppins',
                '400 72px \"Bebas Neue\"',
                '700 34px \"Barlow Condensed\"',
                '600 20px \"IBM Plex Mono\"',
                'italic 600 26px Lora'
              ];
              for (const f of loads) await document.fonts.load(f).catch(() => null);
              await document.fonts.ready;
            }"""
        )
        page.wait_for_timeout(4000)
        slides = page.query_selector_all(".slide")
        assert len(slides) == TOTAL, f"expected {TOTAL}, got {len(slides)}"
        for i, el in enumerate(slides, 1):
            raw = png / f"slide-{i:02d}-raw.png"
            el.screenshot(path=str(raw), type="png", animations="disabled", scale="device")
            im = Image.open(raw).convert("RGB")
            if im.size != CAPTURE:
                im = im.resize(CAPTURE, Image.Resampling.LANCZOS)
            # retina 2160×2700
            save_png(polish(im), png / f"slide-{i:02d}.png")
            # 4K
            im4k = polish(im.resize(SIZE_4K, Image.Resampling.LANCZOS), 1.06)
            save_png(im4k, png4k / f"slide-{i:02d}.png")
            im4k.save(jpg / f"slide-{i:02d}@4k.jpg", "JPEG", quality=92, optimize=True)
            # FHD
            hd = polish(im4k.resize(FHD, Image.Resampling.LANCZOS), 1.1)
            save_png(hd, fhd_dir / f"slide-{i:02d}.png")
            hd.save(jpg / f"slide-{i:02d}@fhd.jpg", "JPEG", quality=90, optimize=True)
            print(f"OK slide-{i:02d}")
        browser.close()


if __name__ == "__main__":
    main()
