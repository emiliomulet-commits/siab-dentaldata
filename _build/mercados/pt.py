# Dental Data Portugal · https://dentaldata.softwareinabox.eu/pt/
# Mercado «pt»: seguradoras com rede, redes de clínicas e medição dos programas públicos (cheque-dentista).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "idiomas"))
from _mercado import desde_claves

SALIDA = "pt/index.html"
LANG = "pt-PT"
IDIOMA_COMUN = "pt"
SIAB = "pt"
PERMITIDO = ['lang="es"', "Español", "España"]
PRES = "pt"
VIDEOS_LANG = "pt"

JSONLD = r'''
{"@context":"https://schema.org","@graph":[
{"@type":"WebPage","@id":"https://dentaldata.softwareinabox.eu/pt/#webpage","url":"https://dentaldata.softwareinabox.eu/pt/","name":"Dental Data Portugal · Espaço de dados dentários federado","inLanguage":"pt-PT","isPartOf":{"@type":"WebSite","@id":"https://www.softwareinabox.eu/#website","name":"Software in a Box"},"publisher":{"@type":"Organization","@id":"https://www.softwareinabox.eu/#org","name":"Software in a Box","url":"https://www.softwareinabox.eu/"}},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Os dados saem da clínica?","acceptedAnswer":{"@type":"Answer","text":"Não. As fichas ficam no software de gestão de cada clínica, rede ou seguradora. Só circulam consentimentos, metadados e resultados agregados, segundo contratos de utilização que a máquina faz cumprir."}},
{"@type":"Question","name":"As seguradoras podem usar os dados para fixar prémios?","acceptedAnswer":{"@type":"Answer","text":"Não. O Espaço Europeu de Dados de Saúde proíbe usar dados de saúde para publicidade ou para decisões que prejudiquem as pessoas, também nos seguros."}},
{"@type":"Question","name":"O que muda com o EEDS em Portugal?","acceptedAnswer":{"@type":"Answer","text":"A SPMS coordena a preparação do EEDS (Despacho 3030/2025) e trabalha num registo de saúde eletrónico único. O organismo de acesso ainda não está designado (novembro de 2026)."}}
]}]}
'''

KB_JS = r'''[
{id:'datos',q:'Os dados saem da clínica?',k:['saem','sair','mover','central','onde ficam','servidor','cópia','partilh'],
 a:['Não. As fichas ficam no software de gestão de cada clínica, rede ou seguradora. A Dental Data é um espaço de dados <b>federado</b>: só circulam consentimentos, metadados e resultados agregados.','Cada acesso é regulado por um contrato ODRL que a máquina faz cumprir: a clínica decide quem acede, para quê e durante quanto tempo. Sem contrato, não há acesso.'],s:['seguradora','seguridad']},
{id:'seguradora',q:'O que ganha uma seguradora com rede dentária?',k:['segurador','seguro','plano','rede','convencion','prémio','premio','asf'],
 a:['Os seguros e planos dentários funcionam com redes de clínicas convencionadas, cada uma com o seu software, e os dados de custos e resultados não se podem comparar.','A Dental Data dá dados coerentes de toda a rede sem centralizar fichas. O EEDS proíbe usar estes dados para publicidade ou para decisões que prejudiquem as pessoas, também nos seguros e nos prémios.'],s:['rede','datos']},
{id:'rede',q:'E para uma rede de clínicas?',k:['rede de clínicas','cadeia','grupo','qualidade','ers','publicidade em saúde'],
 a:['Comparar a qualidade entre clínicas obriga hoje a migrar fichas. Com a Dental Data, um conector junto a cada software calcula os indicadores em cada clínica com a mesma definição.','A rede pode mostrar a sua qualidade com informação verificável, como exige a regulação da publicidade em saúde (ERS), às seguradoras e ao regulador.'],s:['seguradora','colaborar']},
{id:'cheque',q:'Como medir o cheque-dentista?',k:['cheque','pnpso','sns','consultório','centro de saúde','prótese','dgs','programa'],
 a:['O Programa Nacional de Promoção da Saúde Oral paga cheques-dentista e mantém consultórios nos centros de saúde, e uma portaria de 20 de março de 2026 cria o cheque para próteses. Mas 98 dos 278 concelhos do continente continuam sem consultório do SNS.','A Dental Data permite medir os resultados destes programas nas clínicas aderentes, sem centralizar fichas: a pergunta viaja e só volta o resultado agregado.'],s:['ehds','colaborar']},
{id:'ehds',q:'O que muda com o EEDS em Portugal?',k:['eeds','ehds','2027','2029','2031','spms','rse','organismo','artigo 50','micro'],
 a:['Datas-chave: até <b>26 de março de 2027</b> cada Estado designa os seus organismos de acesso; a partir de <b>26 de março de 2029</b> aplica-se a maior parte das regras de uso secundário; em <b>2031</b> entram as imagens médicas.','Em Portugal, a <b>SPMS</b> coordena a preparação (Despacho 3030/2025) e trabalha num registo de saúde eletrónico único, mas o organismo de acesso ainda não está designado. O dado dentário, quase todo privado, não está nesses sistemas.'],s:['cheque','colaborar']},
{id:'ia',q:'Como funciona a IA nas radiografias?',k:[' ia ','inteligência artificial','radiograf','imagem','cárie','periodont','algoritmo','modelo','anacom','infarmed'],
 a:['Com aprendizagem federada e computação confidencial: <b>o algoritmo vai ao dado</b>, e não o contrário. Nenhuma radiografia sai da clínica.','O nosso modelo de cárie interproximal e perda óssea periodontal está em validação clínica e ajuda o profissional sem substituir o diagnóstico. A autoridade para a IA é a ANACOM; para dispositivos médicos, o INFARMED.'],s:['datos','tecnologia']},
{id:'tecnologia',q:'Que tecnologia usam?',k:['tecnolog','conector','norma','gaia','idsa','eclipse','edc','fhir','dicom','software','microsoft','azure'],
 a:['Um conector no <b>Microsoft Azure</b>, com os dados na União Europeia, integrado no software de gestão da clínica.','Nas fronteiras do espaço, normas europeias abertas: Gaia-X, IDSA e Dataspace Protocol, Eclipse EDC, FHIR, DICOM e HealthDCAT-AP. Qualquer um se pode ligar, mesmo sem Microsoft.'],s:['ehds','colaborar']},
{id:'seguridad',q:'Cumpre o RGPD?',k:['rgpd','gdpr','cnpd','privacidade','segurança','consentimento','jurídic'],
 a:['Os dados identificáveis nunca são centralizados: só circulam resultados agregados, sob contrato, no quadro do RGPD e da Lei n.º 58/2019, sob a supervisão da CNPD.','Cada projeto é documentado com o encarregado de proteção de dados da organização e uma avaliação de impacto.'],s:['datos','ehds']},
{id:'publicidad',q:'Os dados podem ser usados para publicidade?',k:['publicidad','marketing','vender','venda','comercial','promover'],
 a:['Nunca. O EEDS proíbe expressamente o uso de dados de saúde para publicidade, e em Portugal a publicidade em saúde é regulada pela ERS.','Os usos previstos são a qualidade dos cuidados, a IA em imagens e evidência para a indústria sobre implantes e materiais.'],s:['datos','seguradora']},
{id:'colaborar',q:'Como podemos colaborar?',k:['colabor','parceir','particip','projeto','piloto','contact','software'],
 a:['Em Portugal procuramos uma <b>rede de clínicas</b> ou uma <b>seguradora com rede dentária</b> para um primeiro projeto de indicadores de qualidade, e propomos ao SNS e ao regulador medir os resultados do cheque-dentista.','O próprio caso de uso financia o conector. Deixe os seus dados no formulário e propomos uma conversa.'],s:['seguradora','cheque']},
{id:'experiencia',q:'Quem são e que experiência têm?',k:['quem','empresa','experiência','software in a box','referência','projetos','global data care'],
 a:['Software in a Box, com escritórios em Madrid e Bruxelas. Entre 2024 e 2026 desenhámos e executámos três demonstradores de espaços de dados financiados pela Secretaria de Estado espanhola da Digitalização e da IA: <b>Global Data Care</b> (saúde), <b>PROCUREDATA</b> (compras) e <b>EcoDataNet</b> (economia circular).','Mais informação sobre os <a href="https://datos.softwareinabox.eu/pt/" target="_blank" rel="noopener">nossos espaços de dados</a>.'],s:['tecnologia','colaborar']},
{id:'documentos',q:'Onde posso ler o estudo?',k:['estudo','documento','pdf','descarreg','relatório','apresentação','vídeo','ler'],
 a:['O estudo comparativo europeu está disponível em <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">inglês</a>, com a apresentação e o vídeo completo. As apresentações animadas desta página resumem cada pergunta em menos de um minuto.'],s:['datos','ehds']}
]'''

BLOQUES = {
"espana": r'''
<section class="s soft" id="mercado-pt"><div class="wrap">
 <div class="head"><div class="eyebrow">O mercado português</div><h2>Os dados existem, são abundantes e ninguém os liga</h2><p>Em Portugal, quem paga a medicina dentária são sobretudo as famílias e as seguradoras; o SNS atua com cheques-dentista e consultórios nos centros de saúde. Cada clínica guarda as fichas e as radiografias no seu próprio software, fora do registo de saúde eletrónico.</p></div>
 <div class="grid4">
  <div class="card"><div class="num">MÉDICOS DENTISTAS</div><h3 class="big">13 876</h3><p>médicos dentistas com inscrição ativa em 2025 (OMD).</p></div>
  <div class="card"><div class="num">FATURAÇÃO</div><h3 class="big">1 875 M€</h3><p>de faturação das clínicas dentárias em 2025, mais 6,3 % (Informa D&amp;B).</p></div>
  <div class="card"><div class="num">CHEQUE-DENTISTA</div><h3 class="big">45 €</h3><p>valor do cheque-dentista do Programa Nacional de Promoção da Saúde Oral.</p></div>
  <div class="card"><div class="num">SNS</div><h3 class="big">98 de 278</h3><p>concelhos do continente sem consultório de saúde oral no SNS no fim de 2025 (ERS).</p></div>
 </div>
 <div class="grid2" style="margin-top:22px">
  <div class="card"><h3>PNPSO 2030</h3><p>Reorganiza os cheques e cria o cheque para próteses (portaria de 20 de março de 2026). Mais de 50.000 utentes passaram pelos consultórios do SNS em 2025, mas ninguém mede os resultados.</p></div>
  <div class="card"><h3>Muitos dentistas, mal distribuídos</h3><p>As inscrições suspensas passaram de 532 em 2005 para 2.583 em 2025, em grande parte por emigração. As famílias pagam diretamente cerca de 29 % da despesa de saúde.</p></div>
 </div>
 <p class="pcap">Fonte: Software in a Box, <a href="/docs/dental-health-data-spaces-europe-ehds.pdf" target="_blank" rel="noopener" lang="en">Dental health data spaces in Europe · Estudo comparativo</a> (novembro de 2026), capítulo Portugal, e as fontes aí citadas (OMD, ERS, DGS, SPMS). Dados atualizados em novembro de 2026.</p>
</div></section>
''',
"para-quien": r'''
<section class="s soft" id="para-quien"><div class="wrap">
 <div class="head"><div class="eyebrow">Para quem</div><h2>O dado clínico dentário, hoje no setor privado, pronto para o EEDS</h2><p>A Dental Data não substitui o registo de saúde eletrónico. Traz o dado clínico dentário num formato interoperável e com catálogo HealthDCAT-AP, pronto para o organismo de acesso que Portugal vier a designar.</p></div>
 <div class="grid4 who-grid">
  <div class="card"><div class="num">SEGURADORAS</div><h3>Dados coerentes da rede</h3><p>Custos e resultados comparáveis entre as clínicas convencionadas, sem centralizar fichas.</p></div>
  <div class="card"><div class="num">REDES DE CLÍNICAS</div><h3>Qualidade comparável</h3><p>Indicadores com a mesma definição em todas as clínicas, apresentados como informação verificável.</p></div>
  <div class="card"><div class="num">SNS, ERS E DGS</div><h3>Medir os programas</h3><p>Resultados do cheque-dentista, do cheque-prótese e dos consultórios dos centros de saúde.</p></div>
  <div class="card"><div class="num">SOFTWARE</div><h3>Um conector a mais</h3><p>Junto ao software de gestão da clínica, com novos serviços para os clientes.</p></div>
 </div>
 <div class="head" style="margin-top:56px;margin-bottom:22px"><h2 style="font-size:28px">Roteiro</h2></div>
 <div class="flow">
  <div class="step"><div class="c">1</div><b>2027 · Primeiro projeto</b><span>Indicadores de qualidade com uma rede de clínicas ou uma seguradora com rede dentária.</span></div>
  <div class="step"><div class="c">2</div><b>2027–2028 · Consolidação</b><span>Consolidação dos projetos e medição dos programas públicos com o SNS e o regulador.</span></div>
  <div class="step"><div class="c">3</div><b>Março de 2029 · Catalogado</b><span>Um conjunto de dados catalogado para o EEDS. A SPMS coordena a preparação; o organismo de acesso está por designar.</span></div>
 </div>
 <div class="nl-band"><div><b>Também em Espanha e em Itália</b><p>Um só produto para toda a Europa, adaptado à língua, aos dados e ao direito de cada país.</p></div><a href="/es/" lang="es" hreflang="es-ES">España →</a>&nbsp;&nbsp;<a href="/it/" lang="it" hreflang="it-IT">Italia →</a></div>
</div></section>
''',
"contacto": r'''
<section class="s cta" id="contacto"><div class="wrap">
 <h2>Primeiros parceiros em Portugal</h2>
 <p>Redes de clínicas, seguradoras, fornecedores de software e instituições: diga-nos brevemente quem é e propomos uma conversa, online ou em Bruxelas.</p>
 <form class="cform" action="https://formsubmit.co/partners@softwareinabox.eu" method="POST">
  <input type="hidden" name="_subject" value="Dental Data · Portugal">
  <input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="https://www.softwareinabox.eu/gracias.html">
  <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
  <label class="sr" for="f-n">Nome</label><input id="f-n" name="Nome" required placeholder="Nome e apelido" autocomplete="name">
  <label class="sr" for="f-o">Organização</label><input id="f-o" name="Organização" placeholder="Organização" autocomplete="organization">
  <label class="sr" for="f-p">Perfil</label><select id="f-p" class="full" name="Perfil"><option value="">Perfil da sua organização</option><option>Seguradora</option><option>Rede de clínicas</option><option>Clínica dentária</option><option>SNS, regulador ou instituição</option><option>Fornecedor de software ou parceiro Microsoft</option><option>Indústria</option><option>Outro</option></select>
  <label class="sr" for="f-e">E-mail</label><input id="f-e" class="full" type="email" name="E-mail" required placeholder="E-mail profissional" autocomplete="email">
  <label class="sr" for="f-m">Mensagem</label><textarea id="f-m" name="Mensagem" placeholder="Sobre o que quer falar connosco?"></textarea>
  <label class="ok full"><input type="checkbox" name="Consentimento" value="Aceita a política de privacidade" required><span>Li e aceito a <a href="https://www.softwareinabox.eu/pt/privacidad.html" target="_blank" rel="noopener">política de privacidade</a>. Só usaremos os seus dados para lhe responder.</span></label>
  <button type="submit">Enviar</button>
 </form>
 <p style="font-size:15px;margin-top:18px">Ou escreva para <a href="mailto:partners@softwareinabox.eu" style="color:#fff;font-weight:600">partners@softwareinabox.eu</a> · <a href="tel:+34601398868" style="color:#fff;font-weight:600">+34 601 398 868</a> · Bruxelas e Madrid</p>
</div></section>
''',
}

TEXTOS = {
"m000": "<title>Dental Data Portugal · Espaço de dados dentários federado para o EEDS | Software in a Box</title>",
"m001": 'content="A Dental Data é um espaço de dados dentários federado no Microsoft Azure: medir a qualidade entre clínicas sem mover um único processo clínico. Para seguradoras, redes de clínicas e programas públicos de saúde oral."',
"m002": '<link rel="canonical" href="https://dentaldata.softwareinabox.eu/pt/">',
"m003": 'content="pt_PT"',
"m004": '<meta property="og:title" content="Dental Data Portugal · Medir a qualidade entre clínicas sem mover um único processo">',
"m005": 'content="Os indicadores são calculados na clínica e só viaja o resultado."',
"m006": '<meta property="og:url" content="https://dentaldata.softwareinabox.eu/pt/">',
"m007": '<a class="brand" href="/pt/" aria-label="Dental Data Portugal, início">',
"m015": '<ul id="m2"><li><a href="#para-quien">Seguradoras</a></li><li><a href="#para-quien">Redes de clínicas</a></li><li><a href="#para-quien">SNS e reguladores</a></li><li><a href="#para-quien">Software e TI</a></li></ul>',
"m017": '<li><a href="#destacados">Estudo, apresentação e vídeos</a></li><li><a href="#mercado-pt">O mercado português</a></li><li><a href="#preguntas">Perguntas frequentes</a></li><li><a href="https://datos.softwareinabox.eu/pt/">Os nossos espaços de dados</a></li>',
"m018": '<a class="tbtn white" href="#contacto">Fale connosco</a>\n  <button',
"m021": '<li><a href="/es/" hreflang="es-ES" lang="es">Español · España</a></li>',
"m027": '<a href="#solucion">Solução</a><a href="#para-quien">Para quem</a><a href="#destacados">Recursos</a><a href="#preguntas">Perguntas frequentes</a><a href="#contacto">Fale connosco</a>',
"m028": '<div class="pre">Portugal · Espaço Europeu de Dados de Saúde</div>',
"m029": '<h1 id="h1">Medir a qualidade entre clínicas <em>sem mover um único processo clínico</em></h1>',
"m030": '<p class="lead">A Dental Data liga clínicas, redes e seguradoras num espaço de dados federado: os indicadores são calculados na clínica e só viaja o resultado.</p>',
"m034": '<button class="chip" type="button" data-q="seguradora">O que ganha uma seguradora?</button>',
"m035": '<button class="chip" type="button" data-q="cheque">Como medir o cheque-dentista?</button>',
"m036": '<button class="chip" type="button" data-q="datos">Os dados saem da clínica?</button>',
"m037": '<button class="chip" type="button" data-q="ehds">O que muda com o EEDS?</button>',
"m038": '<button class="chip" type="button" data-q="colaborar">Como colaborar?</button>',
"m039": '<p class="trust">Experiência em <b>3 espaços de dados</b> financiados com fundos públicos · Conector no <b>Microsoft Azure</b> com os dados na UE</p>',
"m040": '<h2>Ligue as clínicas sem migrar uma única ficha</h2>',
"m041": '<p>Procuramos uma rede de clínicas ou uma seguradora com rede dentária para um primeiro projeto de indicadores de qualidade.</p>',
"m042": '<a class="tbtn white" href="#contacto">Fale connosco</a><button class="tbtn outline" type="button" data-open-assistant>Pergunte ao assistente</button>',
"m043": '<div class="cap">O que ganha</div>',
"m044": '<b>Qualidade comparável entre clínicas</b><span>Indicadores homogéneos mesmo com software diferente.</span>',
"m045": '<b>IA em imagens, sem mover radiografias</b><span>O algoritmo vai ao dado: aprendizagem federada e computação confidencial.</span>',
"m046": '<b>Preparado para o EEDS antes de 2029</b><span>Um espaço catalogado, pronto para os pedidos dos organismos de acesso.</span>',
"m047": '<b>Resultados dos programas públicos</b><span>Cheque-dentista e consultórios do SNS, medidos sem centralizar fichas.</span>',
"m088": '<a class="flogo" href="/pt/" aria-label="Dental Data Portugal, início">',
"m090": '<div><h4>Países</h4><a href="/es/" lang="es">España</a><a href="/it/" lang="it">Italia</a><a href="/fr/" lang="fr">France</a><a href="/">Todos os países</a></div>',
"m094": '<div><h4>Contacto</h4><a href="#contacto">Fale connosco</a>',
"m095": '<a href="/en/" lang="en">Dental Data Europe</a></div>',
"m096": 'stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.8 2.5 15.2 0 18M12 3c-2.5 2.8-2.5 15.2 0 18"/></svg>Português (Portugal)</span>',
"m109": "bot(['Olá! Sou o assistente da Dental Data. Explico como funciona o espaço de dados dentários federado, o que oferece a seguradoras e redes de clínicas e o que significa o Espaço Europeu de Dados de Saúde para a medicina dentária em Portugal.','Escolha uma pergunta ou escreva a sua. Por favor, não escreva dados pessoais nem dados de doentes: guardamos de forma anónima as perguntas e respostas para melhorar o assistente.'],['seguradora','cheque','datos','ehds','colaborar'],true)",
"m115": "['datos','ehds','colaborar','tecnologia']",
"m116": "idioma:'pt',pais:'pt'",
"m118": "var FUENTES={'01-que-es-dental-data.md':'O que é a Dental Data','03-solucion-casos-uso.md':'Solução e casos de uso','05-tecnologia.md':'Tecnologia','08-empresa-recursos.md':'Software in a Box','10-estudio-comparativo-en.md':'Estudo comparativo (PDF)','11-ehds-europa.md':'O EEDS na Europa','pais/pt.md':'Dental Data em Portugal'}",
}

REEMPLAZOS = desde_claves(TEXTOS) + [
('<li><a href="/pt/" hreflang="pt-PT" lang="pt">Português · Portugal</a></li>', '<li><a href="/pt/" hreflang="pt-PT" lang="pt" aria-current="page">Português · Portugal</a></li>'),
]
