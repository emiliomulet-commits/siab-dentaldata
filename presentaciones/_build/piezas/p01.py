TITULO = "¿Por qué faltan los datos dentales en el Espacio Europeo de Datos de Salud?"
CHIP = "¿Por qué faltan los datos dentales en el EEDS?"
DESC = "Presentación animada de Dental Data: por qué la salud bucodental es la gran ausente del Espacio Europeo de Datos de Salud."
FUENTES = "Fuentes: estudio comparativo de Software in a Box (nov. 2026) · INE · Consejo General de Dentistas (colegiados 2025)"

ESCENAS = [
# 1 · Apertura
"""<section class="esc centro" data-nombre="Apertura" data-dur="5.5">
  <img src="/assets/brand/dentaldata-logo-horizontal-white.svg" alt="" style="height:64px;margin:0 auto 44px" data-a="pop">
  <div class="k" data-a="fade" data-t=".5">Dental Data · Pregunta 1</div>
  <div class="h1" data-a="up" data-t=".8">¿Por qué faltan los datos dentales en el <span class="oro">Espacio Europeo de Datos de Salud</span>?</div>
</section>""",

# 2 · Los grandes ausentes
"""<section class="esc" data-nombre="Los grandes ausentes" data-dur="7">
  <div class="k" data-a="fade">Espacio Europeo de Datos de Salud</div>
  <div class="h2" data-a="up" data-t=".2">Los datos dentales son <span class="oro">los grandes ausentes</span></div>
  <div class="rejilla">
    <div class="pieza" data-a="pop" data-t="1.0"><i data-i="expediente"></i>Historia clínica</div>
    <div class="pieza" data-a="pop" data-t="1.3"><i data-i="receta"></i>Receta electrónica</div>
    <div class="pieza" data-a="pop" data-t="1.6"><i data-i="rx"></i>Imagen médica</div>
    <div class="pieza" data-a="pop" data-t="1.9"><i data-i="buscar"></i>Pruebas de laboratorio</div>
    <div class="pieza hueco" data-a="pop" data-t="2.8"><i data-i="muela"></i>Salud bucodental<br><span style="font-size:17px;font-weight:600">sin conectar</span></div>
  </div>
</section>""",

# 3 · Por qué
"""<section class="esc" data-nombre="Por qué" data-dur="8">
  <div class="h2" data-a="up">No por falta de valor, sino por <span class="oro">cómo está organizada</span> la odontología</div>
  <div class="fila">
    <div class="card" data-a="up" data-t="1.0"><div class="ico"><i data-i="clinica"></i></div><h3>Consultas pequeñas</h3><p>La mayoría son microempresas</p></div>
    <div class="card" data-a="up" data-t="1.6"><div class="ico"><i data-i="euro"></i></div><h3>Gasto privado</h3><p>En adultos, lo paga casi todo el paciente</p></div>
    <div class="card" data-a="up" data-t="2.2"><div class="ico"><i data-i="software"></i></div><h3>Software propietario</h3><p>Cada clínica, el suyo</p></div>
    <div class="card" data-a="up" data-t="2.8"><div class="ico"><i data-i="grafica"></i></div><h3>Sin registro nacional</h3><p>No hay registro de salud bucodental</p></div>
  </div>
</section>""",

# 4 · España en cifras
"""<section class="esc" data-nombre="España en cifras" data-dur="9">
  <div class="k" data-a="fade">España</div>
  <div class="h2" data-a="up" data-t=".2">Un mercado grande, privado y fragmentado</div>
  <div class="fila" style="margin-top:64px">
    <div><div class="cifra"><span data-a="count" data-to="97" data-suf="&lt;small&gt;%&lt;/small&gt;" data-w="97">0</span></div><div class="cifra-t" data-a="fade" data-w="paga">del gasto dental lo paga directamente el paciente</div></div>
    <div><div class="cifra"><span data-a="count" data-to="23000" data-mil="." data-pre="&lt;small&gt;+&lt;/small&gt;" data-w="23">0</span></div><div class="cifra-t" data-a="fade" data-w="clinicas">clínicas registradas, casi todas privadas</div></div>
    <div><div class="cifra"><span data-a="count" data-to="43672" data-mil="." data-w="43">0</span></div><div class="cifra-t" data-a="fade" data-w="dentistas">dentistas colegiados en 2025</div></div>
  </div>
</section>""",

# 5 · Islas de datos
"""<section class="esc" data-nombre="Islas de datos" data-dur="8">
  <div class="h2" data-a="up">Los datos existen, pero viven <span class="oro">en islas</span></div>
  <div class="lienzo">
    <div class="isla" style="left:9%;top:35%" data-a="pop" data-t=".8"><div class="disco"><i data-i="clinica"></i></div><div class="mini"><i data-i="expediente"></i><i data-i="rx"></i></div></div>
    <div class="isla" style="left:27%;top:72%" data-a="pop" data-t="1.0"><div class="disco"><i data-i="clinica"></i></div><div class="mini"><i data-i="expediente"></i><i data-i="rx"></i></div></div>
    <div class="isla" style="left:45%;top:30%" data-a="pop" data-t="1.2"><div class="disco"><i data-i="clinica"></i></div><div class="mini"><i data-i="expediente"></i><i data-i="rx"></i></div></div>
    <div class="isla" style="left:63%;top:70%" data-a="pop" data-t="1.4"><div class="disco"><i data-i="clinica"></i></div><div class="mini"><i data-i="expediente"></i><i data-i="rx"></i></div></div>
    <div class="isla" style="left:81%;top:32%" data-a="pop" data-t="1.6"><div class="disco"><i data-i="aseguradora"></i></div><div class="mini"><i data-i="expediente"></i><i data-i="grafica"></i></div></div>
    <div style="position:absolute;left:50%;bottom:-6px;transform:translateX(-50%);display:flex;gap:16px">
      <span class="pild ko" data-a="up" data-w="guarda"><i data-i="no"></i>Sin conexión entre clínicas</span>
      <span class="pild ko" data-a="up" data-w="sin conexion"><i data-i="no"></i>Sin conexión con la historia clínica pública</span>
    </div>
  </div>
</section>""",

# 6 · Cierre
"""<section class="esc centro cierre" data-nombre="Cierre" data-dur="7">
  <div class="frase"><span data-a="up">Los datos existen.</span><br><span class="oro" data-a="up" data-t=".9">Nadie los conecta.</span></div>
  <span class="raya" data-a="bar" data-t="1.8"></span>
  <div class="lead" data-a="fade" data-t="2.4" style="font-size:31px;color:#fff">Dental Data los conecta <b>sin moverlos</b>.</div>
  <img class="logo-fin" src="/assets/brand/dentaldata-logo-horizontal-white.svg" alt="Dental Data" style="margin-left:auto;margin-right:auto" data-a="pop" data-t="3.2">
</section>""",
]
