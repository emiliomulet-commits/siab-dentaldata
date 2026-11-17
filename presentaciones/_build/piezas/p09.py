from comun import *
TITULO = "¿Qué ofrece Dental Data a la industria?"
CHIP = "¿Qué ofrece Dental Data a la industria?"
DESC = "Presentación animada de Dental Data: evidencia del mundo real bajo contrato para fabricantes, empresas de IA y software de gestión clínica."
FUENTES = "Fuentes: Dental Data (base de conocimiento) · Reglamento (UE) 2025/327, art. 54"
CL = [(1180, 90), (1180, 260), (1180, 430)]
I0 = (230, 260)
ESCENAS = [
apertura(9, "¿Qué ofrece Dental Data a la <span class=\"oro\">industria</span>?"),
"""<section class="esc" data-nombre="Quién" data-dur="7">
  <div class="h2" data-a="up">Para quienes necesitan saber <span class="oro">qué pasa en la consulta</span></div>
  <div class="fila">
    <div class="card" data-a="up" data-t=".7"><div class="ico"><i data-i="implante"></i></div><h3>Implantes</h3></div>
    <div class="card" data-a="up" data-w="materiales"><div class="ico"><i data-i="fabrica"></i></div><h3>Materiales</h3></div>
    <div class="card" data-a="up" data-w="inteligencia"><div class="ico"><i data-i="ia"></i></div><h3>Inteligencia artificial</h3></div>
    <div class="card" data-a="up" data-w="necesitan"><div class="ico"><i data-i="software"></i></div><h3>Software de gestión clínica</h3></div>
  </div>
</section>""",
"""<section class="esc" data-nombre="Evidencia del mundo real" data-dur="9">
  <div class="h2" data-a="up">Evidencia del mundo real, <span class="oro">sin datos identificables</span></div>
  <div class="lienzo fijo">""" + lineas(*[(I0[0], I0[1]-28, x, y-28, "disc", .6 + i*.2) for i, (x, y) in enumerate(CL)]) +
  nodo(*I0, "fabrica", "Industria", "pregunta bajo contrato", disco="oro", t=.3, ancho=260) +
  ''.join(nodo(x, y, "clinica", "Clínicas", "", t=.5 + i*.2) for i, (x, y) in enumerate(CL)) +
  ''.join(paquete(I0[0], I0[1]-28, x-I0[0], y-I0[1], 1.8 + i*.2, d=1.1, c="blanco") for i, (x, y) in enumerate(CL)) +
  ''.join(paquete(x, y-28, I0[0]-x, I0[1]-y, 4.0 + i*.2, d=1.1) for i, (x, y) in enumerate(CL)) +
  etq(704, 470, "Vuelven resultados agregados, nunca expedientes", "oro", 4.6) + """</div>
</section>""",
"""<section class="esc" data-nombre="Para el software de gestión" data-dur="7.5">
  <div class="h2" data-a="up">Para el software de gestión: <span class="oro">un conector que suma servicios</span></div>
  <div class="lienzo fijo">""" + lineas((390, 222, 600, 222, "oro", 1.6), (810, 222, 1020, 222, "oro", 2.6)) +
  nodo(270, 250, "software", "Su software de gestión", "", t=.6, ancho=260) + nodo(704, 250, "conector", "Conector integrado", "", disco="oro", t=1.4, ancho=260) +
  nodo(1138, 250, "estrella", "Nuevos servicios", "para sus clientes", t=2.6, ancho=260) + """</div>
</section>""",
"""<section class="esc" data-nombre="Las reglas" data-dur="7">
  <div class="h2" data-a="up">Las reglas <span class="oro">no cambian</span></div>
  <div class="fila">
    <div class="card" data-a="up" data-t=".7"><div class="ico"><i data-i="contrato"></i></div><h3>Contrato para cada uso</h3><p>Quién, para qué y durante cuánto tiempo.</p></div>
    <div class="card" data-a="up" data-w="solo resultados"><div class="ico"><i data-i="grafica"></i></div><h3>Solo agregados</h3><p>Ningún dato identificable sale de la clínica.</p></div>
    <div class="card ko-c" data-a="up" data-w="nunca"><div class="ico"><i data-i="no"></i></div><h3>Nunca publicidad</h3><p>El EEDS lo prohíbe (art. 54).</p></div>
  </div>
</section>""",
cierre("Evidencia real,", "ordenada y bajo contrato.", "Para la industria y el software dental."),
]
