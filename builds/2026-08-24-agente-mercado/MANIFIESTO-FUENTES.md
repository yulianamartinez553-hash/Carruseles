# Manifiesto de fuentes — Agente a medida (2026-08-24)

| Fuente | Peso / estilo | Rol | Origen | Código / comando de carga |
|---|---|---|---|---|
| Poppins | 800 ExtraBold | título display (+ degradé clip) | GitHub google/fonts (`ofl/poppins/Poppins-ExtraBold.ttf`) → `/tmp/stlabs-fonts/` | `@font-face{font-family:'Poppins';font-weight:800;src:url(data:font/ttf;base64,...) format('truetype');}` |
| Poppins | 700 Bold | títulos secundarios / filas | GitHub google/fonts (`ofl/poppins/Poppins-Bold.ttf`) | idem base64 embebido en `carrusel.html` |
| Barlow Condensed | 700 Bold | énfasis en lead | skill assets / stlabs pack | `@font-face{font-family:'Barlow Condensed';font-weight:700;...}` |
| Barlow Condensed | 500 Medium | cuerpo / lead | skill assets | `@font-face{font-family:'Barlow Condensed';font-weight:500;...}` |
| IBM Plex Mono | 600 SemiBold | kickers, chips, labels | skill assets (`IBMPlexMono-SemiBold.ttf`) | `@font-face{font-family:'IBM Plex Mono';font-weight:600;...}` |
| IBM Plex Mono | 500 Medium | footer `sebastian.stlabs.ar` | skill assets | `@font-face{font-family:'IBM Plex Mono';font-weight:500;...}` |

## Asset visual

| Asset | Uso | Notas |
|---|---|---|
| `assets/turbo.png` | Fondo portada + CTA (`.ph-bg`) | Mascota Turbo; scrim degradé negro → verde sutil (`.ph-scrim`) |
| Degradé en letras | `.grad` / `.grad2` / `.cta .kw` | Mecánica `@degradé` — mint → `#00FFB2` → verde oscuro |

Instalación local (sin red en el entorno cloud):

```bash
python3 .claude/skills/carrusel-stlabs/assets/install_fonts.py
# fallback si /usr/share no es escribible:
cp .claude/skills/carrusel-stlabs/assets/fonts/*.ttf /tmp/stlabs-fonts/
```

Todas las caras van **embebidas en base64** dentro de `carrusel.html` (standalone, sin CDN).
