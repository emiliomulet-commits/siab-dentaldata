import importlib.util as _u, os as _o, copy as _c
_s = _u.spec_from_file_location("_nl", _o.path.join(_o.path.dirname(__file__), "nl.py")); _b = _u.module_from_spec(_s); _s.loader.exec_module(_b)
LANG = "nl-BE"
UI = dict(_b.UI)

def _sub(piece, pares):
    seg, loc, anc = _c.deepcopy(piece); loc = " ".join(loc.split())
    for a, b in pares:
        seg = [x.replace(a, b) for x in seg]; loc = loc.replace(a, b); anc = [x.replace(a, b) for x in anc]
    return (seg, loc, anc)

PIEZAS = {}
PIEZAS["p02"] = _sub(_b.PIEZAS["p02"], [("Zorgverzekeraar", "Ziekenfonds"), ("keten of zorgverzekeraar", "groep of ziekenfonds"), ("Tandartsketen", "Praktijkgroep")])
PIEZAS["p06"] = _sub(_b.PIEZAS["p06"], [("Toezicht op medische hulpmiddelen: IGJ", "Medische hulpmiddelen: FAGG · AI-autoriteit nog aan te wijzen")])
PIEZAS["p08"] = _c.deepcopy(_b.PIEZAS["p08"])
PIEZAS["p09"] = _sub(_b.PIEZAS["p09"], [("Uw praktijksoftware", "Uw erkende software (eHealth)")])
PIEZAS["p11"] = _c.deepcopy(_b.PIEZAS["p11"])

# p03: zelfde structuur als /nl/, kader van België
_p3 = list(_b.PIEZAS["p03"][0])
_p3[3] = "Bronnen: Dental Data (kennisbank) · AVG · wet van 30 juli 2018 · wet patiëntenrechten · Verordening (EU) 2025/327, art. 54 en 71 · Algemene informatie; geen juridisch advies"
_i = _p3.index("Nederlandse"); _p3[_i] = "Belgische"; _p3[_i + 1] = "Wet van 30 juli 2018 · Gegevensbeschermingsautoriteit (GBA)"
_i = _p3.index("WGBO"); _p3[_i] = "patiëntenrechten"; _p3[_i + 1] = "Patiëntendossier: 30 jaar bewaard"
PIEZAS["p03"] = (_p3, """Verlaten de gegevens de praktijk? Nee. Geen enkel identificeerbaar dossier verlaat de praktijk. Elk gebruik van de gegevens is
 geregeld door een digitaal contract dat bepaalt wie toegang krijgt, waarvoor en hoelang. En dat contract blijft niet op papier: de
 machine dwingt het zelf af. Als een verzoek geen contract heeft, is er geen toegang. Heeft het er wel een, dan komt alleen een
 geaggregeerd resultaat terug. De praktijk beslist altijd, binnen de algemene verordening gegevensbescherming en de Belgische
 wetgeving over patiëntenrechten. En met een duidelijke regel van de EHDS: gezondheidsgegevens worden nooit gebruikt voor reclame.""",
 ["Verlaten de gegevens", "Elk gebruik", "Als een verzoek", "De praktijk beslist", "FIN"])

PIEZAS["p01"] = ([
 "Waarom ontbreken tandheelkundige gegevens in de Europese ruimte voor gezondheidsgegevens?",
 "Waarom ontbreken tandheelkundige gegevens in de EHDS?",
 "Geanimeerde presentatie van Dental Data: waarom tandzorg de grote afwezige is in de Europese ruimte voor gezondheidsgegevens (EHDS).",
 "Bronnen: vergelijkende studie van Software in a Box (nov. 2026) · RIZIV (conventie 2026) · Gezondheidsenquête Sciensano",
 "Opening", "Dental Data · Vraag 1", "Waarom ontbreken tandheelkundige gegevens in de", "Europese ruimte voor gezondheidsgegevens", "?",
 "De grote afwezigen", "Europese ruimte voor gezondheidsgegevens (EHDS)", "Tandheelkundige gegevens zijn", "de grote afwezigen",
 "Patiëntendossier", "Elektronisch voorschrift", "Medische beelden", "Laboratoriumuitslagen", "Tandzorg", "niet verbonden",
 "Waarom", "Niet door gebrek aan waarde, maar door", "hoe de tandzorg", "is georganiseerd",
 "Verplichte verzekering", "Elke prestatie gecodeerd", "Elektronische facturatie", "Sinds 2025",
 "Erkende software", "Elke praktijk de zijne", "Geen resultaatgegevens", "Gefactureerd, niet gemeten",
 "België in cijfers", "België", "Verzekerd, gecodeerd en toch onzichtbaar",
 "60", "&lt;small&gt;,48 %&lt;/small&gt;", "zestig", "0", "geconventioneerd", "van de tandartsen is geconventioneerd",
 "19", ".", "&lt;small&gt;&amp;lt;&lt;/small&gt;", "negentien", "0", "gratis", "jaar: basistandzorg gratis",
 "4", ".", "vier", "0", "Belgen", "één op vier Belgen gaat niet jaarlijks naar de tandarts",
 "Eilanden van gegevens", "De gegevens bestaan, maar leven", "op eilanden", "gemeten", "Prestaties gefactureerd, resultaten niet gemeten",
 "software", "Geen verbinding tussen praktijken",
 "Afsluiting", "De gegevens bestaan.", "Niemand verbindt ze.", "Dental Data verbindt ze", "zonder ze te verplaatsen", ".",
], """Tandheelkundige gegevens zijn de grote afwezigen in de Europese ruimte voor gezondheidsgegevens. In België zit de tandzorg
 nochtans in de verplichte verzekering: elke terugbetaalde prestatie heeft haar code en wordt sinds september tweeduizend vijfentwintig
 elektronisch gefactureerd. Jongeren onder de negentien krijgen de basiszorg gratis, zestig procent van de tandartsen is
 geconventioneerd, en toch gaat één op de vier Belgen niet elk jaar naar de tandarts. Niemand weet of de behandelingen die betaald worden
 ook werken: de prestaties worden gefactureerd, de resultaten worden niet gemeten. De klinische gegevens bestaan en zitten in elke
 praktijk, in haar eigen software. Wat ontbreekt, is iemand die ze verbindt. Dat is Dental Data.""",
 ["Tandheelkundige gegevens zijn", "In België zit", "Jongeren onder de negentien", "Niemand weet of", "De klinische gegevens bestaan"])

PIEZAS["p04"] = ([
 "Wat levert het een groep van praktijken op?", "Wat levert het een praktijkgroep op?",
 "Geanimeerde presentatie van Dental Data: vergelijkbare kwaliteitsindicatoren tussen praktijken zonder dossiers te migreren.",
 "Bronnen: Dental Data · toepassingen en pilot (kennisbank) · Raad voor de Tandheelkunde (2025) · RIZIV-nomenclatuur · Verordening (EU) 2025/327, art. 72 · Illustratieve staven",
 "Opening", "Dental Data · Vraag 4", "Wat levert het een", "praktijkgroep", "op?",
 "Het probleem", "Financiële groepen kopen praktijken…", "en elke praktijk heeft eigen software",
 "Praktijk 1", "Software A", "Praktijk 2", "Software B", "Praktijk 3", "Software C", "Praktijk 4", "Software D", "Praktijk 5", "Software E",
 "migreren", "Geen specifieke regels voor ketens · vergelijken betekent vandaag dossiers migreren",
 "Zonder migratie", "Met Dental Data is dat niet nodig:", "een connector naast elke software",
 "Praktijk 1", "Software A", "Connector", "Praktijk 2", "Software B", "Connector", "Praktijk 3", "Software C", "Connector",
 "Praktijk 4", "Software D", "Connector", "Praktijk 5", "Software E", "Connector",
 "Vergelijkbare indicatoren", "Dezelfde indicator,", "berekend in elke praktijk",
 "Praktijk 1", "Praktijk 2", "Praktijk 3", "Praktijk 4", "Praktijk 5",
 "Dezelfde definitie, gekoppeld aan de codes van de RIZIV-nomenclatuur", "van plek", "Geen enkel dossier verandert van plek",
 "Meerwaarde", "Bovendien…", "Aantoonbare kwaliteit", "Nog vóór de regels er zijn.",
 "voorbereid", "Voorbereid op de norm van morgen", "Advies van de Raad voor de Tandheelkunde (2025).",
 "Afsluiting", "Aantoonbare kwaliteit,", "zonder één dossier te migreren.", "Vergelijkbare kwaliteitsindicatoren in de hele groep.",
], """In België kopen financiële groepen tandartspraktijken en vormen ze ketens, met praktijken die elk hun eigen software gebruiken.
 De Raad voor de Tandheelkunde waarschuwde in tweeduizend vijfentwintig dat ons land een van de weinige is zonder regels voor die ketens,
 en vroeg dat kwaliteit voorop zou staan. Kwaliteit vergelijken tussen praktijken betekent vandaag dossiers migreren. Met Dental Data is
 dat niet nodig: naast elke software wordt een connector geïnstalleerd, en de indicatoren worden in elke praktijk berekend met dezelfde
 definitie, gekoppeld aan de codes van de nomenclatuur. De directie ziet vergelijkbare resultaten, zonder dat er één dossier van plek
 verandert. Een groep die vandaag haar kwaliteit meet, is voorbereid op de norm van morgen.""",
 ["In België kopen", "Met Dental Data", "De directie ziet", "zonder dat er één dossier van plek", "Een groep die"])

PIEZAS["p05"] = ([
 "Wat levert het een ziekenfonds op?", "Wat levert het een ziekenfonds op?",
 "Geanimeerde presentatie van Dental Data: van gefactureerde prestatie naar gemeten resultaat, zonder dossiers te centraliseren.",
 "Bronnen: Dental Data (kennisbank) · RIZIV · InterMutualistisch Agentschap (IMA) · Verordening (EU) 2025/327, art. 54",
 "Opening", "Dental Data · Vraag 5", "Wat levert het een", "ziekenfonds", "op?",
 "Het netwerk", "Praktijken in heel België,", "elk met eigen software",
 "Ziekenfondsen", "RIZIV", "nomenclatuur", "IMA", "eAttest en eFact", "Praktijk", "eigen software",
 "Praktijk", "eigen software", "Prestaties bekend, resultaten niet",
 "Samenhangende gegevens", "Het resultaat van de zorg,", "zonder dossiers te centraliseren",
 "Ziekenfonds", "Praktijk", "eigen software", "Praktijk", "eigen software", "Praktijk", "eigen software", "Praktijk", "eigen software",
 "Berekend in elke praktijk · alleen het geaggregeerde resultaat komt terug",
 "Een kanaal", "Om het", "mondzorgtraject te evalueren", "Mondzorgtraject", "Gratis zorg < 19 jaar", "cone beam", "Dataruimte voor tandzorg",
 "Duidelijke grenzen", "Met duidelijke grenzen:", "wat de EHDS verbiedt", "reclame", "Reclame",
 "Gezondheidsgegevens worden nooit voor reclame gebruikt.", "beslissingen", "Nadelige beslissingen",
 "Ook niet voor beslissingen die mensen benadelen.", "Verordening (EU) 2025/327, artikel 54",
 "Afsluiting", "Van gefactureerde prestatie", "naar gemeten resultaat.", "Zonder dossiers te centraliseren.",
], """In België betalen de ziekenfondsen de tandzorg terug, en het InterMutualistisch Agentschap analyseert de facturatie van allemaal.
 Ze weten welke prestaties betaald worden, maar niet welk resultaat ze hebben. Dental Data geeft hun dat resultaat zonder dossiers te
 centraliseren: de indicator wordt in elke praktijk berekend en alleen het aggregaat komt terug. Zo kan men nagaan of het
 mondzorgtraject de tandgezondheid verbetert, wat de gratis zorg voor jongeren onder de negentien oplevert of hoe de cone beam gebruikt
 wordt. Met duidelijke grenzen: de EHDS verbiedt deze gegevens te gebruiken voor reclame of voor beslissingen die mensen benadelen. Van
 gefactureerde prestatie naar gemeten resultaat, zonder dossiers te centraliseren.""",
 ["In België betalen", "Dental Data geeft", "Zo kan men", "Met duidelijke grenzen", "Van gefactureerde"])

_p7 = list(_b.PIEZAS["p07"][0])
_p7[2] = "Geanimeerde presentatie van Dental Data: de kalender van de EHDS en de Belgische uitvoering (Health Data Agency)."
_p7[3] = "Bronnen: Verordening (EU) 2025/327 (art. 50 en 105) · wet van 2023 tot oprichting van de Health Data Agency · eHealth-platform"
_i = _p7.index("ketens · KNMT · zorgverzekeraars"); _p7[_i] = "verenigingen · ziekenfondsen · praktijkgroepen"
_i = _p7.index("Wet GIS (wetsvoorstel)"); _p7[_i - 2] = "België"; _p7[_i - 1] = "België"; _p7[_i] = "Health Data Agency (wet van 2023)"
_p7[_i + 1] = "catalogus"
_p7[_i + 2] = "Nationale catalogus en één loket; verwacht als toegangsorgaan, nog niet aangewezen. Het eHealth-platform zorgt voor de pseudonimisering."
_p7[_i + 3] = "pseudonimisering"; _p7[_i + 4] = "Verwacht · nog niet aangewezen (nov. 2026)"
PIEZAS["p07"] = (_p7, """De Europese ruimte voor gezondheidsgegevens is al in werking en heeft data. In maart tweeduizend zevenentwintig heeft elk land
 zijn toegangsorganen aangewezen. In maart tweeduizend negenentwintig geldt het grootste deel van het secundaire gebruik, en in
 tweeduizend eenendertig komen de medische beelden. De meeste tandartspraktijken zijn micro-ondernemingen en zijn standaard vrijgesteld:
 om deel te nemen is een geaggregeerd kanaal nodig, via verenigingen, ziekenfondsen of praktijkgroepen. België was er vroeg bij: de Health
 Data Agency bestaat bij wet sinds tweeduizend drieëntwintig, heeft een nationale catalogus en zal naar verwachting het toegangsorgaan
 worden. Het eHealth-platform biedt al de pseudonimisering. Wie verbonden aankomt, wordt de natuurlijke gesprekspartner.""",
 ["De Europese ruimte", "In maart tweeduizend negenentwintig", "De meeste tandartspraktijken", "België was er", "Wie verbonden"])

PIEZAS["p10"] = ([
 "Hoe doet u mee met Dental Data?", "Hoe doet u mee met Dental Data?",
 "Geanimeerde presentatie van Dental Data: een institutionele alliantie in België, de routekaart en hoe u meedoet.",
 "Bronnen: Dental Data · partnerprogramma België en routekaart (kennisbank) · Geen gepubliceerde tarieven",
 "Opening", "Dental Data · Vraag 10", "Hoe doet u mee met", "Dental Data", "?",
 "We zoeken", "We zoeken", "Een institutionele alliantie", "Met de eerste ketens en praktijkgroepen als gebruikers",
 "alliantie", "Geen geïsoleerde pilot",
 "Financiering", "De eigen toepassing", "financiert de connector", "Groepen financieren de connector met hun interne toepassing; onderzoek met gedeelde projecten met de HDA en de ziekenfondsen.",
 "Routekaart", "De", "routekaart", "2027", "Eerste verbindingen", "verbindingen", "2027–2028",
 "Indicatoren afspreken met RIZIV, HDA en ziekenfondsen", "gecatalogiseerde", "2029", "Gecatalogiseerde datasets bij de HDA",
 "daarna", "2029–2031", "Lijn voor tandheelkundige beelden",
 "We willen ook praten met", "We willen ook praten met…", "RIZIV · HDA · eHealth · IMA", "verenigingen", "VVT en SMD",
 "raad", "Raad voor de Tandheelkunde", "software", "Erkende software", "groepen", "Praktijkgroepen",
 "Praten we?", "Praten we?", "partners@softwareinabox.eu", "+34 601 398 868", "dentaldata.softwareinabox.eu",
], """In België willen we niet beginnen met een geïsoleerde pilot, maar met een alliantie. We willen met het RIZIV, de Health Data
 Agency, het eHealth-platform en de ziekenfondsen de eerste indicatoren voor tandheelkundige resultaten bepalen, en met ketens en
 praktijkgroepen die nu al hun kwaliteit willen meten. De groepen financieren de connector met hun interne toepassing; het onderzoek met
 gedeelde projecten. In tweeduizend zevenentwintig de eerste verbindingen; in tweeduizend negenentwintig gecatalogiseerde datasets, klaar
 voor de HDA; daarna de tandheelkundige beelden. We willen ook praten met de verenigingen van tandartsen, de raad voor de tandheelkunde,
 de leveranciers van erkende software en de praktijkgroepen. Praten we? Schrijf naar partners apenstaartje softwareinabox punt eu.""",
 ["In België willen", "De groepen financieren", "In tweeduizend zevenentwintig", "We willen ook", "Praten we?"])
