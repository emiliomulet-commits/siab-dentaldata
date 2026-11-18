# Dental Data Belgique (français) · https://dentaldata.softwareinabox.eu/fr-be/
# Marché «be» : alliance institutionnelle (Health Data Agency, INAMI, mutualités, associations professionnelles), pas d'appel à pilote.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "idiomas"))
from _mercado import desde_claves

SALIDA = "fr-be/index.html"
LANG = "fr-BE"
IDIOMA_COMUN = "fr"
SIAB = "fr-be"
PERMITIDO = ['lang="es"', "Español", "España"]

JSONLD = r'''
{"@context":"https://schema.org","@graph":[
{"@type":"WebPage","@id":"https://dentaldata.softwareinabox.eu/fr-be/#webpage","url":"https://dentaldata.softwareinabox.eu/fr-be/","name":"Dental Data Belgique · Espace de données dentaires fédéré","inLanguage":"fr-BE","isPartOf":{"@type":"WebSite","@id":"https://www.softwareinabox.eu/#website","name":"Software in a Box"},"publisher":{"@type":"Organization","@id":"https://www.softwareinabox.eu/#organization","name":"Software in a Box","url":"https://www.softwareinabox.eu/"},"areaServed":"BE"},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Mes données quittent-elles le cabinet ?","acceptedAnswer":{"@type":"Answer","text":"Non. Les dossiers restent dans le logiciel de chaque cabinet, chaîne ou assureur. Seuls les consentements, les métadonnées et les résultats agrégés circulent, selon des contrats d’utilisation appliqués par la machine."}},
{"@type":"Question","name":"Qu’apporte Dental Data aux données de l’INAMI ?","acceptedAnswer":{"@type":"Answer","text":"La facturation à l’INAMI et aux mutualités produit des données structurées sur les prestations remboursées. Le dossier complet et les soins non remboursés restent dans le logiciel du cabinet. Dental Data rend cette partie visible sans la centraliser."}},
{"@type":"Question","name":"Que signifie l’EEDS pour les soins dentaires en Belgique ?","acceptedAnswer":{"@type":"Answer","text":"La Health Data Agency (créée en 2023) devrait devenir l’organisme coordinateur responsable de l’accès aux données de santé. D’ici le 26 mars 2027, chaque État membre désigne ses organismes d’accès ; à partir du 26 mars 2029, la plupart des règles d’utilisation secondaire s’appliquent ; à partir de 2031, les images médicales s’y ajoutent."}}
]}]}
'''

KB_JS = r'''[
{id:'datos',q:'Mes données quittent-elles le cabinet ?',k:['quitter','quittent','déplac','central','stock','où sont','cloud','serveur','confidential','copie','partag'],
 a:['Non. Les dossiers restent dans le logiciel de gestion de chaque cabinet, chaîne ou assureur. Dental Data est un espace de données <b>fédéré</b> : seuls les consentements, les métadonnées et les résultats agrégés circulent.','Chaque accès est régi par un contrat ODRL que la machine fait respecter : le cabinet décide qui accède, dans quel but et pour combien de temps. Pas de contrat, pas d’accès.'],s:['ia','seguridad']},
{id:'inami',q:'Qu’apporte Dental Data aux données de l’INAMI ?',k:['inami','riziv','mutualit','rembours','facturation','nomenclature','convention','accord'],
 a:['La facturation à l’INAMI et aux mutualités produit des données bien structurées sur les prestations <b>remboursées</b>. En 2025, l’INAMI a remboursé environ 1,6 milliard d’euros de soins dentaires, soit plus de 50 % de plus qu’en 2021, alors que le nombre de traitements n’a augmenté que de 16 %.','Ce qui manque : le dossier complet et les soins non remboursés, qui restent dans le logiciel de chaque cabinet. Dental Data rend cette partie visible sans la centraliser, en complément de l’INAMI et non en concurrence.'],s:['hda','marche']},
{id:'hda',q:'Quel est le rôle de la Health Data Agency ?',k:['health data agency','hda','eeds','ehds','organisme','2027','2029','2031','loi','réglement','article 50','micro'],
 a:['La Health Data Agency a été créée par la loi du 14 mars 2023 et lancée le 17 janvier 2024. Elle gère un catalogue national de plus de 480 jeux de données et devrait devenir l’<b>organisme coordinateur responsable de l’accès aux données de santé</b> pour l’EEDS ; cette désignation attend encore une approbation interministérielle.','Dates clés : d’ici le <b>26 mars 2027</b>, les organismes d’accès sont désignés ; à partir du <b>26 mars 2029</b>, la plupart des règles d’utilisation secondaire s’appliquent ; à partir de <b>2031</b>, les images médicales s’y ajoutent. L’article 50 exempte par défaut les microentreprises, comme la plupart des cabinets. Un canal agrégé est donc nécessaire, ce que la HDA envisage elle-même avec des intermédiaires et des détenteurs de données de confiance.'],s:['inami','collaborer']},
{id:'ia',q:'Comment fonctionne l’IA sur les radiographies ?',k:[' ia ','intelligence artificielle','radio','image','carie','parodont','algorithme','modèle','fédéré'],
 a:['Grâce à l’apprentissage fédéré et à l’informatique confidentielle : <b>l’algorithme va vers la donnée</b>, et non l’inverse. Aucune radiographie ne quitte le cabinet.','Notre modèle de caries interproximales et de perte osseuse parodontale est en phase de validation clinique. Il aide le professionnel sans remplacer son diagnostic.'],s:['datos','tecnologia']},
{id:'collaborer',q:'Comment pouvons-nous collaborer ?',k:['collabor','partenaire','alliance','particip','rejoindre','intégrateur','association','chaîne','contact','pilote'],
 a:['En Belgique, nous recherchons une <b>alliance institutionnelle</b> : avec la Health Data Agency, l’INAMI et les mutualités, les associations professionnelles bilingues, les chaînes dentaires et les intégrateurs Azure à Bruxelles et en Wallonie. Il n’y a pas encore de pilote en Belgique.','Software in a Box dispose d’un bureau à Bruxelles, dans le quartier européen. Laissez vos coordonnées dans le <a href="#contacto" data-close>formulaire de contact</a> ou écrivez à <a href="mailto:partners@softwareinabox.eu">partners@softwareinabox.eu</a>.'],s:['inami','hda']},
{id:'marche',q:'À quoi ressemble le marché dentaire belge ?',k:['marché','belgique','dentistes','nombre','chaîne','consolidation','conseil','chiffres'],
 a:['En 2023, la Belgique comptait <b>8 479</b> dentistes en activité, soit 71,7 pour 100 000 habitants. L’assurance maladie obligatoire couvre 99 % des résidents et 60,48 % des dentistes ont adhéré à l’accord dento-mutualiste 2026-2027.','La consolidation est plus récente qu’en Espagne ou aux Pays-Bas, mais elle est à l’agenda : le Conseil de l’Art dentaire a rendu en novembre 2025 un avis sur les chaînes dentaires commerciales. La dernière collecte nationale de données de santé bucco-dentaire date de 2012-2014.'],s:['inami','collaborer']},
{id:'tecnologia',q:'Quelle technologie utilisez-vous ? Quel est le rôle de Microsoft ?',k:['technolog','microsoft','azure','connecteur','standard','gaia','idsa','eclipse','edc','fhir','dicom','ehealth','intégr'],
 a:['Un connecteur sur <b>Microsoft Azure</b>, avec des données dans l’UE, intégré au logiciel de gestion du cabinet.','Les frontières de l’espace utilisent des standards ouverts européens : Gaia-X, IDSA et le Dataspace Protocol, Eclipse EDC, FHIR, DICOM et HealthDCAT-AP. Chacun peut ainsi se connecter, même sans Microsoft.'],s:['collaborer','datos']},
{id:'seguridad',q:'Est-ce conforme au RGPD ? Est-ce sûr ?',k:['rgpd','gdpr','protection des données','vie privée','sécurité','sûr','consentement','juridique','confidenti'],
 a:['Les données identifiables ne sont jamais centralisées : seuls des résultats agrégés circulent, sous contrat. Pour l’IA, nous utilisons l’informatique confidentielle.','Chaque projet est documenté avec le délégué à la protection des données de l’organisation et une analyse d’impact relative à la protection des données.'],s:['datos','hda']},
{id:'publicidad',q:'Les données serviront-elles à la publicité ?',k:['publicit','marketing','vendre','vente','commercial'],
 a:['Jamais. L’EEDS interdit expressément l’utilisation des données de santé à des fins publicitaires.','Les usages prévus sont la qualité des soins, l’IA sur les images et des preuves pour l’industrie sur les implants et les matériaux.'],s:['datos','hda']},
{id:'experiencia',q:'Qui êtes-vous et quelle est votre expérience ?',k:['qui','entreprise','expérience','software in a box','référence','projets','global data care','bruxelles'],
 a:['Software in a Box, avec des bureaux à Madrid et à Bruxelles. Entre 2024 et 2026, nous avons conçu et réalisé trois démonstrateurs d’espaces de données financés par le secrétariat d’État espagnol à la Numérisation et à l’IA : <b>Global Data Care</b> (santé), <b>PROCUREDATA</b> (achats) et <b>EcoDataNet</b> (économie circulaire).','Plus d’informations sur <a href="https://datos.softwareinabox.eu/fr-be/">datos.softwareinabox.eu</a>.'],s:['tecnologia','collaborer']},
{id:'documentos',q:'Où puis-je lire l’étude ?',k:['étude','document','pdf','télécharg','rapport','présentation','vidéo','lire'],
 a:['L’étude comparative de cinq marchés, avec un chapitre consacré à la Belgique, est disponible en <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">anglais</a> et en <a href="/docs/tandheelkundige-gezondheidsdataruimtes-europa-ehds.pdf" target="_blank" rel="noopener" lang="nl">néerlandais</a>, avec la présentation et la vidéo complète.'],s:['marche','collaborer']}
]'''

BLOQUES = {
"espana": r'''
<section class="s soft" id="marche"><div class="wrap">
 <div class="head"><div class="eyebrow">Le marché belge</div><h2>Ce qui est remboursé est visible. Le reste est au cabinet.</h2><p>La Belgique suit un modèle de payeur : les données dentaires les mieux structurées naissent de la facturation aux mutualités et à l’INAMI. Précieuses pour la politique de remboursement, elles ne contiennent ni le dossier complet ni les soins non remboursés.</p></div>
 <div class="grid4">
  <div class="card"><div class="num">DENTISTES</div><h3 class="big">8 479</h3><p>en activité en 2023, soit 71,7 pour 100 000 habitants. S’y ajoutent 514 orthodontistes, 205 parodontologues et 452 hygiénistes bucco-dentaires.</p></div>
  <div class="card"><div class="num">REMBOURSEMENT INAMI</div><h3 class="big">1,6 Md€</h3><p>remboursés pour les soins dentaires en 2025, contre un peu plus d’un milliard en 2021 : +50 % pour 16 % de traitements en plus.</p></div>
  <div class="card"><div class="num">ACCORD 2026-2027</div><h3 class="big">60,48 %</h3><p>des dentistes ont adhéré totalement ou partiellement à l’accord dento-mutualiste.</p></div>
  <div class="card"><div class="num">SANTÉ BUCCO-DENTAIRE</div><h3 class="big">2012-2014</h3><p>dernière collecte nationale de données de santé bucco-dentaire. Depuis, il existe une lacune épidémiologique.</p></div>
 </div>
 <div class="grid2" style="margin-top:22px">
  <div class="card"><h3>La Health Data Agency veut atteindre les prestataires indépendants</h3><p>La HDA (loi du 14/03/2023, lancée le 17/01/2024) gère un catalogue de plus de 480 jeux de données et devrait devenir l’organisme coordinateur pour l’EEDS. Elle reconnaît devoir encore ouvrir le dialogue avec les prestataires indépendants et les petites organisations, et explore des intermédiaires et des détenteurs de données de confiance.</p></div>
  <div class="card"><h3>Les chaînes sous le regard du régulateur professionnel</h3><p>La consolidation est plus récente qu’en Espagne ou aux Pays-Bas, mais le Conseil de l’Art dentaire a rendu en novembre 2025 un avis sur les chaînes commerciales. La transparence sur les résultats répond à ce débat. La plateforme fédérale eHealth et le plan d’action interfédéral 2026-2029 en constituent la base numérique.</p></div>
 </div>
 <p class="pcap">Source : Software in a Box, <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">Dental health data spaces in Europe · Étude comparative</a> (novembre 2026), et les sources qui y sont citées (INAMI, Council of European Dentists, Health Data Agency).</p>
</div></section>
''',
"para-quien": r'''
<section class="s soft" id="para-quien"><div class="wrap">
 <div class="head"><div class="eyebrow">Pour qui</div><h2>Un complément à l’INAMI, pas un concurrent</h2><p>L’espace de données fédéré complète ce qui reste aujourd’hui hors champ : les soins non remboursés et le dossier complet, dans le logiciel de chaque cabinet. Pour cela, nous recherchons une alliance institutionnelle, dans laquelle les cabinets restent propriétaires de leurs données.</p></div>
 <div class="grid4 who-grid">
  <div class="card"><div class="num">INSTITUTIONS</div><h3>Health Data Agency et INAMI</h3><p>Un canal agrégé vers les prestataires indépendants, en tant qu’intermédiaire ou détenteur de données de confiance.</p></div>
  <div class="card"><div class="num">MUTUALITÉS</div><h3>Des preuves sur les dépenses</h3><p>Comprendre pourquoi les remboursements augmentent plus vite que le nombre de traitements, par patient et par type de soins.</p></div>
  <div class="card"><div class="num">ASSOCIATIONS PROFESSIONNELLES</div><h3>Une charge administrative faible</h3><p>Les cabinets indépendants participent via leur association, sans devenir eux-mêmes détenteurs de données.</p></div>
  <div class="card"><div class="num">CHAÎNES ET INTÉGRATEURS</div><h3>Comparer et déployer</h3><p>Des indicateurs de qualité entre cabinets pour les chaînes ; des intégrateurs Azure à Bruxelles et en Wallonie déploient le connecteur.</p></div>
 </div>
 <div class="head" style="margin-top:56px;margin-bottom:22px"><h2 style="font-size:28px">Feuille de route</h2></div>
 <div class="flow">
  <div class="step"><div class="c">1</div><b>2027 · Dialogue</b><span>Échanges avec la Health Data Agency, l’INAMI et les associations professionnelles ; premiers pilotes en Espagne et aux Pays-Bas.</span></div>
  <div class="step"><div class="c">2</div><b>2027–2028 · Projet commun</b><span>Un projet avec la HDA et un groupe de cabinets ou une chaîne, déployé par un intégrateur Azure local.</span></div>
  <div class="step"><div class="c">3</div><b>Mars 2029 · Catalogué</b><span>Un espace de données dentaires catalogué, prêt pour les demandes d’accès au titre de l’EEDS.</span></div>
 </div>
 <div class="nl-band"><div><b>Aussi aux Pays-Bas et en Espagne</b><p>Nous construisons un seul produit pour toute l’Europe : aux Pays-Bas avec un partenaire technologique local, en Espagne avec un pilote auprès d’une chaîne ou d’un assureur.</p></div><a href="/nl/" lang="nl" hreflang="nl-NL">Nederland →</a>&nbsp;&nbsp;<a href="/es/" lang="es" hreflang="es-ES">España →</a></div>
</div></section>
''',
"contacto": r'''
<section class="s cta" id="contacto"><div class="wrap">
 <h2>Vous souhaitez en parler avec nous ?</h2>
 <p>Dites-nous brièvement qui vous êtes. Nous vous proposerons un rendez-vous à notre bureau de Bruxelles ou en ligne, pour voir comment Dental Data s’inscrit dans votre organisation.</p>
 <form class="cform" action="https://formsubmit.co/partners@softwareinabox.eu" method="POST">
  <input type="hidden" name="_subject" value="Dental Data · Belgique [FR]">
  <input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="https://www.softwareinabox.eu/gracias.html">
  <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
  <label class="sr" for="f-n">Nom</label><input id="f-n" name="Nom" required placeholder="Prénom et nom" autocomplete="name">
  <label class="sr" for="f-o">Organisation</label><input id="f-o" name="Organisation" placeholder="Organisation" autocomplete="organization">
  <label class="sr" for="f-p">Profil</label><select id="f-p" class="full" name="Profil"><option value="">Profil de votre organisation</option><option>Institution ou administration</option><option>Mutualité ou assureur</option><option>Association professionnelle</option><option>Chaîne dentaire ou cabinet de groupe</option><option>Cabinet indépendant</option><option>Éditeur de logiciel ou partenaire Microsoft</option><option>Autre</option></select>
  <label class="sr" for="f-e">E-mail</label><input id="f-e" class="full" type="email" name="E-mail" required placeholder="Adresse e-mail professionnelle" autocomplete="email">
  <label class="sr" for="f-m">Message</label><textarea id="f-m" name="Message" placeholder="De quoi souhaitez-vous nous parler ?"></textarea>
  <label class="ok full"><input type="checkbox" name="Consentement" value="Accepte la politique de confidentialité" required><span>J’ai lu et j’accepte la <a href="https://www.softwareinabox.eu/fr-be/privacidad.html" target="_blank" rel="noopener">politique de confidentialité</a>. Nous n’utiliserons vos données que pour vous répondre.</span></label>
  <button type="submit">Envoyer</button>
 </form>
 <p style="font-size:15px;margin-top:18px">Ou écrivez à <a href="mailto:partners@softwareinabox.eu" style="color:#fff;font-weight:600">partners@softwareinabox.eu</a> · <a href="tel:+34601398868" style="color:#fff;font-weight:600">+34 601 398 868</a> · Bruxelles et Madrid</p>
</div></section>
''',
}

TEXTOS = {
"m000": "<title>Dental Data Belgique · Espace de données dentaires fédéré pour l’EEDS | Software in a Box</title>",
"m001": 'content="Dental Data est un espace de données dentaires fédéré sur Microsoft Azure : rendre visibles le dossier complet et les soins non remboursés sans centraliser les données. Un complément à l’INAMI pour l’EEDS."',
"m002": '<link rel="canonical" href="https://dentaldata.softwareinabox.eu/fr-be/">',
"m003": 'content="fr_BE"',
"m004": '<meta property="og:title" content="Dental Data Belgique · Votre espace de données dentaires commence ici">',
"m005": 'content="L’INAMI voit ce qui est remboursé. Dental Data rend visible le reste du dossier dentaire, sans déplacer un seul dossier."',
"m006": '<meta property="og:url" content="https://dentaldata.softwareinabox.eu/fr-be/">',
"m007": '<a class="brand" href="/fr-be/" aria-label="Dental Data Belgique, accueil">',
"m015": '<ul id="m2"><li><a href="#para-quien">Institutions</a></li><li><a href="#para-quien">Mutualités</a></li><li><a href="#para-quien">Associations professionnelles</a></li><li><a href="#para-quien">Chaînes et intégrateurs</a></li></ul>',
"m017": '<li><a href="#destacados">Étude, présentation et vidéos</a></li><li><a href="#marche">Le marché belge</a></li><li><a href="#preguntas">Questions fréquentes</a></li><li><a href="https://datos.softwareinabox.eu/fr-be/">Nos espaces de données</a></li>',
"m018": '<a class="tbtn white" href="#contacto">Parlons-en</a>\n  <button',
"m021": '<li><a href="/es/" hreflang="es-ES" lang="es">Español · España</a></li>',
"m027": '<a href="#solucion">Solution</a><a href="#para-quien">Pour qui</a><a href="#destacados">Ressources</a><a href="#preguntas">Questions fréquentes</a><a href="#contacto">Parlons-en</a>',
"m028": '<div class="pre">Belgique · Espace européen des données de santé</div>',
"m029": '<h1 id="h1">Votre espace de données dentaires <em>commence ici</em></h1>',
"m030": '<p class="lead">Ce que l’INAMI rembourse est déjà visible. Demandez comment faire apparaître le reste du dossier sans qu’un seul dossier quitte le cabinet.</p>',
"m034": '<button class="chip" type="button" data-q="datos">Mes données quittent-elles le cabinet ?</button>',
"m035": '<button class="chip" type="button" data-q="inami">Qu’apporte-t-il à l’INAMI ?</button>',
"m036": '<button class="chip" type="button" data-q="hda">Quel rôle pour la Health Data Agency ?</button>',
"m037": '<button class="chip" type="button" data-q="ia">Comment fonctionne l’IA sur les radiographies ?</button>',
"m038": '<button class="chip" type="button" data-q="collaborer">Comment collaborer ?</button>',
"m039": '<p class="trust">Expérience dans <b>3 espaces de données</b> financés par des fonds publics · Bureau à <b>Bruxelles</b> · Connecteur sur <b>Microsoft Azure</b> avec données dans l’UE</p>',
"m040": '<h2>Rendre visible la moitié invisible des soins dentaires</h2>',
"m041": '<p>Nous recherchons des partenaires pour une alliance institutionnelle : la Health Data Agency, l’INAMI et les mutualités, les associations professionnelles, les chaînes et les intégrateurs Azure.</p>',
"m042": '<a class="tbtn white" href="#contacto">Parlons-en</a><button class="tbtn outline" type="button" data-open-assistant>Interroger l’assistant</button>',
"m043": '<div class="cap">Ce que l’alliance apporte</div>',
"m044": '<b>Le dossier complet, pas seulement la facture</b><span>Y compris les soins non remboursés, sans centraliser les données.</span>',
"m045": '<b>Des données actuelles de santé bucco-dentaire</b><span>Aucune collecte nationale n’a eu lieu depuis 2014.</span>',
"m046": '<b>Peu de charge pour les cabinets indépendants</b><span>Un canal agrégé unique vers la Health Data Agency.</span>',
"m047": '<b>De la transparence pour les chaînes</b><span>Des indicateurs de qualité comparables entre cabinets.</span>',
"m088": '<a class="flogo" href="/fr-be/" aria-label="Dental Data Belgique, accueil">',
"m090": '<div><h4>Pays</h4><a href="/nl-be/" lang="nl">België (Nederlands)</a><a href="/nl/" lang="nl">Nederland</a><a href="/de/" lang="de">Deutschland</a><a href="/">Tous les pays</a></div>',
"m094": '<div><h4>Contact</h4><a href="#contacto">Parlons-en</a>',
"m095": '<a href="/en/" lang="en">Dental Data Europe</a></div>',
"m096": 'stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.8 2.5 15.2 0 18M12 3c-2.5 2.8-2.5 15.2 0 18"/></svg>Français (Belgique)</span>',
"m109": "bot(['Bonjour ! Je suis l’assistant de Dental Data. Je vous explique comment fonctionne l’espace de données dentaires fédéré, ce qu’il apporte aux données de l’INAMI et ce que l’Espace européen des données de santé signifie pour les soins dentaires en Belgique.','Choisissez une question ou écrivez la vôtre. Merci de ne pas saisir de données personnelles ni de données de patients : nous conservons les questions et les réponses de manière anonyme pour améliorer l’assistant.'],['datos','inami','hda','ia','collaborer'],true)",
"m115": "['datos','hda','collaborer','tecnologia']",
"m116": "idioma:'fr',pais:'be'",
"m118": "var FUENTES={'01-que-es-dental-data.md':'Ce qu’est Dental Data','03-solucion-casos-uso.md':'Solution et cas d’usage','05-tecnologia.md':'Technologie','08-empresa-recursos.md':'Software in a Box','10-estudio-comparativo-en.md':'Étude comparative (PDF)','11-ehds-europa.md':'L’EEDS en Europe','pais/be.md':'Dental Data en Belgique'}",
}

REEMPLAZOS = desde_claves(TEXTOS) + [
('<li><a href="/fr-be/" hreflang="fr-BE" lang="fr">Français · Belgique</a></li>', '<li><a href="/fr-be/" hreflang="fr-BE" lang="fr" aria-current="page">Français · Belgique</a></li>'),
]

PRES = "fr-be"
VIDEOS_LANG = "fr"
