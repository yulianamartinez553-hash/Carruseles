# -*- coding: utf-8 -*-
"""Traduce texto EN→ES en el mismo lugar/estilo + refuerza verde #00FFB2.

Estrategia: tapa con negro el bbox completo del inglés y escribe ES
en las mismas coordenadas, misma escala aproximada.
"""
from __future__ import annotations

import colorsys
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

B = Path(__file__).resolve().parent
ASSETS = B / "assets"
FONTS = Path("/tmp/stlabs-fonts")
V = (0, 255, 178)
W = (242, 242, 242)
RED = (255, 90, 90)
GY = (180, 180, 180)
TARGET_H = colorsys.rgb_to_hsv(0, 1, 178 / 255)[0]


@dataclass
class T:
    x: int
    y: int
    w: int
    h: int
    text: str = ""
    size: int = 20
    color: tuple[int, int, int] = W
    align: str = "left"
    font: str = "poppins"
    lines: list[str] = field(default_factory=list)
    skip_cover: bool = False


def get_font(kind: str, size: int) -> ImageFont.FreeTypeFont:
    if kind == "mono":
        path = FONTS / "IBMPlexMono-SemiBold.ttf"
    elif kind == "barlow":
        path = FONTS / "BarlowCondensed-Bold.ttf"
    else:
        path = FONTS / "Poppins-Bold.ttf"
    return ImageFont.truetype(str(path), size)


def boost_green(img: Image.Image, strength: float = 0.42) -> Image.Image:
    arr = np.array(img.convert("RGBA"), dtype=np.float32)
    r, g, b, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    mask = (a > 20) & (g > 55) & (g >= r * 0.95) & (g >= b * 0.85) & (lum > 35)
    ys, xs = np.where(mask)
    for y, x in zip(ys.tolist(), xs.tolist()):
        rv, gv, bv = r[y, x] / 255, g[y, x] / 255, b[y, x] / 255
        h, s, v = colorsys.rgb_to_hsv(rv, gv, bv)
        h = h * (1 - strength) + TARGET_H * strength
        s = min(1.0, s * (1 + strength * 0.55))
        v = min(1.0, v * (1 + strength * 0.12))
        nr, ng, nb = colorsys.hsv_to_rgb(h, s, v)
        ng = ng * (1 - strength * 0.25) + (strength * 0.25)
        nr *= 1 - strength * 0.15
        nb *= 1 - strength * 0.2
        arr[y, x, 0] = min(255, nr * 255)
        arr[y, x, 1] = min(255, ng * 255)
        arr[y, x, 2] = min(255, nb * 255)
    return Image.fromarray(arr.astype(np.uint8), "RGBA")


def erase_roi(img: Image.Image, x: int, y: int, w: int, h: int) -> None:
    """Pinta negro sólido en el ROI (tapa cualquier resto EN)."""
    draw = ImageDraw.Draw(img)
    draw.rectangle([x, y, x + w, y + h], fill=(0, 0, 0, 255))


def fit_size(text: str, max_w: int, start: int, kind: str) -> int:
    size = start
    while size > 9:
        f = get_font(kind, size)
        bb = f.getbbox(text)
        if bb[2] - bb[0] <= max_w:
            return size
        size -= 1
    return 9


def draw_t(draw: ImageDraw.ImageDraw, t: T) -> None:
    lines = t.lines if t.lines else ([t.text] if t.text else [])
    if not lines:
        return
    size = t.size
    for line in lines:
        size = min(size, fit_size(line, max(8, t.w - 4), size, t.font))
    font = get_font(t.font, size)
    line_h = size + 3
    total_h = line_h * len(lines) - 3
    y0 = t.y + max(0, (t.h - total_h) // 2)
    for i, line in enumerate(lines):
        bb = font.getbbox(line)
        tw = bb[2] - bb[0]
        if t.align == "center":
            tx = t.x + (t.w - tw) // 2
        elif t.align == "right":
            tx = t.x + t.w - tw
        else:
            tx = t.x + 2
        ty = y0 + i * line_h - bb[1]
        draw.text((tx, ty), line, fill=t.color + (255,), font=font)


def apply(img: Image.Image, labels: list[T]) -> Image.Image:
    out = img.copy()
    for t in labels:
        if not t.skip_cover:
            erase_roi(out, t.x, t.y, t.w, t.h)
    draw = ImageDraw.Draw(out)
    for t in labels:
        draw_t(draw, t)
    return out


# ═══════════════════════════════════════════════════════════════════════════
# Coordenadas = bbox del texto EN original (generoso) → ES en el mismo sitio
# ═══════════════════════════════════════════════════════════════════════════

G1 = [
    # tapa todo el headline EN (incluye 24/7. original con glow)
    T(55, 70, 520, 55),
    T(60, 78, 200, 42, "MEJORA", 34, W, skip_cover=True),
    T(230, 78, 180, 42, "24/7.", 34, V, skip_cover=True),
    T(600, 78, 90, 45, "HACÉ", 28, W, "center"),
    T(95, 430, 110, 45, "PROBÁ", 26, W),
    T(1045, 428, 120, 45, "MEDÍ", 26, W),
    T(165, 780, 190, 45, "MEJORÁ", 26, W),
    T(910, 780, 210, 45, "REFLEXIONÁ", 22, W),
]

G2 = [
    T(0, 0, 410, 42, "...datos de los que puede aprender.", 20, V, font="barlow"),
    T(520, 52, 200, 48, "MEMORIA", 30, V, "center"),
    T(60, 110, 120, 40, "ENTRADA", 20, V, "center"),
    T(960, 110, 160, 40, "SALIDA", 20, V, "center"),
    T(90, 210, 140, 40, "TAREA", 18, W),
    T(90, 332, 140, 40, "ACCIÓN", 18, W),
    T(90, 454, 150, 40, "RESULTADO", 16, W),
    T(90, 576, 160, 40, "CONTEXTO", 16, W),
    T(1030, 210, 90, 40, "ÉXITO", 14, W),
    T(1030, 332, 90, 40, "FALLO", 14, W),
    T(1030, 454, 90, 40, "MEJORA", 13, W),
    T(1030, 576, 90, 40, "APRENDIZ.", 12, W),
]

G3 = [
    # tapa headline EN completo (incluye "it scores every result")
    T(0, 0, 750, 100),
    T(0, 12, 520, 30, "En vez de adivinar,", 22, W, skip_cover=True),
    T(0, 42, 95, 30, "puntúa", 22, V, skip_cover=True),
    T(100, 42, 300, 30, "cada resultado.", 22, W, skip_cover=True),
    T(100, 185, 180, 40, "AGENTE IA", 20, V, "center"),
    T(400, 400, 190, 80, lines=["EVALÚA", "CADA CORRIDA"], size=15, align="center"),
    # métricas — tapa más baja/alta para cubrir EN completo
    T(740, 100, 240, 55, "PRECISIÓN", 18, W),
    T(740, 205, 240, 75, "CALIDAD", 18, W),
    T(740, 315, 230, 80, "ERRORES", 18, W),
    # GOAL COMPLETED está en y=499-518
    T(740, 445, 320, 85, "OBJETIVO CUMPLIDO", 15, W),
    T(630, 560, 480, 55, "Basado en tus métricas personalizadas.", 14, GY, font="barlow"),
    T(660, 630, 440, 55, "DATOS > ANÁLISIS > MEJORA", 14, V),
]

G4 = [
    T(0, 20, 560, 80),
    T(0, 28, 520, 30, "Un segundo agente revisa cada corrida", 18, W, skip_cover=True),
    T(0, 55, 50, 30, "sin", 18, W, skip_cover=True),
    T(48, 55, 140, 30, "sesgo.", 18, V, skip_cover=True),
    T(130, 165, 200, 50, "AGENTE IA", 20, V, "center"),
    T(60, 530, 320, 50, "TRABAJO ENTREGADO", 16, V, "center"),
    T(60, 575, 350, 90, lines=["Salida, acciones,", "decisiones y resultados."], size=14, font="barlow"),
    T(400, 390, 190, 120, lines=["ENVÍA TODO", "A REVISIÓN"], size=14, align="center"),
    # AI CRITIC — tapa desde más arriba el glow EN
    T(750, 110, 300, 110, "CRÍTICO IA", 20, V, "center"),
    T(760, 505, 360, 65, "¿QUÉ FUNCIONÓ?", 16, W, font="mono"),
    T(760, 555, 360, 65, "¿QUÉ FALLÓ?", 16, W, font="mono"),
    T(760, 610, 360, 65, "¿POR QUÉ FALLÓ?", 14, W, font="mono"),
    # WHAT SHOULD CHANGE y=723-742
    T(760, 660, 360, 95, "¿QUÉ CAMBIAR?", 16, W, font="mono"),
]

G5 = [
    T(0, 10, 560, 95),
    T(0, 20, 500, 30, "Un fallo no importa.", 20, W, skip_cover=True),
    T(0, 50, 130, 30, "Un patrón", 20, V, skip_cover=True),
    T(135, 50, 280, 30, "cambia todo.", 20, W, skip_cover=True),
    T(110, 145, 320, 55, "HISTORIAL DE TAREAS", 18, V, "center"),
    T(25, 705, 500, 55, "20 TAREAS EJECUTADAS", 14, W),
    T(290, 705, 200, 55, "6 FALLOS", 14, RED, skip_cover=True),
    T(670, 150, 440, 55, "6 FALLOS DETECTADOS", 17, W),
    T(670, 195, 440, 50, "El agente no solo los registró.", 13, W, font="barlow"),
    T(670, 285, 420, 55, "ANALIZANDO CAUSAS", 17, W),
    T(600, 330, 510, 60, "Compara entradas, acciones, decisiones y resultados.", 12, W, font="barlow"),
    T(670, 445, 440, 55, "4 CAUSAS RAÍZ IGUALES", 15, W),
    T(630, 505, 480, 50, "Tareas distintas. Mismo problema de fondo.", 12, W, font="barlow"),
    T(690, 620, 400, 55, "PATRÓN ENCONTRADO", 17, V),
    T(670, 675, 440, 70, "El agente sigue saltando el Paso #3 del flujo.", 12, W, font="barlow"),
]

G6 = [
    T(0, 0, 750, 55, "...convierte la retro en mejoras en cada parte del agente.", 15, W, font="barlow"),
    T(80, 105, 240, 55, "AGENTE V1", 24, W, "center"),
    T(70, 455, 270, 50, "PIERDE CONTEXTO", 15, W),
    T(70, 510, 280, 50, "OLVIDA PASOS CRÍTICOS", 14, W),
    T(70, 565, 290, 50, "RESULTADOS INCONSISTENTES", 13, W),
    T(70, 735, 260, 50, "PUNTAJE: 72/100", 16, W),
    T(440, 90, 220, 50, "REFLEXIÓN", 18, W, "center"),
    T(410, 395, 300, 50, "MEJORAS HECHAS:", 16, V),
    T(450, 450, 270, 50, "INSTRUCCIÓN ACTUALIZADA", 12, W),
    T(450, 505, 270, 50, "REGLAS REFINADAS", 14, W),
    T(450, 555, 270, 50, "MEMORIA EXPANDIDA", 14, W),
    T(450, 600, 270, 50, "FLUJO OPTIMIZADO", 14, W),
    T(450, 650, 270, 50, "HERRAMIENTAS MEJORADAS", 12, W),
    T(870, 90, 240, 55, "AGENTE V2", 24, V, "center"),
    T(820, 455, 290, 50, "MEJOR CONTEXTO", 15, W),
    T(820, 510, 290, 50, "MENOS ERRORES", 15, W),
    T(820, 565, 290, 50, "MÁS CONSISTENTE", 15, W),
    T(820, 615, 290, 50, "MEJOR CALIDAD", 15, W),
    T(850, 730, 260, 50, "PUNTAJE: 91/100", 16, V),
]

G7 = [
    T(0, 0, 300, 40, "...antes de lanzarlo.", 18, W, font="barlow"),
    T(80, 80, 300, 50, "VERSIÓN 1 (ANTERIOR)", 18, W, "center"),
    T(95, 275, 180, 40, "PRECISIÓN", 16, W),
    T(95, 330, 180, 40, "CALIDAD", 16, W),
    T(95, 375, 240, 40, "TAREAS APROBADAS", 14, W),
    T(95, 425, 160, 40, "ERRORES", 16, W),
    T(100, 555, 280, 50, "PUNTAJE: 82/100", 18, W),
    T(760, 75, 300, 50, "VERSIÓN 2 (NUEVA)", 18, V, "center"),
    T(770, 275, 180, 40, "PRECISIÓN", 16, W),
    T(770, 330, 180, 40, "CALIDAD", 16, W),
    T(770, 375, 240, 40, "TAREAS APROBADAS", 14, W),
    T(770, 425, 160, 40, "ERRORES", 16, W),
    T(770, 555, 280, 50, "PUNTAJE: 91/100", 18, V),
    T(30, 670, 250, 60, lines=["¿MEJOR?", "CONSERVALA."], size=15, align="center"),
    T(80, 750, 200, 45, "DESPLEGAR", 18, V, "center"),
    T(380, 670, 250, 60, lines=["¿PEOR?", "REVERTIR."], size=15, align="center"),
    T(400, 750, 200, 45, "DESCARTAR", 18, RED, "center"),
    T(700, 670, 300, 60, lines=["¿IGUAL?", "SEGUIR PROBANDO"], size=14, align="center"),
    T(760, 750, 200, 45, "ITERAR", 18, (255, 210, 80), "center"),
    T(380, 820, 400, 45, "EL FLUJO DE PRUEBAS", 16, V, "center"),
]

G8 = [
    T(0, 0, 210, 140, lines=["Corre.", "Aprende.", "Evoluciona.", "24/7."], size=16),
    T(200, 30, 280, 40, "DESPLEGÁ", 22, V),
    T(200, 70, 280, 35, "Lanzá la mejor versión", 13, W, font="barlow"),
    T(860, 30, 250, 40, "MEDÍ", 22, V),
    T(860, 70, 250, 35, "Puntúa cada resultado", 13, W, font="barlow"),
    T(140, 285, 200, 40, "PROBÁ", 22, V),
    T(140, 325, 240, 35, "Demostrá que es mejor", 13, W, font="barlow"),
    T(850, 275, 250, 40, "REFLEXIONÁ", 18, V),
    T(850, 315, 260, 35, "Criticá y encontrá fallos", 12, W, font="barlow"),
    T(460, 490, 220, 40, "MEJORÁ", 22, V, "center"),
    T(420, 530, 280, 35, "Mejorá el agente", 13, W, "center", font="barlow"),
    T(440, 365, 300, 40, "SIEMPRE MEJORANDO.", 14, W, "center"),
    T(900, 540, 220, 70, lines=["AGENTE", "AUTOMEJORABLE"], size=13, color=V, align="center"),
]

ALL = {1: G1, 2: G2, 3: G3, 4: G4, 5: G5, 6: G6, 7: G7, 8: G8}


def process(n: int) -> None:
    src = ASSETS / f"graphic-{n:02d}.png"
    bak = ASSETS / f"graphic-{n:02d}.orig.png"
    if not bak.exists():
        Image.open(src).save(bak)
    img = boost_green(Image.open(bak).convert("RGBA"))
    img = apply(img, ALL[n])
    img.save(src, optimize=True)
    print(f"OK graphic-{n:02d}")


def main() -> None:
    for i in range(1, 9):
        process(i)


if __name__ == "__main__":
    main()
