# Dental Data Deutschland · https://dentaldata.softwareinabox.eu/de/
# Markt «de»: Ergänzung zur ePA und zum FDZ Gesundheit für PVS-Hersteller, MVZ und Integratoren. Kein Pilotaufruf.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "idiomas"))
from _mercado import desde_claves

SALIDA = "de/index.html"
LANG = "de-DE"
IDIOMA_COMUN = "de"
SIAB = "de"
PERMITIDO = ['lang="es"', "Español", "España"]

JSONLD = r'''
{"@context":"https://schema.org","@graph":[
{"@type":"WebPage","@id":"https://dentaldata.softwareinabox.eu/de/#webpage","url":"https://dentaldata.softwareinabox.eu/de/","name":"Dental Data Deutschland · Föderierter zahnmedizinischer Datenraum","inLanguage":"de-DE","isPartOf":{"@type":"WebSite","@id":"https://www.softwareinabox.eu/#website","name":"Software in a Box"},"publisher":{"@type":"Organization","@id":"https://www.softwareinabox.eu/#organization","name":"Software in a Box","url":"https://www.softwareinabox.eu/"},"areaServed":"DE"},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Verlassen meine Daten die Praxis?","acceptedAnswer":{"@type":"Answer","text":"Nein. Die Akten bleiben in der Praxisverwaltungssoftware jeder Praxis, jedes MVZ oder jeder Kette. Ausgetauscht werden nur Einwilligungen, Metadaten und aggregierte Ergebnisse, nach Nutzungsverträgen, die die Maschine durchsetzt."}},
{"@type":"Question","name":"Konkurriert Dental Data mit der ePA oder dem FDZ Gesundheit?","acceptedAnswer":{"@type":"Answer","text":"Nein. Dental Data ergänzt die fehlenden Bausteine: zertifizierbare Konnektoren für Praxissoftware, Prüfung von Format und Datenqualität vor dem Hochladen, föderierte Analysen für Ketten und MVZ sowie Kataloge mit standardisierten Metadaten."}},
{"@type":"Question","name":"Was bedeutet der EHDS für die Zahnmedizin in Deutschland?","acceptedAnswer":{"@type":"Answer","text":"Die DACO des BfArM wird koordinierende Zugangsstelle für Gesundheitsdaten. Bis zum 26.03.2027 benennt jeder Mitgliedstaat seine Zugangsstellen; ab dem 26.03.2029 gelten die meisten Regeln zur Sekundärnutzung; ab 2031 kommen medizinische Bilder hinzu."}}
]}]}
'''

KB_JS = r'''[
{id:'datos',q:'Verlassen meine Daten die Praxis?',k:['verlassen','verschoben','zentral','gespeichert','wo liegen','cloud','server','datenschutz','kopie','teilen'],
 a:['Nein. Die Akten bleiben in der Praxisverwaltungssoftware (PVS) jeder Praxis, jedes MVZ oder jeder Kette. Dental Data ist ein <b>föderierter</b> Datenraum: Ausgetauscht werden nur Einwilligungen, Metadaten und aggregierte Ergebnisse.','Jeder Zugriff wird durch einen ODRL-Vertrag geregelt, den die Maschine durchsetzt: Die Praxis entscheidet, wer wofür und wie lange Zugriff erhält. Kein Vertrag, kein Zugriff.'],s:['ia','seguridad']},
{id:'epa',q:'Konkurriert Dental Data mit der ePA oder dem FDZ?',k:['epa','patientenakte','fdz','bfarm','forschungsdatenzentrum','telematik','gematik','ezahnbonusheft','bonusheft','ebz','konkurr'],
 a:['Nein. Die <b>ePA für alle</b> ist seit dem 01.10.2025 in allen Zahnarztpraxen verpflichtend; im April 2026 gab es fast 73 Millionen ePAs und mehr als 5,5 Millionen elektronische Zahnbonushefte. Das FDZ Gesundheit des BfArM nimmt seit dem 09.10.2025 Anträge an.','Dental Data ergänzt die fehlenden Bausteine: <b>zertifizierbare Konnektoren</b> für Praxissoftware, Prüfung von Format und Datenqualität vor dem Hochladen, <b>föderierte Analysen</b> für Ketten und MVZ sowie Kataloge mit standardisierten Metadaten.'],s:['pvs','ehds']},
{id:'ehds',q:'Was bedeutet der EHDS für Zahnarztpraxen?',k:['ehds','gesundheitsdatenraum','zugangsstelle','daco','gdng','gedig','2027','2029','2031','gesetz','verordnung','artikel 50','kleinst'],
 a:['Deutschland hat mit dem Gesundheitsdatennutzungsgesetz (GDNG) viel vorweggenommen. Die DACO des BfArM wird <b>koordinierende Zugangsstelle für Gesundheitsdaten</b>; am 15.07.2026 hat die Bundesregierung den Entwurf des GeDIG beschlossen, das den EHDS auf der bestehenden Infrastruktur umsetzt.','Wichtige Termine: bis zum <b>26.03.2027</b> sind die Zugangsstellen benannt, ab dem <b>26.03.2029</b> gelten die meisten Regeln zur Sekundärnutzung, ab <b>2031</b> kommen medizinische Bilder hinzu, darunter Röntgenbilder und DVT. Die Anbindung der ePA an das FDZ ist für Ende 2026 geplant.'],s:['epa','datos']},
{id:'ia',q:'Wie funktioniert KI auf Röntgenbildern?',k:[' ki ','künstliche intelligenz','röntgen','bild','karies','parodont','algorithmus','modell','föderiert','dvt'],
 a:['Mit föderiertem Lernen und Confidential Computing: <b>Der Algorithmus geht zu den Daten</b>, nicht umgekehrt. Kein Röntgenbild verlässt die Praxis.','Unser Modell für Approximalkaries und parodontalen Knochenabbau befindet sich in der klinischen Validierung. Es unterstützt die Zahnärztin oder den Zahnarzt und ersetzt nicht die Diagnose.'],s:['datos','tecnologia']},
{id:'pvs',q:'Was haben PVS-Hersteller und MVZ davon?',k:['pvs','praxisverwaltung','software','hersteller','anbieter','mvz','imvz','kette','investor','partner','zusammenarbeit','integrator','bürokratie'],
 a:['<b>PVS-Hersteller</b> erhalten einen Konnektor, der Interoperabilität, Protokollierung und Datenqualität für den EHDS abdeckt, ohne eigene Entwicklung. <b>MVZ und Ketten</b>, darunter die investorengetragenen iMVZ (30,4 % der zahnärztlichen MVZ im 3. Quartal 2023), können Ergebnisse zwischen Standorten vergleichen und ihre Versorgungsqualität belegen.','Wichtig für Praxen: Die Lösung muss Zeit sparen, nicht zusätzlichen Aufwand erzeugen. Wir suchen eine Vereinbarung mit einem PVS-Hersteller oder einem auf Telematik spezialisierten Azure-Integrator. Schreiben Sie uns über das <a href="#contacto" data-close>Kontaktformular</a> oder an <a href="mailto:partners@softwareinabox.eu">partners@softwareinabox.eu</a>.'],s:['epa','markt']},
{id:'markt',q:'Wie sieht der deutsche Dentalmarkt aus?',k:['markt','deutschland','zahnärzte','anzahl','gkv','pkv','kzbv','bzäk','kammer','zahlen'],
 a:['2024 gab es <b>43.663</b> aktive Zahnärztinnen und Zahnärzte, etwa 52 je 100.000 Einwohner. Die GKV versichert rund 88 % der Bevölkerung und trägt 65 % der zahnmedizinischen Ausgaben (2023).','Die Einzelpraxis überwiegt, doch die Konsolidierung über MVZ schreitet voran. Die KZBV legt mit den Kassen den Leistungskatalog fest; die BZÄK vereint die 17 Landeszahnärztekammern.'],s:['pvs','epa']},
{id:'tecnologia',q:'Welche Technologie nutzen Sie? Welche Rolle hat Microsoft?',k:['technolog','microsoft','azure','konnektor','standard','gaia','idsa','eclipse','edc','fhir','dicom','integration'],
 a:['Ein Konnektor auf <b>Microsoft Azure</b> mit Daten in der EU, integriert in die Praxisverwaltungssoftware.','An den Grenzen des Datenraums nutzen wir offene europäische Standards: Gaia-X, IDSA und das Dataspace Protocol, Eclipse EDC, FHIR, DICOM und HealthDCAT-AP. So kann sich jeder anschließen, auch ohne Microsoft.'],s:['pvs','datos']},
{id:'seguridad',q:'Ist das DSGVO-konform und sicher?',k:['dsgvo','gdpr','datenschutz','sicherheit','sicher','einwilligung','rechtlich','vertraulich'],
 a:['Identifizierbare Daten werden nie zentralisiert: Es werden nur aggregierte Ergebnisse übertragen, vertraglich geregelt. Für KI nutzen wir Confidential Computing.','Jedes Projekt wird mit der oder dem Datenschutzbeauftragten der Organisation und einer Datenschutz-Folgenabschätzung dokumentiert.'],s:['datos','ehds']},
{id:'publicidad',q:'Werden die Daten für Werbung genutzt?',k:['werbung','marketing','verkaufen','verkauf','kommerziell'],
 a:['Niemals. Der EHDS verbietet ausdrücklich die Nutzung von Gesundheitsdaten für Werbung.','Vorgesehen sind Versorgungsqualität, KI auf Bildern und Evidenz für die Industrie zu Implantaten und Materialien.'],s:['datos','ehds']},
{id:'experiencia',q:'Wer sind Sie und welche Erfahrung haben Sie?',k:['wer','unternehmen','erfahrung','software in a box','referenz','projekte','global data care'],
 a:['Software in a Box mit Sitz in Madrid und Brüssel. Zwischen 2024 und 2026 haben wir drei Demonstratoren für Datenräume entworfen und umgesetzt, gefördert vom spanischen Staatssekretariat für Digitalisierung und KI: <b>Global Data Care</b> (Gesundheit), <b>PROCUREDATA</b> (Beschaffung) und <b>EcoDataNet</b> (Kreislaufwirtschaft).','Mehr unter <a href="https://datos.softwareinabox.eu/de/">datos.softwareinabox.eu</a>.'],s:['tecnologia','pvs']},
{id:'documentos',q:'Wo kann ich die Studie lesen?',k:['studie','dokument','pdf','download','bericht','präsentation','video','lesen'],
 a:['Die Vergleichsstudie zu fünf Märkten mit einem Kapitel zu Deutschland gibt es auf <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">Englisch</a> und <a href="/docs/tandheelkundige-gezondheidsdataruimtes-europa-ehds.pdf" target="_blank" rel="noopener" lang="nl">Niederländisch</a>, zusammen mit der Präsentation und dem vollständigen Video.'],s:['markt','pvs']}
]'''

BLOQUES = {
"espana": r'''
<section class="s soft" id="markt"><div class="wrap">
 <div class="head"><div class="eyebrow">Der deutsche Markt</div><h2>Die Infrastruktur steht. Es fehlen die Bausteine dazwischen.</h2><p>Deutschland verfolgt einen institutionellen, integrierten Ansatz: Zahnmedizinische Daten laufen über die Telematikinfrastruktur, die KZBV-Abrechnung liefert detaillierte Statistiken, und die ePA hat mit dem eZahnbonusheft einen eigenen zahnmedizinischen Teil. Kein anderes Land ist dem Weg der Daten zur Zugangsstelle so nah.</p></div>
 <div class="grid4">
  <div class="card"><div class="num">ZAHNÄRZTE</div><h3 class="big">43.663</h3><p>aktiv im Jahr 2024 (von 103.998 registrierten), etwa 52 je 100.000 Einwohner.</p></div>
  <div class="card"><div class="num">GESETZLICHE KRANKENVERSICHERUNG</div><h3 class="big">65 %</h3><p>der zahnmedizinischen Ausgaben trägt die GKV (2023); sie versichert rund 88 % der Bevölkerung.</p></div>
  <div class="card"><div class="num">EPA IN DER ZAHNARZTPRAXIS</div><h3 class="big">01.10.2025</h3><p>seitdem verpflichtend. Im April 2026: fast 73 Mio. ePAs und mehr als 5,5 Mio. eZahnbonushefte.</p></div>
  <div class="card"><div class="num">INVESTORENGETRAGENE MVZ</div><h3 class="big">30,4 %</h3><p>der zahnärztlichen MVZ im 3. Quartal 2023, mit steigender Tendenz.</p></div>
 </div>
 <div class="grid2" style="margin-top:22px">
  <div class="card"><h3>FDZ Gesundheit, DACO und GeDIG</h3><p>Das Forschungsdatenzentrum Gesundheit des BfArM nimmt seit dem 09.10.2025 Anträge an; die DACO wird koordinierende Zugangsstelle für Gesundheitsdaten. Am 15.07.2026 hat die Bundesregierung den Entwurf des GeDIG beschlossen. Die Anbindung der ePA an das FDZ ist für Ende 2026 geplant.</p></div>
  <div class="card"><h3>Weniger Bürokratie, mehr Qualitätsnachweis</h3><p>Die KZBV beklagt die Bürokratielast in den Praxen; jede Lösung muss Zeit sparen. iMVZ-Netzwerke stehen unter politischer Beobachtung und müssen Qualität belegen, und PVS-Hersteller müssen Anforderungen an Interoperabilität und Konformität erfüllen.</p></div>
 </div>
 <p class="pcap">Quelle: Software in a Box, <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">Dental health data spaces in Europe · Vergleichsstudie</a> (November 2026), mit den dort zitierten Quellen (KZBV, BZÄK, Council of European Dentists, BfArM, Bundesministerium für Gesundheit).</p>
</div></section>
''',
"para-quien": r'''
<section class="s soft" id="para-quien"><div class="wrap">
 <div class="head"><div class="eyebrow">Für wen</div><h2>Keine Konkurrenz zur ePA, sondern die fehlenden Bausteine</h2><p>In Deutschland ersetzt Dental Data weder die ePA noch das FDZ Gesundheit. Wir liefern, was dazwischen fehlt, und arbeiten dafür mit Herstellern von Praxissoftware und Integratoren zusammen.</p></div>
 <div class="grid4 who-grid">
  <div class="card"><div class="num">PVS-HERSTELLER</div><h3>EHDS-bereit ohne Eigenentwicklung</h3><p>Ein zertifizierbarer Konnektor für Interoperabilität, Protokollierung und Datenqualität.</p></div>
  <div class="card"><div class="num">MVZ UND KETTEN</div><h3>Ergebnisse vergleichen</h3><p>Föderierte Analysen zwischen Standorten, ohne Akten zu migrieren, um Versorgungsqualität zu belegen.</p></div>
  <div class="card"><div class="num">AZURE-INTEGRATOREN</div><h3>Telematik und Cloud</h3><p>Partner mit Erfahrung in Gesundheitstelematik, die den Konnektor bereitstellen und betreiben.</p></div>
  <div class="card"><div class="num">INDUSTRIE UND FORSCHUNG</div><h3>Evidenz aus der Versorgung</h3><p>Für Hersteller von Implantaten, Materialien und KI sowie für Forschung, über Kataloge mit standardisierten Metadaten.</p></div>
 </div>
 <div class="head" style="margin-top:56px;margin-bottom:22px"><h2 style="font-size:28px">Roadmap</h2></div>
 <div class="flow">
  <div class="step"><div class="c">1</div><b>2027 · Partner gewinnen</b><span>Vereinbarung mit einem PVS-Hersteller oder Integrator; erste Piloten in Spanien und den Niederlanden.</span></div>
  <div class="step"><div class="c">2</div><b>2027–2028 · Erstes Projekt</b><span>Datenqualitätsprüfung und föderierte Analysen mit einem MVZ-Netzwerk oder einer Kette.</span></div>
  <div class="step"><div class="c">3</div><b>März 2029 · Katalogisiert</b><span>Ein katalogisierter zahnmedizinischer Datenraum, bereit für Zugangsanträge nach dem EHDS.</span></div>
 </div>
 <div class="nl-band"><div><b>Auch in Spanien, den Niederlanden und Belgien</b><p>Wir bauen ein Produkt für ganz Europa und passen es an Sprache, Daten und Recht jedes Landes an.</p></div><a href="/en/" lang="en" hreflang="en">Europe →</a>&nbsp;&nbsp;<a href="/nl/" lang="nl" hreflang="nl-NL">Nederland →</a></div>
</div></section>
''',
"contacto": r'''
<section class="s cta" id="contacto"><div class="wrap">
 <h2>Möchten Sie mit uns sprechen?</h2>
 <p>Erzählen Sie uns kurz, wer Sie sind. Wir schlagen Ihnen ein Gespräch vor, um zu sehen, wie Dental Data zu Ihrer Organisation passt.</p>
 <form class="cform" action="https://formsubmit.co/partners@softwareinabox.eu" method="POST">
  <input type="hidden" name="_subject" value="Dental Data · Deutschland [DE]">
  <input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="https://www.softwareinabox.eu/gracias.html">
  <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
  <label class="sr" for="f-n">Name</label><input id="f-n" name="Name" required placeholder="Vor- und Nachname" autocomplete="name">
  <label class="sr" for="f-o">Organisation</label><input id="f-o" name="Organisation" placeholder="Organisation" autocomplete="organization">
  <label class="sr" for="f-p">Profil</label><select id="f-p" class="full" name="Profil"><option value="">Profil Ihrer Organisation</option><option>Hersteller von Praxissoftware (PVS)</option><option>MVZ oder Praxiskette</option><option>Microsoft-Partner oder Integrator</option><option>Zahnarztpraxis</option><option>Krankenversicherung</option><option>Industrie, Forschung oder Verband</option><option>Sonstiges</option></select>
  <label class="sr" for="f-e">E-Mail</label><input id="f-e" class="full" type="email" name="E-Mail" required placeholder="Geschäftliche E-Mail-Adresse" autocomplete="email">
  <label class="sr" for="f-m">Nachricht</label><textarea id="f-m" name="Nachricht" placeholder="Worüber möchten Sie mit uns sprechen?"></textarea>
  <label class="ok full"><input type="checkbox" name="Einwilligung" value="Akzeptiert die Datenschutzerklärung" required><span>Ich habe die <a href="https://www.softwareinabox.eu/de/privacidad.html" target="_blank" rel="noopener">Datenschutzerklärung</a> gelesen und akzeptiere sie. Wir verwenden Ihre Daten nur, um Ihnen zu antworten.</span></label>
  <button type="submit">Anfrage senden</button>
 </form>
 <p style="font-size:15px;margin-top:18px">Oder schreiben Sie an <a href="mailto:partners@softwareinabox.eu" style="color:#fff;font-weight:600">partners@softwareinabox.eu</a> · <a href="tel:+34601398868" style="color:#fff;font-weight:600">+34 601 398 868</a> · Madrid und Brüssel</p>
</div></section>
''',
}

TEXTOS = {
"m000": "<title>Dental Data Deutschland · Föderierter zahnmedizinischer Datenraum für den EHDS | Software in a Box</title>",
"m001": 'content="Dental Data ist ein föderierter zahnmedizinischer Datenraum auf Microsoft Azure: Datenqualität, Konnektoren für Praxissoftware und föderierte Analysen für MVZ, als Ergänzung zur ePA und zum FDZ Gesundheit."',
"m002": '<link rel="canonical" href="https://dentaldata.softwareinabox.eu/de/">',
"m003": 'content="de_DE"',
"m004": '<meta property="og:title" content="Dental Data Deutschland · Ihr zahnmedizinischer Datenraum beginnt hier">',
"m005": 'content="Die ePA steht. Dental Data liefert die fehlenden Bausteine: Datenqualität, Konnektoren für PVS-Hersteller und föderierte Analysen für MVZ."',
"m006": '<meta property="og:url" content="https://dentaldata.softwareinabox.eu/de/">',
"m007": '<a class="brand" href="/de/" aria-label="Dental Data Deutschland, Startseite">',
"m015": '<ul id="m2"><li><a href="#para-quien">PVS-Hersteller</a></li><li><a href="#para-quien">MVZ und Ketten</a></li><li><a href="#para-quien">Azure-Integratoren</a></li><li><a href="#para-quien">Industrie und Forschung</a></li></ul>',
"m017": '<li><a href="#destacados">Studie, Präsentation und Videos</a></li><li><a href="#markt">Der deutsche Markt</a></li><li><a href="#preguntas">Häufige Fragen</a></li><li><a href="https://datos.softwareinabox.eu/de/">Unsere Datenräume</a></li>',
"m018": '<a class="tbtn white" href="#contacto">Gespräch vereinbaren</a>\n  <button',
"m021": '<li><a href="/es/" hreflang="es-ES" lang="es">Español · España</a></li>',
"m027": '<a href="#solucion">Lösung</a><a href="#para-quien">Für wen</a><a href="#destacados">Ressourcen</a><a href="#preguntas">Häufige Fragen</a><a href="#contacto">Gespräch vereinbaren</a>',
"m028": '<div class="pre">Deutschland · Europäischer Gesundheitsdatenraum</div>',
"m029": '<h1 id="h1">Ihr zahnmedizinischer Datenraum <em>beginnt hier</em></h1>',
"m030": '<p class="lead">Fragen Sie, wie Sie Datenqualität sichern und Ergebnisse zwischen Praxen vergleichen, ohne dass eine einzige Akte die Praxis verlässt.</p>',
"m034": '<button class="chip" type="button" data-q="datos">Verlassen meine Daten die Praxis?</button>',
"m035": '<button class="chip" type="button" data-q="epa">Konkurriert das mit der ePA?</button>',
"m036": '<button class="chip" type="button" data-q="ehds">Was bedeutet der EHDS für Praxen?</button>',
"m037": '<button class="chip" type="button" data-q="ia">Wie funktioniert KI auf Röntgenbildern?</button>',
"m038": '<button class="chip" type="button" data-q="pvs">Was haben PVS-Hersteller und MVZ davon?</button>',
"m039": '<p class="trust">Erfahrung aus <b>3 öffentlich geförderten Datenräumen</b> · Konnektor auf <b>Microsoft Azure</b> mit Daten in der EU</p>',
"m040": '<h2>Die ePA steht. Wir liefern die fehlenden Bausteine.</h2>',
"m041": '<p>Wir suchen einen Hersteller von Praxissoftware oder einen auf Gesundheitstelematik spezialisierten Azure-Integrator, sowie MVZ und Ketten, die ihre Ergebnisse vergleichen wollen.</p>',
"m042": '<a class="tbtn white" href="#contacto">Gespräch vereinbaren</a><button class="tbtn outline" type="button" data-open-assistant>Assistenten fragen</button>',
"m043": '<div class="cap">Was Partner erhalten</div>',
"m044": '<b>Datenqualität vor dem Hochladen</b><span>Prüfung von Format und Inhalt, bevor Daten in ePA oder Katalog gelangen.</span>',
"m045": '<b>Föderierte Analysen für MVZ</b><span>Ergebnisse zwischen Standorten vergleichen, ohne Akten zu migrieren.</span>',
"m046": '<b>EHDS-bereite Konnektoren</b><span>Interoperabilität und Protokollierung für Praxissoftware, ohne Eigenentwicklung.</span>',
"m047": '<b>Weniger Aufwand in der Praxis</b><span>Die Lösung muss Zeit sparen, nicht zusätzliche Bürokratie erzeugen.</span>',
"m088": '<a class="flogo" href="/de/" aria-label="Dental Data Deutschland, Startseite">',
"m090": '<div><h4>Länder</h4><a href="/nl/" lang="nl">Nederland</a><a href="/nl-be/" lang="nl">België</a><a href="/fr-be/" lang="fr">Belgique</a><a href="/">Alle Länder</a></div>',
"m094": '<div><h4>Kontakt</h4><a href="#contacto">Gespräch vereinbaren</a>',
"m095": '<a href="/en/" lang="en">Dental Data Europe</a></div>',
"m096": 'stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.8 2.5 15.2 0 18M12 3c-2.5 2.8-2.5 15.2 0 18"/></svg>Deutsch (Deutschland)</span>',
"m109": "bot(['Hallo! Ich bin der Assistent von Dental Data. Ich erkläre Ihnen, wie der föderierte zahnmedizinische Datenraum funktioniert, wie er ePA und FDZ Gesundheit ergänzt und was der Europäische Gesundheitsdatenraum für Zahnarztpraxen bedeutet.','Wählen Sie eine Frage oder schreiben Sie Ihre eigene. Bitte geben Sie keine personenbezogenen Daten oder Patientendaten ein: Wir speichern Fragen und Antworten anonym, um den Assistenten zu verbessern.'],['datos','epa','ehds','ia','pvs'],true)",
"m115": "['datos','ehds','pvs','tecnologia']",
"m116": "idioma:'de',pais:'de'",
"m118": "var FUENTES={'01-que-es-dental-data.md':'Was Dental Data ist','03-solucion-casos-uso.md':'Lösung und Anwendungsfälle','05-tecnologia.md':'Technologie','08-empresa-recursos.md':'Software in a Box','10-estudio-comparativo-en.md':'Vergleichsstudie (PDF)','11-ehds-europa.md':'Der EHDS in Europa','pais/de.md':'Dental Data in Deutschland'}",
}

REEMPLAZOS = desde_claves(TEXTOS) + [
('<li><a href="/de/" hreflang="de-DE" lang="de">Deutsch · Deutschland</a></li>', '<li><a href="/de/" hreflang="de-DE" lang="de" aria-current="page">Deutsch · Deutschland</a></li>'),
]
