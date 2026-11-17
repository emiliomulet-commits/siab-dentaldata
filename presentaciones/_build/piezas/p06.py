from comun import *
TITULO = "IA sobre radiografías sin mover las radiografías"
CHIP = "¿Cómo funciona la IA sobre radiografías dentales?"
DESC = "Presentación animada de Dental Data: aprendizaje federado y computación confidencial sobre imágenes dentales."
FUENTES = "Fuentes: Dental Data (base de conocimiento) · Reglamento (UE) 2026/1744 · Reglamento (UE) 2025/327 · Modelo en validación clínica; no sustituye el diagnóstico profesional"
M = (704, 90)
CL = [(250, 410), (704, 430), (1158, 410)]
ESCENAS = [
apertura(6, "¿Cómo se entrena una <span class=\"oro\">IA dental</span> sin mover las radiografías?"),
"""<section class="esc" data-nombre="El dilema" data-dur="7">
  <div class="h2" data-a="up">Entrenar una IA exige muchas radiografías… <span class="oro">reunirlas es un riesgo</span></div>
  <div class="lienzo fijo">""" + ''.join(nodo(x, y, "rx", "", "", t=.4 + i*.12, ancho=110) for i, (x, y) in enumerate([(120, 130), (120, 430), (420, 110), (988, 110), (1288, 130), (1288, 430)]))
  + ''.join(paquete(x, y-28, 704-x, 250-y, 1.8 + i*.1, d=1.0, c="blanco") for i, (x, y) in enumerate([(120, 130), (120, 430), (420, 110), (988, 110), (1288, 130), (1288, 430)]))
  + nodo(704, 260, "nube", "Un solo almacén", "", disco="osc", t=1.4) +
  '<div style="position:absolute;left:704px;top:440px;transform:translate(-50%,-50%)"><span class="pild ko" data-a="pop" data-t="3.2"><i data-i="no"></i>Centralizar radiografías multiplica el riesgo</span></div>' + """</div>
</section>""",
"""<section class="esc" data-nombre="El algoritmo viaja" data-dur="9">
  <div class="h2" data-a="up">Dental Data invierte el camino: <span class="oro">el algoritmo viaja</span></div>
  <div class="lienzo fijo">""" + lineas(*[(M[0], M[1]-28, x, y-28, "disc", .6 + i*.2) for i, (x, y) in enumerate(CL)]) +
  nodo(M[0], M[1], "ia", "Modelo de IA", "", disco="oro", t=.3) +
  ''.join(nodo(x, y, "clinica", "Clínica", "sus radiografías se quedan", t=.6 + i*.2, ancho=240) for i, (x, y) in enumerate(CL)) +
  ''.join(paquete(M[0], M[1]-28, x-M[0], y-M[1], 1.8 + i*.2, d=1.1, c="blanco") for i, (x, y) in enumerate(CL)) +
  ''.join(paquete(x, y-28, M[0]-x, M[1]-y, 4.2 + i*.2, d=1.1) for i, (x, y) in enumerate(CL)) +
  etq(400, 250, "Aprende en cada clínica", "", 3.0).replace('data-t="3.0"', 'data-w="aprende"') + etq(1010, 250, "Devuelve solo lo aprendido", "oro", 4.6).replace('data-t="4.6"', 'data-w="devuelve"') + """</div>
</section>""",
"""<section class="esc centro" data-nombre="Computación confidencial" data-dur="6.5">
  <div class="card" data-a="pop" style="width:140px;min-height:0;height:140px;margin:0 auto;display:flex;align-items:center;justify-content:center"><i data-i="candado" class="g" style="width:70px;height:70px"></i></div>
  <div class="h2" data-a="up" data-t=".8" style="margin-top:34px">Computación <span class="oro">confidencial</span></div>
  <div class="lead" data-a="fade" data-t="1.6">Protege los datos también mientras se procesan.</div>
</section>""",
"""<section class="esc" data-nombre="El modelo" data-dur="8.5">
  <div class="k" data-a="fade">Primer modelo</div>
  <div class="fila" style="margin-top:20px">
    <div class="card" data-a="up" data-t=".5"><div class="ico"><i data-i="muela"></i></div><h3>Caries interproximal</h3><p>Sobre radiografías dentales.</p></div>
    <div class="card" data-a="up" data-w="perdida"><div class="ico"><i data-i="rx"></i></div><h3>Pérdida ósea periodontal</h3><p>Sobre radiografías dentales.</p></div>
  </div>
  <div class="pasos" style="margin-top:36px"><span class="pild oro" data-a="pop" data-w="validacion">En validación clínica</span><span class="pild" data-a="pop" data-w="ayuda">Ayuda al profesional: no sustituye su diagnóstico</span></div>
</section>""",
"""<section class="esc" data-nombre="Lo que viene" data-dur="7">
  <div class="h2" data-a="up">Preparado para <span class="oro">lo que viene</span></div>
  <div class="tl"><div class="eje" data-a="bar" data-t=".5"></div>
    <div class="hito" style="left:28%" data-a="up" data-t="1.2"><div class="f">2 ago 2028</div><span class="p"></span><div class="t">Reglamento de IA: obligaciones para la IA de los productos sanitarios</div></div>
    <div class="hito" style="left:72%" data-a="up" data-w="2031"><div class="f">26 mar 2031</div><span class="p"></span><div class="t">Las imágenes médicas entran en el Espacio Europeo de Datos de Salud</div></div>
  </div>
</section>""",
cierre("El algoritmo", "va al dato.", "IA sobre imágenes dentales sin mover radiografías."),
]
