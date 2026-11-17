from comun import *
TITULO = "¿Qué gana una aseguradora con red dental?"
CHIP = "¿Qué gana una aseguradora con red dental?"
DESC = "Presentación animada de Dental Data: datos coherentes de costes y resultados de una red dental sin centralizar historias."
FUENTES = "Fuentes: Dental Data (base de conocimiento) · Reglamento (UE) 2025/327, art. 54"
A = (704, 110)
C = [(170, 400, "Clínica propia"), (437, 430, "Clínica propia"), (971, 430, "Clínica concertada"), (1238, 400, "Clínica concertada")]
def red(t0, cls, a="pop"):
    h = lineas(*[(x, y-28, A[0], A[1]-28, cls, t0 + .8 + i*.2) for i, (x, y, _) in enumerate(C)])
    h += nodo(A[0], A[1], "aseguradora", "Aseguradora", "", disco="oro", a=a, t=t0)
    for i, (x, y, tx) in enumerate(C): h += nodo(x, y, "clinica", tx, "su propio software", a=a, t=t0 + .3 + i*.15)
    return h
ESCENAS = [
apertura(5, "¿Qué gana una <span class=\"oro\">aseguradora</span> con red dental?"),
"""<section class="esc" data-nombre="La red" data-dur="7.5">
  <div class="h2" data-a="up">Clínicas propias y concertadas, <span class="oro">cada una con su software</span></div>
  <div class="lienzo fijo">""" + red(.6, "disc") + etq(704, 300, "Datos de costes y resultados dispersos", "", 2.8) + """</div>
</section>""",
"""<section class="esc" data-nombre="Datos coherentes" data-dur="9">
  <div class="h2" data-a="up">Datos coherentes de toda la red, <span class="oro">sin centralizar historias</span></div>
  <div class="lienzo fijo">""" + red(0, "oro", a="fade") + ''.join(paquete(x, y-28, A[0]-x, A[1]-y, 2.2 + i*.25, d=1.2) for i, (x, y, _) in enumerate(C))
  + etq(704, 300, "Se calcula en cada clínica · vuelve el resultado agregado", "oro", 3.8) + """</div>
</section>""",
"""<section class="esc" data-nombre="Un canal" data-dur="7">
  <div class="h2" data-a="up">La red también es una <span class="oro">puerta de entrada</span></div>
  <div class="lienzo fijo">""" + lineas((360, 222, 600, 222, "oro", 1.4), (810, 222, 1050, 222, "oro", 2.4)) +
  nodo(250, 250, "clinica", "Clínicas independientes", "", t=.6, ancho=240) + nodo(704, 250, "aseguradora", "Red de la aseguradora", "canal agregado", disco="oro", t=1.6, ancho=240) +
  nodo(1158, 250, "red", "Espacio de datos dental", "", t=2.6, ancho=240) + """</div>
</section>""",
"""<section class="esc" data-nombre="Límites claros" data-dur="7.5">
  <div class="h2" data-a="up">Con límites claros: <span class="oro">lo que el EEDS prohíbe</span></div>
  <div class="fila">
    <div class="card ko-c" data-a="up" data-w="publicidad"><h3>Publicidad</h3><p>Los datos de salud nunca se usan con fines publicitarios.</p></div>
    <div class="card ko-c" data-a="up" data-w="decisiones"><h3>Decisiones que perjudiquen</h3><p>Tampoco para decisiones que perjudiquen a las personas, también en seguros.</p></div>
  </div>
  <div class="lead" data-a="fade" data-t="3.4" style="font-size:20px">Reglamento (UE) 2025/327, artículo 54</div>
</section>""",
cierre("Datos coherentes de toda la red,", "sin centralizar historias.", "Con el control siempre en la clínica."),
]
