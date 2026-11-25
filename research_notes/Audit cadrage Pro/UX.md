# Audit cadrage Pro UX et rédaction

Périmètre audité : six fichiers de `docs/UX` et `docs/Redaction/ia-defauts-et-tips.md`. Date : 25 novembre 2026. Aucun fichier de `docs` n'a été modifié. Chaque constat porte une classe : Bloquant, Majeur, Mineur ou Conforme. La colonne Type distingue un défaut documentaire d'un choix de recherche encore à décider.

## Q1 Distinction faits, hypothèses, décisions et inconnues

### Takeaway

La séparation est globalement bien faite : le document dit qu'aucune étude n'a eu lieu, il sépare décisions, preuves externes, hypothèses et questions ouvertes. Les faiblesses portent sur l'opérationnalisation des niveaux de confiance et sur une ligne de base annoncée avant qu'un protocole de mesure existe.

### Cited Findings

| Classe | Type | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Conforme | Défaut documentaire | `docs/UX/ux-research.md` | 1, 2, 6, 7, 15, 16 | Le livrable déclare qu'aucun entretien n'a eu lieu, il table les décisions avec leur source, il borne chaque preuve par une limite, il donne une condition d'infirmation par hypothèse et il liste les inconnues. | Conserver cette architecture et l'utiliser comme modèle pour les mises à jour. | [ux-research.md](../../docs/UX/ux-research.md), sections 1, 2, 6, 7, 15, 16 |
| Majeur | Défaut documentaire | `docs/UX/ux-research.md` | 7 | Les niveaux « Faible », « Moyenne faible » et « Moyenne » ne sont pas définis et aucun attributaire n'est nommé. Le lecteur ne peut pas savoir si H2 est plus fiable que H3 ni pourquoi. | Définir une échelle courte, par exemple 0 = spéculation, 1 = intuition d'équipe, 2 = indicé par une source externe, 3 = observé dans un contexte proche, et indiquer qui attribue le niveau et à quelle date. | [ISO 9241-210:2019](https://www.iso.org/standard/77520.html), principe 5.2 et exigence de compréhension explicite des utilisateurs |
| Majeur | Défaut documentaire | `docs/UX/ux-research.md` | 4 et 11 | Le document affirme que le cycle 1 sert à établir une ligne de base, mais le plan ne prévoit que six sessions J7 et J8 sur prototype et aucun protocole de benchmark répétable. Les mesures `signup_verified` et `video_complete` viennent de la télémétrie produit, pas d'un prototype cliquable. | Séparer deux lignes de base : une ligne qualitative de tâche sur prototype avec protocole écrit, et une ligne analytique après mise en production. Dire explicitement que la seconde n'existe pas encore. | [NN/G, 7 Steps to Benchmark Your Product's UX](https://www.nngroup.com/articles/product-ux-benchmarks/) |
| Majeur | Choix de recherche à décider | `docs/UX/ux-research.md` | 7, 8, 12 | Les seuils d'infirmation mélangent des dénominateurs incompatibles : 5 sur 8, plus de 7 sur 10, 6 sur 8, 4 sur 5. Aucun test prévu ne garantit 10 participants. | Choisir un dénominateur par test et l'inscrire dans le tableau J4 à J8, puis réécrire les conditions avec ce dénominateur. | [Rodden, Hutchinson et Fu, CHI 2010](https://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/36299.pdf), démarche objectifs, signaux, mesures |
| Conforme | Défaut documentaire | `docs/UX/ux-research.md` | 2 | Les décisions produit reprises dans le tableau concordent avec `decisions.md` et le PRD, notamment D-001, D-005, D-007 et D-012. | Maintenir la référence croisée lors de chaque révision. | [decisions.md](../../docs/Product/decisions.md), lignes D-001 à D-012 |

### Inferences

Le document est apte à cadrer la recherche, mais il n'est pas encore apte à produire une mesure comparable. Tant que les échelles de confiance et les dénominateurs restent flous, la règle de décision de la section 12 peut laisser entrer une opinion dans le PRD.

### Gaps

Je n'ai pas trouvé de procédure écrite pour décider qui valide une hypothèse confirmée et qui archive la preuve correspondante. Je n'ai pas trouvé non plus de définition du seuil à partir duquel une friction observée devient un constat, hors de la règle des 5 sur 8 en section 12.

## Q2 Adéquation des méthodes aux questions RQ1 à RQ3

### Takeaway

Les trois questions sont pertinentes au regard du produit, mais les dispositifs prévus ne sont pas encore spécifiés assez précisément pour y répondre. RQ1 manque de stimuli, RQ2 a un seuil impossible avec l'échantillon prévu, RQ3 n'exploite pas les signaux de risque pourtant cités en R7.

### Cited Findings

| Classe | Type | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Majeur | Choix de recherche à décider | `docs/UX/ux-research.md` | 5, 7, 8, 9 | RQ1 porte sur la crédibilité en moins de 60 secondes, mais le guide ne définit aucun stimulus vidéo. La question 6 demande d'imaginer une vidéo de 45 secondes et l'unique mesure est une note de 1 à 5 sur la compréhension de l'identité. | Préparer trois vidéos courtes par secteur avec variation contrôlée du geste visible, du contexte et du nom affiché, puis coder le geste de jugement avant l'opinion déclarée. | [ISO 9241-210:2019](https://www.iso.org/standard/77520.html), évaluation centrée utilisateur et solutions concrètes avant test |
| Majeur | Choix de recherche à décider | `docs/UX/ux-research.md` | 7 H4, 8 J8 | H4 fixe une condition à « plus de 7 personnes sur 10 abandonnent », alors que J8 prévoit six participants. Le test ne peut pas produire ce résultat. | Soit porter J8 à dix participants, soit réécrire la condition en nombre entier sur six, par exemple au moins cinq abandons sur six, et préciser ce qui compte comme abandon. | [Google Design, immersion trips](https://design.google/library/beyond-the-desktop-field-research) |
| Majeur | Choix de recherche à décider | `docs/UX/ux-research.md` | 5 RQ3, 9 O4 | Le scénario suspect de O4 n'est pas construit à partir des signaux documentés en R7 : demande d'informations sensibles 59 %, paiement initial 56 %, pression pour agir 45 %, sortie de plateforme 38 %. | Construire les deux scénarios avec ces quatre signaux et préenregistrer le geste attendu, par exemple ne pas répondre, demander une preuve ou signaler. | [LinkedIn Job Search Safety Pulse 2026](https://news.linkedin.com/2026/LinkedIn-Job-Search-Safety-Pulse) |
| Majeur | Choix de recherche à décider | `docs/UX/ux-research.md` | 7 H8 | H8 utilise comme condition d'infirmation « aucune différence observée entre les deux groupes ». Avec quatre personnes par ville, l'absence d'observation ne peut pas établir l'absence de différence. | Réécrire en signal exploratoire : aucun motif récurrent propre à une ville sur quatre entretiens par ville. Toute divergence observée devient une piste pour le cycle 2, pas une preuve. | [researcher.md](../../../.claude/skills/synced/fe7bce45-f835-4e39-a3c6-b8755d0389f9_7f8962d4-382f-44d6-b4f1-5f3c5f0b7678/deep-research/references/researcher.md), règle d'honnêteté épistémique |
| Majeur | Défaut documentaire | `docs/UX/ux-research.md` | 7 H6, H7 et 8 | H6 et H7 exigent cinq créateurs potentiels, alors que le recrutement principal ne prévoit que deux personnes qui créent déjà du contenu professionnel. La note « si le recrutement le permet » rend le test optionnel sans règle de décision. | Réserver cinq créateurs sur les douze recrutés, ou réduire explicitement l'objectif de H6 et H7 à deux entretiens exploratoires non décisionnels. | [ux-research.md](../../docs/UX/ux-research.md), sections 7 et 8 |
| Mineur | Défaut documentaire | `docs/UX/ux-research.md` | 8 J3, J9 | Le plan parle de « trio » alors que J1 et R1 mobilisent produit, design, développement et modération, soit quatre fonctions. | Remplacer « trio » par « équipe de cycle » ou préciser les trois rôles retenus et le sort de la modération. | [Google Design, immersion trips](https://design.google/library/beyond-the-desktop-field-research) |
| Conforme | Défaut documentaire | `docs/UX/ux-research.md` | 8 | Le guide part du vécu, demande un message réel si la personne l'accepte, interdit les questions suggestives et ouvre la porte à un refus d'enregistrement. | Conserver ce guide et ajouter les stimuli manquants en annexe. | [Google Design, immersion trips](https://design.google/library/beyond-the-desktop-field-research) |

### Inferences

Le plan de terrain est crédible comme immersion courte, mais il n'est pas encore un plan d'évaluation. Les entretiens exploratoires peuvent nourrir O1 à O5 ; ils ne peuvent pas, en l'état, trancher H4, H6, H7 et H8.

### Gaps

Je n'ai pas trouvé de protocole de test pour J7 et J8 : consigne, tâches, critères de réussite, enregistrement des gestes, grille de codage et pilotage. Je n'ai pas trouvé de définition opérationnelle de « regarder autour d'elle avant de taper son email », utilisée comme signal en O2. Je n'ai pas trouvé de source fiable sur la perception des arnaques à l'emploi spécifiquement à Brazzaville et Kinshasa ; R6 et R7 portent sur d'autres marchés.

## Q3 Défendabilité de l'échantillon pour deux villes et quatre profils

### Takeaway

Le volume de douze recrutés et huit entretiens est cohérent avec une immersion courte. La répartition annoncée est en revanche arithmétiquement ambiguë et ne permet pas de couvrir quatre situations dans deux villes avec huit personnes sans chevauchement explicite.

### Cited Findings

| Classe | Type | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Majeur | Défaut documentaire | `docs/UX/ux-research.md` | 8 | La somme des situations annoncées est 4 + 2 + 2 + 2 = 10 pour huit participants principaux. La phrase « les situations peuvent se chevaucher » ne dit pas lesquelles ni combien. | Remplacer par une matrice explicite : 1 chercheur d'emploi, 1 professionnel en poste, 1 créateur, 1 recruteur par ville, puis nommer les chevauchements autorisés, par exemple créateur et chercheur d'emploi. | [NN/G, Journey-Mapping Impact](https://www.nngroup.com/articles/journey-mapping-impact/), facteur « selecting the right persona or segment » |
| Majeur | Choix de recherche à décider | `docs/UX/ux-research.md` | 8, 12, 16 | Huit personnes ne peuvent pas saturer deux villes, quatre situations et six secteurs. La règle de généralisation en section 12 est prudente, mais le plan donne l'impression d'une couverture complète. | Écrire que l'échantillon sert à repérer des motifs, pas à estimer une prévalence ni à comparer statistiquement les deux villes. Limiter le terrain à deux ou trois secteurs par ville pour garder de la profondeur. | [Google Design, immersion trips](https://design.google/library/beyond-the-desktop-field-research), 8 à 10 participants |
| Conforme | Défaut documentaire | `docs/UX/ux-research.md` | 8 | Le plan recrute douze personnes, six par ville, dont quatre réserves, et il mélange explicitement les secteurs plutôt que de limiter à la tech. | Conserver ce principe et documenter la liste anonymisée P1 à P12. | [ux-research.md](../../docs/UX/ux-research.md), section 8 |
| Mineur | Choix de recherche à décider | `docs/UX/ux-research.md` | 15 et 8 | La question d'inclure deux participants anglophones reste ouverte en fin de document, mais le questionnaire de sélection ne demande pas la langue d'usage. | Ajouter la langue d'usage au questionnaire de sélection avant J2, quelle que soit la décision finale. | [ux-research.md](../../docs/UX/ux-research.md), sections 8 et 15 |

### Inferences

L'échantillon est défendable pour une première immersion si l'équipe accepte d'en limiter la portée. Il ne l'est pas pour valider des personas, des différences inter-villes ou des seuils chiffrés.

### Gaps

Je n'ai pas trouvé de budget, de durée de recrutement par ville ni de critère d'exclusion lié à la connectivité ou au type de téléphone. Ces éléments conditionnent pourtant la possibilité de tester la lecture vidéo en contexte réel.

## Q4 Personas fictifs et dérivés des hypothèses

### Takeaway

Le fichier dit clairement que les profils sont fictifs et non validés. Un lien vers une décision ouverte et un rôle de phase 2 présenté sans balise suffisante affaiblissent cette prudence.

### Cited Findings

| Classe | Type | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Conforme | Défaut documentaire | `docs/UX/personas.md` | En-tête et fin | Le statut porte « non validées sur le terrain », l'usage dit que les profils servent à discuter, et la dernière section interdit de justifier une fonctionnalité par un personnage seul. | Conserver ces garde-fous. | [personas.md](../../docs/UX/personas.md), en-tête et « Ce que ces personas ne disent pas » |
| Majeur | Défaut documentaire | `docs/UX/personas.md` | Personne 3 | Chantal est reliée à « H2, H5 et décision D-010 ». Or D-010 est une décision ouverte sur la vérification N2 des candidatures, en phase 2, et non une hypothèse de recherche. Le profil recruteur est par ailleurs hors MVP selon le PRD. | Retirer D-010 des hypothèses liées, garder H5 et ajouter la mention « profil exploratoire, hors cycle 1 et hors MVP ». | [decisions.md](../../docs/Product/decisions.md), D-010 ; [PRD](../../docs/Product/prd.md), sections 3.2 et 4 |
| Mineur | Défaut documentaire | `docs/UX/personas.md` | Personnes 4 et 5 | Le modérateur et le propriétaire d'organisation n'ont pas de mention locale de fictionalité, contrairement aux trois autres cartes qui portent un prénom et un contexte. Le lien direct vers FS-09 ou la section 14 peut laisser croire à un profil validé. | Ajouter « profil fictif, hors cycle 1 » sur ces deux cartes et remplacer le lien direct par un lien vers l'opportunité ou la phase concernée. | [NN/G, 3 Persona Types](https://www.nngroup.com/articles/persona-types/) |
| Mineur | Doublon | `docs/UX/personas.md` | Personnes 1 à 3 | Les signaux qui rassurent reprennent presque mot pour mot H1, H4, H8, H6, H7, H2 et H5 déjà détaillés dans la recherche. | Garder les identifiants d'hypothèses et une seule tension par persona. Laisser les preuves et conditions d'infirmation dans `ux-research.md`. | [NN/G, Research Repositories 101](https://www.nngroup.com/videos/research-repositories-101/) |

### Inferences

Les personas jouent leur rôle de support de discussion. Ils deviennent risqués dès qu'un identifiant de décision ou de spécification est traité comme une preuve utilisateur.

### Gaps

Je n'ai pas trouvé de règle de remplacement des personas après le cycle 1 : qui décide qu'un profil est corrigé, supprimé ou conservé, et dans quel document la version révisée fait foi.

## Q5 Couverture des parcours et des chemins d'erreur du PRD

### Takeaway

Les quatre parcours couvrent bien les événements de mesure, mais ils omettent plusieurs branches d'erreur explicitement écrites dans le PRD. Un parcours introduit aussi une règle de blocage absente du PRD, ce qui crée deux sources de vérité.

### Cited Findings

| Classe | Type | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Majeur | Défaut documentaire | `docs/UX/userflow.md` | Parcours A | Le PRD prévoit un chemin pour le visiteur qui refuse la lecture automatique et un chemin d'expiration de session sans identifiant permanent. Le parcours A n'a ni l'un ni l'autre. | Ajouter deux embranchements : lecture manuelle après refus, et fin de session avec retour au fil sans conservations côté serveur. | [PRD FS-01](../../docs/Product/prd.md) |
| Majeur | Défaut documentaire | `docs/UX/userflow.md` | Parcours B et C | Manquent la suggestion modifiable de métier et ville à l'inscription (FS-03), le message affiché au visiteur qui touche Publier (FS-05), la limite de dix commentaires par minute (FS-06), l'état vide avec retrait d'un filtre (FS-08), l'envoi à soi-même interdit et la limite de 20 messages par minute (FS-07). | Ajouter ces six embranchements aux parcours concernés, avec le libellé d'erreur attendu. | [PRD FS-03, FS-05, FS-06, FS-07, FS-08](../../docs/Product/prd.md) |
| Majeur | Défaut documentaire | `docs/UX/userflow.md` | Parcours B | Les états `draft`, `uploading` et `rejected` du PRD n'apparaissent pas. Seuls `pending_review`, `published` et le retrait sont visibles. | Nommer ces états dans le parcours, en particulier le passage à `rejected` et la voie de contestation associée. | [PRD section 9](../../docs/Product/prd.md) |
| Majeur | Défaut documentaire | `docs/UX/userflow.md` | Parcours C | La branche « le destinataire bloque après réception, la conversation reste lisible mais l'envoi suivant est refusé » n'existe pas dans le PRD. Le fichier dit pourtant que les critères restent dans le PRD. | Déplacer cette règle dans FS-07 ou la marquer comme hypothèse à valider, avec un identifiant H ou O. | [PRD FS-07](../../docs/Product/prd.md) ; [README des docs](../../docs/README.md), règle de mise à jour |
| Majeur | Défaut documentaire | `docs/UX/userflow.md` | Parcours C et A | Le moment de la demande d'autorisation push n'est pas montré. Le PRD impose une demande après la première action significative, jamais au lancement. Le lien direct depuis une notification n'apparaît pas non plus. | Placer explicitement le point de demande après la première action significative et ajouter la branche « notification touchée mène à l'élément ». | [PRD FS-10](../../docs/Product/prd.md) |
| Mineur | Défaut documentaire | `docs/UX/userflow.md` | Parcours D | La contestation est décrite comme un lien, sans préciser le canal email et le lien unique du PRD. La branche « signalement sans motif précis » est ambiguë parce que « autre » est un motif autorisé. | Écrire « contestation par email avec lien unique relié au ticket d'origine » et distinguer « motif autre » de « aucun motif sélectionné ». | [PRD FS-09](../../docs/Product/prd.md) |
| Conforme | Défaut documentaire | `docs/UX/userflow.md` | Parcours A à D | Les douze événements de FS-11 sont couverts : huit en A, deux en B, un en C, un en D. Les branches signalement visiteur, blocage avant fenêtre, code expiré, coupure réseau et refus push sont présentes. | Conserver la liste d'événements en fin de parcours. | [PRD FS-11](../../docs/Product/prd.md) |

### Inferences

Le fichier est une bonne vue d'ensemble des chemins nominaux. Il n'est pas encore une spécification d'erreurs complète. Avant le code, les développeurs devraient lire le PRD en parallèle pour ne pas manquer six branches documentées.

### Gaps

Je n'ai pas trouvé d'états d'erreur pour la modération asynchrone quand la file est saturée, hors alerte infrastructure du PRD. Je n'ai pas trouvé de parcours pour la modification ou la suppression du profil public, alors que FS-04 prévoit la possibilité de masquer ville et bio.

## Q6 Histoires reliées aux FS et à une priorité comprise

### Takeaway

Toutes les histoires portent un lien PRD et une priorité. La priorité elle-même n'est pas définie, et plusieurs histoires contredisent le périmètre MVP ou omettent le lien avec les opportunités exigé par les règles internes.

### Cited Findings

| Classe | Type | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Conforme | Défaut documentaire | `docs/UX/userstories.md` | Phases 1 et 2 | Les seize histoires ont un identifiant, un rôle, une action, un bénéfice, une priorité et un lien vers une FS ou une section du PRD. | Conserver la table comme backlog lisible. | [userstories.md](../../docs/UX/userstories.md) |
| Majeur | Défaut documentaire | `docs/UX/userstories.md` | En-tête et phase 1 | P0 et P1 ne sont pas définis. US-10 sur les notifications est en P1 alors que FS-10 et les notifications push figurent explicitement dans le MVP au PRD section 3.1. | Ajouter une légende : P0 = obligatoire pour le MVP, P1 = phase suivante. Passer US-10 en P0 ou sortir FS-10 du MVP dans le PRD avec une date et un motif. | [PRD](../../docs/Product/prd.md), sections 3.1 et FS-10 |
| Majeur | Défaut documentaire | `docs/UX/userstories.md` | Règle 3 et tableaux | La règle 6 du fichier et le README imposent un rattachement à une opportunité de recherche. Les tableaux ne donnent que le lien PRD, sans colonne O1 à O5 ni identifiant H. | Ajouter une colonne « Opportunité ou hypothèse », par exemple US-01 à O2, US-03 à H3 et O3, US-07 à O4, US-09 à RQ3 et O4. | [ux-research.md](../../docs/UX/ux-research.md), section 9 ; [README des docs](../../docs/README.md), règle de mise à jour ligne 34 |
| Majeur | Défaut documentaire | `docs/UX/userstories.md` | US-06 | Le bénéfice « construire un fil qui me ressemble » suggère une personnalisation à partir d'un historique, ce que le PRD exclut explicitement pour le MVP. | Réécrire en « afin de retrouver ce qui m'a intéressé pendant la session » ou préciser que la sauvegarde reste volontaire et liée au compte. | [PRD](../../docs/Product/prd.md), sections 3.2 et FS-08 |
| Majeur | Défaut documentaire | `docs/UX/userstories.md` | US-16 | L'histoire est marquée P1 et reliée à la section 13 du PRD, qui est une question ouverte, et à D-010, décision ouverte. Le registre interdit d'entrer une décision ouverte dans un sprint. | Remplacer le lien par « à confirmer, D-010 » et retirer la priorité tant que la décision n'est pas retenue. | [decisions.md](../../docs/Product/decisions.md), D-010 et règle « Comment rouvrir une décision » |
| Mineur | Défaut documentaire | `docs/UX/userstories.md` | Phase 2 | Les histoires US-12 à US-16 portent toutes P1, comme si elles étaient prioritaires dans le même backlog que le MVP. | Avec la légende proposée, indiquer que P1 en phase 2 signifie « à préparer, hors sprint MVP ». | [userstories.md](../../docs/UX/userstories.md), phases 1 et 2 |

### Inferences

Le backlog est lisible, mais il ne respecte pas encore sa propre règle de traçabilité. Le risque concret est qu'une histoire sans opportunité soit programmée parce qu'elle porte un lien FS.

### Gaps

Je n'ai pas trouvé de propriétaire ni de définition de « terminé » côté histoire hors du PRD. Je n'ai pas trouvé de règle pour déprioriser une histoire quand une hypothèse est infirmée.

## Q7 Doublons entre research, personas, userflow et userstories

### Takeaway

L'alias `usertories.md` est un choix assumé. Les doublons réels sont la section 10 de la recherche, qui recopie un parcours, et la reprise des hypothèses dans les personas.

### Cited Findings

| Classe | Type | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Conforme | Défaut documentaire | `docs/UX/usertories.md` | Fichier entier | Le fichier est un renvoi explicite vers `userstories.md`, et le lien local fonctionne. Le nom est aussi annoncé dans le README des docs. | Conserver l'alias tel quel. | [usertories.md](../../docs/UX/usertories.md) ; [README des docs](../../docs/README.md), ligne 14 |
| Majeur | Doublon | `docs/UX/ux-research.md` | 10 | Le tableau « Parcours à valider, version provisoire » reprend les étapes du parcours A de `userflow.md` et y ajoute des pensées hypothétiques. Deux représentations du même chemin coexistent avant le code. | Remplacer le tableau par un lien vers le parcours A et garder dans la recherche uniquement les frictions et émotions à confirmer, avec identifiants d'hypothèses. | [NN/G, Research Repositories 101](https://www.nngroup.com/videos/research-repositories-101/) ; [README des docs](../../docs/README.md), règles de mise à jour |
| Mineur | Doublon | `docs/UX/personas.md` | Personnes 1 à 3 | Les signaux et freins recopient les hypothèses H1 à H8 sans ajouter de synthèse nouvelle. | Remplacer les listes longues par une tension courte par persona et un renvoi aux identifiants H. | [NN/G, Research Repositories 101](https://www.nngroup.com/videos/research-repositories-101/) |
| Mineur | Doublon | `docs/Redaction/ia-defauts-et-tips.md` | 6 | La grille dit qu'elle s'applique au document de vision et au manifeste, alors que la règle typographique du README couvre tous les fichiers du dossier, y compris UX. | Étendre la phrase aux dossiers `UX`, `Product`, `Redaction` et aux futurs dossiers. | [README des docs](../../docs/README.md), ligne 4 |
| Conforme | Défaut documentaire | `docs/UX/userstories.md` | Règle 5 | Les critères d'acceptation ne sont pas dupliqués dans le backlog, ils restent dans le PRD. | Conserver cette séparation. | [userstories.md](../../docs/UX/userstories.md) |

### Inferences

La duplication la plus dangereuse est celle du parcours : une correction faite dans un fichier et pas dans l'autre laisserait le design et le développement diverger. Les autres redondances sont surtout des coûts de maintenance.

### Gaps

Je n'ai pas trouvé d'index des artefacts UX indiquant lequel fait foi pour chaque type d'information. Le README donne une hiérarchie partielle, mais pas de table « artefact canonique, contenu, voisin non canonique ».

## Q8 Accessibilité, consentement et confidentialité

### Takeaway

Le consentement de recherche est bien cadré. L'accessibilité est traitée de manière trop générale dans les livrables UX, et le report des sous-titres en phase 2 entre en conflit avec une exigence de base WCAG pour des vidéos avec son.

### Cited Findings

| Classe | Type | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Bloquant | Défaut documentaire | `docs/UX/userflow.md` et `docs/UX/ux-research.md` | Parcours B et section 12 | Les sous-titres automatiques sont renvoyés en phase 2 dans le PRD, et aucun artefact UX ne prévoit de sous-titres ou de transcription pour les vidéos avec son du MVP. | Trancher avant le code : soit sous-titrer les vidéos du MVP, soit garantir une expérience sans audio avec transcription validée, soit exclure le son du MVP. Écrire le choix dans le PRD et le parcours B. | [W3C WCAG 2.2, SC 1.2.2 Captions](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html), niveau A |
| Majeur | Défaut documentaire | `docs/UX/userflow.md` | Parcours A à D | Aucun parcours ne mentionne le lecteur d'écran, l'ordre de focus, le contraste, le mouvement réduit pour la lecture automatique ou la taille des cibles. Le PRD cite 44 pixels sans dire que WCAG 2.2 AA exige 24 x 24 pixels CSS pour le web. | Ajouter une ligne « critères accessibilité » par parcours : libellés, focus, contraste, cibles web 24 x 24 CSS px et recommandation iOS 44 pt, mouvement réduit. | [W3C WCAG 2.2, SC 2.5.8 Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) ; [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/design-principles) |
| Majeur | Défaut documentaire | `docs/UX/ux-research.md` | 13 | Le consentement, la suppression des enregistrements à trente jours et l'absence de données réelles sont écrits. Il manque le cycle de vie des notes et transcriptions, la base légale, le responsable de traitement, la date limite de retrait et le traitement des citations avec ville et secteur dans un échantillon de huit personnes. | Ajouter un petit tableau : donnée, finalité, conservation, accès, suppression. Préciser que les citations sont revues avant publication et que le retrait reste possible jusqu'à J10. | [PRD section 10 Confidentialité](../../docs/Product/prd.md) ; [ISO 9241-210:2019](https://www.iso.org/standard/77520.html), expérience utilisateur dans son ensemble |
| Conforme | Défaut documentaire | `docs/UX/ux-research.md` | 13 | Consentement avant prise de notes, refus d'enregistrement accepté, adresse de test fournie, aucun CV ni pièce d'identité demandé, pas de conseil juridique en cas d'arnaque. | Conserver ces règles et les reporter dans le protocole J2. | [ux-research.md](../../docs/UX/ux-research.md), section 13 |
| Conforme | Défaut documentaire | `docs/UX/userflow.md` | Parcours D | Le signalement est ouvert au visiteur et le ticket utilise une référence pseudonyme, ce qui respecte l'absence d'identifiant permanent visiteur. | Maintenir cette règle et vérifier qu'elle tient dans la réponse API. | [PRD FS-09 et section 8](../../docs/Product/prd.md) |

### Inferences

Le consentement est au niveau attendu pour une recherche qualitative. L'accessibilité reste au stade de déclaration d'intention. Le point bloquant n'est pas une coquille : il concerne une fonctionnalité centrale du MVP.

### Gaps

Je n'ai pas trouvé de politique de conservation des notes de recherche au-delà des enregistrements. Je n'ai pas trouvé de décision sur les langues des sous-titres, alors que le marché vise deux pays francophones et que la question de l'anglais reste ouverte.

## Q9 Artefacts UX manquants et qualité rédactionnelle

### Takeaway

Les contrôles mécaniques sont bons : aucun tiret cadratin ou demi-cadratin dans les six fichiers, aucun lien relatif cassé, et les chiffres externes vérifiés concordent avec leurs sources. Il manque surtout une carte de parcours visuelle, des principes de design d'interface et un référentiel de preuves.

### Cited Findings

| Classe | Type | Fichier | Section | Problème exact | Correction proposée | Source |
|---|---|---|---|---|---|---|
| Majeur | Artefact manquant | `docs/UX/userflow.md` | Ensemble | Les parcours sont des listes numérotées. Il n'existe pas de carte de parcours visuelle avec acteur, scénario, phases, actions, pensées, courbe émotionnelle et opportunités. La section 10 de la recherche n'en tient pas lieu. | Créer `docs/UX/journey-map.md` avec un acteur et un scénario par carte, puis relier chaque creux émotionnel à O1 à O5. Marquer la version actuelle comme issue d'hypothèses. | [NN/G, Journey Mapping 101](https://www.nngroup.com/articles/journey-mapping-101/) ; [NN/G, journey-mapping workshop](https://www.nngroup.com/articles/journey-mapping-workshop/) |
| Majeur | Artefact manquant | `docs/UX/ux-research.md` | 1 et 6 | Apple sert de grille de critique, mais il n'existe pas de principes de design propres à Pro, stables et opposables avant le code. | Créer `docs/UX/design-principles.md` en cinq à huit principes, par exemple public avant compte, identité au geste social, preuve de travail avant badge, réversibilité des actions, accessibilité par défaut, aucun identifiant permanent visiteur. | [Apple Human Interface Guidelines, design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles) ; [ISO 9241-210:2019](https://www.iso.org/standard/77520.html) |
| Majeur | Artefact manquant | `docs/UX/ux-research.md` | 8 et 13 | Les notes anonymisées, les formulaires de consentement, les stimuli, la grille de codage et les versions du guide n'ont pas d'emplacement ni de règle de nommage. | Définir un référentiel de recherche avec P1 à P12, identifiants de session, version du guide, stimuli, notes, citations et décisions issues de chaque constat. | [NN/G, Research Repositories 101](https://www.nngroup.com/videos/research-repositories-101/) |
| Conforme | Défaut documentaire | Six fichiers | Contrôle mécanique | Aucune occurrence de U+2014 ni de U+2013. Tous les liens relatifs pointent vers un fichier existant. Les URL externes testées répondent, sauf ACM qui renvoie un défi anti-bot mais dont la copie PDF Google fonctionne. | Maintenir la passe 1 de la grille de relecture avant chaque commit documentaire. | [ia-defauts-et-tips.md](../../docs/Redaction/ia-defauts-et-tips.md), section 4 |
| Conforme | Défaut documentaire | `docs/UX/ux-research.md` | 6 et 17 | Les chiffres vérifiés concordent : 80,6 millions et 70,1 millions de comptes fictifs, 72 %, 29 %, 28 %, 22 % et 21 % du Safety Pulse, cinq jours et 8 à 10 participants chez Google, HEART chez Rodden et NN/G. | Conserver les mentions de limite qui accompagnent chaque source. | [Rest of World](https://restofworld.org/2025/linkedin-job-scams) ; [LinkedIn Safety Pulse](https://news.linkedin.com/2026/LinkedIn-Job-Search-Safety-Pulse) ; [Google Design](https://design.google/library/beyond-the-desktop-field-research) ; [HEART, PDF](https://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/36299.pdf) |
| Conforme | Défaut documentaire | `docs/Redaction/ia-defauts-et-tips.md` | 2 | Les valeurs avancées pour Graphite et TextPulse concordent avec les pages source : environ huit fois moins de tirets pour GPT-6 Astra, rythme proche de l'humain pour Claude Opus 5, et d = 1,57, 1,12 et 1,31 pour la réécriture. | Conserver les références et leurs limites d'échantillon. | [Graphite AI Tells](https://graphite.io/research/ai-tells) ; [TextPulse](https://textpulse.ai/research/ai-style-fingerprints) |
| Mineur | Défaut documentaire | `docs/UX/ux-research.md` | 9 J9 et 12 | Les formulations « hypothèses confirmées ou tuées » et « une hypothèse est tuée » sont combatives et inhabituelles dans un livrable produit. | Remplacer par « confirmées ou infirmées » et « une hypothèse est infirmée ». | [ia-defauts-et-tips.md](../../docs/Redaction/ia-defauts-et-tips.md), section 3, ligne « Vocabulaire gonflé » |
| Mineur | Défaut documentaire | `docs/UX/ux-research.md` | 1 et 6 | Le texte attribue six principes à Apple. La page actuelle en donne huit : Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight. | Écrire « huit principes, dont six retenus ici comme grille de critique » ou ajouter Simplicity et Craft à la liste. | [Apple HIG, design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles) ; [WWDC26, Principles of great design](https://developer.apple.com/videos/play/wwdc2026/250) |
| Mineur | Défaut documentaire | `docs/Redaction/ia-defauts-et-tips.md` | 1 | « Une étude de 2025 rapporte que 94 % des copies d'examen rédigées par ChatGPT n'ont pas été repérées ». L'article est de juillet 2025, mais l'étude rapportée est datée de 2024 dans l'article. | Réécrire en « Une étude de 2024, rapportée en 2025, ... ». | [The Conversation](https://theconversation.com/too-many-em-dashes-weird-words-like-delves-spotting-text-written-by-chatgpt-is-still-more-art-than-science-259629) |
| Mineur | Défaut documentaire | `docs/Redaction/ia-defauts-et-tips.md` | 1 et 7 | Le retrait du classificateur OpenAI est appuyé sur [8], un blog commercial. La source primaire existe et donne les chiffres 26 % et 9 %. | Remplacer [8] par l'annonce OpenAI, ou conserver [8] comme source secondaire en ajoutant la source primaire. | [OpenAI, New AI classifier](https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text) |
| Mineur | Défaut documentaire | `docs/UX/ux-research.md` | 17 R7 | La référence pointe vers une URL Adobe AEM opaque. Le lien fonctionne, mais une page publique stable existe. | Ajouter l'URL publique `https://news.linkedin.com/2026/LinkedIn-Job-Search-Safety-Pulse` comme source préférée et garder le PDF en miroir. | [LinkedIn Safety Pulse 2026](https://news.linkedin.com/2026/LinkedIn-Job-Search-Safety-Pulse) |

### Inferences

Le socle documentaire est propre sur la forme. Les manques sont structurels : sans carte de parcours, sans principes de design et sans référentiel de preuves, l'équipe peut coder avec des documents cohérents entre eux mais non opposables sur les décisions d'interface.

### Gaps

Je n'ai pas trouvé de maquettes ni de style guide visuel dans le périmètre audité, ce qui empêche de vérifier l'application concrète des principes. Je n'ai pas trouvé de source fiable permettant de dire si l'absence de tirets cadratins dans ces fichiers vient d'une relecture humaine ou d'une consigne appliquée par un modèle. Les deux sont possibles et la grille le reconnaît elle-même.

***

Synthèse finale pour le rapport général : aucune cause d'arrêt immédiat autre que la question bloquante des sous-titres. Les autres points sont des corrections documentaires ou des décisions de recherche à trancher avant d'écrire le code. Le lot le plus rentable est, par ordre : trancher les sous-titres, aligner les parcours sur les chemins d'erreur du PRD, corriger les seuils et l'échantillon, ajouter la colonne opportunité dans les histoires, puis créer la carte de parcours et les principes de design.
