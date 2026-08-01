# -*- coding: utf-8 -*-
"""Render 25 historias 1080×1920 → PNG retina 2160×3840."""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent


def main():
    index = json.loads((B / "stories_index.json").read_text(encoding="utf-8"))
    png_dir = B / "png"
    png_dir.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = br.new_page(
            viewport={"width": 1200, "height": 2200},
            device_scale_factor=2,
        )
        pg.goto((B / "historias.html").as_uri())
        pg.wait_for_function("document.fonts.ready")
        pg.wait_for_timeout(3500)
        slides = pg.query_selector_all(".slide")
        assert len(slides) == len(index), f"{len(slides)} vs {len(index)}"
        for meta, el in zip(index, slides):
            name = f"{meta['n']:02d}-{meta['tema']}-{meta['id']}.png"
            out = png_dir / name
            # ensure tema subfolder copy later; flat render first
            el.screenshot(path=str(out))
            print("OK", name)
        br.close()


if __name__ == "__main__":
    main()
