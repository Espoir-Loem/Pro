# Audit cadrage Pro : Opérations, Croissance, modération et mesure

## La file de modération est-elle réellement prête avant l'ouverture publique ?

### Takeaway

Non. Les quatre documents audités posent une intention et des déclencheurs, mais aucun ne contient le volume, le rôle nominé, la matrice de priorisation chiffrée, le délai cible ni l'escalade. La préparation est planifiée, pas démontrée, et la définition de terminé du PRD ne comporte aucun critère opérationnel de go ou no go.

### Cited Findings

| Classement | Nature | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Bloquant | Défaut documentaire | `docs/Operations/README.md` | Statut et Première action, lignes 4, 5 et 18 | Texte : aucun document n'est encore rédigé ; la première action se limite à décrire une journée type sur une page. Aucune donnée de volume, de rôle, de temps par ticket, de priorisation chiffrée, de délai ni d'escalade n'existe. | Rédiger `journee-type-moderation.md` avant tout lien public : volume attendu par ville et par motif, rôle nominé, temps cible par ticket, seuil d'alerte, délai d'escalade. Ajouter cette pièce comme condition 6 de la section 11 du PRD, avec décision explicite go ou no go avant ouverture. | [Google SRE, Incident Management Guide, préparation, alertes et astreinte](https://sre.google/resources/practices-and-processes/incident-management-guide) ; [Ops README](file:///home/espoir-loemba/work/Projects/pro/docs/Operations/README.md) |
| Bloquant | Défaut documentaire | `docs/Product/prd.md` | Section 11, lignes 383 à 389 | Les cinq conditions de terminé sont toutes produit ou technique. Aucune ne vérifie que la file est armée, qu'un modérateur est joignable ou qu'un test de file a été joué. | Ajouter : revue de la journée type, astreinte nominée, test à blanc d'un signalement visiteur jusqu'à la notification d'auteur, et validation du délai cible. | [Google SRE, préparer les procédures à l'avance](https://sre.google/sre-book/managing-incidents) ; [PRD section 11](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |
| Majeur | Décision opérationnelle à prendre | `docs/Product/prd.md` | FS-09, ligne 293, et section 12, ligne 399 | La priorité est définie comme selon le motif et le nombre de signalements, sans formule, ni seuil, ni délai. La mesure prévoit un roulement bénévole ou salarié, sans effectif, ni tour de garde, ni déclencheur. | Arbitrer une matrice : P1 contenu dangereux ou harcèlement avec signalement unique, P2 contenu trompeur ou spam après deux signalements, P3 autre. Fixer un délai de première prise en charge par priorité et un effectif minimal par ville. Choisir le modèle bénévole ou salarié avant l'ouverture. | [Reddit, modération et appels, traitement dans un délai raisonnable et priorisation automatisée](https://support.reddithelp.com/hc/articles/23511059871252-Content-Moderation-Enforcement-and-Appeals) ; [PRD](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |
| Majeur | Décision opérationnelle à prendre | `docs/Product/prd.md` | Section 10, ligne 379 | Une alerte sur la file est prévue, mais sans seuil de profondeur, sans âge du ticket le plus ancien et sans destinataire. | Définir deux signaux actionnables : nombre de tickets ouverts et âge du plus ancien, avec destinataire nommé et procédure de bascule vers le responsable produit. | [Google SRE, alertes basées sur les symptômes, actionnables et couvrant les fonctions clés](https://sre.google/resources/practices-and-processes/incident-management-guide) ; [PRD section 10](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |
| Conforme | Sans objet | `docs/Operations/README.md` | Règle et tableau, lignes 5, 9 et 10 | La règle pose la file dès le MVP, et les déclencheurs du manuel et de la contestation précèdent FS-09 et la notification des décisions. | Conserver ces deux points comme fondement, puis les rendre opposables dans la section 11 du PRD. | [Ops README](file:///home/espoir-loemba/work/Projects/pro/docs/Operations/README.md) |

Les faits documentaires ci-dessus sont tous vérifiés dans les fichiers locaux : [Ops README](file:///home/espoir-loemba/work/Projects/pro/docs/Operations/README.md) et [PRD](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md). La recommandation de préparation s'appuie sur [Google SRE](https://sre.google/resources/practices-and-processes/incident-management-guide), qui recommande un mécanisme d'alerte fiable, une astreinte définie, des playbooks à jour et de l'entraînement régulier, et sur [le chapitre Managing Incidents](https://sre.google/sre-book/managing-incidents), qui recommande de préparer les procédures par écrit avant l'incident.

### Inferences

- Défaut documentaire : le vide porte sur les quatre paramètres demandés, volume, rôle, délai, escalade. Le tableau Opérations n'est qu'une liste de titres, pas un dispositif.
- Décision opérationnelle à prendre : le niveau de service, l'effectif et le modèle bénévole ou salarié ne peuvent pas être déduits des documents. Le PRD les met explicitement en attente. Il faut les trancher, puis les écrire.
- Le risque n'est pas seulement une file lente. Sans délai de contestation écrit, la conservation des vidéos retirées décrite en section 9 du PRD reste sans borne vérifiable ([PRD section 9](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md)).

### Gaps

- Aucune estimation de volume de signalements par ville et par 1 000 vidéos vues n'est disponible dans le périmètre audité. Le temps par ticket ne peut donc pas être calibré.
- Aucun nom, aucune garde ni aucun canal d'astreinte n'est indiqué. Le classement Bloquant porte sur l'absence de dispositif vérifiable, pas sur une affirmation selon laquelle personne ne serait disponible.
- Aucune source fiable trouvée sur une norme de délai de modération propre à Brazzaville ou Kinshasa. Les délais proposés sont des décisions à prendre, pas des faits de marché.

## Le manuel de contestation et la notification des auteurs sont-ils cohérents avec FS-09 ?

### Takeaway

Partiellement. La boucle ticket, décision, notification, nouveau ticket est correctement spécifiée, mais le canal, la motivation de la décision, le délai de contestation et le niveau de relecture restent implicites. FS-10 ajoute une notification push qui n'est pas articulée avec l'email à lien unique de FS-09.

### Cited Findings

| Classement | Nature | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Majeur | Défaut documentaire | `docs/Product/prd.md` | FS-09 lignes 296 et 302, FS-10 lignes 311 et 314 | FS-09 impose une contestation par email avec lien unique et une notification contenant la décision et un lien de contestation. FS-10 range la décision de modération parmi les push et décrit un lien direct vers l'élément concerné. Aucun texte ne dit quel canal fait foi, ni que le push peut contenir le motif, ni comment éviter d'afficher une sanction sur un écran verrouillé. | Écrire une règle de canal : email canonique contenant motif, décision, délai et lien unique ; push limité à un rappel neutre sans motif sur l'écran verrouillé ; bandeau dans l'application pour les membres connectés. Spécifier que le lien push mène à l'élément, pas à la contestation. | [Commission européenne, base DSA, déclaration de motifs : type de restriction, motifs, faits et circonstances, voies de recours](https://digital-strategy.ec.europa.eu/en/faqs/dsa-transparency-database-questions-and-answers) ; [EDPB lignes 3/2025, paragraphe 24, motivation claire et spécifique et transparence sur les moyens automatisés](https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202503_interplay-dsa-gdpr_v2_en.pdf) |
| Majeur | Décision opérationnelle à prendre | `docs/Operations/README.md` et `docs/Product/prd.md` | Ops ligne 10 ; PRD ligne 363 | `contestation.md` porte la question du délai mais n'est pas rédigé. Le PRD parle du temps du délai de contestation sans le chiffrer, tout en fixant la conservation des vidéos retirées à ce délai. | Choisir un délai unique, par exemple trente jours, et l'écrire dans FS-09, dans la section 9 et dans `contestation.md`. Préciser l'horodatage de réception, le ticket d'origine en référence et le sort de la vidéo à l'échéance. | [Tumblr, appels dans un délai de six mois et accusé de réception](https://help.tumblr.com/knowledge-base/appeals-on-tumblr) ; [arXiv, identifiant de ticket et accusé de réception](https://info.arxiv.org/help/moderation/appeals.html) |
| Majeur | Décision opérationnelle à prendre | `docs/Operations/README.md` | `contestation.md`, ligne 10 | La question traitée couvre réception, délai, nouveau ticket et réponse à l'auteur. Elle ne dit pas qui statue en second, ni comment éviter que le modérateur d'origine juge son propre appel. | Ajouter : relecture par une deuxième personne, extincteur de recours répété, critère de réouverture, et notification finale avec motif. | [Reddit, traitement diligent, non arbitraire et non discriminatoire, avec inversion de la décision si l'évaluation initiale était erronée](https://support.reddithelp.com/hc/articles/23511059871252-Content-Moderation-Enforcement-and-Appeals) ; [Roblox, un seul recours par action modérée](https://en.help.roblox.com/hc/en-us/articles/360000245263-Appeal-Your-Content-or-Account-Moderation) |
| Mineur | Défaut documentaire | `docs/Operations/README.md` | `contestation.md`, ligne 10 | Aucun format de preuve de réception ni de suivi de statut n'est prévu. | Ajouter les champs : référence du ticket d'origine, date de réception, statut, motif invoqué, décision finale, date de clôture. | [arXiv, envoi d'un identifiant de ticket quand l'appel est reçu](https://info.arxiv.org/help/moderation/appeals.html) |
| Conforme | Sans objet | `docs/Product/prd.md` | FS-09 lignes 300, 301 et 303 | Le ticket du signalant visiteur porte une référence pseudonyme, chaque action est journalisée avec identifiant, date, action et motif, et une contestation ouvre un nouveau ticket lié à l'origine. | Conserver ces trois règles telles quelles. | [PRD FS-09](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |

Le paragraphe 24 des [lignes directrices EDPB 3/2025](https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202503_interplay-dsa-gdpr_v2_en.pdf) rappelle que la modération automatisée comporte des risques d'erreur et exige transparence, motivation claire et information sur les taux d'erreur et les garanties. Même si Pro ne dessert pas l'Union européenne dans la phase 1, cela fournit un référentiel de rigueur pour la notification, dès lors que le PRD annonce une extension possible en section 10 ([PRD section 10](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md)). La [FAQ DSA](https://digital-strategy.ec.europa.eu/en/faqs/dsa-transparency-database-questions-and-answers) précise que les voies de recours sont destinées au destinataire de la décision, ce qui conforte le choix d'un email nominatif plutôt qu'une information publique.

### Inferences

- Défaut documentaire : FS-09 et FS-10 se contredisent en apparence sur le canal. Une phrase de priorisation suffit à lever l'ambiguïté, sans changer le produit.
- Décision opérationnelle à prendre : la durée de contestation, le nombre de relecteurs et le sort des contenus après rejet ne sont pas des coquilles. Ce sont des choix de politique de modération à arbitrer avant la notification d'auteur, puisque `contestation.md` est déclenché avant cette notification.
- Conforme : l'épine dorsale FS-09, ticket pseudonyme, journal d'audit, nouveau ticket lié, est solide et ne doit pas être réécrite.

### Gaps

- Aucune source trouvée sur un délai de contestation adapté au contexte congolais. Les délais cités, six mois chez Tumblr et Reddit, deux à quatre semaines chez arXiv, servent de bornes de comparaison, pas de prescription.
- Le document ne dit pas si un visiteur qui signale reçoit un accusé de réception. FS-09 ne prévoit la notification que de l'auteur. Ce point reste ouvert.
- Aucune précision sur le traitement d'une contestation quand le compte est suspendu et ne peut plus recevoir de push. Le email devient alors le seul canal fiable, ce qui renforce la correction proposée.

## Le plan d'acquisition respecte-t-il la gratuité totale et évite-t-il les promesses d'emploi ?

### Takeaway

La règle de gratuité est explicite et cohérente avec le PRD. En revanche, l'interdiction des promesses est formulée de manière trop générale dans `messagerie.md`, sans liste de claims interdits ni circuit de validation, et la veille arnaque démarre trop tard au regard du risque documenté dans la recherche UX.

### Cited Findings

| Classement | Nature | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Conforme | Sans objet | `docs/Growth/README.md` et `docs/Product/prd.md` | Growth ligne 5 ; PRD lignes 26, 48 et 460 | La règle interdit tout privilège payant pendant l'acquisition. Le PRD exclut offres d'emploi, candidatures et monétisation du MVP et confirme la gratuité des pages phase 2. | Maintenir la règle telle quelle et la faire reprendre dans chaque document de campagne. | [Growth README](file:///home/espoir-loemba/work/Projects/pro/docs/Growth/README.md) ; [PRD](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |
| Majeur | Défaut documentaire | `docs/Growth/README.md` | `messagerie.md`, ligne 12, et Première action, ligne 18 | La phrase ce qu'on ne promet pas n'est pas développée. La première action demande une phrase sans promesse d'emploi, mais aucune liste n'interdit par exemple emploi garanti, salaire annoncé, recruteur vérifié ou offre disponible sur Pro. Or le MVP n'a ni offres ni vérification d'identité au-delà de l'email. | Ajouter une liste fermée de claims interdits et une validation écrite obligatoire avant publication, avec un propriétaire par ville. Distinguer formule autorisée : montrer une personne faire son métier, et formule interdite : trouver un emploi garanti. | [FTC, avertissement job scammers, promesses d'embauche rapide et demande de données avant entretien](https://consumer.ftc.gov/consumer-alerts/2025/07/job-scammers-are-looking-hire-you) ; [Indeed Trust and Safety, offres d'emploi par réseaux sociaux ou SMS comme signal d'arnaque](https://www.indeed.com/news/releases/how-to-spot-and-avoid-job-offer-scams) |
| Majeur | Décision opérationnelle à prendre | `docs/Operations/README.md` et `docs/UX/ux-research.md` | Ops `veille-arnaque.md`, ligne 14 ; UX R7 ligne 66 et O4 lignes 171 à 181 | La veille arnaque est déclenchée après les premiers signalements, alors que la recherche UX rapporte que 22 % des professionnels interrogés craignent les arnaques pendant la navigation et 21 % au premier contact d'un recruteur, et propose un avertissement dans le chat qui n'est pas au FS-07 actuel. | Avancer la rédaction de `veille-arnaque.md` avant l'ouverture. Rédiger les avertissements de chat, nommer un responsable, définir un seuil de mise à jour, et arbitrer l'ajout de l'avertissement à FS-07 avant la campagne. | [UX R7, LinkedIn Job Search Safety Pulse](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) ; [FTC, signaux d'arnaque à l'embauche](https://consumer.ftc.gov/consumer-alerts/2025/07/job-scammers-are-looking-hire-you) |
| Conforme | Sans objet | `docs/Product/prd.md` | Section 3.2, ligne 48 | Aucune offre d'emploi n'est livrée dans le MVP, et les pages entreprise arrivent plus tard gratuitement. | Conserver cette frontière et la rappeler dans les textes de campagne pour éviter toute confusion. | [PRD section 3.2](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |

La [FTC](https://consumer.ftc.gov/consumer-alerts/2025/07/job-scammers-are-looking-hire-you) décrit précisément le mécanisme que Pro doit éviter : un recruteur qui envoie une offre avant l'entretien et demande des données financières ou personnelles. [Indeed](https://www.indeed.com/news/releases/how-to-spot-and-avoid-job-offer-scams) ajoute que les promesses d'horaires souples, de forte rémunération et d'embauche rapide sont des signaux d'arnaque. Ces deux sources justifient une liste fermée de claims interdits dans `messagerie.md`, sans inventer de chiffre de conversion.

### Inferences

- Défaut documentaire : la règle de gratuité est bien écrite, mais la règle de promesse ne l'est pas assez pour être appliquée par un partenaire ou un prestataire local.
- Décision opérationnelle à prendre : le moment où l'avertissement arnaque entre dans le chat dépend du résultat de la recherche RQ3. C'est une décision produit à prendre avant la première campagne, pas une simple coquille.
- Le risque réputationnel est asymétrique : une promesse d'emploi non tenue détruit la confiance plus vite qu'une campagne tiède ne la construit, alors que la cible est précisément en recherche d'emploi ([UX section 3](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md)).

### Gaps

- Aucune donnée locale sur la perception des promesses d'emploi à Brazzaville et Kinshasa n'est disponible dans le périmètre. Les sources FTC et Indeed sont anglophones et servent de modèle de signaux, pas de mesure locale.
- Aucun projet de phrase d'invitation n'est fourni dans `Growth/README.md`. Impossible de vérifier concretement le ton avant rédaction de `messagerie.md`.
- Aucun circuit de validation des partenaires n'est décrit dans `partenariats.md`, dont le déclencheur est seulement après la recherche UX.

## Les trois métiers pilotes par ville sont-ils une méthode défendable pour éviter un fil vide ?

### Takeaway

Le principe est défendable comme dispositif anti fil vide, mais il n'est pas encore une méthode. Il manque un seuil de semis écrit avant ouverture, un critère de choix des métiers et un mécanisme de repli mesurable par ville.

### Cited Findings

| Classement | Nature | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Majeur | Décision opérationnelle à prendre | `docs/Growth/README.md` et `docs/Product/prd.md` | Growth ligne 10 et ligne 18 ; PRD section 12 ligne 395 | Le document demande trois métiers par ville et un nombre de créateurs par métier, sans cible chiffrée. Le PRD se contente de recruter sur quelques métiers avant ouverture. Aucun seuil ne permet de décider que le fil n'est pas vide. | Fixer avant ouverture une cible par ville, par exemple au moins trois créateurs actifs et un minimum de vidéos publiées et modérées par métier, puis vérifier le seuil avec `video_published` ventillé par ville. Prévoir un repli explicite vers le fil général si le seuil n'est pas atteint. | [LogRocket, concept testing, les fake doors mesurent l'intérêt et les MVP ne se simulent pas pour les réseaux à interactions multiples](https://blog.logrocket.com/ux-design/using-concept-testing-product-design) ; [guide fake door, seuil de réussite écrit avant le lancement](https://getlaunchlist.com/blog/fake-door-test) ; [PRD section 12](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |
| Majeur | Décision opérationnelle à prendre | `docs/Growth/README.md` | `lanceurs-metiers.md`, ligne 10 | Le document ne dit pas comment éviter que les créateurs recrutés publient une seule vidéo puis disparaissent, alors que le risque fil vide est un risque d'ouverture, pas un risque de jour 1 seulement. | Ajouter un engagement minimal de publication sur les deux premières semaines, un calendrier de relance et un propriétaire par ville, avec mesure `video_published` et `video_complete`. | [HEART, cadre objectifs signaux mesures et engagement rapporté par personne](https://research.google.com/pubs/archive/36299.pdf) ; [UX section 11](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) |
| Mineur | Défaut documentaire | `docs/UX/ux-research.md` | Section 8, lignes 100 à 102 | Le terrain prévoit six secteurs à mélanger et deux personnes qui créent déjà du contenu dans l'échantillon total, sans règle pour passer de six secteurs à trois métiers par ville ni pour recruter les créateurs pilotes. | Ajouter un critère de sélection écrit : demande locale observée, disponibilité de créateurs, couverture de situations distinctes. Consigner le métier retenu et la ville pour chaque décision, comme l'exige déjà la section 12. | [UX section 8 et section 12](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) ; [Rest of World repris en R6, les arnaques changent de forme selon le pays](https://restofworld.org/2025/linkedin-job-scams) |
| Conforme | Sans objet | `docs/UX/ux-research.md` | H8 ligne 83, section 12 lignes 229 et 231 | La recherche prévoit explicitement de comparer Brazzaville et Kinshasa et d'attribuer chaque constat à sa ville. Elle impose un second cycle hors des deux Congo avant toute généralisation. | Conserver ces règles et les relier à `lanceurs-metiers.md`, qui doit s'appuyer sur elles. | [UX H8 et section 12](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) |

[LogRocket](https://blog.logrocket.com/ux-design/using-concept-testing-product-design) rappelle que les plateformes sociales exigent des interactions entre personnes et qu'un prototype ne suffit pas à les reproduire. Cela soutient le choix de créateurs réels avant ouverture. Les guides de fake door recommandent d'écrire le seuil avant de lancer le test ([LaunchList](https://getlaunchlist.com/blog/fake-door-test)). Le seuil proposé ici est une décision à prendre, pas une statistique issue de ces sources.

### Inferences

- Défaut documentaire : le passage de six secteurs observés à trois métiers pilotes n'est pas tracé. La recherche UX et la croissance ne partagent pas encore le même artefact de décision.
- Décision opérationnelle à prendre : le nombre de créateurs, le rythme de publication et le seuil de fil acceptable relèvent d'un arbitrage. Les documents ne permettent pas de les déduire.
- La méthode reste défendable si elle est présentée comme un semis contrôlé par ville, avec mesure et repli, et non comme une supposition sur ce qui plaira au public.

### Gaps

- Aucune donnée de référence sur le nombre de vidéos nécessaires pour qu'un fil vertical paraisse non vide. Les chiffres proposés sont des décisions à valider sur le terrain.
- Aucune liste de métiers pilotes n'est fournie. Le document `lanceurs-metiers.md` n'existe pas encore.
- Aucune mesure de rétention des créateurs n'est prévue dans FS-11 au-delà de `video_published`.

## Les événements de mesure couvrent-ils la découverte, la conversion et la qualité de modération sans pistage intrusif ?

### Takeaway

La couverture découverte et conversion est bonne et la frontière technique visiteur est bien posée. Il manque deux éléments structurants : les dimensions ville, métier et campagne sur les événements, et tout événement de qualité de modération, alors que la modération est une promesse du MVP.

### Cited Findings

| Classement | Nature | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Majeur | Défaut documentaire | `docs/Product/prd.md`, `docs/Growth/README.md` et `docs/UX/ux-research.md` | FS-11 ligne 329 ; Growth ligne 13 ; UX lignes 217 et 218 | FS-11 impose seulement identifiant de session ou de compte, horodatage et plateforme. Growth demande une mesure par ville et UX demande des résultats ventilés par ville. Or `guest_session` contient métier et ville, mais aucun événement ne les porte. Aucun paramètre de campagne propre n'est prévu. | Ajouter aux événements les champs `city`, `trade` et `campaign_ref` issus de la session ou du lien de campagne, avec la même durée de conservation de trente jours et aucun identifiant d'appareil. | [HEART, démarche objectifs, signaux, mesures](https://research.google.com/pubs/archive/36299.pdf) ; [PRD FS-11 et section 8](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) ; [UX section 11](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) |
| Majeur | Défaut documentaire | `docs/Product/prd.md` et `docs/UX/ux-research.md` | FS-11 ligne 328 ; section 10 ligne 379 ; UX section 11 lignes 214 à 220 | La liste ne contient que `report_created` côté modération. Aucun événement ne mesure le délai de traitement, le résultat, la contestation, la réversion d'une décision ou la profondeur de file. Le tableau HEART n'a pas de catégorie modération. | Ajouter `report_resolved`, `moderation_action`, `appeal_opened`, `appeal_resolved`, `queue_depth` et `report_age`, avec motif, ville et durée, sans identité du signalant au delà de la référence pseudonyme. Aligner les alertes de la section 10 sur ces signaux. | [Base DSA transparence, déclaration de motifs et information sur les moyens automatisés](https://transparency.dsa.ec.europa.eu/page/documentation) ; [EDPB 3/2025, paragraphes 15 et 24, taux d'erreur et garanties](https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202503_interplay-dsa-gdpr_v2_en.pdf) ; [Google SRE, alertes actionnables sur les symptômes](https://sre.google/resources/practices-and-processes/incident-management-guide) |
| Majeur | Défaut documentaire | `docs/UX/ux-research.md` et `docs/Product/prd.md` | UX ligne 217 ; FS-11 ligne 329 | La mesure engagement est définie comme nombre moyen de `video_complete` par session visiteur. Or FS-11 remplace l'identifiant de session par l'identifiant de compte après inscription. Le dénominateur change de nature en cours de parcours. | Définir deux mesures distinctes : vidéos complétées par session sans compte, et vidéos complétées par compte et par période. Interdire la fusion des deux dénominateurs dans le tableau de bord. | [HEART, engagement rapporté par personne et non par total brut](https://research.google.com/pubs/archive/36299.pdf) ; [UX section 11](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) ; [PRD FS-11](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |
| Mineur | Décision opérationnelle à prendre | `docs/Product/prd.md` | FS-11 ligne 336 et section 10 ligne 373 | Le passage d'un identifiant de session courte à un identifiant de compte lors de `signup_verified` crée un pont entre comportement visiteur et identité permanente. La durée de trente jours est donnée pour les événements de session, mais pas pour les événements liés au compte. | Écrire explicitement quels événements restent anonymes, lesquels sont rattachés au compte, la base de traitement et la durée de conservation de chaque catégorie. Interdire le rattachement rétroactif d'événements antérieurs à l'inscription sans base documentée. | [EDPB lignes 03/2022, transparence, équité et minimisation des données dans les interfaces de réseaux sociaux](https://www.edpb.europa.eu/system/files/documents/2023-02/edpb_03-2022_guidelines_on_deceptive_design_patterns_in_social_media_platform_interfaces_v2_en_0.pdf) ; [PRD section 10](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |
| Conforme | Sans objet | `docs/Product/prd.md` | FS-11 lignes 330 et 331, section 10 ligne 373, section 11 ligne 389 | Aucun identifiant d'appareil permanent, aucun traceur tiers dans le parcours visiteur, conservation des événements de session à trente jours et revue de confidentialité dans la définition de terminé. | Conserver ces quatre garde-fous. | [PRD](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |

L'article [HEART, CHI 2010](https://research.google.com/pubs/archive/36299.pdf) insiste sur la démarche objectifs, signaux, mesures et sur le fait que les catégories ne fixent pas les seuils. Cela justifie d'ajouter les dimensions nécessaires au calcul avant de fixer des cibles chiffrées. Les [lignes directrices EDPB 3/2025](https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202503_interplay-dsa-gdpr_v2_en.pdf) rappellent que les erreurs de modération automatisée produisent un nombre absolu élevé même à faible taux, ce qui rend la mesure de la qualité indispensable dès le MVP.

### Inferences

- Défaut documentaire : trois incohérences internes sont corrigibles par texte, sans changement d'architecture. La plus grave est l'absence de `city` alors que deux villes sont le premier marché et que deux documents exigent une ventilation.
- Décision opérationnelle à prendre : le rattachement des événements pré inscription au compte et la durée de conservation associée sont des choix juridiques et produit, pas des omissions mécaniques.
- Conforme : le refus du traceur tiers et de l'empreinte d'appareil est non négociable dans les trois documents et ne doit pas être assoupli pour obtenir la ventilation par ville.

### Gaps

- Aucune source trouvée sur un taux d'erreur acceptable pour une modération vidéo en français à Brazzaville ou Kinshasa. Les seuils devront être fixés après la ligne de base.
- Aucun schéma de tableau de bord n'est fourni dans `mesure-campagnes.md`. Impossible de vérifier comment seront calculés les taux de conversion par ville.
- Aucun événement ne mesure l'exposition aux avertissements arnaque, alors que l'opportunité O4 de la recherche UX propose cet avertissement.

## Les documents proposés manquent-ils un élément opérationnel critique ?

### Takeaway

Oui. `incidents.md` n'est qu'un titre, aucune astreinte n'est décrite, et aucun document ne traite de la montée en charge. Ces trois absences sont bloquantes pour une ouverture publique dans deux villes, alors que les alertes techniques existent déjà dans le PRD.

### Cited Findings

| Classement | Nature | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Bloquant | Décision opérationnelle à prendre | `docs/Operations/README.md` | Tableau, aucun document dédié | Aucune astreinte n'est prévue : pas de tour de garde, pas de contact d'urgence, pas de titulaire, pas de passation. Le PRD section 10 prévoit des alertes sans destinataire nommé. | Créer `astreinte.md` avant la première mise en ligne : rôles coordinateur, communication, opérations, rotation hebdomadaire, canal unique, numéro d'urgence, règle de passation et exercice à blanc. | [Google SRE, Incident Management Guide, astreinte définie, playbooks, entraînement, rôles IC, CL et OL](https://sre.google/resources/practices-and-processes/incident-management-guide) ; [SRE Workbook, ligne de commande claire, rôles définis, journal de travail, déclaration précoce](https://sre.google/workbook/incident-response) |
| Majeur | Défaut documentaire | `docs/Operations/README.md` | `incidents.md`, ligne 12 | La question traitée couvre qui décide, qui coupe une fonction, comment on journalise. Aucun schéma de registre n'est défini : gravité, ville, fonction touchée, heure de début, décideur, action, lien avec les tickets de modération, postmortem. | Définir le schéma du registre d'incidents et l'obligation de postmortem sans blâme, avec actions correctives datées et relisables. | [Google SRE, journal de travail pendant l'incident et postmortem ouvert et sans blâme](https://sre.google/resources/practices-and-processes/incident-management-guide) ; [SRE Book, garder une trace du débogage et de l'atténuation](https://sre.google/sre-book/managing-incidents) |
| Bloquant | Décision opérationnelle à prendre | `docs/Operations/README.md` et `docs/Growth/README.md` | Aucun document dédié | Aucun plan de montée en charge n'est prévu, ni pour le volume de modération, ni pour le trafic vidéo et le coût CDN. Le PRD section 12 ligne 396 demande une mesure du coût pour 1 000 vidéos vues, sans seuil ni propriétaire. | Créer `montee-en-charge.md` : courbe de trafic et de signalements par ville, seuils de bascule, budget CDN, capacité de modération, action à chaque seuil, et propriétaire. Relier les seuils aux événements de la section 11. | [Google SRE, alertes basées sur des objectifs de service et préparation avant incident](https://sre.google/resources/practices-and-processes/incident-management-guide) ; [Google Cloud, procédures, rôles et voies d'escalade documentées et entraînement régulier](https://docs.cloud.google.com/architecture/framework/operational-excellence/manage-incidents-and-problems) |
| Majeur | Décision opérationnelle à prendre | `docs/Product/prd.md` | Section 12, lignes 396 et 399 | La mesure du coût vidéo et le roulement bénévole ou salarié n'ont ni seuil de déclenchement ni responsable. | Transformer chaque mesure en règle actionnable : seuil, propriétaire, action, délai. Par exemple, seuil de profondeur de file, seuil de coût pour 1 000 vidéos vues, seuil de taux d'échec d'envoi. | [Google SRE, une alerte non actionnable génère du bruit](https://sre.google/resources/practices-and-processes/incident-management-guide) ; [PRD section 12](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |
| Conforme | Sans objet | `docs/Product/prd.md` | Section 10, ligne 379 | La journalisation des erreurs, la mesure des temps de réponse et les alertes sur la file de modération et sur l'échec d'envoi vidéo constituent une base d'observability correcte. | Conserver cette base et y brancher les seuils et l'astreinte proposés. | [PRD section 10](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |

Le [guide SRE de Google](https://sre.google/resources/practices-and-processes/incident-management-guide) est explicite : la préparation comprend un mécanisme d'alerte fiable et un processus d'astreinte bien défini, et les playbooks ne servent que si les astreints en connaissent l'existence. Le [SRE Workbook](https://sre.google/workbook/incident-response) recommande une ligne de commande claire, des rôles définis, un journal de suivi et une déclaration précoce des incidents. Ces recommandations s'appliquent directement à un incident de modération, par exemple une vague de signalements ou une décision erronée massivement contestée.

### Inferences

- Défaut documentaire : `incidents.md` existe comme ligne de tableau, mais pas comme contenu. Le registre d'incidents est donc une intention, pas un artefact.
- Décision opérationnelle à prendre : l'astreinte et la montée en charge n'ont même pas de titre dans les deux README. Il faut d'abord décider qui est responsable, puis écrire les documents.
- Conforme : l'observability technique du PRD évite de repartir de zéro. Le manque porte sur l'organisation, pas sur la instrumentation.

### Gaps

- Aucune source ne permet de dimensionner une astreinte pour deux villes sans données de trafic. Le nombre de personnes et la rotation sont des décisions internes.
- Aucun budget n'est communiqué dans le PRD, ce qui empêche de chiffrer un plan de montée en charge CDN.
- Aucun scénario d'incident de modération, par exemple fausse suspension d'un créateur pilote, n'est décrit dans le périmètre audité.

## Les deux villes sont-elles traitées comme deux marchés distincts, sans extrapolation abusive ?

### Takeaway

La recherche UX est rigoureuse sur ce point, mais les documents Opérations et Croissance fusionnent les deux pays dans un seul fichier et une seule règle. Cette fusion crée un risque d'extrapolation dans l'acquisition, le dimensionnement de la modération et la mesure.

### Cited Findings

| Classement | Nature | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Majeur | Défaut documentaire | `docs/Growth/README.md` et `docs/Operations/README.md` | Growth `acquisition-congo.md`, ligne 9 ; Ops tableau, lignes 9 à 14 | Un seul document d'acquisition couvre Brazzaville et Kinshasa. Aucun document Opérations ne distingue les deux villes pour la modération, le support ou les incidents. La règle commune de gratuité est juste, mais elle masque les différences de moyens, de partenaires et de signaux de confiance. | Scinder en `acquisition-brazzaville.md` et `acquisition-kinshasa.md`, avec cibles, partenaires, phrases d'invitation et mesure distincts. Ajouter dans chaque document Opérations une colonne ville pour volume de modération, astreinte et registre d'incidents. | [UX R6, les arnaques changent de forme selon le pays et la pression locale](https://restofworld.org/2025/linkedin-job-scams) ; [UX H8 et section 12](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) |
| Majeur | Décision opérationnelle à prendre | `docs/Product/prd.md` | Section 2, ligne 22 | La ligne d'hypothèses unique République du Congo et RDC traite deux pays comme une seule entrée de cadrage, avec un statut retenu. | Conserver le marché commun comme intention, mais dédoubler les hypothèses opérationnelles par ville dans la section 2 ou dans un document d'acquisition, sans modifier le périmètre produit. | [UX section 16, le cycle couvre deux villes et deux pays et ne permet pas de conclure pour le reste de l'Afrique](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) ; [PRD section 2](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |
| Conforme | Sans objet | `docs/UX/ux-research.md` | Section 8 lignes 92 et 100, H8 ligne 83, section 12 ligne 229 | Le recrutement est équilibré six et six, quatre entretiens principales par ville, chaque situation représentée dans les deux villes autant que possible. Toute généralisation au continent exige un second cycle dans un autre pays. | Maintenir ces règles et les rendre visibles dans `acquisition-congo.md` avant sa scission. | [UX section 8 et section 12](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) |

L'article [Rest of World repris en R6](https://restofworld.org/2025/linkedin-job-scams) rapporte que les arnaques à l'emploi changent de forme selon le pays et la pression locale. C'est une source de presse, pas une mesure congolaise, mais elle suffit à refuser une copie identique des messages et des avertissements entre Brazzaville et Kinshasa. La recherche UX elle-même formule l'hypothèse H8 sur des différences de contraintes de données et de signaux de confiance entre les deux villes ([UX H8](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md)).

### Inferences

- Défaut documentaire : la fusion dans `acquisition-congo.md` n'est pas une erreur de fait, mais elle rend impossible une mesure par ville tant que les événements ne portent pas `city`.
- Décision opérationnelle à prendre : le découpage des équipes, des partenaires et des budgets par ville doit être arbitré avant d'écrire les deux documents d'acquisition.
- Conforme : la recherche UX fournit déjà la garde fou la plus importante. Le reste des documents doit s'y aligner au lieu de l'ignorer.

### Gaps

- Aucune donnée de taille de marché, de coût de connexion ou de réseau mobile n'est fournie par ville. Le PRD demande une mesure du coût pour 1 000 vidéos vues sur les réseaux congolais, sans la fournir.
- Aucune analyse juridique locale n'est disponible dans le périmètre audité. La section 10 du PRD évoque le Digital Services Act comme extension possible, sans équivalent pour les deux pays concernés.
- Aucune langue autre que le français n'est tranchée pour le cycle 1, question ouverte en fin du document UX.

## Y a-t-il des coquilles, des caractères U+2014 ou U+2013, des liens cassés ou des formulations non professionnelles ?

### Takeaway

Non pour les caractères interdits et les liens : aucun U+2014 ni U+2013 n'a été trouvé dans les quatre fichiers, et tous les liens locaux résolvent. Trois formulations ou libellés méritent toutefois une correction mineure, dont un risque de contradiction directe avec FS-01.

### Cited Findings

| Classement | Nature | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Conforme | Sans objet | Les quatre fichiers audités | Ensemble du fichier | Analyse automatique des quatre fichiers : aucune occurrence de U+2014 ni de U+2013. Les apostrophes courbes U+2019 sont présentes et acceptables. | Conserver l'usage actuel des tirets simples et des apostrophes courbes. | [Ops README](file:///home/espoir-loemba/work/Projects/pro/docs/Operations/README.md) ; [Growth README](file:///home/espoir-loemba/work/Projects/pro/docs/Growth/README.md) ; [PRD](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) ; [UX](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) |
| Conforme | Sans objet | Les quatre fichiers audités | Liens markdown | Les liens locaux vers `vision.md`, `manifeste.md`, `ia-defauts-et-tips.md` et `prd.md` pointent vers des fichiers existants. Aucun lien local cassé. | Maintenir la vérification lors de l'ajout des nouveaux documents Opérations et Croissance. | [PRD section 15](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) ; [UX en-tête](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) |
| Mineur | Défaut documentaire | `docs/Product/prd.md` | Section 12, ligne 398 | La mesure du risque inscription trop tôt dit de tester le parcours visiteur contre un mur de connexion au lancement. Cette formulation suggère d'introduire un mur, alors que FS-01 ligne 141 interdit tout écran bloquant avant trois vidéos et que la recherche UX interdit tout mur à l'entrée. | Réécrire : vérifier à la première ouverture qu'aucun mur de connexion n'apparaît avant trois vidéos, avec événements `app_open` et `feed_session_start`. | [PRD FS-01 et section 12](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) ; [UX section 12](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) |
| Mineur | Défaut documentaire | `docs/UX/ux-research.md` | J9 ligne 97 et section 12 ligne 230 | Les expressions hypothèses tuées et une hypothèse est tuée sont du registre oral. Le document utilise par ailleurs le terme infirmation dans le registre d'hypothèses. | Remplacer par hypothèses infirmées et une hypothèse est infirmée, pour rester cohérent avec la section 7. | [UX sections 7, 8 et 12](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md) |
| Mineur | Défaut documentaire | `docs/Growth/README.md` | `messagerie.md`, ligne 12 | Le nom `messagerie.md` peut être confondu avec le chat 1:1 du PRD FS-07, alors que le document porte sur les phrases d'invitation de campagne. | Renommer en `phrases-invitation.md` et mettre à jour la ligne du tableau. | [Growth README](file:///home/espoir-loemba/work/Projects/pro/docs/Growth/README.md) ; [PRD FS-07](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md) |

L'absence de U+2014 et U+2013 a été vérifiée par parcours direct des quatre fichiers. Les seuls caractères typographiques particuliers détectés sont des apostrophes courbes U+2019, conformes à la contrainte. Les liens locaux ont été résolus contre le système de fichiers, tous existent au moment de l'audit ([PRD](file:///home/espoir-loemba/work/Projects/pro/docs/Product/prd.md), [UX](file:///home/espoir-loemba/work/Projects/pro/docs/UX/ux-research.md)).

### Inferences

- Défaut documentaire : trois corrections purement rédactionnelles sont possibles sans changer le produit. La plus utile est la reformulation du risque inscription trop tôt, qui évite une lecture littérale contraire à FS-01.
- Conforme : la qualité typographique et les liens ne présentent pas de blocage. Aucune coquille bloquante n'a été identifiée dans le périmètre demandé.
- Aucune formulation promotionnelle aggregée n'est présente dans les quatre fichiers. Le ton reste factuel et professionnel, hormis le registre oral de deux expressions.

### Gaps

- Aucune vérification des URLs externes listées dans la section 17 de la recherche UX n'a été faite, car cette section est hors périmètre de la question 8.
- Aucune relecture linguistique approfondie n'a été menée hors des quatre fichiers audités.
- Les nouveaux documents annoncés dans les tableaux Opérations et Croissance n'existant pas, leurs futures coquilles ne peuvent pas être auditées aujourd'hui.
