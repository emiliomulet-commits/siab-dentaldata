# Dental Data Nederland · https://dentaldata.softwareinabox.eu/nl/
# Markt «nl»: Nederlandse technologiepartner + tandartsketen voor een pilot vóór maart 2027 (vervangt de handmatige pagina,
# gearchiveerd in _archivo/nl-manual/).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "idiomas"))
from _mercado import desde_claves

SALIDA = "nl/index.html"
LANG = "nl-NL"
IDIOMA_COMUN = "nl"
SIAB = "nl"
PERMITIDO = ['lang="es"', "Español", "España"]
PRES = "nl"
VIDEOS_LANG = "nl"

JSONLD = r'''
{"@context":"https://schema.org","@graph":[
{"@type":"WebPage","@id":"https://dentaldata.softwareinabox.eu/nl/#webpage","url":"https://dentaldata.softwareinabox.eu/nl/","name":"Dental Data · federatieve dataruimte voor mondzorg","inLanguage":"nl-NL","isPartOf":{"@type":"WebSite","@id":"https://www.softwareinabox.eu/#website","name":"Software in a Box"},"publisher":{"@type":"Organization","@id":"https://www.softwareinabox.eu/#org","name":"Software in a Box","url":"https://www.softwareinabox.eu/"}},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Is Dental Data een alternatief voor de LSP of de Wegiz?","acceptedAnswer":{"@type":"Answer","text":"Nee. Dental Data vervangt de LSP, de LDN of de Wegiz-standaarden niet. Het voegt toe wat ontbreekt: klinische data uit de mondzorgpraktijk, met een catalogus in HealthDCAT-AP die aansluit op de toekomstige Gezondheidsdata-autoriteit."}},
{"@type":"Question","name":"Wat betekent de Wet GIS voor praktijken?","acceptedAnswer":{"@type":"Answer","text":"De Wet GIS is een wetsvoorstel dat één Gezondheidsdata-autoriteit opricht, met een eerste fase in 2027, het toegangsorgaan operationeel in 2029 en volledige toepassing in 2031. De internetconsultatie liep tot 8 juli 2026."}},
{"@type":"Question","name":"Mogen de gegevens gebruikt worden voor premies of polisvoorwaarden?","acceptedAnswer":{"@type":"Answer","text":"Nee. De EHDS verbiedt het gebruik van gezondheidsgegevens voor reclame en voor beslissingen die mensen benadelen, ook in verzekeringen."}}
]}]}
'''

KB_JS = r'''[
{id:'datos',q:'Verlaten mijn gegevens de praktijk?',k:['verlaten','verplaats','centraal','opgeslagen','waar','server','kopie','delen'],
 a:['Nee. De dossiers blijven in de praktijksoftware van elke praktijk, keten of zorgverzekeraar. Dental Data is een <b>federatieve</b> dataruimte: alleen toestemmingen, metadata en geaggregeerde resultaten gaan over het netwerk.','Elke toegang wordt geregeld door een ODRL-contract dat de machine zelf afdwingt: de praktijk beslist wie toegang krijgt, waarvoor en hoelang. Geen contract, geen toegang.'],s:['kimo','seguridad']},
{id:'kimo',q:'Hoe sluit het aan bij de KIMO-richtlijnen?',k:['kimo','richtlijn','kwaliteit','indicator','keten','vergelijk'],
 a:['De indicatoren worden gedefinieerd met verwijzing naar de richtlijnen van het KIMO en in elke praktijk berekend met dezelfde definitie, ook als elke praktijk andere software gebruikt.','Zo ziet de directie van een keten vergelijkbare resultaten van het hele netwerk, zonder dat er één dossier van plek verandert, en kan ze haar kwaliteit aantonen tegenover de NZa, de Tweede Kamer en de zorgverzekeraars.'],s:['verzekeraar','samenwerken']},
{id:'verzekeraar',q:'Wat levert het een zorgverzekeraar op?',k:['zorgverzekeraar','verzekeraar','aanvullend','basisverzekering','polis','premie','gemeente','azwa'],
 a:['De zorgverzekeraar betaalt de mondzorg van jongeren in de basisverzekering en die van volwassenen in de aanvullende verzekeringen, maar kan de resultaten van honderden praktijken niet vergelijken.','Dental Data geeft samenhangende gegevens van het hele netwerk zonder dossiers te centraliseren. De EHDS verbiedt deze gegevens te gebruiken voor reclame of voor beslissingen die mensen benadelen, ook in verzekeringen.'],s:['kimo','datos']},
{id:'wetgis',q:'Wat verandert er met de Wet GIS?',k:['wet gis','gezondheidsdata-autoriteit','ehds','2027','2029','2031','toegangsorgaan','artikel 50','micro'],
 a:['De <b>Wet GIS</b> is een wetsvoorstel dat één <b>Gezondheidsdata-autoriteit</b> opricht: eerste fase in 2027, het toegangsorgaan operationeel in 2029 en volledige toepassing in 2031. De internetconsultatie liep tot 8 juli 2026.','De meeste praktijken zijn micro-ondernemingen en standaard vrijgesteld: om deel te nemen is een geaggregeerd kanaal nodig, via ketens, de KNMT of de zorgverzekeraars.'],s:['samenwerken','tecnologia']},
{id:'ia',q:'Hoe werkt AI op röntgenfoto\'s?',k:[' ai ','kunstmatige intelligentie','röntgen','beeld','cariës','parodont','algoritme','model','igj'],
 a:['Met federatief leren en vertrouwelijk rekenen: <b>het algoritme gaat naar de gegevens</b>, niet andersom. Geen enkele röntgenfoto verlaat de praktijk.','Ons model voor approximale cariës en parodontaal botverlies is in klinische validatie. Het ondersteunt de professional zonder de diagnose te vervangen. Toezicht op medische hulpmiddelen: IGJ.'],s:['datos','tecnologia']},
{id:'tecnologia',q:'Welke technologie gebruikt u?',k:['technolog','connector','standaard','gaia','idsa','eclipse','edc','fhir','dicom','snomed','nictiz','software','exquise','microsoft','azure'],
 a:['Een connector op <b>Microsoft Azure</b>, met de gegevens in de EU, naast de praktijksoftware. Terminologie in <b>SNOMED CT</b> (Nederlandse editie van Nictiz) en NZa-prestatiecodes voor activiteit.','Aan de grenzen van de ruimte: open Europese standaarden zoals Gaia-X, IDSA en het Dataspace Protocol, Eclipse EDC, FHIR, DICOM en HealthDCAT-AP. Iedereen kan aansluiten, ook zonder Microsoft.'],s:['samenwerken','wetgis']},
{id:'seguridad',q:'Is het AVG-proof?',k:['avg','gdpr','privacy','autoriteit persoonsgegevens','beveilig','toestemming','juridisch','wgbo','bewaar'],
 a:['Identificeerbare gegevens worden nooit gecentraliseerd: alleen geaggregeerde resultaten gaan over het netwerk, onder contract, binnen de AVG, de UAVG en de WGBO, onder toezicht van de Autoriteit Persoonsgegevens.','Dossiers worden volgens de WGBO 20 jaar bewaard; de catalogus vermeldt de beschikbare periode. Elk project wordt gedocumenteerd met een DPIA.'],s:['datos','wetgis']},
{id:'publicidad',q:'Worden de gegevens gebruikt voor reclame?',k:['reclame','marketing','verkopen','verkoop','commercieel','premie'],
 a:['Nooit. De EHDS verbiedt uitdrukkelijk het gebruik van gezondheidsgegevens voor reclame en voor beslissingen die mensen benadelen.','De toepassingen zijn de kwaliteit van zorg, AI op beelden en evidence voor de industrie over implantaten en materialen.'],s:['datos','verzekeraar']},
{id:'samenwerken',q:'Wat zoeken jullie in Nederland?',k:['partner','samenwerk','pilot','meedoen','keten','technologiepartner','contact','kosten'],
 a:['We zoeken een <b>Nederlandse technologiepartner</b>, bij voorkeur een partner van Microsoft Azure, om samen één product te bouwen voor Spanje en Nederland, en een <b>tandartsketen</b> voor een pilot met kwaliteitsindicatoren vóór maart 2027.','De eigen toepassing van de keten financiert de connector, en beide landen delen de kosten. We willen ook praten met zorgverzekeraars, leveranciers van praktijksoftware, het KIMO, Health-RI en de KNMT.'],s:['kimo','tecnologia']},
{id:'experiencia',q:'Wie zijn jullie en welke ervaring hebben jullie?',k:['wie','bedrijf','ervaring','software in a box','referentie','projecten','global data care'],
 a:['Software in a Box, met kantoren in Madrid en Brussel. Tussen 2024 en 2026 ontwierpen en realiseerden we drie demonstrators van dataruimtes, gefinancierd door het Spaanse staatssecretariaat voor Digitalisering en AI: <b>Global Data Care</b> (gezondheid), <b>PROCUREDATA</b> (inkoop) en <b>EcoDataNet</b> (circulaire economie).','Meer informatie over <a href="https://datos.softwareinabox.eu/nl/" target="_blank" rel="noopener">onze dataruimtes</a>.'],s:['tecnologia','samenwerken']},
{id:'documentos',q:'Waar kan ik de studie lezen?',k:['studie','document','pdf','download','rapport','presentatie','video','lezen'],
 a:['De vergelijkende Europese studie is beschikbaar in het <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">Engels</a> en het <a href="/docs/tandheelkundige-gezondheidsdataruimtes-europa-ehds.pdf" target="_blank" rel="noopener">Nederlands</a>, met de presentatie en de volledige video. De geanimeerde presentaties op deze pagina vatten elke vraag samen in minder dan een minuut.'],s:['datos','wetgis']}
]'''

BLOQUES = {
"espana": r'''
<section class="s soft" id="nederland"><div class="wrap">
 <div class="head"><div class="eyebrow">De Nederlandse markt</div><h2>De data bestaan, maar niemand verbindt ze</h2><p>Het KIMO publiceert richtlijnen en indicatoren, de NZa stelt de tarieven vast en de ketens groeien onder het oog van de Tweede Kamer. Maar er is geen circuit dat resultaten in de praktijk meet: elke praktijk bewaart haar gegevens in haar eigen software.</p></div>
 <div class="grid4">
  <div class="card"><div class="num">TANDARTSEN</div><h3 class="big">9 555</h3><p>tandartsen actief in januari 2025 (KNMT).</p></div>
  <div class="card"><div class="num">TOEGANG</div><h3 class="big">≈30 %</h3><p>van de praktijken neemt geen nieuwe patiënten aan (Rabobank).</p></div>
  <div class="card"><div class="num">PRIVATE EQUITY</div><h3 class="big">≈13 %</h3><p>van de praktijken in handen van private equity, goed voor ongeveer 30 % van de omzet.</p></div>
  <div class="card"><div class="num">AANVULLEND</div><h3 class="big">60 %</h3><p>van de bevolking heeft een aanvullende tandartsverzekering (Staat van de Mondzorg 2024).</p></div>
 </div>
 <div class="grid2" style="margin-top:22px">
  <div class="card"><h3>Twee regimes per leeftijd</h3><p>Jongeren onder de 18 zitten in de basisverzekering, volwassenen niet, op uitzonderingen na. 640.000 volwassenen mijden de tandarts om financiële redenen (VWS); de AZWA-pilot van 2 × 5,5 miljoen euro richt zich op mensen met een minimuminkomen.</p></div>
  <div class="card"><h3>Tarieven van de NZa</h3><p>Maximumtarieven voor alle patiënten; de verlaging van 2026 wordt door de KNMT aangevochten. In 2025 keurde de NZa 220 concentraties goed, en de mondzorg was de sector met de meeste.</p></div>
 </div>
 <p class="pcap">Bron: Software in a Box, <a href="/docs/tandheelkundige-gezondheidsdataruimtes-europa-ehds.pdf" target="_blank" rel="noopener">Tandheelkundige gezondheidsdataruimtes in Europa · Vergelijkende studie</a> (november 2026), hoofdstuk Nederland, en de daarin geciteerde bronnen (KNMT, NZa, VWS, Rabobank). Gegevens per november 2026.</p>
</div></section>
''',
"para-quien": r'''
<section class="s soft" id="para-quien"><div class="wrap">
 <div class="head"><div class="eyebrow">Voor wie</div><h2>Wat ontbreekt: klinische data uit de mondzorgpraktijk</h2><p>Dental Data vervangt de LSP, de LDN of de Wegiz-standaarden niet. Het voegt toe wat ontbreekt: klinische data uit de mondzorgpraktijk, met een catalogus in HealthDCAT-AP die aansluit op de toekomstige Gezondheidsdata-autoriteit.</p></div>
 <div class="grid4 who-grid">
  <div class="card"><div class="num">KETENS</div><h3>Aantoonbare kwaliteit</h3><p>Indicatoren met verwijzing naar het KIMO, tegenover de NZa, de Tweede Kamer en de zorgverzekeraars.</p></div>
  <div class="card"><div class="num">ZORGVERZEKERAARS</div><h3>Samenhangende gegevens</h3><p>Resultaten van gecontracteerde praktijken, voor de aanvullende verzekering en de jeugdzorg in de basisverzekering.</p></div>
  <div class="card"><div class="num">GEMEENTEN EN VWS</div><h3>Resultaten meten</h3><p>Indicatoren voor de AZWA-pilot en de gemeentepolis.</p></div>
  <div class="card"><div class="num">IT-PARTNERS</div><h3>De connector integreren</h3><p>Naast de praktijksoftware, uitgerold door Azure-partners.</p></div>
 </div>
 <div class="head" style="margin-top:56px;margin-bottom:22px"><h2 style="font-size:28px">Routekaart</h2></div>
 <div class="flow">
  <div class="step"><div class="c">1</div><b>Vóór maart 2027 · Pilot</b><span>Pilot met kwaliteitsindicatoren bij een tandartsketen, samen met een Nederlandse technologiepartner; eerste fase van de Wet GIS.</span></div>
  <div class="step"><div class="c">2</div><b>2027–2028 · Consolideren</b><span>Pilots consolideren in Spanje en Nederland en meedoen aan de consultaties.</span></div>
  <div class="step"><div class="c">3</div><b>Maart 2029 · Gecatalogiseerd</b><span>Een gecatalogiseerde dataruimte voor mondzorg, klaar voor de EHDS en de Gezondheidsdata-autoriteit. De Wet GIS is een wetsvoorstel; de consultatie liep tot 8 juli 2026.</span></div>
 </div>
 <div class="nl-band"><div><b>En in Spanje?</b><p>We bouwen hetzelfde product met een Spaanse partner: wat we leren met een keten in Madrid versnelt de pilot in Amsterdam, en omgekeerd.</p></div><a href="/es/" lang="es" hreflang="es-ES">España →</a>&nbsp;&nbsp;<a href="/nl-be/" hreflang="nl-BE">België →</a></div>
</div></section>
''',
"contacto": r'''
<section class="s cta" id="contacto"><div class="wrap">
 <h2>Partnerprogramma Nederland</h2>
 <p>We zoeken een Nederlandse technologiepartner en een tandartsketen voor de pilot. Vertel ons kort wie u bent; we stellen een gesprek voor, online of in Brussel.</p>
 <form class="cform" action="https://formsubmit.co/partners@softwareinabox.eu" method="POST">
  <input type="hidden" name="_subject" value="Dental Data · Nederland">
  <input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="https://www.softwareinabox.eu/gracias.html">
  <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
  <label class="sr" for="f-n">Naam</label><input id="f-n" name="Naam" required placeholder="Voor- en achternaam" autocomplete="name">
  <label class="sr" for="f-o">Organisatie</label><input id="f-o" name="Organisatie" placeholder="Organisatie" autocomplete="organization">
  <label class="sr" for="f-p">Profiel</label><select id="f-p" class="full" name="Profiel"><option value="">Profiel van uw organisatie</option><option>Technologiepartner of Microsoft-partner</option><option>Tandartsketen</option><option>Zorgverzekeraar</option><option>Praktijk</option><option>Leverancier van praktijksoftware</option><option>Instelling of overheid</option><option>Anders</option></select>
  <label class="sr" for="f-e">E-mail</label><input id="f-e" class="full" type="email" name="E-mail" required placeholder="Zakelijk e-mailadres" autocomplete="email">
  <label class="sr" for="f-m">Bericht</label><textarea id="f-m" name="Bericht" placeholder="Waarover wilt u met ons praten?"></textarea>
  <label class="ok full"><input type="checkbox" name="Toestemming" value="Gaat akkoord met het privacybeleid" required><span>Ik heb het <a href="https://www.softwareinabox.eu/nl/privacidad.html" target="_blank" rel="noopener">privacybeleid</a> gelezen en ga ermee akkoord. We gebruiken uw gegevens alleen om u te antwoorden.</span></label>
  <button type="submit">Versturen</button>
 </form>
 <p style="font-size:15px;margin-top:18px">Of schrijf naar <a href="mailto:partners@softwareinabox.eu" style="color:#fff;font-weight:600">partners@softwareinabox.eu</a> · <a href="tel:+34601398868" style="color:#fff;font-weight:600">+34 601 398 868</a> · Brussel en Madrid</p>
</div></section>
''',
}

TEXTOS = {
"m000": "<title>Dental Data · federatieve dataruimte voor mondzorg | Software in a Box</title>",
"m001": 'content="Dental Data is een federatieve dataruimte voor mondzorg op Microsoft Azure: kwaliteit aantonen zonder één dossier te verplaatsen, klaar voor de EHDS en de Gezondheidsdata-autoriteit. Partnerprogramma Nederland."',
"m002": '<link rel="canonical" href="https://dentaldata.softwareinabox.eu/nl/">',
"m003": 'content="nl_NL"',
"m004": '<meta property="og:title" content="Dental Data · Kwaliteit aantonen zonder één dossier te verplaatsen">',
"m005": 'content="Indicatoren worden in de praktijk berekend, alleen het resultaat reist. Partnerprogramma Nederland."',
"m006": '<meta property="og:url" content="https://dentaldata.softwareinabox.eu/nl/">',
"m007": '<a class="brand" href="/nl/" aria-label="Dental Data Nederland, home">',
"m015": '<ul id="m2"><li><a href="#para-quien">Ketens</a></li><li><a href="#para-quien">Zorgverzekeraars</a></li><li><a href="#para-quien">Gemeenten en VWS</a></li><li><a href="#para-quien">IT-partners</a></li></ul>',
"m017": '<li><a href="#destacados">Studie, presentatie en video\'s</a></li><li><a href="#nederland">De Nederlandse markt</a></li><li><a href="#preguntas">Veelgestelde vragen</a></li><li><a href="https://datos.softwareinabox.eu/nl/">Onze dataruimtes</a></li>',
"m018": '<a class="tbtn white" href="#contacto">Word partner</a>\n  <button',
"m021": '<li><a href="/es/" hreflang="es-ES" lang="es">Español · España</a></li>',
"m027": '<a href="#solucion">Oplossing</a><a href="#para-quien">Voor wie</a><a href="#destacados">Bronnen</a><a href="#preguntas">Veelgestelde vragen</a><a href="#contacto">Word partner</a>',
"m028": '<div class="pre">Nederland · Europese ruimte voor gezondheidsgegevens</div>',
"m029": '<h1 id="h1">Kwaliteit aantonen <em>zonder één dossier te verplaatsen</em></h1>',
"m030": '<p class="lead">Dental Data verbindt praktijken, ketens en zorgverzekeraars in een federatieve dataruimte: indicatoren worden in de praktijk berekend, alleen het resultaat reist.</p>',
"m034": '<button class="chip" type="button" data-q="kimo">Hoe sluit het aan bij het KIMO?</button>',
"m035": '<button class="chip" type="button" data-q="datos">Verlaten mijn gegevens de praktijk?</button>',
"m036": '<button class="chip" type="button" data-q="wetgis">Wat verandert er met de Wet GIS?</button>',
"m037": '<button class="chip" type="button" data-q="verzekeraar">Wat levert het een zorgverzekeraar op?</button>',
"m038": '<button class="chip" type="button" data-q="samenwerken">Wat zoeken jullie in Nederland?</button>',
"m039": '<p class="trust">Ervaring met <b>3 dataruimtes</b> met publieke financiering · Connector op <b>Microsoft Azure</b> met gegevens in de EU</p>',
"m040": '<h2>De kwaliteit van de mondzorg heeft richtlijnen. Ze mist data.</h2>',
"m041": '<p>We zoeken een Nederlandse technologiepartner, bij voorkeur Microsoft Azure-partner, en een tandartsketen voor een pilot met kwaliteitsindicatoren vóór maart 2027.</p>',
"m042": '<a class="tbtn white" href="#contacto">Word partner</a><button class="tbtn outline" type="button" data-open-assistant>Vraag het de assistent</button>',
"m043": '<div class="cap">Wat het oplevert</div>',
"m044": '<b>Vergelijkbare kwaliteit tussen praktijken</b><span>Indicatoren met verwijzing naar het KIMO, ook met verschillende software.</span>',
"m045": '<b>AI op beelden, zonder röntgenfoto\'s te verplaatsen</b><span>Het algoritme gaat naar de gegevens: federatief leren en vertrouwelijk rekenen.</span>',
"m046": '<b>Klaar voor de Gezondheidsdata-autoriteit</b><span>Een gecatalogiseerde ruimte, klaar voor de EHDS in 2029.</span>',
"m047": '<b>Eén product voor Spanje en Nederland</b><span>Wat we in Madrid leren, versnelt de pilot in Amsterdam.</span>',
"m088": '<a class="flogo" href="/nl/" aria-label="Dental Data Nederland, home">',
"m090": '<div><h4>Landen</h4><a href="/nl-be/">België</a><a href="/es/" lang="es">España</a><a href="/de/" lang="de">Deutschland</a><a href="/">Alle landen</a></div>',
"m094": '<div><h4>Contact</h4><a href="#contacto">Word partner</a>',
"m095": '<a href="/en/" lang="en">Dental Data Europe</a></div>',
"m096": 'stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.8 2.5 15.2 0 18M12 3c-2.5 2.8-2.5 15.2 0 18"/></svg>Nederlands (Nederland)</span>',
"m109": "bot(['Hallo! Ik ben de assistent van Dental Data. Ik leg uit hoe de federatieve dataruimte voor mondzorg werkt, hoe ze aansluit bij het KIMO en wat de Wet GIS en de EHDS betekenen voor de mondzorg in Nederland.','Kies een vraag of typ uw eigen vraag. Typ geen persoonsgegevens of patiëntgegevens: we bewaren vragen en antwoorden anoniem om de assistent te verbeteren.'],['kimo','datos','wetgis','verzekeraar','samenwerken'],true)",
"m115": "['datos','wetgis','samenwerken','tecnologia']",
"m116": "idioma:'nl',pais:'nl'",
"m118": "var FUENTES={'01-que-es-dental-data.md':'Wat Dental Data is','03-solucion-casos-uso.md':'Oplossing en toepassingen','05-tecnologia.md':'Technologie','07-europa-paises-bajos.md':'Nederland en Europa','08-empresa-recursos.md':'Software in a Box','10-estudio-comparativo-en.md':'Vergelijkende studie (pdf)','11-ehds-europa.md':'De EHDS in Europa','pais/nl.md':'Dental Data in Nederland'}",
}

REEMPLAZOS = desde_claves(TEXTOS) + [
('<li><a href="/nl/" hreflang="nl-NL" lang="nl">Nederlands · Nederland</a></li>', '<li><a href="/nl/" hreflang="nl-NL" lang="nl" aria-current="page">Nederlands · Nederland</a></li>'),
]
