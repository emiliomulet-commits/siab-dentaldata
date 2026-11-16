# Generador de páginas de Dental Data

La página española (`es/index.html`) es la **plantilla**: diseño, estilos, asistente y estructura viven ahí.
Cada mercado tiene un archivo en `_build/mercados/<código>.py` con sus textos (común traducido) y sus secciones propias (mercado, para quién, contacto).

```
python3 _build/generar.py en      # una página
python3 _build/generar.py         # todas
```

El script **falla** si un texto de la plantilla ya no existe (hay que actualizar el archivo del mercado) o si queda texto en español en la página generada (visible, en el asistente o en atributos como la descripción).

Regla: **no editar a mano las páginas generadas** (`en/index.html`…). Se cambia la plantilla o el archivo del mercado y se vuelve a generar. La página neerlandesa (`nl/`) todavía es manual; pasará al generador cuando se rehaga con la estructura común.

Mercados previstos (análisis «Dental Data por países e idiomas», 16/11/2026): es, nl, be/nl, be/fr, de, dk, fr, it, pt, en.
La carpeta `_build/` no se publica (GitHub Pages ignora las carpetas que empiezan por «_»).
