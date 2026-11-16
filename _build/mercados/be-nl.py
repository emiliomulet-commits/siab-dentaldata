# Dental Data België (Nederlands) · https://dentaldata.softwareinabox.eu/nl-be/
# Markt «be»: institutionele alliantie (Health Data Agency, RIZIV, ziekenfondsen, beroepsverenigingen), geen pilootoproep.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "idiomas"))
from _mercado import desde_claves

SALIDA = "nl-be/index.html"
LANG = "nl-BE"
IDIOMA_COMUN = "nl"
SIAB = "nl-be"
PERMITIDO = ['lang="es"', "Español", "España"]

JSONLD = r'''
{"@context":"https://schema.org","@graph":[
{"@type":"WebPage","@id":"https://dentaldata.softwareinabox.eu/nl-be/#webpage","url":"https://dentaldata.softwareinabox.eu/nl-be/","name":"Dental Data België · Gefedereerde tandheelkundige dataruimte","inLanguage":"nl-BE","isPartOf":{"@type":"WebSite","@id":"https://www.softwareinabox.eu/#website","name":"Software in a Box"},"publisher":{"@type":"Organization","@id":"https://www.softwareinabox.eu/#organization","name":"Software in a Box","url":"https://www.softwareinabox.eu/"},"areaServed":"BE"},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Verlaten mijn gegevens de praktijk?","acceptedAnswer":{"@type":"Answer","text":"Nee. De dossiers blijven in de software van elke praktijk, keten of verzekeraar. Alleen toestemmingen, metadata en geaggregeerde resultaten worden gedeeld, onder gebruikscontracten die de machine afdwingt."}},
{"@type":"Question","name":"Wat voegt Dental Data toe aan de gegevens van het RIZIV?","acceptedAnswer":{"@type":"Answer","text":"De facturatie aan het RIZIV en de ziekenfondsen levert gestructureerde gegevens over vergoede prestaties. Het volledige dossier en de niet-vergoede behandelingen blijven in de praktijksoftware. Dental Data maakt dat deel zichtbaar zonder het te centraliseren."}},
{"@type":"Question","name":"Wat betekent de EHDS voor de tandzorg in België?","acceptedAnswer":{"@type":"Answer","text":"De Health Data Agency (opgericht in 2023) zal naar verwachting het coördinerende toegangsorgaan worden. Tegen 26 maart 2027 wijst elke lidstaat zijn toegangsorganen aan; vanaf 26 maart 2029 gelden de meeste regels voor secundair gebruik; vanaf 2031 komen medische beelden erbij."}}
]}]}
'''

KB_JS = r'''[
{id:'datos',q:'Verlaten mijn gegevens de praktijk?',k:['verlaten','verplaatst','centraal','opgeslagen','waar','cloud','server','privacy','kopie','delen'],
 a:['Nee. De dossiers blijven in de praktijksoftware van elke praktijk, keten of verzekeraar. Dental Data is een <b>gefedereerde</b> dataruimte: alleen toestemmingen, metadata en geaggregeerde resultaten worden gedeeld.','Elke toegang wordt geregeld door een ODRL-contract dat de machine afdwingt: de praktijk beslist wie toegang krijgt, waarvoor en hoe lang. Geen contract, geen toegang.'],s:['ia','seguridad']},
{id:'riziv',q:'Wat voegt het toe aan de gegevens van het RIZIV?',k:['riziv','inami','ziekenfonds','mutualiteit','vergoed','terugbetaal','facturatie','nomenclatuur','conventie','akkoord'],
 a:['De facturatie aan het RIZIV en de ziekenfondsen levert goed gestructureerde gegevens over <b>vergoede</b> prestaties. Het RIZIV betaalde in 2025 zo\'n 1,6 miljard euro terug voor tandzorg, meer dan 50 % meer dan in 2021, terwijl het aantal behandelingen met 16 % steeg.','Wat ontbreekt: het volledige dossier en de niet-vergoede behandelingen, die in de software van elke praktijk blijven. Dental Data maakt dat deel zichtbaar zonder het te centraliseren, als aanvulling op het RIZIV, niet als concurrent.'],s:['hda','markt']},
{id:'hda',q:'Wat doet de Health Data Agency?',k:['health data agency','hda','ehds','toegangsorgaan','2027','2029','2031','wet','regelgeving','artikel 50','micro'],
 a:['De Health Data Agency werd opgericht bij de wet van 14 maart 2023 en ging op 17 januari 2024 van start. Ze beheert een nationale catalogus met meer dan 480 datasets en zal naar verwachting het <b>coördinerende toegangsorgaan</b> voor de EHDS worden; die aanwijzing wacht nog op interministeriële goedkeuring.','Belangrijke data: tegen <b>26 maart 2027</b> zijn de toegangsorganen aangewezen, vanaf <b>26 maart 2029</b> gelden de meeste regels voor secundair gebruik en vanaf <b>2031</b> komen medische beelden erbij. Artikel 50 stelt micro-ondernemingen, zoals de meeste praktijken, standaard vrij. Daarom is een geaggregeerd kanaal nodig, zoals de HDA zelf vraagt met intermediairs en betrouwbare gegevenshouders.'],s:['riziv','samenwerken']},
{id:'ia',q:'Hoe werkt AI op röntgenfoto\'s?',k:[' ai ','kunstmatige intelligentie','artificiële','röntgen','rontgen','beeld','cariës','caries','parodont','algoritme','model','federated'],
 a:['Met federated learning en confidential computing: <b>het algoritme gaat naar de gegevens</b>, niet andersom. Geen enkele röntgenfoto verlaat de praktijk.','Ons model voor approximale cariës en parodontaal botverlies wordt klinisch gevalideerd. Het ondersteunt de tandarts en vervangt zijn of haar diagnose niet.'],s:['datos','tecnologia']},
{id:'samenwerken',q:'Hoe kunnen wij samenwerken?',k:['samenwerk','partner','alliantie','deelnemen','meedoen','integrator','vereniging','keten','contact','piloot'],
 a:['In België zoeken we een <b>institutionele alliantie</b>: met de Health Data Agency, het RIZIV en de ziekenfondsen, de tweetalige beroepsverenigingen, tandheelkundige ketens en Azure-integratoren in Brussel en Vlaanderen. Er is nog geen piloot in België.','Software in a Box heeft een kantoor in Brussel, in de Europese wijk. Laat uw gegevens achter in het <a href="#contacto" data-close>contactformulier</a> of schrijf naar <a href="mailto:partners@softwareinabox.eu">partners@softwareinabox.eu</a>.'],s:['riziv','hda']},
{id:'markt',q:'Hoe ziet de Belgische tandheelkundige markt eruit?',k:['markt','belgië','belgie','tandartsen','aantal','keten','consolidatie','raad','cijfers'],
 a:['In 2023 waren er <b>8.479</b> actieve tandartsen in België, of 71,7 per 100.000 inwoners. De verplichte ziekteverzekering dekt 99 % van de inwoners en 60,48 % van de tandartsen trad toe tot het akkoord tandartsen-ziekenfondsen 2026-2027.','De consolidatie is recenter dan in Spanje of Nederland, maar staat op de agenda: de Raad van de Tandheelkunde bracht in november 2025 een advies uit over commerciële tandheelkundige ketens. De laatste nationale gegevensverzameling over mondgezondheid dateert van 2012-2014.'],s:['riziv','samenwerken']},
{id:'tecnologia',q:'Welke technologie gebruikt u? Wat is de rol van Microsoft?',k:['technolog','microsoft','azure','connector','standaard','gaia','idsa','eclipse','edc','fhir','dicom','ehealth','integra'],
 a:['Een connector op <b>Microsoft Azure</b>, met gegevens in de EU, geïntegreerd met de praktijksoftware.','De grenzen van de dataruimte gebruiken open Europese standaarden: Gaia-X, IDSA en het Dataspace Protocol, Eclipse EDC, FHIR, DICOM en HealthDCAT-AP. Zo kan iedereen aansluiten, ook zonder Microsoft.'],s:['samenwerken','datos']},
{id:'seguridad',q:'Voldoet het aan de AVG? Is het veilig?',k:['avg','gdpr','gegevensbescherming','privacy','veilig','beveilig','toestemming','juridisch','vertrouwelijk'],
 a:['Identificeerbare gegevens worden nooit gecentraliseerd: alleen geaggregeerde resultaten reizen, onder contract. Voor AI gebruiken we confidential computing.','Elk project wordt gedocumenteerd met de functionaris voor gegevensbescherming van de organisatie en een gegevensbeschermingseffectbeoordeling.'],s:['datos','hda']},
{id:'publicidad',q:'Worden de gegevens gebruikt voor reclame?',k:['reclame','marketing','verkopen','verkoop','commercieel'],
 a:['Nooit. De EHDS verbiedt uitdrukkelijk het gebruik van gezondheidsgegevens voor reclame.','De beoogde toepassingen zijn kwaliteit van zorg, AI op beelden en bewijs voor de industrie over implantaten en materialen.'],s:['datos','hda']},
{id:'experiencia',q:'Wie bent u en welke ervaring hebt u?',k:['wie','bedrijf','ervaring','software in a box','referentie','projecten','global data care','brussel'],
 a:['Software in a Box, met kantoren in Madrid en Brussel. Tussen 2024 en 2026 ontwierpen en realiseerden we drie demonstratoren van dataruimtes met financiering van het Spaanse staatssecretariaat voor Digitalisering en AI: <b>Global Data Care</b> (gezondheid), <b>PROCUREDATA</b> (inkoop) en <b>EcoDataNet</b> (circulaire economie).','Meer op <a href="https://datos.softwareinabox.eu/nl-be/">datos.softwareinabox.eu</a>.'],s:['tecnologia','samenwerken']},
{id:'documentos',q:'Waar kan ik de studie lezen?',k:['studie','document','pdf','download','rapport','presentatie','video','lezen'],
 a:['De vergelijkende studie van vijf markten, met een hoofdstuk over België, bestaat in het <a href="/docs/tandheelkundige-gezondheidsdataruimtes-europa-ehds.pdf" target="_blank" rel="noopener">Nederlands</a> en het <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">Engels</a>, samen met de presentatie en de volledige video.'],s:['markt','samenwerken']}
]'''

BLOQUES = {
"espana": r'''
<section class="s soft" id="markt"><div class="wrap">
 <div class="head"><div class="eyebrow">De Belgische markt</div><h2>Wat vergoed wordt, is zichtbaar. De rest staat in de praktijk.</h2><p>België heeft een betalersmodel: de best gestructureerde tandheelkundige gegevens ontstaan bij de facturatie aan de ziekenfondsen en het RIZIV. Waardevol voor het vergoedingsbeleid, maar zonder het volledige dossier en zonder de niet-vergoede behandelingen.</p></div>
 <div class="grid4">
  <div class="card"><div class="num">TANDARTSEN</div><h3 class="big">8.479</h3><p>actief in 2023, of 71,7 per 100.000 inwoners. Daarnaast 514 orthodontisten, 205 parodontologen en 452 mondhygiënisten.</p></div>
  <div class="card"><div class="num">VERGOEDING RIZIV</div><h3 class="big">€1,6 mld</h3><p>terugbetaald voor tandzorg in 2025, tegenover iets meer dan €1 miljard in 2021: +50 % bij 16 % meer behandelingen.</p></div>
  <div class="card"><div class="num">AKKOORD 2026-2027</div><h3 class="big">60,48 %</h3><p>van de tandartsen trad volledig of gedeeltelijk toe tot het akkoord tandartsen-ziekenfondsen.</p></div>
  <div class="card"><div class="num">MONDGEZONDHEID</div><h3 class="big">2012-2014</h3><p>laatste nationale gegevensverzameling over mondgezondheid. Sindsdien is er een epidemiologische lacune.</p></div>
 </div>
 <div class="grid2" style="margin-top:22px">
  <div class="card"><h3>De Health Data Agency zoekt de zelfstandige zorgverleners</h3><p>De HDA (wet van 14/03/2023, gestart op 17/01/2024) beheert een catalogus met meer dan 480 datasets en zal naar verwachting het coördinerende toegangsorgaan voor de EHDS worden. Ze erkent zelf dat ze de dialoog met zelfstandige zorgverleners en kleinere organisaties nog moet openen, en verkent intermediairs en betrouwbare gegevenshouders.</p></div>
  <div class="card"><h3>Ketens onder de aandacht van de beroepsregulator</h3><p>De consolidatie is recenter dan in Spanje of Nederland, maar de Raad van de Tandheelkunde bracht in november 2025 een advies uit over commerciële ketens. Transparantie over resultaten is een antwoord op dat debat. Het federale eHealth-platform en het interfederale actieplan 2026-2029 vormen de digitale basis.</p></div>
 </div>
 <p class="pcap">Bron: Software in a Box, <a href="/docs/tandheelkundige-gezondheidsdataruimtes-europa-ehds.pdf" target="_blank" rel="noopener">Tandheelkundige gezondheidsdataruimtes in Europa · Vergelijkende studie</a> (november 2026), met de daarin geciteerde bronnen (RIZIV, Council of European Dentists, Health Data Agency).</p>
</div></section>
''',
"para-quien": r'''
<section class="s soft" id="para-quien"><div class="wrap">
 <div class="head"><div class="eyebrow">Voor wie</div><h2>Een aanvulling op het RIZIV, geen concurrent</h2><p>De gefedereerde dataruimte vult aan wat vandaag buiten beeld blijft: de niet-vergoede behandelingen en het volledige dossier in de software van elke praktijk. Daarvoor zoeken we een institutionele alliantie, met de praktijken als eigenaar van hun gegevens.</p></div>
 <div class="grid4 who-grid">
  <div class="card"><div class="num">INSTELLINGEN</div><h3>Health Data Agency en RIZIV</h3><p>Een geaggregeerd kanaal naar de zelfstandige zorgverleners, als intermediair of betrouwbare gegevenshouder.</p></div>
  <div class="card"><div class="num">ZIEKENFONDSEN</div><h3>Bewijs over de uitgaven</h3><p>Begrijpen waarom de terugbetaling sneller stijgt dan het aantal behandelingen, per patiënt en per type zorg.</p></div>
  <div class="card"><div class="num">BEROEPSVERENIGINGEN</div><h3>Weinig administratieve last</h3><p>Zelfstandige praktijken nemen deel via hun vereniging, zonder zelf gegevenshouder te worden.</p></div>
  <div class="card"><div class="num">KETENS EN INTEGRATOREN</div><h3>Vergelijken en uitrollen</h3><p>Kwaliteitsindicatoren tussen praktijken voor ketens; Azure-integratoren in Brussel en Vlaanderen rollen de connector uit.</p></div>
 </div>
 <div class="head" style="margin-top:56px;margin-bottom:22px"><h2 style="font-size:28px">Roadmap</h2></div>
 <div class="flow">
  <div class="step"><div class="c">1</div><b>2027 · Dialoog</b><span>Gesprekken met de Health Data Agency, het RIZIV en de beroepsverenigingen; eerste piloten in Spanje en Nederland.</span></div>
  <div class="step"><div class="c">2</div><b>2027–2028 · Gezamenlijk project</b><span>Een project met de HDA en een groep praktijken of een keten, uitgerold door een lokale Azure-integrator.</span></div>
  <div class="step"><div class="c">3</div><b>Maart 2029 · Gecatalogiseerd</b><span>Een gecatalogiseerde tandheelkundige dataruimte, klaar voor toegangsaanvragen onder de EHDS.</span></div>
 </div>
 <div class="nl-band"><div><b>Ook in Nederland en Spanje</b><p>We bouwen één product voor heel Europa. In Nederland met een lokale technologiepartner, in Spanje met een piloot bij een keten of verzekeraar.</p></div><a href="/nl/" hreflang="nl-NL">Nederland →</a>&nbsp;&nbsp;<a href="/es/" lang="es" hreflang="es-ES">España →</a></div>
</div></section>
''',
"contacto": r'''
<section class="s cta" id="contacto"><div class="wrap">
 <h2>Wilt u met ons praten?</h2>
 <p>Vertel ons kort wie u bent. We stellen een gesprek voor in ons kantoor in Brussel of online, om te zien hoe Dental Data past bij uw organisatie.</p>
 <form class="cform" action="https://formsubmit.co/partners@softwareinabox.eu" method="POST">
  <input type="hidden" name="_subject" value="Dental Data · België [NL]">
  <input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="https://www.softwareinabox.eu/gracias.html">
  <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
  <label class="sr" for="f-n">Naam</label><input id="f-n" name="Naam" required placeholder="Voor- en achternaam" autocomplete="name">
  <label class="sr" for="f-o">Organisatie</label><input id="f-o" name="Organisatie" placeholder="Organisatie" autocomplete="organization">
  <label class="sr" for="f-p">Profiel</label><select id="f-p" class="full" name="Profiel"><option value="">Profiel van uw organisatie</option><option>Instelling of overheid</option><option>Ziekenfonds of verzekeraar</option><option>Beroepsvereniging</option><option>Tandheelkundige keten of groepspraktijk</option><option>Zelfstandige praktijk</option><option>Softwareleverancier of Microsoft-partner</option><option>Andere</option></select>
  <label class="sr" for="f-e">E-mail</label><input id="f-e" class="full" type="email" name="E-mail" required placeholder="Professioneel e-mailadres" autocomplete="email">
  <label class="sr" for="f-m">Bericht</label><textarea id="f-m" name="Bericht" placeholder="Waarover wilt u met ons praten?"></textarea>
  <label class="ok full"><input type="checkbox" name="Toestemming" value="Aanvaardt het privacybeleid" required><span>Ik heb het <a href="https://www.softwareinabox.eu/nl-be/privacidad.html" target="_blank" rel="noopener">privacybeleid</a> gelezen en aanvaard het. We gebruiken uw gegevens alleen om u te antwoorden.</span></label>
  <button type="submit">Verzenden</button>
 </form>
 <p style="font-size:15px;margin-top:18px">Of schrijf naar <a href="mailto:partners@softwareinabox.eu" style="color:#fff;font-weight:600">partners@softwareinabox.eu</a> · <a href="tel:+34601398868" style="color:#fff;font-weight:600">+34 601 398 868</a> · Brussel en Madrid</p>
</div></section>
''',
}

TEXTOS = {
"m000": "<title>Dental Data België · Gefedereerde tandheelkundige dataruimte voor de EHDS | Software in a Box</title>",
"m001": 'content="Dental Data is een gefedereerde tandheelkundige dataruimte op Microsoft Azure: het volledige dossier en de niet-vergoede zorg zichtbaar maken zonder gegevens te centraliseren. Een aanvulling op het RIZIV voor de EHDS."',
"m002": '<link rel="canonical" href="https://dentaldata.softwareinabox.eu/nl-be/">',
"m003": 'content="nl_BE"',
"m004": '<meta property="og:title" content="Dental Data België · Uw tandheelkundige dataruimte begint hier">',
"m005": 'content="Het RIZIV ziet wat vergoed wordt. Dental Data maakt de rest van het tandheelkundige dossier zichtbaar, zonder één dossier te verplaatsen."',
"m006": '<meta property="og:url" content="https://dentaldata.softwareinabox.eu/nl-be/">',
"m007": '<a class="brand" href="/nl-be/" aria-label="Dental Data België, home">',
"m015": '<ul id="m2"><li><a href="#para-quien">Instellingen</a></li><li><a href="#para-quien">Ziekenfondsen</a></li><li><a href="#para-quien">Beroepsverenigingen</a></li><li><a href="#para-quien">Ketens en integratoren</a></li></ul>',
"m017": '<li><a href="#destacados">Studie, presentatie en video\'s</a></li><li><a href="#markt">De Belgische markt</a></li><li><a href="#preguntas">Veelgestelde vragen</a></li><li><a href="https://datos.softwareinabox.eu/nl-be/">Onze dataruimtes</a></li>',
"m018": '<a class="tbtn white" href="#contacto">Praat met ons</a>\n  <button',
"m021": '<li><a href="/es/" hreflang="es-ES" lang="es">Español · España</a></li>',
"m027": '<a href="#solucion">Oplossing</a><a href="#para-quien">Voor wie</a><a href="#destacados">Bronnen</a><a href="#preguntas">Veelgestelde vragen</a><a href="#contacto">Praat met ons</a>',
"m028": '<div class="pre">België · Europese ruimte voor gezondheidsgegevens</div>',
"m029": '<h1 id="h1">Uw tandheelkundige dataruimte <em>begint hier</em></h1>',
"m030": '<p class="lead">Wat het RIZIV vergoedt, is al zichtbaar. Vraag hoe u de rest van het dossier in beeld brengt zonder dat één dossier de praktijk verlaat.</p>',
"m034": '<button class="chip" type="button" data-q="datos">Verlaten mijn gegevens de praktijk?</button>',
"m035": '<button class="chip" type="button" data-q="riziv">Wat voegt het toe aan het RIZIV?</button>',
"m036": '<button class="chip" type="button" data-q="hda">Wat doet de Health Data Agency?</button>',
"m037": '<button class="chip" type="button" data-q="ia">Hoe werkt AI op röntgenfoto\'s?</button>',
"m038": '<button class="chip" type="button" data-q="samenwerken">Hoe kunnen wij samenwerken?</button>',
"m039": '<p class="trust">Ervaring met <b>3 dataruimtes</b> met publieke financiering · Kantoor in <b>Brussel</b> · Connector op <b>Microsoft Azure</b> met gegevens in de EU</p>',
"m040": '<h2>Breng de onzichtbare helft van de tandzorg in beeld</h2>',
"m041": '<p>We zoeken partners voor een institutionele alliantie: de Health Data Agency, het RIZIV en de ziekenfondsen, beroepsverenigingen, ketens en Azure-integratoren.</p>',
"m042": '<a class="tbtn white" href="#contacto">Praat met ons</a><button class="tbtn outline" type="button" data-open-assistant>Vraag het de assistent</button>',
"m043": '<div class="cap">Wat de alliantie oplevert</div>',
"m044": '<b>Het volledige dossier, niet alleen de factuur</b><span>Ook de niet-vergoede zorg, zonder gegevens te centraliseren.</span>',
"m045": '<b>Actuele gegevens over mondgezondheid</b><span>Sinds 2014 is er geen nationale gegevensverzameling meer geweest.</span>',
"m046": '<b>Weinig last voor zelfstandige praktijken</b><span>Eén geaggregeerd kanaal naar de Health Data Agency.</span>',
"m047": '<b>Transparantie voor ketens</b><span>Vergelijkbare kwaliteitsindicatoren tussen praktijken.</span>',
"m088": '<a class="flogo" href="/nl-be/" aria-label="Dental Data België, home">',
"m090": '<div><h4>Landen</h4><a href="/nl/">Nederland</a><a href="/fr-be/" lang="fr">Belgique (français)</a><a href="/de/" lang="de">Deutschland</a><a href="/">Alle landen</a></div>',
"m094": '<div><h4>Contact</h4><a href="#contacto">Praat met ons</a>',
"m095": '<a href="/en/" lang="en">Dental Data Europe</a></div>',
"m096": 'stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.8 2.5 15.2 0 18M12 3c-2.5 2.8-2.5 15.2 0 18"/></svg>Nederlands (België)</span>',
"m109": "bot(['Hallo! Ik ben de assistent van Dental Data. Ik leg uit hoe de gefedereerde tandheelkundige dataruimte werkt, wat ze toevoegt aan de gegevens van het RIZIV en wat de Europese ruimte voor gezondheidsgegevens betekent voor de tandzorg in België.','Kies een vraag of typ uw eigen vraag. Vul geen persoonsgegevens of patiëntgegevens in: we bewaren vragen en antwoorden anoniem om de assistent te verbeteren.'],['datos','riziv','hda','ia','samenwerken'],true)",
"m115": "['datos','hda','samenwerken','tecnologia']",
"m116": "idioma:'nl',pais:'be'",
"m118": "var FUENTES={'01-que-es-dental-data.md':'Wat Dental Data is','03-solucion-casos-uso.md':'Oplossing en toepassingen','05-tecnologia.md':'Technologie','08-empresa-recursos.md':'Software in a Box','10-estudio-comparativo-en.md':'Vergelijkende studie (PDF)','11-ehds-europa.md':'De EHDS in Europa','pais/be.md':'Dental Data in België'}",
}

REEMPLAZOS = desde_claves(TEXTOS) + [
('<li><a href="/nl-be/" hreflang="nl-BE" lang="nl">Nederlands · België</a></li>', '<li><a href="/nl-be/" hreflang="nl-BE" lang="nl" aria-current="page">Nederlands · België</a></li>'),
]
