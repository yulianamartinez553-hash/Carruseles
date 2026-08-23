# -*- coding: utf-8 -*-
"""QA geométrico: detecta solapamientos entre elementos visibles."""
from __future__ import annotations
from pathlib import Path
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
SEL = (
    ".title,.sub,.body,.meta,.box,.card,.pane,.memo,.memo-row,.dec,.cta-frame,"
    ".cta-kw,.hub-core,.node,.status,.sbox,.firma,.ruler,.tag,.flow6 .f,.gear-box,.pat"
)


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


def main() -> None:
    html = next(B.glob("carrusel.html"))
    issues: list[str] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        page = browser.new_page(viewport={"width": 1080, "height": 1350})
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
                    # ignorar contenedor/padre aproximado
                    if rs[a]["txt"] and rs[b]["txt"] and rs[a]["txt"] == rs[b]["txt"]:
                        continue
                    issues.append(
                        f"slide-{i+1:02d}: overlap {rs[a]['tag']}('{rs[a]['txt']}') "
                        f"<-> {rs[b]['tag']}('{rs[b]['txt']}')"
                    )
        browser.close()
    if issues:
        print("FAIL", len(issues), "overlaps")
        for line in issues[:30]:
            print(" ", line)
        raise SystemExit(1)
    print("OK no overlaps detected on", n, "slides")


if __name__ == "__main__":
    main()
