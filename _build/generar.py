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


def generar(codigo):
    m = cargar(codigo)
    html = open(PLANTILLA, encoding="utf-8").read()
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
            faltan.append(viejo[:90])
            continue
        html = html.replace(viejo, nuevo)
    if faltan:
        raise SystemExit("[error] textos de la plantilla no encontrados:\n  - " + "\n  - ".join(faltan))
    restos = []
    permitido = getattr(m, "PERMITIDO", []) + permitido_extra
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
