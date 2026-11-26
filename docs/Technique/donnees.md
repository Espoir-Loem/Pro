# Données : tables et transitions

**Propriétaire.** Espoir LOEMBA, intérimaire depuis le 25 novembre 2026 au titre de A-04. **Statut.** proposée. **Date.** 25 novembre 2026.
**Règle de conflit.** `../Conformite/conservation.md` est la source unique de la politique de conservation. Ce document en est la traduction technique. En cas de divergence, la fiche Conformité prévaut et cette traduction est corrigée.

## Tables héritées du PRD

`guest_session` porte jeton, métier, ville, création et expiration selon `adr-002-identite-session.md`. `account` porte identifiant, email, empreinte du mot de passe, état et création. `profile` porte compte, nom affiché, métier, ville, bio, photo et visibilité des champs. `video` porte identifiant, auteur, clé d'objet, état, légende, durée et création. `interaction` porte identifiant, compte, vidéo, type et création. `report` porte identifiant, référence du signalant dérivée de la clé de modération, cible, motif et état. `moderation_action` porte identifiant, signalement, acteur, action, motif, création et référence de contestation nullable.

Le message sépare trois dimensions au lieu d'un état unique : état de livraison (`sent`, `delivered`, `read`), indicateur de signalement, indicateur de blocage. Un message peut être lu et signalé en même temps.

## Tables ajoutées

| Table | Champs | Règle |
|---|---|---|
| `comment` | identifiant, compte auteur, vidéo, corps, création, modification, suppression logique | Corps limité à 280 caractères, selon FS-06 |
| `block` | bloquant, bloqué, création | Vérifié avant ouverture de la fenêtre de chat et avant envoi, selon FS-07 |
| `analytics_event` | identifiant, type, `session_id` nullable, `account_id` nullable, horodatage, plateforme (`mobile`, `web`, `desktop`), `city`, `trade`, `campaign_ref` optionnels, expiration | Aucun identifiant d'appareil, y compris sur desktop, aucun jeton push, aucun jeton de session brut. Schéma décrit dans `observation.md` |
| `push_subscription` | identifiant, compte obligatoire, plateforme (`mobile`, `web`, `desktop`), jeton fournisseur, date d'opt-in, date de révocation | Aucune ligne sans compte. Aucun abonnement visiteur |
| `appeal` | identifiant, signalement, empreinte du jeton, création, expiration, texte, état, décision, motif, utilisateur qui a statué | Jeton à usage unique, expiré après décision |

Le champ `plateforme` accepte exactement `mobile`, `web` et `desktop` sur `analytics_event` et sur `push_subscription`. Aucun identifiant d'appareil permanent n'est stocké, y compris sur desktop : ni identifiant de machine, ni identifiant d'installation, ni empreinte matérielle. Les événements émis par le client desktop suivent la même conservation de 30 jours que ceux des autres plateformes, selon `../Conformite/conservation.md`.

`moderation_action` est liée à `appeal` par `appeal_id` nullable. L'ouverture d'une contestation écrit une ligne `appeal` puis met à jour le signalement en `appealed`. La décision écrit `decision`, `motif` et l'utilisateur qui a statué, puis révoque le jeton : toute nouvelle tentative est refusée. Aucun jeton brut n'est stocké, seulement son empreinte.

## Transitions d'état

| Objet | État source | État cible | Acteur | Motif ou règle |
|---|---|---|---|---|
| Vidéo | `draft` | `uploading` | `auteur` | Dépôt accepté |
| Vidéo | `uploading` | `pending_review` | `system` | Règle `upload_complete` |
| Vidéo | `pending_review` | `published` | `system` | Règle `auto_publish`, `rule_id` journalisé selon `adr-003-porte-publication.md` |
| Vidéo | `pending_review` | `published` | `moderateur` | Décision humaine, motif obligatoire |
| Vidéo | `pending_review` | `rejected` | `system` ou `moderateur` | Règle ou motif journalisé |
| Vidéo | `published` | `removed` | `moderateur` | Retrait avec notification et lien de contestation |
| Vidéo | `removed` | suppression objet | `system` | Après le délai défini dans `../Conformite/conservation.md` |
| Signalement | `open` | `in_review` | `moderateur` | Prise en charge |
| Signalement | `in_review` | `resolved` | `moderateur` | Décision journalisée |
| Signalement | `resolved` | `appealed` | `system` | Ouverture d'une ligne `appeal` |
| Signalement | `appealed` | `closed` | `moderateur` | Décision de contestation écrite |
| Compte | `active` | `suspended` | `moderateur` | Sanction avec notification |
| Compte | `active` | `deleted` | `auteur` ou `system` | Selon `../Conformite/conservation.md` |

## Suppression de compte

Le profil public et les vidéos associées sont supprimés. Le sort des messages, signalements et actions de modération est celui que `../Conformite/conservation.md` prescrit. Le journal d'audit est en ajout seul : une décision passée n'est pas réécrite, elle est complétée par une nouvelle ligne datée.

## Vérification

Un test de migration vérifie la présence des cinq tables ajoutées, l'unicité de l'empreinte du jeton de contestation, l'absence de ligne `push_subscription` sans compte et la présence de `system` dans les transitions automatiques.
