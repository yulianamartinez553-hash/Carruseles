# -*- coding: utf-8 -*-
"""
Carrusel STLabs — Agente que simplifica procesos
Clon editorial @ninodirector · 8 slides · modo negro · retícula verde · before_after
"""
from __future__ import annotations

import base64
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from stlabs_kit import chrome, write_html

N = 8
PORTADA = BUILD / "assets" / "portada-sebas-papeles.png"
PORTADA_URI = f"data:image/png;base64,{base64.b64encode(PORTADA.read_bytes()).decode()}"

EXTRA_CSS = """
/* ── Modo NEGRO STLabs + retícula verde + manchas ── */
.slide{
  background:#0A0A0A;color:#F2F2F2;
  box-shadow:none;
}
.slide::before{
  content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:
    linear-gradient(rgba(0,255,178,.055) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.055) 1px, transparent 1px);
  background-size:60px 60px;
  opacity:.85;
}
.slide::after{
  content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(38% 32% at 12% 18%, rgba(0,255,178,.14), transparent 68%),
    radial-gradient(42% 36% at 88% 72%, rgba(0,255,178,.10), transparent 65%),
    radial-gradient(28% 24% at 72% 12%, rgba(0,255,178,.08), transparent 70%),
    radial-gradient(22% 20% at 24% 88%, rgba(0,255,178,.06), transparent 72%);
}
.slide>*{position:relative;z-index:2;}
.web{color:#00FFB2;text-shadow:0 0 18px rgba(0,255,178,.35);bottom:64px;font-size:23px;letter-spacing:2px;}

.badge{
  display:inline-block;background:#0A0A0A;color:#00FFB2;
  border:2px solid rgba(0,255,178,.65);
  font-family:var(--mono);font-size:18px;font-weight:600;letter-spacing:2px;
  padding:10px 16px;margin-bottom:36px;text-transform:uppercase;
  box-shadow:0 0 20px rgba(0,255,178,.12);
}
.body-t{
  font-family:var(--cond);font-size:34px;line-height:1.32;color:#9aa39c;
  max-width:900px;margin-top:36px;
}
.body-t b{color:#F2F2F2;font-weight:700;}

.t-mega{
  font-family:'Bebas Neue',sans-serif;font-weight:400;line-height:.9;color:#F2F2F2;
  letter-spacing:0.01em;text-align:left;text-transform:uppercase;
  -webkit-text-stroke:5px #F2F2F2;
  paint-order:stroke fill;
  text-shadow:
    0 0 0 #F2F2F2,
    1px 0 0 #F2F2F2,-1px 0 0 #F2F2F2,0 1px 0 #F2F2F2,0 -1px 0 #F2F2F2,
    2px 0 0 #F2F2F2,-2px 0 0 #F2F2F2,0 2px 0 #F2F2F2,0 -2px 0 #F2F2F2,
    3px 0 0 #F2F2F2,-3px 0 0 #F2F2F2,0 3px 0 #F2F2F2,0 -3px 0 #F2F2F2,
    4px 0 0 #F2F2F2,-4px 0 0 #F2F2F2,0 4px 0 #F2F2F2,0 -4px 0 #F2F2F2,
    5px 0 0 #F2F2F2,-5px 0 0 #F2F2F2,0 5px 0 #F2F2F2,0 -5px 0 #F2F2F2,
    3px 3px 0 #F2F2F2,-3px 3px 0 #F2F2F2,3px -3px 0 #F2F2F2,-3px -3px 0 #F2F2F2,
    4px 3px 0 #F2F2F2,-4px 3px 0 #F2F2F2,4px -3px 0 #F2F2F2,-4px -3px 0 #F2F2F2,
    3px 4px 0 #F2F2F2,-3px 4px 0 #F2F2F2,3px -4px 0 #F2F2F2,-3px -4px 0 #F2F2F2,
    4px 4px 0 #F2F2F2,-4px 4px 0 #F2F2F2,4px -4px 0 #F2F2F2,-4px -4px 0 #F2F2F2,
    0 8px 22px rgba(0,0,0,.7);
}
.t-mega .gr{
  color:#00FFB2;
  -webkit-text-stroke:5px #00FFB2;
  paint-order:stroke fill;
  text-shadow:
    0 0 0 #00FFB2,
    1px 0 0 #00FFB2,-1px 0 0 #00FFB2,0 1px 0 #00FFB2,0 -1px 0 #00FFB2,
    2px 0 0 #00FFB2,-2px 0 0 #00FFB2,0 2px 0 #00FFB2,0 -2px 0 #00FFB2,
    3px 0 0 #00FFB2,-3px 0 0 #00FFB2,0 3px 0 #00FFB2,0 -3px 0 #00FFB2,
    4px 0 0 #00FFB2,-4px 0 0 #00FFB2,0 4px 0 #00FFB2,0 -4px 0 #00FFB2,
    5px 0 0 #00FFB2,-5px 0 0 #00FFB2,0 5px 0 #00FFB2,0 -5px 0 #00FFB2,
    3px 3px 0 #00FFB2,-3px 3px 0 #00FFB2,3px -3px 0 #00FFB2,-3px -3px 0 #00FFB2,
    4px 3px 0 #00FFB2,-4px 3px 0 #00FFB2,4px -3px 0 #00FFB2,-4px -3px 0 #00FFB2,
    3px 4px 0 #00FFB2,-3px 4px 0 #00FFB2,3px -4px 0 #00FFB2,-3px -4px 0 #00FFB2,
    4px 4px 0 #00FFB2,-4px 4px 0 #00FFB2,4px -4px 0 #00FFB2,-4px -4px 0 #00FFB2,
    0 0 36px rgba(0,255,178,.65),0 8px 22px rgba(0,0,0,.6);
}
.t-mega .ac{
  font-family:'Bebas Neue',sans-serif;font-style:normal;font-weight:400;color:#00FFB2;
  text-transform:uppercase;
  -webkit-text-stroke:5px #00FFB2;
  paint-order:stroke fill;
  text-shadow:
    0 0 0 #00FFB2,
    1px 0 0 #00FFB2,-1px 0 0 #00FFB2,0 1px 0 #00FFB2,0 -1px 0 #00FFB2,
    2px 0 0 #00FFB2,-2px 0 0 #00FFB2,0 2px 0 #00FFB2,0 -2px 0 #00FFB2,
    3px 0 0 #00FFB2,-3px 0 0 #00FFB2,0 3px 0 #00FFB2,0 -3px 0 #00FFB2,
    4px 0 0 #00FFB2,-4px 0 0 #00FFB2,0 4px 0 #00FFB2,0 -4px 0 #00FFB2,
    5px 0 0 #00FFB2,-5px 0 0 #00FFB2,0 5px 0 #00FFB2,0 -5px 0 #00FFB2,
    3px 3px 0 #00FFB2,-3px 3px 0 #00FFB2,3px -3px 0 #00FFB2,-3px -3px 0 #00FFB2,
    4px 3px 0 #00FFB2,-4px 3px 0 #00FFB2,4px -3px 0 #00FFB2,-4px -3px 0 #00FFB2,
    3px 4px 0 #00FFB2,-3px 4px 0 #00FFB2,3px -4px 0 #00FFB2,-3px -4px 0 #00FFB2,
    4px 4px 0 #00FFB2,-4px 4px 0 #00FFB2,4px -4px 0 #00FFB2,-4px -4px 0 #00FFB2,
    0 0 36px rgba(0,255,178,.65),0 8px 22px rgba(0,0,0,.6);
}
.t-stat{font-family:'Bebas Neue',sans-serif;font-weight:400;font-size:230px;line-height:.78;letter-spacing:0.01em;}
.t-head{font-size:136px;line-height:.9;letter-spacing:0.01em;}
.t-mid{font-family:'Bebas Neue',sans-serif;font-weight:400;font-size:118px;margin-top:6px;line-height:.9;letter-spacing:0.01em;}

/* Slide 1 — foto protagonista + título Impact ancho */
.s1-wrap{position:relative;height:100%;overflow:hidden;background:#0A0A0A;}
.s1-photo{
  position:absolute;inset:0;z-index:1;overflow:hidden;
  background:#050505;
}
.s1-photo img{
  width:100%;height:100%;object-fit:cover;object-position:center 18%;
  filter:contrast(1.06) saturate(1.08) brightness(1.02);
}
.s1-photo::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(180deg,
    rgba(10,10,10,.04) 0%,
    transparent 32%,
    rgba(10,10,10,.22) 50%,
    rgba(10,10,10,.72) 66%,
    rgba(10,10,10,.94) 78%,
    #0A0A0A 88%);
}
.s1-copy{
  position:absolute;left:0;right:0;bottom:0;z-index:3;
  padding:0 72px 118px;
}
.s1-copy .t-head{
  font-family:'Impact',sans-serif;font-weight:900;
  font-size:112px;line-height:.82;letter-spacing:0.01em;
  max-width:1000px;
  -webkit-text-stroke:6px #F2F2F2;
  paint-order:stroke fill;
  text-shadow:
    0 0 0 #F2F2F2,
    1px 0 0 #F2F2F2,-1px 0 0 #F2F2F2,0 1px 0 #F2F2F2,0 -1px 0 #F2F2F2,
    2px 0 0 #F2F2F2,-2px 0 0 #F2F2F2,0 2px 0 #F2F2F2,0 -2px 0 #F2F2F2,
    3px 0 0 #F2F2F2,-3px 0 0 #F2F2F2,0 3px 0 #F2F2F2,0 -3px 0 #F2F2F2,
    4px 0 0 #F2F2F2,-4px 0 0 #F2F2F2,0 4px 0 #F2F2F2,0 -4px 0 #F2F2F2,
    5px 0 0 #F2F2F2,-5px 0 0 #F2F2F2,0 5px 0 #F2F2F2,0 -5px 0 #F2F2F2,
    6px 0 0 #F2F2F2,-6px 0 0 #F2F2F2,0 6px 0 #F2F2F2,0 -6px 0 #F2F2F2,
    4px 4px 0 #F2F2F2,-4px 4px 0 #F2F2F2,4px -4px 0 #F2F2F2,-4px -4px 0 #F2F2F2,
    5px 5px 0 #F2F2F2,-5px 5px 0 #F2F2F2,5px -5px 0 #F2F2F2,-5px -5px 0 #F2F2F2,
    0 10px 28px rgba(0,0,0,.8);
}
.s1-copy .t-head .gr{
  font-family:'Impact',sans-serif;font-style:normal;font-weight:900;
  letter-spacing:0.01em;color:#00FFB2;
  white-space:nowrap;
  -webkit-text-stroke:6px #00FFB2;
  paint-order:stroke fill;
  text-shadow:
    0 0 0 #00FFB2,
    1px 0 0 #00FFB2,-1px 0 0 #00FFB2,0 1px 0 #00FFB2,0 -1px 0 #00FFB2,
    2px 0 0 #00FFB2,-2px 0 0 #00FFB2,0 2px 0 #00FFB2,0 -2px 0 #00FFB2,
    3px 0 0 #00FFB2,-3px 0 0 #00FFB2,0 3px 0 #00FFB2,0 -3px 0 #00FFB2,
    4px 0 0 #00FFB2,-4px 0 0 #00FFB2,0 4px 0 #00FFB2,0 -4px 0 #00FFB2,
    5px 0 0 #00FFB2,-5px 0 0 #00FFB2,0 5px 0 #00FFB2,0 -5px 0 #00FFB2,
    6px 0 0 #00FFB2,-6px 0 0 #00FFB2,0 6px 0 #00FFB2,0 -6px 0 #00FFB2,
    4px 4px 0 #00FFB2,-4px 4px 0 #00FFB2,4px -4px 0 #00FFB2,-4px -4px 0 #00FFB2,
    5px 5px 0 #00FFB2,-5px 5px 0 #00FFB2,5px -5px 0 #00FFB2,-5px -5px 0 #00FFB2,
    0 0 44px rgba(0,255,178,.75),0 10px 28px rgba(0,0,0,.75);
}
.s1-sub{
  margin-top:20px;font-family:var(--cond);font-weight:700;font-size:34px;
  letter-spacing:3px;color:#9aa39c;text-transform:uppercase;
}
.s1-chip{
  position:absolute;right:56px;top:42%;transform:translateY(-50%);
  width:54px;height:54px;z-index:4;
  background:#00FFB2;border:4px solid #0A0A0A;border-radius:10px;
  box-shadow:0 0 28px rgba(0,255,178,.45);
  image-rendering:pixelated;
}
.s1-chip::before{
  content:'';position:absolute;left:12px;top:10px;width:10px;height:10px;background:#0A0A0A;border-radius:2px;
  box-shadow:18px 0 0 #0A0A0A, 0 14px 0 #0A0A0A, 18px 14px 0 #0A0A0A;
}

/* Slides editoriales 2–7 */
.ed{padding:88px 84px 120px;height:100%;display:flex;flex-direction:column;justify-content:flex-start;}

/* Slide 7 — before/after */
.ba-grid{
  display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:28px;max-width:960px;
}
.ba-col{
  border:2px solid rgba(255,255,255,.12);padding:28px 24px;background:rgba(20,20,20,.72);
}
.ba-col h3{
  font-family:var(--mono);font-size:18px;letter-spacing:2px;margin-bottom:18px;
  color:#F2F2F2;
}
.ba-col ul{list-style:none;display:flex;flex-direction:column;gap:12px;}
.ba-col li{
  font-family:var(--cond);font-size:28px;line-height:1.25;color:#9aa39c;
  padding-left:18px;position:relative;
}
.ba-col li::before{
  content:'';position:absolute;left:0;top:12px;width:8px;height:8px;border-radius:50%;
  background:#666;
}
.ba-col.good{border-color:rgba(0,255,178,.55);background:rgba(0,255,178,.06);}
.ba-col.good h3{color:#00FFB2;}
.ba-col.good li{color:#d8e8e0;}
.ba-col.good li::before{background:#00FFB2;box-shadow:0 0 8px rgba(0,255,178,.55);}

/* Slide 8 — CTA */
.s8-wrap{
  padding:96px 84px 120px;height:100%;display:flex;flex-direction:column;
  justify-content:center;align-items:flex-start;
}
.s8-wrap .t-mega{font-family:'Bebas Neue',sans-serif;font-weight:400;font-size:100px;max-width:960px;line-height:.9;letter-spacing:0.01em;}
.s8-wrap .s8-q{
  font-family:'Bebas Neue',sans-serif;font-weight:400;font-size:100px;
  display:inline-block;vertical-align:baseline;margin-right:6px;
  letter-spacing:0.01em;
  -webkit-text-stroke:5px #F2F2F2;
  paint-order:stroke fill;
  text-shadow:
    0 0 0 #F2F2F2,
    2px 0 0 #F2F2F2,-2px 0 0 #F2F2F2,0 2px 0 #F2F2F2,0 -2px 0 #F2F2F2,
    4px 0 0 #F2F2F2,-4px 0 0 #F2F2F2,0 4px 0 #F2F2F2,0 -4px 0 #F2F2F2,
    3px 3px 0 #F2F2F2,-3px 3px 0 #F2F2F2,3px -3px 0 #F2F2F2,-3px -3px 0 #F2F2F2,
    0 8px 22px rgba(0,0,0,.7);
}
.cta-pill{
  margin-top:44px;display:inline-flex;align-items:center;gap:16px;
  background:rgba(0,255,178,.08);border:2px solid rgba(0,255,178,.65);
  border-radius:999px;padding:20px 36px;
  font-family:var(--pop);font-weight:800;font-size:36px;color:#F2F2F2;
  box-shadow:0 0 32px rgba(0,255,178,.18);
}
.cta-pill span{
  font-family:var(--mono);font-weight:600;font-size:28px;letter-spacing:2px;
  color:#04130b;background:#00FFB2;border-radius:10px;padding:10px 16px;
}
.s8-note{
  margin-top:32px;font-family:var(--cond);font-size:32px;line-height:1.35;
  color:#9aa39c;max-width:860px;
}
.s8-note b{color:#F2F2F2;}
"""


def slide1() -> str:
    return chrome(
        1,
        f"""
<div class="s1-wrap">
  <div class="s1-photo"><img src="{PORTADA_URI}" alt=""></div>
  <span class="s1-chip" aria-hidden="true"></span>
  <div class="s1-copy">
    <h1 class="t-mega t-head">LA IA NO TE<br>SIMPLIFICA<br><span class="gr">TUS PROCESOS</span></h1>
    <p class="s1-sub">Solo te lo mueve de lugar</p>
  </div>
</div>
""",
        total=N,
        bridges=None,
        footer=True,
    )


def slide2() -> str:
    return chrome(
        2,
        """
<div class="ed">
  <span class="badge">El dato</span>
  <h2 class="t-mega t-stat"><span class="gr">+68%</span></h2>
  <h3 class="t-mega t-mid">EN LO REPETITIVO</h3>
  <p class="body-t">Equipos que midieron su operación descubrieron que casi <b>7 de cada 10 horas</b>
  se van en seguimientos, recordatorios, copias y respuestas que un agente bien armado puede ejecutar.</p>
</div>
""",
        total=N,
        bridges=None,
        footer=True,
    )


def slide3() -> str:
    return chrome(
        3,
        """
<div class="ed">
  <span class="badge">El nombre</span>
  <h2 class="t-mega t-head">COSTO<br><span class="ac">OPERATIVO</span></h2>
  <p class="body-t">Así lo llamamos cuando automatizás la escritura pero seguís pagando con
  <b>revisiones, copias y coordinación manual</b>. Producís más rápido. Pagás operando.</p>
</div>
""",
        total=N,
        bridges=None,
        footer=True,
    )


def slide4() -> str:
    return chrome(
        4,
        """
<div class="ed">
  <span class="badge">El cómo / 1</span>
  <h2 class="t-mega t-head">EVALUÁ POR<br><span class="gr">IMPACTO</span></h2>
  <p class="body-t">Tres preguntas: <b>qué se repite</b>, quién lo hace hoy y cuántas horas te come por semana.
  Si no cumple las tres, no va al agente.</p>
</div>
""",
        total=N,
        bridges=None,
        footer=True,
    )


def slide5() -> str:
    return chrome(
        5,
        """
<div class="ed">
  <span class="badge">El cómo / 2</span>
  <h2 class="t-mega t-head">DELEGÁ LO<br><span class="gr">REPETITIVO</span></h2>
  <p class="body-t">Publicaciones, recordatorios, seguimientos, respuestas frecuentes, armado de páginas de captura.
  Eso lo ejecuta el agente — <b>con reglas claras</b> y trazabilidad.</p>
</div>
""",
        total=N,
        bridges=None,
        footer=True,
    )


def slide6() -> str:
    return chrome(
        6,
        """
<div class="ed">
  <span class="badge">El cómo / 3</span>
  <h2 class="t-mega t-head">QUEDATE CON<br><span class="gr">EL JUICIO</span></h2>
  <p class="body-t">Vos decidís excepciones, cierres y estrategia. El agente corre lo predecible
  y te avisa cuando algo necesita <b>tu cabeza</b>, no tu tiempo muerto.</p>
</div>
""",
        total=N,
        bridges=None,
        footer=True,
    )


def slide7() -> str:
    return chrome(
        7,
        """
<div class="ed">
  <span class="badge">Antes / después</span>
  <h2 class="t-mega t-mid">SIN AGENTE VS<br><span class="gr">CON AGENTE</span></h2>
  <div class="ba-grid">
    <div class="ba-col">
      <h3>SIN AGENTE</h3>
      <ul>
        <li>Revisás cada respuesta</li>
        <li>Copiás recordatorios a mano</li>
        <li>Seguís prospectos uno por uno</li>
        <li>La operación depende de vos</li>
      </ul>
    </div>
    <div class="ba-col good">
      <h3>CON AGENTE</h3>
      <ul>
        <li>Ejecuta lo repetitivo 24/7</li>
        <li>Publica, recuerda y sigue</li>
        <li>Escala sin sumarte horas</li>
        <li>Vos supervisás, no empujás</li>
      </ul>
    </div>
  </div>
</div>
""",
        total=N,
        bridges=None,
        footer=True,
    )


def slide8() -> str:
    return chrome(
        8,
        """
<div class="s8-wrap">
  <h2 class="t-mega"><span class="s8-q">¿</span>QUERÉS UN AGENTE QUE<br><span class="gr">SIMPLIFIQUE</span><br>TUS PROCESOS?</h2>
  <div class="cta-pill">Comentá <span>PROCESOS</span></div>
  <p class="s8-note">Te muestro qué tareas delegar primero, cómo armarlo en tu operación
  y qué resultados podés esperar en la primera semana.</p>
</div>
""",
        total=N,
        bridges=None,
        footer=True,
    )


def main() -> None:
    slides = [slide1(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7(), slide8()]
    out = BUILD / "carrusel.html"
    write_html(slides, out, extra_css=EXTRA_CSS)
    print(f"✓ HTML escrito: {out}")


if __name__ == "__main__":
    main()
