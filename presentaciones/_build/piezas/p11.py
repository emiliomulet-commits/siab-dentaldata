from comun import *
import re
def W(h, w):
    """Sincroniza el primer elemento animado con una palabra de la locución."""
    h = re.sub(r' data-t="[0-9.]+"', "", h, count=1)
    return h.replace(" data-a=", f' data-w="{w}" data-a=', 1)

TITULO = "¿Qué montamos en Microsoft Azure?"
CHIP = "¿Qué montamos en Microsoft Azure?"
DESC = "Presentación animada de Dental Data: la arquitectura del espacio de datos dental con los componentes de Microsoft Azure y el conector Eclipse EDC."
FUENTES = ("Fuentes: Dental Data · documento técnico «Espacio de datos de salud dental sobre tecnología Microsoft conforme a Gaia-X» (v1.3) "
           "y propuesta de MVP (v1.4) · Iconos oficiales de Microsoft (Azure, Microsoft Entra y Microsoft Fabric), usados según sus condiciones para diagramas de arquitectura · "
           "Microsoft, Azure, Entra, Fabric y los nombres de sus servicios son marcas de Microsoft Corporation")

ESCENAS = [
apertura(11, "¿Qué montamos en <span class=\"oro\">Microsoft Azure</span>?"),

# 2 · La regla
"""<section class="esc" data-nombre="La regla" data-dur="8">
  <div class="h2" data-a="up">Una regla guía el diseño</div>
  <div class="lienzo fijo">""" +
  caja(150, 30, 1108, 460, "Frontera · estándares abiertos", "oro", t=2.4) +
  caja(340, 130, 728, 260, "Nodo · Microsoft Azure", "", t=.7) +
  '<div style="position:absolute;left:704px;top:260px;transform:translate(-50%,-50%);text-align:center;font:800 40px/1.2 Montserrat,sans-serif;color:#fff" data-a="pop" data-t="1.1">Microsoft<br><span class="oro">dentro del nodo</span></div>' +
  etq(704, 490, "Estándares abiertos en la frontera", "oro", 2.9) + """</div>
</section>""",

# 3 · La clínica
"""<section class="esc" data-nombre="La clínica" data-dur="8">
  <div class="h2" data-a="up">1 · En la <span class="oro">clínica</span></div>
  <div class="lienzo fijo">""" +
  lineas((300, 250, 590, 250, "", 1.2), (820, 250, 1080, 250, "oro", 2.6)) +
  nodo(200, 250, "rx", "Equipo de rayos X", "radiografía, CBCT", t=.5, ancho=230) +
  W(nodo(705, 250, "conector", "Pasarela DICOM", "Orthanc · código abierto", disco="osc", t=1.3, ancho=250), "pasarela") +
  W(nodo(1190, 250, "candado", "Seudonimizado en origen", "sin datos que identifiquen al paciente", disco="oro", t=3.0, ancho=290), "pseudonimiza") +
  paquete(300, 250, 290, 0, 1.8) + paquete(820, 250, 260, 0, 3.3, c="blanco") + """</div>
</section>""",

# 4 · El nodo de datos
"""<section class="esc" data-nombre="El nodo de datos" data-dur="10">
  <div class="h2" data-a="up">2 · El <span class="oro">nodo de datos</span> en Azure</div>
  <div class="lienzo fijo">""" +
  caja(70, 20, 1268, 470, "Nodo de datos · Microsoft Azure", "", t=.2) +
  lineas((480, 200, 600, 200, "", 3.0), (820, 200, 940, 200, "", 4.0)) +
  az(330, 200, "fhir", "Azure Health Data Services", w="azure health", ancho=300) +
  W(etq(255, 365, "Expediente · FHIR", "", 1.6), "el expediente") + W(etq(420, 365, "Imagen · DICOM", "", 2.1), "la imagen") +
  az(710, 200, "fabric", "Microsoft Fabric", "prepara la analítica", w="microsoft fabric", ancho=240) +
  az(1050, 200, "onelake", "OneLake", "formatos abiertos", w="onelake", ancho=240) + """</div>
</section>""",

# 5 · Seguridad e identidad
"""<section class="esc" data-nombre="Seguridad" data-dur="8">
  <div class="h2" data-a="up">3 · Una capa de <span class="oro">seguridad e identidad</span></div>
  <div class="lienzo fijo">""" +
  caja(50, 60, 1308, 400, "Seguridad e identidad · alrededor de todo", "seg", t=.2) +
  az(225, 250, "entra-id", "Microsoft Entra ID", "identidades", w="entra id", ancho=270) +
  az(545, 250, "key-vault", "Azure Key Vault", "claves y secretos", w="key vault", ancho=270) +
  az(865, 250, "defender", "Microsoft Defender for Cloud", "protección", w="defender", ancho=290) +
  az(1185, 250, "sentinel", "Microsoft Sentinel", "vigilancia", w="sentinel", ancho=270) + """</div>
</section>""",

# 6 · La frontera
"""<section class="esc" data-nombre="La frontera" data-dur="11">
  <div class="h2" data-a="up">4 · La <span class="oro">frontera</span>: el conector Eclipse EDC</div>
  <div class="lienzo fijo">""" +
  caja(620, 60, 760, 380, "Frontera · estándares abiertos", "oro", t=2.0) +
  lineas((290, 250, 360, 250, "", 1.4), (560, 250, 690, 250, "oro", 2.4), (850, 250, 930, 250, "oro", 3.8), (1090, 250, 1170, 250, "oro", 5.0)) +
  az(170, 250, "aks", "Azure Kubernetes Service", "donde se despliega", w="azure kubernetes", ancho=240) +
  W(nodo(460, 250, "conector", "Conector Eclipse EDC", "código abierto", disco="oro", t=1.0, ancho=220), "eclipse") +
  W(nodo(770, 250, "catalogo", "Catálogo", "HealthDCAT-AP", t=2.8, ancho=170), "publica") +
  W(nodo(1010, 250, "contrato", "Contrato", "ODRL", t=4.1, ancho=170), "negocia") +
  W(nodo(1250, 250, "escudo", "Credenciales", "Gaia-X", t=5.3, ancho=170), "se identifica") + """</div>
</section>""",

# 7 · La inteligencia artificial
"""<section class="esc" data-nombre="La IA" data-dur="14">
  <div class="h2" data-a="up">5 · La <span class="oro">IA</span>: el modelo viaja, los datos no</div>
  <div class="lienzo fijo">""" +
  lineas((704, 260, 420, 400, "oro", 1.6), (704, 260, 704, 400, "oro", 1.6), (704, 260, 988, 400, "oro", 1.6)) +
  az(704, 150, "azure-ml", "Azure Machine Learning", "aprendizaje federado · NVIDIA FLARE", w="azure machine", ancho=330) +
  nodo(420, 450, "clinica", "Clínica A", t=1.2, ancho=160) +
  nodo(704, 450, "clinica", "Clínica B", t=1.3, ancho=160) +
  nodo(988, 450, "clinica", "Clínica C", t=1.4, ancho=160) +
  W(paquete(704, 262, -284, 140, 2.4, d=1.2), "el modelo viaja") + W(paquete(704, 262, 0, 140, 2.4, d=1.2), "el modelo viaja") + W(paquete(704, 262, 284, 140, 2.4, d=1.2), "el modelo viaja") +
  W(nodo(170, 170, "candado", "Computación confidencial", "protege el dato mientras se procesa", disco="osc", t=4.5, ancho=260), "la computacion") +
  az(1235, 170, "foundry", "Microsoft Foundry", "borradores que revisa el dentista", w="microsoft foundry", ancho=270) + """</div>
</section>""",

# 8 · El recorrido completo
"""<section class="esc" data-nombre="El recorrido" data-dur="10">
  <div class="h2" data-a="up">El recorrido de una radiografía</div>
  <div class="lienzo fijo">""" +
  lineas((210, 170, 330, 170, "", .9), (510, 170, 610, 170, "", .9), (790, 170, 890, 170, "", .9), (1070, 170, 1190, 170, "oro", .9)) +
  nodo(130, 170, "rx", "Clínica", "pasarela DICOM", t=.3, ancho=170) +
  az(420, 170, "fhir", "Azure Health Data Services", t=.5, ancho=230) +
  az(700, 170, "fabric", "Microsoft Fabric y OneLake", t=.7, ancho=230) +
  nodo(980, 170, "conector", "Eclipse EDC", "en Azure Kubernetes Service", disco="oro", t=.9, ancho=230) +
  nodo(1275, 170, "red", "Red europea", "otras clínicas", t=1.1, ancho=170) +
  caja(60, 330, 1288, 100, "Seguridad e identidad", "seg", t=1.4) +
  '<div style="position:absolute;left:704px;top:382px;transform:translate(-50%,-50%);font:700 21px Hanken Grotesk,sans-serif;color:#DDE5EF;white-space:nowrap" data-a="fade" data-t="1.6">Microsoft Entra ID · Azure Key Vault · Microsoft Defender for Cloud · Microsoft Sentinel</div>' +
  paquete(130, 170, 1145, 0, 2.2, d=3.6) +
  '<div style="position:absolute;left:704px;top:492px;transform:translate(-50%,-50%)"><span class="pild ok" data-a="pop" data-w="ningun dato"><i data-i="ok"></i>Ningún dato identificable sale del nodo</span></div>' + """</div>
</section>""",

cierre("Microsoft dentro del nodo.", "Estándares abiertos en la frontera.", "Así montamos Dental Data en Microsoft Azure."),
]
