# -*- coding: utf-8 -*-
"""Clon STLabs — Sistema vs vigilancia (10 slides)
Tipografía: Poppins 800 títulos + Lora italic acentos
Números grandes partidos por costura (arriba/abajo alternados)
"""
from pathlib import Path
import json

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")


def seam_nums(n: int, total: int = 10) -> str:
    """Mitad derecha del número actual + mitad izquierda del anterior.
    Posición vertical: impar = top, par = bottom.
    """
    parts = []
    # completar número anterior (entra por la izquierda)
    if n > 1:
        prev = n - 1
        pos = "top" if prev % 2 == 1 else "bot"
        parts.append(
            f'<div class="seam-num seam-in seam-{pos}" aria-hidden="true">{prev:02d}</div>'
        )
    # empezar número actual (sale por la derecha)
    if n < total:
        pos = "top" if n % 2 == 1 else "bot"
        parts.append(
            f'<div class="seam-num seam-out seam-{pos}" aria-hidden="true">{n:02d}</div>'
        )
    elif n == total:
        # último: solo completa el anterior; número propio grande interno sutil
        parts.append(
            f'<div class="seam-num seam-solo seam-bot" aria-hidden="true">{n:02d}</div>'
        )
    return "\n".join(parts)


def foot(arrow: bool = True) -> str:
    arr = ""
    if arrow:
        arr = '''<div class="arrow" aria-hidden="true">
      <svg viewBox="0 0 40 24" width="36" height="22"><path d="M2 12 H32 M24 4 L34 12 L24 20" fill="none" stroke="#00FFB2" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </div>'''
    return f'''
    <div class="firma">sebastian.stlabs.ar</div>
    {arr}'''


# ── Icons ──────────────────────────────────────────────────────────
def ico_eye():
    return '''<svg class="ico" viewBox="0 0 120 120" aria-hidden="true">
      <path d="M18 18 H38 M18 18 V38" fill="none" stroke="#00FFB2" stroke-width="3.5" stroke-linecap="round"/>
      <path d="M102 18 H82 M102 18 V38" fill="none" stroke="#00FFB2" stroke-width="3.5" stroke-linecap="round"/>
      <path d="M18 102 H38 M18 102 V82" fill="none" stroke="#00FFB2" stroke-width="3.5" stroke-linecap="round"/>
      <path d="M102 102 H82 M102 102 V82" fill="none" stroke="#00FFB2" stroke-width="3.5" stroke-linecap="round"/>
      <ellipse cx="60" cy="60" rx="28" ry="18" fill="none" stroke="#00FFB2" stroke-width="3.5"/>
      <circle cx="60" cy="60" r="8" fill="none" stroke="#00FFB2" stroke-width="3.5"/>
    </svg>'''


def ico_clipboard_search():
    return '''<svg class="ico" viewBox="0 0 120 120" aria-hidden="true">
      <rect x="28" y="22" width="52" height="70" rx="6" fill="none" stroke="#00FFB2" stroke-width="3.5"/>
      <rect x="42" y="14" width="24" height="14" rx="4" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <path d="M40 46 H68 M40 58 H68 M40 70 H56" stroke="#00FFB2" stroke-width="3" stroke-linecap="round"/>
      <circle cx="78" cy="78" r="16" fill="none" stroke="#00FFB2" stroke-width="3.5"/>
      <path d="M90 90 L102 102" stroke="#00FFB2" stroke-width="3.5" stroke-linecap="round"/>
    </svg>'''


def ico_gear_nodes():
    return '''<svg class="ico" viewBox="0 0 120 120" aria-hidden="true">
      <circle cx="60" cy="36" r="16" fill="none" stroke="#00FFB2" stroke-width="3.5"/>
      <circle cx="60" cy="36" r="6" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <path d="M60 52 V68" stroke="#00FFB2" stroke-width="3"/>
      <path d="M60 68 L36 92 M60 68 L60 96 M60 68 L84 92" stroke="#00FFB2" stroke-width="3"/>
      <rect x="24" y="92" width="18" height="14" rx="3" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <rect x="51" y="96" width="18" height="14" rx="3" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <rect x="78" y="92" width="18" height="14" rx="3" fill="none" stroke="#00FFB2" stroke-width="3"/>
    </svg>'''


def ico_dashboard_alert():
    return '''<svg class="ico ico-md" viewBox="0 0 120 100" aria-hidden="true">
      <rect x="8" y="12" width="78" height="64" rx="6" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <path d="M20 58 L36 40 L52 50 L70 28" fill="none" stroke="#00FFB2" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
      <rect x="18" y="64" width="10" height="6" fill="#00FFB2"/>
      <rect x="34" y="60" width="10" height="10" fill="#00FFB2" opacity=".7"/>
      <rect x="50" y="54" width="10" height="16" fill="#00FFB2" opacity=".45"/>
      <circle cx="92" cy="70" r="18" fill="#0A0A0A" stroke="#00FFB2" stroke-width="3"/>
      <path d="M92 58 V72" stroke="#00FFB2" stroke-width="3.5" stroke-linecap="round"/>
      <circle cx="92" cy="80" r="2.5" fill="#00FFB2"/>
    </svg>'''


def ico_question_bubble():
    return '''<svg class="ico ico-md" viewBox="0 0 100 100" aria-hidden="true">
      <path d="M18 22 H72 A12 12 0 0 1 84 34 V58 A12 12 0 0 1 72 70 H48 L32 86 V70 H18 A12 12 0 0 1 6 58 V34 A12 12 0 0 1 18 22 Z" fill="none" stroke="#00FFB2" stroke-width="3.5"/>
      <text x="45" y="58" text-anchor="middle" font-family="Poppins,sans-serif" font-size="36" font-weight="800" fill="#00FFB2">?</text>
    </svg>'''


def ico_shield_docs():
    return '''<svg class="ico ico-md" viewBox="0 0 120 100" aria-hidden="true">
      <rect x="48" y="18" width="40" height="52" rx="4" fill="none" stroke="#00FFB2" stroke-width="2.5" opacity=".5"/>
      <rect x="40" y="24" width="40" height="52" rx="4" fill="none" stroke="#00FFB2" stroke-width="2.5" opacity=".75"/>
      <path d="M18 28 L42 20 L66 28 V52 C66 68 42 78 42 78 C42 78 18 68 18 52 Z" fill="none" stroke="#00FFB2" stroke-width="3.5"/>
      <path d="M32 48 L40 56 L54 38" fill="none" stroke="#00FFB2" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>'''


def ico_folders_q():
    return '''<svg class="ico ico-md" viewBox="0 0 120 100" aria-hidden="true">
      <path d="M16 36 H44 L52 28 H92 A8 8 0 0 1 100 36 V72 A8 8 0 0 1 92 80 H28 A8 8 0 0 1 20 72 V44" fill="none" stroke="#00FFB2" stroke-width="3" opacity=".55"/>
      <path d="M12 44 H40 L48 36 H88 A8 8 0 0 1 96 44 V78 A8 8 0 0 1 88 86 H24 A8 8 0 0 1 16 78 V52" fill="none" stroke="#00FFB2" stroke-width="3.5"/>
      <text x="56" y="72" text-anchor="middle" font-family="Poppins,sans-serif" font-size="32" font-weight="800" fill="#00FFB2">?</text>
    </svg>'''


def ico_report_clip():
    return '''<svg class="ico ico-md" viewBox="0 0 100 110" aria-hidden="true">
      <rect x="22" y="18" width="56" height="78" rx="6" fill="none" stroke="#00FFB2" stroke-width="3.5"/>
      <rect x="36" y="10" width="28" height="14" rx="4" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <path d="M34 42 L42 34 L50 44 L62 28" fill="none" stroke="#00FFB2" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
      <rect x="34" y="58" width="10" height="10" rx="2" fill="none" stroke="#00FFB2" stroke-width="2.5"/>
      <path d="M38 61 L41 64 L48 56" fill="none" stroke="#00FFB2" stroke-width="2" stroke-linecap="round"/>
      <path d="M50 63 H70" stroke="#00FFB2" stroke-width="2.5" stroke-linecap="round"/>
      <rect x="34" y="74" width="10" height="10" rx="2" fill="none" stroke="#00FFB2" stroke-width="2.5"/>
      <path d="M50 79 H66" stroke="#00FFB2" stroke-width="2.5" stroke-linecap="round"/>
    </svg>'''


def ico_meeting():
    return '''<svg class="ico ico-md" viewBox="0 0 120 90" aria-hidden="true">
      <circle cx="30" cy="28" r="10" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <circle cx="60" cy="24" r="10" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <circle cx="90" cy="28" r="10" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <path d="M16 52 Q30 40 44 52" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <path d="M46 48 Q60 36 74 48" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <path d="M76 52 Q90 40 104 52" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <ellipse cx="42" cy="18" rx="10" ry="7" fill="none" stroke="#00FFB2" stroke-width="2.5"/>
      <ellipse cx="78" cy="16" rx="10" ry="7" fill="none" stroke="#00FFB2" stroke-width="2.5"/>
      <path d="M20 70 H100" stroke="#00FFB2" stroke-width="3" stroke-linecap="round"/>
    </svg>'''


def ico_eye_sm():
    return '''<svg class="ico-sm" viewBox="0 0 48 32" aria-hidden="true">
      <ellipse cx="24" cy="16" rx="18" ry="11" fill="none" stroke="#00FFB2" stroke-width="2.5"/>
      <circle cx="24" cy="16" r="5" fill="none" stroke="#00FFB2" stroke-width="2.5"/>
    </svg>'''


def ico_warn():
    return '''<svg class="ico-sm" viewBox="0 0 40 40" aria-hidden="true">
      <path d="M20 6 L36 34 H4 Z" fill="none" stroke="#00FFB2" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="M20 16 V24" stroke="#00FFB2" stroke-width="2.5" stroke-linecap="round"/>
      <circle cx="20" cy="29" r="1.8" fill="#00FFB2"/>
    </svg>'''


def ico_rules_clip():
    return '''<svg class="ico ico-lg" viewBox="0 0 140 160" aria-hidden="true">
      <rect x="30" y="28" width="70" height="100" rx="8" fill="none" stroke="#00FFB2" stroke-width="4"/>
      <rect x="48" y="16" width="34" height="18" rx="5" fill="none" stroke="#00FFB2" stroke-width="3.5"/>
      <circle cx="48" cy="60" r="8" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <path d="M44 60 L47 63 L54 55" fill="none" stroke="#00FFB2" stroke-width="2.5" stroke-linecap="round"/>
      <path d="M64 60 H88" stroke="#00FFB2" stroke-width="3" stroke-linecap="round"/>
      <circle cx="48" cy="84" r="8" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <path d="M44 84 L47 87 L54 79" fill="none" stroke="#00FFB2" stroke-width="2.5" stroke-linecap="round"/>
      <path d="M64 84 H88" stroke="#00FFB2" stroke-width="3" stroke-linecap="round"/>
      <circle cx="48" cy="108" r="8" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <path d="M44 108 L47 111 L54 103" fill="none" stroke="#00FFB2" stroke-width="2.5" stroke-linecap="round"/>
      <path d="M64 108 H82" stroke="#00FFB2" stroke-width="3" stroke-linecap="round"/>
      <circle cx="108" cy="118" r="22" fill="#0A0A0A" stroke="#00FFB2" stroke-width="4"/>
      <path d="M96 118 L105 127 L122 106" fill="none" stroke="#00FFB2" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>'''


def ico_cycle():
    return '''<svg class="ico ico-md" viewBox="0 0 120 120" aria-hidden="true">
      <circle cx="60" cy="60" r="38" fill="none" stroke="#00FFB2" stroke-width="3" opacity=".45"/>
      <circle cx="60" cy="60" r="26" fill="none" stroke="#00FFB2" stroke-width="3"/>
      <path d="M48 42 L60 30 L60 48 Z" fill="#00FFB2"/>
      <path d="M78 70 A22 22 0 1 1 48 42" fill="none" stroke="#00FFB2" stroke-width="3.5" stroke-linecap="round"/>
      <path d="M50 70 L60 82 L70 70 Z" fill="none" stroke="#00FFB2" stroke-width="3" stroke-linejoin="round"/>
      <path d="M54 78 L66 78" stroke="#00FFB2" stroke-width="3" stroke-linecap="round"/>
    </svg>'''


def ico_dm():
    return '''<svg class="ico ico-lg" viewBox="0 0 140 120" aria-hidden="true">
      <rect x="18" y="22" width="100" height="70" rx="16" fill="none" stroke="#00FFB2" stroke-width="4"/>
      <path d="M18 38 L68 62 L118 38" fill="none" stroke="#00FFB2" stroke-width="3.5" stroke-linejoin="round"/>
      <path d="M40 78 H96 M40 90 H78" stroke="#00FFB2" stroke-width="3.5" stroke-linecap="round" opacity=".7"/>
    </svg>'''

def slide_01():
    return (
        '<section class="slide" data-id="01"><div class="gridbg"></div>'
        + seam_nums(1)
        + '<div class="mid mid-center">'
        + '<p class="eyebrow">El problema de fondo</p>'
        + '<h1 class="h1">Si tu empresa <span class="sm">solo funciona</span><br>cuando <span class="ac xl">vos</span> estás encima…</h1>'
        + '<p class="punch"><span class="md">no tenés control.</span><br><span class="ac xl">Tenés vigilancia.</span></p>'
        + '<div class="rule"></div><div class="ico-wrap">' + ico_eye() + '</div></div>'
        + foot()
        + '</section>'
    )

def slide_02():
    return (
        '<section class="slide" data-id="02"><div class="gridbg"></div>'
        + seam_nums(2)
        + '<div class="mid mid-top">'
        + '<p class="lead-sm">Revisar cada pedido, autorizar cada compra,<br>entrar a cada junta y resolver cada excepción…</p>'
        + '<p class="soft-line">puede darte tranquilidad.</p>'
        + '<p class="punch2">Pero no construye<br><span class="ac xl">sistema.</span></p></div>'
        + '<div class="bot-left">' + ico_clipboard_search() + '</div>'
        + foot()
        + '</section>'
    )

def slide_03():
    return (
        '<section class="slide" data-id="03"><div class="gridbg"></div>'
        + seam_nums(3)
        + '<div class="mid mid-stack"><div>'
        + '<p class="lead-sm">La presencia del dueño <span class="ac">no puede ser</span></p>'
        + '<h1 class="h1-tight">el <span class="ac">sistema operativo</span><br><span class="sm">de la empresa.</span></h1></div><div>'
        + '<p class="lead-sm">Una empresa seria debe</p>'
        + '<h1 class="h1-tight"><span class="ac">detectar problemas</span></h1>'
        + '<p class="lead-sm">antes de que lleguen a vos.</p></div></div>'
        + '<div class="bot-left">' + ico_gear_nodes() + '</div>'
        + foot()
        + '</section>'
    )

def slide_04():
    return (
        '<section class="slide" data-id="04"><div class="gridbg"></div>'
        + seam_nums(4)
        + '<div class="mid mid-duo"><div class="duo-row"><div>'
        + '<p class="label-sys">En una empresa <span class="ac">con sistema,</span></p>'
        + '<h1 class="h-duo">los indicadores<br><span class="g xl">alertan.</span></h1></div>'
        + ico_dashboard_alert()
        + '</div><div class="sep"></div><div class="duo-row"><div>'
        + '<p class="label-sys">En una empresa <span class="ac">sin sistema,</span></p>'
        + '<h1 class="h-duo">el dueño pregunta:<br><span class="g xl">“¿Cómo vamos?”</span></h1></div>'
        + ico_question_bubble()
        + '</div></div>'
        + foot()
        + '</section>'
    )

def slide_05():
    return (
        '<section class="slide" data-id="05"><div class="gridbg"></div>'
        + seam_nums(5)
        + '<div class="mid mid-duo"><div class="duo-row"><div>'
        + '<p class="label-sys">En una empresa <span class="ac">con sistema,</span></p>'
        + '<h1 class="h-duo">las políticas <span class="xl">protegen</span><br><span class="sm">decisiones críticas.</span></h1></div>'
        + ico_shield_docs()
        + '</div><div class="sep"></div><div class="duo-row"><div>'
        + '<p class="label-sys">En una empresa <span class="ac">sin sistema,</span></p>'
        + '<h1 class="h-duo"><span class="sm">todo se resuelve</span><br><span class="ac xl">“caso por caso”.</span></h1></div>'
        + ico_folders_q()
        + '</div></div>'
        + foot()
        + '</section>'
    )

def slide_06():
    return (
        '<section class="slide" data-id="06"><div class="gridbg"></div>'
        + seam_nums(6)
        + '<div class="mid mid-duo"><div class="duo-row duo-top"><div>'
        + '<p class="label-sys">En una empresa <span class="ac">con sistema,</span></p>'
        + '<h1 class="h-duo">los reportes muestran:</h1>'
        + '<p class="list-plain"><span class="lg">avance,</span><br><span class="lg">problema,</span><br><span class="lg">responsable</span><br><span class="sm">y siguiente decisión.</span></p></div>'
        + ico_report_clip()
        + '</div><div class="sep"></div><div class="duo-row"><div>'
        + '<p class="label-sys">En una empresa <span class="ac">sin sistema,</span></p>'
        + '<h1 class="h-duo"><span class="sm">las juntas se vuelven</span><br><span class="ac xl">conversaciones largas.</span></h1></div>'
        + ico_meeting()
        + '</div></div>'
        + foot()
        + '</section>'
    )

def slide_07():
    return (
        '<section class="slide" data-id="07"><div class="gridbg"></div>'
        + seam_nums(7)
        + '<div class="mid mid-top">'
        + '<h1 class="h1">Un indicador<br><span class="ac xl">sin consecuencia</span><br><span class="sm">se vuelve</span><br><span class="ac xl">decoración.</span></h1>'
        + '<div class="rows"><div class="row">' + ico_eye_sm() + '<span class="vline"></span><p>Si alguien <span class="ac">cumple</span>, <span class="sm">debe verse.</span></p></div>'
        + '<div class="row">' + ico_warn() + '<span class="vline"></span><p>Si alguien <span class="ac">no cumple</span>, <span class="sm">también.</span></p></div></div></div>'
        + foot()
        + '</section>'
    )

def slide_08():
    return (
        '<section class="slide" data-id="08"><div class="gridbg"></div>'
        + seam_nums(8)
        + '<div class="mid mid-split"><div class="split-left">'
        + '<p class="lead-sm">No necesitás burocracia.</p>'
        + '<h1 class="h1-tight">Necesitás <span class="ac xl">pocas reglas,</span><br><span class="sm">pero</span> <span class="ac">bien elegidas:</span></h1>'
        + '<ul class="checks"><li><span class="tick">✓</span> <span class="lg">dinero,</span></li><li><span class="tick">✓</span> <span class="lg">clientes,</span></li><li><span class="tick">✓</span> <span class="lg">inventario,</span></li><li><span class="tick">✓</span> <span class="lg">calidad,</span></li><li><span class="tick">✓</span> <span class="sm">decisiones críticas.</span></li></ul></div>'
        + '<div class="split-right">' + ico_rules_clip() + '</div></div>'
        + foot()
        + '</section>'
    )

def slide_09():
    return (
        '<section class="slide" data-id="09"><div class="gridbg"></div>'
        + seam_nums(9)
        + '<div class="mid mid-top">'
        + '<h1 class="h1">El <span class="ac xl">control real</span><br><span class="sm">no está en revisar todo.</span></h1>'
        + '<div class="row-9">' + ico_cycle()
        + '<p class="body9"><span class="sm">Está en diseñar procesos para que la empresa</span><span class="ac xl"> se corrija</span><span class="sm"> antes de llegar a vos.</span></p></div></div>'
        + foot()
        + '</section>'
    )

def slide_10():
    return (
        '<section class="slide" data-id="10"><div class="gridbg"></div>'
        + seam_nums(10)
        + '<div class="mid mid-cta">'
        + '<p class="cta-pre">Comentá</p><h1 class="cta-kw">PROCESOS</h1>'
        + '<p class="cta-mid">y te mando por mensaje</p><p class="cta-sub">la guía:</p>'
        + '<p class="cta-quote"><span class="ac">“Cómo pasar del caos operativo<br>a un sistema que funciona <span class="xl">sin vos encima.</span>”</span></p></div>'
        + '<div class="bot-right-ico">' + ico_dm() + '</div>'
        + foot(arrow=False)
        + '</section>'
    )

CSS = "\n@font-face { font-family:'Poppins'; src:url('file:///tmp/stlabs-fonts/Poppins-ExtraBold.ttf') format('truetype'); font-weight:800; }\n@font-face { font-family:'Poppins'; src:url('file:///tmp/stlabs-fonts/Poppins-Bold.ttf') format('truetype'); font-weight:700; }\n@font-face { font-family:'Lora'; src:url('file:///tmp/stlabs-fonts/Lora-Italic-Variable.ttf') format('truetype'); font-style:italic; font-weight:400 700; }\n@font-face { font-family:'IBM Plex Mono'; src:url('file:///tmp/stlabs-fonts/IBMPlexMono-Medium.ttf') format('truetype'); font-weight:500; }\n@font-face { font-family:'Barlow Condensed'; src:url('file:///tmp/stlabs-fonts/BarlowCondensed-Medium.ttf') format('truetype'); font-weight:500; }\n@font-face { font-family:'Barlow Condensed'; src:url('file:///tmp/stlabs-fonts/BarlowCondensed-Bold.ttf') format('truetype'); font-weight:700; }\n\n* { box-sizing:border-box; margin:0; padding:0; -webkit-font-smoothing:antialiased; }\nhtml, body { background:#000; }\n.sheet { display:flex; flex-direction:column; gap:48px; padding:40px; width:max-content; }\n\n.slide {\n  position:relative; width:1080px; height:1350px; overflow:hidden;\n  background:#0A0A0A; color:#F2F2F2;\n}\n.gridbg {\n  position:absolute; inset:0; z-index:0; pointer-events:none;\n  background-image:\n    linear-gradient(rgba(0,255,178,.04) 1px, transparent 1px),\n    linear-gradient(90deg, rgba(0,255,178,.04) 1px, transparent 1px);\n  background-size:48px 48px;\n  -webkit-mask-image: radial-gradient(ellipse 70% 60% at 45% 40%, transparent 0%, transparent 45%, rgba(0,0,0,.35) 80%, #000 100%);\n  mask-image: radial-gradient(ellipse 70% 60% at 45% 40%, transparent 0%, transparent 45%, rgba(0,0,0,.35) 80%, #000 100%);\n}\n\n/* Números partidos por costura */\n.seam-num {\n  position:absolute; z-index:2; pointer-events:none;\n  font-family:'Poppins', sans-serif; font-weight:800;\n  font-size:260px; line-height:.85; letter-spacing:-.04em;\n  color:rgba(0,255,178,.32);\n  width:320px; text-align:center;\n}\n.seam-out { left:920px; }   /* 1080 - 160 → mitad derecha visible */\n.seam-in  { left:-160px; }  /* mitad izquierda visible */\n.seam-solo { left:auto; right:48px; opacity:.4; font-size:200px; }\n.seam-top { top:40px; }\n.seam-bot { bottom:200px; }\n\n.firma {\n  position:absolute; left:0; right:0; bottom:56px; text-align:center; z-index:6;\n  font-family:'IBM Plex Mono', monospace; font-weight:500; font-size:22px;\n  letter-spacing:.14em; color:#00FFB2;\n}\n.arrow { position:absolute; right:64px; bottom:120px; z-index:6; opacity:.9; }\n\n.g { color:#00FFB2; }\n.ac {\n  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;\n  color:#00FFB2;\n}\n/* Jerarquía de tamaño dentro de cada slide — contraste fuerte */\n.xl { font-size:1.42em; letter-spacing:-.035em; line-height:1.02; }\n.lg { font-size:1.18em; }\n.md { font-size:.88em; }\n.sm { font-size:.62em; font-weight:700; letter-spacing:-.01em; opacity:.9; }\n\n.eyebrow {\n  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;\n  font-size:22px; color:#00FFB2; margin-bottom:18px;\n}\n.lead-sm {\n  font-family:'Poppins', sans-serif; font-weight:700; font-size:26px;\n  line-height:1.35; color:#a8b0a9; letter-spacing:-.01em; max-width:880px;\n}\n.soft-line {\n  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:500;\n  font-size:30px; color:#9aa39c; margin:16px 0 26px;\n}\n.label-sys {\n  font-family:'Poppins', sans-serif; font-weight:700; font-size:22px;\n  line-height:1.3; color:#a8b0a9; margin-bottom:12px;\n}\n.label-sys .ac { font-size:1.08em; }\n\n.mid { position:absolute; left:72px; right:72px; top:140px; bottom:160px; z-index:4; }\n.mid-center { display:flex; flex-direction:column; justify-content:center; align-items:flex-start; }\n.mid-top { padding-top:40px; }\n.mid-stack { display:flex; flex-direction:column; justify-content:center; gap:56px; }\n.mid-duo { display:flex; flex-direction:column; justify-content:center; }\n.mid-split { display:flex; flex-direction:row; align-items:center; gap:16px; padding-top:24px; }\n.mid-cta { display:flex; flex-direction:column; justify-content:center; }\n\n.h1 {\n  font-family:'Poppins', sans-serif; font-weight:800; font-size:58px;\n  line-height:1.06; letter-spacing:-.03em; color:#F2F2F2; text-align:left;\n}\n.h1-tight {\n  font-family:'Poppins', sans-serif; font-weight:800; font-size:54px;\n  line-height:1.08; letter-spacing:-.03em; color:#F2F2F2; text-align:left;\n  margin:6px 0;\n}\n.h-duo {\n  font-family:'Poppins', sans-serif; font-weight:800; font-size:44px;\n  line-height:1.12; letter-spacing:-.025em; color:#F2F2F2; text-align:left;\n  max-width:700px;\n}\n.punch {\n  margin-top:28px; font-family:'Poppins', sans-serif; font-weight:800;\n  font-size:52px; line-height:1.08; text-align:left; color:#F2F2F2;\n}\n.punch2 {\n  margin-top:8px; font-family:'Poppins', sans-serif; font-weight:800;\n  font-size:58px; line-height:1.06; color:#F2F2F2;\n}\n.rule {\n  width:120px; height:5px; background:#00FFB2; border-radius:2px;\n  margin:36px 0 28px;\n}\n.ico-wrap { margin-top:8px; }\n.ico { width:120px; height:120px; }\n.ico-md { width:140px; height:120px; flex-shrink:0; }\n.ico-lg { width:200px; height:220px; }\n.ico-sm { width:44px; height:36px; flex-shrink:0; }\n\n.bot-left { position:absolute; left:72px; bottom:160px; z-index:4; }\n.bot-right-ico { position:absolute; right:64px; bottom:160px; z-index:4; }\n\n.duo-row {\n  display:flex; align-items:center; justify-content:space-between; gap:24px;\n  padding:24px 0;\n}\n.sep { width:80px; height:1px; background:rgba(0,255,178,.35); margin:8px 0; }\n.list-plain {\n  margin-top:14px; font-family:'Barlow Condensed', sans-serif; font-weight:500;\n  font-size:34px; line-height:1.3; color:#c5cdc6;\n}\n\n.rows { margin-top:52px; display:flex; flex-direction:column; gap:24px; }\n.row {\n  display:flex; align-items:center; gap:20px;\n  font-family:'Poppins', sans-serif; font-weight:700; font-size:28px; color:#F2F2F2;\n}\n.vline { width:1px; height:36px; background:rgba(0,255,178,.4); }\n\n.split-left { flex:1; }\n.split-right { flex-shrink:0; }\n.checks {\n  list-style:none; margin-top:36px;\n  font-family:'Poppins', sans-serif; font-weight:700; font-size:30px; color:#F2F2F2;\n  display:flex; flex-direction:column; gap:12px;\n}\n.tick {\n  display:inline-flex; align-items:center; justify-content:center;\n  width:28px; height:28px; border-radius:50%; border:2px solid #00FFB2;\n  color:#00FFB2; font-size:16px; margin-right:12px; vertical-align:middle;\n}\n\n.row-9 { margin-top:56px; display:flex; align-items:center; gap:36px; }\n.body9 {\n  font-family:'Poppins', sans-serif; font-weight:700; font-size:32px;\n  line-height:1.35; color:#F2F2F2; max-width:620px;\n}\n\n.cta-pre {\n  font-family:'Poppins', sans-serif; font-weight:800; font-size:36px; color:#F2F2F2;\n}\n.cta-kw {\n  font-family:'Poppins', sans-serif; font-weight:800; font-size:112px;\n  letter-spacing:.04em; color:#00FFB2; line-height:.92; margin:2px 0 14px;\n}\n.cta-mid {\n  font-family:'Poppins', sans-serif; font-weight:700; font-size:30px; color:#a8b0a9;\n}\n.cta-sub {\n  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:500;\n  font-size:24px; color:#9aa39c; margin:14px 0 8px;\n}\n.cta-quote {\n  font-family:'Poppins', sans-serif; font-weight:700; font-size:26px; line-height:1.35;\n  max-width:720px;\n}\n.cta-quote .ac { font-size:1em; }\n"

def main():
    slides = [
        slide_01(), slide_02(), slide_03(), slide_04(), slide_05(),
        slide_06(), slide_07(), slide_08(), slide_09(), slide_10(),
    ]
    html = "<!DOCTYPE html>\n<html lang=\"es\"><head><meta charset=\"UTF-8\">\n<title>Sistema vs vigilancia — STLabs</title>\n<style>" + CSS + "</style></head>\n<body><div class=\"sheet\">" + "".join(slides) + "</div></body></html>"
    (B / "carrusel.html").write_text(html, encoding="utf-8")
    meta = {
        "titulo": "Si tu empresa solo funciona cuando vos estás encima",
        "slides": 10,
        "fondo": "reticula_fina",
        "familia_visual": "dossier_editorial",
        "origen": "screenshot",
        "keyword_portada": "PROCESOS",
        "modo": "negro",
        "id": "2026-08-15-sistema-control",
        "fecha": "2026-08-15",
    }
    (B / "index.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote %d slides · jerarquía tipográfica XL/SM · números partidos" % len(slides))


if __name__ == "__main__":
    main()
