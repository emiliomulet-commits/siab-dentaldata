# Dental Data · página europea en inglés (británico) · https://dentaldata.softwareinabox.eu/en/
# Mercado «eu»: partners de Microsoft e integradores, financiadores, consorcios UE y organizaciones de cualquier país.

SALIDA = "en/index.html"
LANG = "en"
PERMITIDO = ['lang="es"', "Español", "España", "SEDIA"]

JSONLD = r'''
{"@context":"https://schema.org","@graph":[
{"@type":"WebPage","@id":"https://dentaldata.softwareinabox.eu/en/#webpage","url":"https://dentaldata.softwareinabox.eu/en/","name":"Dental Data · Federated dental data space for Europe","inLanguage":"en","isPartOf":{"@type":"WebSite","@id":"https://www.softwareinabox.eu/#website","name":"Software in a Box"},"publisher":{"@type":"Organization","@id":"https://www.softwareinabox.eu/#organization","name":"Software in a Box","url":"https://www.softwareinabox.eu/"},"areaServed":"Europe"},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Does my data leave the practice?","acceptedAnswer":{"@type":"Answer","text":"No. Records stay in each practice's, chain's or insurer's own software. Only consents, metadata and aggregated results move, under machine-enforced usage contracts."}},
{"@type":"Question","name":"In which countries is Dental Data available?","acceptedAnswer":{"@type":"Answer","text":"We start in Spain and the Netherlands, with pages for Belgium (Dutch and French), Germany and Denmark. France, Italy and Portugal are being studied."}},
{"@type":"Question","name":"How does the European Health Data Space (EHDS) affect dental care?","acceptedAnswer":{"@type":"Answer","text":"By 26 March 2027 every Member State will have designated its health data access bodies; from 26 March 2029 most secondary use rules apply; from 2031 medical images are added, including dental X-rays and cone-beam CT."}},
{"@type":"Question","name":"How can a technology partner join?","acceptedAnswer":{"@type":"Answer","text":"Through the contact form on this page or partners@softwareinabox.eu. We are looking especially for Microsoft Azure partners and integrators."}}
]}]}
'''

KB_JS = r'''[
{id:'datos',q:'Does my data leave the practice?',k:['leave','move','moved','central','stored','where is','cloud','server','privacy','copy'],
 a:['No. Records stay in the practice management software of each practice, chain or insurer. Dental Data is a <b>federated</b> data space: only consents, metadata and aggregated results move.','Every access is governed by an ODRL contract that the machine enforces: the practice decides who gets access, for what and for how long. No contract, no access.'],s:['ia','seguridad']},
{id:'paises',q:'In which countries is Dental Data available?',k:['country','countries','europe','spain','netherlands','belgium','germany','denmark','france','italy','portugal','market'],
 a:['We start in <b>Spain</b> (pilot with a dental chain or insurer) and the <b>Netherlands</b> (partner programme), building one product for both markets.','In <b>Belgium</b> we seek an institutional alliance and in <b>Germany</b> partners among practice software vendors and MVZ. In <b>Denmark</b> we propose extending the SCOR register logic to adults. France, Italy and Portugal are being studied. Country pages: <a href="/es/" lang="es">Spain</a> · <a href="/nl/" lang="nl">Netherlands</a> · <a href="/nl-be/" lang="nl">België</a> · <a href="/fr-be/" lang="fr">Belgique</a> · <a href="/de/" lang="de">Deutschland</a> · <a href="/da/" lang="da">Danmark</a>.'],s:['partner','documentos']},
{id:'ehds',q:'How does the EHDS affect dental care?',k:['ehds','health data space','regulation','law','2027','2029','2031','article 50','microenterprise','hdab','access body'],
 a:['Key dates: by <b>26 March 2027</b> every Member State will have designated its health data access bodies; from <b>26 March 2029</b> most secondary use rules apply; from <b>2031</b> medical images are added, including dental X-rays, panoramic radiographs and cone-beam CT.','Article 50 exempts microenterprises (most dental practices) from data holder obligations by default, so an aggregated channel is needed for dental data to reach the access bodies.'],s:['paises','datos']},
{id:'ia',q:'How does AI on dental X-rays work?',k:[' ai ','artificial intelligence','x-ray','xray','image','caries','periodont','algorithm','model','federated','learning'],
 a:['With federated learning and confidential computing: <b>the algorithm goes to the data</b>, not the other way round. No X-ray leaves the practice.','Our model for interproximal caries and periodontal bone loss is in clinical validation. It supports the professional and does not replace their diagnosis.'],s:['datos','tecnologia']},
{id:'partner',q:'How can a technology partner join?',k:['partner','integrator','reseller','join','collaborate','alliance','consortium','microsoft partner'],
 a:['We are looking for technology partners, ideally <b>Microsoft Azure partners and integrators</b>, to deploy the connector and bring Dental Data to their market. In the Netherlands we are building it with a local partner.','Leave your details in the <a href="#contacto" data-close>contact form</a> or write to <a href="mailto:partners@softwareinabox.eu">partners@softwareinabox.eu</a>.'],s:['tecnologia','paises']},
{id:'tecnologia',q:'What technology do you use? What is Microsoft\'s role?',k:['technolog','microsoft','azure','connector','standard','gaia','idsa','eclipse','edc','fhir','dicom','integrat'],
 a:['A connector on <b>Microsoft Azure</b>, with data in the EU, integrated with the practice management software.','The borders of the space use open European standards: Gaia-X, IDSA and the Dataspace Protocol, Eclipse EDC, FHIR, DICOM and HealthDCAT-AP, so anyone can connect even without Microsoft.'],s:['partner','datos']},
{id:'seguridad',q:'Is it GDPR compliant? Is it secure?',k:['gdpr','data protection','security','secure','consent','legal','confidential'],
 a:['By design, identifiable data is never centralised: only aggregated results travel, under contract. For AI we use confidential computing.','Each pilot is documented with the organisation\'s data protection officer and a data protection impact assessment.'],s:['datos','ehds']},
{id:'publicidad',q:'Will the data be used for advertising?',k:['advertis','marketing','sell data','commercial'],
 a:['Never. The EHDS expressly prohibits using health data for advertising.','The intended uses are quality of care, AI on images and evidence for industry on implants and materials.'],s:['datos','ehds']},
{id:'experiencia',q:'Who are you and what experience do you have?',k:['who','company','experience','software in a box','reference','projects','global data care'],
 a:['Software in a Box, based in Madrid and Brussels. Between 2024 and 2026 we designed and delivered three data space demonstrators funded by Spain\'s Secretariat of State for Digitalisation and AI: <b>Global Data Care</b> (health), <b>PROCUREDATA</b> (procurement) and <b>EcoDataNet</b> (circular economy).','More at <a href="https://datos.softwareinabox.eu/">datos.softwareinabox.eu</a>.'],s:['tecnologia','partner']},
{id:'documentos',q:'Where can I read the study?',k:['study','document','pdf','download','report','presentation','video','read'],
 a:['The comparative study of five markets is available in <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener">English</a> and <a href="/docs/tandheelkundige-gezondheidsdataruimtes-europa-ehds.pdf" target="_blank" rel="noopener" lang="nl">Dutch</a>, together with the <a href="/docs/dental-data-es-nl-presentation-en.pdf" target="_blank" rel="noopener">presentation</a> and the full video.'],s:['paises','partner']}
]'''

BLOQUES = {
"espana": r'''
<section class="s soft" id="mercados"><div class="wrap">
 <div class="head"><div class="eyebrow">Markets</div><h2>Five markets, five ways of holding dental data</h2><p>The product is the same everywhere. What changes is who pays for adult dental care and therefore where the data sits today. In every country, the only source present everywhere is each practice's own software.</p></div>
 <div class="grid3">
  <div class="card"><div class="num">SPAIN · PILOT</div><h3>Private and fragmented</h3><p>Patients pay 97% of dental spending; records sit in the software of thousands of private practices, chains and insurers. We are looking for a chain or insurer for a quality indicators pilot.</p><p style="margin-top:10px"><a href="/es/" lang="es" hreflang="es">Spanish page →</a></p></div>
  <div class="card"><div class="num">NETHERLANDS · PARTNERS</div><h3>Consolidation and shortage</h3><p>More than 500 practices owned by private equity and about 30% of practices not taking new patients. Chains need to compare practices without migrating records.</p><p style="margin-top:10px"><a href="/nl/" lang="nl" hreflang="nl">Dutch page →</a></p></div>
  <div class="card"><div class="num">BELGIUM · ALLIANCE</div><h3>Payer-driven data</h3><p>Compulsory insurance turns every reimbursable dental act into structured data, but the full record and non-reimbursed care are missing. A market for an institutional alliance.</p><p style="margin-top:10px"><a href="/nl-be/" lang="nl" hreflang="nl-BE">Nederlands →</a>&nbsp;&nbsp;<a href="/fr-be/" lang="fr" hreflang="fr-BE">Français →</a></p></div>
  <div class="card"><div class="num">GERMANY · SOFTWARE PARTNERS</div><h3>Institutional and integrated</h3><p>The electronic patient record has been mandatory in dental practices since 1 October 2025. The opportunity is data quality, compliance and federated analytics for software vendors.</p><p style="margin-top:10px"><a href="/de/" lang="de" hreflang="de-DE">Deutsch →</a></p></div>
  <div class="card"><div class="num">DENMARK · ALLIANCE</div><h3>A public register for children</h3><p>Free care up to age 21 and a children's oral health register since 1972. Adults treated privately and in chains remain largely invisible.</p><p style="margin-top:10px"><a href="/da/" lang="da" hreflang="da-DK">Dansk →</a></p></div>
  <div class="card"><div class="num">FRANCE · ITALY · PORTUGAL</div><h3>Being studied</h3><p>We are extending our comparative study to these three markets before publishing their pages. If you work there, we would like to hear from you.</p></div>
 </div>
 <p class="pcap">Source: Software in a Box, <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener">Dental health data spaces in Europe · Comparative study</a> (November 2026), and the sources cited in it.</p>
</div></section>
''',
"para-quien": r'''
<section class="s soft" id="para-quien"><div class="wrap">
 <div class="head"><div class="eyebrow">Who it is for</div><h2>One product, built once and adapted to each market</h2><p>A Spanish and a local technology partner build one product together and take it to markets that differ in almost everything but share the same need: fragmented data in private software and strong pressure from chains, insurers and funds to share and compare.</p></div>
 <div class="grid4 who-grid">
  <div class="card"><div class="num">MICROSOFT PARTNERS</div><h3>Deploy and integrate</h3><p>Azure partners and integrators who deploy the connector and integrate it with local practice software.</p></div>
  <div class="card"><div class="num">CHAINS AND INSURERS</div><h3>Compare and manage</h3><p>Comparable quality indicators across practices and consistent data on cost and outcomes across networks.</p></div>
  <div class="card"><div class="num">SOFTWARE VENDORS</div><h3>Get ready for the EHDS</h3><p>Practice management software vendors that need interoperability, logging and data quality for the European health data space.</p></div>
  <div class="card"><div class="num">FUNDERS AND CONSORTIA</div><h3>Build Europe's dental data</h3><p>Public funders, research consortia and EU projects that need dental data in the European health data space.</p></div>
 </div>
 <div class="head" style="margin-top:56px;margin-bottom:22px"><h2 style="font-size:28px">Roadmap</h2></div>
 <div class="flow">
  <div class="step"><div class="c">1</div><b>Before March 2027 · Two pilots</b><span>One chain in Spain and one in the Netherlands, focused on quality indicators.</span></div>
  <div class="step"><div class="c">2</div><b>2027–2028 · Consolidate</b><span>Consolidate both pilots, open new markets and take part in public consultations.</span></div>
  <div class="step"><div class="c">3</div><b>March 2029 · Catalogued</b><span>A catalogued dental data space, ready for access requests under the EHDS.</span></div>
 </div>
 <div class="nl-band"><div><b>Country pages</b><p>Each market has its own page, in its own language, with its own figures, laws and offer.</p></div><a href="/es/" lang="es" hreflang="es">España →</a>&nbsp;&nbsp;<a href="/nl/" lang="nl" hreflang="nl">Nederland →</a>&nbsp;&nbsp;<a href="/nl-be/" lang="nl" hreflang="nl-BE">België</a>&nbsp;·&nbsp;<a href="/fr-be/" lang="fr" hreflang="fr-BE">Belgique →</a>&nbsp;&nbsp;<a href="/de/" lang="de" hreflang="de-DE">Deutschland →</a>&nbsp;&nbsp;<a href="/da/" lang="da" hreflang="da-DK">Danmark →</a></div>
</div></section>
''',
"contacto": r'''
<section class="s cta" id="contacto"><div class="wrap">
 <h2>Do you want to work with us?</h2>
 <p>Tell us briefly who you are and where you work. We will suggest a meeting to see how Dental Data fits your organisation or your market.</p>
 <form class="cform" action="https://formsubmit.co/partners@softwareinabox.eu" method="POST">
  <input type="hidden" name="_subject" value="Dental Data · Europe [EN]">
  <input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="https://www.softwareinabox.eu/gracias.html">
  <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
  <label class="sr" for="f-n">Name</label><input id="f-n" name="Name" required placeholder="Full name" autocomplete="name">
  <label class="sr" for="f-o">Organisation</label><input id="f-o" name="Organisation" placeholder="Organisation and country" autocomplete="organization">
  <label class="sr" for="f-p">Profile</label><select id="f-p" class="full" name="Profile"><option value="">Your organisation's profile</option><option>Microsoft partner / integrator</option><option>Dental chain</option><option>Insurer</option><option>Practice software vendor</option><option>Implant, materials or AI manufacturer</option><option>Funder, consortium or public body</option><option>Other</option></select>
  <label class="sr" for="f-e">Email</label><input id="f-e" class="full" type="email" name="Email" required placeholder="Work email" autocomplete="email">
  <label class="sr" for="f-m">Message</label><textarea id="f-m" name="Message" placeholder="What would you like to discuss with us?"></textarea>
  <label class="ok full"><input type="checkbox" name="Consent" value="Accepts the privacy policy" required><span>I have read and accept the <a href="https://www.softwareinabox.eu/en/privacidad.html" target="_blank" rel="noopener">privacy policy</a>. We will only use your data to reply to you.</span></label>
  <button type="submit">Send request</button>
 </form>
 <p style="font-size:15px;margin-top:18px">Or write to <a href="mailto:partners@softwareinabox.eu" style="color:#fff;font-weight:600">partners@softwareinabox.eu</a> · <a href="tel:+34601398868" style="color:#fff;font-weight:600">+34 601 398 868</a> · Madrid and Brussels</p>
</div></section>
''',
}

_MENU = '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6"><path d="m2 4 4 4 4-4"/></svg>'

REEMPLAZOS = [
# ---- cabecera del documento ----
("<title>Dental Data España · Espacio de datos dental federado para el EHDS | Software in a Box</title>",
 "<title>Dental Data · Federated dental data space for the EHDS in Europe | Software in a Box</title>"),
('content="Dental Data es un espacio de datos dental federado sobre Microsoft Azure: indicadores de calidad entre clínicas e IA sobre imágenes sin que los datos salgan de la consulta. Buscamos cadenas y aseguradoras para el piloto en España."',
 'content="Dental Data is a federated dental data space on Microsoft Azure for the European Health Data Space: quality indicators across practices and AI on images without data leaving the practice. Partners wanted across Europe."'),
('<link rel="canonical" href="https://dentaldata.softwareinabox.eu/es/">', '<link rel="canonical" href="https://dentaldata.softwareinabox.eu/en/">'),
('content="es_ES"', 'content="en_GB"'),
('<meta property="og:title" content="Dental Data · Tu espacio de datos dental empieza aquí">', '<meta property="og:title" content="Dental Data · Your dental data space starts here">'),
('content="Compara la calidad entre tus clínicas y aplica IA a las imágenes sin mover un solo expediente. Piloto en España antes de marzo de 2027."',
 'content="Compare quality across practices and apply AI to images without moving a single record. One federated dental data space for Europe."'),
('<meta property="og:url" content="https://dentaldata.softwareinabox.eu/es/">', '<meta property="og:url" content="https://dentaldata.softwareinabox.eu/en/">'),
# ---- cabecera visible ----
('<a class="brand" href="/es/" aria-label="Dental Data España, inicio">', '<a class="brand" href="/en/" aria-label="Dental Data Europe, home">'),
('<span class="sub">sobre Microsoft Azure</span>', '<span class="sub">on Microsoft Azure</span>'),
('aria-label="Menú principal"', 'aria-label="Main menu"'),
('aria-controls="m1">Solución ', 'aria-controls="m1">Solution '),
('<a href="#solucion">Cómo funciona<small>Los datos nunca salen de la clínica</small></a>', '<a href="#solucion">How it works<small>Data never leaves the practice</small></a>'),
('<a href="#casos">Casos de uso<small>Calidad, IA en imágenes, evidencia</small></a>', '<a href="#casos">Use cases<small>Quality, AI on images, evidence</small></a>'),
('<a href="#tecnologia">Tecnología<small>Azure y estándares abiertos europeos</small></a>', '<a href="#tecnologia">Technology<small>Azure and open European standards</small></a>'),
('aria-controls="m2">Para quién ', 'aria-controls="m2">Who it is for '),
('<ul id="m2"><li><a href="#para-quien">Cadenas dentales</a></li><li><a href="#para-quien">Aseguradoras</a></li><li><a href="#para-quien">Clínicas independientes</a></li><li><a href="#para-quien">Software de gestión e IA</a></li></ul>',
 '<ul id="m2"><li><a href="#para-quien">Microsoft partners</a></li><li><a href="#para-quien">Chains and insurers</a></li><li><a href="#para-quien">Software vendors</a></li><li><a href="#para-quien">Funders and consortia</a></li></ul>'),
('aria-controls="m3">Recursos ', 'aria-controls="m3">Resources '),
('<li><a href="#destacados">Estudio, presentación y vídeos</a></li><li><a href="#espana">El mercado español</a></li><li><a href="#preguntas">Preguntas frecuentes</a></li><li><a href="https://datos.softwareinabox.eu/">Nuestros espacios de datos</a></li>',
 '<li><a href="#destacados">Study, presentation and videos</a></li><li><a href="#mercados">Markets</a></li><li><a href="#preguntas">FAQ</a></li><li><a href="https://datos.softwareinabox.eu/">Our data spaces</a></li>'),
('<a class="tbtn white" href="#contacto">Únete al piloto</a>\n  <button', '<a class="tbtn white" href="#contacto">Become a partner</a>\n  <button'),
('<span>Descubre</span>', '<span>Ask</span>'),
('aria-label="Idioma"', 'aria-label="Country and language"'),
('<li><a href="/es/" hreflang="es-ES" lang="es" aria-current="page">Español · España</a></li>', '<li><a href="/es/" hreflang="es-ES" lang="es">Español · España</a></li>'),
('<li><a href="/en/" hreflang="en" lang="en">English · Europe</a></li>', '<li><a href="/en/" hreflang="en" lang="en" aria-current="page">English · Europe</a></li>'),
('<a href="/">Otros países e idiomas</a></nav>', '<a href="/">Other countries and languages</a></nav>'),
('<a class="contact" href="#contacto"><span>Contacto</span>', '<a class="contact" href="#contacto"><span>Contact</span>'),
('aria-label="Abrir menú"', 'aria-label="Open menu"'),
('aria-label="Menú móvil"', 'aria-label="Mobile menu"'),
('<a href="#solucion">Solución</a><a href="#para-quien">Para quién</a><a href="#destacados">Recursos</a><a href="#preguntas">Preguntas frecuentes</a><a href="#contacto">Únete al piloto</a>',
 '<a href="#solucion">Solution</a><a href="#para-quien">Who it is for</a><a href="#destacados">Resources</a><a href="#preguntas">FAQ</a><a href="#contacto">Become a partner</a>'),
# ---- portada ----
('<div class="pre">España · Espacio Europeo de Datos de Salud</div>', '<div class="pre">Europe · European Health Data Space</div>'),
('<h1 id="h1">Tu espacio de datos dental <em>empieza aquí</em></h1>', '<h1 id="h1">Your dental data space <em>starts here</em></h1>'),
('<p class="lead">Pregunta cómo comparar la calidad entre tus clínicas y aplicar IA a las imágenes sin que un solo expediente salga de la consulta.</p>',
 '<p class="lead">One federated dental data space for Europe: compare quality across practices and apply AI to images without a single record leaving the practice.</p>'),
('<label class="sr" for="q">Haz tu pregunta sobre Dental Data</label>', '<label class="sr" for="q">Ask your question about Dental Data</label>'),
('placeholder="Haz tu pregunta sobre Dental Data…"', 'placeholder="Ask your question about Dental Data…"'),
('aria-label="Enviar pregunta"', 'aria-label="Send question"'),
('<button class="chip" type="button" data-q="datos">¿Mis datos salen de la clínica?</button>', '<button class="chip" type="button" data-q="datos">Does my data leave the practice?</button>'),
('<button class="chip" type="button" data-q="cadena">¿Qué gana mi cadena con esto?</button>', '<button class="chip" type="button" data-q="paises">In which countries?</button>'),
('<button class="chip" type="button" data-q="ehds">¿Cómo me afecta el EHDS?</button>', '<button class="chip" type="button" data-q="ehds">How does the EHDS affect dental care?</button>'),
('<button class="chip" type="button" data-q="ia">¿Cómo funciona la IA en radiografías?</button>', '<button class="chip" type="button" data-q="ia">How does AI on X-rays work?</button>'),
('<button class="chip" type="button" data-q="piloto">¿Cómo entro en el piloto?</button>', '<button class="chip" type="button" data-q="partner">How can a partner join?</button>'),
('<p class="trust">Experiencia en <b>3 espacios de datos</b> financiados por la SEDIA · Conector sobre <b>Microsoft Azure</b> con datos en la UE</p>',
 '<p class="trust">Experience in <b>3 publicly funded data spaces</b> · Connector on <b>Microsoft Azure</b> with data in the EU</p>'),
# ---- bloque oscuro ----
('<h2>Conecta tus clínicas sin migrar un solo expediente</h2>', '<h2>One product, two first markets, a whole continent to connect</h2>'),
('<p>Buscamos una cadena dental o una aseguradora en España para el piloto de indicadores de calidad, antes de marzo de 2027.</p>',
 '<p>We are looking for technology partners, ideally Microsoft Azure partners, and for the first dental chains and insurers in Spain and the Netherlands before March 2027.</p>'),
('<a class="tbtn white" href="#contacto">Únete al piloto</a><button class="tbtn outline" type="button" data-open-assistant>Pregunta al asistente</button>',
 '<a class="tbtn white" href="#contacto">Become a partner</a><button class="tbtn outline" type="button" data-open-assistant>Ask the assistant</button>'),
('<div class="cap">Qué consigues al unirte</div>', '<div class="cap">What partners get</div>'),
('<b>Calidad comparable entre tus clínicas</b><span>Indicadores homogéneos aunque cada clínica use un software distinto.</span>',
 '<b>One product for several markets</b><span>Built once, adapted to each country\'s language, data and law.</span>'),
('<b>IA sobre imágenes, sin mover radiografías</b><span>El algoritmo va al dato: aprendizaje federado y computación confidencial.</span>',
 '<b>AI on images, without moving X-rays</b><span>The algorithm goes to the data: federated learning and confidential computing.</span>'),
('<b>Preparado para el EHDS antes de 2029</b><span>Un espacio catalogado, listo para las solicitudes de los organismos de acceso.</span>',
 '<b>Ready for the EHDS before 2029</b><span>A catalogued space, ready for requests from health data access bodies.</span>'),
('<b>Acceso al área de socios</b><span>Demo en directo, evaluaciones técnicas y sesiones con nuestro equipo.</span>',
 '<b>Access to the partner area</b><span>Live demo, technical assessments and sessions with our team.</span>'),
('<h2>Lo más consultado</h2><p>El estudio, la presentación y los vídeos que más están descargando clínicas y socios.</p></div><a class="all" href="#preguntas">Ver preguntas frecuentes →</a>',
 '<h2>Most viewed</h2><p>The study, the presentation and the videos most downloaded by practices and partners.</p></div><a class="all" href="#preguntas">See the FAQ →</a>'),
('<span class="k">Estudio</span>', '<span class="k">Study</span>'),
('<span class="tag">Inglés</span><span class="tag">También en neerlandés</span><span class="tag">Directivos y técnicos</span>',
 '<span class="tag">English</span><span class="tag">Also in Dutch</span><span class="tag">Executives and technical teams</span>'),
('<h3>Espacios de datos de salud dental en Europa</h3>', '<h3>Dental health data spaces in Europe</h3>'),
('<p>Estudio comparativo de España, Bélgica, Países Bajos, Dinamarca y Alemania: sistema sanitario, mercado, infraestructura digital y adaptación al EHDS.</p>',
 '<p>Comparative study of Spain, Belgium, the Netherlands, Denmark and Germany: health system, market, digital infrastructure and EHDS adaptation.</p>'),
('rel="noopener">Descargar en inglés →</a>', 'rel="noopener">Download in English →</a>'),
('rel="noopener" lang="nl">Descargar en neerlandés →</a>', 'rel="noopener" lang="nl">Download in Dutch →</a>'),
('<span>Noviembre de 2026</span>', '<span>November 2026</span>'),
('<span class="k">Vídeo</span>', '<span class="k">Video</span>'),
('<span class="tag">11 min 35 s</span><span class="tag">Inglés</span><span class="tag">Presentadores generados con IA</span>',
 '<span class="tag">11 min 35 s</span><span class="tag">English</span><span class="tag">AI-generated presenters</span>'),
('<h3>Dental Data: la oportunidad invisible de Europa</h3>', '<h3>Dental Data: Europe\'s invisible opportunity</h3>'),
('<p>Sarah (Madrid) y James (Ámsterdam) repasan el estudio: el problema, cinco países, la propuesta y la hoja de ruta.</p>',
 '<p>Sarah (Madrid) and James (Amsterdam) walk through the study: the problem, five countries, the proposal and the roadmap.</p>'),
('aria-controls="yt1">Ver el vídeo aquí →</button>', 'aria-controls="yt1">Watch the video here →</button>'),
('<span>Noviembre de 2026 · Se carga desde YouTube solo al pulsar</span>', '<span>November 2026 · Loads from YouTube only when you click</span>'),
('<span class="k">Presentación</span>', '<span class="k">Presentation</span>'),
('<span class="tag">PDF · 32 diapositivas</span><span class="tag">Inglés</span><span class="tag">España y Países Bajos</span>',
 '<span class="tag">PDF · 32 slides</span><span class="tag">English</span><span class="tag">Spain and the Netherlands</span>'),
('<h3>Un espacio de datos dental, dos mercados</h3>', '<h3>One dental data space, two markets</h3>'),
('<p>La propuesta de Dental Data para España y Países Bajos dentro del Espacio Europeo de Datos de Salud, con la hoja de ruta hasta 2029.</p>',
 '<p>The Dental Data proposal for Spain and the Netherlands within the European Health Data Space, with the roadmap to 2029.</p>'),
('rel="noopener">Descargar la presentación →</a>', 'rel="noopener">Download the presentation →</a>'),
# ---- solución ----
('<div class="eyebrow">La solución</div><h2>Un espacio de datos federado: los datos nunca salen de la clínica</h2><p>Clínicas, cadenas y aseguradoras conservan sus expedientes. Solo se mueven consentimientos, metadatos y resultados agregados. El espacio se convierte en el interlocutor natural de los organismos de acceso a datos de salud.</p>',
 '<div class="eyebrow">The solution</div><h2>A federated data space: data never leaves the practice</h2><p>Practices, chains and insurers keep their records. Only consents, metadata and aggregated results move. The space becomes the natural counterpart of the health data access bodies.</p>'),
('<h3>Casos de uso con ingresos recurrentes</h3>', '<h3>Use cases with recurring revenue</h3>'),
('<b style="color:#fff">Indicadores de calidad</b> entre clínicas del mismo grupo: el primer caso de uso, aplicable desde hoy.',
 '<b style="color:#fff">Quality indicators</b> across practices of the same group: the first use case, available today.'),
('<b style="color:#fff">IA sobre imágenes dentales</b>, sin mover una sola radiografía. Nuestro modelo de caries interproximal y pérdida ósea periodontal está en fase de validación clínica.',
 '<b style="color:#fff">AI on dental images</b>, without moving a single X-ray. Our model for interproximal caries and periodontal bone loss is in clinical validation.'),
('<b style="color:#fff">Evidencia para la industria</b> sobre implantes y materiales.', '<b style="color:#fff">Evidence for industry</b> on implants and materials.'),
('<b style="color:#fff">Nunca para publicidad</b>: el EHDS lo prohíbe.', '<b style="color:#fff">Never for advertising</b>: the EHDS prohibits it.'),
('<h3>La ventana de oportunidad</h3>', '<h3>The window of opportunity</h3>'),
('<span>Cada país habrá designado sus organismos de acceso a datos de salud</span>', '<span>Every Member State will have designated its health data access bodies</span>'),
('<span>Entra en vigor la mayor parte de las normas de uso secundario</span>', '<span>Most secondary use rules apply</span>'),
('<span>Se incorporan las imágenes médicas: radiografías, ortopantomografías y TC de haz cónico</span>', '<span>Medical images are added: X-rays, panoramic radiographs and cone-beam CT</span>'),
('<p style="margin-top:16px">Quien tenga en 2029 un espacio de datos dental en funcionamiento será el socio natural de los reguladores.</p>',
 '<p style="margin-top:16px">Whoever has a working dental data space in 2029 will be the natural partner of regulators.</p>'),
# ---- tecnología ----
('<div class="eyebrow">Tecnología y experiencia</div><h2>Estándares abiertos europeos, ya probados en tres espacios de datos reales</h2><p>Un conector sobre Microsoft Azure, integrado en el software de gestión de la clínica. Formato europeo de historia clínica y metadatos comunes, adaptados a cada mercado.</p>',
 '<div class="eyebrow">Technology and experience</div><h2>Open European standards, already proven in three real data spaces</h2><p>A connector on Microsoft Azure, integrated with the practice management software. European health record format and common metadata, adapted to each market.</p>'),
('<h3>Soberanía</h3><p>La clínica decide quién accede, para qué y durante cuánto tiempo.</p>', '<h3>Sovereignty</h3><p>The practice decides who gets access, for what and for how long.</p>'),
('<h3>Contratos ODRL</h3><p>Condiciones de uso que hace cumplir la máquina. Sin contrato, no hay acceso.</p>', '<h3>ODRL contracts</h3><p>Usage conditions enforced by the machine. No contract, no access.</p>'),
('<h3>Gaia-X e IDSA</h3><p>Credenciales verificables, Dataspace Protocol, Eclipse EDC, FHIR, DICOM y HealthDCAT-AP.</p>', '<h3>Gaia-X and IDSA</h3><p>Verifiable credentials, Dataspace Protocol, Eclipse EDC, FHIR, DICOM and HealthDCAT-AP.</p>'),
('<h3>IA sin mover datos</h3><p>Aprendizaje federado y computación confidencial: el algoritmo va al dato.</p>', '<h3>AI without moving data</h3><p>Federated learning and confidential computing: the algorithm goes to the data.</p>'),
('<div class="num">SALUD</div><h3>Global Data Care</h3><p>Espacio de datos de salud federado sobre Gaia-X y Pontus-X.</p>', '<div class="num">HEALTH</div><h3>Global Data Care</h3><p>Federated health data space on Gaia-X and Pontus-X.</p>'),
('<div class="num">COMPRAS</div><h3>PROCUREDATA</h3><p>Espacio de datos federado para contratación pública y compras.</p>', '<div class="num">PROCUREMENT</div><h3>PROCUREDATA</h3><p>Federated data space for public procurement and purchasing.</p>'),
('<div class="num">ECONOMÍA CIRCULAR</div><h3>EcoDataNet</h3><p>Espacio de datos para residuos y economía circular.</p>', '<div class="num">CIRCULAR ECONOMY</div><h3>EcoDataNet</h3><p>Data space for waste and the circular economy.</p>'),
('<p class="pcap">Tres demostradores diseñados y ejecutados entre 2024 y 2026 con financiación de la SEDIA (Secretaría de Estado de Digitalización e Inteligencia Artificial). <a href="https://datos.softwareinabox.eu/">Más sobre nuestros espacios de datos</a></p>',
 '<p class="pcap">Three demonstrators designed and delivered between 2024 and 2026 with funding from SEDIA, Spain\'s Secretariat of State for Digitalisation and Artificial Intelligence. <a href="https://datos.softwareinabox.eu/">More about our data spaces</a></p>'),
# ---- preguntas ----
('<div class="eyebrow">Preguntas frecuentes</div><h2>Lo que más nos preguntan</h2><p>Si no encuentras tu respuesta, pregunta al asistente o escríbenos.</p>',
 '<div class="eyebrow">FAQ</div><h2>What people ask us most</h2><p>If you cannot find your answer, ask the assistant or write to us.</p>'),
# ---- pie ----
('<a class="flogo" href="/es/" aria-label="Dental Data, inicio">', '<a class="flogo" href="/en/" aria-label="Dental Data, home">'),
('<div><h4>Dental Data</h4><a href="#solucion">Cómo funciona</a><a href="#casos">Casos de uso</a><a href="#tecnologia">Tecnología</a><a href="#para-quien">Hoja de ruta</a></div>',
 '<div><h4>Dental Data</h4><a href="#solucion">How it works</a><a href="#casos">Use cases</a><a href="#tecnologia">Technology</a><a href="#para-quien">Roadmap</a></div>'),
('<div><h4>Para quién</h4><a href="#para-quien">Cadenas dentales</a><a href="#para-quien">Aseguradoras</a><a href="#para-quien">Clínicas independientes</a><a href="#para-quien">Software e industria</a></div>',
 '<div><h4>Markets</h4><a href="/es/" lang="es">España</a><a href="/nl/" lang="nl">Nederland</a><a href="/nl-be/" lang="nl">België</a><a href="/fr-be/" lang="fr">Belgique</a><a href="/de/" lang="de">Deutschland</a><a href="/da/" lang="da">Danmark</a><a href="#mercados">France · Italy · Portugal</a></div>'),
('<div><h4>Recursos</h4><a href="/docs/dental-health-data-spaces-europe-ehds.pdf">Estudio comparativo (EN)</a><a href="/docs/dental-data-es-nl-presentation-en.pdf">Presentación (EN)</a><a href="#destacados">Vídeos</a><a href="#preguntas">Preguntas frecuentes</a></div>',
 '<div><h4>Resources</h4><a href="/docs/dental-health-data-spaces-europe-ehds.pdf">Comparative study</a><a href="/docs/dental-data-es-nl-presentation-en.pdf">Presentation</a><a href="#destacados">Videos</a><a href="#preguntas">FAQ</a></div>'),
('<div><h4>Software in a Box</h4><a href="https://www.softwareinabox.eu/">Inicio</a><a href="https://datos.softwareinabox.eu/">Espacios de datos</a>',
 '<div><h4>Software in a Box</h4><a href="https://www.softwareinabox.eu/en/">Home</a><a href="https://datos.softwareinabox.eu/en/">Data spaces</a>'),
('<a href="https://cognitiv.softwareinabox.eu/">COGNITIV</a><a href="https://argos.softwareinabox.eu/">ARGOS</a></div>',
 '<a href="https://cognitiv.softwareinabox.eu/en/">COGNITIV</a><a href="https://argos.softwareinabox.eu/en/">ARGOS</a></div>'),
('<div><h4>Contacto</h4><a href="#contacto">Únete al piloto</a>', '<div><h4>Contact</h4><a href="#contacto">Become a partner</a>'),
('<a href="/nl/" lang="nl">Partnerprogramma Nederland</a></div>', '<a href="/nl/" lang="nl">Partnerprogramma Nederland</a></div>'),
('stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.8 2.5 15.2 0 18M12 3c-2.5 2.8-2.5 15.2 0 18"/></svg>Español (España)</span>',
 'stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.8 2.5 15.2 0 18M12 3c-2.5 2.8-2.5 15.2 0 18"/></svg>English (Europe)</span>'),
('<a href="https://www.softwareinabox.eu/aviso-legal.html">Aviso legal</a><a href="https://www.softwareinabox.eu/privacidad.html">Privacidad</a><a href="https://www.softwareinabox.eu/cookies.html">Cookies</a>',
 '<a href="https://www.softwareinabox.eu/en/aviso-legal.html">Legal notice</a><a href="https://www.softwareinabox.eu/en/privacidad.html">Privacy</a><a href="https://www.softwareinabox.eu/en/cookies.html">Cookies</a>'),
('<span>Microsoft y Azure son marcas de Microsoft Corporation.</span>', '<span>Microsoft and Azure are trademarks of Microsoft Corporation.</span>'),
('<span class="copy">© 2026 Software in a Box · Madrid · Bruselas</span>', '<span class="copy">© 2026 Software in a Box · Madrid · Brussels</span>'),
# ---- asistente: ventana ----
('aria-label="Abrir el asistente de Dental Data"', 'aria-label="Open the Dental Data assistant"'),
(' Asistente Dental Data <span class="pl"', ' Dental Data assistant <span class="pl"'),
('<b id="ph-t">Asistente Dental Data</b><small>Con IA, basado en nuestra documentación · <a href="https://www.softwareinabox.eu/privacidad.html" target="_blank" rel="noopener">Privacidad</a></small>',
 '<b id="ph-t">Dental Data assistant</b><small>AI-powered, based on our documentation · <a href="https://www.softwareinabox.eu/en/privacidad.html" target="_blank" rel="noopener">Privacy</a></small>'),
('aria-label="Cerrar el asistente"', 'aria-label="Close the assistant"'),
('aria-label="Nueva conversación"', 'aria-label="New conversation"'),
('<label class="sr" for="pq">Escribe tu pregunta</label>', '<label class="sr" for="pq">Type your question</label>'),
('placeholder="Escribe tu pregunta…"', 'placeholder="Type your question…"'),
('<button type="submit" aria-label="Enviar">', '<button type="submit" aria-label="Send">'),
# ---- asistente: código ----
("f.title='Dental Data: la oportunidad invisible de Europa'", "f.title='Dental Data: Europe\\'s invisible opportunity'"),
("bot(['¡Hola! Soy el asistente de Dental Data. Te explico cómo funciona el espacio de datos dental, el piloto en España y el Espacio Europeo de Datos de Salud.','Elige una pregunta o escribe la tuya. Por favor, no escribas datos personales ni de pacientes: guardamos de forma anónima las preguntas y respuestas para mejorar el asistente.'],['datos','cadena','ehds','ia','piloto'],true)",
 "bot(['Hello! I am the Dental Data assistant. I can explain how the federated dental data space works, where we are in Europe and what the European Health Data Space means for dental care.','Pick a question or type your own. Please do not enter personal or patient data: we store questions and answers anonymously to improve the assistant.'],['datos','paises','ehds','ia','partner'],true)"),
('<em style="font-style:normal">Respuesta preparada</em>', '<em style="font-style:normal">Prepared answer</em>'),
('<em style="font-style:normal">Respuesta generada por IA</em>', '<em style="font-style:normal">AI-generated answer</em>'),
('aria-label="Respuesta útil"', 'aria-label="Helpful answer"'),
('aria-label="Respuesta no útil"', 'aria-label="Unhelpful answer"'),
("'Todavía no tengo una respuesta preparada para eso. Puedes <a href=\"#contacto\" data-close>escribirnos</a> y te contestará una persona del equipo.'",
 "'I do not have a prepared answer for that yet. You can <a href=\"#contacto\" data-close>write to us</a> and someone from the team will reply.'"),
("['datos','ehds','piloto','tecnologia']", "['datos','ehds','partner','tecnologia']"),
("idioma:'es',pais:'es'", "idioma:'en',pais:'eu'"),
("fu.innerHTML='Fuente: '", "fu.innerHTML='Source: '"),
("var FUENTES={'01-que-es-dental-data.md':'Qué es Dental Data','02-mercado-espana.md':'El mercado español','03-solucion-casos-uso.md':'Solución y casos de uso','04-ehds-normativa.md':'EHDS y normativa','05-tecnologia.md':'Tecnología','06-piloto-hoja-ruta.md':'Piloto y hoja de ruta','07-europa-paises-bajos.md':'Países Bajos y Europa','08-empresa-recursos.md':'Software in a Box','09-preguntas-frecuentes.md':'Preguntas frecuentes','10-estudio-comparativo-en.md':'Estudio comparativo (PDF)','11-ehds-europa.md':'El EEDS en Europa'}",
 "var FUENTES={'01-que-es-dental-data.md':'What Dental Data is','03-solucion-casos-uso.md':'Solution and use cases','05-tecnologia.md':'Technology','07-europa-paises-bajos.md':'The Netherlands and Europe','08-empresa-recursos.md':'Software in a Box','10-estudio-comparativo-en.md':'Comparative study (PDF)','11-ehds-europa.md':'The EHDS in Europe','pais/europa.md':'Dental Data in Europe'}"),
]

PRES = "en"
VIDEOS_LANG = "en"
