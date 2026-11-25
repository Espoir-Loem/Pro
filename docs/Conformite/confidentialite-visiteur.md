# Confidentialité du visiteur

**Source primaire.** [RGPD article 5](https://eur-lex.europa.eu/eli/reg/2016/679/oj) pour la minimisation, [EDPB 4/2019](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201904_dataprotection_by_design_and_by_default_v2.0_en.pdf) pour la protection dès la conception, [PRD FS-01 et FS-11](../Product/prd.md).
**Propriétaire de validation.** à nommer. **Statut.** proposée. **Date.** 25 novembre 2026.
**Règle de vocabulaire.** Parler de visiteur non connecté, jamais d'utilisateur anonyme.

## Périmètre des plateformes

La dimension de lecture `plateforme` prend trois valeurs : `mobile` pour les applications natives iOS et Android, `web` pour le navigateur, `desktop` pour l'application exécutable Windows et macOS, rapide, sans lenteur. Linux est différé. Les contrôles ci-dessous couvrent les trois clients et la vérification réseau est menée sur chacun d'eux. Aucune jointure avec `signup_verified` n'est introduite pour le visiteur, quelle que soit la plateforme. Les définitions de mesure restent celles de [mesure.md](../Product/mesure.md), les arbitrages celles de [decisions.md](../Product/decisions.md) et les contrôles techniques sont décrits dans [Technique](../Technique/README.md).

## Contrôles

| Contrôle | Règle | Vérification |
|---|---|---|
| Jeton de session | Court et non durable, durée proposée de 15 minutes, à confirmer dans [adr-002](../Technique/adr-002-identite-session.md) | Un jeton expiré est refusé |
| Identifiant permanent | Aucun identifiant d'appareil stocké, calculé ou transmis sur `mobile`, `web` ou `desktop`, y compris sur l'application exécutable Windows et macOS | Aucun champ d'appareil dans `analytics_event`, quelle que soit la plateforme |
| Traceurs tiers | Aucun traceur tiers dans le parcours du visiteur, desktop compris | Analyse du réseau sur les trois clients : `mobile`, `web` et `desktop` |
| Suivi entre appareils | Aucune correspondance entre appareils | Test de deux sessions distinctes sans recoupement, sur chaque plateforme et entre plateformes |
| Pseudonymes | Clé distincte par finalité, conservée séparément des pseudonymes | Revue de confidentialité |
| Push | Aucun jeton push visiteur, abonnement réservé au compte | Aucune ligne `push_subscription` sans compte |
| Événements | Trente jours de conservation, champs optionnels `city`, `trade`, `campaign_ref` et `plateforme` (`mobile`, `web`, `desktop`) | Requête de purge quotidienne journalisée |
| Métadonnées vidéo | Retrait EXIF et GPS avant stockage | Objet consultable sans coordonnée |
| Signalement visiteur | Référence pseudonyme issue de la clé de modération | Aucune jointure avec `signup_verified` |
| Mise à jour automatique | Aucun identifiant d'appareil, d'installation ou de machine créé par le mécanisme de mise à jour, aucune jointure avec `signup_verified` ; la version appliquée reste dans un journal technique sans rattachement à une personne | Revue du journal technique : zéro identifiant d'installation et aucune jointure |

## Voie de recours du signalant

Choix produit déjà écrit : le signalement fait par un visiteur n'ouvre pas de notification nominative ni de recours rattachés à une identité. Le recours anonyme par jeton n'est pas ouvert en parallèle, selon [contestation.md](../Operations/contestation.md). Si l'Union européenne est desservie, la question est à soumettre à conseil avec l'article 20 du DSA, sans en déduire une règle actuelle.

## Liaison à l'inscription

Au moment de `signup_verified`, les événements antérieurs ne sont pas rattachés au compte. Les dénominateurs visiteur et compte restent distincts dans [mesure.md](../Product/mesure.md).
