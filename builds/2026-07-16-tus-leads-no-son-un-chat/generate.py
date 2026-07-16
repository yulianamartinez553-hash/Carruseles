# -*- coding: utf-8 -*-
"""Carrusel original STLabs — modo blanco · dossier editorial · retícula fina."""
from __future__ import annotations

import base64
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from stlabs_kit import chrome, write_html, render, package  # noqa: E402

KEYWORD = "LEADS"
SEB_URI = f"data:image/jpeg;base64,{base64.b64encode((REPO / 'seb.jpg').read_bytes()).decode()}"
WORD_DIR = REPO / "Word"

EXTRA_CSS = """
/* ── MODO BLANCO ── */
.sheet{background:#e8e8e8;}
.slide{
  color:#0A0A0A;
  background:
    radial-gradient(48% 32% at 88% 8%, rgba(0,255,178,.10), transparent 62%),
    radial-gradient(42% 30% at 8% 92%, rgba(0,255,178,.06), transparent 60%),
    linear-gradient(168deg,#FFFFFF 0%, #F7F7F5 55%, #F2F2F2 100%);
}
.slide.grid::before{
  opacity:.85;
  background-image:
    linear-gradient(rgba(10,10,10,.045) 1px, transparent 1px),
    linear-gradient(90deg, rgba(10,10,10,.045) 1px, transparent 1px);
  background-size:56px 56px;
}
.web{color:var(--verde);opacity:.95;}
.brnode{
  background:radial-gradient(circle at 50% 45%,#ffffff,#f0f0f0);
  border:2px solid var(--verde);
  box-shadow:0 0 24px rgba(0,255,178,.28), inset 0 0 16px rgba(255,255,255,.7);
}
.prog{background:#e0e0e0;}
b{color:#0A0A0A;}

/* tipografía / layout dossier */
.kicker{font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--verde);text-transform:uppercase;}
.kw-pill{
  display:inline-block;margin-top:22px;padding:12px 22px;
  border:2px solid var(--verde);background:rgba(0,255,178,.12);
  font-family:var(--mono);font-size:22px;letter-spacing:3px;color:#0A0A0A;font-weight:600;
}
.disp{font-family:var(--disp);font-weight:400;line-height:.88;letter-spacing:1px;color:#0A0A0A;text-align:left;}
.pop{font-family:var(--pop);font-weight:800;line-height:1.05;color:#0A0A0A;text-align:left;}
.body{font-family:var(--cond);font-size:34px;line-height:1.35;color:#3a3f3c;text-align:left;max-width:900px;}
.body b{color:#0A0A0A;font-weight:700;}
.rule{height:4px;width:120px;background:var(--verde);margin:28px 0 32px;border-radius:2px;}

/* slide 1 cover */
.s1{padding:88px 84px 0;height:100%;}
.s1 .disp{font-size:128px;margin-top:18px;}
.s1 .sub{font-family:var(--cond);font-size:36px;color:#4a524e;margin-top:28px;max-width:820px;text-align:left;}
.s1-photo{
  position:absolute;right:-40px;bottom:140px;width:420px;height:520px;z-index:3;
  border:3px solid rgba(0,255,178,.55);overflow:hidden;
  box-shadow:-18px 24px 60px rgba(10,10,10,.18);
  transform:rotate(-3deg);
}
.s1-photo img{
  width:100%;height:100%;object-fit:cover;object-position:center top;
  filter:brightness(.92) contrast(1.05) saturate(.85);
}
.s1-photo::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(180deg,transparent 45%,rgba(242,242,242,.55) 100%);
}

/* slides interiores */
.pad{padding:96px 84px 0;}
.s-title{font-family:var(--pop);font-weight:800;font-size:64px;line-height:1.05;color:#0A0A0A;text-align:left;margin-top:10px;}
.s-title .ac{font-size:1.05em;}

.list{margin-top:36px;display:flex;flex-direction:column;gap:22px;}
.row{
  display:grid;grid-template-columns:72px 1fr;gap:22px;align-items:start;
  padding:22px 24px;background:rgba(255,255,255,.72);
  border:1px solid rgba(10,10,10,.08);border-left:5px solid var(--verde);
}
.row .n{font-family:var(--disp);font-size:56px;line-height:1;color:var(--verde);}
.row h3{font-family:var(--pop);font-weight:800;font-size:34px;color:#0A0A0A;text-align:left;}
.row p{font-family:var(--cond);font-size:28px;color:#4a524e;margin-top:6px;text-align:left;}

.split{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:40px;}
.card{
  background:#fff;border:1px solid rgba(10,10,10,.08);padding:32px 28px;
  box-shadow:0 16px 40px rgba(10,10,10,.06);
}
.card.bad{border-top:5px solid var(--red);}
.card.good{border-top:5px solid var(--verde);}
.card h4{font-family:var(--mono);font-size:18px;letter-spacing:2px;margin-bottom:16px;}
.card.bad h4{color:var(--red);}
.card.good h4{color:var(--verde);}
.card ul{list-style:none;display:flex;flex-direction:column;gap:14px;}
.card li{font-family:var(--cond);font-size:28px;color:#3a3f3c;padding-left:18px;position:relative;text-align:left;}
.card li::before{content:'';position:absolute;left:0;top:14px;width:8px;height:8px;border-radius:50%;background:#9aa39c;}
.card.good li::before{background:var(--verde);}

.quote{
  margin-top:48px;padding:36px 32px;background:#0A0A0A;color:#F2F2F2;
  border-left:6px solid var(--verde);
}
.quote p{font-family:var(--pop);font-weight:800;font-size:40px;line-height:1.15;text-align:left;}
.quote span{display:block;margin-top:16px;font-family:var(--mono);font-size:18px;color:var(--verde);letter-spacing:2px;}

/* slide foto editorial */
.s5{position:relative;height:100%;}
.s5-img{position:absolute;inset:0;z-index:0;}
.s5-img img{
  width:100%;height:100%;object-fit:cover;object-position:center 20%;
  filter:brightness(.78) contrast(1.08) saturate(.7);
}
.s5-scrim{position:absolute;inset:0;z-index:1;
  background:linear-gradient(180deg,rgba(255,255,255,.15) 0%, rgba(255,255,255,.35) 35%,
   rgba(10,10,10,.55) 68%, rgba(10,10,10,.92) 100%);}
.s5-copy{position:absolute;left:84px;right:84px;bottom:180px;z-index:5;}
.s5-copy .kicker{color:var(--verde);}
.s5-copy .pop{color:#F2F2F2;font-size:58px;margin-top:12px;}
.s5-copy .body{color:#c8ceca;margin-top:18px;}
.s5-copy .body b{color:#F2F2F2;}

/* CTA final */
.s6{padding:110px 84px 0;text-align:left;}
.s6 .disp{font-size:110px;margin-top:12px;}
.s6 .body{margin-top:28px;}
.cta-box{
  margin-top:48px;padding:36px 32px;background:#0A0A0A;color:#F2F2F2;
  border:2px solid rgba(0,255,178,.45);
  box-shadow:0 20px 50px rgba(10,10,10,.18);
}
.cta-box p{font-family:var(--cond);font-size:36px;line-height:1.3;}
.cta-box .kw{font-family:var(--pop);font-weight:800;color:var(--verde);font-size:42px;}
.cta-hint{margin-top:22px;font-family:var(--mono);font-size:20px;letter-spacing:2px;color:#4a524e;}
"""


def slide1():
    return chrome(
        1,
        f"""
<div class="s1">
  <div class="kicker">STLABS · REVOPS</div>
  <h1 class="disp">TUS LEADS<br>NO SON<br><span class="gr">UN CHAT</span></h1>
  <div class="kw-pill">COMENTÁ · {KEYWORD}</div>
  <p class="sub">Si tu seguimiento vive en el chat, estás perdiendo plata todos los días.</p>
</div>
<div class="s1-photo"><img src="{SEB_URI}" alt="Sebastián García"></div>
""",
        total=6,
        bridges="right",
        footer=True,
    ).replace('class="slide"', 'class="slide grid"', 1)


def slide2():
    return chrome(
        2,
        """
<div class="pad">
  <div class="kicker">EL PROBLEMA</div>
  <h2 class="s-title">El caos se disfraza<br>de <span class="ac">respuesta rápida</span></h2>
  <div class="rule"></div>
  <p class="body">Contestás en el momento. Después nadie sabe <b>quién sigue</b>, <b>qué prometiste</b> ni <b>cuándo cerrás</b>.</p>
  <div class="list">
    <div class="row"><div class="n">01</div><div><h3>Mensajes sueltos</h3><p>Leads en chats, notas y “después lo anoto”.</p></div></div>
    <div class="row"><div class="n">02</div><div><h3>Dueño fantasma</h3><p>Si no hay responsable, el lead se enfría.</p></div></div>
    <div class="row"><div class="n">03</div><div><h3>Cierre a suerte</h3><p>Sin próximo paso, no hay embudo. Hay esperanza.</p></div></div>
  </div>
</div>
""",
        total=6,
        bridges="both",
        footer=True,
    ).replace('class="slide"', 'class="slide grid"', 1)


def slide3():
    return chrome(
        3,
        """
<div class="pad">
  <div class="kicker">ANTES / DESPUÉS</div>
  <h2 class="s-title">Misma energía.<br>Otro <span class="ac">resultado</span>.</h2>
  <div class="rule"></div>
  <div class="split">
    <div class="card bad">
      <h4>SIN SISTEMA</h4>
      <ul>
        <li>Lead perdido en el celular</li>
        <li>Seguimiento “cuando me acuerde”</li>
        <li>Equipo preguntando por estado</li>
        <li>Números que no cierran</li>
      </ul>
    </div>
    <div class="card good">
      <h4>CON OPERACIÓN</h4>
      <ul>
        <li>Lead entra a un solo lugar</li>
        <li>Próximo paso con fecha</li>
        <li>Dueño visible en el sistema</li>
        <li>Embudo que se puede leer</li>
      </ul>
    </div>
  </div>
</div>
""",
        total=6,
        bridges="both",
        footer=True,
    ).replace('class="slide"', 'class="slide grid"', 1)


def slide4():
    return chrome(
        4,
        """
<div class="pad">
  <div class="kicker">REGLA DE ORO</div>
  <h2 class="s-title">Un lead.<br>Un dueño.<br>Un <span class="ac">próximo paso</span>.</h2>
  <div class="rule"></div>
  <p class="body">Si no está escrito en el sistema, <b>no existe</b>. El chat es canal. El sistema es memoria.</p>
  <div class="quote">
    <p>Automatizá el seguimiento. Dejá de depender de la memoria del equipo.</p>
    <span>STLABS · OPERACIÓN COMERCIAL</span>
  </div>
</div>
""",
        total=6,
        bridges="both",
        footer=True,
    ).replace('class="slide"', 'class="slide grid"', 1)


def slide5():
    return chrome(
        5,
        f"""
<div class="s5">
  <div class="s5-img"><img src="{SEB_URI}" alt="Sebastián García"></div>
  <div class="s5-scrim"></div>
  <div class="s5-copy">
    <div class="kicker">CÓMO SE VE</div>
    <h2 class="pop">Entrada clara.<br>Seguimiento duro.<br>Cierre medible.</h2>
    <p class="body">Diseñamos la operación para que <b>ningún lead</b> dependa de un chat suelto.</p>
  </div>
</div>
""",
        total=6,
        bridges="both",
        footer=True,
    )


def slide6():
    return chrome(
        6,
        f"""
<div class="s6">
  <div class="kicker">AHORA</div>
  <h2 class="disp">DEJÁ DE<br>PERDER<br><span class="gr">{KEYWORD}</span></h2>
  <div class="rule"></div>
  <p class="body">Si tu equipo vende por chat y pierde oportunidades, esto es para vos.</p>
  <div class="cta-box">
    <p>Comentá <span class="kw">{KEYWORD}</span> y te muestro cómo ordenar el seguimiento sin sumar caos.</p>
  </div>
  <p class="cta-hint">GUARDÁ ESTO · COMPARTILO CON TU EQUIPO</p>
</div>
""",
        total=6,
        bridges="left",
        footer=True,
    ).replace('class="slide"', 'class="slide grid"', 1)


def main():
    slides = [slide1(), slide2(), slide3(), slide4(), slide5(), slide6()]
    write_html(slides, BUILD / "carrusel.html", extra_css=EXTRA_CSS)
    print("HTML escrito:", BUILD / "carrusel.html")
    pngs = render(BUILD)
    print(f"Render OK: {len(pngs)} PNGs")

    meta = {
        "titulo": "Tus Leads No Son Un Chat",
        "slides": 6,
        "fondo": "reticula_fina",
        "familia_visual": "dossier_editorial",
        "origen": "original",
        "keyword_portada": KEYWORD,
        "modo_fondo": "blanco",
        "feedback": {"estado": "borrador"},
    }
    out = package(BUILD, "STLabs-TusLeadsNoSonUnChat", meta=meta)
    print("Package builds:", out)

    WORD_DIR.mkdir(parents=True, exist_ok=True)
    # Entrega limpia en Word/
    for name in (
        "STLabs-TusLeadsNoSonUnChat.html",
        "STLabs-TusLeadsNoSonUnChat.zip",
        "_preview-tira.png",
        "manifest.json",
        "slide-01.png",
        "slide-02.png",
        "slide-03.png",
        "slide-04.png",
        "slide-05.png",
        "slide-06.png",
    ):
        src = out / name
        if src.exists():
            shutil.copy2(src, WORD_DIR / name)

    # Manifiesto de fuentes (entregable skill)
    (WORD_DIR / "MANIFIESTO-FUENTES.md").write_text(
        """# Manifiesto de fuentes — Tus Leads No Son Un Chat

| Fuente | Peso / estilo | Rol | Origen | Código / comando de carga |
|---|---|---|---|---|
| Bebas Neue | 400 | título display portada/CTA | `fonts/BebasNeue-Regular.ttf` (skill STLabs) | `@font-face{font-family:'Bebas Neue';src:url(data:font/ttf;base64,...) format('truetype');}` embebido en HTML |
| Poppins | 800 | titulares de paso / quote | `fonts/Poppins-Bold.ttf` | `@font-face` base64 en HTML final |
| Lora | 600 italic | palabra-acento `.ac` en verde | `fonts/Lora-Italic-Variable.ttf` | `@font-face` italic variable base64 |
| Barlow Condensed | 400–700 | cuerpo / claims | `fonts/BarlowCondensed-*.ttf` | `@font-face` base64 |
| IBM Plex Mono | 400–600 | kickers, footer, URL | `fonts/IBMPlexMono-*.ttf` | `@font-face` base64 |

Modo: **blanco** · Textura: **retícula fina** · Familia visual: **dossier editorial**
Firma en todos los slides: `sebastian.stlabs.ar`
""",
        encoding="utf-8",
    )
    (WORD_DIR / "LEEME.txt").write_text(
        f"""Carrusel STLabs — Tus Leads No Son Un Chat
Modo fondo: BLANCO
Textura: reticula_fina
Familia: dossier_editorial
Keyword: {KEYWORD}
Slides: 6 (retina 2160×2700)

Contenido de esta carpeta:
- slide-01.png … slide-06.png
- _preview-tira.png
- STLabs-TusLeadsNoSonUnChat.html (fuentes embebidas)
- STLabs-TusLeadsNoSonUnChat.zip
- MANIFIESTO-FUENTES.md
- manifest.json
""",
        encoding="utf-8",
    )
    print("Entrega Word/:", WORD_DIR)


if __name__ == "__main__":
    main()
