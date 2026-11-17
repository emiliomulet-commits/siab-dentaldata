from comun import *
TITULO = "¿Cómo funciona un espacio de datos federado?"
CHIP = "¿Cómo funciona un espacio de datos federado?"
DESC = "Presentación animada de Dental Data: cómo funciona un espacio de datos dental federado."
FUENTES = "Fuente: Dental Data · la solución y los casos de uso (base de conocimiento pública)"
CX, CY = 704, 250
P = [(190, 110, "clinica", "Clínica"), (190, 430, "clinica", "Clínica"), (1218, 110, "clinica", "Cadena dental"), (1218, 430, "aseguradora", "Aseguradora")]

def red(t0=0, lin=True):
    h = ''
    if lin: h += lineas(*[(x, y-28, CX, CY-28, "", t0 + .6 + i*.25) for i, (x, y, _, _) in enumerate(P)])
    h += nodo(CX, CY, "catalogo", "Catálogo común", "solo metadatos", disco="oro", t=t0)
    for i, (x, y, ic, tx) in enumerate(P):
        h += nodo(x, y, ic, tx, "+ conector", t=t0 + .2 + i*.2)
    return h

ida = ''.join(paquete(CX, CY-28, x-CX, y-CY, 1.6 + i*.15, d=1.0, c="blanco") for i, (x, y, _, _) in enumerate(P))
vuelta = ''.join(paquete(x, y-28, CX-x, CY-y, 4.0 + i*.15, d=1.0) for i, (x, y, _, _) in enumerate(P))

ESCENAS = [
apertura(2, "¿Cómo funciona un espacio de datos <span class=\"oro\">federado</span>?"),

"""<section class="esc" data-nombre="La clínica" data-dur="7">
  <div class="h2" data-a="up">Cada participante conserva sus expedientes <span class="oro">en su propio software</span></div>
  <div class="lienzo fijo">""" + lineas((520, 222, 880, 222, "oro", 1.6)).replace('data-t="1.6"', 'data-w="junto"') + nodo(440, 250, "software", "Software de gestión", "expedientes y radiografías", t=.6, ancho=260)
  + nodo(960, 250, "conector", "Conector", "se instala a su lado", disco="oro", t=2.2, ancho=260).replace('data-t="2.2"', 'data-w="se instala"') + """</div>
</section>""",

"""<section class="esc" data-nombre="La red" data-dur="8">
  <div class="h2" data-a="up">Los conectores forman una red con un <span class="oro">catálogo común</span></div>
  <div class="lienzo fijo">""" + red(.6) + etq(CX, 470, "El catálogo dice qué datos hay. No guarda los datos.", "oro", 3.4) + """</div>
</section>""",

"""<section class="esc" data-nombre="Una pregunta" data-dur="8.5">
  <div class="h2" data-a="up">La pregunta viaja; <span class="oro">vuelve solo el resultado</span></div>
  <div class="lienzo fijo">""" + red(0, True).replace('data-a="pop"', 'data-a="fade" data-d=".3"').replace('data-a="draw"', 'data-a="fade" data-d=".3"') + ida + vuelta
  + """</div>
  <div class="pasos">
    <span class="pild" data-a="up" data-t="1.4">1 · La pregunta viaja</span>
    <span class="pild" data-a="up" data-t="2.9">2 · Se calcula en cada clínica</span>
    <span class="pild oro" data-a="up" data-t="4.2">3 · Vuelve el resultado agregado</span>
  </div>
</section>""",

"""<section class="esc" data-nombre="Qué viaja y qué no" data-dur="8">
  <div class="h2" data-a="up">Qué se mueve por la red… <span class="oro">y qué no</span></div>
  <div class="fila">
    <div class="card ok-c" data-a="left" data-t=".8"><h3>Viaja</h3><ul class="lista">
      <li data-a="fade" data-t="1.3"><i data-i="ok"></i>Consentimientos</li>
      <li data-a="fade" data-t="1.7"><i data-i="ok"></i>Metadatos del catálogo</li>
      <li data-a="fade" data-t="2.1"><i data-i="ok"></i>Resultados agregados</li></ul></div>
    <div class="card ko-c" data-a="right" data-t="2.8"><h3>No viaja</h3><ul class="lista">
      <li data-a="fade" data-t="3.3"><i data-i="no"></i>Expedientes identificables</li>
      <li data-a="fade" data-t="3.7"><i data-i="no"></i>Radiografías</li></ul></div>
  </div>
</section>""",

cierre("El dato se queda.", "Viaja la respuesta.", "Así funciona un espacio de datos federado."),
]
