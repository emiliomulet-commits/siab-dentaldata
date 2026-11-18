#!/usr/bin/env python3
"""Generador de las páginas de Dental Data por mercado.

La plantilla es la página española (es/index.html): diseño, estilos, asistente y
estructura se mantienen en un solo sitio. Cada mercado tiene un archivo en
_build/mercados/<codigo>.py con:

  SALIDA      ruta de la página generada (p. ej. "en/index.html")
  LANG        atributo lang del <html>
  BLOQUES     {id_de_sección: html}  secciones que se sustituyen enteras (lo local)
  KB_JS       el array de respuestas preparadas del asistente en ese idioma
  JSONLD      datos estructurados (schema.org) de la página
  REEMPLAZOS  lista de (texto_de_la_plantilla, texto_del_mercado) propios del mercado
  IDIOMA_COMUN  (opcional) código de _build/idiomas/<código>.py con los textos comunes del idioma
                (solución, tecnología, asistente, pie). {SIAB} se sustituye por SIAB, la ruta del
                idioma en softwareinabox.eu (nl, nl-be, fr, fr-be, de…)

Comprobaciones (el script falla si alguna no se cumple):
  - cada texto a reemplazar existe en la plantilla;
  - no queda texto visible ni cadenas del asistente en el idioma de la plantilla
    (lista de marcas de español), salvo las permitidas en PERMITIDO.

Uso:  python3 _build/generar.py en        (o: todos)
"""
import importlib.util, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTILLA = os.path.join(RAIZ, "es", "index.html")
MARCAS_ES = [r"\bclínicas?\b", r"\bnuestr[oa]s?\b", r"\bpara\b", r"\bdatos\b", r"\bdel\b", r"\bcon\b", r"\blos\b",
             r"\blas\b", r"\bque\b", r"\bpiloto\b", r"\baseguradoras?\b", r"\bpregunta", r"\brespuesta", r"¿", r"¡",
             r"\bespacio\b", r"\bsalud\b", r"\bunete\b", r"\bÚnete\b", r"\bEspaña\b", r"\bdescubre\b", r"\bmercado\b"]


def cargar(codigo):
    ruta = os.path.join(RAIZ, "_build", "mercados", codigo + ".py")
    spec = importlib.util.spec_from_file_location("m_" + codigo, ruta)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def comprobar_js(html, nombre):
    """Comprueba con node la sintaxis de los <script> en línea (salvo JSON-LD), si node está instalado."""
    import shutil, subprocess, tempfile
    if not shutil.which("node"):
        return
    for i, js in enumerate(re.findall(r"<script(?![^>]*application/ld\+json)(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html, flags=re.S)):
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
            f.write(js)
        r = subprocess.run(["node", "--check", f.name], capture_output=True, text=True)
        os.unlink(f.name)
        if r.returncode:
            raise SystemExit(f"[error] JavaScript no válido en {nombre} (script {i}):\n" + r.stderr[-600:])


def cargar_idioma(codigo):
    ruta = os.path.join(RAIZ, "_build", "idiomas", codigo + ".py")
    spec = importlib.util.spec_from_file_location("i_" + codigo.strip("_"), ruta)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def reemplazar_seccion(html, ident, nuevo):
    patron = re.compile(r'<section[^>]*\bid="%s"[^>]*>.*?</section>' % re.escape(ident), re.S)
    if not patron.search(html):
        raise SystemExit(f"[error] no encuentro la sección id=\"{ident}\" en la plantilla")
    return patron.sub(lambda _: nuevo.strip(), html, count=1)


def texto_visible(html):
    h = re.sub(r"<script[^>]*>.*?</script>|<style[^>]*>.*?</style>", " ", html, flags=re.S)
    h = re.sub(r'<[^>]*\blang="es"[^>]*>.*?</[a-z]+>', " ", h, flags=re.S)  # enlaces marcados como español
    h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", h)


def atributos(html):
    """Textos que no se ven en la página pero sí leen buscadores y lectores de pantalla."""
    vals = re.findall(r'\b(?:content|alt|aria-label|placeholder|title|value)="([^"]{4,})"', html)
    vals += re.findall(r"<title>(.*?)</title>", html, flags=re.S)
    vals = [v for v in vals if not v.startswith(("http", "/", "#", "width=", "text/", "summary"))]
    return " | ".join(vals)


def cadenas_js(html):
    """Cadenas de texto del código del asistente (sin comentarios ni nombres de variables)."""
    js = " ".join(re.findall(r"<script(?![^>]*ld\+json)[^>]*>(.*?)</script>", html, flags=re.S))
    js = re.sub(r"(?m)^\s*//.*$", " ", js)                     # comentarios de línea
    cads = re.findall(r"'((?:[^'\\\n]|\\.){6,})'", js)
    cads = [c for c in cads if " " in c and not re.search(r"[;{}=]\s*(function|var|if|return)\b|\)\s*\{", c)]
    texto = " | ".join(cads)
    texto = re.sub(r"https?://[^\s\"'<>]+", " ", texto)      # las URL no son texto
    return re.sub(r"\b[\w.-]+\.(?:eu|com|es|nl)\b", " ", texto)  # ni los dominios


def reemplazar_saltando_videos(html, viejo, nuevo):
    """Reemplaza viejo (escrito sobre la plantilla sin bloques de vídeo) aunque en html haya bloques
    <!--dd-videos--> intercalados; los bloques que caen dentro del tramo reemplazado se pierden."""
    mapa, limpio, i = [], [], 0
    for mm in re.finditer(r"<!--dd-videos-->.*?<!--/dd-videos-->\n?", html, flags=re.S):
        for k in range(i, mm.start()):
            mapa.append(k)
        limpio.append(html[i:mm.start()]); i = mm.end()
    for k in range(i, len(html)):
        mapa.append(k)
    limpio.append(html[i:]); limpio = "".join(limpio)
    out, pos, hecho = [], 0, False
    for mm in re.finditer(re.escape(viejo), limpio):
        a, b = mapa[mm.start()], mapa[mm.end() - 1] + 1
        out.append(html[pos:a]); out.append(nuevo); pos = b; hecho = True
    if not hecho:
        return None
    out.append(html[pos:])
    return "".join(out)


def noeud_fr():
    """Francia: «Où s'installe le nœud ?» · dos opciones de alojamiento del nodo (plan A4.6)."""
    col = ('<div style="flex:1 1 320px;background:#0B2545;border:1px solid #1E3A5F;border-radius:14px;padding:24px 26px">'
           '<div style="font:700 12px/1.2 Montserrat,sans-serif;letter-spacing:.12em;color:#EDBC6C;text-transform:uppercase">{0}</div>'
           '<h3 style="color:#fff;font-size:20px;margin:10px 0 8px">{1}</h3><p style="color:#C3CFDC;font-size:15.5px;margin:0 0 12px">{2}</p>'
           '<ul style="color:#C3CFDC;font-size:15px;margin:0;padding-left:18px">{3}</ul></div>')
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    a = col.format("Option 1 · Microsoft Azure", "Nœud sur Azure, région Union européenne",
                   "La même architecture que dans les autres pays : les services Azure présentés dans l&#x27;animation, avec les données hébergées dans l&#x27;Union européenne.",
                   li(["Identité Microsoft Entra et calcul confidentiel pour l&#x27;IA", "Déploiement le plus rapide, catalogue de services complet", "Certification HDS d&#x27;Azure, à confirmer pour chaque service utilisé"]))
    b = col.format("Option 2 · Hébergeur souverain", "Nœud chez un hébergeur qualifié SecNumCloud et certifié HDS",
                   "Pour les établissements qui exigent un hébergement souverain : le nœud est installé chez un hébergeur français qualifié par l&#x27;ANSSI et certifié pour les données de santé.",
                   li(["Données et opérations soumises au seul droit de l&#x27;Union", "Mêmes fonctions de connecteur et de catalogue", "Le choix de l&#x27;hébergeur revient à chaque participant"]))
    return ('<div class="wrap" style="padding:8px 28px 56px"><div style="max-width:760px;margin-bottom:22px">'
            '<div class="eyebrow">Où s&#x27;installe le nœud ?</div>'
            '<h2 style="color:#fff;margin:8px 0 10px">Deux options d&#x27;hébergement, les mêmes standards aux frontières</h2>'
            '<p style="color:#C3CFDC;margin:0">Les données cliniques ne quittent jamais le cabinet ou le centre : seuls circulent des questions et des résultats agrégés. '
            'Chaque participant choisit où s&#x27;installe son nœud ; le connecteur Eclipse EDC, le catalogue HealthDCAT-AP, les règles ODRL et les identifiants Gaia-X restent identiques.</p></div>'
            f'<div style="display:flex;flex-wrap:wrap;gap:20px">{a}{b}</div></div>\n')

def videos_mercado(html, pmk, vl):
    """Traduce los bloques <!--dd-videos--> de la plantilla a la versión de presentaciones del mercado pmk."""
    import json, html as H
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from videos_i18n import L
    t = L[vl]
    vids = {v["id"]: v for v in json.load(open(os.path.join(RAIZ, "presentaciones", pmk, "videos.json"), encoding="utf-8"))}
    base = f"/presentaciones/{pmk}/"
    play = '<span class="pl"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4v16l13-8z"/></svg></span>'
    e = lambda x: H.escape(x, quote=True)
    def dur(pid): return f'{round(float(vids[pid]["duracion"]))} s'
    def boton(pid, etiqueta=None):
        v = vids[pid]
        return (f'<button type="button" class="dd-vbtn" data-pres="{pid}" aria-label="{e(t["ver"] + " " + v["titulo"])}">{play}'
                f'<span>{e(etiqueta or v["chip"])} <small data-dur>{dur(pid)}</small></span></button>')
    def botones(txt):
        return re.sub(r'<button type="button" class="dd-vbtn" data-pres="(p\d\d)".*?</button>', lambda x: boton(x.group(1)), txt, flags=re.S)
    def bloque(mm):
        b = mm.group(1)
        if "dd-videos.css" in b:
            out = b
        elif b.startswith('<li><a href="#videos">'):
            out = (f'<li><a href="#videos">{e(t["menu"][0])}<small>{e(t["menu"][1])}</small></a></li>'
                   f'<li><a href="#arquitectura-azure">{e(t["menu"][2])}<small>{e(t["menu"][3])}</small></a></li>')
        elif b.strip() == '<a href="#videos">Presentaciones animadas</a>':
            out = f'<a href="#videos">{e(t["menu"][0])}</a>'
        elif "dd-hero-v" in b:
            out = f' <div class="dd-hero-v">{boton("p01")}<a href="#videos">{e(t["hero"])}</a></div>'
        elif 'id="videos"' in b:
            s = t["sec"]
            out = (f'<section class="s dd-vt" id="videos"><div class="wrap">\n <div class="head"><div class="eyebrow">{e(s[0])}</div>'
                   f'<h2>{e(s[1])}</h2><p>{e(s[2])}</p></div>\n <div id="dd-videoteca"></div>\n'
                   f' <noscript><p><a href="{base}p01/">{e(s[3])}</a></p></noscript>\n</div></section>\n')
        elif 'id="arquitectura-azure"' in b:
            a, v = t["arq"], vids["p11"]
            out = (f'<section class="dd-arq" id="arquitectura-azure" aria-labelledby="dd-arq-t">\n'
                   f' <div class="wrap dd-arq-cab"><div class="eyebrow">{e(a[0])}</div><h2 id="dd-arq-t">{e(v["titulo"])}</h2><p>{e(a[1])}</p></div>\n'
                   f' <div class="dd-arq-v"><iframe src="{base}p11/?modo=web&amp;sonido=1" title="{e(t["T"]["iframe"] + ": " + v["titulo"])}" loading="lazy" allow="autoplay; fullscreen" allowfullscreen></iframe></div>\n'
                   f' <div class="wrap dd-arq-pie">{boton("p11", t["locucion"])}<a href="{base}p11/?modo=video" target="_blank" rel="noopener">{e(t["completa"])}</a>'
                   f'<small>{e(a[2])}</small></div>\n{noeud_fr() if pmk == "fr" else ""}</section>')
        elif "dd-videos-ld" in b:
            dom = "https://dentaldata.softwareinabox.eu"
            items = []
            for i, (pid, v) in enumerate(sorted(vids.items()), 1):
                items.append({"@type": "ListItem", "position": i, "item": {"@type": "VideoObject", "name": v["titulo"],
                    "description": v["transcripcion"][:300], "inLanguage": vl, "thumbnailUrl": dom + v["poster"],
                    "embedUrl": dom + base + pid + "/", "uploadDate": "2026-11-18", "duration": f"PT{round(float(v['duracion']))}S",
                    "transcript": v["transcripcion"]}})
            ld = json.dumps({"@context": "https://schema.org", "@type": "ItemList", "name": t["lista"], "itemListElement": items}, ensure_ascii=False)
            cfg = json.dumps({"base": base, "t": t["T"], "pub": t["PUB"], "cta": t["CTA"]}, ensure_ascii=False)
            out = (f'<script type="application/ld+json" id="dd-videos-ld">\n{ld}\n</script>\n'
                   f'<script>window.DD_VIDEOS={cfg};</script>\n<script src="/presentaciones/assets/dd-videos.js" defer></script>')
        elif "dd-vbtn" in b:
            out = botones(b)
        elif b.strip().startswith('<a href="#videos"'):
            out = f'<a href="#videos">{e(t["menu"][0])}</a>'
        else:
            raise SystemExit("[error] bloque de vídeo no reconocido: " + b[:120])
        return "<!--dd-videos-->" + out + "<!--/dd-videos-->"
    return re.sub(r"<!--dd-videos-->(.*?)<!--/dd-videos-->", bloque, html, flags=re.S)


def generar(codigo):
    m = cargar(codigo)
    html = open(PLANTILLA, encoding="utf-8").read()
    # Presentaciones animadas: si el mercado tiene versión propia (presentaciones/<PRES>/videos.json), los bloques se
    # traducen y apuntan a ella; si no, se quitan.
    pres = getattr(m, "PRES", None)
    vjson = os.path.join(RAIZ, "presentaciones", pres or "-", "videos.json")
    if pres and os.path.exists(vjson):
        html = videos_mercado(html, pres, m.VIDEOS_LANG)
    else:
        html = re.sub(r"<!--dd-videos-->.*?<!--/dd-videos-->\n?", "", html, flags=re.S)
    html = html.replace('<html lang="es">', f'<html lang="{m.LANG}">', 1)
    for ident, nuevo in getattr(m, "BLOQUES", {}).items():
        html = reemplazar_seccion(html, ident, nuevo)
    if getattr(m, "JSONLD", None):
        html = re.sub(r'(<script type="application/ld\+json">).*?(</script>)', lambda x: x.group(1) + "\n" + m.JSONLD.strip() + "\n" + x.group(2), html, count=1, flags=re.S)
    if getattr(m, "KB_JS", None):
        a, b = html.index("var KB=["), html.index("var byId={}")
        html = html[:a] + "var KB=" + m.KB_JS.strip() + ";\n" + html[b:]
    reemplazos = list(m.REEMPLAZOS)
    if getattr(m, "IDIOMA_COMUN", None):            # textos comunes del idioma, después de los del mercado
        c = cargar_idioma(m.IDIOMA_COMUN)
        base = cargar_idioma("_base").CLAVES
        siab = getattr(m, "SIAB", m.IDIOMA_COMUN)
        propios = {v for v, _ in m.REEMPLAZOS}
        for clave, viejo in base.items():
            if viejo in propios:                       # el mercado ya lo adapta
                continue
            if clave not in c.TEXTOS:
                sys.exit(f"[error] falta la clave {clave} en _build/idiomas/{m.IDIOMA_COMUN}.py")
            reemplazos.append((viejo, c.TEXTOS[clave].replace("{SIAB}", siab)))
        permitido_extra = getattr(c, "PERMITIDO", [])
        marcas_propias = getattr(c, "MARCAS_PROPIAS", [])     # palabras que también existen en ese idioma
    else:
        permitido_extra, marcas_propias = [], []
    faltan = []
    for viejo, nuevo in reemplazos:
        if viejo not in html:
            html2 = reemplazar_saltando_videos(html, viejo, nuevo)
            if html2 is None:
                faltan.append(viejo[:90])
            else:
                html = html2
            continue
        html = html.replace(viejo, nuevo)
    if faltan:
        raise SystemExit("[error] textos de la plantilla no encontrados:\n  - " + "\n  - ".join(faltan))
    restos = []
    permitido = getattr(m, "PERMITIDO", []) + permitido_extra + ['["aseguradoras"', '["clinicas"']
    for fuente, texto in (("visible", texto_visible(html)), ("asistente", cadenas_js(html)), ("atributos", atributos(html))):
        for marca in MARCAS_ES:
            if marca in marcas_propias:
                continue
            for x in re.finditer(marca, texto, flags=re.I):
                trozo = texto[max(0, x.start() - 50): x.end() + 50]
                if not any(p in trozo for p in permitido):
                    restos.append(f"{fuente}: …{trozo.strip()}…")
    if restos:
        raise SystemExit(f"[error] quedan {len(restos)} textos en español en {m.SALIDA}:\n  - " + "\n  - ".join(sorted(set(restos))[:40]))
    comprobar_js(html, m.SALIDA)
    salida = os.path.join(RAIZ, m.SALIDA)
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    open(salida, "w", encoding="utf-8").write(html)
    print(f"[ok] {m.SALIDA} ({len(html):,} bytes)")


if __name__ == "__main__":
    codigos = sys.argv[1:] or ["todos"]
    if codigos == ["todos"]:
        codigos = sorted(f[:-3] for f in os.listdir(os.path.join(RAIZ, "_build", "mercados")) if f.endswith(".py") and not f.startswith("_"))
    for c in codigos:
        generar(c)
