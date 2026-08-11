# -*- coding: utf-8 -*-
"""
Carrusel panorámico continuo STLabs — SOLO fondo gráfico (sin copy).
Un único mundo visual de 5×1080px; cada slide es una ventana sobre esa continuidad.

Fondo: reticula_fina · Familia: dossier_editorial
Único texto: sebastian.stlabs.ar · acento #00FFB2
"""
from __future__ import annotations

import base64
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from stlabs_kit import embedded_fonts_css

N = 5
W = 1080
H = 1350
PANO_W = N * W


def b64(path: Path, mime: str) -> str:
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


URI_MON = b64(REPO / "assets" / "slide1-hero.png", "image/png")
URI_SEB = b64(REPO / "seb.jpg", "image/jpeg")

EXTRA_CSS = f"""
:root{{
  --verde:#00FFB2;
  --neg:#0A0A0A;
  --mono:'IBM Plex Mono',monospace;
}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;}}
body{{background:#000;}}
.sheet{{display:flex;flex-direction:column;gap:40px;padding:40px;background:#000;}}
.slide{{
  position:relative;width:{W}px;height:{H}px;overflow:hidden;
  background:var(--neg);color:#F2F2F2;
}}

.pano{{
  position:absolute;top:0;left:0;width:{PANO_W}px;height:{H}px;z-index:1;
  pointer-events:none;
}}
.s1 .pano{{transform:translateX(0);}}
.s2 .pano{{transform:translateX(-{W}px);}}
.s3 .pano{{transform:translateX(-{2*W}px);}}
.s4 .pano{{transform:translateX(-{3*W}px);}}
.s5 .pano{{transform:translateX(-{4*W}px);}}

/* ── Base mineral continua ── */
.pano-base{{
  position:absolute;inset:0;
  background:
    radial-gradient(36% 42% at 18% 22%, rgba(0,255,178,.09), transparent 62%),
    radial-gradient(40% 36% at 72% 78%, rgba(0,255,178,.06), transparent 65%),
    radial-gradient(50% 50% at 48% 48%, #121212, transparent 70%),
    linear-gradient(112deg, #0c0c0c 0%, #080808 42%, #0b0b0b 68%, #0a0a0a 100%);
}}
.pano-grid{{
  position:absolute;inset:0;opacity:.55;z-index:1;
  background-image:
    linear-gradient(rgba(255,255,255,.022) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.022) 1px, transparent 1px);
  background-size:60px 60px;
}}
.pano-noise{{
  position:absolute;inset:0;opacity:.4;mix-blend-mode:overlay;z-index:1;pointer-events:none;
  background:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.5'/%3E%3C/svg%3E");
}}

/* Bandas de luz arquitectónica — continúan en diagonal */
.shadow-band{{
  position:absolute;height:380px;width:170%;left:-12%;z-index:2;
  background:linear-gradient(180deg, rgba(255,255,255,.035), rgba(255,255,255,.01) 50%, transparent);
  transform-origin:left center;
}}
.sb-a{{top:60px;transform:rotate(-16deg);}}
.sb-b{{top:480px;transform:rotate(-16deg);opacity:.7;}}
.sb-c{{top:920px;transform:rotate(-16deg);opacity:.45;}}

/* Haz volumétrico verde paralelo a la diagonal */
.beam{{
  position:absolute;left:-220px;top:40px;width:5900px;height:220px;z-index:2;
  background:linear-gradient(180deg,
    rgba(0,255,178,0),
    rgba(0,255,178,.10) 42%,
    rgba(0,255,178,.03) 72%,
    transparent);
  transform:rotate(12.6deg);transform-origin:left center;
  filter:blur(22px);
}}

/* ── DIAGONAL MAESTRA (atraviesa los 5 slides) ── */
.diag-master{{
  position:absolute;left:-100px;top:150px;width:5650px;height:5px;z-index:8;
  background:linear-gradient(90deg,
    rgba(0,255,178,0) 0%,
    rgba(0,255,178,.45) 3%,
    #00FFB2 10%,
    #00FFB2 90%,
    rgba(0,255,178,.4) 97%,
    rgba(0,255,178,0) 100%);
  transform:rotate(12.6deg);transform-origin:left center;
  box-shadow:0 0 26px rgba(0,255,178,.55), 0 0 2px rgba(0,255,178,.95);
  border-radius:3px;
}}
.diag-thin{{
  position:absolute;left:-60px;top:220px;width:5600px;height:1.5px;z-index:8;
  background:linear-gradient(90deg,
    transparent,
    rgba(0,255,178,.5) 8%,
    rgba(0,255,178,.75) 50%,
    rgba(0,255,178,.4) 92%,
    transparent);
  transform:rotate(12.6deg);transform-origin:left center;
}}
.diag-ghost{{
  position:absolute;left:80px;top:70px;width:5450px;height:1px;z-index:7;
  background:linear-gradient(90deg, transparent, rgba(255,255,255,.12) 18%, rgba(255,255,255,.16) 70%, transparent);
  transform:rotate(12.6deg);transform-origin:left center;
}}

/* Cable fino continuo */
.cable{{
  position:absolute;left:160px;top:1090px;width:5100px;height:1.5px;z-index:7;
  background:linear-gradient(90deg, transparent, rgba(255,255,255,.22) 8%, rgba(0,255,178,.35) 48%, rgba(255,255,255,.18) 90%, transparent);
  transform:rotate(-2.8deg);transform-origin:left center;
}}

/* Rail metálico inferior continuo */
.metal-rail{{
  position:absolute;left:20px;top:1195px;width:5360px;height:12px;z-index:9;
  background:linear-gradient(180deg,#5a5e64 0%,#22252a 32%,#0a0b0c 58%,#3a3e44 100%);
  box-shadow:0 10px 28px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.28);
  border-radius:2px;
}}
.metal-rail::after{{
  content:'';position:absolute;left:0;right:0;top:3px;height:2px;
  background:linear-gradient(90deg, transparent 0%, rgba(0,255,178,.65) 18%, rgba(0,255,178,.2) 58%, transparent 100%);
}}
.ticks{{position:absolute;left:60px;top:1176px;width:5280px;height:12px;z-index:10;display:flex;gap:46px;}}
.ticks i{{display:block;width:2px;height:10px;background:rgba(255,255,255,.22);}}
.ticks i:nth-child(5n){{background:#00FFB2;height:14px;box-shadow:0 0 8px rgba(0,255,178,.55);}}

/* Nodos sobre la diagonal */
.anchor{{
  position:absolute;width:16px;height:16px;border-radius:50%;z-index:11;
  background:#0A0A0A;border:2px solid #00FFB2;
  box-shadow:0 0 18px rgba(0,255,178,.65);
}}
.a1{{left:900px;top:368px;}}
.a2{{left:1960px;top:605px;}}
.a3{{left:3020px;top:842px;}}
.a4{{left:4100px;top:1082px;}}

/* Planos de vidrio oscuro */
.glass{{
  position:absolute;border-radius:16px;z-index:6;overflow:hidden;
  background:linear-gradient(145deg, rgba(255,255,255,.09), rgba(255,255,255,.02) 38%, rgba(0,255,178,.04));
  border:1px solid rgba(255,255,255,.12);
  box-shadow:0 28px 60px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.18);
}}
.glass::before{{
  content:'';position:absolute;inset:0;
  background:linear-gradient(118deg, rgba(255,255,255,.16) 0%, transparent 26%, transparent 70%, rgba(0,255,178,.10) 100%);
}}
.g1{{left:60px;top:160px;width:400px;height:520px;transform:rotate(-7deg);}}
.g2{{left:1240px;top:70px;width:300px;height:240px;transform:rotate(5deg);}}
.g3{{left:2280px;top:140px;width:280px;height:380px;transform:rotate(-3deg);}}
.g4{{left:4560px;top:200px;width:360px;height:480px;transform:rotate(6deg);}}
.g5{{left:3280px;top:180px;width:520px;height:640px;transform:rotate(-4deg);}}
.g6{{left:3880px;top:620px;width:340px;height:280px;transform:rotate(7deg);}}
.g7{{left:4480px;top:720px;width:420px;height:300px;transform:rotate(-5deg);}}

/* Placas metálicas */
.plate{{
  position:absolute;z-index:6;border-radius:10px;
  background:linear-gradient(160deg,#4a4e54 0%,#1b1d20 40%,#0b0c0e 70%,#2a2e33 100%);
  box-shadow:0 24px 48px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.25);
}}
.p1{{left:480px;top:880px;width:250px;height:150px;transform:rotate(11deg);}}
.p2{{left:3360px;top:150px;width:210px;height:130px;transform:rotate(-12deg);}}
.p3{{left:4880px;top:980px;width:270px;height:110px;transform:rotate(3deg);}}
.p4{{left:3420px;top:920px;width:280px;height:140px;transform:rotate(-8deg);}}
.p5{{left:5100px;top:180px;width:240px;height:160px;transform:rotate(10deg);}}
.plate .edge{{
  position:absolute;left:12px;right:12px;top:14px;height:3px;border-radius:2px;
  background:linear-gradient(90deg, #00FFB2, rgba(0,255,178,.12));
  box-shadow:0 0 12px rgba(0,255,178,.5);
}}

/* Bloques geométricos */
.block{{position:absolute;z-index:5;}}
.b1{{
  left:160px;top:1000px;width:150px;height:150px;transform:skewY(-8deg);
  background:linear-gradient(135deg,#2e3238,#121416);
  box-shadow:16px 20px 0 rgba(0,255,178,.08), 0 28px 48px rgba(0,0,0,.5);
}}
.b2{{
  left:2140px;top:980px;width:110px;height:190px;transform:skewY(-8deg);
  background:linear-gradient(135deg,#1a1d22,#070809);
  box-shadow:14px 18px 0 rgba(255,255,255,.04), 0 28px 48px rgba(0,0,0,.55);
}}
.b3{{
  left:4280px;top:100px;width:86px;height:86px;transform:rotate(18deg);
  background:linear-gradient(135deg,#00FFB2,#009e6e);
  box-shadow:0 18px 40px rgba(0,255,178,.4);
}}

/* Anillos */
.ring{{
  position:absolute;border-radius:50%;border:1.5px solid rgba(0,255,178,.35);z-index:5;
  box-shadow:inset 0 0 40px rgba(0,255,178,.04);
}}
.r1{{left:620px;top:400px;width:260px;height:260px;}}
.r2{{left:1640px;top:700px;width:400px;height:400px;border-color:rgba(255,255,255,.08);}}
.r3{{left:3860px;top:460px;width:320px;height:320px;}}
.r4{{left:4700px;top:380px;width:280px;height:280px;border-color:rgba(255,255,255,.1);}}

/* ── Objeto monitor (completo, sin partir UI) — zona slides 1→2 ── */
.obj-monitor{{
  position:absolute;left:760px;top:220px;width:1100px;height:1100px;z-index:12;
  filter:drop-shadow(0 50px 80px rgba(0,0,0,.75));
}}
.obj-monitor img{{
  width:100%;height:100%;object-fit:contain;object-position:center;
}}

/* Retrato — puente visual slide 3 */
.obj-portrait{{
  position:absolute;left:2720px;top:620px;width:240px;height:240px;z-index:13;
  border-radius:50%;overflow:hidden;
  border:3px solid #00FFB2;
  box-shadow:0 0 0 10px rgba(0,255,178,.08), 0 28px 56px rgba(0,0,0,.55), 0 0 36px rgba(0,255,178,.4);
}}
.obj-portrait img{{width:100%;height:100%;object-fit:cover;filter:grayscale(.2) contrast(1.06) brightness(.92);}}

/* Fragmento fotográfico solo en zona inicial (slides 1–2) */
.chip{{
  position:absolute;z-index:11;border-radius:12px;overflow:hidden;
  border:1px solid rgba(255,255,255,.14);
  box-shadow:0 20px 40px rgba(0,0,0,.5);
}}
.chip img{{width:100%;height:100%;object-fit:cover;filter:brightness(.55) contrast(1.08) saturate(.7);}}
.chip-a{{left:200px;top:640px;width:180px;height:220px;transform:rotate(-6deg);}}

/* Orbes de luz */
.orb{{
  position:absolute;border-radius:50%;z-index:4;filter:blur(40px);
  background:radial-gradient(circle, rgba(0,255,178,.35), transparent 70%);
}}
.o1{{left:700px;top:180px;width:220px;height:220px;}}
.o2{{left:2500px;top:900px;width:280px;height:280px;opacity:.7;}}
.o3{{left:4700px;top:300px;width:260px;height:260px;}}

/* Firma — único texto */
.web{{
  position:absolute;left:0;right:0;bottom:70px;text-align:center;z-index:30;
  font-family:var(--mono);font-size:25px;letter-spacing:2px;color:#00FFB2;
  text-shadow:0 0 20px rgba(0,255,178,.35);
  opacity:.95;
}}
"""


def pano_html() -> str:
    ticks = "".join("<i></i>" for _ in range(108))
    return f"""
<div class="pano-base"></div>
<div class="pano-grid"></div>
<div class="pano-noise"></div>
<div class="shadow-band sb-a"></div>
<div class="shadow-band sb-b"></div>
<div class="shadow-band sb-c"></div>
<div class="beam"></div>
<div class="orb o1"></div>
<div class="orb o2"></div>
<div class="orb o3"></div>
<div class="diag-ghost"></div>
<div class="diag-master"></div>
<div class="diag-thin"></div>
<div class="cable"></div>
<div class="metal-rail"></div>
<div class="ticks">{ticks}</div>

<span class="anchor a1"></span>
<span class="anchor a2"></span>
<span class="anchor a3"></span>
<span class="anchor a4"></span>

<div class="glass g1"></div>
<div class="glass g2"></div>
<div class="glass g3"></div>
<div class="glass g4"></div>
<div class="glass g5"></div>
<div class="glass g6"></div>
<div class="glass g7"></div>

<div class="plate p1"><span class="edge"></span></div>
<div class="plate p2"><span class="edge"></span></div>
<div class="plate p3"><span class="edge"></span></div>
<div class="plate p4"><span class="edge"></span></div>
<div class="plate p5"><span class="edge"></span></div>

<div class="block b1"></div>
<div class="block b2"></div>
<div class="block b3"></div>
<div class="block b4"></div>
<div class="block b5"></div>

<div class="ring r1"></div>
<div class="ring r2"></div>
<div class="ring r3"></div>
<div class="ring r4"></div>

<div class="chip chip-a"><img src="{URI_SEB}" alt=""></div>

<div class="obj-monitor"><img src="{URI_MON}" alt=""></div>
<div class="obj-portrait"><img src="{URI_SEB}" alt=""></div>
"""


def slide(idx: int) -> str:
    return (
        f'<section class="slide s{idx}">'
        f'<div class="pano">{pano_html()}</div>'
        f'<div class="web">sebastian.stlabs.ar</div>'
        f"</section>"
    )


def main():
    slides = [slide(i) for i in range(1, N + 1)]
    html = (
        '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">'
        f"<style>{embedded_fonts_css()}{EXTRA_CSS}</style></head>"
        f'<body><div class="sheet">{"".join(slides)}</div></body></html>'
    )
    out = BUILD / "carrusel.html"
    out.write_text(html, encoding="utf-8")
    print(f"✓ HTML escrito: {out} ({out.stat().st_size // 1024} KB)")
    return out


if __name__ == "__main__":
    main()
