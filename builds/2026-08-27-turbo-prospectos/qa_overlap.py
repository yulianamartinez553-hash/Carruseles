# -*- coding: utf-8 -*-
"""QA geométrico: detecta solapamientos entre elementos visibles."""
from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
SEL = ".title,.lead,.meta,.graphic,.cta,.firma,.frame,.badge,.n,.tag"


def rects(slide, sel: str) -> list[dict]:
    return slide.evaluate(
        f"""(el) => {{
          const out = [];
          for (const node of el.querySelectorAll({sel!r})) {{
            const s = getComputedStyle(node);
            if (s.display === 'none' || s.visibility === 'hidden' || s.opacity === '0') continue;
            const r = node.getBoundingClientRect();
            if (r.width < 2 || r.height < 2) continue;
            const tag = node.className || node.tagName;
            const txt = (node.innerText || '').trim().slice(0, 40).replace(/\\n/g, ' ');
            out.push({{x:r.x,y:r.y,w:r.width,h:r.height,tag,txt}});
          }}
          return out;
        }}"""
    )


def overlap(a: dict, b: dict, pad: float = 2) -> bool:
    ax2, ay2 = a["x"] + a["w"], a["y"] + a["h"]
    bx2, by2 = b["x"] + b["w"], b["y"] + b["h"]
    return not (
        ax2 - pad <= b["x"] + pad
        or bx2 - pad <= a["x"] + pad
        or ay2 - pad <= b["y"] + pad
        or by2 - pad <= a["y"] + pad
    )


def contained(inner: dict, outer: dict, tol: float = 4) -> bool:
    return (
        inner["x"] >= outer["x"] - tol
        and inner["y"] >= outer["y"] - tol
        and inner["x"] + inner["w"] <= outer["x"] + outer["w"] + tol
        and inner["y"] + inner["h"] <= outer["y"] + outer["h"] + tol
    )


def main() -> None:
    html = B / "carrusel.html"
    issues: list[str] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        page = browser.new_page(viewport={"width": 1180, "height": 1600})
        page.goto(html.resolve().as_uri())
        page.wait_for_function("document.fonts.ready")
        page.wait_for_timeout(600)
        slides = page.query_selector_all(".slide")
        n = len(slides)
        for i, slide in enumerate(slides):
            rs = rects(slide, SEL)
            for a in range(len(rs)):
                for b in range(a + 1, len(rs)):
                    if not overlap(rs[a], rs[b]):
                        continue
                    if contained(rs[a], rs[b]) or contained(rs[b], rs[a]):
                        continue
                    if rs[a]["txt"] and rs[b]["txt"] and rs[a]["txt"] == rs[b]["txt"]:
                        continue
                    if "frame" in str(rs[a]["tag"]) or "frame" in str(rs[b]["tag"]):
                        continue
                    if "graphic" in str(rs[a]["tag"]) and "graphic" in str(rs[b]["tag"]):
                        continue
                    issues.append(
                        f"slide-{i+1:02d}: overlap {rs[a]['tag']}('{rs[a]['txt']}') "
                        f"<-> {rs[b]['tag']}('{rs[b]['txt']}')"
                    )
        browser.close()
    if issues:
        print("FAIL", len(issues), "overlaps")
        for line in issues[:40]:
            print(" ", line)
        raise SystemExit(1)
    print("OK no overlaps detected on", n, "slides")


if __name__ == "__main__":
    main()
