# Dental Data Italia · https://dentaldata.softwareinabox.eu/it/
# Mercato «it»: catene odontoiatriche e fondi sanitari integrativi; informazione verificabile, mai promozione (comma 525).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "idiomas"))
from _mercado import desde_claves

SALIDA = "it/index.html"
LANG = "it-IT"
IDIOMA_COMUN = "it"
SIAB = "it"
PERMITIDO = ['lang="es"', "Español", "España"]
PRES = "it"
VIDEOS_LANG = "it"

JSONLD = r'''
{"@context":"https://schema.org","@graph":[
{"@type":"WebPage","@id":"https://dentaldata.softwareinabox.eu/it/#webpage","url":"https://dentaldata.softwareinabox.eu/it/","name":"Dental Data Italia · Spazio di dati odontoiatrici federato","inLanguage":"it-IT","isPartOf":{"@type":"WebSite","@id":"https://www.softwareinabox.eu/#website","name":"Software in a Box"},"publisher":{"@type":"Organization","@id":"https://www.softwareinabox.eu/#org","name":"Software in a Box","url":"https://www.softwareinabox.eu/"}},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"I dati escono dallo studio?","acceptedAnswer":{"@type":"Answer","text":"No. Le cartelle restano nel software gestionale di ogni studio, catena o fondo. Si muovono solo consensi, metadati e risultati aggregati, secondo contratti d’uso che la macchina fa rispettare."}},
{"@type":"Question","name":"Che rapporto c’è con il Fascicolo Sanitario Elettronico?","acceptedAnswer":{"@type":"Answer","text":"Dental Data non sostituisce il Fascicolo Sanitario Elettronico. Porta il dato odontoiatrico, oggi quasi tutto fuori dal SSN, in un formato interoperabile e con un catalogo HealthDCAT-AP, pronto a collegarsi all’Ecosistema Dati Sanitari."}},
{"@type":"Question","name":"Si possono usare i dati per promuovere lo studio?","acceptedAnswer":{"@type":"Answer","text":"No. L’informazione sanitaria deve restare informativa (legge 145/2018, comma 525) e lo Spazio europeo dei dati sanitari vieta l’uso dei dati sanitari per la pubblicità."}}
]}]}
'''

KB_JS = r'''[
{id:'datos',q:'I miei dati escono dallo studio?',k:['escono','uscire','sposta','central','dove sono','server','copia','condivid'],
 a:['No. Le cartelle restano nel software gestionale di ogni studio, catena o fondo. Dental Data è uno spazio di dati <b>federato</b>: si muovono solo consensi, metadati e risultati aggregati.','Ogni accesso è regolato da un contratto ODRL che la macchina fa rispettare: lo studio decide chi accede, per cosa e per quanto tempo. Senza contratto, nessun accesso.'],s:['fse','seguridad']},
{id:'catena',q:'Cosa ottiene una catena odontoiatrica?',k:['catena','catene','gruppo','società','direttore sanitario','124/2017','chiusur','qualità'],
 a:['Dal 2017 le società di capitali possono esercitare l’odontoiatria con un direttore sanitario. Una catena che acquista studi riceve in ognuno un software diverso, e confrontare la qualità significa migrare le cartelle.','Con Dental Data un connettore accanto a ogni software calcola gli indicatori nello studio, con la stessa definizione. La direzione vede risultati confrontabili e può mostrarli a fondi, ordini e regolatori, come informazione verificabile e non come promozione.'],s:['fondo','collaborare']},
{id:'fondo',q:'Cosa ottiene un fondo sanitario integrativo?',k:['fondo','fondi','integrativ','assicura','convenzion','rete','polizza','premi'],
 a:['Una parte crescente delle cure dentali è pagata da fondi sanitari integrativi e assicurazioni, attraverso reti di studi convenzionati con software diversi.','Dental Data offre dati coerenti di tutta la rete senza centralizzare le cartelle. L’EHDS vieta di usare questi dati per la pubblicità o per decisioni che danneggiano le persone, anche nelle assicurazioni.'],s:['catena','datos']},
{id:'fse',q:'Come si collega al Fascicolo e all’Ecosistema Dati Sanitari?',k:['fascicolo','fse','ecosistema','eds','agenas','ssn','lea','regioni','cda'],
 a:['Dental Data non sostituisce il <b>Fascicolo Sanitario Elettronico 2.0</b>. Porta il dato odontoiatrico, oggi quasi tutto fuori dal SSN, in un formato interoperabile (HL7 FHIR, con attenzione ai documenti CDA2) e con un catalogo HealthDCAT-AP.','L’<b>Ecosistema Dati Sanitari</b> è gestito da AGENAS (DM 31/12/2024). L’organismo di accesso EHDS per l’Italia non è ancora designato (novembre 2026).'],s:['ehds','tecnologia']},
{id:'ehds',q:'Quali date fissa l’EHDS?',k:['ehds','2027','2029','2031','organismo','articolo 50','micro','regolamento'],
 a:['Date chiave: entro il <b>26 marzo 2027</b> ogni Stato designa i propri organismi di accesso; dal <b>26 marzo 2029</b> si applica la maggior parte delle regole sull’uso secondario; nel <b>2031</b> entrano le immagini mediche.','La maggior parte degli studi sono microimprese, esenti per impostazione predefinita: serve un canale aggregato, attraverso catene, fondi o associazioni.'],s:['fse','collaborare']},
{id:'ia',q:'Come funziona l’IA sulle radiografie?',k:[' ia ','intelligenza artificiale','radiograf','immagin','carie','parodont','algoritmo','modello','agid','acn'],
 a:['Con l’apprendimento federato e il calcolo confidenziale: <b>l’algoritmo va verso il dato</b>, non il contrario. Nessuna radiografia lascia lo studio.','Il nostro modello per carie interprossimali e perdita ossea parodontale è in validazione clinica. Aiuta il professionista senza sostituirne la diagnosi. Per l’IA, le autorità indicate dalla legge 132/2025 sono AgID e ACN.'],s:['datos','tecnologia']},
{id:'tecnologia',q:'Quale tecnologia usate?',k:['tecnolog','connettore','standard','gaia','idsa','eclipse','edc','fhir','dicom','software','gestionale','microsoft','azure'],
 a:['Un connettore su <b>Microsoft Azure</b>, con i dati nell’Unione europea, integrato nel software gestionale dello studio.','Ai confini dello spazio, standard europei aperti: Gaia-X, IDSA e Dataspace Protocol, Eclipse EDC, FHIR, DICOM e HealthDCAT-AP. Le terminologie cliniche (SNOMED CT in Italia) sono da confermare con le istituzioni.'],s:['fse','collaborare']},
{id:'seguridad',q:'È conforme al GDPR?',k:['gdpr','privacy','garante','codice','sicurezza','consenso','legale'],
 a:['I dati identificabili non vengono mai centralizzati: circolano solo risultati aggregati, sotto contratto, nel quadro del GDPR e del Codice privacy, sotto la vigilanza del Garante.','Ogni progetto è documentato con il responsabile della protezione dei dati dell’organizzazione e una valutazione d’impatto.'],s:['datos','fse']},
{id:'publicidad',q:'Si possono usare i dati per promuovere lo studio?',k:['pubblicit','promuover','marketing','525','vender','commercial'],
 a:['No. L’informazione sanitaria deve restare informativa (legge 145/2018, comma 525) e lo Spazio europeo dei dati sanitari vieta l’uso dei dati sanitari per la pubblicità.','Gli usi previsti sono la qualità delle cure, l’IA sulle immagini ed evidenze per l’industria su impianti e materiali.'],s:['datos','catena']},
{id:'collaborare',q:'Come possiamo collaborare?',k:['collabor','partner','partecip','progetto','pilota','contatt','software house'],
 a:['In Italia cerchiamo una <b>catena odontoiatrica</b> o un <b>fondo sanitario integrativo</b> per un primo progetto di indicatori di qualità tra studi, e vogliamo parlare con le software house, la CAO-FNOMCeO, ANDI, AIO, AGENAS e le regioni.','Il caso d’uso stesso finanzia il connettore. Lascia i tuoi dati nel modulo e ti proporremo un incontro.'],s:['catena','fondo']},
{id:'experiencia',q:'Chi siete e che esperienza avete?',k:['chi','azienda','esperienza','software in a box','referenz','progetti','global data care'],
 a:['Software in a Box, con sedi a Madrid e Bruxelles. Tra il 2024 e il 2026 abbiamo progettato e realizzato tre dimostratori di spazi di dati finanziati dalla Segreteria di Stato spagnola per la Digitalizzazione e l’IA: <b>Global Data Care</b> (salute), <b>PROCUREDATA</b> (acquisti) ed <b>EcoDataNet</b> (economia circolare).','Maggiori informazioni sui <a href="https://datos.softwareinabox.eu/it/" target="_blank" rel="noopener">nostri spazi di dati</a>.'],s:['tecnologia','collaborare']},
{id:'documentos',q:'Dove posso leggere lo studio?',k:['studio comparativo','documento','pdf','scaric','rapporto','presentazione','video','leggere'],
 a:['Lo studio comparativo europeo è disponibile in <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">inglese</a>, con la presentazione e il video completo. Le presentazioni animate di questa pagina riassumono ogni domanda in meno di un minuto.'],s:['datos','ehds']}
]'''

BLOQUES = {
"espana": r'''
<section class="s soft" id="mercato"><div class="wrap">
 <div class="head"><div class="eyebrow">Il mercato italiano</div><h2>Oltre 10 miliardi di spesa privata, nessun dato sui risultati</h2><p>Le famiglie pagano quasi tutta l’odontoiatria, le catene crescono e il servizio sanitario nazionale copre le cure dentali solo per i bambini e le persone vulnerabili. Ogni studio conserva cartelle e radiografie nel proprio software, quasi sempre fuori dal Fascicolo Sanitario Elettronico.</p></div>
 <div class="grid4">
  <div class="card"><div class="num">SPESA PRIVATA</div><h3 class="big">&gt; 10 mld €</h3><p>di spesa annua delle famiglie per l’odontoiatria (AIOP, ISTAT-SHA).</p></div>
  <div class="card"><div class="num">SPESA DEL SSN</div><h3 class="big">85 mln €</h3><p>di spesa pubblica per l’odontoiatria, circa l’1 % del totale (Consiglio Superiore di Sanità).</p></div>
  <div class="card"><div class="num">ODONTOIATRI</div><h3 class="big">64 965</h3><p>odontoiatri iscritti all’albo nel gennaio 2024 (CAO-FNOMCeO).</p></div>
  <div class="card"><div class="num">CATENE</div><h3 class="big">&gt; 275</h3><p>studi di proprietà del primo gruppo del settore.</p></div>
 </div>
 <div class="grid2" style="margin-top:22px">
  <div class="card"><h3>LEA odontoiatrici</h3><p>Il SSN garantisce le cure dentali da 0 a 14 anni e alle persone in condizione di vulnerabilità sanitaria o sociale, con criteri regionali. Oltre 200.000 italiani si curano all’estero.</p></div>
  <div class="card"><h3>Società di capitali e direttore sanitario</h3><p>Dal 2017 (legge 124/2017) le società possono esercitare l’odontoiatria con un direttore sanitario. Le chiusure improvvise di alcune catene hanno danneggiato la fiducia, e la professione chiede una riforma.</p></div>
 </div>
 <p class="pcap">Fonte: Software in a Box, <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">Dental health data spaces in Europe · Studio comparativo</a> (novembre 2026), capitolo Italia, e le fonti citate (CAO-FNOMCeO, Consiglio Superiore di Sanità, AGENAS). Dati aggiornati a novembre 2026.</p>
</div></section>
''',
"para-quien": r'''
<section class="s soft" id="para-quien"><div class="wrap">
 <div class="head"><div class="eyebrow">Per chi</div><h2>Il dato odontoiatrico, oggi fuori dal SSN, pronto per l’Ecosistema Dati Sanitari</h2><p>Dental Data non sostituisce il Fascicolo Sanitario Elettronico. Porta il dato odontoiatrico in un formato interoperabile e con un catalogo HealthDCAT-AP, pronto a collegarsi all’Ecosistema Dati Sanitari quando sarà designato l’organismo di accesso.</p></div>
 <div class="grid4 who-grid">
  <div class="card"><div class="num">CATENE</div><h3>Qualità dimostrabile</h3><p>Indicatori confrontabili tra studi, da mostrare a fondi, ordini e regolatori come informazione verificabile.</p></div>
  <div class="card"><div class="num">FONDI E ASSICURAZIONI</div><h3>Dati coerenti della rete</h3><p>Costi e risultati confrontabili tra gli studi convenzionati, senza centralizzare le cartelle.</p></div>
  <div class="card"><div class="num">REGIONI E ASL</div><h3>Misurare i LEA</h3><p>Indicatori delle cure odontoiatriche garantite da 0 a 14 anni e alle persone vulnerabili.</p></div>
  <div class="card"><div class="num">SOFTWARE HOUSE</div><h3>Un connettore in più</h3><p>Accanto al software gestionale dello studio, con nuovi servizi per i clienti.</p></div>
 </div>
 <div class="head" style="margin-top:56px;margin-bottom:22px"><h2 style="font-size:28px">Roadmap</h2></div>
 <div class="flow">
  <div class="step"><div class="c">1</div><b>2027 · Primo progetto</b><span>Indicatori di qualità con una catena o un fondo sanitario integrativo.</span></div>
  <div class="step"><div class="c">2</div><b>2027–2028 · Consolidamento</b><span>Consolidamento dei progetti e partecipazione alle consultazioni; FSE 2.0 ed Ecosistema Dati Sanitari in evoluzione.</span></div>
  <div class="step"><div class="c">3</div><b>Marzo 2029 · Catalogato</b><span>Un insieme di dati catalogato e pronto per l’EHDS. L’organismo di accesso italiano è ancora da designare.</span></div>
 </div>
 <div class="nl-band"><div><b>Anche in Spagna e in Portogallo</b><p>Un solo prodotto per tutta l’Europa, adattato alla lingua, ai dati e al diritto di ogni paese.</p></div><a href="/es/" lang="es" hreflang="es-ES">España →</a>&nbsp;&nbsp;<a href="/pt/" lang="pt" hreflang="pt-PT">Portugal →</a></div>
</div></section>
''',
"contacto": r'''
<section class="s cta" id="contacto"><div class="wrap">
 <h2>Primi partner in Italia</h2>
 <p>Catene odontoiatriche, fondi sanitari integrativi, software house e istituzioni: raccontaci in breve chi sei e ti proporremo un incontro, online o a Bruxelles.</p>
 <form class="cform" action="https://formsubmit.co/partners@softwareinabox.eu" method="POST">
  <input type="hidden" name="_subject" value="Dental Data · Italia">
  <input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="https://www.softwareinabox.eu/gracias.html">
  <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
  <label class="sr" for="f-n">Nome</label><input id="f-n" name="Nome" required placeholder="Nome e cognome" autocomplete="name">
  <label class="sr" for="f-o">Organizzazione</label><input id="f-o" name="Organizzazione" placeholder="Organizzazione" autocomplete="organization">
  <label class="sr" for="f-p">Profilo</label><select id="f-p" class="full" name="Profilo"><option value="">Profilo della tua organizzazione</option><option>Catena odontoiatrica</option><option>Fondo sanitario integrativo o assicurazione</option><option>Studio odontoiatrico</option><option>Istituzione, regione o ASL</option><option>Software house o partner Microsoft</option><option>Industria</option><option>Altro</option></select>
  <label class="sr" for="f-e">E-mail</label><input id="f-e" class="full" type="email" name="E-mail" required placeholder="E-mail di lavoro" autocomplete="email">
  <label class="sr" for="f-m">Messaggio</label><textarea id="f-m" name="Messaggio" placeholder="Di cosa vuoi parlarci?"></textarea>
  <label class="ok full"><input type="checkbox" name="Consenso" value="Accetta l’informativa sulla privacy" required><span>Ho letto e accetto l’<a href="https://www.softwareinabox.eu/it/privacidad.html" target="_blank" rel="noopener">informativa sulla privacy</a>. Useremo i tuoi dati solo per risponderti.</span></label>
  <button type="submit">Invia</button>
 </form>
 <p style="font-size:15px;margin-top:18px">Oppure scrivi a <a href="mailto:partners@softwareinabox.eu" style="color:#fff;font-weight:600">partners@softwareinabox.eu</a> · <a href="tel:+34601398868" style="color:#fff;font-weight:600">+34 601 398 868</a> · Bruxelles e Madrid</p>
</div></section>
''',
}

TEXTOS = {
"m000": "<title>Dental Data Italia · Spazio di dati odontoiatrici federato per l’EHDS | Software in a Box</title>",
"m001": 'content="Dental Data è uno spazio di dati odontoiatrici federato su Microsoft Azure: misurare la qualità tra gli studi senza spostare una sola cartella clinica. Per catene, fondi sanitari integrativi e software house."',
"m002": '<link rel="canonical" href="https://dentaldata.softwareinabox.eu/it/">',
"m003": 'content="it_IT"',
"m004": '<meta property="og:title" content="Dental Data Italia · Misurare la qualità tra gli studi senza spostare una sola cartella">',
"m005": 'content="Gli indicatori si calcolano nello studio, viaggia solo il risultato."',
"m006": '<meta property="og:url" content="https://dentaldata.softwareinabox.eu/it/">',
"m007": '<a class="brand" href="/it/" aria-label="Dental Data Italia, home">',
"m015": '<ul id="m2"><li><a href="#para-quien">Catene odontoiatriche</a></li><li><a href="#para-quien">Fondi e assicurazioni</a></li><li><a href="#para-quien">Regioni e ASL</a></li><li><a href="#para-quien">Software house</a></li></ul>',
"m017": '<li><a href="#destacados">Studio, presentazione e video</a></li><li><a href="#mercato">Il mercato italiano</a></li><li><a href="#preguntas">Domande frequenti</a></li><li><a href="https://datos.softwareinabox.eu/it/">I nostri spazi di dati</a></li>',
"m018": '<a class="tbtn white" href="#contacto">Contattaci</a>\n  <button',
"m021": '<li><a href="/es/" hreflang="es-ES" lang="es">Español · España</a></li>',
"m027": '<a href="#solucion">Soluzione</a><a href="#para-quien">Per chi</a><a href="#destacados">Risorse</a><a href="#preguntas">Domande frequenti</a><a href="#contacto">Contattaci</a>',
"m028": '<div class="pre">Italia · Spazio europeo dei dati sanitari</div>',
"m029": '<h1 id="h1">Misurare la qualità tra gli studi <em>senza spostare una sola cartella clinica</em></h1>',
"m030": '<p class="lead">Dental Data collega studi, catene e fondi sanitari in uno spazio di dati federato: gli indicatori si calcolano nello studio, viaggia solo il risultato.</p>',
"m034": '<button class="chip" type="button" data-q="catena">Cosa ottiene una catena?</button>',
"m035": '<button class="chip" type="button" data-q="fondo">Cosa ottiene un fondo integrativo?</button>',
"m036": '<button class="chip" type="button" data-q="datos">I dati escono dallo studio?</button>',
"m037": '<button class="chip" type="button" data-q="fse">E il Fascicolo Sanitario?</button>',
"m038": '<button class="chip" type="button" data-q="collaborare">Come collaborare?</button>',
"m039": '<p class="trust">Esperienza in <b>3 spazi di dati</b> finanziati con fondi pubblici · Connettore su <b>Microsoft Azure</b> con i dati nell’UE</p>',
"m040": '<h2>Collega gli studi senza migrare una sola cartella</h2>',
"m041": '<p>Cerchiamo una catena odontoiatrica o un fondo sanitario integrativo per un primo progetto di indicatori di qualità tra studi.</p>',
"m042": '<a class="tbtn white" href="#contacto">Contattaci</a><button class="tbtn outline" type="button" data-open-assistant>Chiedi all’assistente</button>',
"m043": '<div class="cap">Cosa ottieni</div>',
"m044": '<b>Qualità confrontabile tra gli studi</b><span>Indicatori omogenei anche con software diversi.</span>',
"m045": '<b>IA sulle immagini, senza spostare radiografie</b><span>L’algoritmo va verso il dato: apprendimento federato e calcolo confidenziale.</span>',
"m046": '<b>Pronto per l’EHDS prima del 2029</b><span>Uno spazio catalogato, pronto per le richieste degli organismi di accesso.</span>',
"m047": '<b>Informazione verificabile</b><span>Risultati misurati, mai promozione.</span>',
"m088": '<a class="flogo" href="/it/" aria-label="Dental Data Italia, home">',
"m090": '<div><h4>Paesi</h4><a href="/es/" lang="es">España</a><a href="/pt/" lang="pt">Portugal</a><a href="/fr/" lang="fr">France</a><a href="/">Tutti i paesi</a></div>',
"m094": '<div><h4>Contatto</h4><a href="#contacto">Contattaci</a>',
"m095": '<a href="/en/" lang="en">Dental Data Europe</a></div>',
"m096": 'stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.8 2.5 15.2 0 18M12 3c-2.5 2.8-2.5 15.2 0 18"/></svg>Italiano (Italia)</span>',
"m109": "bot(['Ciao! Sono l’assistente di Dental Data. Ti spiego come funziona lo spazio di dati odontoiatrici federato, cosa offre a catene e fondi e cosa significa lo Spazio europeo dei dati sanitari per l’odontoiatria in Italia.','Scegli una domanda o scrivi la tua. Per favore, non inserire dati personali né dati di pazienti: conserviamo in forma anonima domande e risposte per migliorare l’assistente.'],['catena','fondo','datos','fse','collaborare'],true)",
"m115": "['datos','fse','collaborare','tecnologia']",
"m116": "idioma:'it',pais:'it'",
"m118": "var FUENTES={'01-que-es-dental-data.md':'Cos’è Dental Data','03-solucion-casos-uso.md':'Soluzione e casi d’uso','05-tecnologia.md':'Tecnologia','08-empresa-recursos.md':'Software in a Box','10-estudio-comparativo-en.md':'Studio comparativo (PDF)','11-ehds-europa.md':'L’EHDS in Europa','pais/it.md':'Dental Data in Italia'}",
}

REEMPLAZOS = desde_claves(TEXTOS) + [
('<li><a href="/it/" hreflang="it-IT" lang="it">Italiano · Italia</a></li>', '<li><a href="/it/" hreflang="it-IT" lang="it" aria-current="page">Italiano · Italia</a></li>'),
]
