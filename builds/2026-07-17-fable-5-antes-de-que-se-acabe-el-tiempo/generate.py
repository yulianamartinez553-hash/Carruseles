# -*- coding: utf-8 -*-
"""Clon Fable 5 (centeia) → STLabs · modo blanco · lino/tela · before_after."""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from stlabs_kit import chrome, write_html, render, package  # noqa: E402

KEYWORD = "FABLE"
WORD_DIR = REPO / "Word"
TOTAL = 8

EXTRA_CSS = """
/* ── MODO BLANCO + LINO ── */
.sheet{background:#e8e8e8;}
.slide{
  color:#0A0A0A;
  background:
    radial-gradient(50% 34% at 50% 0%, rgba(0,255,178,.09), transparent 58%),
    linear-gradient(180deg,#FFFFFF 0%, #F7F7F5 100%);
}
.slide.lino::before{
  content:'';position:absolute;inset:0;z-index:0;pointer-events:none;opacity:.35;
  background-image:
    repeating-linear-gradient(0deg, rgba(10,10,10,.035) 0 1px, transparent 1px 3px),
    repeating-linear-gradient(90deg, rgba(10,10,10,.028) 0 1px, transparent 1px 3px);
  mix-blend-mode:multiply;
}
.web{color:var(--verde)!important;opacity:.95;}
b{color:#0A0A0A;}

.topbar{
  position:absolute;top:56px;left:72px;right:72px;z-index:5;
  display:flex;justify-content:space-between;align-items:center;
  font-family:var(--mono);font-size:18px;letter-spacing:2px;color:#6a736e;
}
.foot-brand{
  position:absolute;left:0;right:0;bottom:70px;z-index:6;text-align:center;
  font-family:var(--mono);font-size:22px;letter-spacing:1px;color:var(--verde);
}
.foot-brand .sep{color:var(--verde);opacity:.7;}
.foot-brand .tag{color:var(--verde);}

.pad{padding:120px 72px 0;}
.kicker{font-family:var(--mono);font-size:18px;letter-spacing:2px;color:#6a736e;}

.h-title{
  font-family:var(--anton);font-weight:400;font-size:56px;line-height:1.02;
  color:#0A0A0A;text-align:left;text-transform:uppercase;letter-spacing:.5px;
  display:flex;gap:22px;align-items:flex-start;margin-top:28px;
}
.h-title .num{
  font-family:var(--impact);font-weight:900;color:var(--verde);
  font-size:78px;line-height:.9;flex:0 0 auto;letter-spacing:0;
}
.h-title .txt{flex:1;padding-top:6px;}
.h-title .hl{color:var(--verde);}

.lead{font-family:var(--cond);font-size:32px;line-height:1.35;color:#3a3f3c;margin-top:28px;text-align:left;max-width:920px;}
.lead .hl{color:var(--verde);font-weight:700;}

.bullets{margin-top:26px;display:flex;flex-direction:column;gap:14px;}
.bullets li{
  list-style:none;font-family:var(--cond);font-size:30px;color:#2a2f2c;
  padding-left:28px;position:relative;text-align:left;
}
.bullets li::before{
  content:'';position:absolute;left:0;top:12px;width:12px;height:12px;background:var(--verde);
}

.bullets-2col{margin-top:22px;display:grid;grid-template-columns:1fr 1fr;gap:10px 36px;}
.bullets-2col li{
  list-style:none;font-family:var(--cond);font-size:28px;color:#2a2f2c;
  padding-left:28px;position:relative;text-align:left;
}
.bullets-2col li::before{
  content:'';position:absolute;left:0;top:12px;width:12px;height:12px;border-radius:50%;background:var(--verde);
}

.prompt{
  margin-top:28px;border:2px solid var(--verde);border-radius:18px;padding:26px 28px;
  background:rgba(255,255,255,.88);box-shadow:0 12px 36px rgba(10,10,10,.06);
}
.prompt .ph{
  font-family:var(--mono);font-size:16px;letter-spacing:2px;color:var(--verde);margin-bottom:12px;
}
.prompt .ph i{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--verde);margin-right:5px;}
.prompt p{font-family:var(--cond);font-size:28px;line-height:1.35;color:#1a1a1a;text-align:left;}

/* ── COVER ── */
.cover{padding:70px 64px 0;display:flex;flex-direction:column;align-items:center;text-align:center;}
.cd-label{font-family:var(--mono);font-size:16px;letter-spacing:3px;color:#6a736e;margin-bottom:10px;}
.cd-wrap{
  width:720px;padding:18px 22px 22px;border-radius:16px;
  border:2px solid rgba(0,255,178,.55);
  background:linear-gradient(180deg,#0f1412,#0a0a0a);
  box-shadow:0 0 40px rgba(0,255,178,.18), inset 0 0 30px rgba(0,255,178,.08);
}
.cd-digits{
  font-family:var(--disp);font-size:110px;line-height:1;letter-spacing:8px;
  color:#FF5247;text-shadow:0 0 18px rgba(255,82,71,.55);
}
.fable-logo{
  margin-top:48px;width:210px;height:210px;border-radius:36px;
  background:radial-gradient(circle at 40% 30%, #1a1a1a, #0a0a0a);
  border:3px solid rgba(0,255,178,.7);
  box-shadow:0 20px 50px rgba(10,10,10,.2), 0 0 40px rgba(0,255,178,.2);
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;
}
.fable-star{
  width:72px;height:72px;color:var(--verde);
  filter:drop-shadow(0 0 12px rgba(0,255,178,.55));
}
.fable-name{font-family:var(--anton);font-weight:400;font-size:34px;color:#F2F2F2;letter-spacing:2px;}
.cover-title{
  margin-top:40px;font-family:var(--impact);font-weight:900;font-size:82px;line-height:.96;
  letter-spacing:1px;text-transform:uppercase;color:#0A0A0A;text-align:center;
}
.cover-title .hl{color:var(--verde);}
.cover-sub{margin-top:22px;font-family:var(--cond);font-size:34px;color:#3a3f3c;}

/* ── boxes uso 05 ── */
.box{margin-top:18px;border-radius:16px;padding:22px 24px;border:2px solid #ddd;background:#fff;text-align:left;}
.box .bl{font-family:var(--mono);font-size:16px;letter-spacing:2px;margin-bottom:10px;}
.box p{font-family:var(--cond);font-size:28px;line-height:1.3;color:#1a1a1a;}
.box.bad{border-color:rgba(255,82,71,.55);}
.box.bad .bl{color:var(--red);}
.box.good{border-color:rgba(0,255,178,.55);}
.box.good .bl{color:var(--verde);}
.box.promptish{border-color:var(--verde);margin-top:16px;}
.box.promptish .bl{color:var(--verde);}

/* ── cuándo usarlo ── */
.neg{margin-top:22px;}
.neg-item{display:flex;align-items:center;gap:14px;margin-top:12px;}
.neg-x{
  width:34px;height:34px;border-radius:50%;background:var(--red);color:#fff;
  display:flex;align-items:center;justify-content:center;
  font-family:var(--pop);font-weight:800;font-size:18px;flex:0 0 auto;
}
.neg-item span{font-family:var(--cond);font-size:30px;color:#2a2f2c;text-align:left;}
.pos{margin-top:28px;}
.pos-intro{font-family:var(--cond);font-size:30px;color:#3a3f3c;text-align:left;}
.pills{margin-top:16px;display:flex;flex-wrap:wrap;gap:12px;}
.pill{
  display:inline-flex;align-items:center;gap:10px;padding:12px 18px;border-radius:999px;
  border:2px solid rgba(0,255,178,.55);background:rgba(0,255,178,.08);
  font-family:var(--cond);font-size:26px;color:#0A0A0A;
}
.pill i{
  width:22px;height:22px;border-radius:50%;background:var(--verde);color:#04130b;
  display:inline-flex;align-items:center;justify-content:center;
  font-family:var(--pop);font-weight:800;font-size:14px;font-style:normal;
}
.value-box{
  margin-top:34px;border:3px solid var(--verde);border-radius:16px;padding:26px;
  background:#0A0A0A;text-align:center;
  font-family:var(--anton);font-weight:400;font-size:36px;color:#F2F2F2;letter-spacing:1px;
}

/* ── CTA final ── */
.cta{padding:90px 64px 0;display:flex;flex-direction:column;align-items:center;text-align:center;}
.cta .cd-wrap{margin-top:8px;}
.cta-kicker{margin-top:54px;font-family:var(--mono);font-size:22px;letter-spacing:3px;color:#B8860B;}
.cta-line{margin-top:18px;font-family:var(--impact);font-weight:900;font-size:76px;color:#0A0A0A;line-height:1;letter-spacing:1px;text-transform:uppercase;}
.cta-kw{
  margin-top:6px;font-family:var(--impact);font-weight:900;font-size:128px;line-height:.95;
  color:var(--verde);letter-spacing:2px;text-transform:uppercase;
}
.cta-sub{margin-top:22px;font-family:var(--cond);font-size:34px;color:#3a3f3c;max-width:820px;}
.cta-sub .hl{color:var(--verde);font-weight:700;}
"""


def brand_footer():
    return (
        '<div class="foot-brand">sebastian.stlabs.ar'
        '<span class="sep"> | </span><span class="tag">RevOps</span></div>'
    )


def top(label: str) -> str:
    return f'<div class="topbar"><span>{label}</span></div>'


def prompt_box(text: str) -> str:
    return (
        '<div class="prompt"><div class="ph"><i></i><i></i><i></i> PROMPT</div>'
        f"<p>{text}</p></div>"
    )


def wrap(idx: int, inner: str, *, cover=False) -> str:
    # sin bridges, sin contador; footer propio (clon) + firma kit desactivada
    html = chrome(idx, inner, total=TOTAL, bridges=None, footer=False)
    html = html.replace('class="slide"', 'class="slide lino"', 1)
    # añadir footer de marca clon
    html = html.replace("</section>", brand_footer() + "</section>", 1)
    return html


def slide1():
    star = (
        '<svg class="fable-star" viewBox="0 0 64 64" fill="currentColor" aria-hidden="true">'
        '<path d="M32 4l5.2 16.2H54l-13.4 9.8 5.1 16.2L32 36.4 18.3 46.2l5.1-16.2L10 20.2h16.8z"/>'
        "</svg>"
    )
    return wrap(
        1,
        f"""
<div class="cover">
  <div class="cd-label">CUENTA REGRESIVA AL IMPACTO</div>
  <div class="cd-wrap"><div class="cd-digits">00:00:07</div></div>
  <div class="fable-logo">{star}<div class="fable-name">FABLE 5</div></div>
  <h1 class="cover-title">ANTES DE QUE<br><span class="hl">SE ACABE EL</span><br>TIEMPO</h1>
  <p class="cover-sub">5 usos que tenés que probar ahora</p>
</div>
""",
        cover=True,
    )


def slide2():
    return wrap(
        2,
        f"""
{top("FABLE 5 · USO 01")}
<div class="pad">
  <div class="h-title"><div class="num">1</div><div class="txt">CREÁ TU PROPIA <span class="hl">APP</span></div></div>
  <p class="lead">No empieces con algo perfecto. Pedile que construya una primera versión funcional de esa herramienta que siempre necesitaste:</p>
  <ul class="bullets">
    <li>Gestor de tareas</li>
    <li>Calendario</li>
    <li>Sistema de notas</li>
    <li>Temporizador de concentración</li>
  </ul>
  {prompt_box("Creá una aplicación personal de productividad con lista de tareas, calendario, notas y temporizador de concentración. Conectá todas las funciones y seguí probando hasta que el flujo completo funcione.")}
</div>
""",
    )


def slide3():
    return wrap(
        3,
        f"""
{top("FABLE 5 · USO 02")}
<div class="pad">
  <div class="h-title"><div class="num">2</div><div class="txt">CONSTRUÍ TU <span class="hl">CLON</span> DE CONTENIDO</div></div>
  <p class="lead">Dale ejemplos reales de cómo escribís y pedile que identifique:</p>
  <ul class="bullets">
    <li>Tu tono</li>
    <li>Tus expresiones</li>
    <li>Tu estructura</li>
    <li>Las palabras que nunca usarías</li>
  </ul>
  <p class="lead">Después va a ayudarte a preparar publicaciones, guiones y respuestas <span class="hl">sin sonar genérico</span>.</p>
  {prompt_box("Analizá estas 30 publicaciones y detectá mi tono, estructura, vocabulario y patrones. Creá una guía de estilo y usala para redactar una semana de contenido que suene como yo.")}
</div>
""",
    )


def slide4():
    return wrap(
        4,
        f"""
{top("FABLE 5 · USO 03")}
<div class="pad">
  <div class="h-title"><div class="num">3</div><div class="txt">INVESTIGÁ <span class="hl">100 LEADS</span> DE UNA VEZ</div></div>
  <p class="lead">En lugar de investigar posibles clientes uno por uno, creá un <span class="hl">sistema</span> que:</p>
  <ul class="bullets">
    <li>Encuentre empresas relevantes</li>
    <li>Analice cada una</li>
    <li>Identifique una oportunidad real</li>
    <li>Prepare un mensaje personalizado</li>
    <li>Compruebe el resultado antes de entregarlo</li>
  </ul>
  {prompt_box("Encontrá 100 clientes potenciales para mi oferta. Investigá cada empresa, identificá una necesidad concreta y redactá un mensaje breve y personalizado. Sumá un segundo agente que compruebe cada dato antes de aprobarlo.")}
</div>
""",
    )


def slide5():
    return wrap(
        5,
        f"""
{top("FABLE 5 · USO 04")}
<div class="pad">
  <div class="h-title"><div class="num">4</div><div class="txt">CONVERTÍ UN PROYECTO EN UN <span class="hl">PLAN EJECUTABLE</span></div></div>
  <p class="lead">Dale una idea compleja y pedile que la convierta en:</p>
  <ul class="bullets-2col">
    <li>Fases</li>
    <li>Decisiones clave</li>
    <li>Riesgos</li>
    <li>Tareas</li>
    <li>Dependencias</li>
    <li>Resultado final</li>
  </ul>
  <p class="lead" style="margin-top:22px">No solo vas a tener una lista. Vas a tener un <span class="hl">sistema que cualquier persona o agente</span> pueda ejecutar paso a paso.</p>
  {prompt_box("Planificá este proyecto completo. Dividí el trabajo en fases, tareas, decisiones, riesgos y preguntas pendientes. Hacé que el plan sea tan claro que otra persona pueda ejecutarlo sin contexto adicional.")}
</div>
""",
    )


def slide6():
    return wrap(
        6,
        f"""
{top("FABLE 5 · USO 05")}
<div class="pad" style="padding-top:110px">
  <div class="h-title"><div class="num">5</div><div class="txt">AUTOMATIZÁ UN PROCESO <span class="hl">COMPLETO</span></div></div>
  <p class="lead">No le pidas una tarea. <span class="hl">Pedile el sistema entero.</span></p>
  <div class="box bad"><div class="bl">× EN LUGAR DE</div><p>Escribí este correo.</p></div>
  <div class="box good"><div class="bl">✓ PROBÁ CON</div><p>Investigá el contexto, redactá el correo, comprobá los datos, adaptá el tono y prepará el seguimiento.</p></div>
  <div class="box promptish"><div class="bl">••• PROMPT</div><p>Diseñá y ejecutá un flujo completo para esta tarea. Primero analizá el objetivo, después investigá la información necesaria, creá el resultado, revisalo con criterios claros y mejorá cualquier parte que no cumpla el estándar.</p></div>
</div>
""",
    )


def slide7():
    return wrap(
        7,
        f"""
{top("FABLE 5 · CUÁNDO USARLO")}
<div class="pad">
  <div class="h-title" style="display:block;font-size:52px;margin-top:10px">
    <div class="txt">FABLE 5 <span class="hl">NO ES</span> PARA PREGUNTAS SIMPLES</div>
  </div>
  <p class="lead">No gastes su capacidad en:</p>
  <div class="neg">
    <div class="neg-item"><div class="neg-x">×</div><span>Resumir tres párrafos</span></div>
    <div class="neg-item"><div class="neg-x">×</div><span>Corregir una frase</span></div>
    <div class="neg-item"><div class="neg-x">×</div><span>Buscar una definición</span></div>
    <div class="neg-item"><div class="neg-x">×</div><span>Escribir un correo básico</span></div>
  </div>
  <div class="pos">
    <p class="pos-intro">Usalo para trabajos que necesiten:</p>
    <div class="pills">
      <span class="pill"><i>✓</i>Contexto</span>
      <span class="pill"><i>✓</i>Planificación</span>
      <span class="pill"><i>✓</i>Herramientas</span>
      <span class="pill"><i>✓</i>Varias etapas</span>
      <span class="pill"><i>✓</i>Revisión autónoma</span>
    </div>
  </div>
  <div class="value-box">MÁS COMPLEJIDAD = MÁS VALOR</div>
</div>
""",
    )


def slide8():
    return wrap(
        8,
        f"""
<div class="cta">
  <div class="cd-label">CUENTA REGRESIVA AL IMPACTO</div>
  <div class="cd-wrap"><div class="cd-digits">00:00:07</div></div>
  <div class="cta-kicker">EMPEZÁ HOY</div>
  <div class="cta-line">Comentá</div>
  <div class="cta-kw">{KEYWORD}</div>
  <p class="cta-sub">y te enviamos los <span class="hl">5 prompts</span> para que empieces HOY.</p>
</div>
""",
        cover=True,
    )


def main():
    slides = [slide1(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7(), slide8()]
    write_html(slides, BUILD / "carrusel.html", extra_css=EXTRA_CSS)
    print("HTML:", BUILD / "carrusel.html")
    pngs = render(BUILD)
    print(f"Render OK: {len(pngs)} PNGs")

    meta = {
        "titulo": "Fable 5 Antes De Que Se Acabe El Tiempo",
        "slides": TOTAL,
        "fondo": "lino_tela",
        "familia_visual": "before_after",
        "origen": "screenshot",
        "keyword_portada": KEYWORD,
        "modo_fondo": "blanco",
        "feedback": {"estado": "borrador"},
    }
    out = package(BUILD, "STLabs-Fable5-AntesDelTiempo", meta=meta)
    print("Package:", out)

    # Entrega limpia en Word/ (reemplaza contenido previo)
    if WORD_DIR.exists():
        for p in WORD_DIR.iterdir():
            if p.is_file():
                p.unlink()
    WORD_DIR.mkdir(parents=True, exist_ok=True)
    for name in (
        "STLabs-Fable5-AntesDelTiempo.html",
        "STLabs-Fable5-AntesDelTiempo.zip",
        "_preview-tira.png",
        "manifest.json",
        *[f"slide-{i:02d}.png" for i in range(1, TOTAL + 1)],
    ):
        src = out / name
        if src.exists():
            shutil.copy2(src, WORD_DIR / name)

    (WORD_DIR / "MANIFIESTO-FUENTES.md").write_text(
        """# Manifiesto de fuentes — Fable 5 Antes Del Tiempo

| Fuente | Peso / estilo | Rol | Origen | Código / comando de carga |
|---|---|---|---|---|
| Impact | 900 Super-Heavy | títulos portada / CTA | `fonts/Impact.ttf` | `@font-face` base64 en HTML |
| Anton | 400 Ultra-Heavy | títulos de usos / value box | `fonts/Anton-Regular.ttf` | `@font-face` base64 |
| Bebas Neue | 400 | dígitos countdown | `fonts/BebasNeue-Regular.ttf` | `@font-face` base64 |
| Barlow Condensed | 400–700 | cuerpo, prompts, bullets | `fonts/BarlowCondensed-*.ttf` | `@font-face` base64 |
| IBM Plex Mono | 400–600 | labels, footer | `fonts/IBMPlexMono-*.ttf` | `@font-face` base64 |

Modo: **blanco** · Textura: **lino/tela** · Familia: **before_after** · Origen: screenshot
Firma: `sebastian.stlabs.ar` · Sin contador de slides · Keyword: FABLE
""",
        encoding="utf-8",
    )
    (WORD_DIR / "LEEME.txt").write_text(
        f"""Carrusel STLabs — Fable 5 Antes De Que Se Acabe El Tiempo
Clon de referencia centeia.education → identidad sebastian.stlabs.ar
Modo fondo: BLANCO · Textura: lino_tela · Familia: before_after
Slides: {TOTAL} · Keyword: {KEYWORD}

Archivos:
- slide-01.png … slide-08.png (retina 2160×2700)
- _preview-tira.png
- STLabs-Fable5-AntesDelTiempo.html / .zip
- MANIFIESTO-FUENTES.md · manifest.json
""",
        encoding="utf-8",
    )
    (WORD_DIR / "BYTEPOST.txt").write_text(
        """Hay decisiones que no esperan a que “tengas tiempo”.
Se van. Y con ellas, la versión de vos que podía haber empezado hoy.

Alita no aparece cuando todo está perfecto:
aparece cuando elegís moverte aunque todavía tiemble la mano.

No es más información.
Es atreverse a construir.

Comentá FABLE.

#EmpezáHoy
""",
        encoding="utf-8",
    )
    print("Word/ listo:", WORD_DIR)


if __name__ == "__main__":
    main()
