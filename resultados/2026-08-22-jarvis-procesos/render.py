# -*- coding: utf-8 -*-
"""Render retina HQ: captura a 3x y baja a 2160x2700 con nitidez."""
from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
TOTAL = 10
CSS_W, CSS_H = 1080, 1350
# Captura supersample 3x → downscale a 2x retina
CAPTURE_DSF = 3
OUT_DSF = 2
OUT_W, OUT_H = CSS_W * OUT_DSF, CSS_H * OUT_DSF


def finalize(im: Image.Image) -> Image.Image:
    """Baja de 3x a 2x con LANCZOS + unsharp controlado."""
    if im.size != (OUT_W, OUT_H):
        im = im.resize((OUT_W, OUT_H), Image.Resampling.LANCZOS)
    # Contraste muy leve + sharpen para texto/bordes nítidos
    im = ImageEnhance.Contrast(im).enhance(1.04)
    im = ImageEnhance.Sharpness(im).enhance(1.25)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=160, threshold=1))
    return im


def main() -> None:
    png_dir = B / "png"
    jpg_dir = B / "jpg"
    png_dir.mkdir(exist_ok=True)
    jpg_dir.mkdir(exist_ok=True)

    html = B / "carrusel.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--font-render-hinting=none",
                "--enable-font-antialiasing",
                            ]
        )
        page = browser.new_page(
            viewport={"width": CSS_W + 100, "height": CSS_H + 100},
            device_scale_factor=CAPTURE_DSF,
        )
        page.goto(html.as_uri(), wait_until="networkidle")
        page.evaluate(
            """async () => {
              await document.fonts.ready;
              const loads = [
                '800 78px Poppins',
                '700 64px Poppins',
                '700 32px Barlow Condensed',
                '500 32px Barlow Condensed',
                '600 22px IBM Plex Mono',
                '500 22px IBM Plex Mono',
                '600 18px IBM Plex Mono',
              ];
              await Promise.all(loads.map(f => document.fonts.load(f).catch(() => null)));
              await document.fonts.ready;
            }"""
        )
        page.wait_for_timeout(800)
        frames = page.query_selector_all(".slide")
        assert len(frames) == TOTAL, f"expected {TOTAL} slides, got {len(frames)}"

        for i, el in enumerate(frames, 1):
            raw_path = png_dir / f"slide-{i:02d}-raw.png"
            el.screenshot(path=str(raw_path), type="png", animations="disabled")
            im = Image.open(raw_path).convert("RGB")
            # Esperado ~3240x4050
            target_cap = (CSS_W * CAPTURE_DSF, CSS_H * CAPTURE_DSF)
            if im.size != target_cap:
                im = im.resize(target_cap, Image.Resampling.LANCZOS)
            im = finalize(im)

            out_png = png_dir / f"slide-{i:02d}.png"
            im.save(out_png, format="PNG", compress_level=1)

            # JPG retina (misma res) + JPG feed 1080
            im.save(
                jpg_dir / f"slide-{i:02d}@2x.jpg",
                format="JPEG",
                quality=95,
                subsampling=0,
                optimize=True,
            )
            feed = im.resize((CSS_W, CSS_H), Image.Resampling.LANCZOS)
            feed = ImageEnhance.Sharpness(feed).enhance(1.1)
            feed.save(
                jpg_dir / f"slide-{i:02d}.jpg",
                format="JPEG",
                quality=97,
                subsampling=0,
                optimize=True,
            )
            raw_path.unlink(missing_ok=True)
            print("OK", out_png.name, im.size, "bytes", out_png.stat().st_size)

        browser.close()


if __name__ == "__main__":
    main()
