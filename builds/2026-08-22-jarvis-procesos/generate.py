# -*- coding: utf-8 -*-
"""Carrusel STLabs — TURBO OS (10 slides, fondo negro).
Sistema: sistema-carrusel-stlabs.json + skill carrusel-stlabs.
Copy: Sebastián te genera el Turbo · CTA PROCESOS.
"""
from __future__ import annotations
import base64, json
from pathlib import Path

B = Path(__file__).resolve().parent
A = B / "assets"
FONTS = Path("/tmp/stlabs-fonts")
G = "#00FFB2"
W = "#F2F2F2"
BG = "#0A0A0A"


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode()


def font_css() -> str:
    faces = [
        ("Bebas Neue", "BebasNeue-Regular.ttf", 400, "normal"),
        ("Poppins", "Poppins-ExtraBold.ttf", 800, "normal"),
        ("Poppins", "Poppins-Bold.ttf", 700, "normal"),
        ("IBM Plex Mono", "IBMPlexMono-SemiBold.ttf", 600, "normal"),
        ("IBM Plex Mono", "IBMPlexMono-Medium.ttf", 500, "normal"),
        ("Barlow Condensed", "BarlowCondensed-Medium.ttf", 500, "normal"),
        ("Barlow Condensed", "BarlowCondensed-Bold.ttf", 700, "normal"),
        ("Lora", "Lora-Italic-Variable.ttf", "400 700", "italic"),
    ]
    out = []
    for fam, fn, w, st in faces:
        data = b64(FONTS / fn)
        out.append(
            f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{w};"
            f"font-display:block;src:url(data:font/ttf;base64,{data}) format('truetype');}}"
        )
    return "\n".join(out)


PARTICLE_BG = b64(A / "sebastian-jarvis-particles.png")
GRAPH = b64(A / "vault-graph.png")
SEB = b64(A / "seb.jpg")

CSS = f"""
{font_css()}
*{{box-sizing:border-box;margin:0;padding:0;-webkit-font-smoothing:antialiased;font-synthesis:none;}}
html,body{{background:#000;}}
.sheet{{display:flex;flex-direction:column;gap:40px;padding:32px;width:max-content;}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{BG};color:{W};}}
.tex{{position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:linear-gradient(rgba(0,255,178,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(0,255,178,.04) 1px,transparent 1px);
  background-size:60px 60px;
  -webkit-mask-image:radial-gradient(ellipse 80% 70% at 50% 40%,#000 25%,transparent 80%);
  mask-image:radial-gradient(ellipse 80% 70% at 50% 40%,#000 25%,transparent 80%);}}
.glow{{position:absolute;border-radius:50%;pointer-events:none;z-index:0;}}
.gtr{{top:-200px;right:-160px;width:560px;height:560px;background:radial-gradient(circle,rgba(0,255,178,.28),rgba(0,255,178,.08) 45%,transparent 70%);}}
.gbl{{bottom:-180px;left:-140px;width:520px;height:520px;background:radial-gradient(circle,rgba(0,255,178,.18),rgba(0,255,178,.05) 45%,transparent 72%);}}
.firma{{position:absolute;left:0;right:0;bottom:72px;text-align:center;z-index:20;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:22px;letter-spacing:.14em;color:{G};}}
.content{{position:absolute;left:72px;right:72px;top:96px;bottom:130px;z-index:5;}}
.badge{{display:inline-block;font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:18px;
  letter-spacing:.16em;text-transform:uppercase;color:{BG};background:{G};padding:10px 18px;border-radius:999px;}}
.badge.ghost{{background:transparent;color:{G};border:1.5px solid {G};}}
.title{{font-family:'Poppins',sans-serif;font-weight:800;font-size:78px;line-height:.95;letter-spacing:-.03em;color:{W};}}
.title.sm{{font-size:64px;}} .title.xs{{font-size:54px;}}
.title .g{{color:{G};}}
.rule{{width:120px;height:5px;background:{G};border-radius:2px;margin:22px 0 18px;}}
.sub{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:32px;line-height:1.3;color:#9aa39c;max-width:920px;}}
.sub b{{color:{W};font-weight:700;}}
.note{{background:#161616;border:1px dashed rgba(0,255,178,.45);border-radius:14px;padding:16px 18px;
  font-family:'IBM Plex Mono',monospace;font-size:18px;letter-spacing:.04em;color:{G};line-height:1.4;}}
.stack{{display:flex;flex-direction:column;gap:14px;margin-top:22px;}}
.row{{display:flex;align-items:center;gap:18px;background:#121212;border:1px solid #2A2A2A;border-radius:16px;padding:16px 20px;}}
.ico{{width:58px;height:58px;border-radius:14px;background:#1A1A1A;border:1px solid rgba(0,255,178,.25);
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
  font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:20px;color:{G};}}
.row .t{{font-family:'Poppins',sans-serif;font-weight:700;font-size:24px;color:{W};}}
.row .d{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:22px;color:#9aa39c;}}
.term{{margin-top:18px;background:#111;border:1px solid #2A2A2A;border-radius:16px;padding:16px 20px;
  font-family:'IBM Plex Mono',monospace;font-size:20px;line-height:1.55;}}
.term .dots{{display:flex;gap:8px;margin-bottom:12px;}}
.term .dots i{{width:11px;height:11px;border-radius:50%;display:block;}}
.term .dots i:nth-child(1){{background:#FF5F57;}}
.term .dots i:nth-child(2){{background:#FEBC2E;}}
.term .dots i:nth-child(3){{background:#28C840;}}
.term .ln{{color:{G};}} .term .hi{{color:#7FDFFF;}}
.bullet{{display:flex;gap:14px;align-items:flex-start;margin-top:14px;}}
.bullet .m{{width:34px;height:34px;border-radius:50%;border:2px solid {G};color:{G};display:flex;align-items:center;
  justify-content:center;flex-shrink:0;font-family:'IBM Plex Mono',monospace;font-size:15px;font-weight:600;}}
.bullet .m.x{{border-color:#FF6B6B;color:#FF6B6B;}}
.bullet .txt{{font-family:'Barlow Condensed',sans-serif;font-size:28px;line-height:1.3;color:{W};}}
.bullet .txt em{{font-style:normal;color:{G};font-weight:700;}}
.bullet .txt b{{color:{W};}}
.hud{{background:#0D0D0D;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;font-family:'IBM Plex Mono',monospace;}}
.hud-bar{{display:flex;align-items:center;gap:8px;padding:12px 16px;background:#151515;border-bottom:1px solid #2A2A2A;
  font-size:14px;color:#9aa39c;letter-spacing:.08em;}}
.hud-body{{padding:14px;display:grid;grid-template-columns:1.1fr 1fr 1fr;gap:12px;}}
.hud-panel{{background:#121212;border:1px solid #242424;border-radius:12px;padding:12px;}}
.hud-panel h4{{font-size:13px;letter-spacing:.12em;color:{G};margin-bottom:8px;text-transform:uppercase;}}
.hud-panel p{{font-size:15px;color:#c8c8c8;line-height:1.35;margin-bottom:4px;}}
.hud-stat{{font-size:22px;font-weight:600;color:{W};}}
.sphere{{height:140px;border-radius:12px;border:1px solid rgba(0,255,178,.2);
  background:radial-gradient(circle at 50% 45%,rgba(0,255,178,.55),rgba(40,120,255,.25) 40%,#0A0A0A 70%);}}
.steps{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:22px;}}
.step{{background:#121212;border:1px solid #2A2A2A;border-radius:18px;padding:20px;}}
.step .n{{font-family:'IBM Plex Mono',monospace;font-size:16px;color:{G};letter-spacing:.14em;}}
.step .tt{{font-family:'Poppins',sans-serif;font-weight:800;font-size:26px;margin-top:8px;}}
.step .dd{{font-family:'Barlow Condensed',sans-serif;font-size:22px;color:#9aa39c;margin-top:6px;line-height:1.25;}}
.table{{width:100%;border-collapse:separate;border-spacing:0;margin-top:18px;border:1px solid #2A2A2A;border-radius:18px;overflow:hidden;}}
.table th{{background:#151515;font-family:'IBM Plex Mono',monospace;font-size:15px;letter-spacing:.12em;color:{G};
  text-align:left;padding:12px 16px;text-transform:uppercase;}}
.table td{{background:#101010;border-top:1px solid #222;padding:14px 16px;font-family:'Barlow Condensed',sans-serif;font-size:24px;vertical-align:top;}}
.table td.t{{font-family:'IBM Plex Mono',monospace;font-size:18px;color:{G};width:160px;}}
.table td b{{color:{W};font-weight:700;display:block;margin-bottom:2px;font-family:'Poppins',sans-serif;font-size:20px;}}
.table td span{{color:#9aa39c;font-size:20px;}}
.cover-bg{{position:absolute;inset:0;z-index:0;width:100%;height:100%;object-fit:cover;}}
.cover-scrim{{position:absolute;inset:0;z-index:1;pointer-events:none;
  background:linear-gradient(90deg,rgba(10,10,10,.92) 0%,rgba(10,10,10,.78) 42%,rgba(10,10,10,.35) 68%,rgba(10,10,10,.55) 100%),
  linear-gradient(180deg,rgba(10,10,10,.25) 0%,transparent 28%,rgba(10,10,10,.55) 100%);}}
.cover{{position:relative;z-index:5;display:flex;flex-direction:column;justify-content:center;height:100%;max-width:620px;}}
.cover .row{{background:rgba(18,18,18,.72);backdrop-filter:blur(6px);}}
.cover .term{{background:rgba(17,17,17,.78);backdrop-filter:blur(6px);}}
.profile{{display:flex;align-items:center;gap:22px;background:#141414;border:1px solid #2A2A2A;border-radius:22px;padding:22px;}}
.profile img{{width:110px;height:110px;border-radius:50%;object-fit:cover;border:3px solid {G};}}
.profile .name{{font-family:'Poppins',sans-serif;font-weight:800;font-size:32px;}}
.profile .bio{{font-family:'Barlow Condensed',sans-serif;font-size:24px;color:#9aa39c;margin-top:6px;}}
.profile .handle{{font-family:'IBM Plex Mono',monospace;font-size:18px;color:{G};margin-top:8px;letter-spacing:.08em;}}
.cta-box{{margin-top:36px;border:3px solid {G};border-radius:22px;padding:32px 24px;text-align:center;}}
.cta-box .kw{{font-family:'Poppins',sans-serif;font-weight:800;font-size:64px;letter-spacing:.12em;color:{G};}}
.cta-box .hint{{margin-top:16px;font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:28px;color:{W};}}
.quad{{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:12px;margin-top:28px;}}
.quad .row{{flex-direction:column;text-align:center;gap:8px;padding:16px 10px;}}
.quad .t{{font-size:18px;}}
"""


def chrome() -> str:
    return (
        '<div class="tex"></div><div class="glow gtr"></div><div class="glow gbl"></div>'
        '<div class="firma">sebastian.stlabs.ar</div>'
    )


def build() -> str:
    slides = []

    slides.append(f"""
<section class="slide" data-id="01">
  <img class="cover-bg" src="data:image/png;base64,{PARTICLE_BG}" alt=""/>
  <div class="cover-scrim"></div>
  <div class="firma">sebastian.stlabs.ar</div>
  <div class="content cover">
      <div class="badge">TURBO A MEDIDA</div>
      <h1 class="title" style="margin-top:24px">Te genero<br>tu <span class="g">TURBO</span><br>OS</h1>
      <div class="rule"></div>
      <p class="sub">Con el último paso, te funciona<br><b>todo el día</b>.</p>
      <div class="stack">
        <div class="row"><div class="ico">01</div><div><div class="t">CLAUDE CODE</div><div class="d">El motor</div></div></div>
        <div class="row"><div class="ico">02</div><div><div class="t">OBSIDIAN</div><div class="d">La memoria</div></div></div>
        <div class="row"><div class="ico">03</div><div><div class="t">VOZ LOCAL</div><div class="d">Oídos + boca</div></div></div>
        <div class="row"><div class="ico">04</div><div><div class="t">UNA INTERFAZ</div><div class="d">El rostro</div></div></div>
      </div>
      <div class="term">
        <div class="dots"><i></i><i></i><i></i></div>
        <div class="ln">&gt; hablar</div>
        <div class="ln">&gt; ejecutar</div>
        <div class="ln">&gt; recordar</div>
        <div class="hi">&gt; TE FUNCIONA TODO EL DÍA_</div>
      </div>
  </div>
</section>""")

    slides.append(f"""
<section class="slide" data-id="02">{chrome()}
  <div class="content">
    <div class="badge ghost">QUÉ ES</div>
    <h1 class="title" style="margin-top:22px">¿Qué es<br><span class="g">esto</span>?</h1>
    <div class="rule"></div>
    <div class="note">UNA VOZ. CADA FLUJO DE TRABAJO. CERO PESTAÑAS.</div>
    <p class="sub" style="margin-top:28px">Vos <b>hablás</b>. TURBO ejecuta el trabajo.</p>
    <div class="bullet"><div class="m">▸</div><div class="txt">Claude Code es el <em>motor</em>. Obsidian es la <em>memoria</em>.</div></div>
    <div class="bullet"><div class="m">▸</div><div class="txt">Armado con Fable 5 — corre en <em>cualquier modelo local</em>.</div></div>
    <div class="bullet"><div class="m">▸</div><div class="txt">Totalmente modular. Intercambiás cualquier pieza.</div></div>
    <div class="quad">
      <div class="row"><div class="ico">01</div><div class="t">HABLAR</div></div>
      <div class="row"><div class="ico">02</div><div class="t">ENRUTAR</div></div>
      <div class="row"><div class="ico">03</div><div class="t">EJECUTAR</div></div>
      <div class="row"><div class="ico">04</div><div class="t">RECORDAR</div></div>
    </div>
    <p class="sub" style="margin-top:28px">Sebastián te lo <b>genera</b>. No tenés que armarlo vos.</p>
  </div>
</section>""")

    slides.append(f"""
<section class="slide" data-id="03">{chrome()}
  <div class="content">
    <div class="badge ghost">CÓMO FUNCIONA</div>
    <h1 class="title sm" style="margin-top:20px">¿Cómo<br><span class="g">funciona</span>?</h1>
    <div class="rule"></div>
    <div class="bullet"><div class="m x">✕</div><div class="txt"><b>Forma antigua:</b> manejás cada herramienta a mano. Pestañas. Tipeo. Contexto perdido.</div></div>
    <div class="bullet"><div class="m">✓</div><div class="txt"><b>Nueva forma:</b> una capa de voz. Hablás y se ejecuta la habilidad correcta. La respuesta vuelve hablada.</div></div>
    <div class="bullet"><div class="m">↻</div><div class="txt">El ciclo: <em>Voz → TURBO → Claude Code → habilidad → respuesta hablada</em>.</div></div>
    <div class="note" style="margin-top:18px">LA VENTAJA · Sin cambio de contexto · Sin notas perdidas · Sin base de datos · Solo markdown</div>
    <div class="hud" style="margin-top:18px">
      <div class="hud-bar"><span style="color:{G}">●</span>&nbsp; BÓVEDA — INTELIGENCIA CENTRALIZADA</div>
      <div class="hud-body">
        <div class="hud-panel"><h4>Vitales</h4><p class="hud-stat">135.000</p><p>subs</p><p class="hud-stat">202K</p><p>consultas</p></div>
        <div class="hud-panel"><div class="sphere"></div><p style="margin-top:10px;text-align:center;color:{G}">SISTEMA VITAL</p></div>
        <div class="hud-panel"><h4>Resueltos</h4><p class="hud-stat">17K</p><p>errores</p><p style="margin-top:12px;color:{G}">Respondé con respuestas.<br>No abras pestañas.</p></div>
      </div>
    </div>
  </div>
</section>""")

    slides.append(f"""
<section class="slide" data-id="04">{chrome()}
  <div class="content">
    <div class="badge">EL MÉTODO</div>
    <h1 class="title sm" style="margin-top:22px">Los 4 pasos<br>con los que<br><span class="g">genero</span> tu Turbo</h1>
    <div class="rule"></div>
    <p class="sub">No es un tutorial para que lo armes solo.<br>Es el proceso que usa Sebastián para <b>generártelo</b>.</p>
    <div class="steps">
      <div class="step"><div class="n">PASO 01</div><div class="tt">Cablear el cerebro</div><div class="dd">Skills en Claude Code. Cada habilidad = un SKILL.md</div></div>
      <div class="step"><div class="n">PASO 02</div><div class="tt">Construir la memoria</div><div class="dd">Bóveda Obsidian. Si no está en la bóveda, no pasó.</div></div>
      <div class="step"><div class="n">PASO 03</div><div class="tt">Conectar la voz</div><div class="dd">Oídos + boca locales. Hablás. Ejecuta. Responde.</div></div>
      <div class="step"><div class="n">PASO 04</div><div class="tt">Construir la cara</div><div class="dd">HUD de una sola pantalla. Sin pestañas.</div></div>
    </div>
  </div>
</section>""")

    slides.append(f"""
<section class="slide" data-id="05">{chrome()}
  <div class="content">
    <div class="badge ghost">PASO 01</div>
    <h1 class="title sm" style="margin-top:16px">Cableá el<br><span class="g">cerebro</span></h1>
    <div class="rule"></div>
    <div class="note">LAS HABILIDADES SON LAS CÉLULAS CEREBRALES.</div>
    <div class="bullet"><div class="m">01</div><div class="txt"><b>Qué es:</b> Claude Code + carpeta de habilidades. Cada una = un SKILL.md. Se activa solo cuando hace falta.</div></div>
    <div class="bullet"><div class="m">02</div><div class="txt"><b>Primeras cinco:</b> métricas · bandeja · tendencias · plan · bóveda</div></div>
    <div class="bullet"><div class="m">03</div><div class="txt"><b>La regla:</b> habilidades chicas, de un solo propósito, le ganan a un prompt gigante.</div></div>
    <div class="hud" style="margin-top:18px">
      <div class="hud-bar">PANEL DE COMANDOS IDLE · 0/3 ACTIVOS · 0 EN COLA</div>
      <div class="hud-body" style="grid-template-columns:1fr 1fr">
        <div class="hud-panel"><p style="color:{G}">EXTRAER MÉTRICAS</p><p style="color:{G}">RESUMEN BANDEJA</p><p style="color:{G}">ESCANEO TENDENCIAS</p><p style="color:{G}">PLAN DE HOY</p><p style="color:{G}">REVISIÓN SEMANAL</p></div>
        <div class="hud-panel"><p style="color:{G}">REPORTE AM</p><p style="color:{G}">TENDENCIAS GH</p><p style="color:{G}">YT SEMANAL</p><p style="color:{G}">PLAN MAÑANA</p><p style="color:{G}">LIMPIEZA BÓVEDA</p></div>
      </div>
    </div>
  </div>
</section>""")

    slides.append(f"""
<section class="slide" data-id="06">{chrome()}
  <div class="content">
    <div class="badge ghost">PASO 02</div>
    <h1 class="title sm" style="margin-top:16px">Construí la<br><span class="g">memoria</span></h1>
    <div class="rule"></div>
    <div class="note">SI NO ESTÁ EN LA BÓVEDA, NO PASÓ.</div>
    <div class="term">
      <div class="dots"><i></i><i></i><i></i></div>
      <div class="hi">bóveda/</div>
      <div class="ln">&nbsp;&nbsp;raw/ — todo capturado</div>
      <div class="ln">&nbsp;&nbsp;wiki/ — conocimiento depurado</div>
      <div class="ln">&nbsp;&nbsp;outputs/ — todo lo que TURBO entrega</div>
    </div>
    <div class="bullet"><div class="m">1</div><div class="txt">Cada reporte aterriza como Markdown. Sin base de datos.</div></div>
    <div class="bullet"><div class="m">2</div><div class="txt">Las notas se enlazan en un gráfico — el sistema Karpathy.</div></div>
    <div class="bullet"><div class="m">3</div><div class="txt">TURBO consulta el gráfico y responde rápido.</div></div>
    <div class="bullet"><div class="m">4</div><div class="txt">Podés leer todo lo que sabe. Son solo archivos.</div></div>
    <div style="margin-top:14px;border-radius:16px;overflow:hidden;border:1px solid #2A2A2A;height:260px">
      <img src="data:image/png;base64,{GRAPH}" style="width:100%;height:100%;object-fit:cover" alt="grafo"/>
    </div>
  </div>
</section>""")

    slides.append(f"""
<section class="slide" data-id="07">{chrome()}
  <div class="content">
    <div class="badge ghost">PASO 03</div>
    <h1 class="title sm" style="margin-top:16px">Conectá<br>la <span class="g">voz</span></h1>
    <div class="rule"></div>
    <div class="note">TUS OÍDOS + TU BOCA. TODO LOCAL.</div>
    <p class="sub" style="margin-top:16px">Sebastián conecta la capa de voz para que hables con el sistema sin abrir una sola pestaña.</p>
    <div class="steps">
      <div class="step"><div class="n">ENTRADA</div><div class="tt">Escucha</div><div class="dd">Voz local → texto. Sin mandar audio a la nube.</div></div>
      <div class="step"><div class="n">ENRUTEO</div><div class="tt">Elige skill</div><div class="dd">TURBO elige la habilidad correcta según lo que pediste.</div></div>
      <div class="step"><div class="n">SALIDA</div><div class="tt">Responde</div><div class="dd">La respuesta vuelve hablada. Vos seguís en flujo.</div></div>
      <div class="step"><div class="n">MEMORIA</div><div class="tt">Guarda</div><div class="dd">Todo queda escrito en la bóveda. Nada se pierde.</div></div>
    </div>
    <div class="term" style="margin-top:22px">
      <div class="dots"><i></i><i></i><i></i></div>
      <div class="ln">&gt; listening…</div>
      <div class="hi">&gt; skill: plan-de-hoy</div>
      <div class="ln">&gt; speaking: “Tus 3 prioridades ya están en la bóveda.”</div>
    </div>
  </div>
</section>""")

    slides.append(f"""
<section class="slide" data-id="08">{chrome()}
  <div class="content">
    <div class="badge ghost">PASO 04</div>
    <h1 class="title sm" style="margin-top:14px">Construí<br>la <span class="g">cara</span></h1>
    <div class="rule"></div>
    <div class="note">UNA PANTALLA. TODO LO QUE TURBO TIENE QUE SABER.</div>
    <p class="sub" style="margin-top:12px;font-size:28px">Prompt que usa Sebastián para generar el HUD:</p>
    <div class="term" style="font-size:18px">
      “Armá un HUD de terminal oscuro para mi OS: vitales · comandos · agenda · audio · datos de la bóveda. <span class="hi">Una pantalla. Sin pestañas.</span>”
    </div>
    <div class="hud" style="margin-top:14px">
      <div class="hud-bar">V.A.U.L.T. INTELIGENCIA CENTRALIZADA · NÚCLEO · IDEAS · ENLACE · EN LÍNEA</div>
      <div class="hud-body">
        <div class="hud-panel"><h4>Vitales</h4><p class="hud-stat">135K</p><p>señales</p><p class="hud-stat">202K</p><p>consultas</p><p class="hud-stat">17K</p><p>resueltas</p></div>
        <div class="hud-panel"><div class="sphere"></div><p style="margin-top:8px;text-align:center">SEGUIDORES 135.000</p><p style="text-align:center;color:{G}">OBJETIVO 150K</p></div>
        <div class="hud-panel"><h4>Comandos</h4><p style="color:{G}">EXTRAER MÉTRICAS</p><p style="color:{G}">RESUMEN BANDEJA</p><p style="color:{G}">PLAN DE HOY</p><h4 style="margin-top:10px">Agenda</h4><p>09:30 trabajo profundo</p><p>16:30 bloquear carga</p></div>
      </div>
    </div>
    <div class="bullet" style="margin-top:12px"><div class="m">▸</div><div class="txt">Ejecutá. Abrilo. · Ajustá por voz. · Tiempo: una tarde.</div></div>
  </div>
</section>""")

    slides.append(f"""
<section class="slide" data-id="09">{chrome()}
  <div class="content">
    <div class="badge ghost">DÍA REAL</div>
    <h1 class="title sm" style="margin-top:18px">Así se ve<br>un <span class="g">día real</span></h1>
    <div class="rule"></div>
    <div style="display:flex;gap:12px;margin-bottom:6px">
      <div class="note" style="flex:1">TU VOZ ES LA INTERFAZ.</div>
      <div class="note" style="flex:1">LA CONSISTENCIA SE ACUMULA.</div>
    </div>
    <table class="table">
      <tr><th>Hora</th><th>Qué pasa</th></tr>
      <tr><td class="t">7:00</td><td><b>Resumen matutino</b><span>Bandeja, calendario, novedades — se lee en voz alta.</span></td></tr>
      <tr><td class="t">9:00</td><td><b>Plan de hoy</b><span>Las 3 prioridades aterrizan en la bóveda.</span></td></tr>
      <tr><td class="t">14:00</td><td><b>Métricas</b><span>Suscripciones, vistas, seguidores — rastreados.</span></td></tr>
      <tr><td class="t">19:00</td><td><b>Cierre</b><span>Reflexión registrada. Mañana en cola.</span></td></tr>
      <tr><td class="t">Siempre</td><td><b>Preguntá lo que quieras</b><span>La bóveda recuerda todo.</span></td></tr>
    </table>
  </div>
</section>""")

    slides.append(f"""
<section class="slide" data-id="10">{chrome()}
  <div class="content" style="display:flex;flex-direction:column;justify-content:center">
    <div class="profile">
      <img src="data:image/jpeg;base64,{SEB}" alt="Sebastián"/>
      <div>
        <div class="name">Sebastián García</div>
        <div class="bio">RevOps · CRM · agentes a medida</div>
        <div class="handle">sebastian.stlabs.ar</div>
      </div>
    </div>
    <h1 class="title xs" style="margin-top:44px;text-align:center">¿Querés que te<br>genere tu <span class="g">Turbo</span>?</h1>
    <div class="cta-box">
      <div class="kw">PROCESOS</div>
      <div class="hint">Comentá <b style="color:{G}">PROCESOS</b> y te escribo para arrancar.</div>
    </div>
    <p class="sub" style="text-align:center;margin:24px auto 0;max-width:760px">
      Te genero el sistema completo: cerebro, memoria, voz y cara. A medida de tu operación.
    </p>
  </div>
</section>""")

    return "".join(slides)


def main():
    html = (
        "<!DOCTYPE html><html lang='es'><head><meta charset='UTF-8'>"
        "<title>TURBO OS — STLabs</title>"
        f"<style>{CSS}</style></head><body><div class='sheet'>"
        f"{build()}</div></body></html>"
    )
    (B / "carrusel.html").write_text(html, encoding="utf-8")
    meta = {
        "id": "2026-08-22-jarvis-procesos",
        "fecha": "2026-08-22",
        "titulo": "Te genero tu TURBO OS",
        "slides": 10,
        "fondo": "reticula_fina",
        "familia_visual": "dossier_editorial",
        "origen": "screenshot",
        "keyword_portada": "PROCESOS",
        "modo": "negro",
        "notas": "Portada: Sebastián blur + partículas azules. Agente TURBO. CTA PROCESOS. Perfil slide 10.",
    }
    (B / "manifest.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print("OK 10 slides →", B / "carrusel.html")


if __name__ == "__main__":
    main()
