# -*- coding: utf-8 -*-
"""Publicación única STLabs — foto familiar + manifiesto meta."""
from __future__ import annotations

import base64
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
B = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from stlabs_kit import BLANCO, NEG, VERDE, embedded_fonts_css, write_html

PHOTO = B / "assets" / "familia.jpg"
PHOTO_URI = (
    f"data:image/jpeg;base64,{base64.b64encode(PHOTO.read_bytes()).decode()}"
)

EXTRA_CSS = f"""
.slide.pub{{
  background:{NEG};
}}
.slide.pub::before{{
  content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(70% 45% at 50% 18%, rgba(0,255,178,.06), transparent 62%),
    radial-gradient(55% 40% at 80% 92%, rgba(0,255,178,.04), transparent 60%);
}}
.photo-wrap{{
  position:absolute;inset:0;
  z-index:1;overflow:hidden;
}}
.photo-wrap img{{
  position:absolute;inset:0;
  width:100%;height:100%;
  object-fit:cover;object-position:46% 32%;
  filter:brightness(.95) contrast(1.05) saturate(.96);
}}
.photo-fade{{
  position:absolute;inset:0;z-index:2;pointer-events:none;
  background:
    linear-gradient(180deg,
      rgba(10,10,10,.08) 0%,
      rgba(10,10,10,.0) 18%,
      rgba(10,10,10,.05) 40%,
      rgba(10,10,10,.38) 55%,
      rgba(10,10,10,.78) 70%,
      rgba(10,10,10,.94) 84%,
      {NEG} 100%),
    linear-gradient(90deg,
      rgba(10,10,10,.22) 0%,
      transparent 9%,
      transparent 91%,
      rgba(10,10,10,.22) 100%);
}}
.copy{{
  position:absolute;left:44px;right:44px;bottom:128px;
  z-index:5;text-align:center;
}}
.line{{
  font-family:var(--disp);font-weight:400;
  letter-spacing:1.5px;line-height:.9;
  text-transform:uppercase;
  text-shadow:0 2px 22px rgba(0,0,0,.65);
}}
.l1{{font-size:58px;color:{BLANCO};margin-bottom:8px;}}
.l2{{font-size:76px;color:{VERDE};margin-bottom:6px;}}
.l3{{font-size:60px;color:{BLANCO};margin-bottom:28px;}}
.l4{{font-size:56px;color:{VERDE};margin-bottom:6px;}}
.l5{{font-size:56px;color:{BLANCO};margin-bottom:6px;}}
.l6{{font-size:54px;color:{VERDE};margin-bottom:6px;}}
.l7{{font-size:50px;color:{BLANCO};line-height:.94;}}
.spark{{
  position:absolute;right:52px;bottom:52px;z-index:6;
  width:14px;height:14px;opacity:.55;
  background:{VERDE};
  clip-path:polygon(50% 0%,61% 35%,100% 50%,61% 65%,50% 100%,39% 65%,0% 50%,39% 35%);
}}
.web{{
  bottom:52px;font-size:22px;letter-spacing:2px;opacity:.92;
}}
"""


def slide_html() -> str:
    return f"""
<section class="slide pub">
  <div class="photo-wrap">
    <img src="{PHOTO_URI}" alt="Familia">
    <div class="photo-fade"></div>
  </div>
  <div class="copy">
    <div class="line l1">LA META DE</div>
    <div class="line l2">TENER UNA EMPRESA</div>
    <div class="line l3">NO ERA SER MILLONARIO</div>
    <div class="line l4">ERA TENER TIEMPO</div>
    <div class="line l5">PARA ESTAR CON ELLAS</div>
    <div class="line l6">CUANDO ME NECESITEN..</div>
    <div class="line l7">SIN TENER QUE PEDIR PERMISO.</div>
  </div>
  <div class="web">sebastian.stlabs.ar</div>
  <span class="spark"></span>
</section>
"""


def main() -> Path:
    out = B / "carrusel.html"
    # write_html adds BASE_CSS; inject fonts separately for package
    html = (
        f"<!DOCTYPE html><html lang=\"es\"><head><meta charset=\"UTF-8\">"
        f"<style>{embedded_fonts_css()}"
        f"{__import__('stlabs_kit').full_css(EXTRA_CSS)}</style></head>"
        f"<body><div class=\"sheet\">{slide_html()}</div></body></html>"
    )
    out.write_text(html, encoding="utf-8")
    print("OK", out)
    return out


if __name__ == "__main__":
    main()
