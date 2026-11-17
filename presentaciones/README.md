# Presentaciones animadas de Dental Data

Diez presentaciones (P01–P10) en español, una por pregunta clave. Guiones: doc «Dental Data · Guiones de las 10 presentaciones animadas» (Claude Docs).
Publicadas el 17/11/2026 y enlazadas en /es/ desde el mismo día: videoteca (#videos) con filtros por perfil, botones en cada sección y botón «Ver animación» en el asistente. Índice interno: `/presentaciones/` (noindex).

## Modos de cada `pNN/`
- `pNN/`: presentación para reuniones (→ o espacio avanza, ← retrocede, 1–9 salta, F pantalla completa, H oculta los controles).
- `?modo=web`: arranca sola y en silencio, con botón «Activar locución». Con `&embed=1`, controles compactos (visor del asistente).
- `?modo=video`: con locución.
- `dentaldata-pNN.mp4`: vídeo 1920×1080 con locución.

## Cómo se generan
- Motor común: `assets/dd-motor.js` y `assets/dd-motor.css` (GSAP, iconos propios, fuentes Montserrat y Hanken Grotesk alojadas aquí).
- Contenido de cada pieza: `_build/piezas/pNN.py`. Página: `python3 _build/construir.py [pNN…]`. No editar a mano los `pNN/index.html`.
- Locución: ElevenLabs, voz «Salva – The Spanish Narrator», Eleven v4 (estabilidad 50, similitud 75), con 3 s de silencio al principio para la apertura y volumen normalizado a −16 LUFS.
- Sincronía: Whisper (faster-whisper, modelo small) da el tiempo de cada palabra. `_build/tiempos.py` fija la duración de cada escena a partir de frases ancla, y `construir.py` convierte `data-w="palabras"` en el momento exacto en que aparece cada elemento.
- MP4: captura fotograma a fotograma (25 fps) con Playwright y ffmpeg (H.264, CRF 20).
- Si se cambia un texto de la locución hay que volver a grabarla, transcribirla, ejecutar `tiempos.py` y `construir.py`, y renderizar el MP4.

## En la web (/es/)
- `assets/dd-videos.js` y `assets/dd-videos.css`: videoteca, reproductor (MP4 con subtítulos, capítulos, siguiente vídeo y llamada a la acción) y botón del asistente (`window.DDV`).
- `videos.json`: catálogo que genera `_build/extras.py`, junto con `pNN/poster.jpg` y `pNN/subtitulos-es.vtt` (texto del guion alineado con los tiempos de Whisper).
- En `es/index.html` todo lo de los vídeos va entre `<!--dd-videos-->` y `<!--/dd-videos-->`. El generador de mercados (`/_build/generar.py`) quita esos bloques hasta que haya versiones traducidas.
