# Manifiesto de fuentes — Te genero un trader IA para tu empresa

| Fuente | Peso / estilo | Rol | Origen | Código de carga |
|---|---|---|---|---|
| Bebas Neue | 400 normal | Títulos display | skill `assets/fonts/` | `@font-face` base64 BebasNeue-Regular.ttf |
| Barlow Condensed | Medium 500 / Bold 700 | Cuerpo / subtítulos | skill `assets/fonts/` | `@font-face` BarlowCondensed-Medium.ttf / Bold.ttf |
| IBM Plex Mono | Medium 500 / SemiBold 600 | Meta box, labels, firma | skill `assets/fonts/` | `@font-face` IBMPlexMono-Medium.ttf / SemiBold.ttf |

Instalación local: `python3 .claude/skills/carrusel-stlabs/assets/install_fonts.py` (o copiar TTFs a `/tmp/stlabs-fonts/`).

Las fuentes van embebidas en base64 dentro de `carrusel.html` vía `generate.py` → `font_css()`.
