# Audit cadrage Produit Pro

Périmètre audité : `docs/README.md`, `docs/Product/vision.md`, `docs/Product/manifeste.md`, `docs/Product/prd.md`, `docs/Product/roadmap.md`, `docs/Product/decisions.md`. Audit réalisé avant écriture de code, sans modification des fichiers `docs`.

Échelle utilisée : Bloquant = empêche le démarrage ou rend une affirmation invérifiable ; Majeur = contradiction ou lacune qui fausserait une décision d'équipe ; Mineur = défaut de forme ou de clarté ; Conforme = point vérifié sans correction requise.

## 1. Contradictions internes entre vision, PRD, roadmap et registre de décisions

### Takeaway

Il existe au moins six contradictions réelles, dont deux bloquantes pour un démarrage : la roadmap ne fait pas dépendre le MVP de la sortie de la phase de recherche, et le registre déclare « retenue » une décision sur les langues que le PRD laisse ouverte. Les autres portent sur le niveau N2, les modes d'inscription, le calendrier de monétisation et les notifications.

### Cited Findings

- [Bloquant] `docs/Product/roadmap.md` l. 6 et l. 18 à 26 : la Phase 1 liste ses dépendances (ADR, service vidéo, service d'emails, modération) mais pas la sortie de la Phase 0. Or `docs/README.md` l. 34 interdit d'entrer une fonctionnalité en sprint sans histoire rattachée à une opportunité de la recherche, et la roadmap l. 14 dit choisir une seule opportunité pour le premier sprint. Un sprint peut donc démarrer avec les FS-01 à FS-11 avant toute validation H1 à H8. Correction : ajouter « Dépendance : critères de sortie de la Phase 0 validés et opportunité retenue par écrit » aux dépendances de la Phase 1, et subordonner le premier sprint à cette sortie. Source : [Opportunity Solution Tree, Product Talk](https://www.producttalk.org/glossary-discovery-opportunity-solution-tree/) et [Building a data-driven UX research plan, LogRocket](https://blog.logrocket.com/ux-design/data-driven-ux-research-plan).
- [Majeur] Langues. `docs/Product/vision.md` l. 65 et `docs/Product/decisions.md` D-008 l. 15 disent français d'abord puis langues décidées marché par marché ; `docs/Product/prd.md` l. 21 marque « anglais dès que possible » comme retenu, `docs/Product/manifeste.md` l. 28 écrit « nous écrivons en français et en anglais », et `docs/Product/prd.md` l. 409 remet le choix des langues en question ouverte. Correction : écrire une seule formulation canonique. Si l'anglais est réellement retenu, préciser le déclencheur et la date, puis aligner vision, manifeste et D-008 ; sinon remplacer les deux affirmations anglaises par « langues validées avec chaque marché ». Source : [ISO/IEC/IEEE 29148, exigences non ambiguës et cohérentes](https://standards.ieee.org/standard/29148-2018.html).
- [Majeur] Niveau N2 et recrutement. `docs/Product/vision.md` l. 58, 71 et 72 promet badge vérifié, candidature avec dossier et message de vérification « quand un recruteur répond », alors que `docs/Product/prd.md` l. 48, 52, 83 et 87 exclut offres, candidatures et comportement propre N2 du MVP. Correction : étiqueler explicitement ces trois phrases comme « phase 2 » dans la vision, ou déplacer N2 dans le MVP avec critères d'acceptation et événements dédiés. Source : [PRD audité, section 3.2 et matrice des droits](/home/espoir-loemba/work/Projects/pro/docs/Product/prd.md).
- [Majeur] Mode d'inscription. `docs/Product/vision.md` l. 57 accepte « email ou téléphone, ou connexion sociale » pour N1, mais la vision l. 74, le parcours A du PRD l. 97 et la liste d'événements FS-11 l. 328 ne spécifient que l'email. Correction : transformer la ligne N1 en « email vérifié en phase 1 ; téléphone et connexion sociale en phase 2, non spécifiés ». Source : [PRD audité, FS-11](/home/espoir-loemba/work/Projects/pro/docs/Product/prd.md).
- [Majeur] Calendrier de monétisation. `docs/Product/roadmap.md` l. 48 à 54 intitule la Phase 4 « monde et niveau organisations payant » et en fait un critère de sortie, alors que l'objectif l. 50 dit « introduire plus tard », et que D-005 limite la gratuité aux phases 1 à 3. Correction : séparer la Phase 4 « ouverture monde » d'une Phase 5 « monétisation organisations », ou écrire que le niveau payant n'est pas livré en Phase 4 et retirer « nom arrêté, privilèges écrits » des critères de sortie. Source : [Vision audité, section 5](/home/espoir-loemba/work/Projects/pro/docs/Product/vision.md).
- [Majeur] Classement payant. `docs/Product/manifeste.md` l. 31 refuse quiconque achète une meilleure position dans un résultat de recherche ; `docs/Product/roadmap.md` l. 52 propose « offres mises en avant » comme privilège futur, sans distinguer recherche et fil. Correction : ajouter une règle explicite « aucun classement payant dans la recherche, les offres mises en avant restent signalées et hors recherche » dans la vision, la roadmap et le registre. Source : [Manifeste audité, point 8](/home/espoir-loemba/work/Projects/pro/docs/Product/manifeste.md).
- [Mineur] Notifications push. `docs/Product/prd.md` FS-10 l. 312 dit « après la première action significative », mais le critère d'acceptation l. 318 interdit toute demande avant trois vidéos vues. Une sauvegarde à la première vidéo est une action significative. Correction : choisir un seul déclencheur, par exemple « après trois vidéos vues et une première action significative ». Source : [Apple Developer, hit targets et permissions contextuelles](https://developer.apple.com/design/tips).
- [Mineur] Vocabulaire réseau. `docs/Product/prd.md` FS-01 l. 148 parle de « connexion mobile de type 4G », la section 10 l. 367 et la roadmap l. 24 parlent de « réseau mobile correct ». Correction : définir un profil réseau de référence unique (débit, latence, perte, modèle de téléphone) et l'utiliser dans les trois endroits. Source : [7 Steps to Benchmark Your Product's UX, Nielsen Norman Group](https://nngroup.com/articles/product-ux-benchmarks).

### Inferences

- Le registre de décisions est traité comme une photo de fin de rédaction, pas comme une source de vérité tenue à jour. Cela explique pourquoi D-008 a figé un compromis que le PRD continue de discuter.
- La vision écrit des scénarios de phase 2 au présent, ce qui donne l'impression au lecteur pressé que N2 et le recrutement font partie du MVP.

### Gaps

- Aucune source externe ne peut trancher les choix métier ci-dessus. Ils doivent être arbitrés par l'équipe et datés dans `decisions.md`.

## 2. Traçabilité des décisions : motif, source, portée, état

### Takeaway

Les douze lignes du registre ont un identifiant, un statut et une portée, mais aucune date ni aucun motif. Le document affirme lui-même qu'une décision a un motif, contredisant sa propre table. Plusieurs décisions structurantes prises ailleurs ne figurent pas dans le registre.

### Cited Findings

- [Bloquant] `docs/Product/decisions.md` l. 4 et l. 6 à 19 : la règle déclare « motif, source et portée », `docs/README.md` l. 33 exige aussi la date, mais la table n'a que Identifiant, Décision, Statut, Source, Portée. Aucune décision n'est datée ni motivée. Correction : ajouter les colonnes Date, Motif, Source liée, Responsable et Historique des révisions ; renseigner les douze lignes existantes avant le premier sprint. Source : [README audité, règle de mise à jour](/home/espoir-loemba/work/Projects/pro/docs/README.md) et [ISO/IEC/IEEE 29148, attributs d'une exigence](https://standards.ieee.org/standard/29148-2018.html).
- [Majeur] `docs/Product/decisions.md` l. 8 à 19 : les sources sont du texte brut du type « Vision section 5 », sans lien, sans numéro de ligne et sans date de consultation. Correction : remplacer par des liens vers les sections, par exemple `[Vision, section 5](/home/espoir-loemba/work/Projects/pro/docs/Product/vision.md)`, avec numéro de ligne ou ancre. Source : [Executing Research, évaluation des sources](file:///home/espoir-loemba/.claude/skills/synced/fe7bce45-f835-4e39-a3c6-b8755d0389f9_7f8962d4-382f-44d6-b4f1-5f3c5f0b7678/deep-research/references/researcher.md).
- [Majeur] `docs/Product/decisions.md` l. 16 à 18 : D-009, D-010 et D-011 sont des questions ouvertes, pas des décisions. Le même tableau mélange « retenue » et « ouverte », ce qui rend ambigu ce qui peut entrer en sprint. Correction : déplacer ces trois lignes dans une table « Questions ouvertes » avec question, phase, responsable, déclencheur et date cible ; ne garder dans le registre que les décisions tranchées. Source : [Hypothesis-driven development, LogRocket](https://blog.logrocket.com/product-management/what-is-hypothesis-driven-development/).
- [Majeur] Couverture incomplète du registre. Décisions structurantes prises ailleurs et absentes de `docs/Product/decisions.md` : notifications push réservées à N1 et plus (`vision.md` l. 108) ; modération en deux temps avec `pending_review` et signalement ouvert aux visiteurs (`vision.md` l. 104 et PRD FS-09) ; durée de conservation des événements de session de 30 jours (`prd.md` l. 373) ; séparation des chemins lecture et écriture et règle « un cache n'est pas une autorisation » (`vision.md` l. 100) ; taxonomie initiale calibrée sur Brazzaville et Kinshasa (`prd.md` l. 34) ; vérification limitée à l'email dans le MVP (`prd.md` l. 52) ; interdiction d'acheter une position dans la recherche (`manifeste.md` l. 31). Correction : créer D-013 à D-019 avec motif, date, source et portée. Source : [README audité, règle l. 33](/home/espoir-loemba/work/Projects/pro/docs/README.md).
- [Mineur] `docs/Product/decisions.md` D-012 l. 19 : la source cite « Vision section 6, PRD section 10 » alors que l'interdiction de suivi est aussi en vision l. 88 et section 7 l. 106, et dans FS-11. Correction : compléter la source, sinon un relecteur croit que le visitor tracking n'est traité qu'en confidentialité. Source : [Vision audité, sections 6 et 7](/home/espoir-loemba/work/Projects/pro/docs/Product/vision.md).
- [Conforme] `docs/Product/decisions.md` l. 6 à 19 : les identifiants D-001 à D-012 sont uniques, les statuts sont explicites et chaque ligne a une portée de phase. Source : [Registre audité](/home/espoir-loemba/work/Projects/pro/docs/Product/decisions.md).
- [Conforme] `docs/Product/decisions.md` l. 21 à 30 : la procédure de réouverture exige preuve, date, décision remplacée et documents touchés. Source : [Registre audité](/home/espoir-loemba/work/Projects/pro/docs/Product/decisions.md).

### Inferences

- Sans date ni motif, une décision « retenue » ne peut pas être auditée six mois plus tard, alors que le manifeste l. 5 prévoit précisément une relecture à six mois.
- Le registre couvre les grandes options de cadrage mais pas les règles de protection et de modération, qui sont pourtant celles qui coûtent le plus cher à revenir après coup.

### Gaps

- Aucun propriétaire de décision n'est nommé dans les six documents. Le registre ne permet donc pas de savoir qui arbitrera D-010 à D-012.

## 3. Critères de sortie et dépendances de la roadmap

### Takeaway

Les phases ont des critères, mais plusieurs ne sont pas vérifiables et les dépendances entre phases sont incomplètes. Le défaut le plus grave est l'absence de dépendance de la Phase 1 envers la Phase 0.

### Cited Findings

- [Bloquant] `docs/Product/roadmap.md` l. 14 : « Chaque hypothèse H1 à H8 est confirmée, infirmée ou explicitement reportée » n'impose aucun seuil pour confirmer ou infirmer, et autorise un report sans date ni responsable. La recherche UX fixe pourtant des seuils par hypothèse, par exemple moins de 5 personnes sur 8 pour H1 et plus de 7 sur 10 abandon pour H4. Correction : reprendre les seuils de `docs/UX/ux-research.md` l. 76 à 83, préciser qui valide, et interdire le report au-delà du premier sprint sans décision écrite. Source : [UX research audité](/home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) et [Translating UX Goals into Analytics Measurement Plans, Nielsen Norman Group](https://nngroup.com/articles/ux-goals-analytics/).
- [Majeur] `docs/Product/roadmap.md` l. 24 : les critères de sortie de la Phase 1 omettent trois des cinq conditions de la définition de terminé du PRD l. 383 à 389, à savoir cas d'erreur testés, revue de code, revue d'accessibilité. Correction : renvoyer explicitement à la section 11 du PRD et exiger la trace des revues. Source : [PRD audité, section 11](/home/espoir-loemba/work/Projects/pro/docs/Product/prd.md).
- [Majeur] `docs/Product/roadmap.md` l. 34 et 36 : le critère « vérification par domaine ou document légal » décrit la vérification d'organisation N3 du PRD l. 445 à 448, pas la vérification de profil N2. La dépendance « Décision sur la règle N2 » renvoie à une question ouverte du PRD l. 406. Correction : scinder en deux critères distincts, N3 organisation vérifiable par domaine ou document, et N2 profil vérifiable seulement après arbitrage de D-010 avec méthode et réversibilité documentées. Source : [Vision audité, l. 128](/home/espoir-loemba/work/Projects/pro/docs/Product/vision.md).
- [Majeur] `docs/Product/roadmap.md` l. 44 : « coût par vidéo vue compris dans le budget » est invérifiable car `docs/Product/prd.md` l. 25 dit budget non communiqué et D-009 à D-012 ne couvrent pas le budget. Correction : écrire un seuil chiffré par vue et par marché, ou reporter le critère après décision budgétaire inscrite au registre. Source : [ISO/IEC/IEEE 29148, caractère vérifiable](https://standards.ieee.org/standard/29148-2018.html).
- [Majeur] `docs/Product/roadmap.md` l. 56 : « Questions ouvertes du PRD tranchées » englobe les neuf questions l. 406 à 414, y compris la stack et la date de lancement qui concernent la Phase 1. Correction : lister uniquement D-010, D-011 et les questions de marché propres à la Phase 4. Source : [Registre audité](/home/espoir-loemba/work/Projects/pro/docs/Product/decisions.md).
- [Mineur] `docs/Product/roadmap.md` l. 6 : « Les durées ci-dessous sont des hypothèses de planification » alors qu'aucune durée n'apparaît dans le document. Correction : ajouter une durée indicatrice par phase ou supprimer la phrase. Source : [Roadmap auditée](/home/espoir-loemba/work/Projects/pro/docs/Product/roadmap.md).
- [Mineur] `docs/Product/prd.md` FS-03 l. 187 : « métier ou métier proche » n'a aucune définition dans la taxonomie. Le critère « au moins la moitié des vidéos » n'est donc pas vérifiable. Correction : publier la taxonomie avec une table de proximité ou remplacer par « appartiennent au métier choisi ». Source : [ISO/IEC/IEEE 29148, exigences vérifiables](https://standards.ieee.org/standard/29148-2018.html).
- [Mineur] `docs/Product/prd.md` FS-08 l. 282 : « sur un réseau correct » n'est pas quantifié. Correction : réutiliser le profil réseau de référence proposé au constat 1.8. Source : [Benchmarking UX, Nielsen Norman Group](https://nngroup.com/articles/benchmarking-ux).

### Inferences

- La roadmap ressemble à une liste d'intentions plus qu'à un contrat de sortie. Une équipe réduite ne peut pas savoir avec certitude quand une phase est terminée.
- Les dépendances nomment des services techniques mais pas les résultats de recherche, alors que le cadrage place la confiance avant la croissance.

### Gaps

- Aucun document n'indique qui valide la sortie de phase, ni où sont archivées les preuves de validation.

## 4. Plan de mesure canonique et définition des métriques

### Takeaway

Il manque l'artefact de cadrage le plus important avant le code : un dictionnaire canonique des mesures. Les indicateurs sont dispersés dans trois documents, avec des noms instruments incompatibles et une métrique phare impossible à calculer avec les événements prévus.

### Cited Findings

- [Bloquant] `docs/Product/vision.md` l. 114 à 118, `docs/Product/manifeste.md` l. 57 et `docs/Product/prd.md` FS-11 l. 322 à 337 : aucun fichier ne définit pour chaque mesure le nom canonique, la formule, le dénominateur, l'événement source, la population, la période, la cible, le garde-fou, le propriétaire et la cadence de revue. Correction : créer `docs/Product/mesure.md` avant le premier sprint et lire cette source dans la vision, le manifeste et le PRD. Source : [Measuring the User Experience on a Large Scale, HEART, CHI 2010](https://research.google/pubs/pub36299.html?frame=0) et [Translating UX Goals into Analytics Measurement Plans, Nielsen Norman Group](https://nngroup.com/articles/ux-goals-analytics/).
- [Bloquant] `docs/Product/vision.md` l. 114, `docs/Product/manifeste.md` l. 57 et `docs/Product/prd.md` l. 337 parlent de « vérifications finalisées pour 1 000 sessions de fil ». FS-11 l. 328 ne contient ni événement de vérification d'identité ni événement de vérification d'organisation ; `signup_verified` l. 336 est la vérification d'email. La source adaptée, Rest of World, parle de « verified registrations per 1,000 page views ». Correction : renommer la mesure en « inscriptions avec email vérifié pour 1 000 sessions de fil » pour la phase 1, la calculer avec `signup_verified` et `feed_session_start`, et créer un événement distinct pour N2 quand la décision sera tranchée. Source : [Rest of World, registration wall, 10 septembre 2026](https://restofworld.org/inside/learned-in-first-months-registration-wall/).
- [Bloquant] `docs/Product/vision.md` l. 114 et `docs/Product/manifeste.md` l. 57 exigent le « retour à sept jours » alors que le visiteur n'a aucun identifiant permanent (`vision.md` l. 56 et 106, `prd.md` l. 373). Une cohorte visiteur à J7 est impossible sans créer un identifiant persistant ou un panel consenti. Correction : décider explicitement que le retour à sept jours est mesuré sur les comptes uniquement, ou documenter un panel consenti avec consentement et durée de conservation ; ne pas laisser les deux règles coexister. Source : [EDPB Guidelines 4/2019, pseudonymisation et clés conservées séparément](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201904_dataprotection_by_design_and_by_default_v2.0_en.pdf).
- [Majeur] `docs/Product/vision.md` l. 116 : les garde-fous sont « pas de hausse des signalements, pas de hausse des comptes suspects, pas de plainte, pas de dégradation du taux de publication ». Sans valeur de base ni seuil, aucune de ces phrases n'est testable. Correction : fixer une valeur de base issue de la phase 0 ou des deux premières semaines, puis un seuil relatif et une fenêtre d'observation. Source : [7 Steps to Benchmark Your Product's UX, Nielsen Norman Group](https://nngroup.com/articles/product-ux-benchmarks).
- [Majeur] `docs/Product/vision.md` l. 112 à 118 : le « premier test oppose deux parcours », mais il n'y a ni taille d'échantillon, ni unité de randomisation, ni durée, ni effet minimal détectable, ni propriétaire de la décision. Correction : écrire une fiche d'expérimentation avec hypothèse, unité, population, durée, métrique primaire, garde-fous et règle d'arrêt. Source : [HEART et processus Goals, Signals, Metrics, CHI 2010](https://research.google/pubs/pub36299.html?frame=0).
- [Majeur] `docs/Product/vision.md` l. 114 et `docs/Product/manifeste.md` l. 57 : « vidéos vues par session » n'est pas défini entre `video_impression` et `video_complete` ; « part des membres qui publient » n'a pas de dénominateur (inscrits, actifs sur 7 jours, ou membres avec profil complété). Correction : écrire les deux formules dans le dictionnaire de mesures et aligner les deux documents. Source : [ISO/IEC/IEEE 29148, absence d'ambiguïté](https://standards.ieee.org/standard/29148-2018.html).
- [Mineur] `docs/Product/manifeste.md` l. 25 dit « nous mesurons le temps », mais le PRD l. 367 ne donne qu'un seuil unique sans percentile ni charge. Correction : définir p50 et p95 pour le démarrage vidéo dans le plan de mesure. Source : [Benchmarking UX: Tracking Metrics, Nielsen Norman Group](https://nngroup.com/articles/benchmarking-ux).
- [Conforme] `docs/Product/prd.md` FS-11 l. 328 à 337 fournit une liste d'événements, un identifiant de session avant inscription et l'interdiction du suivi entre appareils. C'est une base utile, mais ce n'est pas un plan de mesure complet. Source : [PRD audité, FS-11](/home/espoir-loemba/work/Projects/pro/docs/Product/prd.md).

### Inferences

- Le produit veut mesurer la qualité de l'acquisition sans identifier le visiteur. C'est possible pour des taux par session, mais pas pour du retour à sept jours par personne. Le conflit doit être tranché avant l'instrumentation, pas pendant l'analyse.
- Le choix de Rest of World est repris comme une recette, alors que l'article dit explicitement que la gêne doit être proportionnée à la valeur reçue et que son mur intervient après plusieurs articles, pas au premier geste social.

### Gaps

- Aucun tableau de bord n'est spécifié : FS-11 l. 337 suppose son existence, mais aucun livrable de la roadmap ne le mentionne.
- Aucune donnée de base n'existe avant la phase 0. Les seuils devront être posés comme hypothèses puis révisés.

## 5. Séparation des hypothèses, des décisions et des faits

### Takeaway

La séparation est partielle. Le PRD laisse croire que cinq décisions déjà enregistrées sont des hypothèses, et la vision présente des scénarios futurs comme des faits de parcours.

### Cited Findings

- [Majeur] `docs/Product/prd.md` l. 13 à 27 : la table « Hypothèses de départ » mélange des hypothèses à confirmer (équipe, durée, budget) et des décisions déjà prises et enregistrées ailleurs (plateformes D-004, langues D-008, marché D-007, gratuité D-005, données visiteur D-012), avec un statut « retenu » qui n'est pas un statut d'hypothèse. Correction : scinder en deux tables, « Décisions héritées du registre » avec identifiant de décision, et « Hypothèses à valider » avec hypothèse, méthode, seuil et échéance. Source : [Guide for Writing Requirements, INCOSE via ISO/IEC/IEEE 29148](https://standards.ieee.org/standard/29148-2018.html).
- [Majeur] `docs/Product/vision.md` l. 67 à 76 : les phrases de conversion sont écrites au présent et sans statut, alors que trois d'entre elles concernent des capacités de phase 2. Correction : ajouter un marqueur « phase 1 » ou « phase 2 » devant chaque phrase et relier chaque déclencheur à un événement du plan de mesure. Source : [PRD audité, section 3.2](/home/espoir-loemba/work/Projects/pro/docs/Product/prd.md).
- [Mineur] `docs/Product/manifeste.md` l. 9 à 43 : les convictions sont présentées comme des vérités, ce qui est le genre du manifeste, mais le point 12 annonce des tests. Correction : ajouter une phrase unique en tête de section précisant que ces convictions sont des engagements de conception, pas des résultats observés. Source : [Continuous discovery habits, LogRocket](https://blog.logrocket.com/product-management/continuous-discovery-habits-product-team).
- [Conforme] `docs/Product/vision.md` l. 40 à 50 distingue explicitement les données publiées et leurs réserves ; la section 9 l. 122 à 130 liste les limites de transposabilité, le coût, les robots, la vérification et le fil vide. Source : [Vision auditée, sections 4 et 9](/home/espoir-loemba/work/Projects/pro/docs/Product/vision.md).
- [Conforme] `docs/Product/prd.md` l. 15 précise que les valeurs marquées « à confirmer » doivent être validées avant le démarrage du chantier. Source : [PRD audité, section 2](/home/espoir-loemba/work/Projects/pro/docs/Product/prd.md).

### Inferences

- La frontière floue entre hypothèse et décision vient de l'usage du mot « retenu » dans la table du PRD. Ce mot devrait être réservé au registre.

### Gaps

- Aucun lien n'existe entre les hypothèses du PRD et les hypothèses H1 à H8 de la recherche UX. Un même risque peut donc être suivi deux fois ou pas du tout.

## 6. Sources : réalité, dates et liaison avec les affirmations

### Takeaway

Cinq affirmations sont correctement sourcées et vérifiées. Six références ne sont pas datées, deux s'appuient sur des sources secondaires non vérifiées, et une référence est mal attribuée.

### Cited Findings

- [Majeur] `docs/Product/vision.md` l. 46 et référence [8] l. 141 : « FT Strategies et Global Network Initiative » est une erreur d'attribution ; le partenaire du rapport est Google News Initiative. La même phrase affirme que le Guardian a documenté le même arbitrage, sans source Guardian, et que l'inscription obligatoire a fait baisser les revenus publicitaires du FT, affirmation que le rapport cité ne soutient pas directement. Correction : retirer le Guardian ou ajouter sa source, reformuler l'effet sur les revenus à partir du rapport, corriger le nom du partenaire et ajouter une date de publication. Source : [FT Strategies, Turning Anonymous Visitors into Known Users](https://programmes.ftstrategies.com/insights/turning-anonymous-visitors-into-known-users-the-power-of-registration).
- [Majeur] `docs/Product/vision.md` l. 32 et référence [2] l. 135 : le comportement de TikTok dans l'application est affirmé à partir d'un guide tiers que la propre liste de références qualifie de « source secondaire, à confirmer par test manuel ». Correction : transformer l'affirmation en hypothèse à tester ou remplacer par la politique officielle TikTok. Source : [Executing Research, préférer la source primaire](file:///home/espoir-loemba/.claude/skills/synced/fe7bce45-f835-4e39-a3c6-b8755d0389f9_7f8962d4-382f-44d6-b4f1-5f3c5f0b7678/deep-research/references/researcher.md).
- [Majeur] `docs/Product/vision.md` l. 34 et référence [4] l. 137 : les détails techniques du mur LinkedIn (IP, referrer, vitesse, forme d'URL) viennent d'un blog tiers, sans date. Correction : marquer comme observation non vérifiée ou produire un test reproductible daté. Source : [Executing Research, ne pas prendre les résultats pour argent comptant](file:///home/espoir-loemba/.claude/skills/synced/fe7bce45-f835-4e39-a3c6-b8755d0389f9_7f8962d4-382f-44d6-b4f1-5f3c5f0b7678/deep-research/references/researcher.md).
- [Majeur] `docs/Product/vision.md` l. 132 à 147 : les références [3], [4], [8], [11], [12] et [13] n'ont pas de date de publication ou de consultation, contrairement aux références [1], [2], [5], [6], [7], [9], [10] et [14]. Correction : ajouter une date à chaque entrée et une date de dernier accès pour les pages dynamiques. Source : [Executing Research, évaluation des sources](file:///home/espoir-loemba/.claude/skills/synced/fe7bce45-f835-4e39-a3c6-b8755d0389f9_7f8962d4-382f-44d6-b4f1-5f3c5f0b7678/deep-research/references/researcher.md).
- [Mineur] `docs/Product/vision.md` l. 42 : « Les auteurs en tirent une règle d'interface » dépasse ce que l'étude citée établit directement, à savoir un taux de contribution supérieur quand l'inscription est optionnelle. Correction : écrire « ces résultats soutiennent l'hypothèse d'interface suivante » et la relier à H4. Source : [Jay et al., CHI 2016, DOI 10.1145/2858036.2858319](https://doi.org/10.1145/2858036.2858319).
- [Conforme] `docs/Product/vision.md` l. 42 : le chiffre de 62 % est exact. Source : [Jay et al., CHI 2016](https://doi.org/10.1145/2858036.2858319).
- [Conforme] `docs/Product/vision.md` l. 44 : la recommandation depuis 1999 et l'article de 2014 sur les murs de connexion existent et correspondent. Source : [Nielsen Norman Group, Web Research: Believe the Data](https://www.nngroup.com/articles/web-research-believe-the-data/) et [Login Walls Stop Users in Their Tracks](https://www.nngroup.com/articles/login-walls/).
- [Conforme] `docs/Product/vision.md` l. 46 : les chiffres 87 % et environ trois sur cinq avec Google Sign-In sont confirmés par l'article du 10 septembre 2026. Source : [Rest of World](https://restofworld.org/inside/learned-in-first-months-registration-wall/).
- [Conforme] `docs/Product/vision.md` l. 50 : le principe de hachage avec clé conservée séparément est conforme aux recommandations EDPB et ENISA citées. Source : [EDPB Guidelines 4/2019](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201904_dataprotection_by_design_and_by_default_v2.0_en.pdf).

### Inferences

- La vision utilise des sources solides pour le principe général, mais les détails concurrentiels reposent sur des sources faibles. Sur un produit dont le pari est le timing de l'identité, ce déséquilibre est risqué.
- La référence [9] est la mieux reliée à une métrique, mais elle est aussi la plus détournée, puisque son indicateur porte sur des pages vues et des inscriptions vérifiées, pas sur des vérifications d'identité professionnelle.

### Gaps

- Les chiffres Piano rapportés à `vision.md` l. 48 via Digiday n'ont pas été vérifiés dans l'article source au moment de cet audit.
- La date du 15 juillet 2026 attribuée à la politique de confidentialité TikTok n'a pas été vérifiée.
- L'affirmation selon laquelle une personne non connectée peut être une personne concernée au sens du RGPD est juridiquement plausible, mais le lien direct avec les EDPB Guidelines 8/2020 citées n'a pas été confirmé dans le texte de ces lignes directrices.

## 7. Coquilles, numérotation, liens et caractères interdits

### Takeaway

Aucun tiret cadratin ni demi-cadratin n'a été trouvé, les liens internes des six documents résolvent tous, et les numérotations sont continues. Les défauts restants sont de petites incohérences de vocabulaire ou de structure.

### Cited Findings

- [Conforme] `docs/README.md` l. 4, `docs/Product/vision.md`, `manifeste.md`, `prd.md`, `roadmap.md`, `decisions.md` : recherche par expression régulière sur U+2014 et U+2013, zéro occurrence. Source : [README audité, règle typographique](/home/espoir-loemba/work/Projects/pro/docs/README.md).
- [Conforme] Liens internes : `./manifeste.md`, `./vision.md`, `./prd.md`, `./decisions.md` et `../Redaction/ia-defauts-et-tips.md` pointent vers des fichiers existants. Source : [Arborescence docs vérifiée](/home/espoir-loemba/work/Projects/pro/docs/README.md).
- [Conforme] Numérotation : sections 1 à 10 de la vision, 1 à 15 du PRD, FS-01 à FS-11, phases 0 à 4, D-001 à D-012, points 1 à 12 du manifeste. Aucun saut détecté. Source : [Documents audités](/home/espoir-loemba/work/Projects/pro/docs/Product/roadmap.md).
- [Mineur] `docs/README.md` l. 14 : « alias `usertories.md` » présente un fichier au nom mal formé comme un alias, sans expliquer s'il s'agit d'un ancien nom ou d'un renvoi. Correction : préciser « ancien nom conservé pour les liens historiques » ou supprimer l'alias après vérification des liens. Source : [README audité](/home/espoir-loemba/work/Projects/pro/docs/README.md).
- [Mineur] `docs/Product/prd.md` l. 412 : « Faut-il renommer les fichiers avec un préfixe numérique pour forcer l'ordre de lecture ? » est une question de maintenance documentaire dans les questions ouvertes produit. Correction : déplacer dans `docs/README.md` ou trancher immédiatement, puisque les sections sont déjà numérotées. Source : [README audité, organisation des dossiers](/home/espoir-loemba/work/Projects/pro/docs/README.md).
- [Mineur] `docs/Product/vision.md` l. 52 : titre « Décision produit : quatre niveaux d'accès » au singulier pour une section qui contient au moins dix décisions distinctes. Correction : « Décisions produit : quatre niveaux d'accès ». Source : [Vision auditée](/home/espoir-loemba/work/Projects/pro/docs/Product/vision.md).
- [Mineur] `docs/Product/prd.md` l. 360 : les états `blocked` et `reported` d'un message mélangent état de livraison et état de modération. Correction : séparer en deux champs ou documenter la transition. Source : [ISO/IEC/IEEE 29148, cohérence interne](https://standards.ieee.org/standard/29148-2018.html).
- [Mineur] `docs/Product/prd.md` l. 373 : les événements de session sont conservés 30 jours, mais la conservation des agrégats n'est pas définie, alors que le manifeste l. 34 refuse la conservation « au cas où ». Correction : écrire une durée et une finalité pour les agrégats. Source : [EDPB Guidelines 4/2019](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201904_dataprotection_by_design_and_by_default_v2.0_en.pdf).

### Inferences

- Les règles typographiques sont respectées, ce qui montre que le travail de forme a été fait. Les efforts restants portent sur la cohérence sémantique, pas sur la présentation.

### Gaps

- Les URL externes de la vision n'ont pas toutes été testées une par une. Seules les références [5], [6], [7], [8] et [9] ont été vérifiées dans le cadre de cet audit.

## 8. Défauts documentaires et décisions métier encore ouvertes

### Takeaway

Les défauts documentaires sont corrigibles par l'équipe produit sans arbitrage : dates, motifs, liens, critères vérifiables, plan de mesure. Les décisions métier ouvertes exigent un arbitrage et doivent rester hors sprint jusqu'à ce qu'elles soient tranchées.

### Cited Findings

- [Bloquant] Défaut documentaire : `docs/Product/decisions.md` l. 6 à 19 n'a ni date ni motif ; correction exposée au constat 2.1. Source : [README audité](/home/espoir-loemba/work/Projects/pro/docs/README.md).
- [Bloquant] Défaut documentaire : absence de plan de mesure canonique ; correction exposée au constat 4.1. Source : [HEART, CHI 2010](https://research.google/pubs/pub36299.html?frame=0).
- [Bloquant] Défaut documentaire : la métrique « vérifications finalisées pour 1 000 sessions de fil » n'a pas d'événement source ; correction exposée au constat 4.2. Source : [Rest of World](https://restofworld.org/inside/learned-in-first-months-registration-wall/).
- [Bloquant] Défaut documentaire : `docs/Product/roadmap.md` l. 18 à 26 ne fait pas dépendre la Phase 1 de la Phase 0 ; correction exposée au constat 1.1. Source : [Opportunity Solution Tree, Product Talk](https://www.producttalk.org/glossary-discovery-opportunity-solution-tree/).
- [Majeur] Décision métier ouverte : quelles langues ajouter et quand, car `vision.md` l. 65 et `prd.md` l. 21 et 409 ne concordent pas. À trancher avant la fin de la Phase 0. Source : [Registre audité, D-008](/home/espoir-loemba/work/Projects/pro/docs/Product/decisions.md).
- [Majeur] Décision métier ouverte : règle N2 pour les candidatures, enregistrée comme D-010, dépendance directe de la Phase 2. Source : [Registre audité, D-010](/home/espoir-loemba/work/Projects/pro/docs/Product/decisions.md).
- [Majeur] Décision métier ouverte : nom et privilèges du niveau organisations payant, D-011 ; ne doit pas entrer dans la Phase 4 avant arbitrage. Source : [Registre audité, D-011](/home/espoir-loemba/work/Projects/pro/docs/Product/decisions.md).
- [Majeur] Décision métier ouverte : budget CDN et modération, absent du registre alors qu'il conditionne la sortie de la Phase 3. Source : [PRD audité, l. 25 et l. 410](/home/espoir-loemba/work/Projects/pro/docs/Product/prd.md).
- [Majeur] Décision métier ouverte : méthode de mesure du retour à sept jours sans identifiant permanent pour le visiteur. Source : [Vision auditée, l. 56, 106 et 114](/home/espoir-loemba/work/Projects/pro/docs/Product/vision.md).
- [Mineur] Décision métier ouverte : plafond de lecture évoqué en `vision.md` l. 124 comme couverture de coût futur, sans seuil ni phase. Correction : l'inscrire comme question ouverte datée ou retirer. Source : [Vision auditée, section 9](/home/espoir-loemba/work/Projects/pro/docs/Product/vision.md).
- [Conforme] Décision métier déjà tranchée et correctement qualifiée : mobile et web livrés ensemble (D-004), gratuité d'acquisition (D-005), premier marché deux Congo (D-007), aucun identifiant permanent visiteur (D-012). Source : [Registre audité](/home/espoir-loemba/work/Projects/pro/docs/Product/decisions.md).

### Inferences

- Un correctif unique ne suffit pas : il faut d'abord verrouiller le plan de mesure et la dépendance Phase 0 vers Phase 1, car ces deux points changent le contenu des sprints.
- Les autres questions ouvertes peuvent rester ouvertes pendant la Phase 1 si elles sont enregistrées avec un déclencheur de phase, un responsable et une date cible.

### Gaps

- L'équipe n'a pas fourni la date de début de chantier. Les échéances proposées ci-dessus sont donc relatives aux phases, pas calendaires.
