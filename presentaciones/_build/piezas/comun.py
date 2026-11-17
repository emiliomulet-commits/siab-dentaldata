"""Piezas reutilizables para las escenas (coordenadas en px dentro de un .lienzo.fijo de 1408×520)."""
def at(t): return f' data-t="{t}"' if t is not None else ''
def nodo(x, y, icono, texto, sub="", disco="", a="pop", t=0, ancho=200):
    s = f'<small>{sub}</small>' if sub else ''
    return (f'<div class="nodo" style="left:{x}px;top:{y}px;width:{ancho}px" data-a="{a}"{at(t)}>'
            f'<div class="disco {disco}"><i data-i="{icono}" class="{"blanco" if disco=="osc" else ""}"></i></div>{texto}{s}</div>')
def lineas(*segs):
    """segs: (x1,y1,x2,y2,clase,t)"""
    out = ['<svg class="lineas" viewBox="0 0 1408 520">']
    for x1,y1,x2,y2,c,t in segs:
        out.append(f'<path d="M{x1} {y1} L{x2} {y2}" class="{c}" data-a="draw"{at(t)}/>')
    out.append('</svg>')
    return ''.join(out)
def paquete(x, y, dx, dy, t, d=1.1, c="", fin=""):
    f = f' data-fin="{fin}"' if fin else ''
    return f'<div class="paquete {c}" style="left:{x}px;top:{y}px" data-a="mover" data-dx="{dx}" data-dy="{dy}" data-d="{d}"{at(t)}{f}></div>'
def etq(x, y, texto, c="", t=0, a="fade"):
    return f'<div class="etq {c}" style="left:{x}px;top:{y}px" data-a="{a}"{at(t)}>{texto}</div>'
def apertura(n, pregunta_html):
    return f'''<section class="esc centro" data-nombre="Apertura" data-dur="5">
  <img src="/assets/brand/dentaldata-logo-horizontal-white.svg" alt="" style="height:64px;margin:0 auto 44px" data-a="pop">
  <div class="k" data-a="fade" data-t=".5">Dental Data · Pregunta {n}</div>
  <div class="h1" data-a="up" data-t=".8">{pregunta_html}</div>
</section>'''
def cierre(frase1, frase2, lead, dur=6.5):
    return f'''<section class="esc centro cierre" data-nombre="Cierre" data-dur="{dur}">
  <div class="frase"><span data-a="up">{frase1}</span><br><span class="oro" data-a="up" data-t=".9">{frase2}</span></div>
  <span class="raya" data-a="bar" data-t="1.8"></span>
  <div class="lead" data-a="fade" data-t="2.3" style="font-size:31px;color:#fff">{lead}</div>
  <img class="logo-fin" src="/assets/brand/dentaldata-logo-horizontal-white.svg" alt="Dental Data" style="margin-left:auto;margin-right:auto" data-a="pop" data-t="3.0">
</section>'''
def az(x, y, svg, nombre, sub="", t=0, w=None, ancho=210, a="pop"):
    """Icono oficial de Microsoft (assets/azure) con el nombre completo del servicio debajo."""
    s = f'<small>{sub}</small>' if sub else ''
    cuando = f' data-w="{w}"' if w else at(t)
    return (f'<div class="nodo az" style="left:{x}px;top:{y}px;width:{ancho}px" data-a="{a}"{cuando}>'
            f'<div class="disco"><img src="/presentaciones/assets/azure/{svg}.svg" alt=""></div>{nombre}{s}</div>')
def caja(x, y, w, h, titulo, c="", t=0, a="fade"):
    """Recuadro de capa (borde fino) con su rótulo arriba a la izquierda."""
    return (f'<div class="capa {c}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px" data-a="{a}"{at(t)}>'
            f'<span>{titulo}</span></div>')
