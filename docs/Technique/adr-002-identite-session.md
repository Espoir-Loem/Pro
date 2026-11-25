# ADR 002 : identité et session du visiteur

Décision retenue sur les principes, avec des valeurs de session encore à confirmer.

## Titre

Jeton visiteur court, pseudonymisation par finalité et liaison explicite à l'inscription vérifiée.

## Statut

retenue

## Contexte

FS-01 ouvre le fil sans compte. FS-11 émet des événements avant inscription. La vision interdit l'identifiant permanent, le suivi entre appareils et les traceurs tiers chez le visiteur. Sans décision écrite, le code peut faire d'un jeton de session un identifiant d'appareil, rattacher rétroactivement des événements au compte, ou créer un abonnement push visiteur. `signup_verified` désigne la vérification de l'email en phase 1, pas une vérification d'identité N2 ni une vérification d'organisation N3.

## Options

| Option | Effet | Traitement |
|---|---|---|
| Jeton visiteur court, non durable | Permet la session sans identifiant d'appareil | Retenue |
| Identifiant d'appareil permanent | Rend possible le suivi entre appareils | Écartée |
| Jeton push pour visiteur | Crée un identifiant d'appareil effectif | Écartée |
| Pseudonyme de modération dérivé de l'identifiant analytique | Rend possibles des jointures entre finalités | Écartée |

## Décision

Les principes suivants sont retenus.

- Le visiteur reçoit un jeton de session court, non durable, sans correspondance avec un appareil. Aucun identifiant d'appareil permanent n'est stocké ni calculé.
- Toute valeur pseudonyme est dérivée avec une clé propre à sa finalité. La clé de modération est distincte de la clé analytique et de la clé de contestation. Les clés sont conservées séparément des pseudonymes.
- Le jeton de session est rotatif. La rotation crée une nouvelle valeur et inactive l'ancienne. Aucune valeur n'est réutilisée.
- Aucun jeton push n'est créé pour un visiteur. Les abonnements push sont réservés aux comptes, conformément à `donnees.md`.
- Liaison avec `signup_verified` : au moment où `signup_verified` est émis, le compte reçoit un `account_id`. Les événements antérieurs restent pseudonymes et ne sont pas réécrits ni rattachés. Les événements postérieurs portent le `account_id`. Aucune jointure n'est faite entre la clé de pseudonymisation et `account_id`. Les dénominateurs visiteur et compte ne sont pas fusionnés.

| Paramètre | Valeur proposée | Statut de la valeur |
|---|---|---|
| Durée de vie du jeton visiteur | 15 minutes | à confirmer |
| Rotation | à chaque expiration et à chaque élévation de niveau d'accès | à confirmer |
| Conservation des événements de session | 30 jours | retenue par le PRD, traduite dans `conservation.md` |

Le statut « à confirmer » porte sur les valeurs paramétrées. Il ne remet pas en cause le statut retenu de l'ADR sur les principes.

## Conséquences

- FS-01 et FS-11 sont implémentés avec un jeton non durable et sans traceur tiers.
- Le retour à sept jours porte sur les comptes avec email vérifié, conformément à D-020 et à `../Product/mesure.md`. Aucune cohorte visiteur n'est calculée.
- La référence du signalant est dérivée de la clé de modération. Elle ne permet pas de joindre `signup_verified`.
- Le journal de publication et la table `appeal` n'enregistrent jamais le jeton brut, seulement son empreinte.
- Un test vérifie qu'un jeton expiré est refusé, qu'aucun champ d'appareil n'est présent dans `analytics_event` et qu'aucune ligne de `push_subscription` n'est créable sans compte.

## Propriétaire

à nommer

## Date

25 novembre 2026
