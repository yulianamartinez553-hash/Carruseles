# -*- coding: utf-8 -*-
"""Render 4K HQ sin deformar: captura nativa 4x (4320×5400).

- Base CSS: 1080×1350 (4:5 exacto)
- Captura deviceScaleFactor=4 → 4320×5400 (entero, sin stretch)
- PNG master 4K en png/
- Derivados 2x (2160×2700) y JPG feed sin re-escalar raro
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageFilter, ImageEnhance
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
TOTAL = 10
CSS_W, CSS_H = 1080, 1350
DSF = 4  # 4320×5400 master
MASTER_W, MASTER_H = CSS_W * DSF, CSS_H * DSF  # 4320×5400
RETINA_W, RETINA_H = CSS_W * 2, CSS_H * 2  # 2160×2700


def light_polish(im: Image.Image) -> Image.Image:
    """Nitidez suave — sin unsharp agresivo que deforma/bordea."""
    im = ImageEnhance.Contrast(im).enhance(1.02)
    im = ImageEnhance.Sharpness(im).enhance(1.08)
    return im


def downscale(im: Image.Image, size: tuple[int, int]) -> Image.Image:
    out = im.resize(size, Image.Resampling.LANCZOS)
    return light_polish(out)


def main() -> None:
    png_dir = B / "png"
    jpg_dir = B / "jpg"
    png4k = B / "png-4k"
    png_dir.mkdir(exist_ok=True)
    jpg_dir.mkdir(exist_ok=True)
    png4k.mkdir(exist_ok=True)

    html = next(B.glob("*.html"))

    with sync_playwright() as p:
        browser = p.chromium.launch(
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--font-render-hinting=none",
                "--enable-font-antialiasing",
                "--disable-lcd-text",
            ]
        )
        # Viewport exacto al slide: evita letterbox / crop raro
        page = browser.new_page(
            viewport={"width": CSS_W, "height": CSS_H},
            device_scale_factor=DSF,
        )
        page.goto(html.resolve().as_uri(), wait_until="networkidle")
        page.evaluate(
            """async () => {
              await document.fonts.ready;
              const faces = [
                '800 78px Poppins',
                '700 64px Poppins',
                '700 32px Barlow Condensed',
                '500 32px Barlow Condensed',
                '600 22px IBM Plex Mono',
                '500 22px IBM Plex Mono',
              ];
              await Promise.all(faces.map(f => document.fonts.load(f).catch(() => null)));
              await document.fonts.ready;
              // Forzar layout estable
              document.body.style.zoom = '1';
            }"""
        )
        page.wait_for_timeout(1200)

        slides = page.query_selector_all(".slide")
        assert len(slides) == TOTAL, f"slides={len(slides)}"

        for i, el in enumerate(slides, 1):
            # Verificar caja CSS exacta
            box = el.bounding_box()
            assert box is not None
            assert abs(box["width"] - CSS_W) < 1 and abs(box["height"] - CSS_H) < 1, box

            raw = png4k / f"slide-{i:02d}-raw.png"
            el.screenshot(path=str(raw), type="png", animations="disabled", scale="device")

            im = Image.open(raw).convert("RGB")
            # Debe ser exactamente 4320×5400 — si no, NO estirar: recortar/pad centrado
            if im.size != (MASTER_W, MASTER_H):
                canvas = Image.new("RGB", (MASTER_W, MASTER_H), (10, 10, 10))
                # scale uniformly to fit (never stretch)
                sx = MASTER_W / im.size[0]
                sy = MASTER_H / im.size[1]
                s = min(sx, sy)
                nw, nh = int(im.size[0] * s), int(im.size[1] * s)
                tmp = im.resize((nw, nh), Image.Resampling.LANCZOS)
                canvas.paste(tmp, ((MASTER_W - nw) // 2, (MASTER_H - nh) // 2))
                im = canvas
                print("WARN resized uniformly", i, "from", Image.open(raw).size)
            else:
                im = light_polish(im)

            # Master 4K
            master_path = png4k / f"slide-{i:02d}.png"
            im.save(master_path, format="PNG", compress_level=1)

            # Entrega estándar retina 2x (desde master, LANCZOS limpio)
            retina = downscale(im, (RETINA_W, RETINA_H))
            retina.save(png_dir / f"slide-{i:02d}.png", format="PNG", compress_level=1)

            # JPG 4K + retina + feed
            im.save(
                jpg_dir / f"slide-{i:02d}@4k.jpg",
                format="JPEG",
                quality=96,
                subsampling=0,
                optimize=True,
            )
            retina.save(
                jpg_dir / f"slide-{i:02d}@2x.jpg",
                format="JPEG",
                quality=96,
                subsampling=0,
                optimize=True,
            )
            feed = downscale(im, (CSS_W, CSS_H))
            feed.save(
                jpg_dir / f"slide-{i:02d}.jpg",
                format="JPEG",
                quality=98,
                subsampling=0,
                optimize=True,
            )

            raw.unlink(missing_ok=True)
            print(
                "OK",
                f"slide-{i:02d}",
                "4K",
                im.size,
                "2x",
                retina.size,
                "MB",
                round(master_path.stat().st_size / 1e6, 2),
            )

        browser.close()


if __name__ == "__main__":
    main()
