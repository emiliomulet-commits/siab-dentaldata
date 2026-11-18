LANG = "fr"
UI = {
 "rm": "Mouvement réduit : chaque scène est affichée en entier.", "ini": "Appuyez sur → ou sur la barre d'espace pour commencer",
 "locucion": "🔊 Voix off activée", "ctl": "Commandes de la présentation", "ant": "Scène précédente", "pp": "Lecture ou pause",
 "sig": "Scène suivante", "pista": "← → espace · 1–{n} · F · H masque", "pc": "Plein écran",
 "escena": "Scène", "quitar": "🔇 Couper le son", "activar": "🔊 Activer le son", "ver": "▶ Regarder avec la voix off (son activé)",
}
PIEZAS = {
"p01": ([
 "Pourquoi les données dentaires manquent-elles à l'Espace européen des données de santé ?",
 "Pourquoi les données dentaires manquent-elles à l'EHDS ?",
 "Présentation animée de Dental Data : pourquoi l'odontologie est la grande absente de l'Espace européen des données de santé (EHDS).",
 "Sources : étude comparative de Software in a Box (nov. 2026) · DREES (2025) · Comptes de la santé · ARS",
 "Ouverture", "Dental Data · Question 1", "Pourquoi les données dentaires manquent-elles à l'", "Espace européen des données de santé", " ?",
 "Les grandes absentes", "Espace européen des données de santé (EHDS)", "Les données dentaires sont", "les grandes absentes",
 "Dossier patient", "Ordonnance électronique", "Images médicales", "Biologie", "Odontologie", "non reliée",
 "Pourquoi", "Non par manque de valeur, mais à cause de", "l'organisation", "de l'odontologie",
 "AMO + complémentaires", "Deux financeurs", "100 % santé", "Reste à charge zéro sur une partie",
 "Logiciels propriétaires", "Chaque cabinet le sien", "Pas de résultats", "Le SNDS voit le remboursement, pas le résultat",
 "La France en chiffres", "France", "Un marché solvabilisé, mais sans données cliniques",
 "13", "&lt;small&gt;,2 Md€&lt;/small&gt;", "treize", "0", "milliards", "de dépense en cabinet dentaire libéral",
 "47636", " ", "&lt;small&gt;&lt;/small&gt;", "quarante-huit", "0", "chirurgiens-dentistes", "chirurgiens-dentistes en exercice",
 "2055", " ", "deux", "0", "centres", "centres de santé dentaires soumis à agrément",
 "Îlots de données", "Les données existent, mais elles vivent", "sur des îlots", "restent", "Sans lien entre cabinets",
 "logiciel", "Remboursements connus, résultats inconnus",
 "Conclusion", "Les données existent.", "Personne ne les relie.", "Dental Data les relie", "sans les déplacer", ".",
], """Les données dentaires sont les grandes absentes de l'Espace européen des données de santé. En France, les soins dentaires sont
 financés par l'Assurance maladie et surtout par les complémentaires, et la réforme cent pour cent santé a supprimé le reste à charge sur
 une partie des prothèses. Le pays compte près de quarante-huit mille chirurgiens-dentistes, la dépense en cabinet libéral dépasse treize
 milliards d'euros, et plus de deux mille centres de santé dentaires sont soumis à agrément. Le Système national des données de santé
 sait ce qui est remboursé, mais pas ce qui a été trouvé en bouche ni le résultat du traitement : ces données restent dans chaque cabinet
 et chaque centre, dans leur propre logiciel. Les données existent et ont des propriétaires qui ont des raisons de les partager sous
 contrôle. Ce qui manque, c'est quelqu'un pour les relier. C'est Dental Data.""",
 ["Les données dentaires sont", "En France, les soins", "Le pays compte", "Le Système national", "Les données existent et"]),

"p02": ([
 "Comment fonctionne un espace de données fédéré ?", "Comment fonctionne un espace de données fédéré ?",
 "Présentation animée de Dental Data : comment fonctionne un espace de données dentaires fédéré.",
 "Source : Dental Data · la solution et ses cas d'usage (base de connaissances publique)",
 "Ouverture", "Dental Data · Question 2", "Comment fonctionne un", "espace de données", "fédéré ?",
 "Le cabinet", "Chaque participant garde ses dossiers", "dans son propre logiciel", "à côté", "Logiciel de gestion", "dossiers et radiographies",
 "installé", "Connecteur", "installé à côté",
 "Le réseau", "Les connecteurs forment un réseau avec un", "catalogue commun", "Catalogue commun", "métadonnées seulement",
 "Cabinet", "+ connecteur", "Centre de santé", "+ connecteur", "Réseau de centres", "+ connecteur", "Complémentaire", "+ connecteur",
 "Le catalogue dit quelles données existent. Il ne les stocke pas.",
 "Une question", "La question voyage ;", "seul le résultat revient", "Catalogue commun", "métadonnées seulement",
 "Cabinet", "+ connecteur", "Centre de santé", "+ connecteur", "Réseau de centres", "+ connecteur", "Complémentaire", "+ connecteur",
 "1 · La question voyage", "2 · Calculée dans chaque cabinet", "3 · Le résultat agrégé revient",
 "Ce qui voyage et ce qui ne voyage pas", "Ce qui circule sur le réseau…", "et ce qui ne circule pas", "Voyage", "Consentements", "Métadonnées du catalogue",
 "Résultats agrégés", "Ne voyage pas", "Dossiers identifiables", "Radiographies",
 "Conclusion", "Les données restent.", "La réponse voyage.", "Voilà comment fonctionne un espace de données fédéré.",
], """Dans un espace de données fédéré, chaque cabinet ou centre de santé, chaque réseau ou complémentaire garde ses dossiers dans
 son propre logiciel de gestion. À côté de ce logiciel, on installe un connecteur. Le connecteur publie dans un catalogue commun quelles
 données existent, mais pas les données elles-mêmes. Quand quelqu'un a besoin d'un indicateur, la question voyage jusqu'à chaque cabinet,
 y est calculée, et seul le résultat agrégé revient. Sur le réseau circulent des consentements, des métadonnées et des résultats. Jamais
 un dossier identifiable. La donnée reste au cabinet. Ce qui voyage, c'est la réponse.""",
 ["Dans un espace", "Le connecteur publie", "Quand quelqu'un", "Sur le réseau", "La donnée reste"]),

"p03": ([
 "Mes données sortent-elles du cabinet ?", "Mes données sortent-elles du cabinet ?",
 "Présentation animée de Dental Data : protection des données, contrats d'usage et contrôle du cabinet sur ses données.",
 "Sources : Dental Data (base de connaissances) · RGPD · loi Informatique et Libertés · Règlement (UE) 2025/327, art. 54 et 71 · Information générale ; pas un conseil juridique",
 "Ouverture", "Dental Data · Question 3", "Mes données sortent-elles", "du cabinet", " ?",
 "La réponse", "Non.", "Aucun dossier identifiable", "ne quitte le cabinet",
 "Le contrat", "Chaque usage des données a", "un contrat numérique", "Contrat d'usage (ODRL)",
 "qui accède", "Qui accède ?", "pour quoi", "Pour quoi ?", "combien de temps", "Combien de temps ?",
 "ce contrat", "Et il ne reste pas sur le papier :", "la machine", "la machine", "le fait respecter",
 "La machine le fait respecter", "Sans contrat, pas d'accès.", "Avec contrat, seulement un résultat agrégé.",
 "en a un", "Demande", "sans contrat", "en a un", "Demande", "avec contrat", "Cabinet", "avec son connecteur",
 "pas d'accès", "Accès refusé", "seul un", "agrégé", "Résultat agrégé",
 "Le cadre", "Le cabinet décide toujours,", "dans le cadre de la loi", "règlement général", "RGPD", "Informatique",
 "Loi Informatique et Libertés · CNIL", "hébergeur", "Hébergeur certifié HDS",
 "jamais utilisées", "EHDS · art. 54 : jamais pour la publicité", "publicité",
 "EHDS · art. 71 : le patient peut s'y opposer",
 "Conclusion", "Sans contrat,", "pas d'accès.", "Le cabinet décide toujours.",
], """Les données sortent-elles du cabinet ? Non. Aucun dossier identifiable ne quitte le cabinet. Chaque usage des données est
 régi par un contrat numérique qui définit qui accède, pour quoi et combien de temps. Et ce contrat ne reste pas sur le papier : la
 machine le fait respecter elle-même. Si une demande n'a pas de contrat, il n'y a pas d'accès. Si elle en a un, seul un résultat agrégé
 revient. Le cabinet décide toujours, dans le cadre du règlement général sur la protection des données et de la loi Informatique et
 Libertés, avec un hébergeur certifié pour les données de santé. Et avec une règle claire de l'Espace européen des données de santé :
 les données de santé ne sont jamais utilisées pour la publicité.""",
 ["Les données sortent-elles", "Chaque usage", "Si une demande", "Le cabinet décide", "FIN"]),

"p04": ([
 "Que gagne un réseau de centres ?", "Que gagne un réseau de centres ?",
 "Présentation animée de Dental Data : des indicateurs de qualité comparables entre centres, sans migrer les dossiers.",
 "Sources : Dental Data · cas d'usage et pilote (base de connaissances) · loi du 19 mai 2023 (agrément des centres de santé) · Règlement (UE) 2025/327, art. 72 · Barres illustratives",
 "Ouverture", "Dental Data · Question 4", "Que gagne un", "réseau de centres", " ?",
 "Le problème", "Un réseau grandit en ouvrant ou rachetant des centres…", "et chaque centre a son logiciel",
 "Centre 1", "Logiciel A", "Centre 2", "Logiciel B", "Centre 3", "Logiciel C", "Centre 4", "Logiciel D", "Centre 5", "Logiciel E",
 "agrément", "Après Dentexia et Proxidentaire : agrément de l'ARS obligatoire",
 "Sans migration", "Avec Dental Data, inutile de migrer :", "un connecteur à côté de chaque logiciel",
 "Centre 1", "Logiciel A", "Connecteur", "Centre 2", "Logiciel B", "Connecteur", "Centre 3", "Logiciel C", "Connecteur",
 "Centre 4", "Logiciel D", "Connecteur", "Centre 5", "Logiciel E", "Connecteur",
 "Indicateurs comparables", "Le même indicateur,", "calculé dans chaque centre",
 "Centre 1", "Centre 2", "Centre 3", "Centre 4", "Centre 5",
 "Même définition · actes codés en CCAM", "dossier", "Aucun dossier médical n'est transmis",
 "Valeur ajoutée", "Et en plus…", "Qualité démontrable", "Devant l'ARS et l'Assurance maladie.",
 "condition", "Une condition pour rester ouvert", "Et prêt pour l'Espace européen des données de santé.",
 "Conclusion", "Une qualité démontrable,", "sans migrer un seul dossier.", "Des indicateurs de qualité comparables dans tout le réseau.",
], """Un réseau de centres de santé dentaires grandit en ouvrant ou en rachetant des centres, chacun avec son logiciel. Après les
 scandales Dentexia et Proxidentaire, la loi de deux mille vingt-trois impose aux centres dentaires un agrément préalable de l'agence
 régionale de santé, qui peut le refuser ou sanctionner. Démontrer sa qualité est devenu une condition pour rester ouvert. Avec Dental
 Data, inutile de migrer les dossiers : un connecteur à côté de chaque logiciel calcule les indicateurs dans chaque centre, avec la même
 définition et des actes codés dans la classification commune. La direction voit des résultats comparables de tout le réseau, et peut
 les montrer à l'agence régionale et à l'Assurance maladie sans transmettre un seul dossier médical. Une qualité démontrable, sans migrer
 un seul dossier.""",
 ["Un réseau de centres", "Avec Dental", "La direction voit", "et peut les montrer", "Une qualité démontrable, sans"]),

"p05": ([
 "Que gagne une complémentaire ?", "Que gagne une complémentaire ?",
 "Présentation animée de Dental Data : des données cohérentes sur les soins dentaires d'un réseau, sans centraliser les dossiers.",
 "Sources : Dental Data (base de connaissances) · DREES · réforme 100 % santé · Règlement (UE) 2025/327, art. 54",
 "Ouverture", "Dental Data · Question 5", "Que gagne une", "complémentaire", " ?",
 "Le réseau", "Cabinets conventionnés,", "chacun avec son logiciel",
 "Complémentaire", "Premier financeur", "des soins dentaires", "Réseaux de soins", "cabinets partenaires", "Cabinet partenaire", "son logiciel",
 "Cabinet partenaire", "son logiciel", "Prothèses payées, résultats inconnus",
 "Données cohérentes", "Des données cohérentes de tout le réseau,", "sans centraliser les dossiers",
 "Complémentaire", "Cabinet", "son logiciel", "Cabinet", "son logiciel", "Cabinet", "son logiciel", "Cabinet", "son logiciel",
 "Calcul au cabinet · seul le résultat agrégé revient",
 "Un canal", "Pour évaluer", "le 100 % santé", "Panier 100 % santé", "Réseaux conventionnés", "qualité des réseaux", "Espace de données dentaires",
 "Limites claires", "Avec des limites claires :", "ce que l'EHDS interdit", "publicité", "Publicité",
 "Les données de santé ne servent jamais à la publicité.", "décisions", "Décisions préjudiciables",
 "Ni à des décisions qui nuisent aux personnes, y compris en assurance et sur les primes.", "Règlement (UE) 2025/327, article 54",
 "Conclusion", "Des résultats mesurés,", "sans centraliser les dossiers.", "Avec le contrôle toujours au cabinet.",
], """En France, les complémentaires sont le premier financeur des soins dentaires, et beaucoup travaillent avec des réseaux de
 cabinets partenaires. Elles paient des prothèses du panier cent pour cent santé, mais ne savent pas si ces traitements durent ni quel
 résultat ils obtiennent. Dental Data leur donne des données cohérentes de tout leur réseau sans centraliser les dossiers : le calcul se
 fait dans chaque cabinet et seul le résultat agrégé revient. Elles peuvent ainsi évaluer la réforme avec des données cliniques et
 améliorer la qualité de leurs réseaux. Avec des limites claires : l'Espace européen des données de santé interdit d'utiliser ces données
 pour la publicité ou pour des décisions qui nuisent aux personnes, y compris en assurance et sur les primes. Des résultats mesurés,
 sans centraliser les dossiers.""",
 ["En France, les complémentaires", "Dental Data leur donne", "Elles peuvent ainsi", "Avec des limites", "Des résultats mesurés"]),

"p06": ([
 "L'IA sur les radiographies sans déplacer les radiographies", "Comment fonctionne l'IA sur les radiographies dentaires ?",
 "Présentation animée de Dental Data : apprentissage fédéré et calcul confidentiel sur les images dentaires.",
 "Sources : Dental Data (base de connaissances) · Règlement (UE) 2026/1744 · Règlement (UE) 2025/327 · Modèle en validation clinique ; il ne remplace pas le diagnostic · Dispositifs médicaux : ANSM · Autorités IA : loi DDADUE (en attente)",
 "Ouverture", "Dental Data · Question 6", "Comment entraîner une", "IA dentaire", "sans déplacer les radiographies ?",
 "Le dilemme", "Entraîner une IA exige beaucoup de radiographies…", "les réunir est un risque", "Un stockage central",
 "Centraliser les radiographies augmente le risque",
 "L'algorithme voyage", "Dental Data inverse le chemin :", "l'algorithme voyage", "Modèle d'IA",
 "Cabinet", "les radiographies restent", "Cabinet", "les radiographies restent", "Cabinet", "les radiographies restent",
 "apprend", "Apprend dans chaque cabinet", "renvoie", "Ne renvoie que ce qu'il a appris",
 "Calcul confidentiel", "Calcul", "confidentiel", "Protège les données même pendant leur traitement.",
 "Le modèle", "Premier modèle", "Caries interproximales", "Sur radiographies dentaires.", "osseuse", "Perte osseuse parodontale",
 "Sur radiographies dentaires.", "validation", "En validation clinique", "aide", "Une aide pour le professionnel : ne remplace pas le diagnostic",
 "Ce qui vient", "Prêt pour", "ce qui vient", "2 août 2028", "Règlement IA : obligations pour l'IA des dispositifs médicaux",
 "deux mille trente et un", "26 mars 2031", "Les images médicales entrent dans l'Espace européen des données de santé",
 "Conclusion", "L'algorithme", "va vers la donnée.", "L'IA sur les images dentaires sans déplacer les radiographies.",
], """Entraîner une IA dentaire exige beaucoup de radiographies. Mais les réunir en un seul lieu est un risque. Dental Data inverse
 le chemin : l'algorithme voyage jusqu'à chaque cabinet, y apprend et ne renvoie que ce qu'il a appris, jamais les images. Les calculs se
 font avec le calcul confidentiel, qui protège les données pendant leur traitement. Le premier modèle, pour les caries interproximales et
 la perte osseuse parodontale, est en validation clinique. C'est une aide pour le professionnel : il ne remplace pas son diagnostic. Et
 il se prépare à ce qui vient : en deux mille trente et un, les images médicales entrent dans l'Espace européen des données de santé.
 L'algorithme va vers la donnée.""",
 ["Entraîner une IA", "Dental Data inverse", "Les calculs se", "Le premier modèle", "Et il se prépare", "L'algorithme va"]),

"p07": ([
 "Quelles dates fixe l'Espace européen des données de santé ?", "Quelles dates fixe l'EHDS ?",
 "Présentation animée de Dental Data : le calendrier de l'EHDS et la situation en France (Plateforme des données de santé).",
 "Sources : Règlement (UE) 2025/327 (art. 50 et 105) · Plateforme des données de santé · Ministère de la Santé (2026)",
 "Ouverture", "Dental Data · Question 7", "Quelles dates fixe l'", "Espace européen des données de santé", " ?",
 "Calendrier", "Déjà en vigueur", "et avec des dates", "26 mars 2025", "En vigueur", "deux mille vingt-sept", "26 mars 2027",
 "Organismes d'accès désignés", "deux mille vingt-neuf", "26 mars 2029", "Usage secondaire : l'essentiel des règles",
 "deux mille trente et un", "26 mars 2031", "Images médicales, comme les radiographies",
 "La fenêtre", "Entre 2027 et 2029 :", "deux ans pour relier cabinets et réseaux",
 "26 mars 2025", "En vigueur", "26 mars 2027", "Organismes d'accès désignés", "26 mars 2029", "Usage secondaire : l'essentiel des règles",
 "26 mars 2031", "Images médicales, comme les radiographies",
 "Article 50", "La plupart des cabinets sont des microentreprises :", "exemptés par défaut", "participer", "à travers",
 "Cabinets libéraux", "Art. 50 : exemptés sauf décision contraire de l'État", "canal agrégé", "Canal agrégé",
 "réseaux de centres · complémentaires · syndicats", "à travers", "Espace de données dentaires",
 "France", "France", "Plateforme des données de santé (Health Data Hub)", "candidate",
 "La Plateforme se porte candidate pour devenir l'organisme d'accès ; la décision n'est pas prise. Migration vers un hébergement souverain fin 2026–2027. Ségur et Mon espace santé côté soins.",
 "souverain", "Candidate · décision en attente (nov. 2026)",
 "Conclusion", "Qui sera connecté en 2029", "sera l'interlocuteur naturel", "des organismes d'accès aux données de santé.",
], """L'Espace européen des données de santé est déjà en vigueur et a des dates. En mars deux mille vingt-sept, chaque pays aura
 désigné ses organismes d'accès ; en mars deux mille vingt-neuf, l'essentiel de l'usage secondaire s'applique, et en deux mille trente et
 un arrivent les images médicales, comme les radiographies dentaires. La plupart des cabinets sont des microentreprises et sont exemptés
 par défaut : pour participer, il faut un canal agrégé, à travers les réseaux de centres, les complémentaires ou les syndicats. En France,
 la Plateforme des données de santé est candidate pour être l'organisme d'accès, mais la décision n'est pas prise, et elle migre vers un
 hébergement souverain entre fin deux mille vingt-six et deux mille vingt-sept. Qui arrivera connecté sera l'interlocuteur naturel.""",
 ["L'Espace européen des", "en mars deux mille vingt-neuf", "La plupart des cabinets", "En France, la Plateforme", "Qui arrivera"]),

"p08": ([
 "Quelle technologie se cache derrière Dental Data ?", "Quelle technologie derrière Dental Data ?",
 "Présentation animée de Dental Data : Microsoft ou un hébergeur souverain dans le nœud, des standards européens ouverts aux frontières.",
 "Sources : Dental Data · technologie et entreprise (base de connaissances) · Microsoft et Azure sont des marques de Microsoft Corporation ; cités comme texte",
 "Ouverture", "Dental Data · Question 8", "Quelle technologie se cache derrière", "Dental Data", " ?",
 "La règle", "Une règle simple", "Microsoft", "Azure", "ou souverain", "Dans le nœud", "À la frontière : standards ouverts",
 "Dans le nœud", "Dans le nœud :", "Microsoft", "Connecteur sur Azure ou hébergeur souverain", "Avec les données dans l'Union européenne.",
 "intégré", "Intégré", "Au logiciel de gestion du cabinet.", "déployé", "Déployé par des partenaires", "Intégrateurs et partenaires Azure.",
 "À la frontière", "Aux frontières :", "des standards européens ouverts", "gaiax", "Gaia-X", "protocole", "IDSA", "eclipse", "Dataspace Protocol",
 "eclipse edc", "Eclipse EDC", "vérifiables", "Attestations vérifiables", "fhir", "FHIR", "dicom", "DICOM", "healthdcatap", "HealthDCAT-AP",
 "Ouvert à tous", "Tout le monde peut se connecter,", "même sans Microsoft", "Nœud sur Azure", "Participant sans Microsoft",
 "Standards ouverts", "Se connecte de la même façon",
 "Expérience", "Nous ne partons pas de zéro :", "trois espaces de données réels", "Global Data Care", "Santé, sur Gaia-X et Pontus-X.",
 "PROCUREDATA", "Marchés publics.", "EcoDataNet", "Déchets et économie circulaire.",
 "Démonstrateurs financés par la SEDIA (2024–2026), avec nos propres connecteurs basés sur Eclipse.",
 "Conclusion", "Le nœud chez l'hébergeur de votre choix.", "Des standards ouverts aux frontières.", "Un espace de données dentaires ouvert à tous.",
], """Dental Data suit une règle simple : Microsoft dans le nœud, des standards ouverts aux frontières. Dans chaque nœud, le connecteur
 fonctionne sur Microsoft Azure dans l'Union européenne ou chez un hébergeur souverain certifié, intégré au logiciel de gestion du cabinet
 et déployé par des partenaires. Aux frontières, l'espace parle des standards européens ouverts : Gaia-X, le protocole des espaces de
 données, Eclipse EDC, des attestations vérifiables, FHIR, DICOM et HealthDCAT-AP. Ainsi, tout participant peut se connecter, même sans
 Microsoft. Et nous ne partons pas de zéro : Software in a Box a déjà conçu et exploité trois espaces de données réels.""",
 ["suit une règle", "Dans chaque nœud", "Aux frontières, l'espace", "Ainsi, tout", "Et nous ne partons", "FIN"]),

"p09": ([
 "Qu'offre Dental Data à l'industrie ?", "Qu'offre Dental Data à l'industrie ?",
 "Présentation animée de Dental Data : des données de vie réelle sous contrat pour les fabricants, les entreprises d'IA et les éditeurs de logiciels.",
 "Sources : Dental Data (base de connaissances) · Règlement (UE) 2025/327, art. 54",
 "Ouverture", "Dental Data · Question 9", "Qu'offre Dental Data à l'", "industrie", " ?",
 "Qui", "Pour ceux qui doivent savoir", "ce qui se passe au cabinet", "Implants", "matériaux", "Matériaux", "intelligence", "Intelligence artificielle",
 "doivent", "Logiciels de gestion",
 "Données de vie réelle", "Des données de vie réelle,", "sans données identifiables", "Industrie", "question sous contrat",
 "Cabinets", "Cabinets", "Cabinets", "Les résultats agrégés reviennent, jamais les dossiers",
 "Pour les éditeurs", "Pour les éditeurs de logiciels :", "un connecteur qui ajoute des services", "Logiciels référencés Ségur",
 "Connecteur intégré", "Nouveaux services", "pour vos clients",
 "Les règles", "Les règles", "ne changent pas", "Un contrat pour chaque usage", "Qui, pour quoi et combien de temps.", "seulement des résultats",
 "Agrégé uniquement", "Aucune donnée identifiable ne quitte le cabinet.", "jamais", "Jamais de publicité", "L'EHDS l'interdit (art. 54).",
 "Conclusion", "Des preuves réelles,", "ordonnées et sous contrat.", "Pour l'industrie et les logiciels dentaires.",
], """Pour l'industrie dentaire, les données de vie réelle valent beaucoup. Les fabricants d'implants et de matériaux, et les
 entreprises d'intelligence artificielle, doivent savoir comment leurs produits se comportent au cabinet. Dental Data leur offre ces
 preuves, ordonnées et sous contrat : des questions qui trouvent leur réponse dans les cabinets et des résultats agrégés qui reviennent
 sans données identifiables. Pour les éditeurs de logiciels de gestion, le connecteur est une brique qui s'intègre à leur produit et
 ouvre de nouveaux services à leurs clients. Les règles ne changent pas : un contrat pour chaque usage, seulement des résultats agrégés et
 jamais de publicité. Des preuves réelles, ordonnées et sous contrat.""",
 ["Pour l'industrie dentaire", "Dental Data leur offre", "Pour les éditeurs", "Les règles ne", "Des preuves réelles"]),

"p10": ([
 "Comment rejoindre Dental Data ?", "Comment rejoindre Dental Data ?",
 "Présentation animée de Dental Data : le programme de partenaires en France, la feuille de route et comment nous rejoindre.",
 "Sources : Dental Data · programme de partenaires France et feuille de route (base de connaissances) · Pas de tarifs publiés",
 "Ouverture", "Dental Data · Question 10", "Comment rejoindre", "Dental Data", " ?",
 "Nous cherchons", "Nous cherchons", "Une complémentaire ou un réseau de centres", "Pour un premier projet d'indicateurs de qualité",
 "projet", "Premier projet 2027",
 "Financement", "Le cas d'usage", "finance le connecteur", "Hébergement au choix : Azure (région UE) ou hébergeur souverain certifié HDS / SecNumCloud. Le montant dépend du nombre de cabinets et se fixe lors d'un échange.",
 "Feuille de route", "La", "feuille de route", "2027", "Premiers nœuds", "consolidons", "2027–2029",
 "Consolider les projets et participer aux consultations", "catalogués", "2029", "Jeux de données catalogués pour l'EHDS",
 "ensuite", "2029–2031", "Ligne d'imagerie dentaire",
 "Nous voulons aussi parler avec", "Nous voulons aussi parler avec…", "ANS · ONCD", "éditeurs", "Éditeurs Ségur",
 "hébergement", "Hébergeurs HDS / SecNumCloud", "ordre", "Ordre", "syndicats", "CDF et FSDL",
 "On en parle ?", "On en parle ?", "partners@softwareinabox.eu", "+34 601 398 868", "dentaldata.softwareinabox.eu",
], """En France, nous cherchons une complémentaire ou un réseau de centres de santé dentaires pour un premier projet d'indicateurs
 de qualité. Le cas d'usage finance le connecteur, et le client choisit où le nœud est hébergé : sur Azure, dans l'Union européenne, ou
 chez un hébergeur souverain certifié pour les données de santé. En deux mille vingt-sept, les premiers nœuds ; puis nous consolidons les
 projets ; en deux mille vingt-neuf, des jeux de données catalogués et prêts pour l'espace européen ; ensuite, l'imagerie dentaire. Nous
 voulons aussi parler avec les éditeurs de logiciels référencés Ségur, avec les prestataires d'hébergement certifiés, avec l'Ordre et
 avec les syndicats de chirurgiens-dentistes. On en parle ? Écrivez à partners arobase softwareinabox point eu.""",
 ["En France, nous", "Le cas d'usage", "En deux mille vingt-sept", "Nous voulons aussi", "On en parle ?"]),

"p11": ([
 "Que construisons-nous sur Microsoft Azure ?", "Que construisons-nous sur Microsoft Azure ?",
 "Présentation animée de Dental Data : l'architecture de l'espace de données dentaires avec les composants Microsoft Azure, le connecteur Eclipse EDC et l'option d'hébergement souverain.",
 "Sources : Dental Data · document technique (v1.3) et proposition MVP (v1.4) · Icônes officielles Microsoft (Azure, Microsoft Entra et Microsoft Fabric), utilisées selon leurs conditions pour les schémas d'architecture · Microsoft, Azure, Entra, Fabric et les noms de leurs services sont des marques de Microsoft Corporation",
 "Ouverture", "Dental Data · Question 11", "Que construisons-nous sur", "Microsoft Azure", " ?",
 "La règle", "Une règle guide la conception", "Frontière · standards ouverts", "Nœud · Azure ou souverain", "Microsoft", "dans le nœud",
 "Le nœud chez l'hébergeur de votre choix ; des standards ouverts à la frontière",
 "Le cabinet", "1 · Au", "cabinet", "Appareil de radiologie", "radiographie, cone beam", "passerelle DICOM", "Passerelle DICOM", "Orthanc · open source",
 "pseudonymisée", "Pseudonymisée à la source", "sans données identifiant le patient",
 "Le nœud de données", "2 · Le", "nœud de données", "sur Azure ou souverain", "Nœud de données · Azure (région UE) ou hébergeur HDS / SecNumCloud", "azure health", "Azure Health Data Services",
 "le dossier", "Dossier · FHIR", "l'image", "Image · DICOM", "microsoft fabric", "Microsoft Fabric", "prépare l'analyse",
 "onelake", "OneLake", "formats ouverts",
 "Sécurité", "3 · Une couche de", "sécurité et d'identité", "Sécurité et identité · autour de tout",
 "entra id", "Microsoft Entra ID", "identités", "key vault", "Azure Key Vault", "clés et secrets", "defender",
 "Microsoft Defender for Cloud", "protection", "sentinel", "Microsoft Sentinel", "surveillance",
 "La frontière", "4 · La", "frontière", " : le connecteur Eclipse EDC", "Frontière · standards ouverts", "azure kubernetes", "Azure Kubernetes Service",
 "où il tourne", "Eclipse", "Connecteur Eclipse EDC", "open source", "publie", "Catalogue", "HealthDCAT-AP",
 "négocie", "Contrat", "ODRL", "s'identifie", "Attestations", "Gaia-X",
 "L'IA", "5 · L'", "IA", " : le modèle voyage, pas les données", "azure machine", "Azure Machine Learning",
 "apprentissage fédéré · NVIDIA FLARE", "Cabinet A", "Cabinet B", "Cabinet C", "le modèle voyage", "le modèle voyage", "le modèle voyage",
 "calcul confidentiel", "Calcul confidentiel", "protège les données pendant le traitement", "microsoft foundry", "Microsoft Foundry",
 "brouillons que le dentiste vérifie",
 "Le parcours", "Le parcours d'une radiographie", "Cabinet", "Passerelle DICOM", "Azure Health Data Services", "Microsoft Fabric et OneLake",
 "Eclipse EDC", "sur Azure Kubernetes Service", "Réseau européen", "autres cabinets", "Sécurité et identité",
 "Microsoft Entra ID · Azure Key Vault · Microsoft Defender for Cloud · Microsoft Sentinel", "donnée identifiable",
 "Quel que soit l'hébergement, aucune donnée identifiable ne quitte le nœud",
 "Conclusion", "Le nœud chez l'hébergeur de votre choix.", "Des standards ouverts à la frontière.", "Voilà comment nous construisons Dental Data.",
], """Voici ce que nous construisons sur Microsoft Azure pour Dental Data. Une règle guide la conception : le nœud chez l'hébergeur de
 votre choix, des standards ouverts à la frontière. Au cabinet, la radiographie quitte l'appareil par une passerelle DICOM open source,
 Orthanc, et elle est pseudonymisée à la source. Dans le nœud de données, Azure Health Data Services conserve le dossier en FHIR et
 l'image en DICOM. Microsoft Fabric et OneLake préparent les données pour l'analyse. Si le client l'exige, le même nœud peut être installé
 chez un hébergeur européen certifié pour les données de santé et qualifié de cloud de confiance. La sécurité repose sur Microsoft Entra
 ID, Azure Key Vault, Microsoft Defender for Cloud et Microsoft Sentinel. À la frontière travaille le connecteur Eclipse EDC, déployé sur
 Azure Kubernetes Service. Il publie le catalogue en HealthDCAT-AP, négocie des contrats ODRL et s'identifie avec des attestations Gaia-X.
 La frontière ne change pas : le même connecteur, le même catalogue et les mêmes contrats. L'intelligence artificielle est entraînée avec
 Azure Machine Learning et l'apprentissage fédéré : le modèle voyage jusqu'à chaque cabinet et les données restent où elles sont. Le
 calcul confidentiel protège les données même pendant le traitement, et Microsoft Foundry rédige des brouillons de comptes rendus que le
 dentiste vérifie. Ainsi, chaque radiographie suit un chemin sûr et contrôlé, du cabinet au modèle, sans qu'aucune donnée identifiable
 ne quitte le nœud.""",
 ["Voici ce que", "Au cabinet, la radiographie", "Dans le nœud de données", "La sécurité repose", "À la frontière travaille", "L'intelligence artificielle", "Ainsi, chaque", "FIN"]),
}
