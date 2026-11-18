# Dental Data France · https://dentaldata.softwareinabox.eu/fr/
# Marché «fr» : complémentaires et réseaux de centres de santé dentaires ; nœud sur Azure (région UE) ou chez un hébergeur souverain.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "idiomas"))
from _mercado import desde_claves

SALIDA = "fr/index.html"
LANG = "fr-FR"
IDIOMA_COMUN = "fr"
SIAB = "fr"
PERMITIDO = ['lang="es"', "Español", "España"]
PRES = "fr"
VIDEOS_LANG = "fr"

JSONLD = r'''
{"@context":"https://schema.org","@graph":[
{"@type":"WebPage","@id":"https://dentaldata.softwareinabox.eu/fr/#webpage","url":"https://dentaldata.softwareinabox.eu/fr/","name":"Dental Data France · Espace de données dentaires fédéré","inLanguage":"fr-FR","isPartOf":{"@type":"WebSite","@id":"https://www.softwareinabox.eu/#website","name":"Software in a Box"},"publisher":{"@type":"Organization","@id":"https://www.softwareinabox.eu/#org","name":"Software in a Box","url":"https://www.softwareinabox.eu/"}},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Les données sont-elles hébergées chez Microsoft ?","acceptedAnswer":{"@type":"Answer","text":"Le nœud peut fonctionner sur Microsoft Azure dans l’Union européenne ou chez un hébergeur souverain certifié pour les données de santé. Dans les deux cas, les dossiers ne quittent pas le cabinet : seuls des résultats agrégés circulent."}},
{"@type":"Question","name":"Qu’apporte Dental Data aux complémentaires ?","acceptedAnswer":{"@type":"Answer","text":"Des résultats cliniques mesurés dans les cabinets de leurs réseaux, sans centraliser les dossiers : de quoi évaluer le 100 % santé et la qualité des réseaux, avec l’interdiction stricte d’utiliser ces données pour la publicité ou pour fixer des primes."}},
{"@type":"Question","name":"Quel lien avec la Plateforme des données de santé ?","acceptedAnswer":{"@type":"Answer","text":"Dental Data publie un catalogue HealthDCAT-AP compatible. La Plateforme des données de santé est candidate au rôle d’organisme d’accès ; la décision n’est pas encore prise (novembre 2026)."}}
]}]}
'''

KB_JS = r'''[
{id:'datos',q:'Mes données quittent-elles le cabinet ?',k:['quitter','quittent','déplac','central','stock','où sont','serveur','copie','partag'],
 a:['Non. Les dossiers restent dans le logiciel de gestion de chaque cabinet, centre de santé ou réseau. Dental Data est un espace de données <b>fédéré</b> : seuls les consentements, les métadonnées et les résultats agrégés circulent.','Chaque accès est régi par un contrat ODRL que la machine fait respecter : le cabinet décide qui accède, dans quel but et pour combien de temps. Pas de contrat, pas d’accès.'],s:['hebergement','seguridad']},
{id:'hebergement',q:'Où sont hébergées les données ?',k:['héberg','hds','secnumcloud','souverain','microsoft','azure','cloud','cnil'],
 a:['Deux options pour le nœud : <b>Microsoft Azure dans l’Union européenne</b>, ou un <b>hébergeur souverain</b> certifié pour les données de santé et qualifié de cloud de confiance.','Le choix de l’hébergement ne change rien aux règles : les données ne quittent pas le cabinet, et le connecteur Eclipse EDC, le catalogue HealthDCAT-AP et les contrats ODRL restent les mêmes. Dental Data n’héberge pas de dossiers centralisés.'],s:['datos','tecnologia']},
{id:'complementaires',q:'Qu’apporte Dental Data aux complémentaires ?',k:['complémentaire','mutuelle','prévoyance','assureur','100 %','100%','panier','réseau de soins','prime'],
 a:['Les complémentaires sont le premier financeur des soins dentaires et paient les prothèses du panier <b>100 % santé</b>, sans savoir si ces traitements durent ni quel résultat ils obtiennent.','Dental Data leur donne des résultats cliniques mesurés dans les cabinets de leurs réseaux, sans centraliser les dossiers. L’EEDS interdit d’utiliser ces données pour la publicité ou pour des décisions qui nuisent aux personnes, y compris pour fixer des primes.'],s:['centres','datos']},
{id:'centres',q:'Et pour les centres de santé dentaires ?',k:['centre','agrément','ars','dentexia','proxidentaire','réseau','chaîne','qualité'],
 a:['Depuis la loi du 19 mai 2023, les centres dentaires doivent obtenir un <b>agrément préalable de l’ARS</b>, qui peut le refuser ou sanctionner. Démontrer sa qualité est devenu une condition pour rester ouvert.','Avec Dental Data, un connecteur à côté de chaque logiciel calcule les indicateurs dans chaque centre, avec la même définition et des actes codés en CCAM. La direction voit des résultats comparables de tout le réseau, sans transmettre un seul dossier.'],s:['complementaires','collaborer']},
{id:'ehds',q:'Quel calendrier pour l’EEDS en France ?',k:['eeds','ehds','2027','2029','2031','plateforme','health data hub','pds','organisme','article 50','micro'],
 a:['Dates clés : d’ici le <b>26 mars 2027</b>, chaque État désigne ses organismes d’accès ; à partir du <b>26 mars 2029</b>, la plupart des règles d’utilisation secondaire s’appliquent ; en <b>2031</b>, les images médicales entrent dans l’espace.','En France, la <b>Plateforme des données de santé</b> est candidate au rôle d’organisme d’accès, mais la décision n’est pas prise. Elle migre vers un hébergement souverain entre fin 2026 et 2027. La plupart des cabinets sont des microentreprises, exemptées par défaut : il faut un canal agrégé.'],s:['hebergement','collaborer']},
{id:'ia',q:'Comment fonctionne l’IA sur les radiographies ?',k:[' ia ','intelligence artificielle','radio','image','carie','parodont','algorithme','modèle','cone beam'],
 a:['Grâce à l’apprentissage fédéré et au calcul confidentiel : <b>l’algorithme va vers la donnée</b>, et non l’inverse. Aucune radiographie ne quitte le cabinet.','Notre modèle de caries interproximales et de perte osseuse parodontale est en phase de validation clinique. Il aide le professionnel sans remplacer son diagnostic.'],s:['datos','tecnologia']},
{id:'tecnologia',q:'Quelle technologie utilisez-vous ?',k:['technolog','connecteur','standard','gaia','idsa','eclipse','edc','fhir','dicom','snomed','ccam','ségur','logiciel'],
 a:['Un connecteur intégré au logiciel de gestion du cabinet, compatible avec les logiciels référencés Ségur. Terminologie <b>SNOMED CT</b> (édition nationale de l’ANS) et actes codés en <b>CCAM</b>.','Aux frontières de l’espace, des standards ouverts européens : Gaia-X, IDSA et le Dataspace Protocol, Eclipse EDC, FHIR, DICOM et HealthDCAT-AP. Chacun peut se connecter, même sans Microsoft.'],s:['hebergement','collaborer']},
{id:'seguridad',q:'Est-ce conforme au RGPD ?',k:['rgpd','gdpr','informatique et libertés','cnil','vie privée','sécurité','consentement','juridique'],
 a:['Les données identifiables ne sont jamais centralisées : seuls des résultats agrégés circulent, sous contrat, dans le cadre du RGPD et de la loi Informatique et Libertés.','Chaque projet est documenté avec le délégué à la protection des données de l’organisation et une analyse d’impact. L’hébergement du nœud se fait chez un hébergeur certifié pour les données de santé.'],s:['datos','hebergement']},
{id:'publicidad',q:'Les données serviront-elles à la publicité ?',k:['publicit','marketing','vendre','vente','commercial'],
 a:['Jamais. L’EEDS interdit expressément l’utilisation des données de santé à des fins publicitaires, et le code de déontologie encadre déjà la communication des chirurgiens-dentistes.','Les usages prévus sont la qualité des soins, l’IA sur les images et des preuves pour l’industrie sur les implants et les matériaux.'],s:['datos','complementaires']},
{id:'collaborer',q:'Comment pouvons-nous collaborer ?',k:['collabor','partenaire','particip','rejoindre','projet','pilote','contact','hébergeur'],
 a:['En France, nous recherchons une <b>complémentaire</b> ou un <b>réseau de centres de santé dentaires</b> pour un premier projet d’indicateurs de qualité, ainsi qu’un <b>hébergeur souverain</b> partenaire pour l’option certifiée.','Le cas d’usage finance le connecteur. Laissez vos coordonnées dans le formulaire et nous vous proposerons un échange.'],s:['complementaires','centres']},
{id:'experiencia',q:'Qui êtes-vous et quelle est votre expérience ?',k:['qui','entreprise','expérience','software in a box','référence','projets','global data care'],
 a:['Software in a Box, avec des bureaux à Madrid et à Bruxelles. Entre 2024 et 2026, nous avons conçu et réalisé trois démonstrateurs d’espaces de données financés par le secrétariat d’État espagnol à la Numérisation et à l’IA : <b>Global Data Care</b> (santé), <b>PROCUREDATA</b> (achats) et <b>EcoDataNet</b> (économie circulaire).','Plus d’informations sur <a href="https://datos.softwareinabox.eu/fr/" target="_blank" rel="noopener">nos espaces de données</a>.'],s:['tecnologia','collaborer']},
{id:'documentos',q:'Où puis-je lire l’étude ?',k:['étude','document','pdf','télécharg','rapport','présentation','vidéo','lire'],
 a:['L’étude comparative européenne est disponible en <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">anglais</a>, avec la présentation et la vidéo complète. Les présentations animées de cette page résument chaque question en moins d’une minute.'],s:['datos','ehds']}
]'''

BLOQUES = {
"espana": r'''
<section class="s soft" id="marche"><div class="wrap">
 <div class="head"><div class="eyebrow">Le marché français</div><h2>Le 100 % santé a changé qui paie. Il reste à mesurer ce que l’on obtient.</h2><p>Les soins dentaires sont financés par l’Assurance maladie et surtout par les complémentaires. Le Système national des données de santé sait ce qui est remboursé, mais pas ce qui a été trouvé en bouche ni le résultat du traitement : ces données restent dans chaque cabinet et chaque centre, dans leur propre logiciel.</p></div>
 <div class="grid4">
  <div class="card"><div class="num">CHIRURGIENS-DENTISTES</div><h3 class="big">47 636</h3><p>chirurgiens-dentistes au 1er janvier 2025 (DREES).</p></div>
  <div class="card"><div class="num">DÉPENSE EN CABINET</div><h3 class="big">13,2 Md€</h3><p>de soins dentaires en cabinet libéral en 2024 (DREES, comptes de la santé).</p></div>
  <div class="card"><div class="num">100 % SANTÉ</div><h3 class="big">0 €</h3><p>de reste à charge sur les prothèses du panier 100 % santé, depuis la réforme de 2019-2020.</p></div>
  <div class="card"><div class="num">CENTRES DE SANTÉ</div><h3 class="big">2 055</h3><p>centres de santé (dentaire, ophtalmologie, orthoptie) soumis au nouvel agrément.</p></div>
 </div>
 <div class="grid2" style="margin-top:22px">
  <div class="card"><h3>Après Dentexia et Proxidentaire</h3><p>La loi du 19 mai 2023 rétablit l’agrément préalable de l’agence régionale de santé pour les centres dentaires, avec des amendes pouvant atteindre 500 000 €. Démontrer sa qualité devient une condition pour rester ouvert.</p></div>
  <div class="card"><h3>Les complémentaires, premier financeur</h3><p>Le reste à charge des ménages en dentaire est passé de 18,8 % en 2019 à 15,8 % en 2021. Mais 2,5 millions de personnes sans complémentaire restent en dehors du 100 % santé, et personne ne mesure les résultats cliniques des soins payés.</p></div>
 </div>
 <p class="pcap">Source : Software in a Box, <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">Dental health data spaces in Europe · Étude comparative</a> (novembre 2026), chapitre France, et les sources qui y sont citées (DREES, ministère de la Santé, Plateforme des données de santé). Données à novembre 2026.</p>
</div></section>
''',
"para-quien": r'''
<section class="s soft" id="para-quien"><div class="wrap">
 <div class="head"><div class="eyebrow">Pour qui</div><h2>Ce qui manque au DMP, à Mon espace santé et au SNDS : la donnée clinique dentaire</h2><p>Dental Data ne remplace ni le DMP, ni Mon espace santé, ni le SNDS. Il apporte la donnée clinique dentaire, avec un catalogue HealthDCAT-AP compatible avec la Plateforme des données de santé, et un nœud hébergé sur Azure en Europe ou chez un hébergeur souverain.</p></div>
 <div class="grid4 who-grid">
  <div class="card"><div class="num">COMPLÉMENTAIRES</div><h3>Évaluer le 100 % santé</h3><p>Des résultats cliniques mesurés dans les cabinets des réseaux de soins, sans centraliser les dossiers.</p></div>
  <div class="card"><div class="num">CENTRES DE SANTÉ</div><h3>Démontrer la qualité</h3><p>Des indicateurs comparables entre centres, présentables à l’ARS et à l’Assurance maladie.</p></div>
  <div class="card"><div class="num">ASSURANCE MALADIE ET ARS</div><h3>Mesurer la prévention</h3><p>M’T dents, génération sans carie et usage du cone beam : des indicateurs calculés au cabinet.</p></div>
  <div class="card"><div class="num">ÉDITEURS ET DSI</div><h3>Un connecteur de plus</h3><p>À côté des logiciels référencés Ségur, avec SNOMED CT et la CCAM.</p></div>
 </div>
 <div class="head" style="margin-top:56px;margin-bottom:22px"><h2 style="font-size:28px">Feuille de route</h2></div>
 <div class="flow">
  <div class="step"><div class="c">1</div><b>2027 · Premiers nœuds</b><span>Un premier projet d’indicateurs avec une complémentaire ou un réseau de centres, hébergé au choix sur Azure ou chez un hébergeur souverain.</span></div>
  <div class="step"><div class="c">2</div><b>2027–2028 · Consolidation</b><span>Consolidation des projets et participation aux consultations ; migration de la Plateforme des données de santé vers un hébergement souverain.</span></div>
  <div class="step"><div class="c">3</div><b>Mars 2029 · Catalogué</b><span>Des jeux de données catalogués et prêts pour l’EEDS. La Plateforme est candidate au rôle d’organisme d’accès ; sa désignation dépend d’une décision politique.</span></div>
 </div>
 <div class="nl-band"><div><b>Aussi en Belgique et ailleurs en Europe</b><p>Un seul produit pour toute l’Europe, adapté à la langue, aux données et au droit de chaque pays.</p></div><a href="/fr-be/" lang="fr" hreflang="fr-BE">Belgique →</a>&nbsp;&nbsp;<a href="/en/" lang="en" hreflang="en">Europe →</a></div>
</div></section>
''',
"contacto": r'''
<section class="s cta" id="contacto"><div class="wrap">
 <h2>Premiers partenaires en France</h2>
 <p>Complémentaires, réseaux de centres de santé dentaires, hébergeurs souverains et éditeurs : dites-nous brièvement qui vous êtes et nous vous proposerons un échange, en ligne ou à Bruxelles.</p>
 <form class="cform" action="https://formsubmit.co/partners@softwareinabox.eu" method="POST">
  <input type="hidden" name="_subject" value="Dental Data · France">
  <input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="https://www.softwareinabox.eu/gracias.html">
  <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
  <label class="sr" for="f-n">Nom</label><input id="f-n" name="Nom" required placeholder="Prénom et nom" autocomplete="name">
  <label class="sr" for="f-o">Organisation</label><input id="f-o" name="Organisation" placeholder="Organisation" autocomplete="organization">
  <label class="sr" for="f-p">Profil</label><select id="f-p" class="full" name="Profil"><option value="">Profil de votre organisation</option><option>Complémentaire (mutuelle, institution de prévoyance, assureur)</option><option>Réseau de centres de santé dentaires</option><option>Cabinet dentaire</option><option>Institution ou administration</option><option>Hébergeur de données de santé</option><option>Éditeur de logiciel ou partenaire Microsoft</option><option>Autre</option></select>
  <label class="sr" for="f-e">E-mail</label><input id="f-e" class="full" type="email" name="E-mail" required placeholder="Adresse e-mail professionnelle" autocomplete="email">
  <label class="sr" for="f-m">Message</label><textarea id="f-m" name="Message" placeholder="De quoi souhaitez-vous nous parler ?"></textarea>
  <label class="ok full"><input type="checkbox" name="Consentement" value="Accepte la politique de confidentialité" required><span>J’ai lu et j’accepte la <a href="https://www.softwareinabox.eu/fr/privacidad.html" target="_blank" rel="noopener">politique de confidentialité</a>. Nous n’utiliserons vos données que pour vous répondre.</span></label>
  <button type="submit">Envoyer</button>
 </form>
 <p style="font-size:15px;margin-top:18px">Ou écrivez à <a href="mailto:partners@softwareinabox.eu" style="color:#fff;font-weight:600">partners@softwareinabox.eu</a> · <a href="tel:+34601398868" style="color:#fff;font-weight:600">+34 601 398 868</a> · Bruxelles et Madrid</p>
</div></section>
''',
}

TEXTOS = {
"m000": "<title>Dental Data France · Espace de données dentaires fédéré pour l’EEDS | Software in a Box</title>",
"m001": 'content="Dental Data est un espace de données dentaires fédéré : mesurer la qualité des soins dentaires sans déplacer un seul dossier. Nœud sur Microsoft Azure en Europe ou chez un hébergeur souverain. Pour les complémentaires et les centres de santé."',
"m002": '<link rel="canonical" href="https://dentaldata.softwareinabox.eu/fr/">',
"m003": 'content="fr_FR"',
"m004": '<meta property="og:title" content="Dental Data France · Mesurer la qualité des soins dentaires sans déplacer un seul dossier">',
"m005": 'content="Les indicateurs sont calculés au cabinet, seul le résultat circule. Hébergement en Europe, avec une option souveraine."',
"m006": '<meta property="og:url" content="https://dentaldata.softwareinabox.eu/fr/">',
"m007": '<a class="brand" href="/fr/" aria-label="Dental Data France, accueil">',
"m015": '<ul id="m2"><li><a href="#para-quien">Complémentaires</a></li><li><a href="#para-quien">Centres de santé et réseaux</a></li><li><a href="#para-quien">Assurance maladie et ARS</a></li><li><a href="#para-quien">Éditeurs et DSI</a></li></ul>',
"m017": '<li><a href="#destacados">Étude, présentation et vidéos</a></li><li><a href="#marche">Le marché français</a></li><li><a href="#preguntas">Questions fréquentes</a></li><li><a href="https://datos.softwareinabox.eu/fr/">Nos espaces de données</a></li>',
"m018": '<a class="tbtn white" href="#contacto">Nous contacter</a>\n  <button',
"m021": '<li><a href="/es/" hreflang="es-ES" lang="es">Español · España</a></li>',
"m027": '<a href="#solucion">Solution</a><a href="#para-quien">Pour qui</a><a href="#destacados">Ressources</a><a href="#preguntas">Questions fréquentes</a><a href="#contacto">Nous contacter</a>',
"m028": '<div class="pre">France · Espace européen des données de santé</div>',
"m029": '<h1 id="h1">Mesurer la qualité des soins dentaires <em>sans déplacer un seul dossier</em></h1>',
"m030": '<p class="lead">Dental Data relie cabinets, centres de santé et complémentaires dans un espace de données fédéré : les indicateurs sont calculés au cabinet, seul le résultat circule. Hébergement en Europe, avec une option souveraine.</p>',
"m034": '<button class="chip" type="button" data-q="hebergement">Où sont hébergées les données ?</button>',
"m035": '<button class="chip" type="button" data-q="complementaires">Qu’apporte-t-il aux complémentaires ?</button>',
"m036": '<button class="chip" type="button" data-q="centres">Et pour les centres de santé ?</button>',
"m037": '<button class="chip" type="button" data-q="ehds">Quel calendrier pour l’EEDS ?</button>',
"m038": '<button class="chip" type="button" data-q="collaborer">Comment collaborer ?</button>',
"m039": '<p class="trust">Expérience dans <b>3 espaces de données</b> financés par des fonds publics · Nœud sur <b>Microsoft Azure</b> en Europe ou chez un <b>hébergeur souverain</b></p>',
"m040": '<h2>Mesurer ce que l’on obtient, pas seulement ce que l’on rembourse</h2>',
"m041": '<p>Nous recherchons une complémentaire ou un réseau de centres de santé dentaires pour un premier projet d’indicateurs de qualité, et un hébergeur souverain partenaire.</p>',
"m042": '<a class="tbtn white" href="#contacto">Nous contacter</a><button class="tbtn outline" type="button" data-open-assistant>Interroger l’assistant</button>',
"m043": '<div class="cap">Ce que vous obtenez</div>',
"m044": '<b>Des résultats cliniques, pas seulement des remboursements</b><span>Mesurés au cabinet, sans centraliser les dossiers.</span>',
"m045": '<b>Une qualité démontrable devant l’ARS</b><span>Des indicateurs comparables entre centres d’un même réseau.</span>',
"m046": '<b>Le choix de l’hébergement</b><span>Azure dans l’UE ou hébergeur souverain : les règles ne changent pas.</span>',
"m047": '<b>Prêt pour l’EEDS avant 2029</b><span>Un catalogue HealthDCAT-AP compatible avec la Plateforme des données de santé.</span>',
"m088": '<a class="flogo" href="/fr/" aria-label="Dental Data France, accueil">',
"m090": '<div><h4>Pays</h4><a href="/fr-be/" lang="fr">Belgique</a><a href="/de/" lang="de">Deutschland</a><a href="/it/" lang="it">Italia</a><a href="/">Tous les pays</a></div>',
"m094": '<div><h4>Contact</h4><a href="#contacto">Nous contacter</a>',
"m095": '<a href="/en/" lang="en">Dental Data Europe</a></div>',
"m096": 'stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.8 2.5 15.2 0 18M12 3c-2.5 2.8-2.5 15.2 0 18"/></svg>Français (France)</span>',
"m109": "bot(['Bonjour ! Je suis l’assistant de Dental Data. Je vous explique comment fonctionne l’espace de données dentaires fédéré, où sont hébergées les données et ce que l’Espace européen des données de santé signifie pour les soins dentaires en France.','Choisissez une question ou écrivez la vôtre. Merci de ne pas saisir de données personnelles ni de données de patients : nous conservons les questions et les réponses de manière anonyme pour améliorer l’assistant.'],['hebergement','complementaires','centres','ehds','collaborer'],true)",
"m115": "['datos','hebergement','ehds','collaborer']",
"m116": "idioma:'fr',pais:'fr'",
"m118": "var FUENTES={'01-que-es-dental-data.md':'Ce qu’est Dental Data','03-solucion-casos-uso.md':'Solution et cas d’usage','05-tecnologia.md':'Technologie','08-empresa-recursos.md':'Software in a Box','10-estudio-comparativo-en.md':'Étude comparative (PDF)','11-ehds-europa.md':'L’EEDS en Europe','pais/fr.md':'Dental Data en France'}",
}

REEMPLAZOS = desde_claves(TEXTOS) + [
('<li><a href="/fr/" hreflang="fr-FR" lang="fr">Français · France</a></li>', '<li><a href="/fr/" hreflang="fr-FR" lang="fr" aria-current="page">Français · France</a></li>'),
]
