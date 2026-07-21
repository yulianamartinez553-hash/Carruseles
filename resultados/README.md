# resultados/

Carpeta única donde viven **todos los carruseles** de Sebastián García (STLabs), en la rama `main`.

## Convención

- **No se abre una rama por carrusel.** Cada carrusel es una subcarpeta de `resultados/`.
- Las carpetas se numeran de forma **secuencial**: `carrusel-1`, `carrusel-2`, `carrusel-3`, …
- El número lo asigna automáticamente `package()` (id por defecto `carrusel-N`, calculado mirando esta carpeta). Para fijar un número/nombre concreto, pasar `meta["id"]`.

## Contenido de cada carpeta

Cada `carrusel-N/` contiene la entrega generada por `stlabs_kit.package(...)`:

- `slide-01.png`, `slide-02.png`, … — slides retina (2160×2700), versionados en `main`.
- `<nombre>.html` — HTML standalone con fuentes embebidas (editable).
- `_preview-tira.png` — tira de preview.
- `manifest.json` — metadata del carrusel (título, fondo, familia, origen, feedback, etc.).
- `<nombre>.zip` — paquete comprimido (ignorado por `.gitignore`; no se versiona).

## `_legacy/`

Builds antiguos que no siguen la numeración `carrusel-N` (coberturas, borradores previos a esta convención). Se conservan como archivo histórico.
