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
    1: (40, 140, 1095, 900),  # incluye ícono MEDÍ completo
    2: (8, 55, 1085, 725),  # sin franja inferior de íconos
    3: (8, 130, 1065, 840),
    4: (8, 115, 1055, 810),
    5: (8, 115, 1065, 840),
    6: (8, 70, 1065, 840),
    7: (25, 60, 1045, 840),
    8: (60, 20, 1005, 540),
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
# G1: voseo correcto — covers altos; MEDÍ a la derecha del ícono (no lo tapa)
G1 = [
    T(500, 0, 120, 42, "HACÉ", 26, W, "center"),
    T(25, 280, 130, 55, "PROBÁ", 24, W, "center"),
    T(1005, 280, 90, 55, "MEDÍ", 20, W, "center"),  # derecha del ícono
    T(100, 640, 210, 80, "MEJORÁ", 24, W, "center"),
    T(850, 640, 180, 80, "REFLEXIONÁ", 16, W, "center"),
]

# G2: OUTPUT labels izq de íconos; covers altos en INPUT
G2 = [
    T(495, 2, 220, 42, "MEMORIA", 26, V, "center"),
    T(50, 50, 135, 40, "ENTRADA", 18, V, "center"),
    T(950, 50, 130, 40, "SALIDA", 18, V, "center"),
    T(85, 145, 155, 45, "TAREA", 16, W),
    T(85, 265, 155, 45, "ACCIÓN", 16, W),
    T(85, 383, 160, 48, "RESULTADO", 14, W),
    T(85, 503, 165, 48, "CONTEXTO", 14, W),
    T(855, 152, 95, 38, "ÉXITO", 14, W, "center"),
    T(1025, 152, 55, 38),
    T(855, 272, 95, 38, "FALLO", 14, W, "center"),
    T(1025, 272, 55, 38),
    T(855, 392, 95, 38, "MEJORA", 13, W, "center"),
    T(1025, 392, 55, 38),
    T(855, 512, 95, 38, "CAMBIO", 13, W, "center"),
    T(1025, 512, 55, 38),
]

G3 = [
    T(75, 45, 185, 36, "AGENTE IA", 16, V, "center"),
    T(350, 250, 210, 65, lines=["EVALÚA", "CADA CORRIDA"], size=12, align="center"),
    T(680, 15, 175, 36, "PRECISIÓN", 14, W),
    T(680, 115, 165, 36, "CALIDAD", 14, W),
    T(680, 215, 155, 36, "ERRORES", 14, W),
    T(680, 310, 290, 40, "OBJETIVO CUMPLIDO", 12, W),
    T(580, 405, 400, 36, "Basado en tus métricas.", 12, GY, font="barlow"),
    T(605, 470, 370, 38, "DATOS > ANÁLISIS > MEJORA", 11, V),
]

# G4: NO tapar robots — solo texto
G4 = [
    T(115, 40, 180, 36, "AGENTE IA", 16, V, "center"),
    T(55, 400, 280, 36, "TRABAJO ENTREGADO", 13, V, "center"),
    T(55, 440, 300, 55, lines=["Salida, acciones,", "decisiones y resultados."], size=11, font="barlow"),
    T(360, 250, 190, 70, lines=["ENVÍA TODO", "A REVISIÓN"], size=11, align="center"),
    T(710, 5, 280, 55, "CRÍTICO IA", 16, V, "center"),
    T(720, 360, 280, 36, "¿QUÉ FUNCIONÓ?", 13, W, font="mono"),
    T(720, 408, 280, 36, "¿QUÉ FALLÓ?", 13, W, font="mono"),
    T(720, 460, 280, 36, "¿POR QUÉ FALLÓ?", 11, W, font="mono"),
    T(720, 512, 280, 36, "¿QUÉ CAMBIAR?", 13, W, font="mono"),
]

G5 = [
    T(80, 20, 300, 40, "HISTORIAL DE TAREAS", 14, V, "center"),
    T(15, 545, 280, 40, "20 TAREAS EJECUTADAS", 12, W),
    T(280, 545, 155, 40, "6 FALLOS", 12, RED),
    T(620, 25, 370, 36, "6 FALLOS DETECTADOS", 13, W),
    T(620, 62, 370, 30, "El agente no solo los registró.", 11, W, font="barlow"),
    T(620, 145, 370, 36, "ANALIZANDO CAUSAS", 13, W),
    T(585, 185, 430, 34, "Compara entradas, acciones y resultados.", 10, W, font="barlow"),
    T(620, 295, 370, 36, "4 CAUSAS RAÍZ IGUALES", 12, W),
    T(595, 338, 400, 30, "Tareas distintas. Mismo problema.", 10, W, font="barlow"),
    T(645, 450, 340, 36, "PATRÓN ENCONTRADO", 13, V),
    T(625, 492, 380, 40, "El agente salta el Paso #3 del flujo.", 10, W, font="barlow"),
]

G6 = [
    T(55, 25, 250, 42, "AGENTE V1", 18, W, "center"),
    # cada línea EN completa (evita ghosting)
    T(45, 345, 290, 130),
    T(55, 350, 270, 34, "PIERDE CONTEXTO", 12, W, cover=False),
    T(55, 395, 280, 34, "OLVIDA PASOS CRÍTICOS", 11, W, cover=False),
    T(55, 440, 290, 34, "RESULTADOS INCONSISTENTES", 10, W, cover=False),
    T(50, 615, 260, 42, "PUNTAJE: 72/100", 13, W),
    T(385, 10, 240, 40, "REFLEXIÓN", 14, W, "center"),
    T(370, 290, 300, 270),
    T(385, 295, 270, 32, "MEJORAS HECHAS:", 12, V, cover=False),
    T(400, 340, 250, 30, "INSTRUCCIÓN ACTUALIZADA", 10, W, cover=False),
    T(400, 385, 250, 30, "REGLAS REFINADAS", 11, W, cover=False),
    T(400, 430, 250, 30, "MEMORIA EXPANDIDA", 11, W, cover=False),
    T(400, 475, 250, 30, "FLUJO OPTIMIZADO", 11, W, cover=False),
    T(400, 520, 250, 30, "HERRAMIENTAS MEJORADAS", 10, W, cover=False),
    T(815, 10, 240, 42, "AGENTE V2", 18, V, "center"),
    T(765, 345, 295, 180),
    T(780, 350, 270, 34, "MEJOR CONTEXTO", 12, W, cover=False),
    T(780, 395, 270, 34, "MENOS ERRORES", 12, W, cover=False),
    T(780, 440, 270, 34, "MÁS CONSISTENTE", 12, W, cover=False),
    T(780, 485, 270, 34, "MEJOR CALIDAD", 12, W, cover=False),
    T(785, 615, 260, 42, "PUNTAJE: 91/100", 13, V),
]

G7 = [
    T(40, 10, 290, 40, "VERSIÓN 1 (ANTERIOR)", 14, W, "center"),
    T(265, 185, 180, 190),
    T(275, 190, 160, 30, "PRECISIÓN", 11, W, cover=False),
    T(275, 238, 160, 30, "CALIDAD", 11, W, cover=False),
    T(265, 280, 175, 30, "APROBADAS", 11, W, cover=False),
    T(275, 328, 140, 30, "ERRORES", 11, W, cover=False),
    T(60, 450, 280, 48, "PUNTAJE: 82/100", 14, W),
    T(650, 5, 290, 40, "VERSIÓN 2 (NUEVA)", 14, V, "center"),
    T(735, 185, 180, 190),
    T(745, 190, 160, 30, "PRECISIÓN", 11, W, cover=False),
    T(745, 238, 160, 30, "CALIDAD", 11, W, cover=False),
    T(735, 280, 175, 30, "APROBADAS", 11, W, cover=False),
    T(745, 328, 140, 30, "ERRORES", 11, W, cover=False),
    T(680, 450, 280, 48, "PUNTAJE: 91/100", 14, V),
    T(10, 555, 245, 100),
    T(20, 560, 225, 48, lines=["¿MEJOR?", "CONSERVÁLA."], size=12, align="center", cover=False),
    T(40, 630, 180, 36, "DESPLEGAR", 14, V, "center", cover=False),
    T(315, 555, 245, 100),
    T(325, 560, 225, 48, lines=["¿PEOR?", "REVERTIR."], size=12, align="center", cover=False),
    T(340, 630, 180, 36, "DESCARTAR", 14, RED, "center", cover=False),
    T(620, 555, 290, 100),
    T(630, 560, 270, 48, lines=["¿IGUAL?", "SEGUIR PROBANDO"], size=11, align="center", cover=False),
    T(665, 630, 180, 36, "ITERAR", 14, YEL, "center", cover=False),
    T(300, 695, 380, 40, "EL FLUJO DE PRUEBAS", 13, V, "center"),
]

G8 = [
    T(0, 0, 155, 115, lines=["Corré.", "Aprendé.", "Evolucioná.", "24/7."], size=13),
    T(125, 0, 270, 80),
    T(135, 2, 240, 32, "DESPLEGÁ", 16, V, cover=False),
    T(135, 38, 250, 26, "Lanzá la mejor versión", 10, W, font="barlow", cover=False),
    T(700, 0, 250, 80),
    T(715, 2, 210, 32, "MEDÍ", 16, V, cover=False),
    T(715, 38, 230, 26, "Puntuá cada resultado", 10, W, font="barlow", cover=False),
    T(60, 200, 260, 95),
    T(75, 205, 170, 32, "PROBÁ", 16, V, cover=False),
    T(75, 242, 210, 26, "Demostrá que es mejor", 10, W, font="barlow", cover=False),
    T(690, 195, 270, 95),
    T(705, 200, 220, 32, "REFLEXIONÁ", 14, V, cover=False),
    T(705, 237, 240, 26, "Criticá y encontrá fallos", 10, W, font="barlow", cover=False),
    T(330, 375, 290, 100),
    T(360, 385, 220, 32, "MEJORÁ", 16, V, "center", cover=False),
    T(340, 425, 260, 26, "Mejorá el agente", 10, W, "center", font="barlow", cover=False),
    T(340, 265, 300, 42, "SIEMPRE MEJORANDO.", 11, W, "center"),
    T(750, 410, 200, 65, lines=["AGENTE", "AUTOMEJORABLE"], size=11, color=V, align="center"),
]

ALL = {1: G1, 2: G2, 3: G3, 4: G4, 5: G5, 6: G6, 7: G7, 8: G8}


def clean_edges(n: int, img: Image.Image) -> Image.Image:
    out = img.copy()
    w, h = out.size
    if n == 1:
        # basura derecha más allá de MEDÍ
        cover(out, w - 30, 0, 30, h)
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
