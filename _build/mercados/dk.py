# Dental Data Danmark · https://dentaldata.softwareinabox.eu/da/
# Marked «dk»: institutionel alliance (Sundhedsdatastyrelsen, regionerne, Tandlægeforeningen), SCOR-logikken udvidet til voksne. Intet pilotopråb.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "idiomas"))
from _mercado import desde_claves

SALIDA = "da/index.html"
LANG = "da-DK"
IDIOMA_COMUN = "da"
SIAB = "da"
PERMITIDO = ['lang="es"', "Español", "España"]

JSONLD = r'''
{"@context":"https://schema.org","@graph":[
{"@type":"WebPage","@id":"https://dentaldata.softwareinabox.eu/da/#webpage","url":"https://dentaldata.softwareinabox.eu/da/","name":"Dental Data Danmark · Fødereret dentalt dataområde","inLanguage":"da-DK","isPartOf":{"@type":"WebSite","@id":"https://www.softwareinabox.eu/#website","name":"Software in a Box"},"publisher":{"@type":"Organization","@id":"https://www.softwareinabox.eu/#organization","name":"Software in a Box","url":"https://www.softwareinabox.eu/"},"areaServed":"DK"},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Forlader mine data klinikken?","acceptedAnswer":{"@type":"Answer","text":"Nej. Journalerne bliver i hver kliniks, kædes eller forsikringsselskabs eget system. Kun samtykker, metadata og aggregerede resultater deles, efter brugskontrakter som maskinen håndhæver."}},
{"@type":"Question","name":"Hvad tilfører Dental Data i forhold til SCOR?","acceptedAnswer":{"@type":"Answer","text":"SCOR har siden 1972 registreret børn og unges tandsundhed. For voksne, som behandles i private klinikker og kæder, findes der intet tilsvarende. Dental Data bringer samme logik til voksne uden at centralisere journaler."}},
{"@type":"Question","name":"Hvad betyder EHDS for tandplejen i Danmark?","acceptedAnswer":{"@type":"Answer","text":"Senest den 26. marts 2027 udpeger hver medlemsstat sine adgangsorganer for sundhedsdata; fra den 26. marts 2029 gælder de fleste regler for sekundær brug; fra 2031 kommer medicinske billeder med. I Danmark sker tilpasningen gennem Digital Sundhed Danmark og Sundhedsdatastyrelsen."}}
]}]}
'''

KB_JS = r'''[
{id:'datos',q:'Forlader mine data klinikken?',k:['forlad','flytte','central','gemt','hvor ligger','cloud','server','privatliv','kopi','dele'],
 a:['Nej. Journalerne bliver i hver kliniks, kædes eller forsikringsselskabs journalsystem. Dental Data er et <b>fødereret</b> dataområde: kun samtykker, metadata og aggregerede resultater deles.','Al adgang styres af en ODRL-kontrakt, som maskinen håndhæver: klinikken bestemmer, hvem der får adgang, til hvad og hvor længe. Ingen kontrakt, ingen adgang.'],s:['ia','seguridad']},
{id:'scor',q:'Hvad tilfører det i forhold til SCOR?',k:['scor','register','børn','unge','kommunal','børnetandpleje','voksne','voksen','synlig'],
 a:['Danmark er det eneste land i undersøgelsen med et nationalt register for mundsundhed: <b>SCOR</b>, Sundhedsstyrelsens Centrale Odontologiske Register, siden 1972. Kommunerne indberetter børn og unges undersøgelser, og registeret har gjort det muligt at følge mundsundheden i over 50 år.','For <b>voksne</b>, som behandles i private klinikker og kæder, findes der intet tilsvarende. Dental Data bringer SCOR-logikken til voksne med en fødereret, frivillig og aggregeret model, uden uforholdsmæssige byrder for de private klinikker.'],s:['ehds','marked']},
{id:'ehds',q:'Hvad betyder EHDS for tandplejen?',k:['ehds','sundhedsdataområde','adgangsorgan','sundhedsdatastyrelsen','digital sundhed','gateway','2027','2029','2031','lov','forordning','artikel 50','mikro'],
 a:['Siden 1. januar 2026 samler den forberedende enhed <b>Digital Sundhed Danmark</b> sundhed.dk, MedCom, Sundhedsdatastyrelsen og regionale it-opgaver. En <b>Health Data Gateway</b> med én indgang til registre, biobanker og kliniske data er under udvikling med 200 mio. kr. fra Novo Nordisk Fonden. Det formelle adgangsorgan er endnu ikke bekræftet.','Vigtige datoer: senest <b>26. marts 2027</b> er adgangsorganerne udpeget, fra <b>26. marts 2029</b> gælder de fleste regler for sekundær brug, og fra <b>2031</b> kommer medicinske billeder med, herunder røntgen og CBCT. Artikel 50 fritager som udgangspunkt mikrovirksomheder, som de fleste klinikker, og derfor er en aggregeret kanal nødvendig.'],s:['scor','samarbejde']},
{id:'ia',q:'Hvordan virker AI på røntgenbilleder?',k:[' ai ','kunstig intelligens','røntgen','billed','caries','karies','parodont','algoritme','model','fødereret'],
 a:['Med fødereret læring og fortrolig databehandling: <b>algoritmen går til dataene</b>, ikke omvendt. Intet røntgenbillede forlader klinikken.','Vores model for approksimal caries og parodontalt knogletab er i klinisk validering. Den støtter tandlægen og erstatter ikke diagnosen.'],s:['datos','tecnologia']},
{id:'samarbejde',q:'Hvordan kan vi samarbejde?',k:['samarbejd','partner','alliance','deltage','være med','integrator','forening','kæde','region','kontakt','pilot'],
 a:['I Danmark søger vi en <b>institutionel alliance</b>: projekter med Sundhedsdatastyrelsen eller regionerne, sammen med Tandlægeforeningen, tandlægekæderne og danske Azure-integratorer. Der er endnu ikke et pilotprojekt i Danmark.','Udfyld <a href="#contacto" data-close>kontaktformularen</a> eller skriv til <a href="mailto:partners@softwareinabox.eu">partners@softwareinabox.eu</a>.'],s:['scor','ehds']},
{id:'marked',q:'Hvordan ser det danske tandplejemarked ud?',k:['marked','danmark','tandlæger','antal','kæde','overenskomst','tilskud','forsikring','tal','tandplejer'],
 a:['I 2025 var der <b>4.964</b> aktive tandlæger, eller 83,2 pr. 100.000 indbyggere, og ifølge OECD er Danmark det eneste EU-land, hvor tandlægetætheden faldt. Børn og unge op til 21 år får gratis tandpleje; voksne får kun omkring 15 % i offentligt tilskud, og 42 % har en tillægsforsikring.','Voksentandplejen er privat og reguleret af tandlægeoverenskomsten, som begrænser kædernes ejerskab. Alligevel brugte hver tredje voksne en tandlægekæde i 2022.'],s:['scor','samarbejde']},
{id:'tecnologia',q:'Hvilken teknologi bruger I? Hvad er Microsofts rolle?',k:['teknologi','microsoft','azure','connector','standard','gaia','idsa','eclipse','edc','fhir','dicom','medcom','integration'],
 a:['En connector på <b>Microsoft Azure</b>, med data i EU, integreret i klinikkens journalsystem.','Dataområdets grænser bruger åbne europæiske standarder: Gaia-X, IDSA og Dataspace Protocol, Eclipse EDC, FHIR, DICOM og HealthDCAT-AP. Så kan alle koble sig på, også uden Microsoft.'],s:['samarbejde','datos']},
{id:'seguridad',q:'Overholder det GDPR? Er det sikkert?',k:['gdpr','databeskyttelse','privatliv','sikker','samtykke','juridisk','fortrolig'],
 a:['Identificerbare data centraliseres aldrig: kun aggregerede resultater deles, under kontrakt. Til AI bruger vi fortrolig databehandling.','Hvert projekt dokumenteres sammen med organisationens databeskyttelsesrådgiver og en konsekvensanalyse vedrørende databeskyttelse.'],s:['datos','ehds']},
{id:'publicidad',q:'Bliver data brugt til reklame?',k:['reklame','markedsføring','sælge','salg','kommerciel'],
 a:['Aldrig. EHDS forbyder udtrykkeligt brug af sundhedsdata til reklame.','De tilsigtede anvendelser er kvalitet i behandlingen, AI på billeder og evidens til industrien om implantater og materialer.'],s:['datos','ehds']},
{id:'experiencia',q:'Hvem er I, og hvilken erfaring har I?',k:['hvem','virksomhed','erfaring','software in a box','reference','projekter','global data care'],
 a:['Software in a Box med kontorer i Madrid og Bruxelles. Mellem 2024 og 2026 designede og gennemførte vi tre demonstratorer af dataområder, støttet af det spanske statssekretariat for digitalisering og AI: <b>Global Data Care</b> (sundhed), <b>PROCUREDATA</b> (indkøb) og <b>EcoDataNet</b> (cirkulær økonomi).','Læs mere på <a href="https://datos.softwareinabox.eu/da/">datos.softwareinabox.eu</a>.'],s:['tecnologia','samarbejde']},
{id:'documentos',q:'Hvor kan jeg læse undersøgelsen?',k:['undersøgelse','dokument','pdf','hent','rapport','præsentation','video','læse'],
 a:['Den sammenlignende undersøgelse af fem markeder, med et kapitel om Danmark, findes på <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">engelsk</a> og <a href="/docs/tandheelkundige-gezondheidsdataruimtes-europa-ehds.pdf" target="_blank" rel="noopener" lang="nl">nederlandsk</a>, sammen med præsentationen og den fulde video.'],s:['marked','samarbejde']}
]'''

BLOQUES = {
"espana": r'''
<section class="s soft" id="marked"><div class="wrap">
 <div class="head"><div class="eyebrow">Det danske marked</div><h2>Børnene er i registeret. De voksne er usynlige.</h2><p>Danmark har to systemer i tandplejen: gratis kommunal tandpleje for børn og unge, som registreres i SCOR, og en privat voksentandpleje med lavt offentligt tilskud, hvis data bliver i hver klinik og kæde.</p></div>
 <div class="grid4">
  <div class="card"><div class="num">TANDLÆGER</div><h3 class="big">4.964</h3><p>aktive i 2025, eller 83,2 pr. 100.000 indbyggere. Det eneste EU-land, hvor tætheden faldt ifølge OECD.</p></div>
  <div class="card"><div class="num">SCOR</div><h3 class="big">1972</h3><p>siden da har registeret fulgt børn og unges tandsundhed. Gratis tandpleje dækker nu 0-21-årige.</p></div>
  <div class="card"><div class="num">VOKSNE</div><h3 class="big">≈15 %</h3><p>offentligt tilskud til voksentandpleje; 42 % af befolkningen har en tillægsforsikring.</p></div>
  <div class="card"><div class="num">KÆDER</div><h3 class="big">1 ud af 3</h3><p>voksne brugte en tandlægekæde i 2022, trods overenskomstens ejerskabsbegrænsninger.</p></div>
 </div>
 <div class="grid2" style="margin-top:22px">
  <div class="card"><h3>Ny styring: Digital Sundhed Danmark</h3><p>Siden 1. januar 2026 samler den forberedende enhed sundhed.dk, MedCom, Sundhedsdatastyrelsen og regionale it-opgaver. En Health Data Gateway er under udvikling med 200 mio. kr. fra Novo Nordisk Fonden, og den formelle udpegning af adgangsorganet for sundhedsdata er endnu ikke bekræftet.</p></div>
  <div class="card"><h3>Kapacitet og differentiering</h3><p>Med faldende tandlægetæthed kræver produktivitet og opgavefordeling til tandplejere aktivitetsdata. Kæderne skal differentiere sig inden for rammer, der begrænser vækst gennem ejerskab. Begge dele kræver data om voksne.</p></div>
 </div>
 <p class="pcap">Kilde: Software in a Box, <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">Dental health data spaces in Europe · Sammenlignende undersøgelse</a> (november 2026), med de kilder der citeres i den (Sundhedsstyrelsen, Council of European Dentists, OECD, Sundhedsdatastyrelsen).</p>
</div></section>
''',
"para-quien": r'''
<section class="s soft" id="para-quien"><div class="wrap">
 <div class="head"><div class="eyebrow">For hvem</div><h2>SCOR-logikken, udvidet til de voksne</h2><p>I Danmark behøver ingen at blive overbevist om værdien af data om mundsundhed: SCOR har vist den i over 50 år. Dental Data bringer samme logik til voksne og private klinikker, med en fødereret model der passer til den nye styring.</p></div>
 <div class="grid4 who-grid">
  <div class="card"><div class="num">MYNDIGHEDER</div><h3>Sundhedsdatastyrelsen</h3><p>En frivillig, aggregeret kanal fra de private klinikker, kompatibel med Digital Sundhed Danmark og Health Data Gateway.</p></div>
  <div class="card"><div class="num">REGIONER</div><h3>Overblik over voksentandplejen</h3><p>Aktivitetsdata til planlægning af kapacitet og opgavefordeling, uden nye indberetningsbyrder.</p></div>
  <div class="card"><div class="num">TANDLÆGEFORENINGEN</div><h3>Klinikkerne bestemmer</h3><p>Private klinikker deltager frivilligt og beholder kontrollen over deres journaler.</p></div>
  <div class="card"><div class="num">KÆDER OG INTEGRATORER</div><h3>Sammenlign og udrul</h3><p>Kvalitetsindikatorer på tværs af klinikker for kæderne; danske Azure-integratorer udruller connectoren.</p></div>
 </div>
 <div class="head" style="margin-top:56px;margin-bottom:22px"><h2 style="font-size:28px">Køreplan</h2></div>
 <div class="flow">
  <div class="step"><div class="c">1</div><b>2027 · Dialog</b><span>Samtaler med Sundhedsdatastyrelsen, regionerne og Tandlægeforeningen; de første pilotprojekter i Spanien og Nederlandene.</span></div>
  <div class="step"><div class="c">2</div><b>2027–2028 · Fælles projekt</b><span>Et projekt med en region eller en kæde, udrullet af en dansk Azure-integrator.</span></div>
  <div class="step"><div class="c">3</div><b>Marts 2029 · Katalogiseret</b><span>Et katalogiseret dentalt dataområde, klar til adgangsansøgninger under EHDS.</span></div>
 </div>
 <div class="nl-band"><div><b>Også i resten af Europa</b><p>Vi bygger ét produkt til hele Europa og tilpasser det til hvert lands sprog, data og lovgivning.</p></div><a href="/en/" lang="en" hreflang="en">Europe →</a>&nbsp;&nbsp;<a href="/de/" lang="de" hreflang="de-DE">Deutschland →</a></div>
</div></section>
''',
"contacto": r'''
<section class="s cta" id="contacto"><div class="wrap">
 <h2>Vil du tale med os?</h2>
 <p>Fortæl os kort, hvem du er. Vi foreslår et møde for at se, hvordan Dental Data passer til din organisation.</p>
 <form class="cform" action="https://formsubmit.co/partners@softwareinabox.eu" method="POST">
  <input type="hidden" name="_subject" value="Dental Data · Danmark [DA]">
  <input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="https://www.softwareinabox.eu/gracias.html">
  <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
  <label class="sr" for="f-n">Navn</label><input id="f-n" name="Navn" required placeholder="Fulde navn" autocomplete="name">
  <label class="sr" for="f-o">Organisation</label><input id="f-o" name="Organisation" placeholder="Organisation" autocomplete="organization">
  <label class="sr" for="f-p">Profil</label><select id="f-p" class="full" name="Profil"><option value="">Din organisations profil</option><option>Myndighed eller region</option><option>Forening</option><option>Tandlægekæde</option><option>Privat klinik</option><option>Forsikringsselskab</option><option>Softwareleverandør eller Microsoft-partner</option><option>Andet</option></select>
  <label class="sr" for="f-e">E-mail</label><input id="f-e" class="full" type="email" name="E-mail" required placeholder="Arbejdsmail" autocomplete="email">
  <label class="sr" for="f-m">Besked</label><textarea id="f-m" name="Besked" placeholder="Hvad vil du gerne tale med os om?"></textarea>
  <label class="ok full"><input type="checkbox" name="Samtykke" value="Accepterer privatlivspolitikken" required><span>Jeg har læst og accepterer <a href="https://www.softwareinabox.eu/da/privacidad.html" target="_blank" rel="noopener">privatlivspolitikken</a>. Vi bruger kun dine oplysninger til at svare dig.</span></label>
  <button type="submit">Send</button>
 </form>
 <p style="font-size:15px;margin-top:18px">Eller skriv til <a href="mailto:partners@softwareinabox.eu" style="color:#fff;font-weight:600">partners@softwareinabox.eu</a> · <a href="tel:+34601398868" style="color:#fff;font-weight:600">+34 601 398 868</a> · Madrid og Bruxelles</p>
</div></section>
''',
}

TEXTOS = {
"m000": "<title>Dental Data Danmark · Fødereret dentalt dataområde til EHDS | Software in a Box</title>",
"m001": 'content="Dental Data er et fødereret dentalt dataområde på Microsoft Azure: SCOR-logikken udvidet til voksne og private klinikker, uden at centralisere journaler. Til Det europæiske sundhedsdataområde (EHDS)."',
"m002": '<link rel="canonical" href="https://dentaldata.softwareinabox.eu/da/">',
"m003": 'content="da_DK"',
"m004": '<meta property="og:title" content="Dental Data Danmark · Dit dentale dataområde starter her">',
"m005": 'content="Børnenes tandsundhed er i SCOR. Dental Data gør voksentandplejen synlig, uden at en eneste journal forlader klinikken."',
"m006": '<meta property="og:url" content="https://dentaldata.softwareinabox.eu/da/">',
"m007": '<a class="brand" href="/da/" aria-label="Dental Data Danmark, forside">',
"m015": '<ul id="m2"><li><a href="#para-quien">Myndigheder</a></li><li><a href="#para-quien">Regioner</a></li><li><a href="#para-quien">Tandlægeforeningen</a></li><li><a href="#para-quien">Kæder og integratorer</a></li></ul>',
"m017": '<li><a href="#destacados">Undersøgelse, præsentation og videoer</a></li><li><a href="#marked">Det danske marked</a></li><li><a href="#preguntas">Ofte stillede spørgsmål</a></li><li><a href="https://datos.softwareinabox.eu/da/">Vores dataområder</a></li>',
"m018": '<a class="tbtn white" href="#contacto">Tal med os</a>\n  <button',
"m021": '<li><a href="/es/" hreflang="es-ES" lang="es">Español · España</a></li>',
"m027": '<a href="#solucion">Løsning</a><a href="#para-quien">For hvem</a><a href="#destacados">Ressourcer</a><a href="#preguntas">Ofte stillede spørgsmål</a><a href="#contacto">Tal med os</a>',
"m028": '<div class="pre">Danmark · Det europæiske sundhedsdataområde</div>',
"m029": '<h1 id="h1">Dit dentale dataområde <em>starter her</em></h1>',
"m030": '<p class="lead">Børnenes tandsundhed er registreret siden 1972. Spørg, hvordan voksentandplejen kan blive synlig, uden at en eneste journal forlader klinikken.</p>',
"m034": '<button class="chip" type="button" data-q="datos">Forlader mine data klinikken?</button>',
"m035": '<button class="chip" type="button" data-q="scor">Hvad tilfører det i forhold til SCOR?</button>',
"m036": '<button class="chip" type="button" data-q="ehds">Hvad betyder EHDS for tandplejen?</button>',
"m037": '<button class="chip" type="button" data-q="ia">Hvordan virker AI på røntgenbilleder?</button>',
"m038": '<button class="chip" type="button" data-q="samarbejde">Hvordan kan vi samarbejde?</button>',
"m039": '<p class="trust">Erfaring fra <b>3 offentligt finansierede dataområder</b> · Connector på <b>Microsoft Azure</b> med data i EU</p>',
"m040": '<h2>Gør voksentandplejen lige så synlig som børnetandplejen</h2>',
"m041": '<p>Vi søger partnere til en institutionel alliance: Sundhedsdatastyrelsen, regionerne, Tandlægeforeningen, tandlægekæderne og danske Azure-integratorer.</p>',
"m042": '<a class="tbtn white" href="#contacto">Tal med os</a><button class="tbtn outline" type="button" data-open-assistant>Spørg assistenten</button>',
"m043": '<div class="cap">Hvad alliancen giver</div>',
"m044": '<b>Data om voksne, ikke kun børn</b><span>Den private voksentandpleje bliver synlig, uden at journaler centraliseres.</span>',
"m045": '<b>Aktivitetsdata til kapacitetsplanlægning</b><span>Produktivitet og opgavefordeling til tandplejere, med faldende tandlægetæthed.</span>',
"m046": '<b>Frivilligt og aggregeret</b><span>Ingen uforholdsmæssige byrder for de private klinikker.</span>',
"m047": '<b>Kompatibelt med den nye styring</b><span>Klar til Digital Sundhed Danmark og Health Data Gateway.</span>',
"m088": '<a class="flogo" href="/da/" aria-label="Dental Data Danmark, forside">',
"m090": '<div><h4>Lande</h4><a href="/de/" lang="de">Deutschland</a><a href="/nl/" lang="nl">Nederland</a><a href="/nl-be/" lang="nl">België</a><a href="/">Alle lande</a></div>',
"m094": '<div><h4>Kontakt</h4><a href="#contacto">Tal med os</a>',
"m095": '<a href="/en/" lang="en">Dental Data Europe</a></div>',
"m096": 'stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.8 2.5 15.2 0 18M12 3c-2.5 2.8-2.5 15.2 0 18"/></svg>Dansk (Danmark)</span>',
"m109": "bot(['Hej! Jeg er Dental Datas assistent. Jeg forklarer, hvordan det fødererede dentale dataområde virker, hvad det tilfører i forhold til SCOR, og hvad Det europæiske sundhedsdataområde betyder for tandplejen i Danmark.','Vælg et spørgsmål eller skriv dit eget. Skriv venligst ikke personoplysninger eller patientdata: vi gemmer spørgsmål og svar anonymt for at forbedre assistenten.'],['datos','scor','ehds','ia','samarbejde'],true)",
"m115": "['datos','ehds','samarbejde','tecnologia']",
"m116": "idioma:'da',pais:'dk'",
"m118": "var FUENTES={'01-que-es-dental-data.md':'Hvad Dental Data er','03-solucion-casos-uso.md':'Løsning og anvendelser','05-tecnologia.md':'Teknologi','08-empresa-recursos.md':'Software in a Box','10-estudio-comparativo-en.md':'Sammenlignende undersøgelse (PDF)','11-ehds-europa.md':'EHDS i Europa','pais/dk.md':'Dental Data i Danmark'}",
}

REEMPLAZOS = desde_claves(TEXTOS) + [
('<li><a href="/da/" hreflang="da-DK" lang="da">Dansk · Danmark</a></li>', '<li><a href="/da/" hreflang="da-DK" lang="da" aria-current="page">Dansk · Danmark</a></li>'),
]
