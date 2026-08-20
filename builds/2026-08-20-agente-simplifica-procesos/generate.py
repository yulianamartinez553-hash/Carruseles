# -*- coding: utf-8 -*-
"""
Carrusel STLabs — Agente que simplifica procesos
Clon editorial @ninodirector · 8 slides · modo blanco · lino_tela · before_after
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
PORTADA = BUILD / "assets" / "portada-hombre-papeles.png"
PORTADA_URI = f"data:image/png;base64,{base64.b64encode(PORTADA.read_bytes()).decode()}"

EXTRA_CSS = """
/* ── Modo BLANCO + textura lino_tela ── */
.slide{
  background:#F5F0E8;color:#0A0A0A;
  box-shadow:inset 0 0 0 1px rgba(10,10,10,.04);
}
.slide::before{
  content:'';position:absolute;inset:0;z-index:0;pointer-events:none;opacity:.35;
  background:
    repeating-linear-gradient(0deg, rgba(10,10,10,.025) 0 1px, transparent 1px 4px),
    repeating-linear-gradient(90deg, rgba(10,10,10,.018) 0 1px, transparent 1px 5px);
}
.slide>*{position:relative;z-index:2;}
.web{color:#00FFB2;text-shadow:none;bottom:64px;font-size:23px;letter-spacing:2px;}

.badge{
  display:inline-block;background:#0A0A0A;color:#F5F0E8;
  font-family:var(--mono);font-size:18px;font-weight:600;letter-spacing:2px;
  padding:10px 16px;margin-bottom:36px;text-transform:uppercase;
}
.body-t{
  font-family:var(--cond);font-size:32px;line-height:1.35;color:#3a3a3a;
  max-width:900px;margin-top:36px;
}
.body-t b{color:#0A0A0A;font-weight:700;}

.t-mega{
  font-family:var(--disp);font-weight:400;line-height:.88;color:#0A0A0A;
  letter-spacing:.5px;text-align:left;
}
.t-mega .gr{color:#00FFB2;}
.t-mega .ac{
  font-family:var(--serif);font-style:italic;font-weight:700;color:#00FFB2;
}
.t-stat{font-size:168px;line-height:.82;}
.t-head{font-size:118px;}
.t-mid{font-size:96px;margin-top:4px;}

/* Slide 1 — portada dividida */
.s1-wrap{position:relative;height:100%;overflow:hidden;background:#F5F0E8;}
.s1-photo{
  position:absolute;left:0;right:0;top:0;height:47%;overflow:hidden;
  background:#111;
}
.s1-photo img{
  width:100%;height:100%;object-fit:cover;object-position:center 22%;
  filter:grayscale(1) contrast(1.08) brightness(.92);
}
.s1-photo::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(180deg, transparent 55%, rgba(245,240,232,.92) 100%);
}
.s1-copy{
  position:absolute;left:0;right:0;bottom:0;height:53%;
  padding:28px 72px 120px;display:flex;flex-direction:column;justify-content:center;
}
.s1-sub{
  margin-top:22px;font-family:var(--cond);font-weight:700;font-size:34px;
  letter-spacing:1px;color:#0A0A0A;text-transform:uppercase;
}
.s1-chip{
  position:absolute;right:56px;bottom:52%;transform:translateY(50%);
  width:54px;height:54px;z-index:4;
  background:#00FFB2;border:4px solid #F5F0E8;border-radius:10px;
  box-shadow:0 8px 24px rgba(0,0,0,.18);
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
  border:2px solid rgba(10,10,10,.12);padding:28px 24px;background:rgba(255,255,255,.45);
}
.ba-col h3{
  font-family:var(--mono);font-size:18px;letter-spacing:2px;margin-bottom:18px;
  color:#0A0A0A;
}
.ba-col ul{list-style:none;display:flex;flex-direction:column;gap:12px;}
.ba-col li{
  font-family:var(--cond);font-size:26px;line-height:1.25;color:#3a3a3a;
  padding-left:18px;position:relative;
}
.ba-col li::before{
  content:'';position:absolute;left:0;top:11px;width:8px;height:8px;border-radius:50%;
  background:#0A0A0A;
}
.ba-col.good{border-color:rgba(0,255,178,.55);background:rgba(0,255,178,.06);}
.ba-col.good h3{color:#00a874;}
.ba-col.good li::before{background:#00FFB2;}

/* Slide 8 — CTA */
.s8-wrap{
  padding:96px 84px 120px;height:100%;display:flex;flex-direction:column;
  justify-content:center;align-items:flex-start;
}
.s8-wrap .t-mega{font-size:92px;max-width:920px;}
.cta-pill{
  margin-top:44px;display:inline-flex;align-items:center;gap:16px;
  background:#0A0A0A;border-radius:999px;padding:20px 36px;
  font-family:var(--pop);font-weight:800;font-size:34px;color:#F5F0E8;
}
.cta-pill span{
  font-family:var(--mono);font-weight:600;font-size:28px;letter-spacing:2px;
  color:#04130b;background:#00FFB2;border-radius:10px;padding:10px 16px;
}
.s8-note{
  margin-top:32px;font-family:var(--cond);font-size:30px;line-height:1.35;
  color:#3a3a3a;max-width:860px;
}
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
    <p class="s1-sub">Solo te los mueve de lugar</p>
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
  <b>revisiones, copias y coordinación manual</b>. Produís más rápido. Pagás operando.</p>
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
  Si no pasa esas tres, no va al agente.</p>
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
  <p class="body-t">Publicaciones, recordatorios, seguimientos, respuestas frecuentes, armado de landings.
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
        <li>Seguís leads uno por uno</li>
        <li>La operación depende de vos</li>
      </ul>
    </div>
    <div class="ba-col good">
      <h3>CON AGENTE</h3>
      <ul>
        <li>Ejecuta lo repetitivo 24/7</li>
        <li>Publica, recuerda y sigue</li>
        <li>Te escala sin sumar horas</li>
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
  <h2 class="t-mega">¿QUERÉS UN AGENTE QUE<br><span class="gr">SIMPLIFIQUE</span><br>TUS PROCESOS?</h2>
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
