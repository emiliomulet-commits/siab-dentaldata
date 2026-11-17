from comun import *
TITULO = "¿Mis datos salen de la clínica?"
CHIP = "¿Mis datos salen de la clínica?"
DESC = "Presentación animada de Dental Data: privacidad, contratos de uso y control de la clínica sobre sus datos."
FUENTES = "Fuentes: Dental Data (base de conocimiento) · RGPD · LO 3/2018 · Ley 41/2002 · Reglamento (UE) 2025/327, arts. 54 y 71 · Información general; no es asesoramiento jurídico"
ESCENAS = [
apertura(3, "¿Mis datos <span class=\"oro\">salen de la clínica</span>?"),
"""<section class="esc centro" data-nombre="La respuesta" data-dur="6.5">
  <div class="cifra" style="font-size:190px" data-a="pop">No.</div>
  <div class="h2" data-a="up" data-t="1.0" style="margin-top:30px">Ningún expediente identificable <span class="oro">abandona la clínica</span></div>
</section>""",
"""<section class="esc" data-nombre="El contrato" data-dur="8">
  <div class="h2" data-a="up">Cada uso de los datos tiene <span class="oro">un contrato digital</span></div>
  <div class="fila" style="align-items:stretch">
    <div class="card acento" data-a="left" data-t=".8" style="flex:1.2"><div class="ico"><i data-i="contrato"></i></div><h3>Contrato de uso (ODRL)</h3>
      <ul class="lista">
        <li data-a="fade" data-w="quien accede"><i data-i="personas"></i>¿Quién accede?</li>
        <li data-a="fade" data-w="para que"><i data-i="buscar"></i>¿Para qué?</li>
        <li data-a="fade" data-w="durante"><i data-i="reloj"></i>¿Durante cuánto tiempo?</li></ul></div>
    <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:22px">
      <div class="lead" data-a="fade" data-w="y ese contrato" style="margin:0">Y no se queda en papel:</div>
      <div class="h2" data-a="up" data-w="lo hace cumplir" style="font-size:40px">lo hace cumplir <span class="oro">la propia máquina</span></div>
    </div>
  </div>
</section>""",
"""<section class="esc" data-nombre="La máquina lo hace cumplir" data-dur="9">
  <div class="h2" data-a="up">Sin contrato no hay acceso. <span class="oro">Con contrato, solo un resultado agregado.</span></div>
  <div class="lienzo fijo">""" + lineas((300, 112, 640, 112, "disc", .8), (300, 382, 1080, 302, "oro", 3.0)).replace('data-t="3.0"', 'data-w="si lo tiene"') +
  nodo(190, 140, "pregunta", "Solicitud", "sin contrato", disco="osc", t=.4) +
  nodo(190, 410, "contrato", "Solicitud", "con contrato", t=2.6).replace('data-t="2.6"', 'data-w="si lo tiene"') +
  nodo(1180, 300, "clinica", "Clínica", "con su conector", disco="oro", t=.2) +
  '<div style="position:absolute;left:640px;top:112px;transform:translate(-50%,-50%)" data-a="pop" data-w="no hay acceso"><span class="pild ko"><i data-i="no"></i>Acceso denegado</span></div>' +
  paquete(1080, 302, -780, 80, 4.6, d=1.3, fin="queda").replace('data-t="4.6"', 'data-w="solo vuelve"') +
  etq(700, 470, "Resultado agregado", "oro", 5.6).replace('data-t="5.6"', 'data-w="agregado"') + """</div>
</section>""",
"""<section class="esc centro" data-nombre="El marco" data-dur="7.5">
  <div class="h2" data-a="up">La clínica decide siempre, <span class="oro">dentro de la ley</span></div>
  <div class="nube" style="margin-top:50px;max-width:1250px;margin-left:auto;margin-right:auto">
    <span class="pild" data-a="pop" data-w="reglamento general"><i data-i="ley" class="blanco"></i>RGPD</span>
    <span class="pild" data-a="pop" data-w="normativa">LO 3/2018 de protección de datos</span>
    <span class="pild" data-a="pop" data-w="espanola">Ley 41/2002 de autonomía del paciente</span>
    <span class="pild oro" data-a="pop" data-w="nunca se usan">EEDS · art. 54: nunca para publicidad</span>
    <span class="pild oro" data-a="pop" data-w="publicidad">EEDS · art. 71: el paciente puede oponerse</span>
  </div>
</section>""",
cierre("Sin contrato,", "no hay acceso.", "La clínica decide siempre."),
]
