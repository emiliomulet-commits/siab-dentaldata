import importlib.util as _u, os as _o, copy as _c
_s = _u.spec_from_file_location("_fr", _o.path.join(_o.path.dirname(__file__), "fr.py")); _b = _u.module_from_spec(_s); _s.loader.exec_module(_b)
LANG = "fr-BE"
UI = dict(_b.UI)

def _sub(piece, pares):
    seg, loc, anc = _c.deepcopy(piece); loc = " ".join(loc.split())
    for a, b in pares:
        seg = [x.replace(a, b) for x in seg]; loc = loc.replace(a, b); anc = [x.replace(a, b) for x in anc]
    return (seg, loc, anc)

PIEZAS = {}
PIEZAS["p02"] = _sub(_b.PIEZAS["p02"], [
    ("chaque cabinet ou centre de santé, chaque réseau ou complémentaire", "chaque cabinet, chaque groupe, chaque mutualité ou assureur"),
    ("Centre de santé", "Cabinet"), ("Réseau de centres", "Groupe de cabinets"), ("Complémentaire", "Mutualité")])
PIEZAS["p06"] = _sub(_b.PIEZAS["p06"], [("Dispositifs médicaux : ANSM · Autorités IA : loi DDADUE (en attente)", "Dispositifs médicaux : AFMPS · autorité IA encore à désigner")])
PIEZAS["p09"] = _sub(_b.PIEZAS["p09"], [("Logiciels référencés Ségur", "Logiciels homologués eHealth")])

_p8 = _sub(_b.PIEZAS["p08"], [
    ("Microsoft ou un hébergeur souverain dans le nœud", "Microsoft dans le nœud"),
    ("Connecteur sur Azure ou hébergeur souverain", "Connecteur sur Microsoft Azure"),
    ("sur Microsoft Azure dans l'Union européenne ou chez un hébergeur souverain certifié, intégré", "sur Microsoft Azure, avec les données dans l'Union européenne, intégré"),
    ("Le nœud chez l'hébergeur de votre choix.", "Microsoft dans le nœud.")])
_p8[0][_p8[0].index("ou souverain")] = "données dans l'UE"
PIEZAS["p08"] = _p8

_p11 = _sub(_b.PIEZAS["p11"], [
    ("Le nœud chez l'hébergeur de votre choix ; des standards ouverts à la frontière", "Des standards ouverts à la frontière"),
    ("Nœud · Azure ou souverain", "Nœud · Microsoft Azure"), ("sur Azure ou souverain", "sur Azure"),
    ("Nœud de données · Azure (région UE) ou hébergeur HDS / SecNumCloud", "Nœud de données · Microsoft Azure"),
    (", le connecteur Eclipse EDC et l'option d'hébergement souverain", " et le connecteur Eclipse EDC"),
    ("Quel que soit l'hébergement, aucune donnée identifiable ne quitte le nœud", "Aucune donnée identifiable ne quitte le nœud"),
    ("Le nœud chez l'hébergeur de votre choix.", "Microsoft dans le nœud."),
    ("Une règle guide la conception : le nœud chez l'hébergeur de votre choix, des standards ouverts à la frontière.",
     "Une règle guide la conception : Microsoft dans le nœud, des standards ouverts à la frontière."),
    (" Si le client l'exige, le même nœud peut être installé chez un hébergeur européen certifié pour les données de santé et qualifié de cloud de confiance.", ""),
    (" La frontière ne change pas : le même connecteur, le même catalogue et les mêmes contrats.", "")])
PIEZAS["p11"] = _p11

_p3 = list(_b.PIEZAS["p03"][0])
_p3[3] = "Sources : Dental Data (base de connaissances) · RGPD · loi du 30 juillet 2018 · loi relative aux droits du patient · Règlement (UE) 2025/327, art. 54 et 71 · Information générale ; pas un conseil juridique"
_i = _p3.index("Informatique"); _p3[_i] = "belge"; _p3[_i + 1] = "Loi du 30 juillet 2018 · Autorité de protection des données (APD)"
_i = _p3.index("hébergeur"); _p3[_i] = "patient"; _p3[_i + 1] = "Dossier patient conservé 30 ans"
PIEZAS["p03"] = (_p3, """Les données sortent-elles du cabinet ? Non. Aucun dossier identifiable ne quitte le cabinet. Chaque usage des données est
 régi par un contrat numérique qui définit qui accède, pour quoi et combien de temps. Et ce contrat ne reste pas sur le papier : la
 machine le fait respecter elle-même. Si une demande n'a pas de contrat, il n'y a pas d'accès. Si elle en a un, seul un résultat agrégé
 revient. Le cabinet décide toujours, dans le cadre du règlement général sur la protection des données et de la législation belge sur
 les droits du patient. Et avec une règle claire de l'Espace européen des données de santé : les données de santé ne sont jamais
 utilisées pour la publicité.""",
 ["Les données sortent-elles", "Chaque usage", "Si une demande", "Le cabinet décide", "FIN"])

PIEZAS["p01"] = ([
 "Pourquoi les données dentaires manquent-elles à l'Espace européen des données de santé ?",
 "Pourquoi les données dentaires manquent-elles à l'EHDS ?",
 "Présentation animée de Dental Data : pourquoi les soins dentaires sont les grands absents de l'Espace européen des données de santé (EHDS).",
 "Sources : étude comparative de Software in a Box (nov. 2026) · INAMI (accord 2026) · Enquête de santé Sciensano",
 "Ouverture", "Dental Data · Question 1", "Pourquoi les données dentaires manquent-elles à l'", "Espace européen des données de santé", " ?",
 "Les grandes absentes", "Espace européen des données de santé (EHDS)", "Les données dentaires sont", "les grandes absentes",
 "Dossier patient", "Prescription électronique", "Images médicales", "Biologie", "Soins dentaires", "non reliés",
 "Pourquoi", "Non par manque de valeur, mais à cause de", "l'organisation", "des soins dentaires",
 "Assurance obligatoire", "Chaque acte codé", "Facturation électronique", "Depuis 2025",
 "Logiciels homologués", "Chaque cabinet le sien", "Pas de résultats", "Facturé, pas mesuré",
 "La Belgique en chiffres", "Belgique", "Assurée, codée et pourtant invisible",
 "60", "&lt;small&gt;,48 %&lt;/small&gt;", "soixante", "0", "conventionnés", "des dentistes sont conventionnés",
 "19", " ", "&lt;small&gt;&amp;lt;&lt;/small&gt;", "dix-neuf", "0", "gratuits", "ans : soins de base gratuits",
 "4", " ", "quatre", "0", "Belge", "un Belge sur quatre ne va pas chez le dentiste chaque année",
 "Îlots de données", "Les données existent, mais elles vivent", "sur des îlots", "mesurés", "Actes facturés, résultats non mesurés",
 "logiciel", "Sans lien entre cabinets",
 "Conclusion", "Les données existent.", "Personne ne les relie.", "Dental Data les relie", "sans les déplacer", ".",
], """Les données dentaires sont les grandes absentes de l'Espace européen des données de santé. En Belgique, pourtant, les soins
 dentaires relèvent de l'assurance obligatoire : chaque acte remboursé a son code et, depuis septembre deux mille vingt-cinq, il est
 facturé électroniquement. Les jeunes de moins de dix-neuf ans ont des soins de base gratuits, soixante pour cent des dentistes sont
 conventionnés, et pourtant un Belge sur quatre ne va pas chez le dentiste chaque année. Personne ne sait si les traitements payés
 fonctionnent : les actes sont facturés, les résultats ne sont pas mesurés. Les données cliniques existent et se trouvent dans chaque
 cabinet, dans son propre logiciel. Ce qui manque, c'est quelqu'un pour les relier. C'est Dental Data.""",
 ["Les données dentaires sont", "En Belgique, pourtant", "Les jeunes de moins", "Personne ne sait", "Les données cliniques existent"])

PIEZAS["p04"] = ([
 "Que gagne un groupe de cabinets ?", "Que gagne un groupe de cabinets ?",
 "Présentation animée de Dental Data : des indicateurs de qualité comparables entre cabinets, sans migrer les dossiers.",
 "Sources : Dental Data · cas d'usage et pilote (base de connaissances) · Conseil de l'Art dentaire (2025) · nomenclature INAMI · Règlement (UE) 2025/327, art. 72 · Barres illustratives",
 "Ouverture", "Dental Data · Question 4", "Que gagne un", "groupe de cabinets", " ?",
 "Le problème", "Des groupes financiers rachètent des cabinets…", "et chaque cabinet a son logiciel",
 "Cabinet 1", "Logiciel A", "Cabinet 2", "Logiciel B", "Cabinet 3", "Logiciel C", "Cabinet 4", "Logiciel D", "Cabinet 5", "Logiciel E",
 "migrer", "Pas de règles spécifiques pour les chaînes · comparer oblige aujourd'hui à migrer les dossiers",
 "Sans migration", "Avec Dental Data, inutile de migrer :", "un connecteur à côté de chaque logiciel",
 "Cabinet 1", "Logiciel A", "Connecteur", "Cabinet 2", "Logiciel B", "Connecteur", "Cabinet 3", "Logiciel C", "Connecteur",
 "Cabinet 4", "Logiciel D", "Connecteur", "Cabinet 5", "Logiciel E", "Connecteur",
 "Indicateurs comparables", "Le même indicateur,", "calculé dans chaque cabinet",
 "Cabinet 1", "Cabinet 2", "Cabinet 3", "Cabinet 4", "Cabinet 5",
 "Même définition, liée aux codes de la nomenclature INAMI", "change de place", "Aucun dossier ne change de place",
 "Valeur ajoutée", "Et en plus…", "Qualité démontrable", "Avant même que la règle n'arrive.",
 "préparé", "Préparé pour la norme de demain", "Avis du Conseil de l'Art dentaire (2025).",
 "Conclusion", "Une qualité démontrable,", "sans migrer un seul dossier.", "Des indicateurs de qualité comparables dans tout le groupe.",
], """En Belgique, des groupes financiers rachètent des cabinets dentaires et forment des chaînes, chacune avec des cabinets qui
 utilisent leur propre logiciel. Le Conseil de l'Art dentaire a averti en deux mille vingt-cinq que le pays est l'un des rares sans règles
 pour ces chaînes, et a demandé que la qualité prime. Comparer la qualité entre cabinets oblige aujourd'hui à migrer les dossiers. Avec
 Dental Data, inutile de migrer : un connecteur est installé à côté de chaque logiciel et les indicateurs sont calculés dans chaque cabinet
 avec la même définition, liés aux codes de la nomenclature. La direction voit des résultats comparables sans qu'aucun dossier ne change
 de place. Un groupe qui mesure sa qualité aujourd'hui sera préparé pour la norme de demain.""",
 ["En Belgique, des groupes", "Avec Dental Data", "La direction voit", "sans qu'aucun dossier", "Un groupe qui"])

PIEZAS["p05"] = ([
 "Que gagne une mutualité ?", "Que gagne une mutualité ?",
 "Présentation animée de Dental Data : de l'acte facturé au résultat mesuré, sans centraliser les dossiers.",
 "Sources : Dental Data (base de connaissances) · INAMI · Agence InterMutualiste (AIM) · Règlement (UE) 2025/327, art. 54",
 "Ouverture", "Dental Data · Question 5", "Que gagne une", "mutualité", " ?",
 "Le réseau", "Des cabinets dans toute la Belgique,", "chacun avec son logiciel",
 "Mutualités", "INAMI", "nomenclature", "AIM", "eAttest et eFact", "Cabinet", "son logiciel",
 "Cabinet", "son logiciel", "Actes connus, résultats inconnus",
 "Données cohérentes", "Le résultat des soins,", "sans centraliser les dossiers",
 "Mutualité", "Cabinet", "son logiciel", "Cabinet", "son logiciel", "Cabinet", "son logiciel", "Cabinet", "son logiciel",
 "Calcul au cabinet · seul le résultat agrégé revient",
 "Un canal", "Pour évaluer", "le trajet de soins buccaux", "Trajet de soins buccaux", "Gratuité < 19 ans", "cone beam", "Espace de données dentaires",
 "Limites claires", "Avec des limites claires :", "ce que l'EHDS interdit", "publicité", "Publicité",
 "Les données de santé ne servent jamais à la publicité.", "décisions", "Décisions préjudiciables",
 "Ni à des décisions qui nuisent aux personnes.", "Règlement (UE) 2025/327, article 54",
 "Conclusion", "De l'acte facturé", "au résultat mesuré.", "Sans centraliser les dossiers.",
], """En Belgique, les mutualités remboursent les soins dentaires, et l'Agence InterMutualiste analyse la facturation de toutes. Elles
 savent quels actes sont payés, mais pas quel résultat ils ont. Dental Data leur donne ce résultat sans centraliser les dossiers :
 l'indicateur est calculé dans chaque cabinet et seul l'agrégat revient. On peut ainsi évaluer si le trajet de soins buccaux améliore la
 santé dentaire, quel effet a la gratuité pour les moins de dix-neuf ans ou comment le cone beam est utilisé. Avec des limites claires :
 l'EHDS interdit d'utiliser ces données pour la publicité ou pour des décisions qui nuisent aux personnes. De l'acte facturé au résultat
 mesuré, sans centraliser les dossiers.""",
 ["En Belgique, les mutualités", "Dental Data leur donne", "On peut ainsi", "Avec des limites", "De l'acte facturé"])

_p7 = list(_b.PIEZAS["p07"][0])
_p7[2] = "Présentation animée de Dental Data : le calendrier de l'EHDS et la mise en œuvre belge (Health Data Agency)."
_p7[3] = "Sources : Règlement (UE) 2025/327 (art. 50 et 105) · loi de 2023 créant la Health Data Agency · plateforme eHealth"
_i = _p7.index("réseaux de centres · complémentaires · syndicats"); _p7[_i] = "associations · mutualités · groupes de cabinets"
_i = _p7.index("Plateforme des données de santé (Health Data Hub)"); _p7[_i - 2] = "Belgique"; _p7[_i - 1] = "Belgique"
_p7[_i] = "Health Data Agency (loi de 2023)"; _p7[_i + 1] = "catalogue"
_p7[_i + 2] = "Catalogue national et guichet unique ; attendue comme organisme d'accès, pas encore désignée. La plateforme eHealth assure la pseudonymisation."
_p7[_i + 3] = "pseudonymisation"; _p7[_i + 4] = "Attendue · pas encore désignée (nov. 2026)"
PIEZAS["p07"] = (_p7, """L'Espace européen des données de santé est déjà en vigueur et a des dates. En mars deux mille vingt-sept, chaque pays aura
 désigné ses organismes d'accès ; en mars deux mille vingt-neuf, l'essentiel de l'usage secondaire s'applique, et en deux mille trente et
 un arrivent les images médicales. La plupart des cabinets dentaires sont des microentreprises et sont exemptés par défaut : pour participer,
 il faut un canal agrégé, à travers les associations, les mutualités ou les groupes de cabinets. La Belgique a pris de l'avance : la Health Data
 Agency existe par la loi depuis deux mille vingt-trois, dispose d'un catalogue national et devrait devenir l'organisme d'accès. La
 plateforme eHealth offre déjà la pseudonymisation. Qui arrivera connecté sera l'interlocuteur naturel.""",
 ["L'Espace européen des", "en mars deux mille vingt-neuf", "La plupart des cabinets", "La Belgique a pris", "Qui arrivera"])

PIEZAS["p10"] = ([
 "Comment rejoindre Dental Data ?", "Comment rejoindre Dental Data ?",
 "Présentation animée de Dental Data : une alliance institutionnelle en Belgique, la feuille de route et comment nous rejoindre.",
 "Sources : Dental Data · programme de partenaires Belgique et feuille de route (base de connaissances) · Pas de tarifs publiés",
 "Ouverture", "Dental Data · Question 10", "Comment rejoindre", "Dental Data", " ?",
 "Nous cherchons", "Nous cherchons", "Une alliance institutionnelle", "Avec les premières chaînes et groupes de cabinets comme utilisateurs",
 "alliance", "Pas un pilote isolé",
 "Financement", "Le cas d'usage", "finance le connecteur", "Les groupes financent le connecteur par leur cas d'usage interne ; la recherche par des projets partagés avec la HDA et les mutualités.",
 "Feuille de route", "La", "feuille de route", "2027", "Premières connexions", "connexions", "2027–2028",
 "Définir les indicateurs avec l'INAMI, la HDA et les mutualités", "catalogués", "2029", "Jeux de données catalogués auprès de la HDA",
 "ensuite", "2029–2031", "Ligne d'imagerie dentaire",
 "Nous voulons aussi parler avec", "Nous voulons aussi parler avec…", "INAMI · HDA · eHealth · AIM", "associations", "SMD et VVT",
 "conseil", "Conseil de l'Art dentaire", "logiciels", "Logiciels homologués", "groupes", "Groupes de cabinets",
 "On en parle ?", "On en parle ?", "partners@softwareinabox.eu", "+34 601 398 868", "dentaldata.softwareinabox.eu",
], """En Belgique, nous ne voulons pas commencer par un pilote isolé, mais par une alliance. Nous voulons définir avec l'INAMI, la
 Health Data Agency, la plateforme eHealth et les mutualités les premiers indicateurs de résultats dentaires, et travailler avec des
 chaînes et des groupes de cabinets qui veulent mesurer leur qualité dès maintenant. Les groupes financent le connecteur par leur cas
 d'usage interne ; la recherche, par des projets partagés. En deux mille vingt-sept, les premières connexions ; en deux mille vingt-neuf,
 des jeux de données catalogués et prêts pour la HDA ; ensuite, l'imagerie dentaire. Nous voulons aussi parler avec les associations de
 dentistes, le conseil de l'art dentaire, les éditeurs de logiciels homologués et les groupes de cabinets. On en parle ? Écrivez à
 partners arobase softwareinabox point eu.""",
 ["En Belgique, nous ne", "Les groupes financent", "En deux mille vingt-sept", "Nous voulons aussi", "On en parle ?"])
