# Manifiesto de fuentes — Agente simplifica procesos

| Fuente | Peso / estilo | Rol | Origen | Código / comando |
|---|---|---|---|---|
| Bebas Neue | 400 | Títulos display (mega headlines) | GitHub google/fonts `ofl/bebasneue/` | `@font-face` embebido vía `stlabs_kit.embedded_fonts_css()` |
| Poppins | 700 / 800 | CTA pill | GitHub google/fonts `ofl/poppins/` | idem |
| Barlow Condensed | 400–700 | Cuerpo, subtítulos | GitHub google/fonts `ofl/barlowcondensed/` | idem |
| IBM Plex Mono | 400–600 | Badges, footer `sebastian.stlabs.ar` | apt / repo `fonts/` | idem |
| Lora | 400–700 itálica | Palabras acento (`OPERATIVO`) | GitHub google/fonts `ofl/lora/` | idem |

Instalación local (si hace falta regenerar):

```bash
python .claude/skills/carrusel-stlabs/assets/install_fonts.py
```
