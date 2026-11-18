LANG = "it"
UI = {
 "rm": "Movimento ridotto: ogni scena viene mostrata per intero.", "ini": "Premi → o la barra spaziatrice per iniziare",
 "locucion": "🔊 Voce narrante attiva", "ctl": "Comandi della presentazione", "ant": "Scena precedente", "pp": "Riproduci o metti in pausa",
 "sig": "Scena successiva", "pista": "← → spazio · 1–{n} · F · H nasconde", "pc": "Schermo intero",
 "escena": "Scena", "quitar": "🔇 Disattiva audio", "activar": "🔊 Attiva audio", "ver": "▶ Guarda con la voce narrante (audio attivo)",
}
PIEZAS = {
"p01": ([
 "Perché i dati odontoiatrici mancano nello Spazio europeo dei dati sanitari?",
 "Perché i dati odontoiatrici mancano nell'EHDS?",
 "Presentazione animata di Dental Data: perché l'odontoiatria è la grande assente dello Spazio europeo dei dati sanitari (EHDS).",
 "Fonti: studio comparativo di Software in a Box (nov. 2026) · ISTAT · Ministero della Salute · FNOMCeO-CAO",
 "Apertura", "Dental Data · Domanda 1", "Perché i dati odontoiatrici mancano nello", "Spazio europeo dei dati sanitari", "?",
 "I grandi assenti", "Spazio europeo dei dati sanitari (EHDS)", "I dati odontoiatrici sono", "i grandi assenti",
 "Profilo sanitario sintetico", "Ricetta elettronica", "Immagini mediche", "Referti di laboratorio", "Odontoiatria", "non collegata",
 "Perché", "Non per mancanza di valore, ma per", "come è organizzata", "l'odontoiatria",
 "SSN quasi assente", "LEA solo 0–14 anni e vulnerabili", "Spesa privata", "Pagano le famiglie",
 "Software proprietario", "Ogni studio il suo", "Nessun dato sui risultati", "Nessun confronto tra studi",
 "L'Italia in cifre", "Italia", "Un mercato privato e frammentato",
 "10", "&lt;small&gt; mld €&lt;/small&gt;", "dieci", "0", "miliardi", "di spesa privata delle famiglie per le cure dentali",
 "85", ".", "&lt;small&gt;&lt;/small&gt;", "ottantacinque", "0", "milioni", "milioni di € di spesa del SSN per l'odontoiatria",
 "65000", ".", "sessantacinquemila", "0", "odontoiatri", "odontoiatri (stima)",
 "Isole di dati", "I dati esistono, ma vivono", "su isole", "conserva", "Studi non collegati",
 "fuori", "Fuori dal Fascicolo Sanitario Elettronico",
 "Chiusura", "I dati esistono.", "Nessuno li collega.", "Dental Data li collega", "senza spostarli", ".",
], """I dati odontoiatrici sono i grandi assenti dello Spazio europeo dei dati sanitari. Non per mancanza di valore, ma per come è
 organizzata l'odontoiatria. In Italia il servizio sanitario nazionale copre le cure dentali solo per i bambini e le persone vulnerabili.
 Spende circa ottantacinque milioni di euro, contro oltre dieci miliardi pagati dalle famiglie, e ci sono circa sessantacinquemila
 odontoiatri, mentre le catene crescono. Ogni studio conserva cartelle e radiografie nel proprio software, quasi sempre fuori dal
 fascicolo sanitario elettronico, e nessuno può confrontare i risultati tra studi. I dati esistono, sono abbondanti e hanno proprietari
 con buone ragioni per condividerli sotto controllo. Ciò che manca è qualcuno che li colleghi. Questo è Dental Data.""",
 ["I dati odontoiatrici sono", "Non per mancanza", "Spende circa", "Ogni studio conserva", "I dati esistono, sono"]),

"p02": ([
 "Come funziona uno spazio di dati federato?", "Come funziona uno spazio di dati federato?",
 "Presentazione animata di Dental Data: come funziona uno spazio di dati odontoiatrici federato.",
 "Fonte: Dental Data · la soluzione e i casi d'uso (base di conoscenza pubblica)",
 "Apertura", "Dental Data · Domanda 2", "Come funziona uno", "spazio di dati", "federato?",
 "Lo studio", "Ogni partecipante conserva le sue cartelle", "nel proprio software", "accanto", "Software gestionale", "cartelle e radiografie",
 "installa", "Connettore", "installato accanto",
 "La rete", "I connettori formano una rete con un", "catalogo comune", "Catalogo comune", "solo metadati",
 "Studio", "+ connettore", "Studio", "+ connettore", "Catena", "+ connettore", "Fondo sanitario o assicurazione", "+ connettore",
 "Il catalogo dice quali dati esistono. Non li conserva.",
 "Una domanda", "La domanda viaggia;", "torna solo il risultato", "Catalogo comune", "solo metadati",
 "Studio", "+ connettore", "Studio", "+ connettore", "Catena", "+ connettore", "Fondo sanitario o assicurazione", "+ connettore",
 "1 · La domanda viaggia", "2 · Calcolata in ogni studio", "3 · Torna il risultato aggregato",
 "Cosa viaggia e cosa no", "Cosa passa sulla rete…", "e cosa no", "Viaggia", "Consensi", "Metadati del catalogo",
 "Risultati aggregati", "Non viaggia", "Cartelle identificabili", "Radiografie",
 "Chiusura", "Il dato resta.", "Viaggia la risposta.", "Così funziona uno spazio di dati federato.",
], """In uno spazio di dati federato, ogni studio, catena, fondo sanitario o assicurazione conserva le proprie cartelle nel suo
 software gestionale. Accanto a quel software si installa un connettore. Il connettore pubblica in un catalogo comune quali dati esistono,
 ma non i dati. Quando qualcuno ha bisogno di un indicatore, la domanda viaggia fino a ogni studio, viene calcolata lì e torna solo il
 risultato aggregato. Sulla rete passano consensi, metadati e risultati. Mai una cartella identificabile. Il dato resta nello studio. Ciò
 che viaggia è la risposta.""",
 ["In uno spazio", "Il connettore pubblica", "Quando qualcuno", "Sulla rete passano", "Il dato resta"]),

"p03": ([
 "I miei dati escono dallo studio?", "I miei dati escono dallo studio?",
 "Presentazione animata di Dental Data: privacy, contratti d'uso e controllo dello studio sui propri dati.",
 "Fonti: Dental Data (base di conoscenza) · GDPR · Codice privacy · Regolamento (UE) 2025/327, artt. 54 e 71 · Informazione generale; non è consulenza legale",
 "Apertura", "Dental Data · Domanda 3", "I miei dati escono", "dallo studio", "?",
 "La risposta", "No.", "Nessuna cartella identificabile", "lascia lo studio",
 "Il contratto", "Ogni uso dei dati ha", "un contratto digitale", "Contratto d'uso (ODRL)",
 "chi accede", "Chi accede?", "per cosa", "Per cosa?", "per quanto tempo", "Per quanto tempo?",
 "quel contratto", "E non resta sulla carta:", "la macchina", "la macchina", "lo fa rispettare",
 "La macchina lo fa rispettare", "Senza contratto, nessun accesso.", "Con contratto, solo un risultato aggregato.",
 "lo ha", "Richiesta", "senza contratto", "lo ha", "Richiesta", "con contratto", "Studio", "con il suo connettore",
 "nessun accesso", "Accesso negato", "solo un", "aggregato", "Risultato aggregato",
 "Il quadro", "Lo studio decide sempre,", "nel quadro della legge", "regolamento generale", "GDPR", "privacy",
 "Codice privacy (D.lgs. 196/2003)", "garante", "Garante per la protezione dei dati personali",
 "mai usati", "EHDS · art. 54: mai per la pubblicità", "pubblicità",
 "EHDS · art. 71: il paziente può opporsi",
 "Chiusura", "Senza contratto,", "nessun accesso.", "Lo studio decide sempre.",
], """I dati escono dallo studio? No. Nessuna cartella identificabile lascia lo studio. Ogni uso dei dati è regolato da un contratto
 digitale che definisce chi accede, per cosa e per quanto tempo. E quel contratto non resta sulla carta: la macchina lo fa rispettare da
 sola. Se una richiesta non ha un contratto, nessun accesso. Se lo ha, torna solo un risultato aggregato. Lo studio decide sempre, nel
 quadro del regolamento generale sulla protezione dei dati e del Codice privacy, sotto la vigilanza del Garante. E con una regola chiara
 dello Spazio europeo dei dati sanitari: i dati sanitari non sono mai usati per la pubblicità.""",
 ["I dati escono", "Ogni uso", "Se una richiesta", "Lo studio decide", "FIN"]),

"p04": ([
 "Cosa ci guadagna una catena odontoiatrica?", "Cosa ci guadagna una catena?",
 "Presentazione animata di Dental Data: indicatori di qualità confrontabili tra studi senza migrare le cartelle.",
 "Fonti: Dental Data · casi d'uso e pilota (base di conoscenza) · L. 124/2017 · Regolamento (UE) 2025/327, art. 72 · Barre illustrative",
 "Apertura", "Dental Data · Domanda 4", "Cosa ci guadagna una", "catena odontoiatrica", "?",
 "Il problema", "Una catena cresce acquistando studi…", "e ogni studio ha il suo software",
 "Studio 1", "Software A", "Studio 2", "Software B", "Studio 3", "Software C", "Studio 4", "Software D", "Studio 5", "Software E",
 "migrare", "Società di capitali con direttore sanitario (L. 124/2017) · confrontare oggi significa migrare cartelle",
 "Senza migrazione", "Con Dental Data non serve:", "un connettore accanto a ogni software",
 "Studio 1", "Software A", "Connettore", "Studio 2", "Software B", "Connettore", "Studio 3", "Software C", "Connettore",
 "Studio 4", "Software D", "Connettore", "Studio 5", "Software E", "Connettore",
 "Indicatori confrontabili", "Lo stesso indicatore,", "calcolato in ogni studio",
 "Studio 1", "Studio 2", "Studio 3", "Studio 4", "Studio 5",
 "La stessa definizione in tutti gli studi", "cartella", "Nessuna cartella clinica viene ceduta",
 "Valore aggiunto", "E in più…", "Qualità dimostrabile", "Verso fondi, ordini e regolatori.",
 "informazione", "Informazione verificabile, non promozione", "Fiducia dei pazienti dopo le chiusure improvvise.",
 "Chiusura", "Qualità dimostrabile,", "senza migrare una sola cartella.", "Indicatori di qualità confrontabili in tutta la rete.",
], """In Italia, dal duemiladiciassette, le società di capitali possono esercitare l'odontoiatria con un direttore sanitario in ogni
 studio. Così sono cresciute le catene, e la chiusura improvvisa di alcune ha danneggiato la fiducia. Una catena che acquista studi riceve
 in ognuno un software diverso, e confrontare la qualità significa migrare le cartelle. Con Dental Data non serve: un connettore accanto a
 ogni software calcola gli indicatori nello studio, con la stessa definizione, e la direzione vede risultati confrontabili di tutta la
 rete. È informazione verificabile, non promozione: la catena può mostrare la sua qualità ai fondi, agli ordini e ai regolatori senza
 cedere una sola cartella clinica. Qualità dimostrabile, senza migrare una sola cartella.""",
 ["In Italia, dal", "Con Dental Data", "e la direzione vede", "È informazione", "Qualità dimostrabile, senza"]),

"p05": ([
 "Cosa ci guadagna un fondo integrativo o un'assicurazione?", "Cosa ci guadagna un fondo integrativo?",
 "Presentazione animata di Dental Data: dati coerenti su costi e risultati di una rete odontoiatrica senza centralizzare le cartelle.",
 "Fonti: Dental Data (base di conoscenza) · Anagrafe dei fondi sanitari · Regolamento (UE) 2025/327, art. 54",
 "Apertura", "Dental Data · Domanda 5", "Cosa ci guadagna un", "fondo integrativo", "?",
 "La rete", "Studi convenzionati,", "ognuno con il suo software",
 "Fondo o assicurazione", "Fondi integrativi", "in crescita", "Assicurazioni", "reti convenzionate", "Studio convenzionato", "proprio software",
 "Studio convenzionato", "proprio software", "Costi e risultati dispersi",
 "Dati coerenti", "Dati coerenti di tutta la rete,", "senza centralizzare le cartelle",
 "Fondo", "Studio", "proprio software", "Studio", "proprio software", "Studio", "proprio software", "Studio", "proprio software",
 "Calcolo nello studio · torna solo il risultato aggregato",
 "Un canale", "La rete come", "canale di partecipazione", "Studi indipendenti", "Reti convenzionate", "partecipino", "Spazio di dati odontoiatrici",
 "Limiti chiari", "Con limiti chiari:", "ciò che l'EHDS vieta", "pubblicità", "Pubblicità",
 "I dati sanitari non si usano mai per la pubblicità.", "decisioni", "Decisioni pregiudizievoli",
 "Né per decisioni che danneggiano le persone, anche nelle assicurazioni.", "Regolamento (UE) 2025/327, articolo 54",
 "Chiusura", "Dati coerenti di tutta la rete,", "senza centralizzare le cartelle.", "Con il controllo sempre nello studio.",
], """In Italia una parte crescente delle cure dentali è pagata da fondi sanitari integrativi e assicurazioni, attraverso reti di studi
 convenzionati, ognuno con il proprio software. I loro dati su costi e risultati sono dispersi e non si possono confrontare. Dental Data
 offre dati coerenti di tutta la rete senza centralizzare le cartelle: il calcolo si fa in ogni studio e torna solo il risultato
 aggregato. La rete serve anche da canale perché partecipino gli studi indipendenti. Con limiti chiari: lo Spazio europeo dei dati
 sanitari vieta di usare questi dati per la pubblicità o per decisioni che danneggiano le persone, anche nelle assicurazioni. Dati
 coerenti di tutta la rete, senza centralizzare le cartelle.""",
 ["In Italia una parte", "Dental Data offre", "La rete serve", "Con limiti chiari", "Dati coerenti di tutta la rete, senza"]),

"p06": ([
 "L'IA sulle radiografie senza spostare le radiografie", "Come funziona l'IA sulle radiografie dentali?",
 "Presentazione animata di Dental Data: apprendimento federato e calcolo confidenziale sulle immagini dentali.",
 "Fonti: Dental Data (base di conoscenza) · Regolamento (UE) 2026/1744 · Regolamento (UE) 2025/327 · Modello in validazione clinica; non sostituisce la diagnosi · Dispositivi medici: Ministero della Salute · IA: AgID e ACN (L. 132/2025)",
 "Apertura", "Dental Data · Domanda 6", "Come si addestra una", "IA odontoiatrica", "senza spostare le radiografie?",
 "Il dilemma", "Addestrare un'IA richiede molte radiografie…", "riunirle è un rischio", "Un archivio centrale",
 "Centralizzare le radiografie aumenta il rischio",
 "L'algoritmo viaggia", "Dental Data inverte il percorso:", "l'algoritmo viaggia", "Modello di IA",
 "Studio", "le radiografie restano", "Studio", "le radiografie restano", "Studio", "le radiografie restano",
 "impara", "Impara in ogni studio", "restituisce", "Restituisce solo ciò che ha imparato",
 "Calcolo confidenziale", "Calcolo", "confidenziale", "Protegge i dati anche mentre vengono elaborati.",
 "Il modello", "Primo modello", "Carie interprossimali", "Su radiografie dentali.", "ossea", "Perdita ossea parodontale",
 "Su radiografie dentali.", "validazione", "In validazione clinica", "aiuto", "Un aiuto per il professionista: non sostituisce la diagnosi",
 "Cosa arriva", "Pronto per", "ciò che arriva", "2 ago 2028", "Regolamento IA: obblighi per l'IA nei dispositivi medici",
 "duemilatrentuno", "26 mar 2031", "Le immagini mediche entrano nello Spazio europeo dei dati sanitari",
 "Chiusura", "L'algoritmo", "va verso il dato.", "IA sulle immagini dentali senza spostare le radiografie.",
], """Addestrare un'IA odontoiatrica richiede molte radiografie. Ma riunirle in un solo luogo è un rischio. Dental Data inverte il
 percorso: l'algoritmo viaggia fino a ogni studio, impara lì e restituisce solo ciò che ha imparato, mai le immagini. I calcoli avvengono
 con il calcolo confidenziale, che protegge i dati mentre vengono elaborati. Il primo modello, per le carie interprossimali e la perdita
 ossea parodontale, è in validazione clinica. È un aiuto per il professionista: non sostituisce la sua diagnosi. E si prepara a ciò che
 arriva: nel duemilatrentuno le immagini mediche entrano nello Spazio europeo dei dati sanitari. L'algoritmo va verso il dato.""",
 ["Addestrare un'IA", "Dental Data inverte", "I calcoli avvengono", "Il primo modello", "E si prepara", "L'algoritmo va"]),

"p07": ([
 "Quali date fissa lo Spazio europeo dei dati sanitari?", "Quali date fissa l'EHDS?",
 "Presentazione animata di Dental Data: il calendario dell'EHDS e la situazione in Italia (FSE 2.0, Ecosistema Dati Sanitari).",
 "Fonti: Regolamento (UE) 2025/327 (artt. 50 e 105) · DM 31/12/2024 (Ecosistema Dati Sanitari) · L. 132/2025",
 "Apertura", "Dental Data · Domanda 7", "Quali date fissa lo", "Spazio europeo dei dati sanitari", "?",
 "Calendario", "Già in vigore", "e con date", "26 mar 2025", "In vigore", "duemilaventisette", "26 mar 2027",
 "Organismi di accesso designati", "duemilaventinove", "26 mar 2029", "Uso secondario: la maggior parte delle regole",
 "duemilatrentuno", "26 mar 2031", "Immagini mediche, come le radiografie",
 "La finestra", "Tra 2027 e 2029:", "due anni per collegare studi e catene",
 "26 mar 2025", "In vigore", "26 mar 2027", "Organismi di accesso designati", "26 mar 2029", "Uso secondario: la maggior parte delle regole",
 "26 mar 2031", "Immagini mediche, come le radiografie",
 "Articolo 50", "La maggior parte degli studi sono microimprese:", "esenti per impostazione predefinita", "partecipare", "attraverso",
 "Studi indipendenti", "Art. 50: esenti salvo diversa decisione dello Stato", "canale aggregato", "Canale aggregato",
 "catene · fondi · associazioni", "attraverso", "Spazio di dati odontoiatrici",
 "Italia", "Italia", "FSE 2.0 · Ecosistema Dati Sanitari (AGENAS)", "agenas",
 "Ecosistema Dati Sanitari gestito da AGENAS (DM 31/12/2024) e L. 132/2025 sull'IA e l'uso secondario. Organismo di accesso da designare; il dato dentale, quasi tutto privato, ne resta fuori.",
 "designato", "Organismo di accesso non ancora designato (nov. 2026)",
 "Chiusura", "Chi sarà collegato nel 2029", "sarà l'interlocutore naturale", "degli organismi di accesso ai dati sanitari.",
], """Lo Spazio europeo dei dati sanitari è già in vigore e ha delle date: organismi di accesso a marzo duemilaventisette, uso
 secondario a marzo duemilaventinove e immagini mediche nel duemilatrentuno. La maggior parte degli studi sono microimprese ed esenti per
 impostazione predefinita: per partecipare serve un canale aggregato, attraverso catene, fondi o associazioni. L'Italia ha già il
 fascicolo sanitario elettronico due punto zero, un Ecosistema Dati Sanitari gestito da AGENAS e una legge sull'intelligenza artificiale
 che facilita la ricerca con i dati sanitari. L'organismo di accesso non è ancora designato, e il dato dentale, quasi tutto privato, resta
 fuori. Chi lo collegherà per primo sarà l'interlocutore naturale.""",
 ["Lo Spazio europeo", "uso secondario a marzo", "La maggior parte", "L'Italia ha già", "Chi lo collegherà"]),

"p08": ([
 "Quale tecnologia c'è dietro Dental Data?", "Quale tecnologia c'è dietro Dental Data?",
 "Presentazione animata di Dental Data: Microsoft dentro il nodo, standard europei aperti ai confini.",
 "Fonti: Dental Data · tecnologia e azienda (base di conoscenza) · Microsoft e Azure sono marchi di Microsoft Corporation; citati come testo",
 "Apertura", "Dental Data · Domanda 8", "Quale tecnologia c'è dietro", "Dental Data", "?",
 "La regola", "Una regola semplice", "Microsoft", "Azure", "dati nell'UE", "Dentro il nodo", "Al confine: standard aperti",
 "Dentro il nodo", "Dentro il nodo:", "Microsoft", "Connettore su Microsoft Azure", "Con i dati nell'Unione europea.",
 "integrato", "Integrato", "Con il software gestionale dello studio.", "distribuito", "Distribuito da partner", "Integratori e partner Azure.",
 "Al confine", "Ai confini:", "standard europei aperti", "gaiax", "Gaia-X", "protocollo", "IDSA", "eclipse", "Dataspace Protocol",
 "eclipse edc", "Eclipse EDC", "verificabili", "Credenziali verificabili", "fhir", "FHIR", "dicom", "DICOM", "healthdcatap", "HealthDCAT-AP",
 "Aperto a tutti", "Chiunque può collegarsi,", "anche senza Microsoft", "Nodo su Azure", "Partecipante senza Microsoft",
 "Standard aperti", "Si collega allo stesso modo",
 "Esperienza", "Non partiamo da zero:", "tre spazi di dati reali", "Global Data Care", "Salute, su Gaia-X e Pontus-X.",
 "PROCUREDATA", "Appalti pubblici.", "EcoDataNet", "Rifiuti ed economia circolare.",
 "Dimostratori finanziati dalla SEDIA (2024–2026), con connettori propri basati su Eclipse.",
 "Chiusura", "Microsoft dentro il nodo.", "Standard aperti ai confini.", "Uno spazio di dati odontoiatrici aperto a tutti.",
], """Dental Data segue una regola semplice: Microsoft dentro il nodo, standard aperti ai confini. Dentro ogni nodo, il connettore
 funziona su Microsoft Azure, con i dati nell'Unione europea, integrato con il software gestionale dello studio e distribuito da partner
 Azure. Ai confini, lo spazio parla standard europei aperti: Gaia-X, il protocollo degli spazi di dati, Eclipse EDC, credenziali
 verificabili, FHIR, DICOM e HealthDCAT-AP. Così qualsiasi partecipante può collegarsi, anche senza Microsoft. E non partiamo da zero:
 Software in a Box ha già progettato e realizzato tre spazi di dati reali.""",
 ["segue una regola", "Dentro ogni", "Ai confini, lo spazio", "Così qualsiasi", "E non partiamo", "FIN"]),

"p09": ([
 "Cosa offre Dental Data all'industria?", "Cosa offre Dental Data all'industria?",
 "Presentazione animata di Dental Data: evidenze dal mondo reale sotto contratto per produttori, aziende di IA e software gestionali.",
 "Fonti: Dental Data (base di conoscenza) · Regolamento (UE) 2025/327, art. 54",
 "Apertura", "Dental Data · Domanda 9", "Cosa offre Dental Data all'", "industria", "?",
 "Chi", "Per chi deve sapere", "cosa succede nello studio", "Impianti", "materiali", "Materiali", "intelligenza", "Intelligenza artificiale",
 "devono", "Software gestionale",
 "Evidenze reali", "Evidenze dal mondo reale,", "senza dati identificabili", "Industria", "domanda sotto contratto",
 "Studi", "Studi", "Studi", "Tornano risultati aggregati, mai cartelle",
 "Per il gestionale", "Per il software gestionale:", "un connettore che aggiunge servizi", "Il vostro software gestionale",
 "Connettore integrato", "Nuovi servizi", "per i vostri clienti",
 "Le regole", "Le regole", "non cambiano", "Un contratto per ogni uso", "Chi, per cosa e per quanto tempo.", "solo risultati",
 "Solo aggregati", "Nessun dato identificabile lascia lo studio.", "mai", "Mai pubblicità", "L'EHDS lo vieta (art. 54).",
 "Chiusura", "Evidenze reali,", "ordinate e sotto contratto.", "Per l'industria e il software odontoiatrico.",
], """Per l'industria odontoiatrica, le evidenze dal mondo reale valgono molto. I produttori di impianti e materiali, e le aziende di
 intelligenza artificiale, devono sapere come si comportano i loro prodotti nello studio. Dental Data offre loro queste evidenze, ordinate
 e sotto contratto: domande a cui si risponde negli studi e risultati aggregati che tornano senza dati identificabili. Per i produttori di
 software gestionale, il connettore è un componente che si integra nel loro prodotto e apre nuovi servizi ai loro clienti. Le regole non
 cambiano: un contratto per ogni uso, solo risultati aggregati e mai pubblicità. Evidenze reali, ordinate e sotto contratto.""",
 ["Per l'industria odontoiatrica", "Dental Data offre", "Per i produttori", "Le regole non", "Evidenze reali, ordinate"]),

"p10": ([
 "Come partecipare a Dental Data?", "Come partecipare a Dental Data?",
 "Presentazione animata di Dental Data: il programma partner in Italia, la roadmap e come partecipare.",
 "Fonti: Dental Data · programma partner Italia e roadmap (base di conoscenza) · Nessuna tariffa pubblicata",
 "Apertura", "Dental Data · Domanda 10", "Come partecipare a", "Dental Data", "?",
 "Cerchiamo", "Cerchiamo", "Una catena o un fondo integrativo", "Per un primo progetto di indicatori di qualità tra studi",
 "progetto", "Primo progetto 2027",
 "Finanziamento", "Il caso d'uso", "finanzia il connettore", "Caso d'uso interno della catena o del fondo; l'importo dipende dal numero di studi e si definisce in un colloquio.",
 "Roadmap", "La", "roadmap", "2027", "Primo progetto", "consolidiamo", "2027–2028",
 "Consolidare i progetti e partecipare alle consultazioni", "catalogato", "2029", "Insieme di dati catalogato per l'EHDS",
 "poi", "2029–2031", "Linea per le immagini dentali",
 "Vogliamo parlare anche con", "Vogliamo parlare anche con…", "CAO-FNOMCeO · ANDI · AIO", "software", "Software house",
 "agenas", "AGENAS", "regioni", "Regioni", "fondi", "Fondi sanitari",
 "Ne parliamo?", "Ne parliamo?", "partners@softwareinabox.eu", "+34 601 398 868", "dentaldata.softwareinabox.eu",
], """In Italia cerchiamo una catena odontoiatrica o un fondo sanitario integrativo per un primo progetto di indicatori di qualità tra
 studi. Il caso d'uso stesso finanzia il connettore. Nel duemilaventisette il primo progetto; poi consolidiamo i progetti; nel
 duemilaventinove un insieme di dati catalogato e pronto per lo spazio europeo; poi le immagini dentali. Vogliamo parlare anche con le
 aziende di software gestionale, con la commissione degli odontoiatri, con le associazioni dei dentisti, con AGENAS, con le regioni che
 vogliono misurare i livelli essenziali di assistenza odontoiatrica e con i fondi. Ne parliamo? Scrivici a partners chiocciola
 softwareinabox punto eu.""",
 ["In Italia cerchiamo", "Il caso d'uso", "Nel duemilaventisette", "Vogliamo parlare", "Ne parliamo?"]),

"p11": ([
 "Cosa costruiamo su Microsoft Azure?", "Cosa costruiamo su Microsoft Azure?",
 "Presentazione animata di Dental Data: l'architettura dello spazio di dati odontoiatrici con i componenti di Microsoft Azure e il connettore Eclipse EDC.",
 "Fonti: Dental Data · documento tecnico (v1.3) e proposta MVP (v1.4) · Icone ufficiali Microsoft (Azure, Microsoft Entra e Microsoft Fabric), usate secondo le loro condizioni per i diagrammi di architettura · Microsoft, Azure, Entra, Fabric e i nomi dei loro servizi sono marchi di Microsoft Corporation",
 "Apertura", "Dental Data · Domanda 11", "Cosa costruiamo su", "Microsoft Azure", "?",
 "La regola", "Una regola guida il progetto", "Confine · standard aperti", "Nodo · Microsoft Azure", "Microsoft", "dentro il nodo",
 "Standard aperti al confine",
 "Lo studio", "1 · Nello", "studio", "Apparecchio radiografico", "radiografia, CBCT", "gateway DICOM", "Gateway DICOM", "Orthanc · open source",
 "pseudonimizzata", "Pseudonimizzata all'origine", "senza dati che identificano il paziente",
 "Il nodo di dati", "2 · Il", "nodo di dati", "su Azure", "Nodo di dati · Microsoft Azure", "azure health", "Azure Health Data Services",
 "la cartella", "Cartella · FHIR", "l'immagine", "Immagine · DICOM", "microsoft fabric", "Microsoft Fabric", "prepara l'analisi",
 "onelake", "OneLake", "formati aperti",
 "Sicurezza", "3 · Uno strato di", "sicurezza e identità", "Sicurezza e identità · intorno a tutto",
 "entra id", "Microsoft Entra ID", "identità", "key vault", "Azure Key Vault", "chiavi e segreti", "defender",
 "Microsoft Defender for Cloud", "protezione", "sentinel", "Microsoft Sentinel", "monitoraggio",
 "Il confine", "4 · Il", "confine", ": il connettore Eclipse EDC", "Confine · standard aperti", "azure kubernetes", "Azure Kubernetes Service",
 "dove gira", "Eclipse", "Connettore Eclipse EDC", "open source", "pubblica", "Catalogo", "HealthDCAT-AP",
 "negozia", "Contratto", "ODRL", "si identifica", "Credenziali", "Gaia-X",
 "L'IA", "5 · L'", "IA", ": viaggia il modello, non i dati", "azure machine", "Azure Machine Learning",
 "apprendimento federato · NVIDIA FLARE", "Studio A", "Studio B", "Studio C", "il modello viaggia", "il modello viaggia", "il modello viaggia",
 "calcolo confidenziale", "Calcolo confidenziale", "protegge i dati durante l'elaborazione", "microsoft foundry", "Microsoft Foundry",
 "bozze che il dentista verifica",
 "Il percorso", "Il percorso di una radiografia", "Studio", "Gateway DICOM", "Azure Health Data Services", "Microsoft Fabric e OneLake",
 "Eclipse EDC", "su Azure Kubernetes Service", "Rete europea", "altri studi", "Sicurezza e identità",
 "Microsoft Entra ID · Azure Key Vault · Microsoft Defender for Cloud · Microsoft Sentinel", "dato identificabile",
 "Nessun dato identificabile lascia il nodo",
 "Chiusura", "Microsoft dentro il nodo.", "Standard aperti al confine.", "Così costruiamo Dental Data su Microsoft Azure.",
], """Ecco cosa costruiamo su Microsoft Azure per Dental Data. Una regola guida il progetto: Microsoft dentro il nodo, standard aperti
 al confine. Nello studio, la radiografia lascia l'apparecchio attraverso un gateway DICOM open source, Orthanc, e viene pseudonimizzata
 all'origine. Nel nodo di dati, Azure Health Data Services conserva la cartella in FHIR e l'immagine in DICOM. Microsoft Fabric e OneLake
 preparano i dati per l'analisi. La sicurezza viene da Microsoft Entra ID, Azure Key Vault, Microsoft Defender for Cloud e Microsoft
 Sentinel. Al confine lavora il connettore Eclipse EDC, distribuito su Azure Kubernetes Service. Pubblica il catalogo in HealthDCAT-AP,
 negozia contratti ODRL e si identifica con credenziali Gaia-X. L'intelligenza artificiale si addestra con Azure Machine Learning e
 l'apprendimento federato: il modello viaggia fino a ogni studio e i dati restano dove sono. Il calcolo confidenziale protegge i dati anche
 durante l'elaborazione, e Microsoft Foundry scrive bozze di referto che il dentista verifica. Così ogni radiografia segue un percorso
 sicuro e controllato, dallo studio al modello, senza che nessun dato identificabile lasci il nodo.""",
 ["Ecco cosa", "Nello studio, la radiografia", "Nel nodo di dati", "La sicurezza viene", "Al confine lavora", "L'intelligenza artificiale", "Così ogni radiografia", "FIN"]),
}
