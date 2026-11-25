# Pro : recherche UX et cadrage produit

**Statut** : version 2, 25 novembre 2026  
**Commanditaire** : équipe produit Pro  
**Nature du livrable** : plan de recherche exécutable et synthèse des preuves disponibles  
**Premier marché** : République du Congo (Brazzaville) et RDC (Kinshasa)  
**Documents liés** : [PRD](../Product/prd.md), [Décisions](../Product/decisions.md), [Mesure](../Product/mesure.md), [Parcours](./userflow.md), [Carte de parcours](./journey-map.md), [Principes de design](./design-principles.md), [Référentiel de recherche](./referentiel-recherche.md), [Grille de relecture](../Redaction/ia-defauts-et-tips.md)

## 1. Ce que ce document est

Ce document cadre la recherche avant l'écriture du code. Il contient un problème formulé une seule fois, trois questions de recherche, un registre d'hypothèses avec échelle de confiance et dénominateurs, un plan de terrain de dix jours ouvrés, un arbre d'opportunités et des règles de décision.

Aucun entretien n'a encore eu lieu pour Pro. Les chiffres présentés viennent de sources publiques. Chaque affirmation porte une source ou un identifiant d'hypothèse. Ce document ne rapporte aucune donnée de participant.

La forme s'inspire de pratiques documentées. Google décrit des immersions de cinq jours avec 8 à 10 participants. LogRocket recommande un seul énoncé de problème, une à trois questions et des cycles courts. Teresa Torres relie résultat, opportunités, solutions et tests. Apple publie huit principes de design, dont six sont retenus ici comme grille de critique : finalité, liberté d'action, responsabilité, familiarité, souplesse et plaisir. Ces principes servent à critiquer une interface, jamais à prouver un besoin. Les principes propres à Pro sont écrits dans [design-principles.md](./design-principles.md).

## 2. Décisions déjà prises et ce qu'elles imposent

| Décision | Source | Ce que la recherche doit éclairer |
|---|---|---|
| Lecture publique sans compte, identité au premier geste social | D-001, [Décisions](../Product/decisions.md), PRD FS-01 | Le moment précis où la personne accepte de s'identifier |
| Vidéo courte et authentique, 60 secondes maximum | PRD FS-02 | Ce qui rend une vidéo croyable |
| Métier et ville choisis à la première ouverture, sans compte | PRD FS-03 | Si ces deux filtres sont les premiers réflexes |
| Langues : « Français d'abord. Les langues suivantes sont validées marché par marché, avec date et responsable inscrits au registre. Aucune autre langue n'est datée dans ce cadrage. » | D-008, [Décisions](../Product/decisions.md) | Le terrain du cycle 1 se déroule en français ; aucune autre langue n'est programmée |
| Sous-titres du MVP : « Les vidéos avec son du MVP disposent de sous-titres générés automatiquement et corrigés par l'auteur avant publication. Si la correction n'est pas faite, la vidéo reste en brouillon et n'est pas publiée. » | D-021, [Décisions](../Product/decisions.md), parcours B | La correction des sous-titres fait partie de la préparation de la vidéo et du contrôle en modération |
| Gratuité totale pendant l'acquisition | D-005, PRD section 14.5 | Si la confiance vient de la preuve de travail plus que d'un badge |
| Chat 1:1 entre membres | PRD FS-07 | Ce qui rassure avant de répondre à un inconnu |
| Aucun identifiant permanent pour le visiteur | D-012, [Décisions](../Product/decisions.md) | Aucune solution proposée ne réintroduit de suivi permanent |
| deux Congo d'abord | D-007, PRD section 2 | Aucune extrapolation au continent sans second cycle |

Les définitions de mesure et les dénominateurs canoniques relèvent de [mesure.md](../Product/mesure.md). D-009 est retenue et décrite dans `../Technique/adr-001-stack.md`. Les niveaux D-010 et D-011 restent des questions ouvertes du registre et n'orientent pas le cycle 1.

**Plateformes.** La dimension `plateforme` prend trois valeurs : `mobile` pour les applications natives iOS et Android sur téléphone, `web` pour le site responsive dans un navigateur, `desktop` pour l'application exécutable Windows et macOS. Linux est différé. Les trois plateformes sont livrées ensemble. Le cycle 1 couvre les trois plateformes déclarées, `mobile`, `web` et `desktop`, sans présumer que les usages desktop soient identiques au mobile.

## 3. Énoncé de problème

Les personnes en recherche d'emploi, d'abord à Brazzaville et Kinshasa, doivent juger si un contact vaut leur temps avant de donner leurs données, mais les réseaux professionnels demandent souvent un profil complet avant de montrer une preuve de travail, et la multiplication des offres trompeuses rend chaque message risqué. Pro doit permettre de voir une personne faire son métier en quelques secondes, puis de nouer un contact avec une identité suffisante, sans transformer la découverte en parcours publicitaire.

Si ce problème change, le document est réécrit plutôt que complété.

## 4. Résultat visé et deux lignes de base

Le résultat visé est un comportement produit : augmenter la part des visiteurs qui, dans une seule session, parviennent à nommer une personne ou un métier utile, puis acceptent de s'identifier pour conserver une vidéo ou envoyer un message.

La valeur de départ n'est pas connue. Deux lignes sont donc distinctes et ne doivent pas être confondues :

| Ligne | Ce que c'est | Protocole | État |
|---|---|---|---|
| Qualitative | Tâches sur prototype lors de J7 et J8, avec consigne, gestes codés et critères de réussite écrits avant le test | Guide version 2, stimuli enregistrés dans le [référentiel](./referentiel-recherche.md) | À exécuter au cycle 1 |
| Analytique | Mesures de télémétrie produit, par exemple `signup_verified` et `video_complete`, avec population et période définies dans [mesure.md](../Product/mesure.md) | Formules et événements source du dictionnaire de mesures | **N'existe pas encore.** Aucune valeur de départ analytique n'est annoncée dans ce cadrage |

Le retour à J7 portera sur les comptes seulement. Aucun identifiant permanent visiteur n'étant autorisé, aucun panel visiteur consenti n'est prévu dans ce cadrage.

## 5. Questions de recherche

| Question | Dispositif | Stimulus et mesure |
|---|---|---|
| **RQ1.** Dans une vidéo de moins de 60 secondes, qu'est-ce qui fait qu'un professionnel paraît crédible et utile ? | Entretiens et test sur prototype | Trois vidéos par secteur retenu, avec variation contrôlée du geste visible, du contexte et du nom affiché. Une seule mesure chiffrée : une note de 1 à 5 à « j'ai compris qui était cette personne et ce qu'elle fait ». Le geste de jugement est codé avant l'opinion déclarée |
| **RQ2.** À quel moment précis un visiteur accepte-t-il de donner son email, et que craint-il à cet instant ? | Deux formulations à l'étape email, puis entretien | Observation du geste, code expiré inclus, sans recueillir d'adresse réelle |
| **RQ3.** Quels signaux font qu'un message paraît sûr ou suspect avant toute réponse ? | Deux scénarios, l'un neutre et l'un suspect | Quatre signaux de R7 introduits dans le scénario suspect ; geste attendu préenregistré : ne pas répondre, demander une preuve ou signaler |

Une question secondaire est gardée pour le cycle 2 : qu'est-ce qui empêche une personne en poste de publier une vidéo visible par son employeur ? Les pages d'organisation, les offres, les lives, les langues supplémentaires et la monétisation ne sont pas testés dans ce cycle.

## 6. Revue des preuves disponibles

Chaque ligne relie une preuve à une tension de recherche, pas à une liste de signaux recopiés.

| Référence | Ce qui est rapporté | Tension éclairée | Limite |
|---|---|---|---|
| [R1] Google Design | Immersions de cinq jours, 8 à 10 participants, équipes mélangées, consentement avant enregistrement | Méthode du cycle 1, H1 à H5 | Méthode, pas conclusion sur les chercheurs d'emploi |
| [R2] LogRocket | Un problème, une à trois questions, cycles de une à deux semaines | Sections 3, 5 et 8 | Source de pratique produit |
| [R3] Apple | Huit principes de design, dont six utilisés comme grille de critique | [Principes de design](./design-principles.md) | Orientations générales, aucun chiffre d'usage |
| [R4] Rodden, Hutchinson et Fu, CHI 2010 | Cadre HEART et démarche objectifs, signaux, mesures | Section 11 et [mesure.md](../Product/mesure.md) | Cadre de mesure, pas cible de performance |
| [R5] Torres | Arbre d'opportunités, une seule opportunité par sprint | Section 9 | La méthode ne choisit pas l'opportunité |
| [R6] Rest of World, 22 décembre 2025 | 80,6 millions de comptes fictifs supprimés à l'inscription au second semestre 2024, contre 70,1 millions au semestre précédent | O1 et H2 | Chiffre communiqué par LinkedIn, repris par la presse |
| [R7] LinkedIn Job Search Safety Pulse 2026 | 72 % des professionnels interrogés pensent au moins parfois à la légitimité d'une offre. La réputation de l'entreprise arrive en premier à 29 %, le lieu de trouvaille à 28 %. Demandes d'informations sensibles 59 %, paiement initial 56 %, pression pour agir 45 %, sortie de plateforme 38 % | O4 et H5, scénario suspect de RQ3 | Déclaratif, commandité par LinkedIn |
| [R8] Étude coréenne sur les contenus courts, 30 septembre 2025 | La longueur des commentaires est liée positivement à l'engagement ; la durée de la vidéo est liée négativement à la vitesse des réactions | H7, prudence sur la limite de 60 secondes | Corpus coréen, hors contexte professionnel |
| [R9] Nielsen Norman Group | Méthode de benchmark UX, tâches et critères de réussite | Sections 4 et 11 | Méthodologie générale |

## 7. Échelle de confiance et registre d'hypothèses

### Échelle de confiance

L'échelle va de 0 à 3. L'attributaire est l'équipe produit pour toutes les valeurs attribuées dans ce cadrage. Le responsable de la recherche UX sera nommé avant J1 et tient la date d'attribution à jour dans le registre de recherche.

| Niveau | Valeur | Définition | Attributaire | Date d'attribution |
|---|---|---|---|---|
| Faible | 0 | Spéculation sans preuve ni observation | Équipe produit | 25 novembre 2026 |
| Moyenne faible | 1 | Intuition d'équipe, non encore observée | Équipe produit | 25 novembre 2026 |
| Moyenne | 2 | Indiquée par une source externe ou un raisonnement documenté | Équipe produit | 25 novembre 2026 |
| Élevée | 3 | Observée dans un contexte proche, preuve archivée | Équipe produit | Non attribuée dans ce cadrage |

Aucune hypothèse du cycle 1 n'est au niveau Élevée (3). Le passage de 0, 1 ou 2 à 3 exige une preuve archivée dans le [référentiel de recherche](./referentiel-recherche.md) et une nouvelle date d'attribution.

### Registre

Un dénominateur est choisi par test. Deux dénominateurs ne sont jamais mélangés dans une même condition.

| Identifiant | Hypothèse | Confiance | Test et dénominateur | Condition d'infirmation |
|---|---|---|---|---|
| H1 | Un visiteur comprend l'utilité de Pro après trois vidéos, sans écran de connexion | Faible (0, 25 novembre 2026) | J7, prototype fil, 8 participants | Moins de 5 personnes sur 8 savent nommer un métier ou une personne utile |
| H2 | Une vidéo de travail convainc davantage qu'un badge vérifié | Moyenne (2, 25 novembre 2026) | J4 à J6, comparaison de deux profils, 8 participants | Au moins 5 personnes sur 8 choisissent le badge et demandent une preuve hors vidéo |
| H3 | Métier et ville sont les premiers filtres spontanés | Moyenne faible (1, 25 novembre 2026) | J4 à J6, tri de cartes, 8 participants | Les gens rangent « résultat obtenu » ou « outil maîtrisé » avant le lieu chez au moins 5 des 8 participants |
| H4 | L'email est accepté au premier geste social si la phrase explique l'identité de l'interlocuteur | Faible (0, 25 novembre 2026) | J8, 10 participants (8 principaux et 2 réserves). Repli : 6 participants si 10 sont impossibles | Plus de 7 abandons sur 10, ou au moins 5 abandons sur 6 dans le variant repli. Abandon : quitter l'étape sans saisir l'adresse de test ou refuser la variante |
| H5 | Un message sans CV, avec identité affichée, réduit la peur du faux recruteur | Faible (0, 25 novembre 2026) | J4 à J6, deux messages, 8 participants | 6 personnes sur 8 demandent une preuve d'identité avant de répondre |
| H6 | Un professionnel en poste hésite à publier une vidéo visible par son employeur | Moyenne (2, 25 novembre 2026) | J4 à J6, 5 créateurs réservés sur les 12 recrutés | 4 créateurs sur 5 disent publier sans y penser |
| H7 | La limite de 60 secondes et de 150 caractères suffit à décrire un travail | Faible (0, 25 novembre 2026) | J4 à J6, enregistrement d'une vidéo, les 5 créateurs réservés | 3 créateurs sur 5 demandent plus de temps ou renoncent |
| H8 | Les contraintes de données et les signaux de confiance diffèrent entre Brazzaville et Kinshasa | Moyenne (2, 25 novembre 2026) | J4 à J6, 4 entretiens par ville, signal exploratoire | Aucun motif récurrent propre à une ville sur 4 entretiens par ville. Une divergence observée est une piste pour le cycle 2, pas une preuve d'absence ni de présence de différence |
| H9 | Un blocage après réception doit laisser la conversation lisible et refuser l'envoi suivant | Faible (0, 25 novembre 2026) | J4 à J6, mise en situation avec conversation, 8 participants | Au moins 5 personnes sur 8 trouvent la règle surprenante ou illisible. Règle absente du PRD : hypothèse à valider avant spécification |

H6 et H7 portent sur la question secondaire et utilisent les cinq créateurs réservés. H9 concerne une branche du parcours C marquée comme hypothèse, pas comme règle du PRD. Les pages d'organisation, les offres, la vérification N2 et la monétisation ne sont pas testés dans ce cycle.

## 8. Plan de terrain, dix jours ouvrés

| Jour | Activité | Participants | Livrable |
|---|---|---|---|
| J1 | Cadrage interne, relecture des documents, attribution des rôles, nommage du responsable recherche | Équipe de cycle : produit, design, développement, modération | Plan validé, guide version 1 |
| J2 et J3 | Recrutement avec questionnaire de sélection, consentement, préparation des stimuli | 12 personnes, 6 par ville, dont 4 de réserve | Liste anonymisée P1 à P12 dans le référentiel |
| J3 | Test interne du guide, une personne de l'équipe joue le participant | Équipe de cycle | Guide version 2 et journal des versions |
| J4, J5 et J6 | Huit entretiens contextuels de 45 minutes | 8 participants principaux | Notes anonymisées, une fiche par personne |
| J7 | Trois écrans sur prototype, tâches écrites, gestes codés | 6 des 8 participants principaux | Observations classées par écran |
| J8 | Deux formulations à l'étape email, un seul dénominateur par variante | 10 personnes : 8 principales et 2 réserves | Tableau de préférence, abandon et renoncement |
| J9 | Synthèse en équipe de cycle, mise à jour de l'arbre | Produit, design, développement, modération | Arbre à jour, hypothèses confirmées ou infirmées |
| J10 | Restitution d'une page, décisions d'action, retrait des citations | Équipe complète | Décisions écrites, PRD révisé |

### Matrice des situations par ville

Huit entretiens principaux, quatre par ville. Les réserves servent à la fois à J8 et aux cinq créateurs nécessaires à H6 et H7. Chaque cellule nomme une situation ; les chevauchements sont explicités dans la dernière colonne.

| Ville | Situation 1 | Situation 2 | Situation 3 | Situation 4 | Réserves et chevauchements nommés |
|---|---|---|---|---|---|
| Brazzaville | Chercheur d'emploi | Professionnel en poste | Créateur | Recruteur | Réserve B5 : créateur et chercheur d'emploi. Réserve B6 : créateur et professionnel en poste |
| Kinshasa | Chercheur d'emploi | Professionnel en poste | Créateur | Recruteur | Réserve K5 : créateur et professionnel en poste. Réserve K6 : recruteur seul |

Les cinq créateurs sont B3, B5, B6, K3 et K5. Une personne victime d'une arnaque reste classée dans l'une de ces situations, sans catégorie supplémentaire.

Secteurs retenus : deux par ville, logistique et santé. L'échantillon sert à repérer des motifs, pas à estimer une prévalence ni à comparer statistiquement les deux villes. Il ne sature ni deux villes, ni quatre situations, ni davantage de secteurs. Un troisième secteur peut être ajouté au cycle 2 seulement.

### Questionnaire de sélection

1. Cherchez-vous un emploi en ce moment ? Depuis combien de temps ?
2. Dans quel secteur travaillez-vous ou avez-vous travaillé en dernier ?
3. Quelle langue utilisez-vous habituellement pour chercher un travail ou parler de votre métier ?
4. Quelle application utilisez-vous pour voir le travail d'autres professionnels ?
5. Avez-vous déjà envoyé un message à une personne vue sur un profil ou une vidéo ?
6. Avez-vous déjà eu un doute sur une offre ou sur un message de recruteur ?
7. Êtes-vous d'accord pour un entretien de 45 minutes, avec prise de notes et enregistrement si vous l'acceptez ?

La dernière question ouvre la porte à un refus d'enregistrement. Dans ce cas, la personne reste incluse et la note est prise à la main. La question 3 est posée quelle que soit la décision future sur les langues.

### Guide d'entretien, version 2

Les questions vont du vécu vers le produit. Le mot « Pro » n'est pas prononcé avant la fin. Les trois vidéos par secteur sont présentées à la question 6, dans un ordre tiré au sort et consigné dans le référentiel.

1. Raconte-moi la dernière fois où tu as cherché un travail, ou regardé le travail d'un autre professionnel.
2. Qu'est-ce que tu as fait juste avant ? Et juste après ?
3. Si tu es d'accord, montre-moi le dernier message d'un recruteur ou d'un pair que tu as reçu.
4. Comment tu sais que cette personne est réelle ?
5. Est-ce qu'un détail t'a fait douter ? Lequel ?
6. Regarde ces trois vidéos. Qu'est-ce qui te manquerait pour croire la personne et comprendre son travail ?
7. Quand donnes-tu ton email à un site que tu ne connais pas ? Qu'est-ce qui t'arrête d'habitude ?
8. Voici deux messages. Qu'est-ce que tu ferais avant de répondre ?
9. Si tu devais refaire cette recherche autrement, tu commencerais par où ?
10. Sur quel appareil as-tu fait cette recherche, et qu'est-ce qui a déterminé ce choix ?

La question 10 porte sur l'appareil utilisé. Elle n'offre aucune réponse suggérée. Les trois plateformes sont couvertes sans présumer que les usages desktop soient identiques au mobile.

Questions à ne pas poser : « Est-ce qu'une application vidéo pro te serait utile ? », « Est-ce que tu aimerais un réseau sans CV ? ». Elles suggèrent la réponse. Le codage des gestes suit la [grille de codage](./referentiel-recherche.md).

## 9. Arbre d'opportunités, de solutions et de tests

Les opportunités sont écrites du point de vue de la personne, jamais sous forme de fonctionnalité. Une seule sera choisie pour le premier sprint.

### O1. Je ne sais pas si je peux croire ce que je vois

Tension : la preuve de travail et le badge sont deux promesses concurrentes. Origine : R6, R7, H2. Solutions : montrer la vidéo avant le profil complet ; garder un badge discret lié à l'email vérifié ; vérifier la cohérence entre vidéo, métier affiché et mots-clés. Test : comparaison de deux profils chez 8 participants, avec codage du geste avant l'opinion.

### O2. Je ne veux pas donner mon profil avant de savoir si ça vaut le coup

Tension : la sauvegarde souhaitée arrive avant la confiance dans l'usage de l'email. Origine : H1, H4, décision D-001. Solutions : choisir métier et ville sans compte ; expliquer en une phrase l'utilité du compte ; demander uniquement l'email au geste social, avec suggestions de FS-03 modifiables. Test : variantes de phrase à l'étape email, `guest_save_attempt` et `signup_verified`, avec le dénominateur de H4.

### O3. Je ne sais pas par où commencer quand je cherche

Tension : le fil proche aide, mais l'historique conservé n'est pas autorisé au MVP. Origine : H3. Solutions : fil influencé par métier et ville ; recherche par métier et ville sans historique ; suggestion liée à la vidéo en cours, sans historique conservé. Test : tri de cartes chez 8 participants, puis délai avant la première vidéo complétée. Le seuil de 500 millisecondes du premier lot de recherche est un garde-fou technique, pas une preuve d'utilité.

### O4. J'ai peur qu'un message vienne d'un faux recruteur

Tension : la fenêtre de message rassure par l'identité, mais les demandes suspectes arrivent après le premier contact. Origine : R6, R7 et ses quatre signaux (demande d'informations sensibles 59 %, paiement initial 56 %, pression pour agir 45 %, sortie de plateforme 38 %), H5. Solutions : afficher l'identité dans la composition ; avertir sans bloquer la conversation ; signaler et bloquer depuis le chat. Test : deux scénarios dont le scénario suspect mobilise explicitement les quatre signaux de R7 ; geste attendu préenregistré, observation du geste et non de l'opinion déclarée.

### O5. Je ne veux pas exposer mon travail à mon employeur actuel

Tension : publier sa preuve de travail peut coûter sa place. Origine : H6, H7, champs masquables de FS-04. Solutions : masquer ville et bio ; brouillon privé ; option de visibilité employer à n'étudier que si H6 est confirmée. Test : entretien avec les 5 créateurs réservés, question sur la personne à qui montrer la vidéo avant publication.

## 10. Frictions et émotions à confirmer

Le chemin nominal est décrit une seule fois dans le [parcours A](./userflow.md). Le tableau ci-dessous ne le répète pas : il ne retient que les frictions et les émotions à confirmer par le terrain.

| Moment du parcours A | Friction à observer | Émotion hypothétique | Identifiant |
|---|---|---|---|
| Ouverture du fil | Réflexe de fermeture dans les premières secondes | Soupçon | H1 |
| Choix des filtres | Valeur proposée qui ne correspond pas au métier exercé | Indécision | H3 |
| Lecture des vidéos | Vidéo trop travaillée, contexte absent, lecture automatique non voulue | Doute sur la réalité de la personne | H1, H2 |
| Geste de sauvegarde | Phrase d'explication trop longue ou commerciale | Hésitation à donner l'email | H4 |
| Vérification du code | Doute sur l'usage de l'email, code expiré | Irritation | H4 |
| Premier message | Identité absente de la fenêtre, peur du faux recruteur | Appréhension | H5, H9 |

Ces émotions sont des hypothèses. Elles deviennent des constats seulement si la preuve est archivée selon la règle de la section 12. La [carte de parcours](./journey-map.md) représente les creux associés et les opportunités O1 à O5.

## 11. Plan de mesure avec le cadre HEART

Les mesures ci-dessous ne sont pas des objectifs contractuels. Le dictionnaire canonique est [mesure.md](../Product/mesure.md).

| Catégorie | Objectif | Signal | Mesure |
|---|---|---|---|
| Satisfaction | La personne comprend à qui elle parle | Réponse à la question courte | Note de 1 à 5, mesure unique de RQ1 |
| Engagement | La personne regarde au moins trois vidéos par session | Vidéos complétées | `video_complete` par session, ventilé par ville |
| Adoption | Le geste social mène à un compte vérifié | Sauvegarde tentée puis email vérifié | `signup_verified` pour 100 `guest_save_attempt` |
| Rétention | Le compte revient après sa première session | Retour à J7 | Part des comptes actifs à sept jours, à établir au cycle 2 |
| Réussite de tâche | Première vidéo, recherche et message sans erreur | Délais et échecs | Délai de première vidéo, délai du premier lot, taux d'échec d'envoi |

L'engagement se rapporte à une personne, jamais au total brut. Le temps passé n'est pas une preuve de réussite : une personne qui trouve vite le bon contact peut passer moins de temps dans Pro qu'une personne perdue dans le fil.

## 12. Règles de décision

- Une opportunité est retenue si au moins 5 participants sur 8 la mentionnent spontanément dans deux contextes différents. Le dénominateur est celui du test considéré, jamais un mélange de 8, 10, 6 et 5.
- Une hypothèse est confirmée ou infirmée par sa condition écrite en section 7. Elle n'est pas réécrite pour passer. Le passage au niveau Élevée (3) exige une preuve archivée et une date.
- Chaque constat porte la ville où il a été recueilli. Une généralisation à l'Afrique exige un second cycle dans un autre pays.
- Un sprint ne traite qu'une opportunité, avec une histoire utilisateur reliée à O1 à O5 ou à H1 à H9 dans [userstories.md](./userstories.md).
- Aucune solution ne réintroduit de mur à l'entrée ni d'identifiant permanent pour le visiteur.
- Un constat sans citation anonymisée relue ni observation notée n'entre pas dans le PRD.
- Les pages d'organisation, les offres, les lives et la monétisation restent hors du cycle 1. Les sous-titres du MVP sont, eux, une règle D-021 applicable dès la préparation de la vidéo et au contrôle en modération.
- Si le terrain contredit le MVP, le PRD est modifié explicitement avec la date et le motif. Aucune modification silencieuse.

## 13. Éthique, consentement et données de recherche

Le consentement est demandé avant toute prise de notes ou enregistrement. La personne peut refuser l'enregistrement et continuer l'entretien. Les participants sont identifiés par P1 à P12 dans les notes, sans nom, email, téléphone ni identifiant de compte réel. Le prototype n'envoie aucun email réel : une adresse de test fournie par l'équipe est utilisée. Aucun CV ni document d'identité n'est demandé. Si un participant raconte une arnaque, l'entretien reste sur le récit du parcours, sans conseil juridique ni recueil de preuve d'argent.

| Donnée | Finalité | Conservation | Accès | Suppression |
|---|---|---|---|---|
| Notes anonymisées P1 à P12 | Synthèse des entretiens et suivi des hypothèses | Jusqu'à J10, puis constats anonymisés sans citation | Équipe de cycle | À la demande de la personne, immédiate ; sinon à J10 |
| Enregistrements audio | Relecture du codage des gestes | Trente jours après la restitution | Responsable recherche et codeur désigné | À la demande, immédiate ; sinon à trente jours |
| Citations anonymisées avec ville et secteur | Preuve d'un constat dans le PRD | Jusqu'à J10 | Équipe produit et rédacteur du PRD | Retrait possible jusqu'à J10, sur simple demande |
| Formulaires de consentement | Preuve de l'accord donné avant prise de notes | Jusqu'à J10 | Responsable recherche | À J10, sauf conservation anonymisée du seul fait du consentement |
| Stimuli vidéo et ordres de présentation | Répétabilité de RQ1 | Durée du cycle 1 dans le référentiel | Équipe de cycle | À la clôture du cycle 1 |
| Versions du guide et grille de codage | Traçabilité du protocole | Conservées sans donnée personnelle | Équipe de cycle | Non supprimées pendant le cadrage |
| Adresse de test | Remplacement d'une adresse réelle | Non conservée | Aucun accès après le test | Immédiate |

Les citations sont relues par la personne participante avant publication dans un livrable et retirables jusqu'à J10. Une citation non relue n'entre dans aucun document.

Base légale : consentement de la personne participante, à confirmer par la personne responsable conformité avant J2. Responsable du traitement des données de recherche : à nommer avant J2. Responsable de la recherche : à nommer avant J1. Aucune obligation juridique supplémentaire n'est affirmée dans ce document ; le périmètre applicable sera tranché dans les documents de conformité.

## 14. Ce que la recherche peut changer au PRD

| Résultat possible | Conséquence prévue |
|---|---|
| RQ1 montre que le badge compte plus que la vidéo | Renforcer FS-04 et clarifier la vérification d'email |
| RQ1 montre que le contexte manque dans la vidéo | Ajouter un champ court « ce que je fais » à FS-02 et FS-05 |
| RQ2 montre un abandon massif à l'email | Réécrire la phrase d'accompagnement de FS-01 et les suggestions de FS-03, puis retester |
| RQ2 montre que la sauvegarde locale suffit | Décider si la sauvegarde sans compte reste limitée à la session |
| RQ3 montre une peur forte au premier message | Ajouter l'avertissement de O4 à FS-07 |
| H6 est confirmée | Écrire une règle de visibilité employeur dans FS-05, puis trancher la question ouverte correspondante |
| H3 est infirmée | Remplacer métier et ville par d'autres filtres dans FS-03 et FS-08 |
| H9 est confirmée | Inscrire la règle de blocage après réception dans FS-07 avec un libellé d'erreur |

## 15. Questions ouvertes après le cycle 1

- Quand ouvrir le reste de l'Afrique, puis le monde, après le démarrage dans les deux Congo ?
- Quelles langues validées marché par marché seront ajoutées, avec date et responsable inscrits au registre ? Aucune autre langue n'est datée dans ce cadrage.
- Faut-il une option explicite pour ne pas apparaître devant les collègues ou l'employeur actuel ?
- Faut-il avertir automatiquement sur les demandes d'argent ou d'identifiants dans le chat ?
- La règle de blocage après réception (H9) devient-elle une règle FS-07 ?
- La vérification N2 reste reportée : D-010 est ouverte et relève de la phase 2.
- Le nom et les privilèges du futur niveau payant relèvent de D-011, ouverte et hors MVP.

## 16. Limites de ce document

Les sources viennent surtout de guides de méthode, de presse et de rapports d'entreprise. Aucune ne porte sur Pro. Le cycle 1 couvre deux villes et deux pays congolais, deux secteurs et huit entretiens principaux. Il ne permet de conclure ni pour le reste de l'Afrique, ni pour le monde, ni pour une prévalence.

Le chiffre de 80,6 millions de comptes fictifs est communiqué par LinkedIn et dit quelque chose de l'échelle du problème, pas de la façon dont un chercheur d'emploi le ressent. Le rapport de sécurité de LinkedIn repose sur des réponses déclaratives. Les quatre signaux repris en O4 servent à construire un scénario de test, pas à fixer une règle produit. L'étude de 19 084 vidéos courtes porte sur un corpus coréen non professionnel. Les principes d'Apple et les catégories HEART n'indiquent pas ce que les chercheurs d'emploi veulent.

Équipe, budget, stack et date de lancement restent non communiqués. Ce document ne devine pas de réponse.

## 17. Références

- **[R1]** Google Design, *Beyond the desktop field research*. https://design.google/library/beyond-the-desktop-field-research , consulté le 25 novembre 2026.
- **[R2]** Bart Krawczyk, *Building a data-driven UX research plan in 6 steps*, LogRocket, 8 janvier 2025. https://blog.logrocket.com/ux-design/data-driven-ux-research-plan/
- **[R3]** Apple, *Design principles*, Human Interface Guidelines, mise à jour du 8 juin 2026. https://developer.apple.com/design/human-interface-guidelines/design-principles , consulté le 25 novembre 2026.
- **[R4]** Kerry Rodden, Hilary Hutchinson et Xin Fu, *Measuring the user experience on a large scale*, CHI 2010. https://research.google/pubs/pub36299.html?frame=0 et https://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/36299.pdf
- **[R5]** Teresa Torres, *Opportunity Solution Trees*, Product Talk, 6 décembre 2023. https://www.producttalk.org/opportunity-solution-trees
- **[R6]** Damilare Dosunmu, *The LinkedIn job scam is global. The hook is local*, Rest of World, 22 décembre 2025. https://restofworld.org/2025/linkedin-job-scams
- **[R7]** LinkedIn, *The LinkedIn Job Search Safety Pulse 2026*, mai 2026, URL publique préférée : https://news.linkedin.com/2026/LinkedIn-Job-Search-Safety-Pulse , miroir PDF : https://delivery-p143253-e1476319.adobeaemcloud.com/adobe/assets/urn:aaid:aem:b70b094e-5698-46ac-bc80-2021be466b9f/original/as/original.pdf
- **[R8]** *Analyse des indices émotionnels et comportementaux des contenus courts*, revue coréenne de contenu numérique, 30 septembre 2025. http://journal.dcs.or.kr/_PR/view/index.php?aidx=46603&bidx=4216
- **[R9]** Nielsen Norman Group, *7 Steps to Benchmark Your Product's UX*, 13 septembre 2020. https://www.nngroup.com/articles/product-ux-benchmarks/
- **[R10]** Documents internes Pro : [vision](../Product/vision.md), [manifeste](../Product/manifeste.md), [PRD](../Product/prd.md), [grille de relecture](../Redaction/ia-defauts-et-tips.md). L'ancrage dans les deux Congo est une décision interne, pas une donnée de marché vérifiée.
- **[R11]** LinkedIn, *Community Report*, juillet à décembre 2024, cité dans [R6]. https://about.linkedin.com/transparency/community-report
