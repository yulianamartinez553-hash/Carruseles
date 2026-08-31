# -*- coding: utf-8 -*-
"""Render íconos Highlight 1080×1080 → PNG retina 2160×2160."""
from pathlib import Path
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
NAMES = ["resultados", "proceso", "clientes", "servicios", "contacto"]


def main():
    png_dir = B / "png"
    png_dir.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = br.new_page(
            viewport={"width": 1200, "height": 6200},
            device_scale_factor=2,
        )
        pg.goto((B / "highlights.html").as_uri())
        pg.wait_for_function("document.fonts.ready")
        pg.wait_for_timeout(3000)
        slides = pg.query_selector_all(".slide")
        assert len(slides) == 5, f"expected 5 slides, got {len(slides)}"
        for i, el in enumerate(slides):
            name = NAMES[i]
            out = png_dir / f"highlight-{i+1:02d}-{name}.png"
            el.screenshot(path=str(out))
            print("OK", out.name)
        br.close()


if __name__ == "__main__":
    main()
