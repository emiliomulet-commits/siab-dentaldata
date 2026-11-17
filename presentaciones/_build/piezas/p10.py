from comun import *
TITULO = "¿Cómo se participa en Dental Data?"
CHIP = "¿Cómo se participa en Dental Data?"
DESC = "Presentación animada de Dental Data: el piloto en España, la hoja de ruta y cómo participar."
FUENTES = "Fuentes: Dental Data · piloto, hoja de ruta y alianza España–Países Bajos (base de conocimiento) · Sin tarifas publicadas"
RUTA = [("8%", "Antes de mar. 2027", "Piloto con una cadena o aseguradora"), ("36%", "2027–2028", "Consolidar los pilotos"), ("64%", "Mar. 2029", "Espacio dental catalogado para el EEDS"), ("92%", "2029–2031", "Línea de imagen dental")]
ESCENAS = [
apertura(10, "¿Cómo se participa en <span class=\"oro\">Dental Data</span>?"),
"""<section class="esc" data-nombre="Buscamos" data-dur="8">
  <div class="k" data-a="fade">Buscamos</div>
  <div class="card acento" data-a="up" data-t=".4" style="max-width:1150px"><div class="ico"><i data-i="mano"></i></div>
    <h3 style="font-size:34px">Una cadena dental o una aseguradora en España</h3>
    <ul class="lista">
      <li data-a="fade" data-t="1.6"><i data-i="grafica"></i>Piloto de indicadores de calidad entre clínicas</li>
      <li data-a="fade" data-w="antes de marzo"><i data-i="calendario"></i>Antes de marzo de 2027</li></ul></div>
</section>""",
"""<section class="esc centro" data-nombre="Cómo se financia" data-dur="6.5">
  <div class="h2" data-a="up">El propio caso de uso <span class="oro">financia el conector</span></div>
  <div class="lead" data-a="fade" data-t="1.4">El coste depende del número de clínicas y del caso de uso. Se concreta en una reunión.</div>
</section>""",
"""<section class="esc" data-nombre="Hoja de ruta" data-dur="10">
  <div class="h2" data-a="up">La <span class="oro">hoja de ruta</span></div>
  <div class="tl"><div class="eje" data-a="bar" data-t=".5"></div>""" +
  ''.join(f'<div class="hito" style="left:{x}" data-a="up" {w}><div class="f" style="font-size:26px">{f}</div><span class="p"></span><div class="t">{t}</div></div>' for (x, f, t), w in zip(RUTA, ['data-t="1.0"', 'data-w="consolidamos"', 'data-w="catalogado"', 'data-w="a partir"'])) + """</div>
</section>""",
"""<section class="esc centro" data-nombre="También buscamos" data-dur="7.5">
  <div class="h2" data-a="up">También queremos hablar con…</div>
  <div class="nube" style="margin-top:50px;max-width:1150px;margin-left:auto;margin-right:auto">
    <span class="pild" style="font-size:23px;padding:13px 24px" data-a="pop" data-t=".8">Proveedores de software de gestión</span>
    <span class="pild" style="font-size:23px;padding:13px 24px" data-a="pop" data-w="partners">Partners de Microsoft</span>
    <span class="pild" style="font-size:23px;padding:13px 24px" data-a="pop" data-w="industria">Industria</span>
    <span class="pild" style="font-size:23px;padding:13px 24px" data-a="pop" data-w="colegios">Colegios profesionales</span>
  </div>
  <div style="margin-top:34px"><span class="pild oro" style="font-size:24px;padding:14px 28px" data-a="pop" data-w="alianza"><i data-i="globo"></i>Alianza España–Países Bajos</span></div>
</section>""",
"""<section class="esc centro cierre" data-nombre="¿Hablamos?" data-dur="8">
  <div class="frase oro" data-a="pop">¿Hablamos?</div>
  <span class="raya" data-a="bar" data-t=".9"></span>
  <ul class="lista" style="align-items:center;margin-top:34px">
    <li data-a="fade" data-t="1.4"><i data-i="correo" class="oro"></i>partners@softwareinabox.eu</li>
    <li data-a="fade" data-t="1.9"><i data-i="telefono" class="oro"></i>+34 601 398 868</li>
    <li data-a="fade" data-t="2.4"><i data-i="globo" class="oro"></i>dentaldata.softwareinabox.eu</li>
  </ul>
  <img class="logo-fin" src="/assets/brand/dentaldata-logo-horizontal-white.svg" alt="Dental Data" style="margin-left:auto;margin-right:auto;height:60px" data-a="pop" data-t="3.0">
</section>""",
]
