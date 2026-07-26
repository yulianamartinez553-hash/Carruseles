# -*- coding: utf-8 -*-
"""Carrusel STLabs — clon del carrusel 'memoria que nunca olvida' (7 slides),
modo blanco, adaptado en voseo a un agente que vende la marca de Sebastián."""
import sys

sys.path.insert(0, "/workspace")
from stlabs_kit import chrome, write_html  # noqa: E402
from elements import (starburst, diamond, spark, flower_badge, constellation,  # noqa: E402
                      graph_cluster, window, NARANJA, VIOLETA, DORADO, NAVY)

BUILD = "/tmp/build-agente"

CSS = """
/* ── MODO BLANCO STLabs — todos los fondos blancos ── */
.slide{background:#FFFFFF;color:#0A0A0A;}
.slide::after{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
 background:radial-gradient(44% 30% at 50% 34%, rgba(0,255,178,.07), transparent 65%);}
b{color:#0A0A0A;}
.web{left:50%;right:auto;transform:translateX(-50%);width:max-content;opacity:1;
 text-shadow:0 0 1px rgba(0,90,60,.35);}

/* tipografía */
.blk{font-family:'Archivo Black',sans-serif;font-weight:400;color:#0A0A0A;text-align:left;line-height:1.0;}
.ser{font-family:var(--serif);font-style:italic;font-weight:600;color:#0A0A0A;text-align:left;}
.body{font-family:var(--cond);font-weight:500;font-size:35px;line-height:1.34;color:#3c403d;text-align:left;}
.body b{font-weight:700;}
.lab{font-family:var(--mono);font-weight:600;font-size:25px;letter-spacing:4px;}
/* acento de texto: verde de marca (la estrella gráfica sigue naranja) */
.nar{color:#00FFB2;text-shadow:0 0 1px rgba(0,110,75,.45);}

/* badge portada */
.badge-row{display:flex;justify-content:center;align-items:center;gap:14px;
 font-family:var(--mono);font-weight:600;font-size:24px;letter-spacing:4px;color:#0A0A0A;}
.badge-row svg{vertical-align:middle;}
.badge-x{color:#b9b9b1;font-size:20px;}

/* ventana de app */
.win{border-radius:16px;overflow:hidden;box-shadow:0 24px 48px rgba(10,10,10,.22);
 border:1.5px solid #d8d4c8;}
.win-bar{display:flex;align-items:center;gap:9px;background:#EFEBDF;padding:14px 18px;}
.win-bar i{width:15px;height:15px;border-radius:50%;}
.win-bar span{margin-left:12px;font-family:var(--mono);font-size:22px;color:#5a5f5b;}
.win-screen{background:#131720;display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative;}

/* UI del agente (ventana slide 4) */
.ag-h{font-family:'Archivo Black',sans-serif;font-size:34px;color:#F2F2F2;margin-top:18px;}
.ag-sub{font-family:var(--mono);font-size:17px;color:#8b949e;margin-top:10px;}
.ag-pill{font-family:var(--mono);font-size:18px;color:#c9d1d9;background:#1b2130;border:1px solid #2c3446;
 border-radius:12px;padding:12px 20px;margin-top:12px;}
.ag-input{width:78%;font-family:var(--mono);font-size:18px;color:#6a7382;background:#0d1118;
 border:1px solid #2c3446;border-radius:14px;padding:16px 20px;margin-top:24px;text-align:left;}

/* lista numerada slide 5 */
.num-row{display:flex;gap:26px;align-items:flex-start;margin-top:38px;}
.num-row .n{font-family:'Archivo Black',sans-serif;font-size:37px;color:#0A0A0A;line-height:1.15;}
.num-row p{font-family:var(--cond);font-weight:500;font-size:36px;line-height:1.3;color:#2c2f2d;text-align:left;}
.num-row p b{font-weight:700;}

/* círculos slide 6 */
.circ{width:210px;height:210px;border-radius:50%;background:#1A2230;display:flex;align-items:center;
 justify-content:center;box-shadow:0 16px 36px rgba(10,10,10,.2);}
.circ-name{font-family:'Archivo Black',sans-serif;font-size:37px;color:#0A0A0A;margin-top:24px;text-align:center;}
.circ-sub{font-family:var(--serif);font-style:italic;font-weight:500;font-size:25px;color:#6a6f6b;margin-top:6px;text-align:center;}

/* pill CTA slide 7 */
.cta-pill{display:inline-block;background:#E85A24;border-radius:22px;padding:34px 56px;text-align:center;
 box-shadow:0 0 70px rgba(232,90,36,.35);}
.cta-pill .big{font-family:'Archivo Black',sans-serif;font-size:47px;color:#160b05;}
.cta-pill .small{font-family:var(--cond);font-weight:600;font-size:29px;color:#3d1503;margin-top:8px;}

.swipe{position:absolute;left:50%;transform:translateX(-50%);bottom:150px;z-index:5;
 font-family:var(--mono);font-weight:500;font-size:23px;letter-spacing:5px;color:#8a8f8b;}
.wrap{position:absolute;inset:0;padding:150px 92px 0;z-index:3;}
"""

S = []

# ─────────────── SLIDE 1 — Portada (constelación) ───────────────
S.append(constellation() + f'''
<div style="position:absolute;left:0;right:0;top:262px;z-index:5;">
  <div class="badge-row" style="width:max-content;margin:0 auto;">{diamond(26)} CRM <span class="badge-x">&times;</span>
   {spark(26)} AGENTE <span class="badge-x">&times;</span>
   {starburst(26, arms=9, thick=13)} CLAUDE</div>
</div>
<div style="position:absolute;left:0;right:0;top:352px;text-align:center;z-index:5;">
  <div class="blk" style="font-size:116px;text-align:center;letter-spacing:1px;width:max-content;margin:0 auto;">LE CONSTRU&Iacute;<br>A CLAUDE</div>
  <div class="ser nar" style="font-size:92px;line-height:1.04;text-align:center;margin-top:18px;width:max-content;margin-left:auto;margin-right:auto;">
    una memoria que<br>nunca olvida.</div>
</div>
<div style="position:absolute;left:150px;right:150px;top:872px;z-index:5;">
  <div class="body" style="text-align:center;font-size:36px;">Un segundo cerebro que no solo guarda tus datos:
   <b>los lee, los conecta y aprende a vender tu marca</b> cada d&iacute;a.</div>
</div>
<div class="swipe">DESLIZ&Aacute; PARA VER C&Oacute;MO &rarr;</div>
''')

# ─────────────── SLIDE 2 — un solo lugar (estrella naranja grande) ───────────────
S.append(f'''
<div style="position:absolute;right:64px;top:96px;z-index:4;">{starburst(330, arms=8, thick=17)}</div>
<div class="wrap" style="padding-top:472px;">
  <div class="blk" style="font-size:97px;">un solo lugar<br>para cada pieza<br>de <span class="nar">contexto.</span></div>
  <div class="ser" style="font-size:41px;line-height:1.38;margin-top:44px;max-width:880px;">
    Llamadas, correos, propuestas, notas de voz &mdash; todo en una sola b&oacute;veda que tu IA
    puede leer de verdad. Nada se pierde, nada se explica dos veces y cada respuesta se apoya
    en lo que ya sab&eacute;s de tu cliente.</div>
</div>
''')

# ─────────────── SLIDE 3 — la bóveda / tu crm ───────────────
S.append(f'''
<div class="wrap" style="padding-top:132px;">
  <div style="display:flex;align-items:center;gap:14px;">{diamond(30)}
    <span class="lab nar">LA B&Oacute;VEDA</span></div>
  <div class="blk" style="font-size:120px;margin-top:20px;">tu crm</div>
  <div class="ser" style="font-size:40px;margin-top:14px;">Tus clientes, como un grafo conectado.</div>
  <div class="body" style="margin-top:30px;max-width:880px;">Una base ordenada donde todo es <b>dato tuyo</b>.
   Conect&aacute; cada contacto con sus llamadas y propuestas, y tu cartera se convierte en un
   <b>mapa vivo</b> en lugar de un cementerio de carpetas.</div>
</div>
<div style="position:absolute;left:50%;transform:translateX(-50%);top:706px;z-index:5;">
  {window("CRM &mdash; Vista de grafo", graph_cluster(), width=880, screen_h=440)}
</div>
''')

# ─────────────── SLIDE 4 — la memoria / el agente ───────────────
S.append(f'''
<div class="wrap" style="padding-top:132px;">
  <div style="display:flex;align-items:center;gap:14px;">{spark(32)}
    <span class="lab" style="color:#c98f1a;">LA MEMORIA</span></div>
  <div class="blk" style="font-size:120px;margin-top:20px;">el agente</div>
  <div class="ser" style="font-size:40px;margin-top:14px;">La IA que lee tu b&oacute;veda y vende tu marca.</div>
  <div class="body" style="margin-top:30px;max-width:900px;">El agente se convierte en <b>memoria viva</b>.
   Preguntale lo que quieras: responde con lo que de verdad pas&oacute; con cada
   cliente, <b>con las fuentes adjuntas</b>.</div>
</div>
<div style="position:absolute;left:50%;transform:translateX(-50%);top:700px;z-index:5;">
  {window("Agente &mdash; Preguntale a tu b&oacute;veda",
          f'<div style="text-align:center;">{starburst(46, arms=9, thick=13)}</div>'
          '<div class="ag-h">&iquest;Con qu&eacute; te ayudo?</div>'
          '<div class="ag-sub">Pregunt&aacute; por clientes, propuestas o seguimientos.</div>'
          '<div class="ag-pill">&iquest;Qu&eacute; objeciones puso Acme en la &uacute;ltima llamada?</div>'
          '<div class="ag-pill">Armame el seguimiento de hoy</div>'
          '<div class="ag-input">Escribile al agente&hellip;</div>',
          width=880, screen_h=440)}
</div>
''')

# ─────────────── SLIDE 5 — aprende solo ───────────────
S.append(f'''
<div style="position:absolute;left:84px;top:96px;z-index:5;">{flower_badge(150)}</div>
<div style="position:absolute;right:64px;top:64px;z-index:4;">{starburst(220, arms=12, thick=9)}</div>
<div class="wrap" style="padding-top:296px;">
  <div class="blk" style="font-size:108px;">aprende solo</div>
  <div class="ser" style="font-size:41px;margin-top:16px;">Cada interacci&oacute;n lo afila.</div>
  <div style="margin-top:26px;max-width:900px;">
    <div class="num-row"><span class="n">1</span><p>Cuanto m&aacute;s vend&eacute;s, <b>m&aacute;s te conoce</b> &mdash;
      tu voz, tus objeciones, tus llamadas pasadas.</p></div>
    <div class="num-row"><span class="n">2</span><p>Lo que repet&iacute;s <b>gana peso</b>. Lo que ignor&aacute;s se apaga.
      La memoria se ajusta sola.</p></div>
    <div class="num-row"><span class="n">3</span><p>El mes uno es una libreta. <b>El mes seis responde como vos.</b></p></div>
  </div>
</div>
''')

# ─────────────── SLIDE 6 — cómo funciona en conjunto ───────────────
S.append(f'''
<div class="wrap" style="padding-top:150px;">
  <div class="blk" style="font-size:104px;">c&oacute;mo funciona<br>en conjunto</div>
</div>
<div style="position:absolute;left:130px;top:560px;z-index:5;text-align:center;width:260px;">
  <div class="circ" style="margin:0 auto;">{diamond(96)}</div>
  <div class="circ-name">CRM</div><div class="circ-sub">tus clientes, conectados</div>
</div>
<div style="position:absolute;left:50%;transform:translateX(-50%);top:646px;z-index:5;width:260px;text-align:center;">
  <svg width="240" viewBox="0 0 120 24" xmlns="http://www.w3.org/2000/svg">
    <line x1="4" y1="12" x2="116" y2="12" stroke="{NARANJA}" stroke-width="3.4" stroke-dasharray="1 9" stroke-linecap="round"/>
    <circle cx="60" cy="12" r="7" fill="{NARANJA}"/></svg>
</div>
<div style="position:absolute;right:130px;top:560px;z-index:5;text-align:center;width:260px;">
  <div class="circ" style="margin:0 auto;">{spark(100)}</div>
  <div class="circ-name">Agente</div><div class="circ-sub">lee + recuerda</div>
</div>
<div style="position:absolute;left:150px;right:150px;top:966px;z-index:5;">
  <div class="body" style="text-align:center;font-size:37px;">El CRM guarda lo que sab&eacute;s. El agente lo lee,
   lo conecta y <b class="nar">se lo pasa a Claude</b> &mdash; as&iacute; cada respuesta
   nace de tu propio negocio.</div>
</div>
''')

# ─────────────── SLIDE 7 — CTA final ───────────────
S.append(f'''
<div class="wrap" style="padding-top:150px;">
  <div style="display:flex;align-items:center;gap:14px;">{starburst(30, arms=9, thick=13)}
    <span class="lab nar">EL SISTEMA COMPLETO</span></div>
  <div class="blk" style="font-size:112px;margin-top:26px;">lo constru&iacute;<br><span class="nar">completo.</span></div>
  <div class="body" style="margin-top:32px;max-width:860px;">La b&oacute;veda, la configuraci&oacute;n del agente y
   <b>cada prompt</b> &mdash; todo escrito.</div>
</div>
<div style="position:absolute;left:92px;top:706px;z-index:5;">
  <div class="cta-pill"><div class="big">Coment&aacute; &laquo;AGENTE&raquo;</div>
    <div class="small">y te mando todo lo que necesit&aacute;s.</div></div>
</div>
<div style="position:absolute;left:92px;right:92px;top:1040px;z-index:5;">
  <div class="body" style="font-size:33px;">&iquest;Quer&eacute;s el <b class="nar">desglose completo</b>,
   paso a paso? Dec&iacute;melo en los comentarios.</div>
</div>
''')

slides = [chrome(i + 1, inner, total=7, bridges=None, footer=True) for i, inner in enumerate(S)]
write_html(slides, f"{BUILD}/carrusel.html", extra_css=CSS)
print(f"HTML escrito: {BUILD}/carrusel.html — {len(slides)} slides")
