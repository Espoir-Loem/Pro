# Pro : cahier des charges produit, MVP

**Statut** : version 6, 26 novembre 2026  
**Périmètre** : phase 1, MVP  
**Documents liés** : [Vision](./vision.md), [Manifeste](./manifeste.md), [Décisions](./decisions.md), [Mesure](./mesure.md), [Expérimentation](./experimentation.md), [Tableau de bord](./tableau-de-bord.md), [Grille de relecture](../Redaction/ia-defauts-et-tips.md), [Parcours](../UX/userflow.md), [Histoires](../UX/userstories.md)

## 1. Objet du document

La vision explique pourquoi Pro existe. Le manifeste fixe les convictions. Ce document fixe ce qui est livré dans la première version, pour qui, avec quelles règles, et comment on sait que chaque brique est terminée.

Il ne contient aucun choix d'architecture définitive. La stack sera arrêtée dans un document séparé, avec ses décisions et leurs motifs, comme décrit dans `../Technique/README.md`.

## 2. Décisions héritées et hypothèses à valider

**Langues** : Français d'abord. Le français est la seule langue des phases 0, 1 et 2 selon A-08, arbitrée le 26 novembre 2026. Toute langue ajoutée à partir de la Phase 3 est inscrite au registre avec date, responsable et marché avant le premier contenu dans cette langue. Les langues suivantes sont validées marché par marché, avec date et responsable inscrits au registre. Aucune autre langue n'est datée dans ce cadrage.

**Plateformes.** La dimension `plateforme` prend les valeurs `mobile`, `web` et `desktop`, définies ainsi :

- `mobile` : applications natives iOS et Android sur téléphone.
- `web` : site responsive dans un navigateur, utilisé sur ordinateur et tablette.
- `desktop` : application exécutable installée sur Windows et macOS. Linux est différé et non spécifié en phase 1.

Aucune mesure ne fusionne ces plateformes sans le dire explicitement. Les dimensions `city`, `trade` et `campaign_ref` restent séparées de `plateforme`.

### 2.1 Décisions héritées du registre

Ces lignes ne sont pas des hypothèses. Leur statut est celui du [registre des décisions](./decisions.md).

| Décision | Identifiant | Portée | Effet sur le MVP |
|---|---|---|---|
| Périmètre fil, profils, publication, chat, recherche, modération de base | D-003 | Phase 1 | FS-01 à FS-11 |
| Les clients `mobile`, `web` et `desktop` livrés ensemble | D-004 | Phase 1 | Chaque FS est validée sur les trois plateformes |
| Client desktop exécutable Windows et macOS, léger et rapide, sans attente perceptible | D-023 | Phase 1 | Cinq cibles de revue arbitrées le 26 novembre 2026 par A-03, section 9.1 |
| Gratuité des phases 1 à 4, niveau payant en phase 5 | D-005 | Phases 1 à 4 | Aucun privilège payant dans le MVP |
| Premier marché, deux Congo | D-007 | Phase 0 à 4 | Taxonomie initiale calibrée sur les deux villes |
| Langues validées marché par marché, aucune autre langue datée | D-008 | Toutes les phases | Français dans le MVP |
| Aucun identifiant permanent pour le visiteur | D-012 | Toutes les phases | Jeton court, aucun traceur tiers |
| Vérification limitée à l'email en phase 1 | D-018 | Phase 1 | Parcours A et `signup_verified` |
| Sous-titres et correction par l'auteur avant publication | D-021 | Phase 1 | FS-02 et FS-05 |
| Mise à jour automatique des clients, sans cycle de store pour ce qui est servi hors binaire natif | D-024 | Phase 1 et suivantes | Section 10.1, validation avant FS-01 |

### 2.2 Hypothèses à valider

La stack est retenue en D-009. Les autres lignes n'ont pas le statut « retenu ». Les valeurs marquées « à confirmer » doivent être tranchées avant le démarrage du chantier concerné.

| Hypothèse | Valeur ou question | Méthode | Seuil ou condition | Échéance |
|---|---|---|---|---|
| Équipe | 2 à 3 développeurs, 1 designer, 1 personne produit à temps partiel | Porteur unique intérimaire appuyé par les outils IA, jamais auteurs, selon A-04 | Référence de planification, pas un engagement ; prestataires du client `desktop` à nommer avant le premier commit de code de stack | Arbitrée le 26 novembre 2026 |
| Durée du MVP | 8 à 12 semaines | Jalons par critères de sortie, selon A-05 | Référence de planification, pas un engagement ; aucune date de lancement inventée ; date à nommer avant le planning | Arbitrée le 26 novembre 2026 |
| Budget CDN et modération | 1 000 USD par mois, 500 USD par ville | D-022 retenue le 26 novembre 2026 | 0,001 USD par vue, lu séparément par ville, fenêtre de mois civil | Inscrite avant `video.md` dans `../Technique/README.md` |
| Stack `mobile`, `web` et `desktop` | Retenue en D-009 | ADR unique décrit dans `../Technique/adr-001-stack.md` | Tout TypeScript, versions LTS, zéro CVE connue non traitée au merge et à la release | Avant le premier sprint |
| H1 à H8 | Registre d'hypothèses de la recherche UX | Phase 0, seuils chiffrés et validateurs nommés dans `./roadmap.md` | Confirmation ou infirmation selon les seuils | Sortie de la Phase 0 |
| Opportunité du premier sprint | Une seule opportunité O1 à O5 | Arbre d'opportunités, compte rendu de J10 | Identifiant O écrit | Sortie de la Phase 0 |

## 3. Périmètre

### 3.1 Ce qui entre dans le MVP

Les trois clients, `mobile`, `web` et `desktop`, sont livrés ensemble en Phase 1, conformément à D-004.

- Fil vidéo vertical consultable sans compte.
- Taxonomie initiale des métiers et des villes calibrée sur Brazzaville et Kinshasa, selon D-017.
- Lecture, recherche et consultation de profils publics sans compte.
- Choix du métier et de la ville à la première ouverture, sans création de compte.
- Profil public simple pour les membres.
- Publication de vidéos avec compression et modération asynchrone.
- Sous-titres des vidéos avec son, générés puis corrigés avant publication, selon D-021.
- Like, commentaire, suivi et sauvegarde.
- Chat 1:1 entre membres.
- Signalement, blocage et file de modération.
- Notifications push pour les membres.
- Événements de mesure dès la première version.
- Mise à jour automatique des clients selon D-024 et la section 10.1, sans cycle de store pour ce qui peut être servi hors binaire natif.

### 3.2 Ce qui reste dehors

- Client desktop pour Linux. Linux est différé et non spécifié en phase 1, selon la définition de `desktop` en section 2.
- Lives.
- Pages entreprise, organisations et offres d'emploi. Le modèle de pages et de rôles est spécifié en section 14, mais aucune de ces fonctions n'est livrée dans le MVP. Elles seront gratuites dans leur première version.
- Candidatures, messagerie recruteur, badge N2 et comportement propre aux niveaux N2 et N3.
- Monétisation et publicité. Le niveau organisations payant relève de la Phase 5, avec le nom et les privilèges définis par D-011, retenue le 26 novembre 2026.
- Recommandations personnalisées à partir d'un historique conservé.
- Vérification d'identité au-delà de la vérification d'email. Téléphone et connexion sociale en phase 2, non spécifiés.
- Offres signalées dans la recherche. Aucun classement payant dans la recherche, y compris en Phase 5.

Les vidéos avec son ne sont pas exclues du MVP : elles suivent la règle de sous-titrage D-021, écrite en FS-02 et FS-05.

### 3.3 Dépendances externes

Le MVP a besoin de quatre services extérieurs : stockage d'objets, CDN avec transcoding adaptatif, service de notifications push et service d'envoi d'emails de vérification. Le choix entre services gérés et auto-hébergés sera fait dans l'ADR décrit dans `../Technique/README.md`. Le budget qui conditionne ces choix est inscrit en D-022 : 1 000 USD par mois et un seuil de 0,001 USD par vue, lu séparément par ville.

## 4. Rôles et tâches à accomplir

| Rôle | Besoin principal | Tâche à accomplir |
|---|---|---|
| Visiteur | Voir si Pro lui est utile avant de donner ses données | Découvrir trois vidéos pertinentes, puis décider de s'inscrire |
| Créateur | Montrer son travail sans remplir un CV | Publier une vidéo courte et voir qui la regarde |
| Membre | Entrer en contact avec une personne réelle | Envoyer un message à partir d'un profil ou d'une vidéo |
| Modérateur | Garder la file sous contrôle | Traiter un signalement avec une décision tracée |
| Propriétaire d'organisation | Créer et faire vérifier une organisation, nommer les rôles | Voir section 14, phase 2 |
| Administrateur de page | Gérer une page au nom de l'organisation | Voir section 14, phase 2 |

Le recruteur et l'entreprise sont des rôles de la phase 2. Leurs besoins sont documentés dans la vision, mais aucune fonctionnalité ne leur est destinée dans le MVP. Les rôles internes à une organisation sont détaillés en section 14.

## 5. Matrice des droits par action

| Action | Visiteur | Membre | Profil vérifié | Organisation |
|---|---|---|---|---|
| Lire le fil public | Oui | Oui | Oui | Oui |
| Voir un profil public | Oui | Oui | Oui | Oui |
| Chercher par métier ou ville | Oui | Oui | Oui | Oui |
| Liker, commenter, suivre, sauvegarder | Non | Oui | Oui | Oui |
| Publier une vidéo | Non | Oui | Oui | Oui |
| Envoyer un message | Non | Oui | Oui | Oui |
| Recevoir des notifications | Non | Oui | Oui | Oui |
| Postuler à une offre | Non | Non | Phase 2, après D-010 | Phase 2 |
| Publier une offre | Non | Non | Non | Phase 2 |
| Voir les statistiques d’audience | Non | Non | Non | Phase 2 |

Le profil vérifié et l'organisation n'ont pas de comportement propre dans le MVP. Ils figurent dans le tableau pour éviter une contradiction avec la vision. Leur activation arrive avec les offres d'emploi, et les rôles internes sont décrits en section 14.

## 6. Parcours principaux

### Parcours A : le visiteur devient membre

1. La personne ouvre Pro et voit le fil. Aucun écran de connexion.
2. Elle choisit un métier et une ville. Les choix restent dans la session.
3. Elle regarde trois vidéos. Le fil tient compte de ses choix.
4. Elle touche « Sauvegarder ». Une phrase explique qu'un compte permet de retrouver la vidéo.
5. Elle saisit un email vérifié en phase 1. Un code de vérification est envoyé. Téléphone et connexion sociale en phase 2, non spécifiés.
6. L'email vérifié, elle retrouve les vidéos sauvegardées et elle peut publier.

Chemin d'erreur : si le code expire, un nouveau code est envoyé après un délai court. Le nombre de tentatives est limité.

### Parcours B : le créateur publie

1. Le membre touche « Publier » et sélectionne une vidéo depuis son téléphone.
2. Il ajoute une légende de 150 caractères maximum et jusqu'à trois mots-clés.
3. La vidéo est compressée sur l'appareil, puis envoyée.
4. La vidéo passe à l'état `pending_review`.
5. Après validation automatique et correction des sous-titres par l'auteur pour une vidéo avec son, elle devient `published`.
6. Elle apparaît sur son profil et dans le fil des personnes qui le suivent.

Chemin d'erreur : si le fichier dépasse 200 Mo ou 60 secondes, l'application affiche la limite avant l'envoi. Si l'envoi échoue, la vidéo reste dans la file locale avec un bouton « Réessayer ». Si les sous-titres ne sont pas corrigés, la vidéo reste en brouillon et n'est pas publiée.

### Parcours C : le membre contacte une personne

1. Le membre ouvre un profil public ou une vidéo.
2. Il touche « Message ». Son identité affichée est visible dans la fenêtre de composition.
3. Il envoie un message de 2 000 caractères maximum.
4. Le destinataire reçoit une notification s'il a accepté les notifications.
5. Le destinataire peut répondre, bloquer ou signaler.

Chemin d'erreur : si le destinataire a bloqué l'expéditeur, l'envoi est refusé avant l'affichage de la fenêtre, sans préciser qui a bloqué qui. L'état de livraison et l'état de modération du message sont deux champs distincts, spécifiés en section 9.

### Parcours D : un signalement est traité

1. Une personne, avec ou sans compte, ouvre le menu d'une vidéo et choisit un motif de signalement.
2. Un ticket est créé avec une référence au contenu et au motif.
3. Le modérateur ouvre la file et voit le contenu, le motif et l'historique du compte.
4. Il choisit une action : conserver, masquer, retirer, suspendre le compte.
5. L'action est journalisée avec une date, un motif et l'identifiant du modérateur, ou l'acteur `system` lorsque la décision est automatique.
6. L'auteur du contenu reçoit une notification avec la décision et un lien de contestation. Le test à blanc de cette chaîne est la condition 6 de la section 11.

## 7. Spécifications fonctionnelles

### FS-01 : fil public sans compte

**Histoire.** En tant que visiteur, je veux regarder des vidéos sans créer de compte, afin de décider si Pro me concerne.

**Règles.**

- Fil vertical, lecture automatique sans son, défilement par geste.
- Aucun écran bloquant de création de compte avant trois vidéos vues.
- Préchargement limité à dix vidéos.
- Bitrate adaptatif mesuré sur le profil réseau de référence publié dans `../Technique/README.md`.
- Les choix de métier et de ville influencent l'ordre du fil.

**Critères d’acceptation.**

- Soit le profil réseau de référence, quand la personne ouvre l'application, alors la première vidéo démarre en moins de trois secondes.
- Soit un visiteur, quand il fait défiler trois vidéos, alors aucun formulaire ne bloque le fil.
- Soit un visiteur qui refuse le chargement automatique, quand il touche une vidéo, alors la lecture démarre manuellement.
- Soit une session de visiteur, quand la session expire, alors aucun identifiant permanent n'est conservé côté serveur.

### FS-02 : lecture vidéo et compression

**Histoire.** En tant que créateur, je veux envoyer une vidéo depuis mon téléphone, afin de publier sans logiciel externe.

**Règles.**

- Format accepté : MP4 ou MOV.
- Durée maximale : 60 secondes.
- Taille maximale : 200 Mo.
- Résolution maximale à l'envoi : 1080p.
- Transcoding en HLS ou DASH avant publication.
- La vidéo n'est visible par personne tant que l'état n'est pas `published`.
- Les vidéos avec son du MVP disposent de sous-titres générés automatiquement et corrigés par l'auteur avant publication. Si la correction n'est pas faite, la vidéo reste en brouillon et n'est pas publiée.

**Critères d’acceptation.**

- Soit un fichier de 61 secondes, quand la personne le sélectionne, alors un message affiche la limite avant l'envoi.
- Soit un fichier conforme, quand l'envoi réussit, alors l'état passe à `pending_review`.
- Soit une vidéo en attente, quand le créateur ouvre son profil, alors il voit un état « en vérification » et non une vidéo publique.
- Soit un échec réseau, quand la connexion revient, alors un bouton permet de reprendre l'envoi sans sélectionner à nouveau le fichier.
- Soit une vidéo avec son, quand l'auteur n'a pas corrigé les sous-titres générés automatiquement, alors la vidéo reste en brouillon et n'est pas publiée.

### FS-03 : onboarding métier et ville

**Histoire.** En tant que visiteur, je veux indiquer mon métier et ma ville, afin de voir des vidéos proches de mon travail.

**Règles.**

- Deux sélecteurs, avec possibilité de passer.
- Listes alimentées par la taxonomie D-017, calibrée sur Brazzaville et Kinshasa.
- Valeurs conservées dans la session du visiteur.
- À l'inscription, les valeurs sont proposées, jamais importées sans accord.

**Critères d’acceptation.**

- Soit un visiteur qui passe les deux sélecteurs, quand il ouvre le fil, alors il voit un fil général.
- Soit un visiteur qui choisit un métier, quand il regarde le fil, alors au moins la moitié des vidéos proposées appartiennent au métier choisi dans la taxonomie D-017.
- Soit un visiteur qui s'inscrit, quand le formulaire s'ouvre, alors ses choix apparaissent comme suggestions modifiables.

### FS-04 : profil public

**Histoire.** En tant que membre, je veux un profil public lisible sans compte, afin que les autres sachent qui je suis avant de me contacter.

**Règles.**

- Champs visibles par défaut : nom affiché, métier, ville, bio courte, photo, nombre de vidéos.
- Email, téléphone et statistiques privées ne sont jamais renvoyés dans la réponse publique.
- Le propriétaire peut masquer la ville et la bio.
- Le profil n'affiche pas la liste des personnes suivies dans le MVP.

**Critères d’acceptation.**

- Soit un visiteur non connecté, quand il ouvre un profil public, alors il voit les champs autorisés.
- Soit un membre qui masque sa ville, quand un visiteur consulte son profil, alors la ville n'apparaît ni dans l'interface ni dans la réponse de l'API.
- Soit une requête publique, quand elle est inspectée, alors elle ne contient ni email ni téléphone.

### FS-05 : publication vidéo

**Histoire.** En tant que membre, je veux publier une vidéo, afin de montrer mon travail aux autres professionnels.

**Règles.**

- Réservé aux comptes N1 et plus.
- Légende de 150 caractères maximum.
- Jusqu'à trois mots-clés.
- Un visiteur qui touche « Publier » voit une explication courte, pas un formulaire complet.
- Les vidéos avec son du MVP disposent de sous-titres générés automatiquement et corrigés par l'auteur avant publication. Si la correction n'est pas faite, la vidéo reste en brouillon et n'est pas publiée.
- Le compteur de vidéos publiées est affiché sur le profil.

**Critères d’acceptation.**

- Soit un visiteur, quand il touche « Publier », alors il voit une phrase expliquant qu'un compte est nécessaire pour être identifiable.
- Soit un membre, quand il publie, alors la vidéo passe à `pending_review`.
- Soit une vidéo avec son, quand l'auteur n'a pas corrigé les sous-titres générés automatiquement, alors la vidéo reste en brouillon et n'est pas publiée.
- Soit une vidéo validée, quand elle est publiée, alors elle apparaît sur le profil de l'auteur et dans le fil.
- Soit une vidéo retirée par la modération, quand l'auteur ouvre son profil, alors elle n'apparaît plus.

### FS-06 : interactions sociales

**Histoire.** En tant que membre, je veux aimer, commenter, suivre et sauvegarder, afin de construire un fil qui me ressemble.

**Règles.**

- Like et sauvegarde réversibles.
- Commentaire de 280 caractères maximum, stocké dans la table `comment` décrite en section 8.
- Limite de dix commentaires par minute par compte.
- Un visiteur qui touche une interaction voit une phrase, puis un formulaire avec un seul champ email vérifié.
- Le nombre de follows peut être limité à 100 par heure pour détecter les comportements automatisés.

**Critères d’acceptation.**

- Soit un visiteur, quand il touche « J’aime », alors il voit une explication et un champ email, sans autre donnée demandée.
- Soit un membre, quand il sauvegarde une vidéo, alors elle apparaît dans sa liste personnelle.
- Soit un membre, quand il annule un like, alors le compteur revient à sa valeur précédente.
- Soit un compte qui dépasse dix commentaires en une minute, quand il tente un onzième commentaire, alors l’envoi est bloqué avec un message clair.

### FS-07 : chat 1:1

**Histoire.** En tant que membre, je veux écrire à une personne dont j'ai vu le travail, afin d'engager une conversation professionnelle.

**Règles.**

- Réservé aux comptes N1 et plus.
- Envoi impossible à soi-même.
- Longueur maximale : 2 000 caractères par message.
- Limite de 20 messages par minute par compte.
- Identité affichée visible dans la fenêtre de composition.
- Blocage et signalement accessibles depuis la conversation, avec écriture dans la table `block`.
- Accusé de lecture affiché quand le destinataire a ouvert le message.
- L'état de livraison et l'état de modération d'un message sont deux champs distincts, spécifiés en section 9.

Le [modèle de décision de l'ajout des avertissements arnaque](../../research_notes/Planning/decision-avertissements-arnaque-FS07.md) prépare la décision à trancher avant la première campagne, sans texte ni date préremplis. Tant que la décision n'est pas écrite, le chat reste inchangé.

**Critères d’acceptation.**

- Soit un visiteur, quand il touche « Message », alors il est invité à créer un compte avec une phrase sur l'identité de l'interlocuteur.
- Soit un membre bloqué, quand il tente d'envoyer un message, alors l'envoi est refusé avant l'ouverture de la fenêtre.
- Soit un message signalé, quand il est traité, alors un ticket de modération est créé avec son identifiant et son état de modération change sans modifier son état de livraison.
- Soit une conversation, quand le destinataire la lit, alors l'expéditeur voit l'accusé de lecture.

### FS-08 : recherche et filtres

**Histoire.** En tant que visiteur, je veux chercher par métier ou par ville, afin de trouver des personnes sans m'inscrire.

**Règles.**

- Recherche sur les profils publics et les vidéos publiées.
- Filtres métier et ville combinables, selon la taxonomie D-017.
- Aucun résultat personnalisé à partir de l'historique du visiteur.
- Réponse limitée à 20 résultats par page.
- Aucun mur d'authentification sur les résultats publics.
- Aucun classement payant dans la recherche. Les offres signalées éventuelles restent hors recherche et relèvent de la Phase 5.

**Critères d’acceptation.**

- Soit un visiteur, quand il cherche un métier, alors il obtient des profils et des vidéos publics.
- Soit deux filtres actifs, quand aucun résultat ne correspond, alors un état vide propose de retirer un filtre.
- Soit une requête, quand elle est mesurée, alors le premier lot arrive en moins de 500 millisecondes sur le profil réseau de référence publié dans `../Technique/README.md`.
- Soit un visiteur non connecté, quand il ouvre un résultat, alors aucun écran de connexion ne s'affiche.

### FS-09 : signalement et modération

**Histoire.** En tant que personne qui voit un contenu problématique, je veux le signaler, afin que la plateforme prenne une décision tracée.

**Règles.**

- Motifs : spam, contenu trompeur, harcèlement, contenu dangereux, autre.
- Signalement ouvert aux visiteurs, sans identifiant permanent.
- File de modération avec priorité selon le motif et le nombre de signalements, selon la procédure décrite dans `../Operations/README.md`.
- Actions possibles : conserver, masquer, retirer, suspendre le compte.
- Journal d'audit pour chaque action, avec acteur `moderateur` ou acteur `system` et règle journalisée.
- Contestation par email avec lien unique, stockée dans la table `appeal` décrite en section 8, avec expiration et usage unique. La [fiche de contrôle de la contestation](../../research_notes/Sprint-1/fiche-controle-contestation.md) prépare les points à vérifier, sans ticket ni date préremplis.

**Critères d’acceptation.**

- Soit un visiteur sans compte, quand il signale une vidéo, alors un ticket est créé avec une référence pseudonyme.
- Soit un modérateur, quand il traite un ticket, alors son identifiant, la date, l'action et le motif sont enregistrés.
- Soit une décision automatique, quand elle est appliquée, alors l'acteur `system` et la règle appliquée sont journalisés.
- Soit un contenu retiré, quand l'auteur est notifié, alors le message inclut un lien de contestation.
- Soit une contestation, quand elle est reçue, alors un nouveau ticket est ouvert avec le ticket d'origine en référence et les événements `appeal_opened` puis `appeal_resolved` sont émis.

### FS-10 : notifications push

**Histoire.** En tant que membre, je veux être informé d'une réponse ou d'une décision, afin de revenir au bon moment.

**Règles.**

- Événements : commentaire, suivi, message, décision de modération.
- Demande d'autorisation après trois vidéos vues et une première action significative, jamais au lancement.
- Abonnement enregistré dans la table `push_subscription`, réservée au compte ; aucun jeton push n'est rattaché à un visiteur.
- Désactivation possible sans effet sur les autres fonctions.
- Lien direct vers l'élément concerné.

**Critères d’acceptation.**

- Soit un nouveau visiteur, quand il ouvre l'application, alors aucune demande d'autorisation push n'apparaît avant trois vidéos vues.
- Soit une première action significative après trois vidéos vues, quand elle survient, alors la demande d'autorisation peut apparaître.
- Soit un membre qui refuse les notifications, quand il reçoit un message, alors le message est disponible dans le chat sans notification système.
- Soit une notification touchée, quand l'application s'ouvre, alors elle affiche directement la vidéo, le profil ou la conversation concernée.

### FS-11 : événements de mesure

**Histoire.** En tant qu'équipe produit, je veux disposer d'événements propres, afin de mesurer la découverte et la conversion sans pistage intrusif.

**Règles.**

- Événements canoniques : `app_open`, `feed_session_start`, `video_impression`, `video_complete`, `guest_save_attempt`, `signup_start`, `signup_verified`, `push_opt_in`, `video_publish_attempt`, `video_published`, `message_sent`, `report_created`, `report_resolved`, `moderation_action`, `appeal_opened`, `appeal_resolved`, `queue_depth`, `report_age`.
- Chaque événement porte la dimension `plateforme` avec une valeur parmi `mobile`, `web` et `desktop`, en plus de l'horodatage. Il peut porter `city`, `trade` et `campaign_ref`, qui restent des dimensions distinctes de `plateforme`.
- Chaque événement porte un identifiant de session courte avant inscription et un identifiant de compte après inscription, selon l'ADR d'identité de session décrit dans `../Technique/README.md`.
- Aucun identifiant d'appareil permanent. Aucun traceur tiers.
- Conservation des événements : 30 jours. Les agrégats ont une durée et une finalité inscrites au registre avant la première mesure.
- Le nom canonique, la formule, le dénominateur, la population et le garde-fou de chaque mesure sont ceux de `./mesure.md`.

**Critères d’acceptation.**

- Soit une session de visiteur, quand un événement est envoyé, alors il contient un identifiant de session sans correspondance avec un appareil.
- Soit une inscription vérifiée, quand l'événement `signup_verified` est envoyé, alors il est relié au compte créé et porte l'email vérifié comme seul mode en phase 1.
- Soit un tableau de bord, quand il affiche les inscriptions avec email vérifié pour 1 000 sessions de fil, alors le chiffre correspond à `signup_verified / feed_session_start * 1000` sur les événements enregistrés.
- Soit un événement conservé, quand il dépasse 30 jours, alors il est supprimé et aucun identifiant d'appareil permanent n'a été introduit.

## 8. Modèle de données minimal

| Table | Champs principaux |
|---|---|
| `guest_session` | jeton, métier, ville, création, expiration |
| `account` | identifiant, email, empreinte du mot de passe, état, création |
| `profile` | compte, nom affiché, métier, ville, bio, photo, visibilité des champs |
| `video` | identifiant, auteur, clé d'objet, état, légende, durée, création |
| `interaction` | identifiant, compte, vidéo, type, création |
| `comment` | identifiant, vidéo, compte, corps, état de livraison, état de modération, création |
| `message` | identifiant, expéditeur, destinataire, corps, état de livraison, état de modération, création |
| `block` | identifiant, compte, type de cible, cible, création |
| `report` | identifiant, référence du signalant, type de cible, cible, motif, état |
| `moderation_action` | identifiant, signalement, acteur, action, motif, création |
| `appeal` | identifiant, signalement, empreinte du jeton, création, expiration, texte, état, décision, motif, utilisateur qui a statué |
| `analytics_event` | identifiant, type, session, compte, horodatage, plateforme, city, trade, campaign_ref |
| `push_subscription` | identifiant, compte, jeton, création, révocation |

La référence du signalant est un pseudonyme de session, pas un identifiant d'appareil. Elle permet de relier deux signalements sans identifier la personne de façon permanente.

La table `comment` porte le corps du commentaire et sépare son état de livraison de son état de modération. La table `block` enregistre les blocages sans exposer l'identité de la personne bloquée dans une réponse publique. La table `analytics_event` est le magasin des événements canoniques de FS-11, avec une conservation de 30 jours. Son champ `plateforme` prend les valeurs `mobile`, `web` et `desktop` définies en section 2 et reste distinct de `city`, `trade` et `campaign_ref`. La table `push_subscription` est réservée au compte : aucun jeton push n'est attaché à `guest_session`. La table `appeal` comporte dix champs nommés, dont l'empreinte du jeton, l'expiration et l'utilisateur qui a statué ; son lien avec `moderation_action` est décrit dans `../Conformite/README.md`.

## 9. États à implémenter

| Objet | Champ | États |
|---|---|---|
| Vidéo | état de publication | `draft`, `uploading`, `pending_review`, `published`, `rejected`, `removed` |
| Compte | état | `unverified`, `active`, `suspended`, `deleted` |
| Message | état de livraison | `sent`, `delivered`, `read` |
| Message | état de modération | `none`, `reported`, `blocked`, `removed` |
| Commentaire | état de livraison | `sent`, `delivered` |
| Commentaire | état de modération | `none`, `reported`, `hidden`, `removed` |
| Signalement | état | `open`, `in_review`, `resolved`, `appealed`, `closed` |
| Contestation | état | `open`, `in_review`, `resolved`, `rejected` |

Les états de livraison décrivent le trajet technique d'un message ou d'un commentaire. Les états de modération décrivent une décision sur son contenu. Aucun état ne mélange les deux dimensions : un message `read` peut passer à `reported` sans perdre son accusé de lecture.

Une vidéo `removed` reste dans le stockage le temps du délai de contestation, puis est supprimée. Un compte `deleted` entraîne la suppression du profil public et des vidéos associées, sauf obligation légale contraire documentée dans `../Conformite/README.md`.

### 9.1 Client desktop

Le client desktop est livré dans le MVP avec `mobile` et `web`, selon D-004 et D-023. A-03 est arbitrée le 26 novembre 2026 : les cinq cibles ci-dessous sont des cibles de revue, aucune n'est présentée comme mesurée.

| Cible de revue | Valeur | Condition |
|---|---|---|
| Démarrage à froid jusqu'au fil interactif | Moins de 2 secondes | Machine R2, Windows 11 et macOS supportés séparés, p75 sur 30 lancements |
| Changement de vue locale | Moins de 100 ms | Machine R2, Windows et macOS séparés |
| Première image vidéo | Moins de 300 ms | Profil R1, cache froid et cache chaud séparés |
| Consommation mémoire au repos | Sous 150 Mo | Machine R2, Windows et macOS séparés |
| Taille de l'installateur | Sous 80 Mo | Windows et macOS séparés |

La machine R2 retenue est volontairement modeste : Windows 11 et macOS en version supportée, 2 cœurs, 4 Go de RAM et SSD. La méthode porte sur 30 lancements à froid par système, le p75 et des traces jointes. La revue est prévue le 26 décembre 2026. Ces cibles découlent de la référence de rapidité donnée par le porteur du produit, sans chiffre recopié ni résultat revendiqué. Le profil R1 reste une proposition décrite dans `../Technique/performance.md`. Linux reste différé et non spécifié en phase 1.

## 10. Exigences non fonctionnelles

**Performance.** Première vidéo en moins de trois secondes sur le profil réseau de référence publié dans `../Technique/README.md`. Démarrage d'une vidéo après toucher en moins de 1,5 seconde. Défilement fluide sur un appareil de gamme moyenne. Le démarrage vidéo est suivi en p50 et en p95 dans `./mesure.md`.

**Bande passante.** Bitrate adaptatif. Mode faible consommation qui désactive le préchargement et limite la qualité. Aucun téléchargement spéculatif au-delà de dix vidéos. Un plafond de lecture est une question ouverte, sans seuil ni phase dans ce cadrage.

**Accessibilité.** Le web vise WCAG 2.2 AA. Cibles tactiles d'au moins 24 sur 24 CSS px selon SC 2.5.8, avec un objectif produit de 44 pixels. Ratio de contraste visé à confirmer lors de la revue d'accessibilité. Libellés pour lecteur d'écran et navigation au clavier sur le web. Le desktop suit les API d'accessibilité natives Windows et macOS avec les mêmes objectifs de lisibilité, de focus et de contraste, vérifiés en revue d'accessibilité. Les vidéos avec son du MVP disposent de sous-titres générés automatiquement et corrigés par l'auteur avant publication. Si la correction n'est pas faite, la vidéo reste en brouillon et n'est pas publiée (D-021, FS-02 et FS-05).

**Référencement web.** Le client web suit la fiche [seo-web.md](../Technique/seo-web.md). La checklist minimale porte sur la structure sémantique, l'unicité du titre et de la description, l'URL canonique sans paramètre de session, la déclaration de langue, les données structurées, le plan du site et les signaux web essentiels. Aucune page n'est créée pour un moteur seulement, aucun classement payant n'est introduit et la lecture publique sans compte reste intacte. Les mesures SEO-01 et SEO-02 sont définies dans [kpi.md](./kpi.md), sans cible chiffrée avant décision écrite.

| Contrôle SEO | Moment | Preuve |
|---|---|---|
| Titre, description et URL canonique uniques | Avant la revue de chaque page publique | Extrait du rendu et de l'en-tête |
| Données structurées conformes au contenu réel | Avant la publication d'une offre, d'une vidéo ou d'une organisation | Validation du schéma |
| Plan du site et règles d'accès sans contenu privé | Avant le déploiement web | Fichiers publiés et chemin vérifié |
| Signaux web essentiels | Après chaque mise en production web | Rapport de terrain daté |

**Confidentialité.** Pas d'empreinte d'appareil. Jeton de visiteur à courte durée. Pas de suivi entre appareils. Pas de traceur tiers pour les non-connectés. Durée de conservation des événements de session fixée à 30 jours. Aucune cohorte visiteur à sept jours, conformément à D-020. La durée de conservation des agrégats et leur finalité sont inscrites au registre avant la première mesure.

**Sécurité.** Authentification limitée à cinq tentatives par minute et par adresse. Lecture limitée à 200 requêtes par minute. Vitesse de follow et de like surveillée. Les erreurs répétées consomment plus vite le budget de requêtes. Le niveau OWASP ASVS 2 est visé depuis le 26 novembre 2026, avec la portée et les contrôles décrits dans `../Technique/securite.md`.

**Modération.** Journal d'audit complet, notification des auteurs, voie de contestation. Les états de livraison et les états de modération sont distincts. L'acteur `system` est journalisé avec sa règle. Le dispositif est conçu pour pouvoir être étendu au cadre applicable si Pro dessert l'Union européenne, sous validation du conseil local dans `../Conformite/README.md`.

**Observabilité.** Journalisation des erreurs, mesure des temps de réponse, alerte sur la file de modération et sur le taux d'échec d'envoi vidéo. Les destinataires et les seuils des alertes sont décrits dans `../Operations/README.md`.

### 10.1 Mise à jour automatique des clients

La règle D-024 s'applique aux trois clients. Elle vise à livrer une correction sans attendre un cycle de validation de store quand le changement peut être servi autrement. A-13 est arbitrée le 26 novembre 2026 : la part modifiable hors binaire natif sur `mobile` est une liste fermée de six catégories, avec les deux preuves de store datées dans `./arbitrage.md`.

| Client | Chemin de mise à jour | Limite écrite |
|---|---|---|
| `web` | Déploiement côté serveur, visible à la navigation suivante | La session en cours continue sur la version chargée, sans perte de sauvegarde ni de message en cours |
| `desktop` | Paquet signé téléchargé en arrière-plan, appliqué au redémarrage ou au lancement suivant | Signature et intégrité vérifiées avant installation ; retour à la version précédente si la vérification échoue ; démarrage et mémoire restent dans les cibles de la section 9.1 |
| `mobile` | Six catégories servies côté serveur : règles, contenus, textes et traductions, taxonomies, indicateurs de fonctionnalité et valeurs de configuration | Aucun code exécutable téléchargé ; tout changement de binaire natif suit le circuit du store ; retour au binaire natif si une règle de store change, selon A-13 |

Règles communes :

1. Aucune mise à jour ne coupe une session en cours. Le moment d'application est celui du client concerné, décrit dans le tableau ci-dessus.
2. Une mise à jour ne modifie pas une décision de modération et ne contourne pas la porte de publication décrite dans `../Technique/adr-003-porte-publication.md`. Toute transition liée à une règle reste journalisée avec un acteur `system` et un identifiant de règle.
3. Le mécanisme ne crée aucun identifiant d'appareil, d'installation ou de machine, et aucune jointure avec `signup_verified`, selon D-012 et `../Conformite/confidentialite-visiteur.md`.
4. Le journal technique porte la version appliquée, le résultat de la vérification et le retour arrière éventuel, sans rattachement à une personne.
5. La signature, l'échec de vérification, le retour arrière et la non interruption de session sont testés avant FS-01 et rejoués en revue de sortie MVP. Le contrôle est détaillé dans `../Technique/securite.md` et la revue dans `../Technique/responsabilites.md`.

## 11. Définition de terminé

Une brique est terminée quand les sept conditions sont réunies :

1. Les critères d’acceptation de chaque FS sont vérifiés sur les trois plateformes, `mobile`, `web` et `desktop`. La [grille de validation de cette condition](../../research_notes/Sprint-1/sprint/grille-validation-criteres-FS.md) porte les preuves à archiver par FS et par plateforme, sans recopier les critères ni case cochée.
2. Les événements prévus sont émis et visibles dans le tableau de bord décrit dans `./tableau-de-bord.md`. La [fiche de contrôle de cette condition](../../research_notes/Sprint-1/revue-evenements-tableau-bord-condition2.md) prépare les points et les preuves à archiver, sans relevé prérempli.
3. Les cas d’erreur décrits dans le parcours correspondant ont été testés. La [fiche de contrôle de cette condition](../../research_notes/Sprint-1/revue-cas-erreur-condition3.md) prépare les cas à rejouer et les traces à archiver, sans cas supposé ni résultat prérempli.
4. La revue de code et la revue d’accessibilité sont passées. La [fiche de contrôle de ces revues](../../research_notes/Sprint-1/revue-code-accessibilite-condition4.md) prépare les points et les traces à archiver, sans revue tenue ni résultat prérempli.
5. La revue de confidentialité confirme qu'aucun identifiant permanent n'a été introduit pour un visiteur. La [fiche de contrôle de cette condition](../../research_notes/Sprint-1/revue-confidentialite-condition5.md) prépare la revue sans résultat prérempli.
6. La file de modération est armée, l'astreinte est nominée et le test à blanc du signalement visiteur jusqu'à la notification d'auteur est réussi. La [fiche de contrôle de cette condition](../../research_notes/Sprint-1/fiche-controle-condition6.md) prépare les points à vérifier et les preuves à archiver, sans titulaire ni résultat prérempli.
7. La mise à jour automatique est vérifiée sur `mobile`, `web` et `desktop` selon la section 10.1, avec la preuve du contrôle de signature, du retour arrière et de la non interruption de session. La [fiche de préparation du premier rendu signé](../../research_notes/Sprint-1/fiche-premier-rendu-signe.md) prépare ces preuves par client, sans signature ni résultat préremplis.

La condition 6 est détaillée dans `../Operations/README.md`. La condition 7 est détaillée dans `../Technique/securite.md`. La roadmap renvoie à cette section 11 pour les critères de sortie de la Phase 1 et exige la trace datée des revues de cas d'erreur, de revue de code, de revue d'accessibilité et de mise à jour.

## 12. Risques et dépendances

| Risque | Effet | Mesure |
|---|---|---|
| Fil vide au lancement | Les visiteurs repartent avant de s'inscrire | Recruter des créateurs avant l'ouverture publique, selon `../Growth/README.md`, puis appliquer le repli immédiat vers le fil général de la ville concernée selon A-10, sans seuil chiffré |
| Coût de la vidéo | La facture CDN dépasse l'enveloppe inscrite en D-022 | Transcoding adaptatif, plafond de préchargement, seuil de 0,001 USD par vue inscrit en D-022 et lu par ville |
| Comptes fictifs | La confiance s'effondre dans le chat | Vérification d'email, limites de vitesse, signalement dès le MVP |
| Inscription trop tôt | La portée du réseau reste faible | Tester le parcours visiteur contre un mur de connexion au lancement, selon `./experimentation.md` |
| File de modération saturée | Les vidéos restent en attente | Prioriser par motif, alerte avec destinataire nommé et montée en charge décrite dans `../Operations/README.md` |
| Stack retenue mal appliquée | Le chantier diverge du cadre validé | Respecter D-009 et `../Technique/adr-001-stack.md`, revue en CI et contrôle des versions LTS |
| Cycle de validation des stores | Une correction mobile attend un guichet externe | Six catégories servies côté serveur selon A-13, arbitrée le 26 novembre 2026 ; binaire natif soumis au circuit du store |

## 13. Suivi des décisions et points restants

Aucune question ouverte ne reste au registre au 26 novembre 2026. Les décisions retenues et les arbitrages inscrits sont opposables dans [decisions.md](./decisions.md). Les points restant à lever sont suivis dans [arbitrage.md](./arbitrage.md) selon leur échéance. Les points A-01 à A-11 et A-13 sont arbitrés et inscrits ce jour. A-04, A-05, A-08, A-09 et A-10 sont inscrits sans numéro D supplémentaire. A-09 retient la couverture de 08:00 à 20:00 en heure locale avec astreinte P1 hors plage, et le renfort bénévole coopté et encadré. A-12 reste à lever.

| Sujet | Identifiant | Phase | Traitement |
|---|---|---|---|
| Règle N2 pour les candidatures, vérification à la demande de l'employeur | D-010 retenue le 26 novembre 2026 | Phase 2, hors MVP | Avant l'ouverture des offres |
| Niveau organisations payant `Organisation Avancée`, privilèges définis | D-011 retenue le 26 novembre 2026 | Phase 5 | Avant la conception du niveau payant |
| Budget CDN et modération, 1 000 USD par mois et 0,001 USD par vue | D-022 retenue le 26 novembre 2026 | Phase 1, avant FS-02 | Inscrite avant `video.md` et la montée en charge |
| Équipe intérimaire et outils IA, jamais auteurs, prestataires `desktop` à nommer | A-04 arbitrée le 26 novembre 2026 | Avant le premier commit de code de stack | Porteur unique et intérimaire ; effectif du PRD comme référence de planification, pas comme engagement |
| Jalons par critères de sortie, sans date de lancement fixée | A-05 arbitrée le 26 novembre 2026 | Toutes les phases | Date de lancement à nommer avant le planning ; recrutement et astreinte déclenchés par les critères |
| Français seul jusqu'à la Phase 3, langues suivantes inscrites au registre | A-08 arbitrée le 26 novembre 2026, D-008 | Phases 0 à 5 | Date, responsable et marché inscrits avant le premier contenu dans une nouvelle langue |
| Seuil de fil non vide | A-10 arbitrée le 26 novembre 2026 | Ouverture publique | Aucun seuil ; repli immédiat vers le fil général de la ville concernée, sans transposition |
| Langues à valider avec chaque marché, avec date et responsable inscrits au registre | D-008 | Phases 3 et 4 | À chaque ouverture de marché |
| Date de lancement | A-05 arbitrée le 26 novembre 2026 | Phase 1 | Aucune date inventée ; date à nommer avant le planning |
| Modèle de modération, couverture et renfort | A-09 arbitrée le 26 novembre 2026 | Avant ouverture | Couverture de 08:00 à 20:00 en heure locale, astreinte P1 hors plage et renfort bénévole coopté avec engagement écrit et relecture obligatoire, écrits dans `../Operations/README.md` et `../Operations/astreinte.md` |
| Seuil et phase d'un éventuel plafond de lecture | à nommer | À trancher | Sans valeur avancée dans ce cadrage ; ce plafond n'est pas le seuil de fil non vide tranché en A-10 |
| Part du `mobile` modifiable hors binaire natif | A-13 arbitrée le 26 novembre 2026 | Phase 1 | Six catégories fermées servies sans binaire natif, preuves des stores datées dans `./arbitrage.md` |

La question de l'ordre de lecture des fichiers est tranchée dans `docs/README.md` : les sections sont numérotées et aucun préfixe numérique n'est ajouté aux noms de fichiers.

## 14. Phase 2 : organisations, entreprises et pages

Une organisation vérifiée peut posséder plusieurs pages. Toutes les pages utilisent le même modèle, avec les mêmes capacités. Une page parle au nom de l'organisation, jamais au nom d'une personne. Les actions réalisées depuis une page sont attribuées à un compte identifié et journalisées. Cette section ne modifie pas le périmètre du MVP défini en section 3.

### 14.1 Pages et rattachement

- Une organisation possède une page principale, puis autant de pages rattachées que nécessaire : département, marque, antenne ou équipe.
- Les pages rattachées portent un nom et un rattachement différents, mais elles disposent des mêmes fonctions que la page principale.
- Aucune catégorie de page n'est réservée à un usage particulier dans le modèle. Une page peut publier, modérer et afficher des personnes dès sa création.
- Les offres d'emploi arriveront avec la phase emploi et seront disponibles sur toutes les pages, sans créer un type de page distinct.

Une page commence à l'état `unverified`. Elle ne devient publique qu'après vérification de l'entité mère. Une personne peut appartenir à plusieurs organisations avec des rôles différents, mais un rôle s'applique toujours à une page précise, jamais à l'ensemble du réseau.

### 14.2 Rôles dans une organisation

| Rôle | Ce qu'il peut faire | Ce qu'il ne peut pas faire | Condition |
|---|---|---|---|
| Propriétaire | Créer l'organisation, demander la vérification, nommer et révoquer les administrateurs, supprimer la page | Publier une offre sans disposer du rôle recruteur | Compte N3, domaine ou document légal vérifié |
| Administrateur | Modifier les paramètres de la page, inviter des personnes, nommer les éditeurs, recruteurs, analystes et modérateurs | Supprimer la page, changer le propriétaire | Nommé par le propriétaire, invitation acceptée |
| Éditeur de contenu | Publier des vidéos et des textes au nom de la page, programmer une publication, répondre aux commentaires | Modifier les rôles, publier des offres | Compte N1 au minimum, invitation acceptée |
| Recruteur | Publier des offres, consulter les candidatures, répondre aux candidats | Modifier les paramètres de la page, nommer d'autres rôles | Compte N2 au minimum, rôle activé en phase emploi après D-010 |
| Analyste | Consulter les statistiques et exporter des rapports | Publier, modérer, modifier les paramètres | Nommé par un administrateur |
| Modérateur de page | Masquer les commentaires, traiter les signalements sur le contenu de la page | Retirer la page, suspendre un compte | Nommé par un administrateur |
| Membre de l'organisation | Être rattaché à l'organisation, apparaître dans la liste des personnes, être mentionné | Gérer la page par défaut | Invitation acceptée, email vérifié |

Les permissions sont propres à chaque page. Un même compte peut être éditeur sur une page et analyste sur une autre. Aucun mot de passe ni identifiant n'est partagé entre personnes. Chaque nomination, révocation et publication au nom de la page est enregistrée dans le journal d'audit.

### 14.3 Création et vérification

1. Un compte N1 demande la création d'une organisation. L'état est `unverified`.
2. Il fournit une adresse email de domaine ou un document légal selon le type d'entité.
3. Après vérification, l'état passe à `verified`, ce qui correspond au niveau N3 de la vision.
4. La page principale devient publique. Le demandeur devient propriétaire.
5. Le propriétaire crée les pages rattachées et nomme les rôles.
6. Chaque invitation est acceptée par la personne concernée après vérification de son email.

Une organisation peut être refusée ou suspendue. Dans ce cas, ses pages cessent d'être publiques et un motif est envoyé au propriétaire avec une voie de contestation. La vérification N3 par domaine ou document légal ne doit pas être confondue avec la vérification de profil N2, qui suit D-010, retenue le 26 novembre 2026.

### 14.4 Ce que cela change pour le MVP

Rien dans la phase 1. Cette section sert de spécification pour la phase 2 et évite de devoir réécrire la matrice des droits plus tard. Les écrans, les endpoints et les tests associés seront détaillés dans un cahier des charges de phase 2 ou dans un fichier `docs/pages-organisation.md` si le sujet devient plus dense.

### 14.5 Gratuité des phases 1 à 4 et niveau payant de la phase 5

Les pages et les rôles décrits ici sont gratuits. Aucun rôle, aucun rattachement et aucune fonction de page n'est réservé à un abonnement dans la première version des pages. Le réseau est gratuit à 100 % pendant les phases 1 à 4, avec pour objectif d'attirer les personnes en recherche d'emploi.

La Phase 5 introduit `Organisation Avancée`, niveau payant défini par D-011, retenue le 26 novembre 2026. Ses privilèges se limitent aux statistiques agrégées avancées des pages de l'organisation, à l'export mensuel et aux alertes de suivi définies par l'organisation. Aucun classement payant dans la recherche, y compris en Phase 5. Les offres signalées éventuelles restent hors recherche et relèvent de la Phase 5. Le nom retenu est distinct de celui du réseau Pro.

## 15. Liens

- [Document de vision](./vision.md)
- [Manifeste](./manifeste.md)
- [Décisions produit](./decisions.md)
- [Dictionnaire de mesures](./mesure.md)
- [Fiche d'expérimentation](./experimentation.md)
- [Tableau de bord](./tableau-de-bord.md)
- [Parcours utilisateur](../UX/userflow.md)
- [Histoires utilisateur](../UX/userstories.md)
- [Défauts de rédaction IA et conseils de relecture](../Redaction/ia-defauts-et-tips.md)
