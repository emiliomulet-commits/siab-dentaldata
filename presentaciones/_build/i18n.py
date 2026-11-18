"""Extracción y sustitución de textos de las piezas para versiones por mercado.
Segmentos: TITULO, CHIP, DESC, FUENTES, textos entre etiquetas y atributos traducibles de ESCENAS."""
import re, html
ATTRS = ("data-w", "data-to", "data-suf", "data-pre", "data-mil", "alt", "aria-label", "data-nombre")
TAG = re.compile(r"(<[^>]+>)")
AT = re.compile(r'\b(' + "|".join(ATTRS) + r')="([^"]*)"')
def _partes(h):
    for p in TAG.split(h):
        yield p
def extraer(m):
    seg = [("TITULO", m.TITULO), ("CHIP", m.CHIP), ("DESC", m.DESC), ("FUENTES", m.FUENTES)]
    for i, h in enumerate(m.ESCENAS):
        for p in _partes(h):
            if p.startswith("<"):
                for a, v in AT.findall(p):
                    if v.strip() and a != "alt": seg.append((f"e{i+1}@{a}", v))
            elif p.strip():
                seg.append((f"e{i+1}", p.strip()))
    return seg
def aplicar(m, trad):
    """trad: lista de textos en el mismo orden que extraer(m). Devuelve dict con TITULO, CHIP, DESC, FUENTES, ESCENAS."""
    orig = extraer(m)
    if len(trad) != len(orig): raise SystemExit(f"{m.__name__}: {len(trad)} textos, se esperaban {len(orig)}")
    it = iter(trad[4:])
    out = []
    for h in m.ESCENAS:
        res = []
        for p in _partes(h):
            if p.startswith("<"):
                def r(mm):
                    a, v = mm.group(1), mm.group(2)
                    if v.strip() and a != "alt": return f'{a}="{next(it)}"'
                    return mm.group(0)
                res.append(AT.sub(r, p))
            elif p.strip():
                lead = p[:len(p) - len(p.lstrip())]; tail = p[len(p.rstrip()):]
                res.append(lead + next(it) + tail)
            else: res.append(p)
        out.append("".join(res))
    return {"TITULO": trad[0], "CHIP": trad[1], "DESC": trad[2], "FUENTES": trad[3], "ESCENAS": out}
