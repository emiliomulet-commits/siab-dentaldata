from comun import *
TITULO = "¿Qué gana una cadena dental?"
CHIP = "¿Qué gana una cadena dental?"
DESC = "Presentación animada de Dental Data: indicadores de calidad comparables entre clínicas sin migrar expedientes."
FUENTES = "Fuentes: Dental Data · casos de uso y piloto (base de conocimiento) · Reglamento (UE) 2025/327, art. 72 · Barras ilustrativas"
XS = [150, 427, 704, 981, 1258]
def clinicas(t0, con=False, a="pop"):
    h = ''
    for i, x in enumerate(XS):
        h += nodo(x, 150, "clinica", f"Clínica {i+1}", f"Software {'ABCDE'[i]}", a=a, t=t0 + i*.2)
        if con: h += nodo(x, 400, "conector", "Conector", "", disco="oro", t=t0 + 1.2 + i*.25, ancho=160)
    if con: h = lineas(*[(x, 205, x, 350, "oro", t0 + 1.0 + i*.25) for i, x in enumerate(XS)]) + h
    return h
ESCENAS = [
apertura(4, "¿Qué gana una <span class=\"oro\">cadena dental</span>?"),
"""<section class="esc" data-nombre="El problema" data-dur="7.5">
  <div class="h2" data-a="up">Una cadena crece comprando clínicas… <span class="oro">y cada una trae su software</span></div>
  <div class="lienzo fijo">""" + clinicas(.8) + '<div style="position:absolute;left:704px;top:430px;transform:translate(-50%,-50%)"><span class="pild ko" data-a="up" data-w="migrar"><i data-i="no"></i>Comparar hoy obliga a migrar expedientes: caro y arriesgado</span></div>' + """</div>
</section>""",
"""<section class="esc" data-nombre="Sin migrar" data-dur="7">
  <div class="h2" data-a="up">Con Dental Data no hace falta: <span class="oro">un conector junto a cada software</span></div>
  <div class="lienzo fijo">""" + clinicas(0, True, a="fade") + """</div>
</section>""",
"""<section class="esc" data-nombre="Indicadores comparables" data-dur="9">
  <div class="h2" data-a="up">El mismo indicador, <span class="oro">calculado en cada clínica</span></div>
  <div class="barras" style="margin-top:46px">
    <div class="b"><i style="height:72%" data-a="barv" data-t=".9"></i>Clínica 1</div>
    <div class="b"><i style="height:58%" data-a="barv" data-t="1.1"></i>Clínica 2</div>
    <div class="b"><i style="height:85%" data-a="barv" data-t="1.3"></i>Clínica 3</div>
    <div class="b"><i style="height:64%" data-a="barv" data-t="1.5"></i>Clínica 4</div>
    <div class="b"><i style="height:77%" data-a="barv" data-t="1.7"></i>Clínica 5</div>
  </div>
  <div class="pasos" style="margin-top:30px"><span class="pild" data-a="up" data-t="3.0">Misma definición en toda la red</span><span class="pild oro" data-a="up" data-w="ningun expediente">Ningún expediente cambia de sitio</span></div>
</section>""",
"""<section class="esc" data-nombre="Valor añadido" data-dur="8">
  <div class="h2" data-a="up">Además…</div>
  <div class="fila">
    <div class="card" data-a="up" data-t=".8"><div class="ico"><i data-i="euro"></i></div><h3>Se financia con su propio uso</h3><p>El caso de uso interno de la cadena financia el despliegue del conector.</p></div>
    <div class="card" data-a="up" data-w="prepara"><div class="ico"><i data-i="escudo"></i></div><h3>Preparada para el EEDS</h3><p>Base para optar al estatus de titular de datos de confianza (art. 72).</p></div>
  </div>
</section>""",
cierre("Conecta tus clínicas", "sin migrar un solo expediente.", "Indicadores de calidad comparables en toda la red."),
]
