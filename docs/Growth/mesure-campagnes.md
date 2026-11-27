# Mesure des campagnes

**Déclencheur.** Avant le premier lien de campagne.  
**Dépendances.** [Dictionnaire de mesures](../Product/mesure.md), [PRD FS-11](../Product/prd.md), [Décisions produit](../Product/decisions.md), [Recherche UX](../UX/ux-research.md), [Technique](../Technique/README.md), [Conformité](../Conformite/README.md).  
**Propriétaire.** Référent mesure, à nommer.  
**Statut.** Événements et champs définis, tableaux de bord à construire après publication du dictionnaire de mesures.

## Événements disponibles

`app_open`, `feed_session_start`, `video_impression`, `video_complete`, `guest_save_attempt`, `signup_start`, `signup_verified`, `push_opt_in`, `video_publish_attempt`, `video_published`, `message_sent`, `report_created`, `report_resolved`, `moderation_action`, `appeal_opened`, `appeal_resolved`, `queue_depth`, `report_age`.

Chaque événement porte les champs `city`, `trade`, `campaign_ref` et `plateforme`, avec `plateforme` valant `mobile` pour les applications natives iOS et Android, `web` pour le navigateur ou `desktop` pour l'application exécutable Windows et macOS, rapide, sans lenteur, ainsi qu’un horodatage. Linux est différé. Conservation : 30 jours. Aucun identifiant d’appareil permanent, y compris sur desktop. Aucun traceur tiers dans le parcours visiteur et aucun traceur tiers sur desktop. Le rattachement d’événements antérieurs à `signup_verified` à un compte est interdit sans base documentée dans [Conformité](../Conformite/README.md). La dimension `plateforme` s'ajoute aux définitions de [mesure.md](../Product/mesure.md) et aux arbitrages de [decisions.md](../Product/decisions.md), avec le socle de [Technique](../Technique/README.md).

## Tableau de bord

| Vue | Numérateur | Dénominateur | Ventilation | Règle de non fusion |
|---|---|---|---|---|
| Découverte | `video_complete` | `feed_session_start` | `city`, `trade`, `campaign_ref`, `plateforme` | Sessions visiteur avant `signup_verified` uniquement |
| Conversion | `signup_verified` | `feed_session_start` | `city`, `campaign_ref`, `plateforme` | Inscriptions avec email vérifié pour 1 000 sessions de fil, sans entrée post inscription au dénominateur |
| Publication | `video_published` | `video_publish_attempt` | `city`, `trade`, `campaign_ref`, `plateforme` | Taux de publication séparé des sessions visiteur |
| Modération | `report_resolved` | `report_created` | `city`, `campaign_ref`, `plateforme` | `queue_depth` et `report_age` affichés séparément, avec `moderation_action`, `appeal_opened`, `appeal_resolved` |
| Chat | `message_sent` | Non agrégé avec la découverte | `city`, `trade`, `plateforme` | Aucun contenu de message dans l’événement |
| Push | `push_opt_in` | `app_open` | `city`, `campaign_ref`, `plateforme` | Population membres, jamais fusionnée avec les visiteurs |

**Interdiction explicite.** Le dénominateur avant `signup_verified` et le dénominateur après `signup_verified` ne peuvent pas être fusionnés dans un graphique, un total ou un export. Les deux séries restent séparées pour Brazzaville et pour Kinshasa, et lues par `plateforme` sans fusion entre `mobile`, `web` et `desktop`. La [fiche de contrôle des phrases et des campagnes](../../research_notes/Planning/controle-phrases-campagnes.md) prépare la vérification de ces règles de lecture, sans relevé ni résultat prérempli.

La profondeur de file et l’âge des signalements alimentent aussi les alertes de [journée type](../Operations/journee-type-moderation.md) avec les mêmes seuils et les mêmes destinataires.
