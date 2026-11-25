# Observation : événements et tableau de bord

**Propriétaire.** à nommer. **Statut.** proposée. **Date.** 25 novembre 2026.
**Déclencheur.** Avant l'implémentation de FS-11. Le schéma précède le code, pas le tableau de bord.
**Source des formules.** `../Product/mesure.md` est la source unique des définitions de mesures. Cette fiche fixe le schéma des événements, pas les formules.

## Événements canoniques

| Famille | Événements |
|---|---|
| Ouverture et fil | `app_open`, `feed_session_start` |
| Vidéo | `video_impression`, `video_complete`, `video_publish_attempt`, `video_published` |
| Conversion | `guest_save_attempt`, `signup_start`, `signup_verified`, `push_opt_in` |
| Social et modération | `message_sent`, `report_created`, `report_resolved`, `moderation_action`, `appeal_opened`, `appeal_resolved` |
| Santé de la file | `queue_depth`, `report_age` |

`signup_verified` désigne l'email vérifié en phase 1. Ce n'est ni la vérification N2 ni la vérification N3.

## Schéma d'un événement

Chaque ligne de `analytics_event` porte : identifiant, type pris dans la liste ci-dessus, horodatage, plateforme, `session_id` nullable, `account_id` nullable. Le champ `plateforme` prend les valeurs `mobile`, `web` et `desktop`. Les champs `city`, `trade` et `campaign_ref` sont optionnels. L'expiration est fixée à 30 jours après l'horodatage pour toutes les plateformes, y compris le desktop, conformément à `../Conformite/conservation.md`.

Aucun identifiant d'appareil permanent, aucun jeton push, aucun jeton de session brut ni aucune clé de pseudonymisation n'est écrit dans un événement. L'interdiction s'applique aussi au client desktop : ni identifiant de machine, ni identifiant d'installation, ni empreinte matérielle. Les événements desktop suivent la même conservation de 30 jours que les deux autres plateformes. La seule liaison entre session visiteur et compte est celle de `adr-002-identite-session.md` au moment de `signup_verified` : aucun événement antérieur n'est réécrit.

## Tableau HEART

| Objectif | Signal | Mesure | Seuil | Propriétaire | Source |
|---|---|---|---|---|---|
| Découverte du fil | Entrée dans le fil | `video_impression` sur `feed_session_start` | à confirmer | à nommer | `analytics_event` |
| Conversion vers compte | Email vérifié | `signup_verified` pour 1 000 `feed_session_start` | défini dans `../Product/mesure.md` | à nommer | `analytics_event` |
| Qualité de lecture | Vidéos terminées | `video_complete` sur `video_impression` | à confirmer | à nommer | `analytics_event` |
| Santé de la modération | Âge des signalements | `report_age` médian et p95 | à confirmer | à nommer | `analytics_event` |

## Tableau de bord et alertes

Les vues sont ventilées par `city`, `trade` et `campaign_ref` quand ces champs sont présents, sans identifiant permanent. Les alertes portent sur `queue_depth`, sur le p95 de `report_age` et sur le taux d'échec d'envoi vidéo, avec destinataire défini dans `../Operations/README.md`. Les dénominateurs visiteur et compte restent distincts.

## Vérification

Un test de schéma en intégration refuse tout type d'événement absent de la liste, toute valeur de `plateforme` hors de `mobile`, `web`, `desktop` et tout champ d'appareil, y compris depuis le client desktop. Un second test vérifie qu'aucun événement antérieur à `signup_verified` ne porte d'`account_id` et qu'une ligne desktop expire après 30 jours comme les autres.
