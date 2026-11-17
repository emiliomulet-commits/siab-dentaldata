#!/usr/bin/env python3
"""Genera presentaciones/pNN/index.html a partir de las fichas de piezas/pNN.py.

Cada ficha define: ID, TITULO (pregunta), CHIP (versión corta), FUENTES, ESCENAS (HTML de cada <section>).
Uso: python3 _build/construir.py [p01 p02 …]   (sin argumentos, todas)
"""
import importlib.util, os, sys, html, json, re, unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "piezas"))
RAIZ = os.path.dirname(AQUI)  # presentaciones/

PLANTILLA = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="index,follow">
<title>{id_up} · {titulo_txt} · Dental Data</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/assets/brand/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../assets/dd-motor.css">
</head>
<body class="al-inicio">
<div id="marco"><div id="stage" role="img" aria-label="{titulo_txt}">
<img id="marca" src="/assets/brand/dentaldata-logo-horizontal-white.svg" alt="Dental Data" width="220" height="40">
<div id="chip"><b>{id_up}</b><span>{chip}</span></div>
{escenas}
<div id="pie"><span>{fuentes}</span><span>Dental Data · Software in a Box</span></div>
</div></div>
<div class="nota-rm">Movimiento reducido: se muestra cada escena completa.</div>
<div id="inicio"><span>Pulse → o la barra espaciadora para empezar</span></div>
{audio}<button id="voz-btn" hidden>🔊 Activar locución</button>
<nav class="ui" aria-label="Controles de la presentación">
<button id="ant" title="Escena anterior (←)" aria-label="Escena anterior"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7z"/></svg></button>
<button title="Reproducir o pausar" aria-label="Reproducir o pausar"><svg viewBox="0 0 24 24" id="pp"><path d="M8 5v14l11-7z"/></svg></button>
<button id="sig" title="Escena siguiente (→)" aria-label="Escena siguiente"><svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7z"/></svg></button>
<div class="escenas" id="escenas"></div>
<span class="pista">← → espacio · 1–{n} · F · H oculta</span>
<button id="pc" title="Pantalla completa (F)" aria-label="Pantalla completa"><svg viewBox="0 0 24 24"><path d="M4 4h6v2H6v4H4zM14 4h6v6h-2V6h-4zM4 14h2v4h4v2H4zM18 14h2v6h-6v-2h4z"/></svg></button>
</nav>
<script src="../assets/gsap.min.js"></script>
<script src="../assets/dd-motor.js"></script>
</body>
</html>
"""

def _norm(w): return re.sub(r"[^a-z0-9ñ]", "", unicodedata.normalize("NFKD", w.lower()).encode("ascii", "ignore").decode())

def sincronizar(h, i, T):
    """Ajusta data-dur a la locución y convierte data-w="palabras" en data-t (segundos desde el inicio de la escena)."""
    ini = T["inicios"][i]; fin = ini + T["dur"][i]
    h = re.sub(r'data-dur="[0-9.]+"', f'data-dur="{T["dur"][i]}"', h, count=1)
    pal = [(t, w) for t, w in T["palabras"] if ini - .5 <= t < fin]
    def rep(m):
        toks = [_norm(x) for x in m.group(1).split()]
        for k in range(len(pal)):
            if [w for _, w in pal[k:k+len(toks)]] == toks:
                return f'data-t="{max(0, pal[k][0] - ini - .45):.2f}"'
        print("  aviso: sin sincronizar", m.group(1)); return 'data-t="0"'
    # data-w sustituye al data-t que lleve el mismo elemento
    h = re.sub(r'data-t="[0-9.]+"(\s+data-w=")', r'\1', h)
    return re.sub(r'data-w="([^"]+)"', rep, h)

def cargar(pid):
    ruta = os.path.join(AQUI, "piezas", f"{pid}.py")
    spec = importlib.util.spec_from_file_location(pid, ruta)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def construir(pid, lang="es"):
    m = cargar(pid)
    carpeta = os.path.join(RAIZ, pid)
    os.makedirs(carpeta, exist_ok=True)
    voz = f"voz-{pid}.mp3"
    audio = f'<audio id="voz" src="{voz}" preload="auto"></audio>\n' if os.path.exists(os.path.join(carpeta, voz)) else ""
    escenas = list(m.ESCENAS)
    T = json.load(open(os.path.join(AQUI, "tiempos.json"))).get(pid) if os.path.exists(os.path.join(AQUI, "tiempos.json")) else None
    if T and audio:
        escenas = [sincronizar(h, i, T) for i, h in enumerate(escenas)]
    escenas = "\n".join(escenas)
    out = PLANTILLA.format(lang=lang, id_up=pid.upper(), titulo_txt=html.escape(m.TITULO), desc=html.escape(m.DESC),
                           chip=m.CHIP, fuentes=m.FUENTES, escenas=escenas, audio=audio, n=len(m.ESCENAS))
    open(os.path.join(carpeta, "index.html"), "w", encoding="utf-8").write(out)
    print("ok", pid, len(m.ESCENAS), "escenas")

if __name__ == "__main__":
    ids = sys.argv[1:] or sorted(f[:-3] for f in os.listdir(os.path.join(AQUI, "piezas")) if f.startswith("p") and f.endswith(".py"))
    for pid in ids: construir(pid)
