# -*- coding: utf-8 -*-
"""Overlays HTML sobre graphic-XX.orig.png — tapa EN, escribe ES, conserva visuales."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Zone:
    x: float
    y: float
    w: float
    h: float
    text: str = ""
    color: str = "#F2F2F2"
    green: bool = False
    size: float = 15.0
    mono: bool = False
    lines: tuple[str, ...] = ()
    cover: bool = True


RW = 1158


def _z(x: int, y: int, w: int, h: int, rh: int, **kw) -> Zone:
    return Zone(x / RW * 100, y / rh * 100, w / RW * 100, h / rh * 100, **kw)


def _cover(x: int, y: int, w: int, h: int, rh: int) -> Zone:
    return _z(x, y, w, h, rh, cover=True)


def _lbl(x: int, y: int, w: int, h: int, rh: int, **kw) -> list[Zone]:
    return [_cover(x, y, w, h, rh), _z(x, y, w, h, rh, cover=False, **kw)]


LAYERS: dict[int, tuple[int, list[Zone]]] = {
    1: (
        700,
        [
            _cover(0, 0, 1158, 82, 700),
            *_lbl(418, 42, 155, 62, 700, text="HACÉ", green=True, size=28),
            *_lbl(0, 218, 235, 88, 700, text="PROBÁ", green=True, size=26),
            *_lbl(945, 218, 213, 88, 700, text="MEDÍ", green=True, size=26),
            *_lbl(48, 588, 250, 95, 700, text="MEJORÁ", green=True, size=24),
            *_lbl(798, 588, 240, 95, 700, text="REFLEXIONÁ", green=True, size=20),
            _cover(1080, 180, 78, 520, 700),
        ],
    ),
    2: (
        860,
        [
            _cover(0, 0, 1158, 78, 860),
            *_lbl(448, 78, 360, 58, 860, text="MEMORIA", green=True, size=28),
            *_lbl(18, 62, 175, 52, 860, text="ENTRADA", green=True, size=19),
            *_lbl(962, 62, 175, 52, 860, text="SALIDA", green=True, size=19),
            *_lbl(108, 158, 215, 88, 860, text="TAREA", size=18),
            *_lbl(108, 268, 215, 88, 860, text="ACCIÓN", size=18),
            *_lbl(108, 378, 215, 88, 860, text="RESULTADO", size=16),
            *_lbl(108, 488, 215, 88, 860, text="CONTEXTO", size=16),
            *_lbl(835, 158, 320, 88, 860, text="QUÉ FUNCIONA", size=15),
            *_lbl(835, 268, 320, 88, 860, text="QUÉ FALLÓ", size=15),
            *_lbl(835, 378, 320, 88, 860, text="QUÉ MEJORÓ", size=15),
            *_lbl(835, 488, 320, 88, 860, text="QUÉ CAMBIAR", size=15),
            _cover(0, 738, 1158, 122, 860),
        ],
    ),
    3: (
        820,
        [
            *_lbl(82, 0, 210, 55, 820, text="AGENTE TURBO", green=True, size=18),
            *_lbl(375, 168, 220, 98, 820, text="", lines=("EVALÚA", "CADA CORRIDA"), size=14),
            *_lbl(625, 0, 160, 55, 820, text="PUNTUACIÓN", green=True, size=17),
            *_lbl(625, 28, 225, 48, 820, text="PRECISIÓN", size=16),
            *_lbl(625, 118, 215, 48, 820, text="CALIDAD", size=16),
            *_lbl(625, 208, 205, 48, 820, text="ERRORES", size=16),
            *_lbl(625, 302, 355, 52, 820, text="OBJETIVO CUMPLIDO", size=14),
            *_lbl(525, 412, 470, 48, 820, text="Las puntuaciones usan tus criterios.", size=13, color="#9aa39c"),
            *_lbl(555, 478, 450, 52, 820, text="DATOS → INSIGHT → MEJORA", green=True, size=13),
        ],
    ),
    4: (
        720,
        [
            *_lbl(108, 12, 325, 95, 720, text="AGENTE", green=True, size=19),
            _cover(22, 338, 355, 165, 720),
            *_lbl(28, 358, 340, 44, 720, text="TRABAJO ENTREGADO", green=True, size=15),
            *_lbl(28, 402, 345, 82, 720, text="", lines=("Resultados, acciones,", "decisiones de la corrida."), size=12, color="#9aa39c"),
            *_lbl(262, 228, 325, 115, 720, text="", lines=("ENVÍA TODO", "A REVISIÓN"), size=13),
            *_lbl(758, 0, 355, 102, 720, text="CRÍTICO", green=True, size=19),
            *_lbl(678, 342, 375, 50, 720, text="¿QUÉ FUNCIONÓ?", size=15, mono=True),
            *_lbl(678, 392, 375, 50, 720, text="¿QUÉ FALLÓ?", size=15, mono=True),
            *_lbl(678, 444, 375, 50, 720, text="¿POR QUÉ FALLÓ?", size=13, mono=True),
            *_lbl(678, 496, 375, 50, 720, text="¿QUÉ CAMBIAR?", size=15, mono=True),
        ],
    ),
    5: (
        860,
        [
            *_lbl(58, 0, 355, 55, 860, text="HISTORIAL DE TAREAS", green=True, size=16),
            *_lbl(0, 508, 315, 58, 860, text="20 CORRIDAS", size=13),
            *_lbl(265, 508, 200, 58, 860, text="6 FALLAS", color="#ff5252", size=13),
            _cover(585, 0, 430, 95, 860),
            *_lbl(592, 5, 415, 44, 860, text="6 FALLAS DETECTADAS", size=15),
            *_lbl(592, 45, 415, 38, 860, text="Turbo no solo las registró.", size=12, color="#9aa39c"),
            *_lbl(592, 115, 415, 48, 860, text="ANALIZANDO CAUSAS", size=15),
            *_lbl(555, 155, 450, 42, 860, text="Compara entradas, acciones y resultados.", size=11, color="#9aa39c"),
            *_lbl(592, 265, 415, 48, 860, text="4 MISMA CAUSA RAÍZ", size=14),
            *_lbl(555, 305, 450, 42, 860, text="Tareas distintas. Mismo problema.", size=11, color="#9aa39c"),
            *_lbl(612, 420, 395, 48, 860, text="PATRÓN ENCONTRADO", green=True, size=15),
            *_lbl(592, 465, 420, 55, 860, text="Sigue fallando el Paso #3 del flujo.", size=11, color="#9aa39c"),
        ],
    ),
    6: (
        840,
        [
            *_lbl(22, 0, 315, 75, 840, text="TURBO V1", size=21),
            *_lbl(32, 318, 305, 42, 840, text="PIERDE CONTEXTO", size=14),
            *_lbl(32, 362, 310, 42, 840, text="OLVIDA PASOS CLAVE", size=13),
            *_lbl(32, 406, 310, 42, 840, text="SALIDAS INCONSISTENTES", size=12),
            *_lbl(18, 572, 315, 68, 840, text="PUNTAJE: 72/100", size=15),
            *_lbl(358, 0, 285, 55, 840, text="REFLEXIÓN", size=16),
            *_lbl(358, 268, 295, 36, 840, text="MEJORAS APLICADAS:", green=True, size=14),
            *_lbl(372, 312, 280, 32, 840, text="PROMPT ACTUALIZADO", size=11),
            *_lbl(372, 356, 280, 32, 840, text="REGLAS REFINADAS", size=12),
            *_lbl(372, 400, 280, 32, 840, text="MEMORIA EXPANDIDA", size=12),
            *_lbl(372, 444, 280, 32, 840, text="FLUJO OPTIMIZADO", size=12),
            *_lbl(372, 488, 280, 32, 840, text="HERRAMIENTAS MEJORADAS", size=11),
            *_lbl(778, 0, 310, 75, 840, text="TURBO V2", green=True, size=21),
            *_lbl(748, 318, 295, 42, 840, text="MEJOR CONTEXTO", size=13),
            *_lbl(748, 362, 295, 42, 840, text="MENOS ERRORES", size=13),
            *_lbl(748, 406, 295, 42, 840, text="MÁS CONSISTENTE", size=13),
            *_lbl(748, 450, 295, 42, 840, text="MAYOR CALIDAD", size=13),
            *_lbl(738, 572, 315, 68, 840, text="PUNTAJE: 91/100", green=True, size=15),
        ],
    ),
    7: (
        860,
        [
            *_lbl(5, 0, 355, 65, 860, text="VERSIÓN 1 (ANTERIOR)", size=15),
            *_lbl(255, 162, 195, 42, 860, text="PRECISIÓN", size=12),
            *_lbl(255, 208, 195, 42, 860, text="CALIDAD", size=12),
            *_lbl(245, 254, 205, 42, 860, text="TAREAS OK", size=12),
            *_lbl(255, 300, 185, 42, 860, text="ERRORES", size=12),
            *_lbl(32, 422, 325, 58, 860, text="PUNTAJE: 82/100", size=15),
            *_lbl(618, 0, 355, 65, 860, text="VERSIÓN 2 (NUEVA)", green=True, size=15),
            *_lbl(728, 162, 195, 42, 860, text="PRECISIÓN", size=12),
            *_lbl(728, 208, 195, 42, 860, text="CALIDAD", size=12),
            *_lbl(718, 254, 205, 42, 860, text="TAREAS OK", size=12),
            *_lbl(728, 300, 185, 42, 860, text="ERRORES", size=12),
            *_lbl(652, 422, 325, 58, 860, text="PUNTAJE: 91/100", green=True, size=15),
            _cover(0, 528, 275, 125, 860),
            *_lbl(5, 532, 260, 58, 860, text="", lines=("¿MEJOR?", "QUEDATE."), size=13),
            *_lbl(22, 612, 205, 45, 860, text="DESPLEGAR", green=True, size=15),
            _cover(288, 528, 275, 125, 860),
            *_lbl(295, 532, 260, 58, 860, text="", lines=("¿PEOR?", "DESCARTÁ."), size=13),
            *_lbl(318, 612, 205, 45, 860, text="DESCARTAR", color="#ff5252", size=15),
            _cover(592, 528, 330, 125, 860),
            *_lbl(602, 532, 305, 58, 860, text="", lines=("¿IGUAL?", "SEGUÍ PROBANDO."), size=12),
            *_lbl(652, 612, 205, 45, 860, text="ITERAR", color="#ffc107", size=15),
            *_lbl(248, 662, 450, 62, 860, text="PIPELINE DE PRUEBAS", green=True, size=14),
        ],
    ),
    8: (
        630,
        [
            _cover(0, 0, 175, 135, 630),
            *_lbl(0, 0, 175, 135, 630, text="", lines=("Corré.", "Aprendé.", "Evolucioná."), size=14),
            *_lbl(102, 0, 295, 88, 630, text="DESPLEGÁ", green=True, size=18),
            *_lbl(102, 34, 280, 32, 630, text="Liberá la mejor versión", size=12, color="#9aa39c"),
            *_lbl(668, 0, 295, 88, 630, text="MEDÍ", green=True, size=18),
            *_lbl(668, 34, 280, 32, 630, text="Puntúa cada resultado", size=12, color="#9aa39c"),
            *_lbl(35, 178, 295, 108, 630, text="PROBÁ", green=True, size=18),
            *_lbl(35, 218, 280, 32, 630, text="Demostrá que funciona", size=11, color="#9aa39c"),
            *_lbl(658, 172, 305, 108, 630, text="REFLEXIONÁ", green=True, size=16),
            *_lbl(658, 212, 290, 32, 630, text="Critica y detecta fallas", size=11, color="#9aa39c"),
            *_lbl(312, 238, 330, 58, 630, text="SIEMPRE MEJORANDO", size=13),
            *_lbl(342, 358, 255, 42, 630, text="MEJORÁ", green=True, size=18),
            *_lbl(322, 398, 280, 32, 630, text="Aplicá upgrades", size=12, color="#9aa39c"),
            *_lbl(708, 388, 235, 82, 630, text="", lines=("24/7", "TURBO"), size=15, green=True),
        ],
    ),
}


def layer_html(n: int, img_b64: str) -> str:
    rh, zones = LAYERS[n]
    parts = [f'<div class="g-wrap g{n}"><img class="g-bg" src="{img_b64}" width="1158" height="{rh}" alt=""/>']
    parts.append('<div class="g-ol">')
    for z in zones:
        style = f"left:{z.x:.3f}%;top:{z.y:.3f}%;width:{z.w:.3f}%;height:{z.h:.3f}%;"
        if z.cover and not z.text and not z.lines:
            parts.append(f'<div class="g-cover" style="{style}"></div>')
        elif z.cover and (z.text or z.lines):
            parts.append(f'<div class="g-cover" style="{style}"></div>')
            fs = f"font-size:{z.size}px;"
            if z.color != "#F2F2F2":
                fs += f"color:{z.color};"
            cls = "g-lbl"
            if z.green:
                cls += " gr"
            if z.mono:
                cls += " mono"
            inner = "".join(f"<span>{ln}</span>" for ln in z.lines) if z.lines else z.text
            parts.append(f'<div class="{cls}" style="{style}{fs}">{inner}</div>')
        elif z.text or z.lines:
            fs = f"font-size:{z.size}px;"
            if z.color != "#F2F2F2":
                fs += f"color:{z.color};"
            cls = "g-lbl"
            if z.green:
                cls += " gr"
            if z.mono:
                cls += " mono"
            inner = "".join(f"<span>{ln}</span>" for ln in z.lines) if z.lines else z.text
            parts.append(f'<div class="{cls}" style="{style}{fs}">{inner}</div>')
    parts.append("</div></div>")
    return "".join(parts)
