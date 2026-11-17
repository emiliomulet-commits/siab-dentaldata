from comun import *
TITULO = "¿Qué tecnología hay detrás de Dental Data?"
CHIP = "¿Qué tecnología hay detrás de Dental Data?"
DESC = "Presentación animada de Dental Data: Microsoft dentro del nodo, estándares abiertos europeos en las fronteras."
FUENTES = "Fuentes: Dental Data · tecnología y empresa (base de conocimiento) · Microsoft y Azure son marcas de Microsoft Corporation; se citan como texto"
EST = ["Gaia-X", "IDSA", "Dataspace Protocol", "Eclipse EDC", "Credenciales verificables", "FHIR", "DICOM", "HealthDCAT-AP"]
ESCENAS = [
apertura(8, "¿Qué tecnología hay detrás de <span class=\"oro\">Dental Data</span>?"),
"""<section class="esc centro" data-nombre="La regla" data-dur="7">
  <div class="h2" data-a="up">Una regla sencilla</div>
  <div style="position:relative;width:440px;height:440px;margin:56px auto 0;flex:none">
    <div data-a="pop" data-t="1.6" style="position:absolute;inset:0;border-radius:50%;border:4px dashed var(--gold)"></div>
    <div data-a="pop" data-t=".6" style="position:absolute;inset:70px;border-radius:50%;background:#fff;color:var(--navy);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;font:800 30px/1.15 'Montserrat',sans-serif">Microsoft<br>Azure<span style="font:600 19px 'Hanken Grotesk';color:var(--mute)">datos en la UE</span></div>
    <div class="etq" style="left:50%;top:50%;transform:translate(-50%,140px)" data-a="fade" data-t="1.2">Dentro del nodo</div>
    <div class="etq oro" style="left:50%;top:0" data-a="fade" data-t="2.4">En la frontera: estándares abiertos</div>
  </div>
</section>""",
"""<section class="esc" data-nombre="Dentro del nodo" data-dur="7.5">
  <div class="h2" data-a="up">Dentro del nodo: <span class="oro">Microsoft</span></div>
  <div class="fila">
    <div class="card" data-a="up" data-t=".7"><div class="ico"><i data-i="nube"></i></div><h3>Conector sobre Microsoft Azure</h3><p>Con los datos en la Unión Europea.</p></div>
    <div class="card" data-a="up" data-w="integrado"><div class="ico"><i data-i="software"></i></div><h3>Integrado</h3><p>Con el software de gestión de la clínica.</p></div>
    <div class="card" data-a="up" data-w="desplegado"><div class="ico"><i data-i="mano"></i></div><h3>Desplegado por partners</h3><p>Integradores y partners de Azure.</p></div>
  </div>
</section>""",
"""<section class="esc centro" data-nombre="En la frontera" data-dur="8">
  <div class="h2" data-a="up">En las fronteras: <span class="oro">estándares europeos abiertos</span></div>
  <div class="nube" style="margin-top:56px;max-width:1150px;margin-left:auto;margin-right:auto">""" +
  ''.join(f'<span class="pild" style="font-size:24px;padding:14px 26px" data-a="pop" data-w="{w}">{e}</span>' for e, w in zip(EST, ["gaiax", "protocolo", "eclipse", "eclipse edc", "credenciales", "fiir", "daicom", "health"])) + """</div>
</section>""",
"""<section class="esc" data-nombre="Abierto a todos" data-dur="6.5">
  <div class="h2" data-a="up">Cualquiera puede conectarse, <span class="oro">aunque no use Microsoft</span></div>
  <div class="lienzo fijo">""" + lineas((420, 222, 990, 222, "oro", 1.4)) +
  nodo(300, 250, "nube", "Nodo sobre Azure", "", disco="oro", t=.6, ancho=260) + nodo(1108, 250, "red", "Participante sin Microsoft", "", t=1.0, ancho=260) +
  etq(704, 222, "Estándares abiertos", "oro", 2.2) + '<div style="position:absolute;left:704px;top:420px;transform:translate(-50%,-50%)"><span class="pild ok" data-a="pop" data-t="3.0"><i data-i="ok"></i>Se conecta igual</span></div>' + """</div>
</section>""",
"""<section class="esc" data-nombre="Experiencia" data-dur="7">
  <div class="h2" data-a="up">No partimos de cero: <span class="oro">tres espacios de datos reales</span></div>
  <div class="fila">
    <div class="card" data-a="up" data-t=".8"><div class="ico"><i data-i="muela"></i></div><h3>Global Data Care</h3><p>Salud, sobre Gaia-X y Pontus-X.</p></div>
    <div class="card" data-a="up" data-t="1.4"><div class="ico"><i data-i="contrato"></i></div><h3>PROCUREDATA</h3><p>Compras públicas.</p></div>
    <div class="card" data-a="up" data-t="2.0"><div class="ico"><i data-i="red"></i></div><h3>EcoDataNet</h3><p>Residuos y economía circular.</p></div>
  </div>
  <div class="lead" data-a="fade" data-t="3.0" style="font-size:21px">Demostradores financiados por la SEDIA (2024–2026), con conectores propios basados en Eclipse.</div>
</section>""",
cierre("Microsoft dentro del nodo.", "Estándares abiertos en las fronteras.", "Un espacio de datos dental abierto a todos."),
]
