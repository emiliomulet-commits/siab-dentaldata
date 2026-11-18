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
<link rel="stylesheet" href="{A}assets/dd-motor.css">
</head>
<body class="al-inicio">
<div id="marco"><div id="stage" role="img" aria-label="{titulo_txt}">
<img id="marca" src="/assets/brand/dentaldata-logo-horizontal-white.svg" alt="Dental Data" width="220" height="40">
<div id="chip"><b>{id_up}</b><span>{chip}</span></div>
{escenas}
<div id="pie"><span>{fuentes}</span><span>Dental Data · Software in a Box</span></div>
</div></div>
<div class="nota-rm">{u_rm}</div>
<div id="inicio"><span>{u_ini}</span></div>
{audio}<button id="voz-btn" hidden>{u_loc}</button>
<nav class="ui" aria-label="{u_ctl}">
<button id="ant" title="{u_ant} (←)" aria-label="{u_ant}"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7z"/></svg></button>
<button title="{u_pp}" aria-label="{u_pp}"><svg viewBox="0 0 24 24" id="pp"><path d="M8 5v14l11-7z"/></svg></button>
<button id="sig" title="{u_sig} (→)" aria-label="{u_sig}"><svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7z"/></svg></button>
<div class="escenas" id="escenas"></div>
<span class="pista">{u_pista}</span>
<button id="pc" title="{u_pc} (F)" aria-label="{u_pc}"><svg viewBox="0 0 24 24"><path d="M4 4h6v2H6v4H4zM14 4h6v6h-2V6h-4zM4 14h2v4h4v2H4zM18 14h2v6h-6v-2h4z"/></svg></button>
</nav>
{uijs}<script src="{A}assets/gsap.min.js"></script>
<script src="{A}assets/dd-motor.js"></script>
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

def UI_ES(n):
    return dict(u_rm="Movimiento reducido: se muestra cada escena completa.", u_ini="Pulse → o la barra espaciadora para empezar",
                u_loc="🔊 Activar locución", u_ctl="Controles de la presentación", u_ant="Escena anterior", u_pp="Reproducir o pausar",
                u_sig="Escena siguiente", u_pista=f"← → espacio · 1–{n} · F · H oculta", u_pc="Pantalla completa")

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
                           chip=m.CHIP, fuentes=m.FUENTES, escenas=escenas, audio=audio, n=len(m.ESCENAS), A="../", uijs="", **UI_ES(len(m.ESCENAS)))
    open(os.path.join(carpeta, "index.html"), "w", encoding="utf-8").write(out)
    print("ok", pid, len(m.ESCENAS), "escenas")



# ---------------------------------------------------------------- versiones por mercado
# python3 _build/construir.py --mercado nl [p01 …]
# Textos: _build/mercados/<mercado>.json  {"lang", "base" (mercado del que hereda piezas), "ui", "piezas": {pNN: {"seg", "loc", "anclas"}}}
# Salida: presentaciones/<mercado>/pNN/index.html ; voz: presentaciones/<mercado>/pNN/voz-pNN.mp3 ; tiempos: _build/tiempos-<mercado>.json
import i18n

def conf_mercado(mk):
    c = json.load(open(os.path.join(AQUI, "mercados", mk + ".json"), encoding="utf-8"))
    piezas = dict(c.get("piezas", {}))
    base = c.get("base")
    while base:
        b = json.load(open(os.path.join(AQUI, "mercados", base + ".json"), encoding="utf-8"))
        for k, v in b.get("piezas", {}).items(): piezas.setdefault(k, v)
        for k, v in b.get("ui", {}).items(): c.setdefault("ui", {}).setdefault(k, v)
        base = b.get("base")
    c["piezas"] = piezas
    return c

def sincronizar_m(h, i, T):
    ini = T["inicios"][i]; fin = ini + T["dur"][i]
    h = re.sub(r'data-dur="[0-9.]+"', f'data-dur="{T["dur"][i]}"', h, count=1)
    pal = [(t, w) for t, w in T["palabras"] if ini - .5 <= t < fin]
    def rep(m):
        toks = [_norm(x) for x in m.group(1).split()]
        for k in range(len(pal)):
            if [w for _, w in pal[k:k+len(toks)]] == toks:
                return f'data-t="{max(0, pal[k][0] - ini - .45):.2f}"'
        print("  aviso: sin sincronizar", m.group(1)); return 'data-t="1.5"'
    h = re.sub(r'data-t="[0-9.]+"(\s+data-w=")', r'\1', h)
    return re.sub(r'data-w="([^"]+)"', rep, h)

def construir_mercado(mk, pid, c=None):
    c = c or conf_mercado(mk)
    m = cargar(pid)
    p = c["piezas"][pid]
    d = i18n.aplicar(m, p["seg"])
    carpeta = os.path.join(RAIZ, mk, pid); os.makedirs(carpeta, exist_ok=True)
    voz = f"voz-{pid}.mp3"
    audio = f'<audio id="voz" src="{voz}" preload="auto"></audio>\n' if os.path.exists(os.path.join(carpeta, voz)) else ""
    escenas = list(d["ESCENAS"])
    tp = os.path.join(AQUI, f"tiempos-{mk}.json")
    T = json.load(open(tp)).get(pid) if os.path.exists(tp) else None
    if T and audio:
        escenas = [sincronizar_m(h, i, T) for i, h in enumerate(escenas)]
    else:  # sin locución: los data-w se convierten en un retraso fijo
        escenas = [re.sub(r'data-w="[^"]+"', 'data-t="1.5"', re.sub(r'data-t="[0-9.]+"(\s+data-w=")', r'\1', h)) for h in escenas]
    u = c["ui"]; n = len(escenas)
    ui = dict(u_rm=u["rm"], u_ini=u["ini"], u_loc=u["locucion"], u_ctl=u["ctl"], u_ant=u["ant"], u_pp=u["pp"], u_sig=u["sig"],
              u_pista=u["pista"].replace("{n}", str(n)), u_pc=u["pc"])
    uijs = "<script>window.DD_UI=" + json.dumps({k: u[k] for k in ("escena", "quitar", "activar", "locucion", "ver") if k in u}, ensure_ascii=False) + "</script>\n"
    out = PLANTILLA.format(lang=c["lang"], id_up=pid.upper(), titulo_txt=html.escape(d["TITULO"]), desc=html.escape(d["DESC"]),
                           chip=d["CHIP"], fuentes=d["FUENTES"], escenas="\n".join(escenas), audio=audio, n=n, A="../../", uijs=uijs, **ui)
    open(os.path.join(carpeta, "index.html"), "w", encoding="utf-8").write(out)
    print("ok", mk, pid, n, "escenas", "con voz" if audio else "sin voz")

if __name__ == "__main__":
    args = sys.argv[1:]
    todas = sorted(f[:-3] for f in os.listdir(os.path.join(AQUI, "piezas")) if f.startswith("p") and f.endswith(".py"))
    if args[:1] == ["--mercado"]:
        mk = args[1]; c = conf_mercado(mk)
        for pid in (args[2:] or todas): construir_mercado(mk, pid, c)
    else:
        for pid in (args or todas): construir(pid)
