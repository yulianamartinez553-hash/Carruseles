# -*- coding: utf-8 -*-
from pathlib import Path
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
TOTAL = 6
CSS_W, CSS_H = 1080, 1920
DSF = 2  # 2160×3840
SAFE_TOP = 180
SAFE_BOTTOM = 1640


def qa_overlaps(page) -> None:
    stories = page.query_selector_all(".story")
    assert len(stories) == TOTAL, len(stories)
    for i, story in enumerate(stories, 1):
        nodes = story.query_selector_all(".brand, .kicker, .claim, .apoyo, .hint, .kw, .firma, .rule")
        boxes = []
        for el in nodes:
            box = el.bounding_box()
            if not box or box["width"] < 2 or box["height"] < 2:
                continue
            text = (el.inner_text() or "").strip()
            boxes.append((el, box, text[:40]))
        for a, ba, ta in boxes:
            y1, y2 = ba["y"], ba["y"] + ba["height"]
            # coordenadas relativas al story
            sb = story.bounding_box()
            rel_top = ba["y"] - sb["y"]
            rel_bot = rel_top + ba["height"]
            if rel_top < SAFE_TOP - 4:
                raise SystemExit(f"QA story {i}: '{ta}' entra en UI superior ({rel_top:.0f}px)")
            if rel_bot > SAFE_BOTTOM + 4:
                raise SystemExit(f"QA story {i}: '{ta}' entra en UI inferior ({rel_bot:.0f}px)")
        for j, (a, ba, ta) in enumerate(boxes):
            for k, (b, bb, tb) in enumerate(boxes):
                if k <= j:
                    continue
                # firma vs resto: no solapar
                ax2, ay2 = ba["x"] + ba["width"], ba["y"] + ba["height"]
                bx2, by2 = bb["x"] + bb["width"], bb["y"] + bb["height"]
                ox = min(ax2, bx2) - max(ba["x"], bb["x"])
                oy = min(ay2, by2) - max(ba["y"], bb["y"])
                if ox > 4 and oy > 4:
                    raise SystemExit(f"QA story {i}: overlap '{ta}' × '{tb}' ({ox:.0f}×{oy:.0f})")
        print(f"QA ok {i:02d}")


def main():
    png_dir = B / "png-retina"
    jpg_dir = B / "jpg"
    png1080 = B / "png-1080"
    png_dir.mkdir(exist_ok=True)
    jpg_dir.mkdir(exist_ok=True)
    png1080.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = br.new_page(
            viewport={"width": 1180, "height": 2020},
            device_scale_factor=DSF,
        )
        pg.goto((B / "historias.html").as_uri())
        pg.wait_for_function("document.fonts.ready")
        pg.evaluate(
            """async () => {
              await Promise.all([
                document.fonts.load("400 128px Bebas Neue"),
                document.fonts.load("italic 600 88px Lora"),
                document.fonts.load("500 36px Barlow Condensed"),
                document.fonts.load("500 22px IBM Plex Mono"),
              ]);
            }"""
        )
        pg.wait_for_timeout(2500)
        qa_overlaps(pg)
        frames = pg.query_selector_all(".story")
        assert len(frames) == TOTAL, len(frames)
        for i, el in enumerate(frames, 1):
            raw = png_dir / f"historia-{i:02d}-raw.png"
            el.screenshot(path=str(raw), type="png", animations="disabled")
            im = Image.open(raw).convert("RGB")
            target = (CSS_W * DSF, CSS_H * DSF)
            if im.size != target:
                im = im.resize(target, Image.Resampling.LANCZOS)
            im = im.filter(ImageFilter.UnsharpMask(radius=0.8, percent=110, threshold=2))
            out = png_dir / f"historia-{i:02d}.png"
            im.save(out, format="PNG", compress_level=1)
            ig = im.resize((CSS_W, CSS_H), Image.Resampling.LANCZOS)
            ig.save(png1080 / f"historia-{i:02d}.png", format="PNG", compress_level=1)
            ig.save(
                jpg_dir / f"historia-{i:02d}.jpg",
                format="JPEG",
                quality=96,
                subsampling=0,
                optimize=True,
            )
            raw.unlink(missing_ok=True)
            print("OK", out.name, im.size)
        br.close()


if __name__ == "__main__":
    main()
