# -*- coding: utf-8 -*-
"""Elementos SVG del carrusel 'memoria que vende' — recreados de la referencia.
La estrella naranja se mantiene EXACTA: starburst de brazos redondeados, color naranja
de la referencia (#E85A24). Claude siempre naranja."""
import math
import random

NARANJA = "#E85A24"     # naranja de la referencia (estrella / acentos / pill)
VIOLETA = "#8B5CF6"     # diamante (la bóveda)
DORADO = "#E8B23A"      # chispa (el agente)
NAVY = "#1A2230"        # círculos oscuros / ventana


def starburst(width, color=NARANJA, arms=8, thick=15, cls="", opacity=1):
    """Estrella de brazos redondeados idéntica a la de la referencia."""
    parts = []
    for i in range(arms):
        ang = i * 360 / arms
        parts.append(
            f'<rect x="{50 - thick / 2}" y="3" width="{thick}" height="47" rx="{thick / 2}" '
            f'fill="{color}" transform="rotate({ang} 50 50)"/>'
        )
    return (f'<svg class="{cls}" width="{width}" viewBox="0 0 100 100" style="opacity:{opacity}" '
            f'xmlns="http://www.w3.org/2000/svg">' + "".join(parts) + "</svg>")


def diamond(size, color=VIOLETA):
    """Gema estilo Obsidian simplificada."""
    return (f'<svg width="{size}" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="M12 1 L22 9 L12 23 L2 9 Z" fill="{color}"/>'
            f'<path d="M12 1 L12 23 L2 9 Z" fill="{color}" opacity=".72"/></svg>')


def spark(size, color=DORADO):
    """Pluma/chispa dorada estilo Hermes simplificada."""
    return (f'<svg width="{size}" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="M22 3 C 12 4, 5 10, 3 21 C 10 19, 17 14, 19 9 L15 10 L21 5 Z" fill="{color}"/></svg>')


def flower_badge(width):
    """Flor festoneada crema con estrella oscura adentro (slide aprende solo)."""
    petals = []
    for i in range(10):
        a = math.radians(i * 36)
        petals.append(f'<circle cx="{50 + 32 * math.cos(a):.1f}" cy="{50 + 32 * math.sin(a):.1f}" '
                      f'r="15" fill="#F3EDDE" stroke="#E2DAC6" stroke-width="1"/>')
    star_pts = []
    for i in range(10):
        r = 20 if i % 2 == 0 else 8.5
        a = math.radians(-90 + i * 36)
        star_pts.append(f"{50 + r * math.cos(a):.1f},{50 + r * math.sin(a):.1f}")
    return (f'<svg width="{width}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">'
            + "".join(petals) + f'<circle cx="50" cy="50" r="33" fill="#F3EDDE"/>'
            f'<polygon points="{" ".join(star_pts)}" fill="{NAVY}"/></svg>')


def constellation(w=1080, h=1350, seed=7):
    """Grafo de puntos y líneas sutil para la portada (blanco)."""
    rnd = random.Random(seed)
    pts = [(rnd.randint(40, w - 40), rnd.randint(60, h - 120)) for _ in range(22)]
    lines, dots = [], []
    for i, (x, y) in enumerate(pts):
        # conectar con el vecino más cercano
        best, bd = None, 1e9
        for j, (x2, y2) in enumerate(pts):
            if i == j:
                continue
            d = (x - x2) ** 2 + (y - y2) ** 2
            if d < bd:
                bd, best = d, (x2, y2)
        lines.append(f'<line x1="{x}" y1="{y}" x2="{best[0]}" y2="{best[1]}" '
                     f'stroke="#d9d9d2" stroke-width="1.4"/>')
        color, r = "#c9c9c2", 5
        if i % 7 == 0:
            color, r = NARANJA, 7
        elif i % 9 == 3:
            color, r = VIOLETA, 6
        dots.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>')
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'style="position:absolute;inset:0;z-index:0;" xmlns="http://www.w3.org/2000/svg">'
            + "".join(lines) + "".join(dots) + "</svg>")


def graph_cluster(w=560, h=330, seed=11):
    """Nube de puntitos de colores tipo vista de grafo (ventana del CRM)."""
    rnd = random.Random(seed)
    cx, cy = w / 2, h / 2
    colors = [NARANJA, "#00FFB2", VIOLETA, "#6FA8FF", "#E8B23A", "#c9c9c2"]
    lines, dots = [], []
    pts = []
    for _ in range(60):
        a = rnd.uniform(0, 6.283)
        r = abs(rnd.gauss(0, 1)) * min(w, h) * 0.24
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a) * 0.8))
    for i in range(0, 40, 2):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        lines.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
                     f'stroke="#2a3040" stroke-width="1"/>')
    for i, (x, y) in enumerate(pts):
        dots.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(2.2, 4.4):.1f}" '
                    f'fill="{colors[i % len(colors)]}"/>')
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'xmlns="http://www.w3.org/2000/svg">' + "".join(lines) + "".join(dots) + "</svg>")


def window(title, inner, width=880, screen_h=430):
    """Ventana de app estilo mac: barra con tres puntos + pantalla oscura."""
    return (f'<div class="win" style="width:{width}px;">'
            f'<div class="win-bar"><i style="background:#FF5F57"></i><i style="background:#FEBC2E"></i>'
            f'<i style="background:#28C840"></i><span>{title}</span></div>'
            f'<div class="win-screen" style="height:{screen_h}px;">{inner}</div></div>')
