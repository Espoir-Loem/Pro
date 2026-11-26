# Inventaire des contrats typés du sprint 1

**Statut** : préparé le 26 novembre 2026, aucun contrat écrit  
**Destination** : `packages/domain`, selon la [stack retenue](../../../docs/Technique/adr-001-stack.md)  
**Règle** : cet inventaire donne les noms et leurs sources. Il ne contient ni déclaration de type, ni signature de fonction, ni interface de programmation. Aucun contrat n'est écrit avant la levée des portes.

## Entités du modèle minimal

| Contrat | Source canonique | Contenu attendu | Règle de non-régression |
|---|---|---|---|
| `guest_session` | PRD section 8 | Jeton, métier, ville, création, expiration | Aucun identifiant permanent visiteur, aucun identifiant d'appareil |
| `account` | PRD section 8 | Identifiant, email, empreinte du mot de passe, état, création | État pris dans la liste du PRD section 9 |
| `profile` | PRD section 8 et FS-04 | Compte, nom affiché, métier, ville, bio, photo, visibilité des champs | Aucune donnée privée dans une réponse publique |
| `video` | PRD section 8 et FS-02 | Identifiant, auteur, clé d'objet, état, légende, durée, création | État pris dans la liste du PRD section 9 |
| `interaction` | PRD section 8 | Identifiant, compte, vidéo, type, création | Geste volontaire, aucun historique conservé au MVP |
| `comment` | PRD section 8 et 9 | Identifiant, vidéo, compte, corps, état de livraison, état de modération, création | Les deux états restent séparés |
| `message` | PRD section 8 et 9 | Identifiant, expéditeur, destinataire, corps, état de livraison, état de modération, création | Le contrôle de `block` précède l'envoi |
| `block` | PRD section 8 | Identifiant, compte, type de cible, cible, création | Aucune identité bloquée exposée dans une réponse publique |
| `report` | PRD section 8 | Identifiant, référence du signalant, type de cible, cible, motif, état | Référence pseudonyme de session, pas d'identifiant d'appareil |
| `moderation_action` | PRD section 8 | Identifiant, signalement, acteur, action, motif, création | Acteur pris parmi `system`, `moderateur`, `auteur` |
| `appeal` | PRD section 8 | Dix champs nommés, dont empreinte du jeton, expiration, texte, état, décision, motif et utilisateur qui a statué | Jeton à usage unique, décision modifiée tracée |
| `analytics_event` | PRD section 8 et observation | Identifiant, type, horodatage, plateforme, `session_id` nullable, `account_id` nullable, `city`, `trade`, `campaign_ref` | Aucun champ d'appareil, conservation de 30 jours |
| `push_subscription` | PRD section 8 | Identifiant, compte, jeton, création, révocation | Aucun abonnement attaché à une session visiteuse |

## États et dimensions

| Contrat | Valeurs | Source canonique | Règle de non-régression |
|---|---|---|---|
| État de publication de la vidéo | `draft`, `uploading`, `pending_review`, `published`, `rejected`, `removed` | PRD section 9 | Aucune publication avant modération du texte et correction des sous-titres |
| État du compte | `unverified`, `active`, `suspended`, `deleted` | PRD section 9 | Aucune vérification d'identité ou d'organisation en phase 1 |
| États du message | Livraison `sent`, `delivered`, `read` et modération `none`, `reported`, `blocked`, `removed` | PRD section 9 | Les deux dimensions ne sont jamais fusionnées |
| États du commentaire | Livraison `sent`, `delivered` et modération `none`, `reported`, `hidden`, `removed` | PRD section 9 | Les deux dimensions ne sont jamais fusionnées |
| États du signalement et de la contestation | Signalement `open`, `in_review`, `resolved`, `appealed`, `closed` ; contestation `open`, `in_review`, `resolved`, `rejected` | PRD section 9 | Toute décision porte un motif et un acteur |
| `plateforme` | `mobile`, `web`, `desktop` | Mesure, règle commune | Distincte de `city`, `trade` et `campaign_ref`. Linux différé |
| Types d'événement | `app_open`, `feed_session_start`, `video_impression`, `video_complete`, `guest_save_attempt`, `signup_start`, `signup_verified`, `push_opt_in`, `video_publish_attempt`, `video_published`, `message_sent`, `report_created`, `report_resolved`, `moderation_action`, `appeal_opened`, `appeal_resolved`, `queue_depth`, `report_age` | [Mesure](../../../docs/Product/mesure.md), règle commune | Un type hors liste est refusé par un test de schéma |

## Points d'accès

Les noms de chemins sont des propositions de la [fiche API](../../../docs/Technique/api.md), pas des décisions du PRD. Le contrat partagé porte la validation et la sérialisation.

| Point d'accès | Contrat associé | Règle de non-régression |
|---|---|---|
| `GET /feed` | `video`, `profile`, `decision_visibilite` | Lecture sans compte, aucune donnée privée |
| `GET /video/{id}` | `video`, `profile` | Réponse sans email, téléphone ni donnée de vérification |
| `GET /search` | `profile` | Champs publics seulement, aucun classement payant selon D-019 |
| `POST /video` | `video` | État `draft` puis `uploading`, compte requis |
| `POST /report` | `report` | Visiteur autorisé, référence pseudonyme |
| `POST /appeal/{jeton}` | `appeal` | Jeton à usage unique, empreinte vérifiée |
| `GET /messages`, `POST /messages` | `message`, `block` | Contrôle de blocage avant envoi |
| `POST /signup/verify` | `account`, `analytics_event` | Émet `signup_verified`, aucun rattachement rétroactif |

## Règles partagées

| Règle | Source | Ce que le contrat doit porter |
|---|---|---|
| `decision_visibilite` | D-016 et [observation](../../../docs/Technique/observation.md) | Appliquée à la lecture, malgré le cache et le CDN |
| Repli du fil | A-10 et mesure | Aucun seuil de fil non vide, retour immédiat au fil général de la ville concernée |
| Jeton visiteur | D-012 et [identité de session](../../../docs/Technique/adr-002-identite-session.md) | Court, non durable, rotatif, aucune correspondance entre appareils |
| Sous-titres | D-021 et parcours B | Vidéo avec son en brouillon tant que la correction par l'auteur n'est pas faite |
| Mise à jour | D-024 et PRD section 10.1 | Session non interrompue, changement tracé avec acteur `system` et identifiant de règle |
| Modération | D-014 | Texte vérifiable avant publication, vidéo en `pending_review`, journal en ajout seul |

## Propriétaire et état

Tous les contrats de cet inventaire sont à écrire après la levée des portes décrites dans le [README](../README.md). Le propriétaire technique reste Espoir LOEMBA, intérimaire, jusqu'à nomination explicite des titulaires des fiches. Aucun contrat typé n'existe dans le dépôt à la date de préparation.
