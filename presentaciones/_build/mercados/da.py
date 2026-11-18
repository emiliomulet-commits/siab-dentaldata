LANG = "da"
UI = {
 "rm": "Reduceret bevægelse: hver scene vises i sin helhed.", "ini": "Tryk på → eller mellemrumstasten for at starte",
 "locucion": "🔊 Speak slået til", "ctl": "Styring af præsentationen", "ant": "Forrige scene", "pp": "Afspil eller pause",
 "sig": "Næste scene", "pista": "← → mellemrum · 1–{n} · F · H skjuler", "pc": "Fuld skærm",
 "escena": "Scene", "quitar": "🔇 Lyd fra", "activar": "🔊 Lyd til", "ver": "▶ Se med speak (lyd til)",
}
PIEZAS = {
"p01": ([
 "Hvorfor mangler tandlægedata i det europæiske sundhedsdataområde?",
 "Hvorfor mangler tandlægedata i EHDS?",
 "Animeret præsentation fra Dental Data: hvorfor tandplejen er den store fraværende i det europæiske sundhedsdataområde (EHDS).",
 "Kilder: sammenlignende undersøgelse fra Software in a Box (nov. 2026) · Sundhedsdatastyrelsen (SCOR) · Tandlægeforeningen",
 "Indledning", "Dental Data · Spørgsmål 1", "Hvorfor mangler tandlægedata i det", "europæiske sundhedsdataområde", "?",
 "De store fraværende", "Det europæiske sundhedsdataområde (EHDS)", "Tandlægedata er", "de store fraværende",
 "Patientoversigt", "E-recept", "Medicinske billeder", "Laboratoriesvar", "Tandpleje", "ikke forbundet",
 "Hvorfor", "Ikke af mangel på værdi, men på grund af", "måden tandplejen", "er organiseret på",
 "SCOR kun for børn", "Børne- og ungdomstandpleje", "Voksne i private klinikker", "Uden for registret",
 "Egen software", "Hver klinik sin", "Kun tilskud ses", "Ikke hvordan munden har det",
 "Danmark i tal", "Danmark", "Verdens bedste registre, men ikke for voksne",
 "21", "&lt;small&gt; år&lt;/small&gt;", "enogtyve", "0", "gratis", "gratis kommunal tandpleje op til 21 år",
 "4931", ".", "&lt;small&gt;&lt;/small&gt;", "femtusind", "0", "tandlæger", "tandlæger i Danmark",
 "54", ".", "halvtreds", "0", "SCOR-registret", "år med SCOR-registret (siden 1972)",
 "Dataøer", "Dataene findes, men de lever", "på øer", "software", "Voksnes kliniske data: intet register",
 "forbindelse", "Klinikker uden forbindelse",
 "Afslutning", "Dataene findes.", "Ingen forbinder dem.", "Dental Data forbinder dem", "uden at flytte dem", ".",
], """Tandlægedata er de store fraværende i det europæiske sundhedsdataområde, selv i Danmark, der har nogle af verdens bedste
 registre. Børn og unge får gratis kommunal tandpleje og registreres i SCOR, men voksne går til private klinikker, og om dem ved man kun,
 hvilke behandlinger der får tilskud, ikke hvordan munden har det. Tandplejen er gratis op til enogtyve år, knap femtusind tandlæger
 arbejder i landet, og i over halvtreds år har SCOR-registret fulgt børnenes tænder. Hver klinik gemmer de voksnes data i sin egen
 software, uden forbindelse til de andre, og med den nye tandkonto skal man vide, om den virker. Det, der mangler, er nogen, der
 forbinder dataene. Det er Dental Data.""",
 ["Tandlægedata er de", "Børn og unge", "Tandplejen er gratis", "Hver klinik gemmer", "Det, der mangler"]),

"p02": ([
 "Hvordan fungerer et fødereret dataområde?", "Hvordan fungerer et fødereret dataområde?",
 "Animeret præsentation fra Dental Data: hvordan et fødereret dataområde for tandpleje fungerer.",
 "Kilde: Dental Data · løsningen og anvendelserne (offentlig vidensbase)",
 "Indledning", "Dental Data · Spørgsmål 2", "Hvordan fungerer et", "fødereret", "dataområde?",
 "Klinikken", "Hver deltager beholder sine journaler", "i sin egen software", "ved siden af", "Kliniksystem", "journaler og røntgenbilleder",
 "installeres", "Konnektor", "installeres ved siden af",
 "Netværket", "Konnektorerne danner et netværk med et", "fælles katalog", "Fælles katalog", "kun metadata",
 "Klinik", "+ konnektor", "Klinik", "+ konnektor", "Kæde", "+ konnektor", "Region eller forsikring", "+ konnektor",
 "Kataloget siger, hvilke data der findes. Det gemmer dem ikke.",
 "Et spørgsmål", "Spørgsmålet rejser;", "kun resultatet kommer tilbage", "Fælles katalog", "kun metadata",
 "Klinik", "+ konnektor", "Klinik", "+ konnektor", "Kæde", "+ konnektor", "Region eller forsikring", "+ konnektor",
 "1 · Spørgsmålet rejser", "2 · Beregnes i hver klinik", "3 · Det aggregerede resultat kommer tilbage",
 "Hvad rejser, og hvad gør ikke", "Hvad går over netværket…", "og hvad gør ikke", "Rejser", "Samtykker", "Katalogets metadata",
 "Aggregerede resultater", "Rejser ikke", "Identificerbare journaler", "Røntgenbilleder",
 "Afslutning", "Dataene bliver.", "Svaret rejser.", "Sådan fungerer et fødereret dataområde.",
], """I et fødereret dataområde beholder hver klinik, kæde, region eller forsikring sine journaler i sit eget kliniksystem. Ved siden af
 systemet installeres en konnektor. Konnektoren offentliggør i et fælles katalog, hvilke data der findes, men ikke selve dataene. Når nogen
 har brug for en indikator, rejser spørgsmålet til hver klinik, beregnes der, og kun det aggregerede resultat kommer tilbage. Over
 netværket går samtykker, metadata og resultater. Aldrig en identificerbar journal. Dataene bliver i klinikken. Det, der rejser, er
 svaret.""",
 ["I et fødereret", "Konnektoren offentliggør", "Når nogen", "Over netværket", "Dataene bliver"]),

"p03": ([
 "Forlader mine data klinikken?", "Forlader mine data klinikken?",
 "Animeret præsentation fra Dental Data: databeskyttelse, brugskontrakter og klinikkens kontrol over sine data.",
 "Kilder: Dental Data (vidensbase) · GDPR · databeskyttelsesloven · forordning (EU) 2025/327, art. 54 og 71 · Generel information; ikke juridisk rådgivning",
 "Indledning", "Dental Data · Spørgsmål 3", "Forlader mine data", "klinikken", "?",
 "Svaret", "Nej.", "Ingen identificerbar journal", "forlader klinikken",
 "Kontrakten", "Hver brug af dataene har", "en digital kontrakt", "Brugskontrakt (ODRL)",
 "hvem der får adgang", "Hvem får adgang?", "til hvad", "Til hvad?", "hvor længe", "Hvor længe?",
 "kontrakten", "Og den bliver ikke på papiret:", "maskinen", "maskinen", "håndhæver den selv",
 "Maskinen håndhæver den", "Uden kontrakt ingen adgang.", "Med kontrakt kun et aggregeret resultat.",
 "har den en", "Anmodning", "uden kontrakt", "har den en", "Anmodning", "med kontrakt", "Klinik", "med sin konnektor",
 "ingen adgang", "Adgang nægtet", "kun et", "aggregeret", "Aggregeret resultat",
 "Rammen", "Klinikken bestemmer altid,", "inden for loven", "databeskyttelsesforordning", "GDPR", "databeskyttelsesloven",
 "Databeskyttelsesloven", "datatilsynet", "Datatilsynet",
 "aldrig", "EHDS · art. 54: aldrig til reklame", "reklame",
 "EHDS · art. 71: patienten kan gøre indsigelse",
 "Afslutning", "Uden kontrakt", "ingen adgang.", "Klinikken bestemmer altid.",
], """Forlader dataene klinikken? Nej. Ingen identificerbar journal forlader klinikken. Hver brug af dataene er reguleret af en digital
 kontrakt, der fastlægger, hvem der får adgang, til hvad og hvor længe. Og kontrakten bliver ikke på papiret: maskinen håndhæver den selv.
 Hvis en anmodning ikke har en kontrakt, er der ingen adgang. Har den en, kommer kun et aggregeret resultat tilbage. Klinikken bestemmer
 altid, inden for den generelle databeskyttelsesforordning og databeskyttelsesloven, under tilsyn af Datatilsynet. Og med en klar regel
 i det europæiske sundhedsdataområde: sundhedsdata bruges aldrig til reklame.""",
 ["Forlader dataene", "Hver brug", "Hvis en anmodning", "Klinikken bestemmer", "FIN"]),

"p04": ([
 "Hvad får en kæde ud af det?", "Hvad får en kæde ud af det?",
 "Animeret præsentation fra Dental Data: sammenlignelige kvalitetsindikatorer mellem klinikker uden at flytte journaler.",
 "Kilder: Dental Data · anvendelser og pilot (vidensbase) · autorisationsloven (ejerskabsregler) · Dansk Tandsundhed · forordning (EU) 2025/327, art. 72 · Illustrative søjler",
 "Indledning", "Dental Data · Spørgsmål 4", "Hvad får en", "kæde", "ud af det?",
 "Problemet", "En kæde vokser med nye klinikker…", "og hver klinik har sin egen software",
 "Klinik 1", "Software A", "Klinik 2", "Software B", "Klinik 3", "Software C", "Klinik 4", "Software D", "Klinik 5", "Software E",
 "migrere", "Begrænset ejerskab: flertal hos en tandlæge, højst to klinikker · at sammenligne kræver i dag at migrere journaler",
 "Uden migrering", "Med Dental Data er det ikke nødvendigt:", "en konnektor ved siden af hver software",
 "Klinik 1", "Software A", "Konnektor", "Klinik 2", "Software B", "Konnektor", "Klinik 3", "Software C", "Konnektor",
 "Klinik 4", "Software D", "Konnektor", "Klinik 5", "Software E", "Konnektor",
 "Sammenlignelige indikatorer", "Den samme indikator,", "beregnet i hver klinik",
 "Klinik 1", "Klinik 2", "Klinik 3", "Klinik 4", "Klinik 5",
 "Indikatorer afstemt med SCOR, hvor det er muligt (caries, hygiejne)", "journal", "Ingen journal udleveres",
 "Merværdi", "Og desuden…", "Dokumenterbar kvalitet", "Data til debatten om kvalitet og ejerskab.",
 "debatten", "Data til debatten", "Over hundrede klinikker i Dansk Tandsundhed.",
 "Afslutning", "Dokumenterbar kvalitet,", "uden at migrere en eneste journal.", "Sammenlignelige kvalitetsindikatorer i hele kæden.",
], """I Danmark har tandlægekæder grænser: kun en tandlæge må eje flertallet af en klinik, og ingen må eje mere end to uden særlig
 tilladelse. Alligevel tæller kæderne i Dansk Tandsundhed over hundrede klinikker, og de tilbyder at dele data til forskning. Hver klinik
 bruger sin egen software, og at sammenligne kvaliteten kræver at migrere journaler. Med Dental Data er det ikke nødvendigt: en konnektor
 ved siden af hver software beregner indikatorerne i klinikken, med samme definition som børneregistret, når det er muligt. Kæden ser
 sammenlignelige resultater og kan bidrage med data til debatten om kvalitet og ejerskab, uden at udlevere en eneste journal.""",
 ["I Danmark har", "Med Dental Data", "Kæden ser", "og kan bidrage", "uden at udlevere en eneste journal."]),

"p05": ([
 "Hvad får regionerne ud af det?", "Hvad får regionerne ud af det?",
 "Animeret præsentation fra Dental Data: kliniske data til at evaluere tandkontoen uden at centralisere journaler.",
 "Kilder: Dental Data (vidensbase) · aftale om tandkonto (2025) · forordning (EU) 2025/327, art. 54",
 "Indledning", "Dental Data · Spørgsmål 5", "Hvad får", "regionerne", "ud af det?",
 "Netværket", "Private klinikker,", "hver med sin egen software",
 "Regioner", "Tilskud til voksne", "i dag", "Tandkonto", "fra slutningen af 2027", "Privat klinik", "egen software",
 "Privat klinik", "egen software", "Ingen kliniske data om voksne",
 "Sammenhængende data", "Kliniske data fra hele netværket,", "uden at centralisere journaler",
 "Region", "Klinik", "egen software", "Klinik", "egen software", "Klinik", "egen software", "Klinik", "egen software",
 "Beregnet i hver klinik · kun aggregatet kommer tilbage",
 "En kanal", "Til at", "evaluere tandkontoen", "Gratis eftersyn", "Behandling bagefter", "virker", "Dataområde for tandpleje",
 "Klare grænser", "Med klare grænser:", "hvad EHDS forbyder", "reklame", "Reklame",
 "Sundhedsdata bruges aldrig til reklame.", "beslutninger", "Skadelige beslutninger",
 "Heller ikke til beslutninger, der skader mennesker.", "Forordning (EU) 2025/327, artikel 54",
 "Afslutning", "Evaluér reformen med data,", "uden at centralisere journaler.", "Med kontrollen altid i klinikken.",
], """I Danmark giver regionerne tilskud til en del af voksnes tandpleje, og fra slutningen af totusind syvogtyve skal de administrere
 en årlig tandkonto for alle over enogtyve år. Reformen har kritikere: tandlæger og ældreorganisationer frygter, at et gratis eftersyn
 hjælper lidt, hvis behandlingen bagefter ikke er til at betale. For at vide, om den virker, kræves kliniske data om voksne, som ikke
 findes i dag. Dental Data leverer dem uden at centralisere journaler: indikatoren beregnes i hver klinik, og kun aggregatet kommer
 tilbage. Med klare grænser: EHDS forbyder at bruge disse data til reklame eller til beslutninger, der skader mennesker. Evaluér
 reformen med data, uden at centralisere journaler.""",
 ["I Danmark giver", "For at vide", "Dental Data leverer", "Med klare grænser", "Evaluér reformen"]),

"p06": ([
 "AI på røntgenbilleder uden at flytte røntgenbillederne", "Hvordan fungerer AI på tandrøntgenbilleder?",
 "Animeret præsentation fra Dental Data: fødereret læring og fortrolig beregning på tandbilleder.",
 "Kilder: Dental Data (vidensbase) · forordning (EU) 2026/1744 · forordning (EU) 2025/327 · Model i klinisk validering; erstatter ikke diagnosen · Medicinsk udstyr: Lægemiddelstyrelsen · AI: Digitaliseringsstyrelsen",
 "Indledning", "Dental Data · Spørgsmål 6", "Hvordan træner man en", "AI til tandpleje", "uden at flytte røntgenbillederne?",
 "Dilemmaet", "At træne AI kræver mange røntgenbilleder…", "at samle dem er en risiko", "Et centralt lager",
 "At centralisere røntgenbilleder øger risikoen",
 "Algoritmen rejser", "Dental Data vender vejen om:", "algoritmen rejser", "AI-model",
 "Klinik", "røntgenbillederne bliver", "Klinik", "røntgenbillederne bliver", "Klinik", "røntgenbillederne bliver",
 "lærer", "Lærer i hver klinik", "sender", "Sender kun det lærte tilbage",
 "Fortrolig beregning", "Fortrolig", "beregning", "Beskytter dataene, også mens de behandles.",
 "Modellen", "Første model", "Approksimal caries", "På tandrøntgenbilleder.", "knogletab", "Parodontalt knogletab",
 "På tandrøntgenbilleder.", "validering", "I klinisk validering", "hjælp", "En hjælp til tandlægen: erstatter ikke diagnosen",
 "Det, der kommer", "Klar til", "det, der kommer", "2. aug. 2028", "AI-forordningen: krav til AI i medicinsk udstyr",
 "totusind enogtredive", "26. mar. 2031", "Medicinske billeder kommer ind i det europæiske sundhedsdataområde",
 "Afslutning", "Algoritmen", "går til dataene.", "AI på tandbilleder uden at flytte røntgenbilleder.",
], """At træne en AI til tandpleje kræver mange røntgenbilleder. Men at samle dem ét sted er en risiko. Dental Data vender vejen om:
 algoritmen rejser til hver klinik, lærer der og sender kun det lærte tilbage, aldrig billederne. Beregningerne sker med fortrolig
 beregning, som beskytter dataene, mens de behandles. Den første model, for approksimal caries og parodontalt knogletab, er i klinisk
 validering. Den er en hjælp til tandlægen: den erstatter ikke diagnosen. Og den forbereder sig på det, der kommer: i totusind
 enogtredive kommer medicinske billeder ind i det europæiske sundhedsdataområde. Algoritmen går til dataene.""",
 ["At træne en AI", "Dental Data vender", "Beregningerne sker", "Den første model", "Og den forbereder", "Algoritmen går"]),

"p07": ([
 "Hvilke datoer fastsætter det europæiske sundhedsdataområde?", "Hvilke datoer fastsætter EHDS?",
 "Animeret præsentation fra Dental Data: tidsplanen for EHDS og situationen i Danmark (Digital Health Denmark).",
 "Kilder: forordning (EU) 2025/327 (art. 50 og 105) · Indenrigs- og Sundhedsministeriet (2026) · Sundhedsdatastyrelsen",
 "Indledning", "Dental Data · Spørgsmål 7", "Hvilke datoer fastsætter det", "europæiske sundhedsdataområde", "?",
 "Tidslinje", "Allerede i kraft", "og med datoer", "26. mar. 2025", "I kraft", "totusind syvogtyve", "26. mar. 2027",
 "Adgangsorganer udpeget", "totusind niogtyve", "26. mar. 2029", "Sekundær brug: de fleste regler",
 "totusind enogtredive", "26. mar. 2031", "Medicinske billeder, som røntgenbilleder",
 "Vinduet", "Mellem 2027 og 2029:", "to år til at forbinde klinikker og kæder",
 "26. mar. 2025", "I kraft", "26. mar. 2027", "Adgangsorganer udpeget", "26. mar. 2029", "Sekundær brug: de fleste regler",
 "26. mar. 2031", "Medicinske billeder, som røntgenbilleder",
 "Artikel 50", "De fleste klinikker er små virksomheder:", "fritaget som udgangspunkt", "deltage", "gennem",
 "Selvstændige klinikker", "Art. 50: fritaget, medmindre staten beslutter andet", "aggregeret kanal", "Aggregeret kanal",
 "kæder · Tandlægeforeningen", "gennem", "Dataområde for tandpleje",
 "Danmark", "Danmark", "Digital Health Denmark (1.1.2027)", "metadatakatalog",
 "Samler Sundhedsdatastyrelsen, sundhed.dk og MedCom. Adgangsorgan og nationalt metadatakatalog under forberedelse; voksnes tandlægedata mangler.",
 "forberedelse", "Adgangsorgan under forberedelse (nov. 2026)",
 "Afslutning", "Den, der er forbundet i 2029,", "bliver den naturlige partner", "for adgangsorganerne for sundhedsdata.",
], """Det europæiske sundhedsdataområde er allerede i kraft og har datoer: adgangsorganer i marts totusind syvogtyve, sekundær brug i
 marts totusind niogtyve og medicinske billeder i totusind enogtredive. De fleste klinikker er små og fritaget som udgangspunkt: for at
 deltage kræves en aggregeret kanal, gennem kæderne eller tandlægeforeningen. Danmark samler den første januar totusind syvogtyve
 Sundhedsdatastyrelsen, sundhed.dk og MedCom i en ny styrelse og forbereder sit adgangsorgan og et nationalt metadatakatalog, men det er
 stadig under forberedelse. Voksnes tandlægedata er det, der mangler i kataloget. Den, der kommer forbundet, bliver den naturlige
 partner.""",
 ["Det europæiske", "marts totusind niogtyve", "De fleste klinikker", "Danmark samler", "Den, der kommer"]),

"p08": ([
 "Hvilken teknologi ligger bag Dental Data?", "Hvilken teknologi ligger bag Dental Data?",
 "Animeret præsentation fra Dental Data: Microsoft inde i knuden, åbne europæiske standarder ved grænserne.",
 "Kilder: Dental Data · teknologi og virksomhed (vidensbase) · Microsoft og Azure er varemærker tilhørende Microsoft Corporation; nævnt som tekst",
 "Indledning", "Dental Data · Spørgsmål 8", "Hvilken teknologi ligger bag", "Dental Data", "?",
 "Reglen", "Én enkel regel", "Microsoft", "Azure", "data i EU", "Inde i knuden", "Ved grænsen: åbne standarder",
 "Inde i knuden", "Inde i knuden:", "Microsoft", "Konnektor på Microsoft Azure", "Med dataene i Den Europæiske Union.",
 "integreret", "Integreret", "Med klinikkens system.", "udrullet", "Udrullet af partnere", "Integratorer og Azure-partnere.",
 "Ved grænsen", "Ved grænserne:", "åbne europæiske standarder", "gaiax", "Gaia-X", "dataområdeprotokollen", "IDSA", "eclipse", "Dataspace Protocol",
 "eclipse edc", "Eclipse EDC", "verificerbare", "Verificerbare legitimationer", "fhir", "FHIR", "dicom", "DICOM", "healthdcatap", "HealthDCAT-AP",
 "Åben for alle", "Alle kan koble sig på,", "også uden Microsoft", "Knude på Azure", "Deltager uden Microsoft",
 "Åbne standarder", "Kobler sig på samme måde",
 "Erfaring", "Vi starter ikke fra nul:", "tre rigtige dataområder", "Global Data Care", "Sundhed, på Gaia-X og Pontus-X.",
 "PROCUREDATA", "Offentligt udbud.", "EcoDataNet", "Affald og cirkulær økonomi.",
 "Demonstratorer finansieret af SEDIA (2024–2026), med egne Eclipse-baserede konnektorer.",
 "Afslutning", "Microsoft inde i knuden.", "Åbne standarder ved grænserne.", "Et dataområde for tandpleje, åbent for alle.",
], """Dental Data følger en enkel regel: Microsoft inde i knuden, åbne standarder ved grænserne. Inde i hver knude kører konnektoren på
 Microsoft Azure, med dataene i Den Europæiske Union, integreret med klinikkens system og udrullet af Azure-partnere. Ved grænserne taler
 området åbne europæiske standarder: Gaia-X, dataområdeprotokollen, Eclipse EDC, verificerbare legitimationer, FHIR, DICOM og
 HealthDCAT-AP. Så kan enhver deltager koble sig på, også uden Microsoft. Og vi starter ikke fra nul: Software in a Box har allerede
 designet og drevet tre rigtige dataområder.""",
 ["følger en enkel", "Inde i hver", "Ved grænserne taler", "Så kan enhver", "Og vi starter", "FIN"]),

"p09": ([
 "Hvad tilbyder Dental Data industrien?", "Hvad tilbyder Dental Data industrien?",
 "Animeret præsentation fra Dental Data: real-world evidence under kontrakt for producenter, AI-virksomheder og kliniksystemer.",
 "Kilder: Dental Data (vidensbase) · forordning (EU) 2025/327, art. 54",
 "Indledning", "Dental Data · Spørgsmål 9", "Hvad tilbyder Dental Data", "industrien", "?",
 "Hvem", "Til dem, der skal vide,", "hvad der sker i klinikken", "Implantater", "materialer", "Materialer", "kunstig", "Kunstig intelligens",
 "skal", "Kliniksystemer",
 "Real-world evidence", "Real-world evidence,", "uden identificerbare data", "Industri", "spørgsmål under kontrakt",
 "Klinikker", "Klinikker", "Klinikker", "Aggregerede resultater kommer tilbage, aldrig journaler",
 "Til kliniksystemet", "Til kliniksystemet:", "en konnektor, der tilføjer tjenester", "Jeres kliniksystem",
 "Integreret konnektor", "Nye tjenester", "til jeres kunder",
 "Reglerne", "Reglerne", "ændrer sig ikke", "En kontrakt for hver brug", "Hvem, til hvad og hvor længe.", "kun aggregerede",
 "Kun aggregeret", "Ingen identificerbare data forlader klinikken.", "aldrig", "Aldrig reklame", "EHDS forbyder det (art. 54).",
 "Afslutning", "Ægte evidens,", "ordnet og under kontrakt.", "Til industrien og tandplejens software.",
], """For tandindustrien er real-world evidence meget værd. Producenter af implantater og materialer og virksomheder inden for kunstig
 intelligens skal vide, hvordan deres produkter klarer sig i klinikken. Dental Data tilbyder dem den evidens, ordnet og under kontrakt:
 spørgsmål, der besvares i klinikkerne, og aggregerede resultater, der kommer tilbage uden identificerbare data. For leverandører af
 kliniksystemer er konnektoren en komponent, der integreres i deres produkt og åbner nye tjenester for deres kunder. Reglerne ændrer sig
 ikke: en kontrakt for hver brug, kun aggregerede resultater og aldrig reklame. Ægte evidens, ordnet og under kontrakt.""",
 ["For tandindustrien", "Dental Data tilbyder", "For leverandører", "Reglerne ændrer", "Ægte evidens"]),

"p10": ([
 "Hvordan kommer man med i Dental Data?", "Hvordan kommer man med i Dental Data?",
 "Animeret præsentation fra Dental Data: et institutionelt samarbejde i Danmark, køreplanen og hvordan man kommer med.",
 "Kilder: Dental Data · partnerprogram Danmark og køreplan (vidensbase) · Ingen offentliggjorte priser",
 "Indledning", "Dental Data · Spørgsmål 10", "Hvordan kommer man med i", "Dental Data", "?",
 "Vi søger", "Vi søger", "Et institutionelt samarbejde", "Med kæderne som første brugere",
 "samarbejde", "Ikke en isoleret pilot",
 "Finansiering", "Den egne anvendelse", "finansierer konnektoren", "Kæderne finansierer konnektoren med deres anvendelse; evalueringen med offentlige projekter eller forskningsprojekter.",
 "Køreplan", "", "Køreplanen", "2027", "Første forbindelser", "forbindelser", "2027–2028",
 "Indikatorer for tandkontoen og voksne", "katalogiserede", "2029", "Katalogiserede datasæt til EHDS",
 "derefter", "2029–2031", "Linje for tandbilleder",
 "Vi vil også tale med", "Vi vil også tale med…", "Ministeriet · Digital Health Denmark", "regionerne", "Regioner",
 "kommunerne", "Kommuner", "tandlægeforeningen", "Tandlægeforeningen", "universiteterne", "Universiteter",
 "Skal vi tale sammen?", "Skal vi tale sammen?", "partners@softwareinabox.eu", "+34 601 398 868", "dentaldata.softwareinabox.eu",
], """I Danmark søger vi ikke en isoleret pilot, men et institutionelt samarbejde: med ministeriet, den nye styrelse for digital sundhed,
 regionerne og kommunerne, for at definere indikatorer, der kan evaluere tandkontoen og udvide logikken fra SCOR til voksne. Og med de
 kæder, der allerede vil dele data, som første brugere. Kæderne finansierer konnektoren med deres anvendelse; evalueringen med offentlige
 projekter eller forskningsprojekter. I totusind syvogtyve de første forbindelser; i totusind niogtyve katalogiserede datasæt; derefter
 tandbillederne. Vi vil også tale med tandlægeforeningen og universiteterne. Skal vi tale sammen? Skriv til partners snabel-a
 softwareinabox punktum eu.""",
 ["I Danmark søger", "Kæderne finansierer", "I totusind syvogtyve", "Vi vil også", "Skal vi tale"]),

"p11": ([
 "Hvad bygger vi på Microsoft Azure?", "Hvad bygger vi på Microsoft Azure?",
 "Animeret præsentation fra Dental Data: arkitekturen i dataområdet for tandpleje med komponenter fra Microsoft Azure og Eclipse EDC-konnektoren.",
 "Kilder: Dental Data · teknisk dokument (v1.3) og MVP-forslag (v1.4) · Officielle Microsoft-ikoner (Azure, Microsoft Entra og Microsoft Fabric), brugt efter deres vilkår for arkitekturdiagrammer · Microsoft, Azure, Entra, Fabric og navnene på deres tjenester er varemærker tilhørende Microsoft Corporation",
 "Indledning", "Dental Data · Spørgsmål 11", "Hvad bygger vi på", "Microsoft Azure", "?",
 "Reglen", "Én regel styrer designet", "Grænse · åbne standarder", "Knude · Microsoft Azure", "Microsoft", "inde i knuden",
 "Åbne standarder ved grænsen",
 "Klinikken", "1 · I", "klinikken", "Røntgenapparat", "røntgen, CBCT", "DICOM-gateway", "DICOM-gateway", "Orthanc · open source",
 "pseudonymiseres", "Pseudonymiseret ved kilden", "uden data, der identificerer patienten",
 "Dataknuden", "2 · ", "Dataknuden", "på Azure", "Dataknude · Microsoft Azure", "azure health", "Azure Health Data Services",
 "journalen", "Journal · FHIR", "billedet", "Billede · DICOM", "microsoft fabric", "Microsoft Fabric", "forbereder analysen",
 "onelake", "OneLake", "åbne formater",
 "Sikkerhed", "3 · Et lag af", "sikkerhed og identitet", "Sikkerhed og identitet · omkring det hele",
 "entra id", "Microsoft Entra ID", "identiteter", "key vault", "Azure Key Vault", "nøgler og hemmeligheder", "defender",
 "Microsoft Defender for Cloud", "beskyttelse", "sentinel", "Microsoft Sentinel", "overvågning",
 "Grænsen", "4 · ", "Grænsen", ": Eclipse EDC-konnektoren", "Grænse · åbne standarder", "azure kubernetes", "Azure Kubernetes Service",
 "hvor den kører", "Eclipse", "Eclipse EDC-konnektor", "open source", "offentliggør", "Katalog", "HealthDCAT-AP",
 "forhandler", "Kontrakt", "ODRL", "identificerer", "Legitimationer", "Gaia-X",
 "AI'en", "5 · ", "AI'en", ": modellen rejser, dataene gør ikke", "azure machine", "Azure Machine Learning",
 "fødereret læring · NVIDIA FLARE", "Klinik A", "Klinik B", "Klinik C", "modellen rejser", "modellen rejser", "modellen rejser",
 "fortrolig beregning", "Fortrolig beregning", "beskytter dataene under behandlingen", "microsoft foundry", "Microsoft Foundry",
 "udkast, som tandlægen kontrollerer",
 "Vejen", "Et røntgenbilledes vej", "Klinik", "DICOM-gateway", "Azure Health Data Services", "Microsoft Fabric og OneLake",
 "Eclipse EDC", "på Azure Kubernetes Service", "Europæisk netværk", "andre klinikker", "Sikkerhed og identitet",
 "Microsoft Entra ID · Azure Key Vault · Microsoft Defender for Cloud · Microsoft Sentinel", "identificerbare data",
 "Ingen identificerbare data forlader knuden",
 "Afslutning", "Microsoft inde i knuden.", "Åbne standarder ved grænsen.", "Sådan bygger vi Dental Data på Microsoft Azure.",
], """Det her bygger vi på Microsoft Azure til Dental Data. Én regel styrer designet: Microsoft inde i knuden, åbne standarder ved
 grænsen. I klinikken forlader røntgenbilledet apparatet gennem en open source DICOM-gateway, Orthanc, og det pseudonymiseres ved kilden.
 I dataknuden gemmer Azure Health Data Services journalen i FHIR og billedet i DICOM. Microsoft Fabric og OneLake forbereder dataene til
 analyse. Sikkerheden kommer fra Microsoft Entra ID, Azure Key Vault, Microsoft Defender for Cloud og Microsoft Sentinel. Ved grænsen
 arbejder Eclipse EDC-konnektoren, udrullet på Azure Kubernetes Service. Den offentliggør kataloget i HealthDCAT-AP, forhandler
 ODRL-kontrakter og identificerer sig med Gaia-X-legitimationer. Den kunstige intelligens trænes med Azure Machine Learning og fødereret
 læring: modellen rejser til hver klinik, og dataene bliver, hvor de er. Fortrolig beregning beskytter dataene selv under behandlingen,
 og Microsoft Foundry skriver udkast til rapporter, som tandlægen kontrollerer. Sådan følger hvert røntgenbillede en sikker og
 kontrolleret vej, fra klinikken til modellen, uden at identificerbare data forlader knuden.""",
 ["Det her bygger", "I klinikken forlader", "I dataknuden", "Sikkerheden kommer", "Ved grænsen arbejder", "Den kunstige intelligens", "Sådan følger hvert", "FIN"]),
}
