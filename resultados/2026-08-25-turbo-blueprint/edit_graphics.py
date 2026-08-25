# -*- coding: utf-8 -*-
"""Traduce texto EN→ES y refuerza verde #00FFB2 en gráficos recortados."""
from __future__ import annotations

import colorsys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

B = Path(__file__).resolve().parent
ASSETS = B / "assets"
FONTS = Path("/tmp/stlabs-fonts")
TARGET = (0, 255, 178)
TARGET_H = colorsys.rgb_to_hsv(TARGET[0] / 255, TARGET[1] / 255, TARGET[2] / 255)[0]


@dataclass
class Rect:
    x: int
    y: int
    w: int
    h: int


@dataclass
class Label:
    x: int
    y: int
    w: int
    h: int
    text: str
    size: int = 22
    color: tuple[int, int, int] = (242, 242, 242)
    bold: bool = False
    green: bool = False
    center: bool = False
    mono: bool = False


def _font(size: int, bold: bool = False, mono: bool = False) -> ImageFont.FreeTypeFont:
    if mono:
        fn = "IBMPlexMono-SemiBold.ttf" if bold else "IBMPlexMono-Medium.ttf"
    elif bold:
        fn = "BarlowCondensed-Bold.ttf"
    else:
        fn = "BarlowCondensed-Medium.ttf"
    return ImageFont.truetype(str(FONTS / fn), size)


def boost_green(img: Image.Image, strength: float = 0.45) -> Image.Image:
    arr = np.array(img.convert("RGBA"), dtype=np.float32)
    r, g, b, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    mask = (
        (a > 20)
        & (g > 55)
        & (g >= r * 0.95)
        & (g >= b * 0.85)
        & (lum > 35)
    )
    idx = np.where(mask)
    for i in range(len(idx[0])):
        y, x = idx[0][i], idx[1][i]
        rv, gv, bv = r[y, x] / 255, g[y, x] / 255, b[y, x] / 255
        h, s, v = colorsys.rgb_to_hsv(rv, gv, bv)
        h = h * (1 - strength) + TARGET_H * strength
        s = min(1.0, s * (1 + strength * 0.6))
        v = min(1.0, v * (1 + strength * 0.14))
        nr, ng, nb = colorsys.hsv_to_rgb(h, s, v)
        ng = ng * (1 - strength * 0.28) + (TARGET[1] / 255) * (strength * 0.28)
        nr *= 1 - strength * 0.16
        nb *= 1 - strength * 0.22
        arr[y, x, 0] = min(255, nr * 255)
        arr[y, x, 1] = min(255, ng * 255)
        arr[y, x, 2] = min(255, nb * 255)
    return Image.fromarray(arr.astype(np.uint8), "RGBA")


def paint_covers(img: Image.Image, covers: list[Rect]) -> None:
    draw = ImageDraw.Draw(img)
    for c in covers:
        draw.rectangle([c.x, c.y, c.x + c.w, c.y + c.h], fill=(0, 0, 0, 255))


def _fit_size(text: str, max_w: int, start: int, bold: bool, mono: bool) -> int:
    size = start
    while size > 8:
        f = _font(size, bold=bold, mono=mono)
        bbox = f.getbbox(text)
        if bbox[2] - bbox[0] <= max_w:
            return size
        size -= 1
    return 8


def draw_label(draw: ImageDraw.ImageDraw, lb: Label) -> None:
    color = TARGET if lb.green else lb.color
    size = _fit_size(lb.text, lb.w, lb.size, lb.bold, lb.mono)
    font = _font(size, bold=lb.bold, mono=lb.mono)
    bbox = font.getbbox(lb.text)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = lb.x + (lb.w - tw) // 2 if lb.center else lb.x
    ty = lb.y + (lb.h - th) // 2 - bbox[1]
    draw.text((tx, ty), lb.text, fill=color + (255,), font=font)


def process_image(
    n: int,
    covers: list[Rect],
    labels: list[Label],
) -> None:
    src = ASSETS / f"graphic-{n:02d}.png"
    bak = ASSETS / f"graphic-{n:02d}.orig.png"
    if not bak.exists():
        Image.open(src).save(bak)
    img = boost_green(Image.open(bak).convert("RGBA"))
    paint_covers(img, covers)
    draw = ImageDraw.Draw(img)
    for lb in labels:
        draw_label(draw, lb)
    img.save(src, optimize=True)
    print(f"OK graphic-{n:02d}")


# ── gráfico 1 ────────────────────────────────────────────────────────────────
G1_COVERS = [
    Rect(55, 72, 660, 55),
    Rect(10, 395, 260, 100),
    Rect(840, 395, 320, 100),
    Rect(640, 685, 520, 100),
    Rect(10, 685, 420, 100),
    Rect(650, 760, 510, 70),
    Rect(10, 760, 420, 70),
]
G1_LABELS = [
    Label(60, 78, 640, 48, "MEJORA TODO EL TIEMPO 24/7.", 36, bold=True),
    Label(15, 410, 240, 70, "PROBÁ", 50, bold=True, center=True),
    Label(850, 410, 300, 70, "MEDÍ", 50, bold=True, center=True),
    Label(650, 700, 500, 70, "REFLEXIONÁ", 44, bold=True, center=True),
    Label(15, 700, 400, 70, "MEJORÁ", 50, bold=True, center=True),
]

# ── gráfico 2 ────────────────────────────────────────────────────────────────
G2_COVERS = [
    Rect(0, 0, 420, 42),
    Rect(95, 112, 200, 42),
    Rect(820, 112, 300, 42),
    Rect(165, 175, 220, 62),
    Rect(165, 255, 220, 62),
    Rect(165, 335, 220, 62),
    Rect(165, 415, 220, 62),
    Rect(810, 175, 310, 62),
    Rect(810, 255, 310, 62),
    Rect(810, 335, 310, 62),
    Rect(810, 415, 310, 62),
]
G2_LABELS = [
    Label(0, 4, 410, 34, "...datos de los que puede aprender.", 24, green=True),
    Label(510, 58, 190, 36, "MEMORIA", 30, bold=True, green=True, center=True),
    Label(95, 116, 195, 34, "ENTRADA", 24, bold=True, green=True, center=True),
    Label(820, 116, 295, 34, "SALIDA", 24, bold=True, green=True, center=True),
    Label(165, 182, 215, 42, "TAREA", 22, bold=True, center=True),
    Label(165, 262, 215, 42, "ACCIÓN", 22, bold=True, center=True),
    Label(165, 342, 215, 42, "RESULTADO", 20, bold=True, center=True),
    Label(165, 422, 215, 42, "CONTEXTO", 20, bold=True, center=True),
    Label(810, 182, 305, 42, "LO QUE FUNCIONÓ", 18, bold=True, center=True),
    Label(810, 262, 305, 42, "LO QUE FALLÓ", 18, bold=True, center=True),
    Label(810, 342, 305, 42, "LO QUE MEJORÓ", 18, bold=True, center=True),
    Label(810, 422, 305, 42, "LO APRENDIDO", 18, bold=True, center=True),
]

# ── gráfico 3 ────────────────────────────────────────────────────────────────
G3_COVERS = [
    Rect(0, 0, 1120, 108),
    Rect(85, 168, 210, 48),
    Rect(85, 278, 210, 48),
    Rect(395, 398, 200, 55),
    Rect(445, 458, 420, 48),
    Rect(165, 518, 420, 125),
    Rect(730, 518, 260, 125),
    Rect(655, 648, 465, 55),
    Rect(655, 695, 465, 38),
]
G3_LABELS = [
    Label(4, 8, 1100, 44, "En vez de adivinar, puntúa cada resultado.", 28, bold=True),
    Label(90, 175, 200, 34, "AGENTE IA", 22, bold=True, green=True, center=True),
    Label(400, 405, 190, 40, "EVALÚA CADA CORRIDA", 17, bold=True, center=True),
    Label(450, 462, 410, 40, "PUNTAJE DE RENDIMIENTO", 22, bold=True, green=True, center=True),
    Label(175, 525, 170, 26, "PRECISIÓN", 18, bold=True),
    Label(175, 555, 170, 26, "CALIDAD", 18, bold=True),
    Label(175, 585, 170, 26, "ERRORES", 18, bold=True),
    Label(175, 615, 220, 26, "OBJETIVO CUMPLIDO", 16, bold=True),
    Label(735, 525, 250, 26, "PRECISIÓN", 18, bold=True, green=True),
    Label(735, 555, 250, 26, "CALIDAD", 18, bold=True, green=True),
    Label(735, 585, 250, 26, "ERRORES", 18, bold=True, green=True),
    Label(735, 615, 250, 26, "OBJETIVO CUMPLIDO", 16, bold=True, green=True),
    Label(660, 652, 455, 28, "El puntaje usa tus métricas personalizadas.", 16),
    Label(660, 698, 455, 30, "DATOS > ANÁLISIS > MEJORA", 16, bold=True, green=True, center=True),
]

# ── gráfico 4 ────────────────────────────────────────────────────────────────
G4_COVERS = [
    Rect(0, 0, 920, 58),
    Rect(50, 168, 180, 38),
    Rect(50, 368, 310, 90),
    Rect(380, 250, 160, 100),
    Rect(670, 168, 190, 38),
    Rect(670, 365, 300, 175),
]
G4_LABELS = [
    Label(4, 8, 900, 44, "Un segundo agente revisa cada corrida sin sesgo.", 26, bold=True),
    Label(50, 172, 175, 30, "AGENTE IA", 22, bold=True, green=True, center=True),
    Label(50, 372, 300, 32, "TRABAJO ENTREGADO", 18, bold=True, green=True, center=True),
    Label(50, 408, 300, 44, "Salida, acciones, decisiones y resultados.", 15),
    Label(385, 265, 150, 70, "ENVÍA TODO A REVISIÓN", 15, bold=True, center=True),
    Label(670, 172, 185, 30, "CRÍTICO IA", 22, bold=True, green=True, center=True),
    Label(675, 372, 270, 30, "¿QUÉ FUNCIONÓ?", 17, bold=True, center=True),
    Label(675, 408, 270, 30, "¿QUÉ FALLÓ?", 17, bold=True, center=True),
    Label(675, 444, 270, 30, "¿POR QUÉ FALLÓ?", 17, bold=True, center=True),
    Label(675, 480, 270, 30, "¿QUÉ CAMBIAR?", 17, bold=True, center=True),
]

# ── gráfico 5 ────────────────────────────────────────────────────────────────
G5_COVERS = [
    Rect(0, 0, 720, 58),
    Rect(0, 52, 500, 75),
    Rect(120, 88, 360, 38),
    Rect(25, 508, 440, 42),
    Rect(510, 118, 610, 55),
    Rect(510, 178, 610, 55),
    Rect(510, 238, 610, 75),
    Rect(510, 358, 610, 55),
    Rect(510, 418, 610, 55),
    Rect(510, 478, 610, 95),
    Rect(510, 668, 610, 100),
]
G5_LABELS = [
    Label(4, 8, 700, 44, "Un fallo no importa. Un patrón cambia todo.", 26, bold=True),
    Label(30, 58, 430, 34, "HISTORIAL DE TAREAS", 24, bold=True, green=True, center=True),
    Label(125, 92, 350, 30, "HISTORIAL DE TAREAS", 22, bold=True, green=True, center=True),
    Label(30, 512, 220, 34, "20 TAREAS EJECUTADAS", 18, bold=True, green=True),
    Label(250, 512, 200, 34, "6 FALLOS", 18, bold=True, color=(255, 90, 90)),
    Label(515, 122, 600, 44, "6 FALLOS DETECTADOS", 20, bold=True, green=True, center=True),
    Label(515, 182, 600, 28, "El agente no solo los registró.", 16),
    Label(515, 242, 600, 44, "ANALIZANDO CAUSAS", 20, bold=True, green=True, center=True),
    Label(515, 278, 600, 28, "Compara entradas, acciones, decisiones y resultados.", 14),
    Label(515, 362, 600, 44, "4 CAUSAS RAÍZ IGUALES", 18, bold=True, green=True, center=True),
    Label(515, 402, 600, 28, "Tareas distintas. Mismo problema de fondo.", 14),
    Label(515, 482, 600, 44, "PATRÓN ENCONTRADO", 22, bold=True, green=True, center=True),
    Label(515, 522, 600, 40, "El agente sigue saltando el Paso #3 del flujo.", 14),
]

# ── gráfico 6 ────────────────────────────────────────────────────────────────
G6_COVERS = [
    Rect(0, 0, 1120, 45),
    Rect(25, 88, 230, 38),
    Rect(25, 368, 260, 110),
    Rect(25, 500, 230, 42),
    Rect(370, 48, 200, 38),
    Rect(360, 268, 260, 200),
    Rect(810, 88, 260, 38),
    Rect(810, 368, 280, 110),
    Rect(810, 500, 260, 42),
]
G6_LABELS = [
    Label(4, 2, 700, 32, "...convierte retroalimentación en mejoras en cada parte del agente.", 20, bold=True),
    Label(30, 92, 220, 30, "AGENTE V1", 26, bold=True, center=True),
    Label(30, 375, 250, 28, "PIERDE CONTEXTO", 17, bold=True, center=True),
    Label(30, 408, 250, 28, "OLVIDA PASOS CRÍTICOS", 16, bold=True, center=True),
    Label(30, 441, 250, 28, "RESULTADOS INCONSISTENTES", 14, bold=True, center=True),
    Label(30, 504, 220, 34, "PUNTAJE: 72/100", 20, bold=True, center=True),
    Label(375, 52, 190, 30, "REFLEXIÓN", 20, bold=True, center=True),
    Label(365, 275, 250, 28, "MEJORAS REALIZADAS:", 17, bold=True, green=True, center=True),
    Label(365, 308, 250, 24, "INSTRUCCIÓN ACTUALIZADA", 14, bold=True, green=True, center=True),
    Label(365, 336, 250, 24, "REGLAS REFINADAS", 15, bold=True, green=True, center=True),
    Label(365, 364, 250, 24, "MEMORIA EXPANDIDA", 15, bold=True, green=True, center=True),
    Label(365, 392, 250, 24, "FLUJO OPTIMIZADO", 15, bold=True, green=True, center=True),
    Label(365, 420, 250, 24, "HERRAMIENTAS MEJORADAS", 14, bold=True, green=True, center=True),
    Label(815, 92, 250, 30, "AGENTE V2", 26, bold=True, green=True, center=True),
    Label(815, 375, 270, 28, "MEJOR CONTEXTO", 17, bold=True, green=True, center=True),
    Label(815, 408, 250, 28, "MENOS ERRORES", 17, bold=True, green=True, center=True),
    Label(815, 441, 250, 28, "MÁS CONSISTENTE", 17, bold=True, green=True, center=True),
    Label(815, 474, 270, 28, "MEJOR CALIDAD", 17, bold=True, green=True, center=True),
    Label(815, 504, 250, 34, "PUNTAJE: 91/100", 20, bold=True, green=True, center=True),
]

# ── gráfico 7 ────────────────────────────────────────────────────────────────
G7_COVERS = [
    Rect(0, 0, 520, 32),
    Rect(15, 45, 330, 55),
    Rect(15, 188, 330, 130),
    Rect(15, 368, 330, 42),
    Rect(0, 460, 1120, 270),
    Rect(545, 45, 330, 55),
    Rect(545, 188, 330, 130),
    Rect(545, 368, 330, 42),
]
G7_LABELS = [
    Label(4, 0, 500, 28, "...antes de quedar en producción.", 20, bold=True),
    Label(25, 52, 320, 34, "VERSIÓN 1 (ANTIGUA)", 22, bold=True, center=True),
    Label(25, 195, 200, 26, "PRECISIÓN", 18, bold=True),
    Label(25, 225, 200, 26, "CALIDAD", 18, bold=True),
    Label(25, 255, 280, 26, "TAREAS APROBADAS", 16, bold=True),
    Label(25, 285, 200, 26, "ERRORES", 18, bold=True),
    Label(25, 372, 300, 34, "PUNTAJE: 82/100", 22, bold=True, center=True),
    Label(555, 52, 310, 34, "VERSIÓN 2 (NUEVA)", 22, bold=True, green=True, center=True),
    Label(555, 195, 200, 26, "PRECISIÓN", 18, bold=True, green=True),
    Label(555, 225, 200, 26, "CALIDAD", 18, bold=True, green=True),
    Label(555, 255, 280, 26, "TAREAS APROBADAS", 16, bold=True, green=True),
    Label(555, 285, 200, 26, "ERRORES", 18, bold=True, green=True),
    Label(555, 372, 300, 34, "PUNTAJE: 91/100", 22, bold=True, green=True, center=True),
    Label(30, 478, 280, 28, "¿MEJOR? CONSERVALA.", 16, bold=True, center=True),
    Label(30, 555, 200, 32, "DESPLEGAR", 20, bold=True, green=True, center=True),
    Label(380, 478, 200, 28, "¿PEOR? REVERTIR.", 16, bold=True, center=True),
    Label(380, 555, 200, 32, "DESCARTAR", 20, bold=True, color=(255, 90, 90), center=True),
    Label(730, 478, 220, 28, "¿IGUAL? SEGUIR PROBANDO", 14, bold=True, center=True),
    Label(730, 555, 200, 32, "ITERAR", 20, bold=True, color=(255, 210, 80), center=True),
    Label(335, 600, 450, 34, "EL FLUJO DE PRUEBAS", 20, bold=True, green=True, center=True),
]

# ── gráfico 8 ────────────────────────────────────────────────────────────────
G8_COVERS = [
    Rect(0, 0, 210, 130),
    Rect(50, 295, 210, 95),
    Rect(370, 125, 250, 105),
    Rect(700, 125, 300, 105),
    Rect(700, 295, 300, 105),
    Rect(370, 425, 250, 105),
    Rect(400, 500, 280, 55),
    Rect(770, 500, 340, 75),
]
G8_LABELS = [
    Label(4, 4, 200, 120, "Corre.\nAprende.\nEvoluciona.\n24/7.", 17, bold=True),
    Label(55, 310, 200, 40, "PROBAR", 28, bold=True, green=True, center=True),
    Label(55, 350, 200, 28, "Demostrá que es mejor", 13, center=True),
    Label(380, 140, 230, 40, "DESPLEGAR", 26, bold=True, green=True, center=True),
    Label(380, 180, 230, 28, "Lanzá la mejor versión", 13, center=True),
    Label(380, 440, 230, 40, "MEJORAR", 28, bold=True, green=True, center=True),
    Label(380, 480, 230, 28, "Mejora el agente", 13, center=True),
    Label(420, 200, 100, 36, "24/7", 34, bold=True, green=True, center=True),
    Label(395, 508, 250, 28, "SIEMPRE MEJORANDO.", 15, bold=True, center=True),
    Label(710, 140, 280, 40, "MEDIR", 28, bold=True, green=True, center=True),
    Label(710, 180, 280, 28, "Puntúa cada resultado", 13, center=True),
    Label(710, 310, 280, 40, "REFLEXIONAR", 24, bold=True, green=True, center=True),
    Label(710, 350, 280, 28, "Critica y encuentra fallos", 13, center=True),
    Label(780, 505, 320, 55, "AGENTE IA AUTOMEJORABLE", 15, bold=True, green=True, center=True),
]


def main() -> None:
    specs = [
        (1, G1_COVERS, G1_LABELS),
        (2, G2_COVERS, G2_LABELS),
        (3, G3_COVERS, G3_LABELS),
        (4, G4_COVERS, G4_LABELS),
        (5, G5_COVERS, G5_LABELS),
        (6, G6_COVERS, G6_LABELS),
        (7, G7_COVERS, G7_LABELS),
        (8, G8_COVERS, G8_LABELS),
    ]
    for n, covers, labels in specs:
        process_image(n, covers, labels)


if __name__ == "__main__":
    main()
