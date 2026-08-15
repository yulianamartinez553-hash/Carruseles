# -*- coding: utf-8 -*-
"""Clon STLabs — 3 pasos para no perder ningún lead
Modo: NEGRO · Fondo: lino_tela + grilla verde · Familia: blueprint
Portada sin imagen · Slide 6 mantiene foto de Sebastián.
"""
from pathlib import Path
import base64
import json

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")
ASSETS = B / "assets"


def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


IMG6 = b64(ASSETS / "slide6-hero.png")


def chrome_top(badge="SOLUCIÓN"):
    return f'''
    <div class="topbar">
      <div class="brand"><span class="star">✦</span> Sebastián García · RevOps</div>
      <div class="badge">{badge}</div>
    </div>'''


def chrome_foot(topic="3 pasos para no perder ningún lead"):
    return f'''
    <div class="footbar">
      <div class="foot-url">sebastian.stlabs.ar</div>
      <div class="foot-topic">{topic}</div>
    </div>'''


ICON_MAIL = '''<svg class="ico" viewBox="0 0 64 64" aria-hidden="true"><rect x="6" y="14" width="52" height="36" rx="6" fill="none" stroke="#00FFB2" stroke-width="3.5"/><path d="M8 18 L32 36 L56 18" fill="none" stroke="#00FFB2" stroke-width="3.5" stroke-linejoin="round"/></svg>'''
ICON_CLOCK = '''<svg class="ico" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="24" fill="none" stroke="#00FFB2" stroke-width="3.5"/><path d="M32 18 V34 L44 40" fill="none" stroke="#00FFB2" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
ICON_CHECK = '''<svg class="ico ico-fill" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="26" fill="#00FFB2"/><path d="M20 33 L29 42 L46 24" fill="none" stroke="#04130b" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'''


def slide_portada():
    return f'''
    <section class="slide s-cover" data-id="portada">
      <div class="gridbg"></div>
      <div class="linen"></div>
      {chrome_top("SOLUCIÓN")}
      <div class="mid mid-cover">
        <p class="kicker">KEYWORD · LEAD</p>
        <h1 class="cover-title">3 pasos para<br>no perder<br><span class="gr">ningún lead.</span></h1>
        <p class="cover-sub">Tu problema no es conseguir más.<br>Es dejar de enfriar los que ya llegan.</p>
      </div>
      {chrome_foot()}
    </section>'''


def slide_problema():
    return f'''
    <section class="slide" data-id="problema">
      <div class="gridbg"></div>
      <div class="linen"></div>
      {chrome_top("SOLUCIÓN")}
      <div class="mid mid-problem">
        <p class="eyebrow">El error de siempre</p>
        <h1 class="h-big">El lead llega…<br><span class="strike">y lo respondés tarde.</span></h1>
        <p class="punch">Y se enfría solo.</p>
      </div>
      {chrome_foot()}
    </section>'''


def slide_paso(n, icon, title, body, bold_tail=""):
    body_html = body
    if bold_tail:
        body_html = f'{body} <b>{bold_tail}</b>'
    return f'''
    <section class="slide" data-id="paso{n}">
      <div class="gridbg"></div>
      <div class="linen"></div>
      {chrome_top("SOLUCIÓN")}
      <div class="mid mid-step">
        <div class="step-row">
          <div class="step-num">{n}</div>
          {icon}
          <div class="step-lab">Paso {n}</div>
        </div>
        <h1 class="h-step">{title}</h1>
        <p class="body-step">{body_html}</p>
      </div>
      {chrome_foot()}
    </section>'''


def slide_cambia():
    return f'''
    <section class="slide s-photo" data-id="cambia">
      <img class="ph" src="data:image/png;base64,{IMG6}" alt="">
      <div class="ph-wash"></div>
      <div class="gridbg gridbg-photo"></div>
      {chrome_top("SOLUCIÓN")}
      <div class="mid mid-photo">
        <p class="script">Lo que cambia</p>
        <h1 class="h-photo">No necesitás<br>más leads.</h1>
        <p class="h-photo-sub">Necesitás <span class="script-inline">dejar de perder<br>los que ya tenés.</span></p>
      </div>
      {chrome_foot()}
    </section>'''


def slide_cta():
    return f'''
    <section class="slide" data-id="cta">
      <div class="gridbg"></div>
      <div class="linen"></div>
      {chrome_top("SOLUCIÓN")}
      <div class="mid mid-cta">
        <p class="eyebrow">A un mensaje de distancia</p>
        <h1 class="h-cta">¿Te paso la plantilla<br>de seguimiento<br>que usamos?</h1>
        <div class="cta-row">
          <div class="cta-box">PLANTILLA</div>
          <div class="cta-hint"><span class="arrow">←</span> comentá esto</div>
        </div>
        <p class="cta-line">Comentá <b>PLANTILLA</b> en este posteo y te la paso.</p>
      </div>
      {chrome_foot()}
    </section>'''


CSS = f"""
@font-face {{ font-family:'Poppins'; src:url('file://{FONTS}/Poppins-ExtraBold.ttf') format('truetype'); font-weight:800; }}
@font-face {{ font-family:'Poppins'; src:url('file://{FONTS}/Poppins-Bold.ttf') format('truetype'); font-weight:700; }}
@font-face {{ font-family:'Lora'; src:url('file://{FONTS}/Lora-Italic-Variable.ttf') format('truetype'); font-style:italic; font-weight:400 700; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{FONTS}/IBMPlexMono-Medium.ttf') format('truetype'); font-weight:500; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{FONTS}/IBMPlexMono-SemiBold.ttf') format('truetype'); font-weight:600; }}
@font-face {{ font-family:'Barlow Condensed'; src:url('file://{FONTS}/BarlowCondensed-Medium.ttf') format('truetype'); font-weight:500; }}
@font-face {{ font-family:'Barlow Condensed'; src:url('file://{FONTS}/BarlowCondensed-SemiBold.ttf') format('truetype'); font-weight:600; }}
@font-face {{ font-family:'Barlow Condensed'; src:url('file://{FONTS}/BarlowCondensed-Bold.ttf') format('truetype'); font-weight:700; }}

* {{ box-sizing:border-box; margin:0; padding:0; -webkit-font-smoothing:antialiased; }}
html, body {{ background:#000; }}
.sheet {{ display:flex; flex-direction:column; gap:48px; padding:40px; width:max-content; }}

.slide {{
  position:relative; width:1080px; height:1350px; overflow:hidden;
  background:#0A0A0A; color:#F2F2F2;
}}
.gridbg {{
  position:absolute; inset:0; z-index:0; pointer-events:none;
  background-image:
    linear-gradient(rgba(0,255,178,.28) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.28) 1px, transparent 1px);
  background-size:44px 44px;
  opacity:1;
}}
.linen {{
  position:absolute; inset:0; z-index:0; pointer-events:none; opacity:.35;
  background:
    repeating-linear-gradient(0deg, rgba(255,255,255,.03) 0 1px, transparent 1px 3px),
    repeating-linear-gradient(90deg, rgba(255,255,255,.02) 0 1px, transparent 1px 4px);
}}

.topbar {{
  position:absolute; left:64px; right:64px; top:52px; z-index:5;
  display:flex; align-items:center; justify-content:space-between;
}}
.brand {{
  font-family:'Barlow Condensed', sans-serif; font-weight:600; font-size:28px;
  color:#F2F2F2; letter-spacing:.02em; display:flex; align-items:center; gap:10px;
}}
.star {{ color:#00FFB2; font-size:22px; }}
.badge {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:18px;
  letter-spacing:.14em; color:#04130b; background:#00FFB2;
  padding:12px 22px; border-radius:999px;
}}

.footbar {{
  position:absolute; left:64px; right:64px; bottom:52px; z-index:5;
  display:flex; flex-direction:column; align-items:center; gap:10px;
}}
.foot-url {{
  font-family:'IBM Plex Mono', monospace; font-weight:500; font-size:22px;
  letter-spacing:.12em; color:#00FFB2;
}}
.foot-topic {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:500;
  font-size:22px; color:#9aa39c;
}}

.mid {{
  position:absolute; left:72px; right:72px; top:160px; bottom:160px; z-index:4;
  display:flex; flex-direction:column; justify-content:center;
}}
.gr {{ color:#00FFB2; }}
b {{ font-weight:700; color:#FFFFFF; }}

.eyebrow {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;
  font-size:36px; color:#00FFB2; margin-bottom:28px;
}}
.h-big {{
  font-family:'Poppins', sans-serif; font-weight:800; font-size:68px;
  line-height:1.05; letter-spacing:-.02em; color:#F2F2F2; text-align:left;
}}
.strike {{
  text-decoration: none;
  background-image: linear-gradient(#00FFB2,#00FFB2);
  background-size: 100% 6px;
  background-position: 0 58%;
  background-repeat: no-repeat;
}}
.punch {{
  margin-top:36px; font-family:'Poppins', sans-serif; font-weight:700;
  font-size:42px; color:#F2F2F2;
}}

.step-row {{
  display:flex; align-items:center; gap:22px; margin-bottom:36px;
}}
.step-num {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:700;
  font-size:120px; line-height:1; color:#F2F2F2;
}}
.ico {{ width:72px; height:72px; flex-shrink:0; }}
.step-lab {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:500;
  font-size:32px; color:#9aa39c;
}}
.h-step {{
  font-family:'Poppins', sans-serif; font-weight:800; font-size:54px;
  line-height:1.12; letter-spacing:-.02em; color:#F2F2F2; text-align:left;
  max-width:900px; margin-bottom:28px;
}}
.body-step {{
  font-family:'Barlow Condensed', sans-serif; font-weight:500; font-size:36px;
  line-height:1.35; color:#9aa39c; max-width:860px;
}}

/* COVER — sin imagen */
.kicker {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:20px;
  letter-spacing:.22em; color:#00FFB2; margin-bottom:28px;
}}
.cover-title {{
  font-family:'Poppins', sans-serif; font-weight:800; font-size:84px;
  line-height:1.02; letter-spacing:-.03em; color:#F2F2F2; text-align:left;
}}
.cover-sub {{
  margin-top:32px; font-family:'Barlow Condensed', sans-serif; font-weight:500;
  font-size:34px; line-height:1.35; color:#9aa39c; max-width:780px;
}}

/* PHOTO SLIDE — foto Sebas + wash negro + grilla verde */
.s-photo .ph {{
  position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:0;
  filter: brightness(.78) contrast(1.05) saturate(.95);
}}
.s-photo .ph-wash {{
  position:absolute; inset:0; z-index:1;
  background: linear-gradient(180deg,
    rgba(10,10,10,.55) 0%,
    rgba(10,10,10,.15) 28%,
    rgba(10,10,10,.55) 52%,
    rgba(10,10,10,.92) 72%,
    #0A0A0A 90%);
}}
.s-photo .gridbg-photo {{
  z-index:2;
  background-image:
    linear-gradient(rgba(0,255,178,.22) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.22) 1px, transparent 1px);
  background-size:44px 44px;
}}
.mid-photo {{ justify-content:flex-end; padding-bottom:40px; }}
.script {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;
  font-size:34px; color:#00FFB2; margin-bottom:18px;
}}
.h-photo {{
  font-family:'Poppins', sans-serif; font-weight:800; font-size:64px;
  line-height:1.05; letter-spacing:-.02em; color:#F2F2F2; text-align:left;
}}
.h-photo-sub {{
  margin-top:22px; font-family:'Poppins', sans-serif; font-weight:700;
  font-size:36px; line-height:1.25; color:#F2F2F2;
}}
.script-inline {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;
  color:#00FFB2;
}}

/* CTA */
.h-cta {{
  font-family:'Poppins', sans-serif; font-weight:800; font-size:56px;
  line-height:1.1; letter-spacing:-.02em; color:#F2F2F2; text-align:left;
  margin-bottom:48px;
}}
.cta-row {{
  display:flex; align-items:center; gap:24px; margin-bottom:36px;
}}
.cta-box {{
  font-family:'Poppins', sans-serif; font-weight:800; font-size:42px;
  letter-spacing:.06em; color:#00FFB2; background:transparent;
  border:3px solid #00FFB2; padding:22px 36px; border-radius:8px;
}}
.cta-hint {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;
  font-size:28px; color:#9aa39c; display:flex; align-items:center; gap:10px;
}}
.arrow {{ color:#00FFB2; font-style:normal; font-family:'Poppins', sans-serif; font-weight:800; }}
.cta-line {{
  font-family:'Barlow Condensed', sans-serif; font-weight:500; font-size:34px;
  color:#9aa39c;
}}
"""


def main():
    slides = [
        slide_portada(),
        slide_problema(),
        slide_paso(1, ICON_MAIL,
                   "Un solo lugar donde caen todos los mensajes.",
                   "Web, Instagram, WhatsApp:",
                   "todo centralizado, nada se pierde."),
        slide_paso(2, ICON_CLOCK,
                   "Respuesta en menos de 1 hora.",
                   "Aunque sea solo para decir “te leo, te contesto con calma en X minutos”."),
        slide_paso(3, ICON_CHECK,
                   "Un seguimiento a los 3 días si no contestó.",
                   "El 40% de tus clientes cierran",
                   "en ese segundo mensaje."),
        slide_cambia(),
        slide_cta(),
    ]
    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8">
<title>3 pasos para no perder ningún lead — STLabs</title>
<style>{CSS}</style></head>
<body><div class="sheet">{''.join(slides)}</div></body></html>"""
    (B / "carrusel.html").write_text(html, encoding="utf-8")
    (B / "index.json").write_text(json.dumps({
        "titulo": "3 pasos para no perder ningún lead",
        "slides": 7,
        "fondo": "lino_tela",
        "familia_visual": "blueprint",
        "origen": "screenshot",
        "keyword_portada": "LEAD",
        "modo": "negro",
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(slides)} slides · negro · sin imagen portada")


if __name__ == "__main__":
    main()
