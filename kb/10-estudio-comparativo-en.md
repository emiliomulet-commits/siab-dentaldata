# Estudio comparativo (texto íntegro, en inglés)

Fuente: Software in a Box, "Dental health data spaces in Europe · Comparative study", noviembre de 2026. PDF público: https://dentaldata.softwareinabox.eu/docs/dental-health-data-spaces-europe-ehds.pdf

Contents
Executive summary4
1. Purpose, scope and methodology6
 1.1. Purpose of the study6
 1.2. Scope6
 1.3. Methodology and sources6

2. The European Health Data Space: what changes for dentistry7
 2.1. What the EHDS is7
 2.2. A phased timeline8
 2.3. The dental clinic's two entry doors9
 2.4. The clause that may leave the dentist out: Article 5010
 2.5. Implementation status11

3. Spain11
 3.1. Health system and funding of dental care11
 3.2. Structure of the dental clinic market12
 3.3. Digital health infrastructure12
 3.4. Regulatory framework and adaptation to the EHDS12
 3.5. Approach to oral health data13
 3.6. Market needs and regulatory needs14
 3.7. Value of a dental data space and opportunity for partners14

4. Belgium14
 4.1. Health system and funding of dental care14
 4.2. Structure of the dental clinic market15
 4.3. Digital health infrastructure15
 4.4. Regulatory framework and adaptation to the EHDS15
 4.5. Approach to oral health data15
 4.6. Market needs and regulatory needs16
 4.7. Value of a dental data space and opportunity for partners17

5. The Netherlands17
 5.1. Health system and funding of dental care17
 5.2. Structure of the dental clinic market17
 5.3. Digital health infrastructure17
 5.4. Regulatory framework and adaptation to the EHDS17
 5.5. Approach to oral health data18
 5.6. Market needs and regulatory needs19
 5.7. Value of a dental data space and opportunity for partners19

6. Denmark19
 6.1. Health system and funding of dental care19
 6.2. Structure of the dental clinic market19
 6.3. Digital health infrastructure20
 6.4. Regulatory framework and adaptation to the EHDS20
 6.5. Approach to oral health data20
 6.6. Market needs and regulatory needs21

 6.7. Value of a dental data space and opportunity for partners21

7. Germany22
 7.1. Health system and funding of dental care22
 7.2. Structure of the dental clinic market22
 7.3. Digital health infrastructure22
 7.4. Regulatory framework and adaptation to the EHDS22
 7.5. Approach to oral health data22
 7.6. Market needs and regulatory needs24
 7.7. Value of a dental data space and opportunity for partners24

8. Comparative analysis24
 8.1. Correlation between professional density and public funding24
 8.2. Differences in the approach to oral health data25
 8.3. Regulatory comparison26
 8.4. Readiness map and opportunity matrix27
 8.5. Cross-cutting market constraints29

9. Market needs, regulatory needs and alignment with the EHDS30
 9.1. Market needs by country30
 9.2. Regulatory needs by country31
 9.3. Alignment with Regulation (EU) 2025/32731
 9.4. The importance of national participation in the EHDS33

10. Use cases for the oral health data space33
11. Proposed architecture and the role of Software in a Box34
 11.1. Why a federated architecture34
 11.2. Components35
 11.3. Role of Software in a Box and its partners35
 11.4. Compliance framework for the connector36

12. Roadmap 2026-203137
13. Risks and constraints38
14. Conclusions40
About Software in a Box40
Annex A. Stakeholder map by country40
Annex B. Partner FAQ41
Annex C. Glossary42
Annex D. Sources42

Executive summary
This study compares how five European markets —Spain, Belgium, the Netherlands, Denmark and Germany—
are preparing for oral health data to become part of the European Health Data Space (EHDS), created by
Regulation (EU) 2025/327. The aim is practical: to identify in each country the market needs and regulatory
needs that a federated dental health data space can address, and to align them with the obligations and
opportunities the EHDS introduces between 2027 and 2031.

The central conclusion is that dental data is today the great absentee from Europe's health data architecture,
not for lack of clinical or economic value, but because of the way dentistry is organised in Europe: small
practices, mostly private spending for adults, proprietary practice software and little integration with public
health records. The EHDS does not solve this on its own; indeed, by exempting microenterprises from data
holder obligations unless a Member State decides otherwise [1], it may leave most clinics out. A federated data
space that aggregates clinics, chains and insurers is the most direct way for oral health data to reach health data
access bodies (HDABs) without professionals giving up control of their records.

Five very different starting points
 - Spain combines the highest dentist density in the group (87.3 per 100,000 inhabitants) with spending that
 patients pay 97% of themselves [2]. It already has a digital national health record and interoperable
 ePrescription in place, and a National Health Data Space live since February 2026 with more than 330
 datasets [3], but the private dentist is outside that circuit. Adaptation to the EHDS will be channelled
 through the draft Digital Health Act, under public consultation since September 2025 [4].
 - Belgium has a public reimbursement system (INAMI) that turns every reimbursable dental act into
 structured data: INAMI reimbursed €1.6 billion in dental care in 2025 [5]. Its Health Data Agency, created by
 law in 2023, already maintains a national catalogue of more than 480 datasets and is set to become the
 coordinating HDAB [6].
 - The Netherlands suffers a structural shortage of dentists —a quarter were trained abroad [7]— and rapid
 consolidation: more than 500 practices owned by private equity, accounting for about 30% of revenue [8].
 The Wet GIS creates a single health data authority that will take on the roles of digital health authority and
 HDAB [9].
 - Denmark offers free dental care up to age 21 and has kept the SCOR child oral health register since 1972, a
 European example of public oral health data used to make policy [10][11]. The challenge is adults, who are
 subsidised only around 15%.
 - Germany is the most advanced country: the ePA has been mandatory in dental practices since 1 October
 2025, there are more than 5.5 million electronic dental bonus booklets (eZahnbonusheft) in the ePA [12]
 and the Forschungsdatenzentrum Gesundheit has been operating since 9 October 2025 [13].

 Infographic 1 · Five markets facing the EHDS: key figures and institutional status

What this means for Software in a Box and its partners
The analysis allows commercial entry to be prioritised. Spain and the Netherlands are the markets where a
private federated space adds the most value, because data is fragmented in private software and there is strong
private pressure —chains, insurers, funds— to share and compare data. Germany is a complement market: you
do not compete with the ePA, but sell data quality, compliance and federated analytics to chains, investor-owned
centres (iMVZ) and software vendors. Belgium and Denmark are institutional alliance markets, where the value
lies in projects with the data authority to bring in adults and private clinics.

In every case the vehicle is the same: a data space connector built into clinical software and deployed on
Microsoft Azure by integrators and partners, allowing each clinic to contribute data to specific use cases —quality
across clinics, artificial intelligence on dental imaging, evaluation of prevention programmes, evidence for
industry— without moving health records out of its control.

 The window of opportunity is concrete: between the designation of the access bodies (26 March 2027) and
 the start of most secondary use rules (26 March 2029) there are two years to connect clinics and chains.
 Whoever reaches 2029 with an operational federated dental space will be the natural counterpart of the
 HDABs.

Main recommendations
 - Close two pilots with dental chains before March 2027 —one in Spain and one in the Netherlands— through
 Azure partners, focused on comparable quality indicators across clinics.
 - Design the connector from the start with the European electronic health record exchange format (EEHRxF)
 and HealthDCAT-AP metadata, so that every dental dataset can be catalogued by HDABs.
 - Propose to chains and insurers the trusted data holder status provided for in Article 72 of the Regulation,
 which reduces the burden of each access request [14].
 - Position the dental imaging module (X-rays and CBCT) as a product line for 2029-2031, when medical images
 join the priority exchange categories.
 - In Germany, enter through a dental practice software vendor; in Belgium and Denmark, through projects
 with the Health Data Agency and Sundhedsdatastyrelsen.

1. Purpose, scope and methodology

1.1. Purpose of the study
The study answers three questions. First: how are the dental clinic markets of Spain, Belgium, the Netherlands,
Denmark and Germany similar and different, and what constraints do they place on an oral health data space?
Second: what national rules govern health data in each country today and how are they adapting to the EHDS?
Third: which market needs and regulatory needs can be linked to specific mechanisms of Regulation (EU)
2025/327, so that a federated dental data space is presented as a compliance tool and not just a technology
project?

The document is intended for three audiences: the Software in a Box team; Microsoft Azure partners and
technology integrators who can add the solution to their offering; and sector stakeholders —dental chains,
insurers, professional colleges and associations— with whom those partners will work.

1.2. Scope
The analysis covers five dimensions per country: structure of the health system and funding of dental care;
structure of supply (professionals, practices and chains); digital health infrastructure and the degree of dentist
integration; national regulatory framework and status of adaptation to the EHDS, including the data access body;
and the approach —explicit or implicit— to oral health data in public policy.

The analysis of treatment prices and fees has been deliberately excluded, as it does not affect data architecture,
as has the detail of professional regulation (specialties, continuing education) except where it affects data
availability.

1.3. Methodology and sources
The study is based on public sources consulted in November 2026: the text of the Regulation and European
Commission documentation; the country chapters of the Council of European Dentists (CED) Manual of Dental
Practice 2026, which provide consistent figures on professionals and funding; official national sources (ministries,
statistical institutes, health data agencies, public insurers and parliaments); analysis by specialised law firms; and
trade and business press for market data (consolidation, chains, transactions). References are cited using the
notation [Rn] and listed in Annex D.

Where sources give figures for different years, the reference year is indicated. Comparisons between countries
should be read with caution: public funding indicators are not homogeneous (share of spending, total
reimbursement or coverage by age group) and are presented as published by the sources.

 The readiness assessments by country and the opportunity matrix (chapter 8), the location of dental data by
 country, the risk matrix and the roadmap are Software in a Box analytical work and not official
 measurements. They are flagged as such in each piece.

2. The European Health Data Space: what changes for dentistry

2.1. What the EHDS is
Regulation (EU) 2025/327 of 11 February 2025 on the European Health Data Space was published in the Official
Journal of the EU on 5 March 2025 and entered into force on 26 March 2025 [15][16]. It is the Union's first
common data space dedicated to a specific domain and stems from the European Strategy for Data [17]. Its
architecture rests on two pillars:

 - Primary use: the use of electronic health data to provide healthcare. The Regulation strengthens people's
 rights —to access their data immediately and free of charge, to insert information, to restrict access by
 professionals and to know who has accessed it— and requires certain priority categories of data to be
 exchanged in a common European format [15].
 - Secondary use: the reuse of that data for research, innovation, policy-making, statistics or training, through
 health data access bodies (HDABs) that grant permits and require data to be processed in secure
 environments [15][14].

 Infographic 2 · Actors and infrastructures of the EHDS in three layers

A third block is added, less visible but decisive for the dental sector: a harmonised framework for electronic
health record (EHR) systems, with common interoperability and logging components and a conformity regime
for manufacturers [17].

2.2. A phased timeline
The Regulation applies in phases. The general date of application is 26 March 2027, by which Member States
must have designated their digital health authorities and HDABs [16]. On 26 March 2029 the exchange of the
first group of priority categories begins —patient summaries and ePrescription and eDispensation— together
with most secondary use rules [17][3]. On 26 March 2031 medical images, test results and discharge reports are
added [18]. In parallel, on 7 April 2026 the Commission adopted Implementing Regulation (EU) 2026/771, which
governs the functioning of the EHDS Board [19].

 Infographic 3 · EHDS timeline and national milestones to scale

Table 1 · EHDS milestones and their implications for the dental sector

 Date Milestone of Regulation (EU) 2025/327 Implication for clinics, chains and partners

 05/03/2025 Publication in the Official Journal of the EU [15] The transition period begins; the text is the reference
 for product design.

 26/03/2025 Entry into force [16] Member States start preparing national rules and
 bodies.

 Date Milestone of Regulation (EU) 2025/327 Implication for clinics, chains and partners

 07/04/2026 Implementing Regulation (EU) 2026/771 on the First piece of European governance; more technical
 EHDS Board [19] implementing acts will follow.

 26/03/2027 General date of application: digital health Formal counterparts in each country; the moment to
 authorities and HDABs designated [16] present the dental space as a source.

 26/03/2029 Exchange of patient summaries and The dental space must be catalogued and ready for
 ePrescriptions; application of most secondary use access requests.
 rules [17][3]

 26/03/2031 Medical images, test results and discharge reports Dental imaging (X-rays, CBCT) becomes an exchange
 [18] asset.

 2035 Evaluation of the Regulation [16] Possible review of categories and obligations.

2.3. The dental clinic's two entry doors
The dental clinic relates to the EHDS in two ways. As a healthcare provider, it generates health records that
patients are entitled to consult and which, insofar as they include priority categories, must be exchangeable in
the European format. As a data holder, it may be called upon to make data available to HDABs for secondary
uses, with the safeguards of the Regulation.

 Infographic 4 · Primary and secondary use read from the dental practice

Three elements are particularly relevant for dentistry:

 - Priority categories. The dental record is not a category in its own right, but several of its contents fit the
 planned categories: the patient summary (allergies, medication, history relevant to dental treatment),

 ePrescription and, from 2031, medical images. In our reading, intraoral X-rays, panoramic radiographs and
 cone-beam computed tomography (CBCT) are medical images for the purposes of the Regulation, which will
 turn dental imaging into an asset for exchange and reuse.
 - EHR systems. Dental practice software that processes priority categories will be subject to the
 interoperability and logging requirements for EHR systems. In the Netherlands, the forthcoming Wet GIS
 replaces third-party certification with manufacturer self-assessment in a European testing environment [9],
 which illustrates where conformity is heading.
 - Prohibited uses. Article 54 prohibits using data obtained through secondary use for advertising or for
 decisions detrimental to individuals [14]. For a sector with a strong commercial component, this prohibition
 is both a limit and an argument for trust.
The diagram below summarises how a piece of dental data reaches a user under the EHDS: no data leaves the
clinic without a permit from the access body and, once granted, the analysis takes place in a secure environment
from which only anonymous or aggregated results come out.

 Infographic 5 · Journey of a secondary use request for dental data

2.4. The clause that may leave the dentist out: Article 50
Article 50 provides that data holder obligations regarding secondary use do not apply to natural persons or
microenterprises, unless the Member State decides to extend them in its national legislation [1][14]. Most
European dental practices are small: in the Netherlands, for example, a Rabobank sector analysis from the last
decade estimated that 58% of practices were single-handed [8]. If States do not use the option to extend the
obligations, most dental data will not reach the HDABs through the mandatory route.

The Regulation does, however, offer two routes that a federated space can use. The first is voluntary
participation: nothing prevents exempt clinics from making data available through an intermediary. The second is
the trusted data holder (Article 72), which allows a designated entity to handle access requests that concern
only its own data, easing the burden on the HDAB [14]. For a dental chain with hundreds of clinics, or an insurer
with its own network, it is a particularly suitable route.

 Infographic 6 · Why dental data may be left out of the EHDS and how to prevent it

2.5. Implementation status
One year after entry into force, all Member States are working on the designation of their bodies. The guidelines
of the TEHDAS2 Joint Action —on fees, penalties, data access and data access application management systems
(DAAMS)— have been put to consultation in successive waves in 2025 and 2026 [9]. The five countries analysed
show very different levels of progress, detailed in the following chapters: Germany already operates a research
data centre and an access coordination office; Belgium has its agency created by law and an operational
catalogue; Denmark has reorganised its digital governance into a new entity; the Netherlands has consulted on
the law creating its authority; and Spain is preparing a Digital Health Act while its National Health Data Space is
already running.

3. Spain

3.1. Health system and funding of dental care
Spain has a universal National Health System (SNS), funded by taxes and managed by the autonomous
communities. Dentistry is the great exception to that universality: public coverage is essentially limited to
emergencies, extractions and basic care, and the CED estimates that 97% of dental care is paid directly by the

patient [2]. Voluntary insurance covering additional dental care reaches only 1-2% of the population, although
one in five people has some form of private health insurance [2].

The Oral Health Plan approved in June 2022, with a budget of €68 million, extended the common benefit
package for all beneficiaries to some services —treatment of acute infections, extractions— and expanded
benefits for children aged 0 to 14, pregnant women and people with disabilities or head and neck cancer [2]. It is
a significant step, but it does not change the essentially private nature of the sector.

3.2. Structure of the dental clinic market
Spain has the most dentists in the group analysed, in both absolute and relative terms. According to the INE,
there were 43,672 registered dentists in 2025, 1.9% more than the previous year; 59.9% are women and the
highest concentrations are in Madrid (9,707), Catalonia (6,507) and the Valencian Community (4,852) [20]. The
CED puts the number of active dentists at 41,558 in 2024, equivalent to 87.3 per 100,000 inhabitants [2]. The
General Council of Dentists warns of possible oversupply, with about 2,000 new graduates a year [20].

Supply is almost entirely private: an analysis by the University of Granada put private practice at around 97%, in
more than 23,000 registered clinics [21]. Alongside the independent practice, which remains the majority, the
market has undergone intense consolidation. DONTE Group —owned by the Canadian fund OTPP— ended 2025
with 440 owned clinics, 407 of them under the Vitaldent brand, and almost 750,000 diagnoses performed [22].
Health insurers (Sanitas, Adeslas, Asisa, DKV, Caser) have developed their own dental networks, and operators
such as Vivanta and Institutos Odontológicos complete a chain segment that is already a major stakeholder.

3.3. Digital health infrastructure
In public healthcare Spain starts from a favourable position: the SNS digital health record and interoperable
ePrescription form a base that is already deployed, and all autonomous communities are connected to
MyHealth@EU or in testing [3]. The National Health Data Space (ENDS) has had its own portal since February
2026, with more than 330 datasets published in its catalogue and a federated model in which sources keep
control and data are provided on request in secure environments [3].

The problem for dentistry is that all this infrastructure belongs to the public system. The dental records of the
vast majority of patients reside in the practice software of private clinics and chains, with no connection to the
SNS health record or the ENDS. The challenge of public-private interoperability is explicitly listed among the five
challenges the Government's own data portal identifies ahead of 2029 [3].

3.4. Regulatory framework and adaptation to the EHDS
On 22 September 2025 the Ministry of Health opened the prior public consultation on the draft Digital Health
Act, which will adapt Spanish law to the EHDS Regulation and regulate the interoperable digital health record
and the use of digital technologies in care [4]. The consultation proposed regulating an interoperable health
record across the whole country and including private providers [3], a critical point for the dental sector.

For secondary use, the draft provides for regional health data access bodies and a national body, whose
functions will be taken on by the Ministry of Health, coordinated with each other and integrated into the
European HealthData@EU infrastructure [4]. This multi-level design is consistent with the division of powers, but
it means a dental data space must deal with several bodies.

At the date of this study, the sources consulted do not record approval of the draft by the Council of Ministers.
The reference framework therefore remains the GDPR and Organic Law 3/2018 on data protection, Law 41/2002
on patient autonomy and regional health record legislation.

3.5. Approach to oral health data
Spain has no national oral health register comparable to Denmark's. Population information comes from periodic
surveys and regional child dental care programmes, whose data stays with the regional health services. Private
data —by far the most abundant— is fragmented across thousands of clinics and several dozen chains and
insurers, each with its own software. In practice, the approach is sectoral and private, with no public piece to
bring it together.

Table 2 · Spain fact sheet

 Indicator Value Source

 Registered dentists (2025) 43,672 (+1.9%); 59.9% women [20]

 Active dentists (2024) 41,558 · 87.3 per 100,000 inhabitants [2]

 Dental spending paid by the patient 97% [2]

 Oral Health Plan (2022) €68M; benefits extended to ages 0-14, pregnant women [2]
 and other groups

 Leading chain DONTE Group: 440 owned clinics (407 Vitaldent) at end [22]
 of 2025

 National Health Data Space Portal operational since Feb. 2026; 330+ datasets [3]

 EHDS adaptation law Draft Digital Health Bill; public consultation from [4]
 22/09/2025

 Planned access bodies One national (Ministry of Health) and regional ones [4]

 Infographic 7 · Spain: key indicators of the dental market and its readiness for the EHDS

3.6. Market needs and regulatory needs
Market needs
 - Differentiation through quality. In a market at risk of oversupply and with strong price competition, chains
 and insurers need comparable quality indicators across clinics to defend their value proposition and their
 relationship with patients.
 - Trust after the crises of large chains. The sector still carries the reputational impact of the collapse of
 Dentix, some of whose clinics were taken over by Vitaldent [22]; transparency on clinical outcomes is a
 commercial asset.
 - Network management for insurers. Insurers with their own or contracted dental networks need consistent
 data to manage costs and outcomes, without centralising identifiable records.
 - Data for innovation. Manufacturers of implants, materials and artificial intelligence solutions need
 real-world evidence that they cannot currently obtain in an orderly way.

Regulatory needs
 - Inclusion of the private sector in the interoperable health record envisaged by the Digital Health Act, with a
 format and timeline that dental software can meet.
 - Decision on Article 50: whether or not Spain extends data holder obligations to microenterprises; in either
 case an aggregated participation channel is needed.
 - Coordination between regional and national bodies so that a dental dataset from a chain operating in
 several regions can be requested only once.

3.7. Value of a dental data space and opportunity for partners
Spain is the market where a federated oral health data space adds the most distinctive value: the data exists, it is
abundant and it has owners with incentives to share it under control, but no infrastructure brings it together. The
recommended sequence is to start with the internal use case of a chain or insurer —comparable quality
indicators across its clinics—, which funds the deployment of the connector, and then extend the federation to
independent clinics through professional colleges or insurer networks. Once the national and regional bodies are
operational, the dental space can be presented as a catalogued source.

For Microsoft Azure partners, the proposition fits Azure's penetration of the Spanish private healthcare sector
and the requirement for data residency in the EU. Software in a Box brings experience from the SEDIA-funded
data space demonstrators —in particular Global Data Care, in health— and its own Eclipse-based connectors.

4. Belgium

4.1. Health system and funding of dental care
Belgium has compulsory health insurance covering 99% of residents, funded mainly by payroll contributions and
managed through sickness funds that apply common rules, fees and reimbursements [23]. The National Institute
for Health and Disability Insurance (INAMI/RIZIV) is the central piece. Unlike Spain, a significant share of
dentistry goes through public reimbursement: INAMI reimbursed just over €1 billion in dental care in 2021 and
€1.6 billion in 2025, an increase of more than 50% against 16% growth in the number of treatments [5].

The relationship between dentists and sickness funds is organised through national dento-mutualist agreements
that set maximum fees. The 2026-2027 agreement, signed in December 2025 and published in February 2026,

has been joined fully or partially by 60.48% of dentists, compared with 56.97% for the previous agreement [24];
in 2024, 50.4% of the 7,869 registered practising dentists had rejected the agreement then in force [5].

4.2. Structure of the dental clinic market
The CED puts the number of active dentists at 8,479 in 2023, equivalent to 71.7 per 100,000 inhabitants [23].
General dental practice requires working within the INAMI system after one year of vocational training, with
places limited to 170 by federal decree [23]. The country has 514 active orthodontists and 205 periodontists and
only 452 dental hygienists, a profession still developing [23].

Consolidation is more recent than in Spain or the Netherlands, but it has reached the regulatory agenda: the
Dental Council (Conseil de l'Art dentaire / Raad van de Tandheelkunde) issued a specific opinion in November
2025 on commercial dental chains and their effect on the profession [25]. European groups such as Colosseum
Dental operate in the Benelux.

4.3. Digital health infrastructure
Belgium has a federal eHealth platform underpinning online health services and a citizen portal (MaSanté / Mijn
Gezondheid). The 2026-2029 interfederal eHealth action plan, successor to the 2025-2027 plan, focuses on
operationalisation and synergies between projects [26]. For dentists, INAMI has granted since 2016 a telematics
bonus linked to the use of telematics and electronic record management [26], which has encouraged the
digitalisation of practices.

4.4. Regulatory framework and adaptation to the EHDS
The Health Data Agency (HDA) was created by the Act of 14 March 2023, in force since 13 April 2023, and was
officially launched on 17 January 2024 [6]. Its mission is to facilitate the secondary use of health data in a
uniform, transparent and secure way. The HDA has built a national metadata catalogue with more than 480
datasets and a data access application management system (DAAMS), and accepts requests for catalogued data
and open requests for data not yet listed [6].

The HDA is expected to act as the coordinating HDAB and national contact point, as an interfederal institution
and in collaboration with the Information Security Committee as the permit-granting entity; the designation still
requires political approval at interministerial level [6]. The agency itself acknowledges that it still has to open
dialogue with independent providers and smaller organisations, and that the cross-border connection to
HealthData@EU will not be activated before March 2029 [6].

4.5. Approach to oral health data
The Belgian approach is that of a payer: the best-structured dental data is generated by billing reimbursable
services to the sickness funds and INAMI. That data is valuable for reimbursement policy, but it does not capture
the full health record or non-reimbursed treatments. The last national oral health data collection took place in
2012-2014 and has not been repeated since [27], leaving an epidemiological gap.

Table 3 · Belgium fact sheet

 Indicator Value Source

 Active dentists (2023) 8,479 · 71.7 per 100,000 inhabitants [23]

 Compulsory insurance coverage 99% of residents [23]

 INAMI reimbursement for dental care ≈€1,000M (2021) → €1,600M (2025) [5]

 Indicator Value Source

 Adherence to the 2026-2027 60.48% of dentists [24]
 dento-mutualist agreement

 Health Data Agency Law of 14/03/2023; launched on 17/01/2024 [6]

 HDA national catalogue 480+ datasets and DAAMS system [6]

 Last national oral health data collection 2012-2014 [27]

 eHealth plan Interfederal action plan 2026-2029 [26]

 Infographic 8 · Belgium: data journey of a dental service

4.6. Market needs and regulatory needs
Market needs
 - Evidence on spending. Dental reimbursement growing faster than treatment volume requires data
 explaining the evolution of cost per patient and per type of treatment.
 - Up-to-date epidemiological surveillance, given the absence of a national oral health survey since 2014.
 - Positioning of chains in the face of scrutiny by the professional regulator: transparency on outcomes is a
 response to the debate opened by the 2025 opinion.

Regulatory needs
 - Formalise the governance of the HDA as HDAB, which the agency itself identifies as a priority.
 - Bring independent providers —including dental practices— into the data holder ecosystem, with low
 administrative burden mechanisms.
 - Develop intermediary entities: the HDA is exploring hospital data networks as intermediaries and envisages
 trusted data holders to ease the burden on the HDAB, following the experience of Findata in Finland [6].

4.7. Value of a dental data space and opportunity for partners
In Belgium the federated space does not compete with INAMI: it completes the 'no' branch, that is, the
non-reimbursed treatments and the full health record that today remain in each practice's software. The value
proposition matches the HDA's stated need to reach independent providers and to have intermediaries and
trusted holders. The recommended channel is a joint project with the HDA and bilingual professional
associations, delivered by Azure integrators present in Brussels and Flanders. Software in a Box has an office in
Brussels, in the European quarter, which makes this dialogue easier.

5. The Netherlands

5.1. Health system and funding of dental care
The Netherlands has a decentralised system with compulsory basic insurance. Dental care for under-18s is
included in basic insurance —check-ups, cleaning, fluoride, periodontal treatment, root canals, fillings and some
surgical treatments—, while adults mostly rely on voluntary supplementary insurance [28]. The public system
covers 33% of the cost of dental care (OECD, 2023), compared with 83% of total health spending covered by the
State and social insurance [28]. Maximum fees are set by the health authority NZa.

5.2. Structure of the dental clinic market
In January 2025 the country had 9,555 active dentists, 53 per 100,000 inhabitants, the lowest density in the
group together with Germany [28]. The shortage is structural: according to the professional association KNMT,
too few dentists have been trained for years, and around a quarter of practising dentists trained abroad; there
are 2,287 dentists with a foreign degree, and in Zeeland they are more than half [7]. About 30% of practices do
not accept new patients [8].

The second force is consolidation. A 2025 study by the association Bevlogen Tandartsen identified more than
500 practices owned by private equity, around 13% of the total, with an estimated 30% share of revenue, and
more than 21 active chains [8]. ABN AMRO estimated that 13% of some 4,400 practices belonged to a chain [8].
The competition authority ACM reviews deals such as the integration of Top Mondzorg and other groups, and
Parliament has debated motions on private equity in healthcare [8].

5.3. Digital health infrastructure
The reference legislation is the Wegiz (Electronic Data Exchange in Healthcare Act), which requires certain
prioritised datasets to be exchanged electronically according to quality and information standards. Its priority
exchanges —basic data set (BgZ), urgent care, medication transfer, image availability and nursing transfer—
resemble the EHDS categories, but are not identical [9]. Nictiz is the national competence centre for standards.

Dutch legal analysis itself acknowledges a bottleneck: the country does not yet have a fully functioning national
health information system, and the national coverage network (LDN) is central to connecting to the EHDS [9].
Oral health is not among the prioritised Wegiz exchanges.

5.4. Regulatory framework and adaptation to the EHDS
Adaptation is organised through the Wet GIS (Health Information System Act), the first phase of a future
framework law on data processing in healthcare. Its public consultation ran from 28 May to 8 July 2026 [9]. The

law designates the authorities required by 26 March 2027 and sets up the supervisory framework; primary use,
secondary use and EHR systems will be regulated in a second phase [9].

The main institutional innovation is the creation of a Gezondheidsdata Autoriteit (Health Data Authority), an
independent body that will take on the roles of digital health authority for primary use and HDAB for secondary
use, as well as national contact point [9]. Some lawyers question its independence, since it will sit within the
Ministry of Health (VWS), which is also a data holder and data user [9]. The law also replaces third-party
certification of EHR manufacturers with self-assessment [9].

In parallel, Health-RI —a foundation dedicated to the reuse of health data through a national infrastructure—
has been registered by the ACM as a data intermediation service under the Data Governance Act [29], a useful
precedent for private federated models.

5.5. Approach to oral health data
The Dutch approach is that of a regulated market: fees set by the NZa, competition monitored by the ACM and a
strong role for private providers organised in chains. Dental data has no public register of its own and no specific
Wegiz exchange; it resides in practice software and in the systems of chains and insurers.

 Infographic 9 · The Netherlands: the two pressures on the oral health market

Table 4 · The Netherlands fact sheet

 Indicator Value Source

 Active dentists (2025) 9,555 · 53.0 per 100,000 inhabitants [28]

 Public coverage of dental costs (2023) 33%; under-18s in basic insurance [28]

 Foreign-trained dentists ≈25%; 2,287 with a foreign degree [7]

 Indicator Value Source

 Practices not accepting new patients ≈30% [8]

 Private equity practices 500+ (≈13%), ≈30% of turnover; 21+ chains [8]

 EHDS adaptation law Wet GIS; consultation 28/05-08/07/2026 [9]

 Authority and HDAB Gezondheidsdata Autoriteit (primary and secondary use) [9]

 Registered data intermediary Health-RI (Data Governance Act) [29]

5.6. Market needs and regulatory needs
Market needs
 - Productivity with fewer professionals. The shortage requires work to be reorganised between dentists,
 hygienists (about 3,900 in 2022) and assistants [28]; activity and outcome data are essential to do so with
 quality.
 - Post-acquisition integration. Chains buying practices with heterogeneous software need to compare
 indicators without migrating all records at once.
 - Transparency towards the regulator and Parliament, which are closely following the effect of private equity
 on costs and access.

Regulatory needs
 - Add oral health to the data exchange agenda (Wegiz and EHDS), currently focused on hospital, primary and
 pharmaceutical care.
 - Guarantee the operational independence of the new health data authority.
 - Develop the second phase of the law (secondary use and EHR systems) in time for 2029.

5.7. Value of a dental data space and opportunity for partners
The Netherlands is, together with Spain, the priority opportunity market. The natural customers are private
equity-backed chains and their technology integrators: the federated space offers them benchmarking across
practices today, without costly migrations, and a route to connect to the Gezondheidsdata Autoriteit tomorrow.
The precedent of Health-RI as a registered data intermediary makes it easier to explain the model to regulators.
For selling through partners, a Dutch version of the sales material and the presentation video is a requirement.

6. Denmark

6.1. Health system and funding of dental care
Denmark has a national health service funded by general taxation. In dentistry the system is dual. Children and
young people receive free dental care from the municipal dental service; coverage, which spanned ages 0 to 20
from 2023, was extended to ages 0-21 from 2025 [10]. Adults, by contrast, receive a public subsidy of only about
15%; adult dental care accounts for 31% of all out-of-pocket health payments in the country, and 42% of the
population has supplementary insurance that can cover up to half of the remaining cost [10].

6.2. Structure of the dental clinic market
In 2025 Denmark had 4,964 active dentists —8,808 registered—, i.e. 83.2 per 100,000 inhabitants, and 2,471
dental hygienists in 2022 [10]. According to the OECD, it is the only EU country where the number of dentists per
inhabitant fell over the period analysed in its 2024 report [30]. Child care is mostly provided in municipal clinics,
often located in schools, with public subsidy for care in private practices where there are no public clinics [11].

Adult practice is private and regulated by the dental agreement (tandlægeoverenskomst) negotiated between
the regions and the dental association, which includes ownership restrictions that limit the expansion of chains
[31]. Even so, chains have grown: by 2022 one in three adults was already using a dental chain [31], and
Colosseum Tandlægerne, part of the European Colosseum group, operates around 26 clinics in the country.

6.3. Digital health infrastructure
Denmark is a European reference in digital health, with the sundhed.dk portal and a long tradition of national
registers. The health reform has driven a new organisation: since 1 January 2026 the preparatory entity Digital
Sundhed Danmark has been operating, bringing together sundhed.dk, MedCom, the Danish Health Data
Authority (Sundhedsdatastyrelsen) and various regional IT tasks [32]. Denmark is connecting to the European
eHealth Digital Service Infrastructure (eHDSI) as part of its EHDS preparation [32].

For secondary use, a Health Data Gateway is being developed: a single entry point to data from registers,
biobanks and clinical sources, supported by a DKK 200 million grant from the Novo Nordisk Foundation; the
sources consulted describe it as still in development [33].

6.4. Regulatory framework and adaptation to the EHDS
Dentistry is regulated by the Danish Health Authority (Sundhedsstyrelsen), which administers the legislation, and
by the Danish Patient Safety Authority, which grants authorisations and recognises specialists [10]. Institutional
adaptation to the EHDS is taking place through the reform of digital governance —Digital Sundhed Danmark—
and Sundhedsdatastyrelsen's projects on MyHealth@EU and secondary use [32]. The sources consulted do not
yet confirm the formal designation of the Danish HDAB, so this study treats it as a process under way. Denmark
also takes part in Nordic cooperation on the secondary use of health data (VALO project) [32].

6.5. Approach to oral health data
Denmark is the only country in the group with a long-standing national oral health register: SCOR (the Danish
Health Authority's Central Odontological Register), created with free child dentistry in 1972, which systematically
records the check-ups of children and young people in a standardised way [11]. Municipal services are required
to report their data to SCOR, and the register has made it possible to monitor oral health at municipal, regional
and national level for more than five decades [11]. It is the best available demonstration that well-structured
public oral health data produces useful policy.

Table 5 · Denmark fact sheet

 Indicator Value Source

 Active dentists (2025) 4,964 · 83.2 per 100,000 inhabitants [10]

 Free care Ages 0-21 since 2025 [10]

 Adult subsidy ≈15%; 42% with supplementary insurance [10]

 Dental hygienists (2022) 2,471 [10]

 National dental register SCOR, since 1972 (children and young people) [11]

 Indicator Value Source

 Digital governance Digital Sundhed Danmark (preparatory since 01/01/2026) [32]

 Data access Health Data Gateway in development (Novo Nordisk [33]
 Foundation, DKK 200M)

 Adults treated in chains One in three (2022) [31]

 Infographic 10 · Denmark: the data cycle in public child dentistry

6.6. Market needs and regulatory needs
Market needs
 - Visibility of adults. There is no equivalent of SCOR for the adult population, treated in private practices and
 chains.
 - Capacity. With falling dentist density, productivity and the allocation of tasks to hygienists require activity
 data.
 - Differentiation of chains in a framework that limits their growth through ownership.

Regulatory needs
 - Complete the institutional transition to Digital Sundhed Danmark and define the HDAB and the single data
 entry point.
 - Extend the SCOR logic to adults without imposing disproportionate burdens on private practices, which
 requires voluntary or aggregated mechanisms.

6.7. Value of a dental data space and opportunity for partners
In Denmark the federated space does not have to prove the value of oral health data: SCOR has already done so.
Its value lies in bringing that logic to the adult population and private clinics, connecting chains and practices
through a federated model compatible with the new governance. The recommended channel is institutional
—projects with Sundhedsdatastyrelsen or the regions— supported by Danish Azure integrators already validated
by Software in a Box.

7. Germany

7.1. Health system and funding of dental care
Germany combines statutory health insurance (GKV), covering around 88% of the population, with substitutive
private insurance (PKV) for 11% [34]. Dentistry is widely integrated into statutory insurance: 65% of dental
spending is covered by statutory insurance (2023), and dental spending equals 0.7% of GDP [34]. The National
Association of Statutory Health Insurance Dentists (KZBV) defines the benefit catalogue together with the funds,
and the German Dental Association (BZÄK) brings together the 17 regional chambers [34].

7.2. Structure of the dental clinic market
The CED puts the number of active dentists at 43,663 in 2024 —out of 103,998 registered—, i.e. about 52 per
100,000 inhabitants [34]. The independent practice predominates, but consolidation is advancing through
medical care centres (MVZ). According to the KZBV and BZÄK, investor-owned MVZs (iMVZ) accounted for
30.4% of all dental MVZs in the third quarter of 2023, with a rising trend; the profession is calling for limits on
their expansion [35]. They are concentrated in large cities and in regions with patients willing to pay
supplements.

7.3. Digital health infrastructure
In 2025-2026 Germany made the most visible leap in the group. The 'ePA für alle' —an electronic health record
for all statutorily insured people, with an opt-out model— started in pilot regions on 15 January 2025, was
opened nationwide on 29 April 2025 and has been mandatory for all dental practices since 1 October 2025 [12].
By April 2026 the funds had created an ePA for almost 73 million of the just over 74 million insured, there were
more than 5.5 million electronic dental bonus booklets (eZahnbonusheft) accessible in the ePA, and up to
93,000 medical and dental practices were accessing their patients' ePA every week [12].

Dental telematics also has its own components, such as the electronic application and approval procedure (EBZ),
in production nationwide since 1 January 2023 [36]. The KZBV stresses, however, that in dental practices the ePA
is used mainly for medical history taking and that there are fewer mandatory document upload cases than in
medicine [12].

7.4. Regulatory framework and adaptation to the EHDS
Germany has brought forward much of the secondary use architecture with the Health Data Use Act (GDNG).
The Forschungsdatenzentrum Gesundheit (FDZ Gesundheit), the research data centre of the Federal Institute
for Drugs and Medical Devices (BfArM), began accepting applications on 9 October 2025 and is designed as the
piece that will connect Germany to the EHDS [13]. BfArM's Data Access and Coordination Office (DACO/DAKO)
will act as coordinating HDAB, with domain-specific access bodies [13]. Connection of the ePA to the FDZ for
secondary use of its data is planned for the end of 2026 [37].

On 15 July 2026 the Federal Government approved the draft Act on Promoting Data and Digital Innovation in
Healthcare (GeDIG), which sets the framework for data reuse across the entire health system and implements
the EHDS building on existing infrastructure [37].

7.5. Approach to oral health data
The German approach is institutional and integrated: dental data flows through the public telematics
infrastructure, KZBV billing generates detailed statistics —published annually in its Jahrbuch— and the ePA
includes a dental component of its own, the eZahnbonusheft. It is the country where oral health data is closest to
reaching the HDAB through the public route.

 Infographic 11 · Germany: value chain of dental data and contribution of a federated space

Table 6 · Germany fact sheet

 Indicator Value Source

 Active dentists (2024) 43,663 · 52 per 100,000 inhabitants [34]

 Share of dental spending covered by 65%; GKV ≈88% of the population [34]
 statutory insurance (2023)

 ePA in dental practices Mandatory since 01/10/2025 [12]

 ePAs created / eZahnbonusheft ≈73 million / 5.5+ million (Apr. 2026) [12]

 EBZ procedure In production since 01/01/2023 [36]

 FDZ Gesundheit (BfArM) Applications since 09/10/2025; DACO as coordinating [13]
 HDAB

 Indicator Value Source

 EHDS adaptation law GDNG in force; GeDIG approved by the Government on [37]
 15/07/2026

 iMVZ as a share of all dental MVZs 30.4% (Q3 2023) [35]

7.6. Market needs and regulatory needs
Market needs
 - Reducing the bureaucratic burden. The KZBV complains that administrative tasks arising from regulation
 weigh on the daily running of practices [35]; any solution must save time, not add to it.
 - Management of iMVZ networks under political scrutiny, with a need to demonstrate quality and
 contribution to care.
 - Data for software and industry: dental practice software vendors must meet interoperability and
 conformity requirements.

Regulatory needs
 - Parliamentary passage of the GeDIG and alignment of the coordinating HDAB with the domain bodies.
 - Effective ePA-FDZ connection and definition of which dental contents are reused.
 - Regulation of iMVZs, demanded by the profession.

7.7. Value of a dental data space and opportunity for partners
In Germany you do not compete with the ePA or the FDZ. The opportunity lies in the missing pieces: certifiable
connectors for dental practice software, format and data quality validation before upload, federated analytics for
chains and iMVZs that need to compare outcomes across centres, and catalogues with standardised metadata.
The recommended channel is an agreement with a dental software vendor or an Azure integrator specialising in
health telematics.

8. Comparative analysis

8.1. Correlation between professional density and public funding
Comparing the five countries reveals a striking relationship: the countries with the most dentists per inhabitant
are those where adults pay out of pocket. Spain (87.3 per 100,000) and Denmark (83.2) lead on density and
have, respectively, 97% private spending and an adult subsidy of around 15%; Germany (52) and the Netherlands
(53) have the lowest density and, in the German case, the highest public coverage (65%). Belgium sits in between
on both axes.

With only five observations, the relationship is indicative, not statistical. But its consequence for data
architecture is clear: where spending is private, dental data does not reach the public system by itself, because
it does not go through public billing or the system's health record. In those markets, a federated space is the
condition for the data to exist at scale.

 Infographic 12 · Dentist density and adult funding model

Table 7 · Comparison of dental clinic markets

 Dimension Spain Belgium The Netherlands Denmark Germany

 Active dentists 41,558 (2024) 8,479 (2023) 9,555 (2025) 4,964 (2025) 43,663 (2024)

 Per 100,000 inhabitants 87.3 71.7 53.0 83.2 52

 Funding of dental care 97% out of pocket INAMI 33% public Free 0-21; adults 65% public
 reimbursement ≈15%
 €1,600M (2025)

 Supply structure Almost 100% Contracted Shortage; ≈13% Municipal for Practice + MVZ;
 private; chains and practice; debate on PE-owned children; private for iMVZ 30% of MVZs
 insurers chains adults

 Key trend Oversupply and Rising spending Consolidation and Falling density Mandatory
 consolidation shortage digitalisation

 Approach to oral health data Sectoral and Payer-driven Regulated market Public register Institutional and
 private integrated

8.2. Differences in the approach to oral health data
Each country has developed a different approach to dental data, which shapes the form a data space must take:

 - Spain: sectoral and private. Data is abundant but fragmented in private software; there is no public piece to
 bring it together.
 - Belgium: payer-driven. The best-structured data is INAMI billing; the full health record and up-to-date
 epidemiological surveillance are missing.
 - The Netherlands: regulated market. Chains and insurers concentrate the data; exchange regulation does
 not yet include oral health.

 - Denmark: public register. SCOR has structured child data since 1972; adults are left out.
 - Germany: institutional and integrated. Dental data flows through telematics and the ePA; the challenge is
 quality, reuse and the integration of iMVZs.
The practical consequence becomes clear when crossing countries and repositories: the only source of dental
data present with intensity in all five markets is each clinic's practice software.

 Infographic 13 · Where oral health data resides today in each country (analytical assessment)

8.3. Regulatory comparison
Table 8 · Comparison of health data regulation and governance

 Element Spain Belgium The Netherlands Denmark Germany

 EHDS adaptation rule Draft Digital Health HDA Law 2023; Wet GIS Health reform and GDNG; GeDIG
 Bill (consultation transposition (consultation 2026) Digital Sundhed (Government,
 2025) pending Danmark 07/2026)

 Secondary use body National (Health Health Data Agency Gezondheidsdata Sundhedsdatastyrel DACO (BfArM) +
 Ministry) + regional (designation Autoriteit sen; Health Data domain bodies
 pending) Gateway

 Operational infrastructure ENDS: 330+ Catalogue of 480+ Health-RI; LDN National registers; FDZ Gesundheit
 datasets datasets; DAAMS network in eHDSI operational
 development

 Health record / primary use HCDSNS and eHealth platform; Wegiz; no complete sundhed.dk ePA for all (opt-out)
 ePrescription MaSanté national system

 Dentist integration Low (private sector) Medium (INAMI Medium-low High for children; High (mandatory
 billing) low for adults ePA)

 Specific treatment of dental No No No SCOR (children) eZahnbonusheft in
 data the ePA

 Infographic 14 · Milestones of institutional adaptation to the EHDS by country, 2023-2027

The table and the timeline show that the five countries have chosen different institutional models for secondary
use: a newly created specialised body (Belgium), a single authority for primary and secondary use (the
Netherlands), an office within a medicines agency with domain bodies (Germany), a multi-level regional and
national structure (Spain) and integration into a new national digital entity (Denmark). None of them, in the
sources consulted, provides for specific treatment of oral health data.

8.4. Readiness map and opportunity matrix
To summarise the comparison, this study assesses six readiness dimensions on a scale of 1 to 4. This is an
analytical assessment based on the sources in the previous chapters, not an official measurement.

Three readings stand out. First, Germany is the only country with high readiness in almost every dimension,
which reduces the room for a new player but increases demand for compliance. Second, Spain has solid public
digital infrastructure but the lowest level of dentist integration and public funding, creating a gap that can only
be closed from the private sector. Third, the structured dental register is the dimension with the lowest average
and is at a low level in three of the five countries: it is exactly the gap an oral health data space is meant to fill.

 Infographic 15 · Readiness map by country and dimension (analytical assessment)

The matrix combines two axes: the degree of integration of dental data into public infrastructure and private
pressure —consolidation, insurers, funds— to share and compare data. Spain and the Netherlands occupy the
priority opportunity quadrant; Germany, the complement quadrant; Belgium and Denmark, the institutional
alliance quadrant.

 Infographic 16 · Opportunity matrix: public integration versus private pressure to share data

8.5. Cross-cutting market constraints
Beyond national differences, five constraints run across all five markets and must guide the design of any dental
data space.

1. Practice size. The independent practice remains the dominant form of practice in all five countries. Its size
exempts it by default from data holder obligations (Article 50) and limits its capacity to take on technology
projects of its own. Any solution must be deployable without technical staff in the clinic and at a very low
marginal cost per participating practice.

2. Regulation of ownership and capital. The entry of investors is the subject of regulatory debate in almost every
market: Denmark keeps ownership restrictions in its dental agreement [31]; in Germany the profession is calling
for limits on iMVZs [35]; in Belgium the Dental Council has issued an opinion on commercial chains [25]; in the
Netherlands the competition authority reviews concentrations and Parliament debates the role of private equity
[8]. A data space that brings transparency on quality and access can become an ally of chains in the face of that
scrutiny.

3. Imbalance in professional supply. Spain faces a risk of oversupply, with about 2,000 graduates a year [20]; the
Netherlands and Denmark face shortages and falling density [7][30]. In both scenarios activity and outcome data
are needed: to differentiate in one case and to redistribute tasks between dentists and hygienists in the other.

 Infographic 17 · Cross-cutting constraints of the dental market and design implications

4. Heterogeneous software. Each country has its own ecosystem of dental practice software, tied to national
billing (sickness funds in Belgium, KZV in Germany, NZa fees in the Netherlands). That link to billing explains why
national vendors dominate and why the connector must adapt to each one, preferably through alliances with the
vendors themselves.

5. Professional and patient trust. The Belgian data agency identifies the perception of 'commercialisation' of
data as a risk to public trust [6]. In dentistry, where the commercial relationship with the patient is direct, that
perception is even more sensitive. Federated architecture, explicit usage policies and the Article 54 ban on
advertising uses are the answer.

9. Market needs, regulatory needs and alignment with the EHDS

9.1. Market needs by country
Table 9 · Market needs by country

 Country Main need Response of the dental data space

 Spain Comparable quality indicators across chain clinics and Internal federation of the chain or insurer; extension
 insurer networks; patient trust to independent clinics via professional colleges

 Belgium Explain rising spending; epidemiological surveillance Complete non-reimbursed data; oral health series
 since 2014 for the HDA and INAMI

 Country Main need Response of the dental data space

 The Netherlands Productivity under shortage; post-acquisition Benchmarking across practices without migrating
 integration of practices records

 Denmark Visibility of adults treated privately and in chains Extend the SCOR logic to adults with voluntary
 participation

 Germany Less bureaucracy; demonstrating iMVZ quality; software Data quality validation, federated analytics and
 conformity connectors for vendors

9.2. Regulatory needs by country
Table 10 · Regulatory needs by country and link to the EHDS

 Country Regulatory need Related EHDS mechanism

 Spain Include the private sector in the interoperable record; Ch. III (EHR systems); Ch. IV (HDAB); Art. 50
 coordinate regional and national bodies; decide on
 microenterprises

 Belgium Formalise HDAB governance; bring in independent Ch. IV; Art. 72 (trusted holders)
 providers; intermediaries

 The Netherlands Independence of the new authority; second phase of the Digital health authority and HDAB; Ch. III
 law; include oral health in Wegiz

 Denmark Complete the institutional transition; define the HDAB and Ch. IV; HealthData@EU
 the single entry point

 Germany Pass the GeDIG; ePA-FDZ connection; regulate iMVZs Ch. IV; priority categories (Art. 14)

9.3. Alignment with Regulation (EU) 2025/327
The value of this analysis for selling through partners is that every need identified already has an EHDS
mechanism that supports it. This makes it possible to present the dental data space not as yet another
technology project, but as a route to early compliance.

 - Interoperability of clinical software. The Chapter III requirements on EHR systems —harmonised
 interoperability and logging components, the European EEHRxF format— give dental software vendors in all
 five countries a common horizon.
 - Patient rights. Articles 3 to 5 —access, access services, insertion of information— turn the portability of the
 dental record between clinics, chains and countries into an enforceable right.
 - Secondary use with control. Chapter IV allows data to reach researchers and innovators through HDAB
 permits and in secure environments, without holders handing over copies.
 - Inclusion of the small clinic. Article 50 leaves the decision on microenterprises to each State; a federated
 space offers a voluntary, aggregated channel regardless of that decision.
 - Burden on chains. Article 72 allows trusted data holders to be designated to handle requests concerning
 their own data.
 - Public trust. Article 54 prohibits advertising or discriminatory uses, a key argument against the perception of
 'commercialisation' of data that also concerns the agencies [6].
 - Dental imaging. The inclusion of medical images in the priority categories in 2031 opens the way to the
 reuse of X-rays and CBCT.

The full mapping between needs and mechanisms is summarised in the following diagram.

 Infographic 18 · Mapping between dental market needs and EHDS mechanisms

For patients, alignment with the EHDS has a very concrete meaning, which is also the easiest argument to explain
to clinics:

 Infographic 19 · Illustrative primary use scenario: patient with a dental emergency in another Member State

9.4. The importance of national participation in the EHDS
The comparison shows that the EHDS sets the framework, but the real value for dental data is decided by
national rules: whether obligations are extended to microenterprises, whether the interoperable health record
includes the private sector, whether the HDAB has the capacity to deal with independent providers, whether
recognised intermediaries exist. In all five countries these decisions are being taken between 2025 and 2027. This
is the moment when professional colleges, chains, insurers and technology providers can influence matters so
that oral health is not left out.

 Positioning recommendation: in each country, Software in a Box and its partners should take part in the
 public consultations and working groups on EHDS adaptation with a concrete proposal for dental data
 —voluntary aggregated participation, trusted holders for chains and common metadata—, backed by a pilot
 already under way.

10. Use cases for the oral health data space
The use cases have been selected for their compatibility with the secondary use purposes permitted by the
Regulation and their capacity to generate recurring revenue for partners.

 Infographic 20 · Six use cases for the oral health data space

1. Quality across clinics. Comparable indicators —treatment success, re-treatments, waiting times, adherence to
check-ups— calculated in a federated way across the clinics of a chain or an insurer network. This is the entry
case: it has a paying customer, does not require an HDAB permit because the data is used within the group itself
on its own legal basis, and prepares the infrastructure for everything else.

2. Artificial intelligence on dental imaging. The dental diagnostic AI market is growing rapidly in Europe: Align
Technology launched in the EU an assisted detection solution for 2D X-rays; Dentsply Sirona announced in May
2026 a CE-marked tool to detect periapical radiolucencies in CBCT; and Colosseum Dental Group, with more than
630 clinics in 11 countries, is piloting AI diagnostic solutions [38]. Federated training and validation make it
possible to improve these models without moving X-rays out of the clinics.

3. Programme evaluation. Child dental care programmes (Spain, the Netherlands, Denmark) and oral health
plans need to measure outcomes with real data, beyond activity.

4. Oral health surveillance. Prevalence of caries, periodontal disease and edentulism by territory, particularly
valuable in Belgium, with no national survey since 2014, and in Spain, with no national register.

5. Evidence for industry. Survival of implants and performance of materials based on real-world data, within the
permitted purposes of product development and innovation and without advertising uses.

6. Oral and systemic health. The relationship between periodontal disease and diabetes, cardiovascular disease
or pregnancy, which requires crossing dental and medical data and is only feasible through HDAB permits.

11. Proposed architecture and the role of Software in a Box

11.1. Why a federated architecture
A central repository would copy identifiable dental records into a single database, with a single point of failure
and a loss of control the sector would not accept. A federated data space leaves the data in each clinic and only
moves metadata, permits and, where applicable, aggregated results or trained models. It is the model behind the
EHDS itself —processing in secure environments, without copies— and the one already used, for example, by
Spain's National Health Data Space [3].

 Infographic 21 · Centralised versus federated architecture

11.2. Components
 - Data space connector based on Eclipse Dataspace Components, built into the practice software or deployed
 alongside it, which exposes catalogues and enforces usage policies.
 - Machine-readable usage policies (ODRL) that translate HDAB permits and agreements between holders
 into executable rules.
 - Catalogue with HealthDCAT-AP metadata, the profile HDABs use to describe datasets [3].
 - Secure processing environment on Microsoft Azure in EU regions, or on the customer's premises when data
 sovereignty requires it.

 - Interoperability layer towards the European EEHRxF format and HL7 FHIR standards for the priority
 categories.

11.3. Role of Software in a Box and its partners
Software in a Box does not intend to sell directly to clinics. Its model is B2B: it provides federated data space
technology and regulatory know-how to Microsoft Azure partners, technology integrators and software
developers, who build it into their solutions for chains, insurers, associations and clinics. Software in a Box's
experience in the SEDIA-funded data space demonstrators —Global Data Care in health, PROCUREDATA in
procurement and EcoDataNet in the circular economy— and in developing its own connectors on Eclipse and
Pontus-X is its main competitive advantage.

 Infographic 22 · B2B collaboration model and partner revenue streams

For the partner, the model offers three revenue streams: the deployment project and integration with the
practice software; recurring operation of the environment on Azure; and value-added services on the use cases
(quality analytics, AI on imaging, support for HDAB requests).

11.4. Compliance framework for the connector
The dental data space is not governed by the EHDS alone. Its design must incorporate from the outset a set of
European rules that apply simultaneously:

 - General Data Protection Regulation (GDPR). Health data is a special category (Article 9) and requires a
 specific legal basis, an impact assessment and enhanced measures [39]. The EHDS complements the GDPR;
 it does not replace it.
 - Data Governance Act (DGA). When a third party brings data holders and users together, it may be a data
 intermediation service subject to notification and neutrality [40]. Health-RI's registration in the Netherlands

 [29] shows how this applies to health; whether the operator of the dental space falls within that category
 should be analysed case by case.
 - Artificial Intelligence Act. AI systems that are medical devices, or safety components of them, subject to
 third-party conformity assessment are considered high-risk [41]. Diagnostic AI on dental X-rays falls within
 that scope, with training data governance obligations that a federated space helps to meet.
 - Medical Devices Regulation (MDR). Software with a diagnostic purpose is a medical device and requires CE
 marking [42]; the data space provides clinical evidence and post-market surveillance.
 - EHDS. Requirements for EHR systems (Chapter III), data holder obligations and the permit procedure
 (Chapter IV), and prohibited uses (Article 54) [15].

 Infographic 23 · European regulatory layers affecting the oral health data space

Table 11 · Regulatory requirements and design response

 Regulation Relevant requirement Response in the dental data space

 GDPR [39] Health data as a special category; legal basis, Data at source; pseudonymisation in the clinic;
 minimisation and impact assessment impact assessment per use case

 EHDS [15] Interoperability of EHR systems; HDAB permits; EEHRxF format; HealthDCAT-AP catalogue; secure
 secure environments; Art. 54 environment on Azure (EU)

 DGA [40] Neutrality and notification of data Analysis of the operator's role; separation between
 intermediation services intermediation and value-added services

 AI Act [41] High risk for AI embedded in medical devices; Traceability of training datasets and federated
 training data governance validation

 MDR [42] CE marking and post-market surveillance of Real-world clinical evidence from the federation
 diagnostic software

12. Roadmap 2026-2031
The roadmap is organised according to the EHDS timeline and the opportunity matrix. It is a Software in a Box
proposal, subject to validation with partners and customers.

 Infographic 24 · Partner roadmap 2026-2031

 - Phase 0 (November 2026 - March 2027): preparation. Dental connector on Azure ready for pilots;
 agreements with partners in Spain and the Netherlands; sales material and videos by language; participation
 in public consultations.
 - Gate 1 (26 March 2027): designation of HDABs. Decide in which countries to seek formal dialogue with the
 access body.
 - Phase 1 (2027-2028): pilots. Quality across clinics with a Spanish chain and a Dutch chain; agreement with a
 software vendor in Germany; project with the Belgian HDA or with Sundhedsdatastyrelsen.
 - Gate 2 (26 March 2029): start of secondary use. The dental space must be catalogued with HealthDCAT-AP
 metadata and with datasets ready for requests.
 - Phase 2 (2029-2031): scale-up. Federation of independent clinics, trusted data holders, connection to the
 access bodies.
 - Gate 3 (26 March 2031): medical images. Launch of the dental imaging module for exchange and reuse.

13. Risks and constraints
Deployment risks have been assessed by probability and impact. The two critical ones are regulatory in nature
and share the same mitigation: start with use cases in which chains share data in their own interest, without
depending on the access bodies' timeline.

 Infographic 25 · Probability and impact matrix of risks (analytical assessment)

Table 12 · Deployment risks and constraints

 Risk Level Mitigation

 Delays in national laws and in the High Start with chains' internal use cases, which do not depend on the HDAB; follow
 designation of HDABs public consultations.

 Microenterprise exemption (Art. High Voluntary, aggregated participation model; trusted holders for chains.
 50) reducing the mandatory
 supply of data

 Professional distrust of the Medium Federated architecture; ODRL policies; highlight the ban on advertising uses
 'commercialisation' of data (Art. 54).

 Heterogeneity of dental practice Medium Enter through software vendors and partners; reusable connectors per country.
 software

 Independence and capacity of Medium Offer well-catalogued datasets (HealthDCAT-AP) that reduce their workload.
 the access bodies

 Political scrutiny of chains and Medium Position the space as a transparency and quality tool.
 private equity (NL, DE, BE)

 Risk Level Mitigation

 Language and commercial culture Low Material and videos per language; local partners.
 in each country

14. Conclusions
Oral health data is one of the great untapped assets of European healthcare, and the EHDS offers for the first
time a common framework to bring it in. But the comparison between Spain, Belgium, the Netherlands,
Denmark and Germany shows that the Regulation alone does not guarantee that dental data will arrive: the
structure of the sector —small practices, private spending, proprietary software— and the microenterprise
exemption may leave it out.

The five countries start from very different approaches: sectoral and private in Spain, payer-driven in Belgium,
regulated market in the Netherlands, public register in Denmark and institutional in Germany. These differences
are not an obstacle but the basis for a differentiated strategy: federate from the private sector where data is
fragmented (Spain and the Netherlands), complement where public infrastructure already channels it (Germany)
and ally with the data authority where the challenge is to bring in adults and private clinics (Belgium and
Denmark).

In every case, each country's participation in the EHDS and the decisions it takes in its national legislation
between 2025 and 2027 will determine whether oral health becomes part of the European space. Software in a
Box and its partners can help make that happen with a concrete proposal, a pilot under way and a federated
architecture that respects professionals' control over their data.

About Software in a Box
Software in a Box is a technology company based in Madrid with an office in Brussels, specialising in federated
data spaces, data sovereignty and proprietary artificial intelligence. Its model is exclusively B2B: it develops the
technology and regulatory know-how that Microsoft Azure partners, technology integrators and software
developers build into their solutions for end customers.

Its experience comes from the federated data space demonstrators funded by SEDIA and delivered between
2024 and 2026: Global Data Care (health), PROCUREDATA (procurement) and EcoDataNet (circular economy and
waste). In them it has developed its own connectors on Eclipse Dataspace Components and Pontus-X, aligned
with the Gaia-X and IDSA frameworks and with ODRL usage policies.

The oral health data space applies that experience to a specific sector, with an architecture on Microsoft Azure
designed for partners to deploy with chains, insurers, professional associations and dental software vendors in
Spain, Belgium, the Netherlands, Denmark and Germany.

 Partner programme: integrators and Microsoft Azure partners interested in adding the oral health data
 space to their offering can request the partner briefing at softwareinabox.eu or by writing to
 emilio.mulet@softwareinabox.eu.

Annex A. Stakeholder map by country
This annex identifies the stakeholders that appear in the analysis and their potential role in a dental data space. It
is not intended to be exhaustive and should be completed with partner research in each country.

Table 13 · Relevant stakeholders by country

 Country Institutions and regulators Private and professional sector

 Spain Ministry of Health (General Secretariat for Digital General Council of Dentists and professional colleges;
 Health); regional health services; National Health Data DONTE Group (Vitaldent, MAEX); insurers with dental
 Space; Ministry for Digital Transformation networks (Sanitas, Adeslas, Asisa, DKV, Caser); Vivanta;
 Institutos Odontológicos

 Belgium INAMI/RIZIV; Health Data Agency; FPS Public Health; Sickness funds (mutualities); dentists' professional
 Sciensano; Information Security Committee; Dental associations; Benelux chains (Colosseum Dental
 Council Benelux)

 The Netherlands Ministry of VWS; future Gezondheidsdata Autoriteit; KNMT; private equity-backed chains (Top Mondzorg,
 NZa; IGJ; ACM; Nictiz; Zorginstituut Fresh, among others); health insurers; Health-RI

 Denmark Sundhedsstyrelsen; Styrelsen for Patientsikkerhed; Danish Dental Association (Tandlægeforeningen);
 Sundhedsdatastyrelsen; Digital Sundhed Danmark; chains (Colosseum Tandlægerne and others); Novo
 municipalities and regions Nordisk Foundation (Health Data Gateway)

 Germany Federal Ministry of Health; BfArM (FDZ Gesundheit, KZBV and regional KZVs; BZÄK and regional chambers;
 DACO); gematik; statutory health insurance funds iMVZs and groups (Colosseum Dental Deutschland);
 dental software vendors

Annex B. Partner FAQ
Is the dental clinic obliged to share data under the EHDS?
As a data holder for secondary use, a microenterprise is exempt unless its State decides otherwise (Article 50). As
a healthcare provider, it must respect patients' access rights and, insofar as it processes priority categories, use
conformant EHR systems [15][1].

Why isn't each country's public health record enough?
Because in Spain, and in much of adult care in the Netherlands and Denmark, dental data does not go through
public infrastructure. Only Germany has made it mandatory for dental practices to be integrated into its
electronic health record [12].

Does patient data leave the clinic?
Not in the federated model. The clinic keeps its data; the connector exposes metadata and enforces usage
policies. Analyses run in secure environments and the user receives aggregated results or trained models.

What role does Microsoft Azure play?
Azure provides the secure processing environments, data residency in EU regions and health interoperability
services. When data sovereignty requires it, the same model can be deployed on the customer's premises.

What is the recommended first project?
A pilot of quality indicators across the clinics of a chain or insurer network: it has a customer to fund it, it does
not depend on the HDAB being operational and it leaves the connector installed for later use cases.

What happens in 2029?
The exchange of patient summaries and ePrescription begins, together with most secondary use rules [17]. A
dental space catalogued with HealthDCAT-AP metadata will be able to receive requests through the access
bodies.

And in 2031?
Medical images join the priority categories [18]. This is the time to offer the dental imaging module for exchange
and for federated training of AI models.

Annex C. Glossary
Table 14 · Glossary

 Term Definition

 EHDS European Health Data Space, established by Regulation (EU) 2025/327.

 Primary use Processing of electronic health data to provide healthcare.

 Secondary use Reuse of health data for research, innovation, public policy, statistics or training.

 HDAB Health Data Access Body: the body that grants permits for secondary use.

 Trusted data holder Designated entity that handles access requests concerning only its own data (Art. 72).

 EEHRxF European Electronic Health Record Exchange Format.

 HealthDCAT-AP Metadata profile for describing health datasets in catalogues.

 MyHealth@EU / European infrastructures for cross-border primary use and for secondary use.
 HealthData@EU

 Federated data space Architecture in which data stays at source and is shared under usage policies through connectors.

 ODRL Standard language for expressing machine-readable data usage policies.

 ePA German electronic health record ('elektronische Patientenakte').

 iMVZ Investor-funded medical care centre in Germany.

 SCOR Danish central odontological register of child oral health.

 ENDS Spain's National Health Data Space.

Annex D. Sources
[1]SPMS (2025). Health data holders and the European Health Data Space (EHDS) regulation.
 https://www.spms.min-saude.pt/wp-content/uploads/2025/08/Health-Data-Holders-EHDS-flyer.pdf
[2]Council of European Dentists (2026). Manual of Dental Practice 2026 – Spain.
 https://www.cedentists.eu/wp-content/uploads/2026/02/Spain-2026-03.02.2026.pdf
[3]datos.gob.es (05/08/2026). Spain and the European Health Data Space: a vision for healthcare transformation.
 https://datos.gob.es/es/blog/espana-ante-el-espacio-europeo-de-datos-de-salud-una-vision-para-la-transformacion-sanitaria
[4]Spanish Ministry of Health (22/09/2025). Health Ministry prepares a law to regulate the use of big data in research and clinical trials
 (public consultation on the Draft Digital Health Bill); Cuatrecasas (29/09/2025).
 https://www.sanidad.gob.es/gabinete/notasPrensa.do?id=6750

[5]The Brussels Times (2026). Dentistry costs skyrocketing in Belgium, official figures show; The Brussels Times: Over half of all dentists
 remain not covered by medical fee agreement.
 https://www.brusselstimes.com/2376270/dentistry-costs-skyrocketing-in-belgium-official-figures-show
[6]Belgian Health Data Agency (2026). Happy first birthday to the EHDS! What does it mean for Belgium?; Hogan Lovells (2024). Creation of
 a Health Data Agency in Belgium. https://www.hda.belgium.be/en/about_us
[7]NL Times (19/08/2026). A quarter of dentists in the Netherlands came from abroad; DutchNews (2026).
 https://nltimes.nl/2026/08/19/quarter-dentists-netherlands-came-abroad
[8]Rabobank (2025). Dutch oral care has good prospects but also faces challenges; ABN AMRO. Chain formation in oral care; Rabobank.
 Figures and trends for dentists; House of Representatives, parliamentary questions on private equity in oral care (2025).
 https://www.rabobank.nl/kennis/d011514544-nederlandse-mondzorg-heeft-goed-perspectief-maar-kent-ook-de-nodige-uitdagingen
[9]ICTRecht (2026). From Wegiz to the GIS Act: the Dutch implementation of the EHDS; ICTRecht. The implementation of the EHDS: where
 do we stand in early 2026?; Senate, letter of 18/05/2026.
 https://www.ictrecht.nl/en/blog/van-wegiz-tot-wet-gis-de-nederlandse-invulling-van-de-ehds
[10]Council of European Dentists (2026). Manual of Dental Practice 2026 – Denmark.
 https://www.cedentists.eu/wp-content/uploads/2026/02/Denmark-2026-03.02.2026.pdf
[11]Lex.dk. The Danish Health Authority's Central Odontological Register (SCOR); Lex.dk. Child and youth dental care.
 https://lex.dk/sundhedsstyrelsens_centrale_odontologiske_register_(SCOR)
[12]zm-online (16/04/2026). More than 5.5 million eZahnbonushefte stored in the ePA; zm-online (2025). The soft start has taken place;
 zm-online (2026). Process rather than big bang.
 https://www.zm-online.de/news/detail/mehr-als-55-millionen-ezahnbonushefte-sind-in-der-epa-gespeichert
[13]Latham & Watkins (04/12/2025). New Health Data Lab in Germany facilitates secondary use of health data; BfArM. Data Access and
 Coordination Office; TMF (2026). Registers in the EHDS.
 https://www.lw.com/en/insights/new-health-data-lab-in-germany-facilitates-secondary-use-of-health-data
[14]Covington, Inside Privacy. EHDS Series 2: the European Health Data Space from the health data holders' perspective.
 https://www.insideprivacy.com/big-data/ehds-series-2-the-european-health-data-space-from-the-health-data-holders-perspective/
[15]Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the European Health Data Space.
 Legislative file 2022/0140(COD), European Parliament. https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1805726
[16]Kennedys (2026). The European Health Data Space is in force: implications for healthcare, MedTech and life sciences; Arthur Cox (2025).
 https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-european-health-data-space-is-in-force-implications-for-hea
 lthcare-medtech-and-life-sciences
[17]European Commission. European Health Data Space Regulation (EHDS).
 https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en
[18]Ringholm. EHDS, Article 105 (dates of application by priority category). https://www.ringholm.com/ehds/article-105.htm
[19]Lovguiden (08/04/2026). EU opretter bestyrelse for Europæisk Sundhedsdatarum (Implementing Regulation 2026/771).
 https://lovguiden.dk/en/det-offentlige/eur-lex-eu-tidende/2026-04-08-eu-opretter-bestyrelse-for-europaeisk-sundhedsdatarum-ehd
 s
[20]Redacción Médica (27/05/2026). Spain registers 43,672 registered dentists (INE 2025 data).
 https://www.redaccionmedica.com/profesionales/20260527/espana-registra-dentistas-colegiados-un-mas-que-hace-ano/272349_0.
 html
[21]University of Granada, Faculty of Dentistry. Analysis of the situation of dentists in Spain.
 https://odontologia.ugr.es/sites/centros/odontologia/public/ficheros/analisis-dentistas-espa%C3%B1a.pdf
[22]Alimarket (2026). DONTE Group grows more than 11% and exceeds €427M in revenue in 2025; Forbes España (2026); Alimarket:
 Vitaldent adds Dentix's 76 clinics.
 https://www.alimarket.es/sanidad/noticia/425914/donte-group-crece-mas-de-un-11--y-supera-los-427-m-de-facturacion-en-2025
[23]Council of European Dentists (2026). Manual of Dental Practice 2026 – Belgium.
 https://www.cedentists.eu/wp-content/uploads/2026/02/Belgium-2026-03.02.2026.pdf
[24]INAMI (2026). Adherence figures for national agreements and conventions; National dento-mutualist agreement 2026-2027.
 https://www.inami.fgov.be/fr/presse/accord-national-dento-mutualiste-2026-2027-plus-de-60-des-dentistes-rejoignent-l-accord-tari
 faire

[25]Conseil de l'Art dentaire / Raad van de Tandheelkunde (04/11/2025). Opinion on commercial dental chains and the dental profession.
 https://overlegorganen.gezondheid.belgie.be/sites/default/files/documents/adav_2025-03_commerciele_tandheelkundige_centra-c
 entres_dentaires_commerciaux.pdf
[26]INAMI. Interfederal eHealth action plan 2026-2029; news.belgium.be: telematics bonus for dentists.
 https://www.inami.fgov.be/fr/themes/esante/plan-d-action-interfederal-esante-2026-2029
[27]RIZIV-INAMI. Final report OHDRES 2023-2024 (annexes).
 https://www.riziv.fgov.be/SiteCollectionDocuments/FINAL_REPORT_OHDRES_2023_2024_ANNEXES_ENG.pdf
[28]Council of European Dentists (2026). Manual of Dental Practice 2026 – The Netherlands.
 https://www.cedentists.eu/wp-content/uploads/2026/06/Netherlands-2026-23.06.2026.pdf
[29]Netherlands Authority for Consumers and Markets (ACM). Decision on data intermediation service under the Data Governance Act –
 Health-RI. https://www.acm.nl/nl/publicaties/besluit-databemiddelingsdienst-onder-de-data-governance-act-health-ri
[30]OECD/European Commission (2024). Health at a Glance: Europe 2024 – Dental care.
 https://www.oecd.org/en/publications/health-at-a-glance-europe-2024_b3704e14-en/full-report/component-60.html
[31]Dansk Erhverv (2022). Danish dental health: more dentists must be trained; CEPOS. Ownership restrictions on dental chains.
 https://www.danskerhverv.dk/presse-og-nyheder/nyheder/2022/september/dansk-tandsundhed-der-skal-uddannes-flere-tandlager/
[32]Sundhedsdatastyrelsen. Digital Health Denmark; European Health Data Space – MyHealth@EU; Altinget (2026); Sitra (2025), VALO WS2
 Final Report. https://english.sundhedsdatastyrelsen.dk/about-us/digital-health-denmark
[33]Invest in Denmark (02/06/2025). New Health Data Gateway strengthens Denmark's innovative edge within Life Science & Digital Health.
 https://investindk.com/insights/new-health-data-gateway-strengthens-denmarks-innovative-edge-within-life-science-og-digital-healt
 h/
[34]Council of European Dentists (2026). Manual of Dental Practice 2026 – Germany.
 https://www.cedentists.eu/wp-content/uploads/2026/02/Germany-2026-03.02.2026.pdf
[35]KZBV and BZÄK (2024). Press release on iMVZs; zm-online. Dentists renew call for regulation of investor-owned MVZs; zm-online.
 Prevention-oriented dentistry is a success model.
 https://www.bzaek.de/fileadmin/PDFs/pm24/20240123_PM_BZAEK_KZBV_iMVZ.pdf
[36]vdek (2025). Digitalisation in healthcare: electronic application and approval procedure for dentists (EBZ).
 https://www.vdek.com/LVen/SAH/fokus/digitalisierung-loesungen-fuer-unsere-versicherten-2025.html
[37]Universität Witten/Herdecke (2026). Better data for better healthcare (GeDIG); AOK (2026). DMEA 2026.
 https://www.uni-wh.de/en/better-data-for-better-healthcare
[38]Dentistry Today (2025). Align X-ray Insights launches in Europe; Dentsply Sirona (04/05/2026). Smart View – Detect; Dentistry.co.uk
 (01/11/2025). Colosseum Dental Group pilots AI.
 https://dentistry.co.uk/2025/11/01/colosseum-dental-group-pilots-ai-to-improve-diagnostics-and-patient-care/
[39]Regulation (EU) 2016/679, General Data Protection Regulation (GDPR). https://eur-lex.europa.eu/eli/reg/2016/679/oj
[40]Regulation (EU) 2022/868 on European Data Governance (Data Governance Act). https://eur-lex.europa.eu/eli/reg/2022/868/oj
[41]Regulation (EU) 2024/1689 on Artificial Intelligence (AI Act). https://eur-lex.europa.eu/eli/reg/2024/1689/oj
[42]Regulation (EU) 2017/745 on medical devices (MDR). https://eur-lex.europa.eu/eli/reg/2017/745/oj
