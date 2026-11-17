from comun import *
TITULO = "¿Qué fechas marca el Espacio Europeo de Datos de Salud?"
CHIP = "¿Qué fechas marca el EEDS?"
DESC = "Presentación animada de Dental Data: el calendario del Espacio Europeo de Datos de Salud y la ventana 2027–2029."
FUENTES = "Fuentes: Reglamento (UE) 2025/327 (arts. 50 y 105) · Ministerio de Sanidad: consulta pública previa del anteproyecto de Ley de Salud Digital (sept. 2025) y declaraciones del 17/09/2026"
HITOS = [("8%", "26 mar 2025", "Entra en vigor"), ("36%", "26 mar 2027", "Organismos de acceso designados"), ("64%", "26 mar 2029", "Uso secundario: la mayor parte de las normas"), ("92%", "26 mar 2031", "Imágenes médicas, como las radiografías")]
W = [None, "2027", "2029", "2031"]
def linea(t0, a="up"):
    h = f'<div class="eje" data-a="{"bar" if a=="up" else "fade"}" data-t="{t0}"></div>'
    for i, (x, f, tx) in enumerate(HITOS):
        sync = f'data-w="{W[i]}"' if (a == "up" and W[i]) else f'data-t="{t0 + .8 if a=="up" else 0}"'
        h += f'<div class="hito" style="left:{x}" data-a="{a}" {sync}><div class="f">{f}</div><span class="p"></span><div class="t">{tx}</div></div>'
    return h
ESCENAS = [
apertura(7, "¿Qué fechas marca el <span class=\"oro\">Espacio Europeo de Datos de Salud</span>?"),
"""<section class="esc" data-nombre="Línea de tiempo" data-dur="10.5">
  <div class="h2" data-a="up">Ya está en vigor <span class="oro">y tiene fechas</span></div>
  <div class="tl">""" + linea(.6) + """</div>
</section>""",
"""<section class="esc" data-nombre="La ventana" data-dur="7">
  <div class="h2" data-a="up">Entre 2027 y 2029: <span class="oro">dos años para conectar clínicas y cadenas</span></div>
  <div class="tl"><div class="ventana" style="left:36%;width:28%" data-a="bar" data-t=".8"></div>""" + linea(0, "fade") + """</div>
</section>""",
"""<section class="esc" data-nombre="Artículo 50" data-dur="9">
  <div class="h2" data-a="up">La mayoría de las clínicas son microempresas: <span class="oro">exentas por defecto</span></div>
  <div class="lienzo fijo">""" + lineas((370, 222, 590, 222, "oro", 2.0), (820, 222, 1040, 222, "oro", 3.2)).replace('data-t="2.0"', 'data-w="para que participen"').replace('data-t="3.2"', 'data-w="a traves"') +
  nodo(250, 250, "clinica", "Clínicas independientes", "art. 50: exentas salvo decisión del Estado", t=.8, ancho=300) +
  nodo(704, 250, "red", "Canal agregado", "colegios profesionales · redes de aseguradoras", disco="oro", t=2.2, ancho=300).replace('data-t="2.2"', 'data-w="canal agregado"') +
  nodo(1158, 250, "catalogo", "Espacio de datos dental", "", t=3.4, ancho=300).replace('data-t="3.4"', 'data-w="a traves"') + """</div>
</section>""",
"""<section class="esc" data-nombre="España" data-dur="7.5">
  <div class="k" data-a="fade">España</div>
  <div class="card" data-a="up" data-t=".4" style="max-width:1100px"><div class="ico"><i data-i="ley"></i></div><h3>Ley de Salud Digital (anteproyecto)</h3>
    <p style="font-size:23px" data-a="fade" data-w="prevé">El Ministerio de Sanidad la prepara. Prevé organismos de acceso autonómicos y uno nacional (Ministerio de Sanidad), coordinados entre sí e integrados en HealthData@EU.</p>
    <div style="margin-top:18px"><span class="pild" style="background:var(--paper);color:var(--navy);border-color:var(--line)" data-a="fade" data-w="autonomicos">Borrador en preparación · pendiente de audiencia pública</span></div></div>
</section>""",
cierre("Quien llegue a 2029 conectado", "será el interlocutor natural.", "de los organismos de acceso a datos de salud.", dur=7),
]
