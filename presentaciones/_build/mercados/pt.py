LANG = "pt-PT"
UI = {
 "rm": "Movimento reduzido: cada cena é mostrada completa.", "ini": "Prima → ou a barra de espaço para começar",
 "locucion": "🔊 Narração ativa", "ctl": "Controlos da apresentação", "ant": "Cena anterior", "pp": "Reproduzir ou pausar",
 "sig": "Cena seguinte", "pista": "← → espaço · 1–{n} · F · H oculta", "pc": "Ecrã inteiro",
 "escena": "Cena", "quitar": "🔇 Desligar som", "activar": "🔊 Ligar som", "ver": "▶ Ver com narração (som ligado)",
}
PIEZAS = {
"p01": ([
 "Porque é que os dados dentários faltam no Espaço Europeu de Dados de Saúde?",
 "Porque faltam os dados dentários no EEDS?",
 "Apresentação animada da Dental Data: porque é que a medicina dentária é a grande ausente do Espaço Europeu de Dados de Saúde (EEDS).",
 "Fontes: estudo comparativo da Software in a Box (nov. 2026) · Ordem dos Médicos Dentistas · INE · DGS",
 "Abertura", "Dental Data · Pergunta 1", "Porque é que os dados dentários faltam no", "Espaço Europeu de Dados de Saúde", "?",
 "Os grandes ausentes", "Espaço Europeu de Dados de Saúde (EEDS)", "Os dados dentários são", "os grandes ausentes",
 "Resumo do paciente", "Receita eletrónica", "Imagens médicas", "Análises clínicas", "Medicina dentária", "não ligada",
 "Porquê", "Não por falta de valor, mas pela", "forma como está organizada", "a medicina dentária",
 "Pagamento direto", "Famílias e seguradoras", "Programas focalizados", "Cheque-dentista",
 "Software próprio", "Cada clínica o seu", "Sem dados de resultados", "Ninguém mede o resultado",
 "Portugal em números", "Portugal", "Um mercado privado e fragmentado",
 "98", "&lt;small&gt;/278&lt;/small&gt;", "noventa", "0", "municípios", "municípios sem consultório dentário do SNS",
 "13876", ".", "&lt;small&gt;&lt;/small&gt;", "catorze", "0", "dentistas", "médicos dentistas em atividade",
 "1875", ".", "oitocentos", "0", "milhões", "milhões de € de faturação das clínicas",
 "Ilhas de dados", "Os dados existem, mas vivem", "em ilhas", "software", "Clínicas sem ligação",
 "fora", "Fora do registo de saúde eletrónico",
 "Fecho", "Os dados existem.", "Ninguém os liga.", "A Dental Data liga-os", "sem os mover", ".",
], """Os dados dentários são os grandes ausentes do Espaço Europeu de Dados de Saúde. Não por falta de valor, mas pela forma como a
 medicina dentária está organizada. Em Portugal, quem paga são sobretudo as famílias e as seguradoras; o Serviço Nacional de Saúde atua
 com cheques-dentista e consultórios nos centros de saúde. Mas noventa e oito dos duzentos e setenta e oito municípios continuam sem
 consultório, há quase catorze mil dentistas em atividade e as clínicas faturam mil oitocentos e setenta e cinco milhões de euros. Cada
 clínica guarda as fichas e as radiografias no seu próprio software, fora do registo de saúde eletrónico, e ninguém mede os resultados do
 dinheiro público. Os dados existem e têm donos com razões para os partilhar sob controlo. O que falta é quem os ligue. Isso é a Dental
 Data.""",
 ["Os dados dentários são", "Não por falta", "Mas noventa e oito", "Cada clínica guarda", "Os dados existem e"]),

"p02": ([
 "Como funciona um espaço de dados federado?", "Como funciona um espaço de dados federado?",
 "Apresentação animada da Dental Data: como funciona um espaço de dados dentários federado.",
 "Fonte: Dental Data · a solução e os casos de uso (base de conhecimento pública)",
 "Abertura", "Dental Data · Pergunta 2", "Como funciona um", "espaço de dados", "federado?",
 "A clínica", "Cada participante guarda as suas fichas", "no seu próprio software", "junto", "Software de gestão", "fichas e radiografias",
 "instala", "Conector", "instalado ao lado",
 "A rede", "Os conectores formam uma rede com um", "catálogo comum", "Catálogo comum", "só metadados",
 "Clínica", "+ conector", "Clínica", "+ conector", "Rede de clínicas", "+ conector", "Seguradora", "+ conector",
 "O catálogo diz que dados existem. Não os guarda.",
 "Uma pergunta", "A pergunta viaja;", "só volta o resultado", "Catálogo comum", "só metadados",
 "Clínica", "+ conector", "Clínica", "+ conector", "Rede de clínicas", "+ conector", "Seguradora", "+ conector",
 "1 · A pergunta viaja", "2 · Calculada em cada clínica", "3 · Volta o resultado agregado",
 "O que viaja e o que não", "O que passa pela rede…", "e o que não passa", "Viaja", "Consentimentos", "Metadados do catálogo",
 "Resultados agregados", "Não viaja", "Fichas identificáveis", "Radiografias",
 "Fecho", "O dado fica.", "Viaja a resposta.", "Assim funciona um espaço de dados federado.",
], """Num espaço de dados federado, cada clínica, rede ou seguradora guarda as suas fichas no seu próprio software de gestão. Junto a
 esse software instala-se um conector. O conector publica num catálogo comum que dados existem, mas não os dados. Quando alguém precisa
 de um indicador, a pergunta viaja até cada clínica, é calculada lá e volta só o resultado agregado. Pela rede passam consentimentos,
 metadados e resultados. Nunca uma ficha identificável. O dado fica na clínica. O que viaja é a resposta.""",
 ["Num espaço", "O conector publica", "Quando alguém", "Pela rede passam", "O dado fica"]),

"p03": ([
 "Os meus dados saem da clínica?", "Os meus dados saem da clínica?",
 "Apresentação animada da Dental Data: privacidade, contratos de utilização e o controlo da clínica sobre os seus dados.",
 "Fontes: Dental Data (base de conhecimento) · RGPD · Lei n.º 58/2019 · Regulamento (UE) 2025/327, art. 54.º e 71.º · Informação geral; não é aconselhamento jurídico",
 "Abertura", "Dental Data · Pergunta 3", "Os meus dados saem", "da clínica", "?",
 "A resposta", "Não.", "Nenhuma ficha identificável", "sai da clínica",
 "O contrato", "Cada utilização dos dados tem", "um contrato digital", "Contrato de utilização (ODRL)",
 "quem acede", "Quem acede?", "para quê", "Para quê?", "durante quanto tempo", "Durante quanto tempo?",
 "esse contrato", "E não fica no papel:", "a máquina", "a máquina", "fá-lo cumprir",
 "A máquina fá-lo cumprir", "Sem contrato, não há acesso.", "Com contrato, só um resultado agregado.",
 "o tiver", "Pedido", "sem contrato", "o tiver", "Pedido", "com contrato", "Clínica", "com o seu conector",
 "não há acesso", "Acesso negado", "só volta", "agregado", "Resultado agregado",
 "O quadro", "A clínica decide sempre,", "no quadro da lei", "regulamento geral", "RGPD", "portuguesa",
 "Lei n.º 58/2019 (execução do RGPD)", "cnpd", "Comissão Nacional de Proteção de Dados (CNPD)",
 "nunca são usados", "EEDS · art. 54.º: nunca para publicidade", "publicidade",
 "EEDS · art. 71.º: o doente pode opor-se",
 "Fecho", "Sem contrato,", "não há acesso.", "A clínica decide sempre.",
], """Os dados saem da clínica? Não. Nenhuma ficha identificável sai da clínica. Cada utilização dos dados é regulada por um contrato
 digital que define quem acede, para quê e durante quanto tempo. E esse contrato não fica no papel: a máquina fá-lo cumprir. Se um pedido
 não tiver contrato, não há acesso. Se o tiver, só volta um resultado agregado. A clínica decide sempre, no quadro do regulamento geral
 sobre a proteção de dados e da lei portuguesa de proteção de dados, sob a supervisão da CNPD. E com uma regra clara do Espaço Europeu de
 Dados de Saúde: os dados de saúde nunca são usados para publicidade.""",
 ["Os dados saem", "Cada utilização", "Se um pedido", "A clínica decide", "FIN"]),

"p04": ([
 "O que ganha uma rede de clínicas?", "O que ganha uma rede de clínicas?",
 "Apresentação animada da Dental Data: indicadores de qualidade comparáveis entre clínicas sem migrar fichas.",
 "Fontes: Dental Data · casos de uso e piloto (base de conhecimento) · ERS · Regulamento (UE) 2025/327, art. 72.º · Barras ilustrativas",
 "Abertura", "Dental Data · Pergunta 4", "O que ganha uma", "rede de clínicas", "?",
 "O problema", "As redes de clínicas crescem…", "e cada clínica tem o seu software",
 "Clínica 1", "Software A", "Clínica 2", "Software B", "Clínica 3", "Software C", "Clínica 4", "Software D", "Clínica 5", "Software E",
 "migrar", "Comparar hoje obriga a migrar fichas: caro e arriscado",
 "Sem migrar", "Com a Dental Data não é preciso:", "um conector junto a cada software",
 "Clínica 1", "Software A", "Conector", "Clínica 2", "Software B", "Conector", "Clínica 3", "Software C", "Conector",
 "Clínica 4", "Software D", "Conector", "Clínica 5", "Software E", "Conector",
 "Indicadores comparáveis", "O mesmo indicador,", "calculado em cada clínica",
 "Clínica 1", "Clínica 2", "Clínica 3", "Clínica 4", "Clínica 5",
 "Mesma definição em todas as clínicas", "lugar", "Nenhuma ficha muda de lugar",
 "Valor acrescentado", "E além disso…", "Qualidade verificável", "Perante seguradoras e a ERS.",
 "informação", "Informação verificável, não publicidade", "Como exige a regulação da publicidade em saúde.",
 "Fecho", "Qualidade comparável,", "sem migrar uma única ficha.", "Indicadores de qualidade comparáveis em toda a rede.",
], """As redes de clínicas dentárias crescem em Portugal, embora a maioria das clínicas continue independente e cada uma tenha o seu
 próprio software. Comparar a qualidade entre clínicas obriga hoje a migrar fichas, um processo caro e arriscado. Com a Dental Data não é
 preciso: instala-se um conector junto a cada software e os indicadores são calculados em cada clínica com a mesma definição. A direção vê
 resultados comparáveis de toda a rede sem que nenhuma ficha mude de lugar. E a rede pode mostrar a sua qualidade com informação
 verificável, como exige a regulação da publicidade em saúde, às seguradoras e ao regulador. Qualidade comparável, sem migrar uma única
 ficha.""",
 ["As redes de clínicas", "Com a Dental Data", "A direção vê", "E a rede pode", "Qualidade comparável, sem"]),

"p05": ([
 "O que ganha uma seguradora?", "O que ganha uma seguradora?",
 "Apresentação animada da Dental Data: dados coerentes sobre custos e resultados de uma rede dentária sem centralizar fichas.",
 "Fontes: Dental Data (base de conhecimento) · ASF · Regulamento (UE) 2025/327, art. 54.º",
 "Abertura", "Dental Data · Pergunta 5", "O que ganha uma", "seguradora", "?",
 "A rede", "Clínicas convencionadas,", "cada uma com o seu software",
 "Seguradora", "Seguros e planos", "dentários", "Clínicas próprias", "algumas seguradoras", "Clínica convencionada", "software próprio",
 "Clínica convencionada", "software próprio", "Custos e resultados dispersos",
 "Dados coerentes", "Dados coerentes de toda a rede,", "sem centralizar fichas",
 "Seguradora", "Clínica", "software próprio", "Clínica", "software próprio", "Clínica", "software próprio", "Clínica", "software próprio",
 "Cálculo na clínica · só volta o resultado agregado",
 "Um canal", "A rede como", "canal de participação", "Clínicas independentes", "Redes convencionadas", "participem", "Espaço de dados dentários",
 "Limites claros", "Com limites claros:", "o que o EEDS proíbe", "publicidade", "Publicidade",
 "Os dados de saúde nunca são usados para publicidade.", "decisões", "Decisões prejudiciais",
 "Nem para decisões que prejudiquem as pessoas, também nos seguros.", "Regulamento (UE) 2025/327, artigo 54.º",
 "Fecho", "Dados coerentes de toda a rede,", "sem centralizar fichas.", "Com o controlo sempre na clínica.",
], """Em Portugal, os seguros e planos dentários funcionam com redes de clínicas convencionadas, e algumas seguradoras já abrem clínicas
 próprias. Cada clínica usa o seu software, e os dados de custos e resultados não se podem comparar. A Dental Data dá à seguradora dados
 coerentes de toda a rede sem centralizar fichas: o cálculo faz-se em cada clínica e só volta o resultado agregado. A rede pode ainda
 servir de canal para que participem clínicas independentes. Com limites claros: o Espaço Europeu de Dados de Saúde proíbe usar estes
 dados para publicidade ou para decisões que prejudiquem as pessoas, também nos seguros. Dados coerentes de toda a rede, sem centralizar
 fichas.""",
 ["Em Portugal, os seguros", "A Dental Data dá", "A rede pode", "Com limites claros", "Dados coerentes de toda a rede, sem"]),

"p06": ([
 "IA nas radiografias sem mover as radiografias", "Como funciona a IA nas radiografias dentárias?",
 "Apresentação animada da Dental Data: aprendizagem federada e computação confidencial em imagens dentárias.",
 "Fontes: Dental Data (base de conhecimento) · Regulamento (UE) 2026/1744 · Regulamento (UE) 2025/327 · Modelo em validação clínica; não substitui o diagnóstico · Dispositivos médicos: INFARMED · IA: ANACOM",
 "Abertura", "Dental Data · Pergunta 6", "Como se treina uma", "IA dentária", "sem mover as radiografias?",
 "O dilema", "Treinar uma IA exige muitas radiografias…", "juntá-las é um risco", "Um arquivo central",
 "Centralizar radiografias aumenta o risco",
 "O algoritmo viaja", "A Dental Data inverte o caminho:", "o algoritmo viaja", "Modelo de IA",
 "Clínica", "as radiografias ficam", "Clínica", "as radiografias ficam", "Clínica", "as radiografias ficam",
 "aprende", "Aprende em cada clínica", "devolve", "Devolve só o que aprendeu",
 "Computação confidencial", "Computação", "confidencial", "Protege os dados mesmo durante o processamento.",
 "O modelo", "Primeiro modelo", "Cárie interproximal", "Em radiografias dentárias.", "óssea", "Perda óssea periodontal",
 "Em radiografias dentárias.", "validação", "Em validação clínica", "ajuda", "Uma ajuda para o profissional: não substitui o diagnóstico",
 "O que vem", "Preparado para", "o que vem", "2 ago 2028", "Regulamento da IA: obrigações para IA em dispositivos médicos",
 "dois mil e trinta e um", "26 mar 2031", "As imagens médicas entram no Espaço Europeu de Dados de Saúde",
 "Fecho", "O algoritmo", "vai ao dado.", "IA em imagens dentárias sem mover radiografias.",
], """Treinar uma IA dentária exige muitas radiografias. Mas juntá-las num só lugar é um risco. A Dental Data inverte o caminho: o
 algoritmo viaja até cada clínica, aprende lá e devolve só o que aprendeu, nunca as imagens. Os cálculos fazem-se com computação
 confidencial, que protege os dados enquanto são processados. O primeiro modelo, para cárie interproximal e perda óssea periodontal, está
 em validação clínica. É uma ajuda para o profissional: não substitui o seu diagnóstico. E prepara-se para o que vem: em dois mil e
 trinta e um, as imagens médicas entram no Espaço Europeu de Dados de Saúde. O algoritmo vai ao dado.""",
 ["Treinar uma IA", "A Dental Data inverte", "Os cálculos fazem-se", "O primeiro modelo", "E prepara-se", "O algoritmo vai"]),

"p07": ([
 "Que datas fixa o Espaço Europeu de Dados de Saúde?", "Que datas fixa o EEDS?",
 "Apresentação animada da Dental Data: o calendário do EEDS e a situação em Portugal (SPMS).",
 "Fontes: Regulamento (UE) 2025/327 (art. 50.º e 105.º) · Despacho n.º 3030/2025 · SPMS",
 "Abertura", "Dental Data · Pergunta 7", "Que datas fixa o", "Espaço Europeu de Dados de Saúde", "?",
 "Calendário", "Já em vigor", "e com datas", "26 mar 2025", "Em vigor", "dois mil e vinte e sete", "26 mar 2027",
 "Organismos de acesso designados", "dois mil e vinte e nove", "26 mar 2029", "Uso secundário: a maior parte das regras",
 "dois mil e trinta e um", "26 mar 2031", "Imagens médicas, como as radiografias",
 "A janela", "Entre 2027 e 2029:", "dois anos para ligar clínicas e redes",
 "26 mar 2025", "Em vigor", "26 mar 2027", "Organismos de acesso designados", "26 mar 2029", "Uso secundário: a maior parte das regras",
 "26 mar 2031", "Imagens médicas, como as radiografias",
 "Artigo 50.º", "A maioria das clínicas são microempresas:", "isentas por defeito", "participar", "através",
 "Clínicas independentes", "Art. 50.º: isentas salvo decisão contrária do Estado", "canal agregado", "Canal agregado",
 "redes · seguradoras · Ordem", "através", "Espaço de dados dentários",
 "Portugal", "Portugal", "SPMS coordena a preparação do EEDS (Despacho 3030/2025)", "registo",
 "Trabalho num registo de saúde eletrónico único. Organismo de acesso por designar; o dado dentário, quase todo privado, fica de fora.",
 "designado", "Organismo de acesso ainda não designado (nov. 2026)",
 "Fecho", "Quem estiver ligado em 2029", "será o interlocutor natural", "dos organismos de acesso a dados de saúde.",
], """O Espaço Europeu de Dados de Saúde já está em vigor e tem datas: organismos de acesso em março de dois mil e vinte e sete, uso
 secundário em março de dois mil e vinte e nove e imagens médicas em dois mil e trinta e um. A maioria das clínicas são microempresas e
 ficam isentas por defeito: para participar é preciso um canal agregado, através de redes, seguradoras ou da Ordem. Em Portugal, os
 Serviços Partilhados do Ministério da Saúde coordenam a preparação desde dois mil e vinte e cinco e trabalham num registo de saúde
 eletrónico único, mas o organismo de acesso ainda não está designado. E o dado dentário, quase todo privado, não está em nenhum desses
 sistemas. Quem o ligar primeiro será o interlocutor natural.""",
 ["O Espaço Europeu", "secundário em março", "A maioria das clínicas", "Em Portugal, os", "Quem o ligar"]),

"p08": ([
 "Que tecnologia está por trás da Dental Data?", "Que tecnologia está por trás da Dental Data?",
 "Apresentação animada da Dental Data: Microsoft dentro do nó, normas europeias abertas nas fronteiras.",
 "Fontes: Dental Data · tecnologia e empresa (base de conhecimento) · Microsoft e Azure são marcas da Microsoft Corporation; citadas como texto",
 "Abertura", "Dental Data · Pergunta 8", "Que tecnologia está por trás da", "Dental Data", "?",
 "A regra", "Uma regra simples", "Microsoft", "Azure", "dados na UE", "Dentro do nó", "Na fronteira: normas abertas",
 "Dentro do nó", "Dentro do nó:", "Microsoft", "Conector no Microsoft Azure", "Com os dados na União Europeia.",
 "integrado", "Integrado", "Com o software de gestão da clínica.", "implementado", "Implementado por parceiros", "Integradores e parceiros Azure.",
 "Na fronteira", "Nas fronteiras:", "normas europeias abertas", "gaiax", "Gaia-X", "protocolo", "IDSA", "eclipse", "Dataspace Protocol",
 "eclipse edc", "Eclipse EDC", "verificáveis", "Credenciais verificáveis", "fhir", "FHIR", "dicom", "DICOM", "healthdcatap", "HealthDCAT-AP",
 "Aberto a todos", "Qualquer um se pode ligar,", "mesmo sem Microsoft", "Nó no Azure", "Participante sem Microsoft",
 "Normas abertas", "Liga-se da mesma forma",
 "Experiência", "Não partimos do zero:", "três espaços de dados reais", "Global Data Care", "Saúde, em Gaia-X e Pontus-X.",
 "PROCUREDATA", "Contratação pública.", "EcoDataNet", "Resíduos e economia circular.",
 "Demonstradores financiados pela SEDIA (2024–2026), com conectores próprios baseados em Eclipse.",
 "Fecho", "Microsoft dentro do nó.", "Normas abertas nas fronteiras.", "Um espaço de dados dentários aberto a todos.",
], """A Dental Data segue uma regra simples: Microsoft dentro do nó, normas abertas nas fronteiras. Dentro de cada nó, o conector
 funciona no Microsoft Azure, com os dados na União Europeia, integrado com o software de gestão da clínica e implementado por parceiros
 Azure. Nas fronteiras, o espaço fala normas europeias abertas: Gaia-X, o protocolo dos espaços de dados, Eclipse EDC, credenciais
 verificáveis, FHIR, DICOM e HealthDCAT-AP. Assim, qualquer participante se pode ligar, mesmo sem Microsoft. E não partimos do zero: a
 Software in a Box já desenhou e executou três espaços de dados reais.""",
 ["segue uma regra", "Dentro de cada", "Nas fronteiras, o espaço", "Assim, qualquer", "E não partimos", "FIN"]),

"p09": ([
 "O que oferece a Dental Data à indústria?", "O que oferece a Dental Data à indústria?",
 "Apresentação animada da Dental Data: evidência do mundo real sob contrato para fabricantes, empresas de IA e software de gestão.",
 "Fontes: Dental Data (base de conhecimento) · Regulamento (UE) 2025/327, art. 54.º",
 "Abertura", "Dental Data · Pergunta 9", "O que oferece a Dental Data à", "indústria", "?",
 "Quem", "Para quem precisa de saber", "o que acontece na clínica", "Implantes", "materiais", "Materiais", "inteligência", "Inteligência artificial",
 "precisam", "Software de gestão",
 "Evidência real", "Evidência do mundo real,", "sem dados identificáveis", "Indústria", "pergunta sob contrato",
 "Clínicas", "Clínicas", "Clínicas", "Voltam resultados agregados, nunca fichas",
 "Para o software", "Para o software de gestão:", "um conector que acrescenta serviços", "O seu software de gestão",
 "Conector integrado", "Novos serviços", "para os seus clientes",
 "As regras", "As regras", "não mudam", "Um contrato para cada utilização", "Quem, para quê e durante quanto tempo.", "só resultados",
 "Só agregado", "Nenhum dado identificável sai da clínica.", "nunca", "Nunca publicidade", "O EEDS proíbe-o (art. 54.º).",
 "Fecho", "Evidência real,", "ordenada e sob contrato.", "Para a indústria e o software dentário.",
], """Para a indústria dentária, a evidência do mundo real vale muito. Os fabricantes de implantes e materiais, e as empresas de
 inteligência artificial, precisam de saber como os seus produtos se comportam na clínica. A Dental Data oferece-lhes essa evidência,
 ordenada e sob contrato: perguntas respondidas nas clínicas e resultados agregados que voltam sem dados identificáveis. Para os
 fornecedores de software de gestão, o conector é uma peça que se integra no seu produto e abre novos serviços aos seus clientes. As
 regras não mudam: um contrato para cada utilização, só resultados agregados e nunca publicidade. Evidência real, ordenada e sob
 contrato.""",
 ["Para a indústria dentária", "A Dental Data oferece-lhes", "Para os fornecedores", "As regras não", "Evidência real, ordenada"]),

"p10": ([
 "Como participar na Dental Data?", "Como participar na Dental Data?",
 "Apresentação animada da Dental Data: o programa de parceiros em Portugal, o roteiro e como participar.",
 "Fontes: Dental Data · programa de parceiros Portugal e roteiro (base de conhecimento) · Sem tarifas publicadas",
 "Abertura", "Dental Data · Pergunta 10", "Como participar na", "Dental Data", "?",
 "Procuramos", "Procuramos", "Uma rede de clínicas ou uma seguradora", "Para um primeiro projeto de indicadores de qualidade",
 "projeto", "Primeiro projeto 2027",
 "Financiamento", "O caso de uso", "financia o conector", "E propomos ao SNS e ao regulador medir os resultados do cheque-dentista, do cheque-prótese e dos consultórios dos centros de saúde.",
 "Roteiro", "O", "roteiro", "2027", "Primeiro projeto", "consolidamos", "2027–2028",
 "Consolidar projetos e participar nas consultas", "catalogado", "2029", "Conjunto de dados catalogado para o EEDS",
 "depois", "2029–2031", "Linha de imagem dentária",
 "Queremos falar também com", "Queremos falar também com…", "SNS · DGS · ERS", "ordem", "Ordem dos Médicos Dentistas",
 "universidades", "Universidades", "software", "Software de gestão", "seguradoras", "Seguradoras",
 "Falamos?", "Falamos?", "partners@softwareinabox.eu", "+34 601 398 868", "dentaldata.softwareinabox.eu",
], """Em Portugal procuramos uma rede de clínicas ou uma seguradora com rede dentária para um primeiro projeto de indicadores de
 qualidade. O próprio caso de uso financia o conector. E propomos ao Serviço Nacional de Saúde e ao regulador medir os resultados do
 cheque-dentista, do novo cheque-prótese e dos consultórios dos centros de saúde, sem centralizar fichas. Em dois mil e vinte e sete, o
 primeiro projeto; depois consolidamos os projetos; em dois mil e vinte e nove, um conjunto de dados catalogado; depois, a imagem
 dentária. Queremos falar também com a Ordem dos Médicos Dentistas, com as universidades, com as empresas de software de gestão e com as
 seguradoras. Falamos? Escreva para partners arroba softwareinabox ponto eu.""",
 ["Em Portugal procuramos", "O próprio caso", "Em dois mil e vinte e sete", "Queremos falar", "Falamos?"]),

"p11": ([
 "O que construímos no Microsoft Azure?", "O que construímos no Microsoft Azure?",
 "Apresentação animada da Dental Data: a arquitetura do espaço de dados dentários com os componentes do Microsoft Azure e o conector Eclipse EDC.",
 "Fontes: Dental Data · documento técnico (v1.3) e proposta MVP (v1.4) · Ícones oficiais da Microsoft (Azure, Microsoft Entra e Microsoft Fabric), usados segundo as suas condições para diagramas de arquitetura · Microsoft, Azure, Entra, Fabric e os nomes dos seus serviços são marcas da Microsoft Corporation",
 "Abertura", "Dental Data · Pergunta 11", "O que construímos no", "Microsoft Azure", "?",
 "A regra", "Uma regra guia o desenho", "Fronteira · normas abertas", "Nó · Microsoft Azure", "Microsoft", "dentro do nó",
 "Normas abertas na fronteira",
 "A clínica", "1 · Na", "clínica", "Aparelho de raio-X", "radiografia, CBCT", "gateway DICOM", "Gateway DICOM", "Orthanc · código aberto",
 "pseudonimizada", "Pseudonimizada na origem", "sem dados que identifiquem o doente",
 "O nó de dados", "2 · O", "nó de dados", "no Azure", "Nó de dados · Microsoft Azure", "azure health", "Azure Health Data Services",
 "a ficha", "Ficha · FHIR", "a imagem", "Imagem · DICOM", "microsoft fabric", "Microsoft Fabric", "prepara a análise",
 "onelake", "OneLake", "formatos abertos",
 "Segurança", "3 · Uma camada de", "segurança e identidade", "Segurança e identidade · à volta de tudo",
 "entra id", "Microsoft Entra ID", "identidades", "key vault", "Azure Key Vault", "chaves e segredos", "defender",
 "Microsoft Defender for Cloud", "proteção", "sentinel", "Microsoft Sentinel", "monitorização",
 "A fronteira", "4 · A", "fronteira", ": o conector Eclipse EDC", "Fronteira · normas abertas", "azure kubernetes", "Azure Kubernetes Service",
 "onde corre", "Eclipse", "Conector Eclipse EDC", "código aberto", "publica", "Catálogo", "HealthDCAT-AP",
 "negocia", "Contrato", "ODRL", "identifica-se", "Credenciais", "Gaia-X",
 "A IA", "5 · A", "IA", ": viaja o modelo, não os dados", "azure machine", "Azure Machine Learning",
 "aprendizagem federada · NVIDIA FLARE", "Clínica A", "Clínica B", "Clínica C", "o modelo viaja", "o modelo viaja", "o modelo viaja",
 "computação confidencial", "Computação confidencial", "protege os dados durante o processamento", "microsoft foundry", "Microsoft Foundry",
 "rascunhos que o dentista revê",
 "O percurso", "O percurso de uma radiografia", "Clínica", "Gateway DICOM", "Azure Health Data Services", "Microsoft Fabric e OneLake",
 "Eclipse EDC", "no Azure Kubernetes Service", "Rede europeia", "outras clínicas", "Segurança e identidade",
 "Microsoft Entra ID · Azure Key Vault · Microsoft Defender for Cloud · Microsoft Sentinel", "dado identificável",
 "Nenhum dado identificável sai do nó",
 "Fecho", "Microsoft dentro do nó.", "Normas abertas na fronteira.", "Assim construímos a Dental Data no Microsoft Azure.",
], """Isto é o que construímos no Microsoft Azure para a Dental Data. Uma regra guia o desenho: Microsoft dentro do nó, normas abertas
 na fronteira. Na clínica, a radiografia sai do aparelho através de um gateway DICOM de código aberto, Orthanc, e é pseudonimizada na
 origem. No nó de dados, o Azure Health Data Services guarda a ficha em FHIR e a imagem em DICOM. O Microsoft Fabric e o OneLake
 preparam os dados para análise. A segurança vem do Microsoft Entra ID, do Azure Key Vault, do Microsoft Defender for Cloud e do
 Microsoft Sentinel. Na fronteira trabalha o conector Eclipse EDC, implementado no Azure Kubernetes Service. Publica o catálogo em
 HealthDCAT-AP, negocia contratos ODRL e identifica-se com credenciais Gaia-X. A inteligência artificial treina-se com o Azure Machine
 Learning e a aprendizagem federada: o modelo viaja até cada clínica e os dados ficam onde estão. A computação confidencial protege os
 dados mesmo durante o processamento, e o Microsoft Foundry escreve rascunhos de relatórios que o dentista revê. Assim, cada radiografia
 segue um percurso seguro e controlado, da clínica ao modelo, sem que nenhum dado identificável saia do nó.""",
 ["Isto é o que", "Na clínica, a radiografia", "No nó de dados", "A segurança vem", "Na fronteira trabalha", "A inteligência artificial", "Assim, cada radiografia", "FIN"]),
}
