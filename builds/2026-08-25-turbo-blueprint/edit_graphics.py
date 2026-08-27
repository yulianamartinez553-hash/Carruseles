# -*- coding: utf-8 -*-
"""Traduce EN→ES en gráficos Turbo + verde #00FFB2.

Recorta basura de bordes. Tapa EN con negro justo en el texto
(fondo negro → invisible) y escribe ES en el mismo lugar.
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
YEL = (255, 210, 80)
TARGET_H = colorsys.rgb_to_hsv(0, 1, 178 / 255)[0]

# Recortes limpios sobre .orig.png (sin leads EN cortados ni franjas basura)
CROPS: dict[int, tuple[int, int, int, int]] = {
    1: (40, 140, 1095, 900),
    2: (8, 120, 1085, 725),
    3: (8, 155, 1065, 840),
    4: (8, 145, 1055, 810),
    5: (8, 145, 1065, 840),
    6: (8, 105, 1065, 840),
    7: (25, 75, 1045, 840),
    8: (60, 35, 1005, 540),
}


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
    cover: bool = True


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


def cover(img: Image.Image, x: int, y: int, w: int, h: int) -> None:
    ImageDraw.Draw(img).rectangle([x, y, x + w, y + h], fill=(0, 0, 0, 255))


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
        if t.cover:
            cover(out, t.x, t.y, t.w, t.h)
    draw = ImageDraw.Draw(out)
    for t in labels:
        draw_t(draw, t)
    return out


# ── Coords relativas a CROPS ───────────────────────────────────────────────
# G1 — tapa TEST/MEASURE y escribe voseo
G1 = [
    T(488, 0, 145, 50, "HACÉ", 26, W, "center"),
    T(0, 235, 255, 115, "PROBÁ", 24, W, "center"),
    T(865, 235, 190, 115, "MEDÍ", 22, W, "center"),
    T(65, 625, 260, 95, "MEJORÁ", 24, W, "center"),
    T(805, 625, 230, 95, "REFLEXIONÁ", 16, W, "center"),
]

# G2 — tapa INPUT/MEMORY/OUTPUT completo
G2 = [
    T(455, 0, 260, 52, "MEMORIA", 26, V, "center"),
    T(25, 28, 175, 48, "ENTRADA", 18, V, "center"),
    T(915, 28, 165, 48, "SALIDA", 18, V, "center"),
    T(45, 118, 240, 52, "TAREA", 16, W),
    T(45, 235, 240, 54, "ACCIÓN", 16, W),
    T(45, 352, 245, 54, "RESULTADO", 14, W),
    T(45, 470, 245, 54, "CONTEXTO", 14, W),
    T(755, 118, 320, 52, "QUÉ FUNCIONA", 13, W),
    T(755, 235, 320, 54, "QUÉ FALLÓ", 13, W),
    T(755, 352, 320, 54, "QUÉ MEJORÓ", 13, W),
    T(755, 470, 320, 54, "QUÉ CAMBIAR", 13, W),
]

G3 = [
    T(35, 0, 300, 110),
    T(75, 12, 190, 38, "AGENTE TURBO", 16, V, "center", cover=False),
    T(550, 0, 340, 110),
    T(620, 12, 210, 38, "PUNTUACIÓN", 16, V, cover=False),
    T(245, 172, 430, 145),
    T(340, 205, 210, 58, lines=["EVALÚA", "CADA CORRIDA"], size=12, align="center", cover=False),
    T(585, 45, 460, 46, "PRECISIÓN", 14, W),
    T(585, 128, 460, 46, "CALIDAD", 14, W),
    T(585, 211, 460, 46, "ERRORES", 14, W),
    T(585, 294, 460, 46, "OBJETIVO CUMPLIDO", 12, W),
    T(540, 368, 480, 42, "Basado en tus métricas.", 11, GY, font="barlow"),
    T(515, 418, 520, 68),
    T(555, 425, 440, 42, "DATOS → INSIGHT → MEJORA", 11, V, cover=False),
]

G4 = [
    T(95, 0, 220, 55),
    T(115, 8, 180, 38, "AGENTE TURBO", 16, V, "center", cover=False),
    T(40, 385, 320, 110),
    T(55, 395, 290, 34, "TRABAJO ENTREGADO", 13, V, "center", cover=False),
    T(55, 435, 300, 52, lines=["Salida, acciones,", "decisiones y resultados."], size=11, font="barlow", cover=False),
    T(330, 225, 220, 85),
    T(360, 240, 190, 58, lines=["ENVÍA TODO", "A REVISIÓN"], size=11, align="center", cover=False),
    T(680, 0, 320, 58),
    T(710, 8, 280, 42, "CRÍTICO", 16, V, "center", cover=False),
    T(695, 345, 320, 44, "¿QUÉ FUNCIONÓ?", 13, W, font="mono"),
    T(695, 395, 320, 44, "¿QUÉ FALLÓ?", 13, W, font="mono"),
    T(695, 445, 320, 44, "¿POR QUÉ FALLÓ?", 11, W, font="mono"),
    T(695, 495, 320, 44, "¿QUÉ CAMBIAR?", 13, W, font="mono"),
]

G5 = [
    T(55, 0, 360, 52),
    T(80, 8, 300, 38, "HISTORIAL DE TAREAS", 14, V, "center", cover=False),
    T(5, 520, 320, 48, "20 CORRIDAS", 12, W),
    T(255, 520, 200, 48, "6 FALLAS", 12, RED),
    T(575, 0, 450, 95),
    T(592, 5, 415, 38, "6 FALLAS DETECTADAS", 13, W, cover=False),
    T(585, 42, 425, 32, "Turbo no solo las registró.", 11, GY, font="barlow", cover=False),
    T(575, 105, 450, 48, "ANALIZANDO CAUSAS", 13, W),
    T(555, 148, 470, 34, "Compara entradas, acciones y resultados.", 10, GY, font="barlow"),
    T(575, 255, 450, 48, "4 MISMA CAUSA RAÍZ", 12, W),
    T(555, 298, 470, 34, "Tareas distintas. Mismo problema.", 10, GY, font="barlow"),
    T(575, 405, 450, 52),
    T(612, 412, 395, 38, "PATRÓN ENCONTRADO", 13, V, cover=False),
    T(585, 452, 430, 42, "Sigue fallando el Paso #3 del flujo.", 10, GY, font="barlow", cover=False),
]

G6 = [
    T(25, 0, 310, 78),
    T(55, 22, 250, 38, "TURBO V1", 18, W, "center", cover=False),
    T(25, 305, 330, 230),
    T(45, 312, 290, 36, "PIERDE CONTEXTO", 12, W, cover=False),
    T(45, 355, 295, 36, "OLVIDA PASOS CLAVE", 11, W, cover=False),
    T(45, 398, 300, 36, "SALIDAS INCONSISTENTES", 10, W, cover=False),
    T(30, 565, 295, 58, "PUNTAJE: 72/100", 13, W),
    T(340, 0, 350, 78),
    T(375, 18, 270, 38, "REFLEXIÓN", 14, V, "center", cover=False),
    T(335, 248, 360, 300),
    T(360, 255, 310, 32, "MEJORAS APLICADAS:", 12, V, cover=False),
    T(372, 298, 285, 32, "PROMPT ACTUALIZADO", 10, W, cover=False),
    T(372, 340, 285, 32, "REGLAS REFINADAS", 11, W, cover=False),
    T(372, 382, 285, 32, "MEMORIA EXPANDIDA", 11, W, cover=False),
    T(372, 424, 285, 32, "FLUJO OPTIMIZADO", 11, W, cover=False),
    T(372, 466, 285, 32, "HERRAMIENTAS MEJORADAS", 10, W, cover=False),
    T(735, 0, 325, 78),
    T(768, 22, 250, 38, "TURBO V2", 18, V, "center", cover=False),
    T(725, 305, 335, 240),
    T(748, 312, 295, 36, "MEJOR CONTEXTO", 12, W, cover=False),
    T(748, 355, 295, 36, "MENOS ERRORES", 12, W, cover=False),
    T(748, 398, 295, 36, "MÁS CONSISTENTE", 12, W, cover=False),
    T(748, 441, 295, 36, "MAYOR CALIDAD", 12, W, cover=False),
    T(725, 565, 300, 58, "PUNTAJE: 91/100", 13, V),
]

G7 = [
    T(20, 0, 340, 72),
    T(40, 18, 290, 38, "VERSIÓN 1 (ANTERIOR)", 14, W, "center", cover=False),
    T(240, 155, 220, 210),
    T(250, 162, 200, 34, "PRECISIÓN", 11, W, cover=False),
    T(250, 208, 200, 34, "CALIDAD", 11, W, cover=False),
    T(240, 254, 210, 34, "TAREAS OK", 11, W, cover=False),
    T(250, 300, 190, 34, "ERRORES", 11, W, cover=False),
    T(40, 415, 310, 55, "PUNTAJE: 82/100", 14, W),
    T(615, 0, 340, 72),
    T(645, 18, 290, 38, "VERSIÓN 2 (NUEVA)", 14, V, "center", cover=False),
    T(710, 155, 220, 210),
    T(720, 162, 200, 34, "PRECISIÓN", 11, W, cover=False),
    T(720, 208, 200, 34, "CALIDAD", 11, W, cover=False),
    T(710, 254, 210, 34, "TAREAS OK", 11, W, cover=False),
    T(720, 300, 190, 34, "ERRORES", 11, W, cover=False),
    T(640, 415, 310, 55, "PUNTAJE: 91/100", 14, V),
    T(0, 505, 295, 145),
    T(8, 512, 275, 55, lines=["¿MEJOR?", "QUEDATE."], size=12, align="center", cover=False),
    T(25, 598, 210, 42, "DESPLEGAR", 14, V, "center", cover=False),
    T(280, 505, 295, 145),
    T(288, 512, 275, 55, lines=["¿PEOR?", "DESCARTÁ."], size=12, align="center", cover=False),
    T(308, 598, 210, 42, "DESCARTAR", 14, RED, "center", cover=False),
    T(575, 505, 345, 145),
    T(585, 512, 320, 55, lines=["¿IGUAL?", "SEGUÍ PROBANDO."], size=11, align="center", cover=False),
    T(640, 598, 210, 42, "ITERAR", 14, YEL, "center", cover=False),
    T(225, 655, 470, 52, "PIPELINE DE PRUEBAS", 13, V, "center"),
]

G8 = [
    T(0, 0, 175, 125, lines=["Corré.", "Aprendé.", "Evolucioná."], size=13),
    T(115, 0, 290, 88),
    T(125, 2, 250, 34, "DESPLEGÁ", 16, V, cover=False),
    T(125, 38, 260, 28, "Liberá la mejor versión", 10, GY, font="barlow", cover=False),
    T(680, 0, 270, 88),
    T(695, 2, 220, 34, "MEDÍ", 16, V, cover=False),
    T(695, 38, 240, 28, "Puntúa cada resultado", 10, GY, font="barlow", cover=False),
    T(45, 175, 285, 105),
    T(60, 182, 180, 34, "PROBÁ", 16, V, cover=False),
    T(60, 218, 230, 28, "Demostrá que funciona", 10, GY, font="barlow", cover=False),
    T(675, 168, 285, 105),
    T(690, 175, 230, 34, "REFLEXIONÁ", 14, V, cover=False),
    T(690, 212, 250, 28, "Critica y detecta fallas", 10, GY, font="barlow", cover=False),
    T(305, 248, 340, 52, "SIEMPRE MEJORANDO", 12, W, "center"),
    T(315, 345, 300, 95),
    T(345, 352, 240, 34, "MEJORÁ", 16, V, "center", cover=False),
    T(325, 392, 270, 28, "Aplicá upgrades", 10, GY, "center", font="barlow", cover=False),
    T(695, 375, 240, 78, lines=["24/7", "TURBO"], size=14, color=V, align="center"),
]

ALL = {1: G1, 2: G2, 3: G3, 4: G4, 5: G5, 6: G6, 7: G7, 8: G8}


def clean_edges(n: int, img: Image.Image) -> Image.Image:
    out = img.copy()
    w, h = out.size
    if n == 1:
        cover(out, w - 55, 0, 55, h)
    elif n == 2:
        cover(out, 0, h - 12, w, 12)
        cover(out, w - 8, 130, 8, 420)
        cover(out, w - 100, h - 180, 70, 50)  # ... UI
    elif n == 3:
        cover(out, w - 18, h - 85, 18, 85)
    elif n == 7:
        cover(out, w - 22, 0, 22, 55)
        cover(out, w - 25, h - 70, 25, 70)
    elif n == 8:
        cover(out, w - 15, 0, 15, h)
        cover(out, w - 160, h - 60, 160, 60)
    return out


def process(n: int) -> None:
    bak = ASSETS / f"graphic-{n:02d}.orig.png"
    src = ASSETS / f"graphic-{n:02d}.png"
    if not bak.exists():
        Image.open(src).save(bak)
    img = Image.open(bak).convert("RGBA")
    img = img.crop(CROPS[n])
    img = boost_green(img)
    img = clean_edges(n, img)
    img = apply(img, ALL[n])
    img.save(src, optimize=True)
    print(f"OK graphic-{n:02d} → {img.size}")


def main() -> None:
    for i in range(1, 9):
        process(i)


if __name__ == "__main__":
    main()
