# Opérations : exploitation, modération et support

**Métier.** Modération, support, animation de créateurs et continuité de service.  
**Déclencheur.** File de modération armée avant tout lien public, astreinte nominée avant la première mise en ligne.  
**Dépendances.** [PRD](../Product/prd.md), [Dictionnaire de mesures](../Product/mesure.md), [Décisions produit](../Product/decisions.md), [Recherche UX](../UX/ux-research.md), [Technique](../Technique/README.md), [Conformité](../Conformite/README.md).  
**Propriétaire.** Coordinateur des opérations, à nommer. Un référent par ville, à nommer.  
**Statut.** Procédures écrites, titulaires et numéro d’urgence à nommer, exercice à blanc à passer. Modèle bénévole ou salarié à trancher. Budget CDN à fixer après D-022.

**Règle.** La file de modération existe dès le MVP. Brazzaville et Kinshasa sont deux villes distinctes : volumes, garde, incidents et mesures ne sont pas fusionnés. Aucune valeur de l’une n’est extrapolée vers l’autre. La dimension `plateforme` s’ajoute à la ville comme dimension de lecture : `mobile` pour les applications natives iOS et Android, `web` pour le navigateur, `desktop` pour l’application exécutable Windows et macOS, rapide, sans lenteur. Linux est différé. Une coupure peut toucher le client desktop seul. L’exercice à blanc et la montée en charge couvrent les trois clients. Aucun titulaire n’est inventé : les propriétaires restent « à nommer ».

| Document | Question traitée | Ville | Déclencheur | Propriétaire |
|---|---|---|---|---|
| [journee-type-moderation.md](./journee-type-moderation.md) | Volume, priorités P1 à P3, délais et escalade | Brazzaville, Kinshasa | Avant tout lien public | Coordinateur des opérations, à nommer |
| [astreinte.md](./astreinte.md) | Rôles de garde, rotation, canal, numéro, passation | Brazzaville, Kinshasa, commun | Avant la première mise en ligne | Coordinateur des opérations, à nommer |
| [montee-en-charge.md](./montee-en-charge.md) | Courbes, seuils de bascule, budget CDN, capacité | Brazzaville, Kinshasa | Avant ouverture publique | Référent technique, à nommer |
| [moderation-manuel.md](./moderation-manuel.md) | Traitement d’un ticket, masquage, suspension, canaux | Brazzaville, Kinshasa | Avant FS-09 | Référent modération, à nommer |
| [contestation.md](./contestation.md) | Réception, délai unique, nouveau ticket, réponse | Brazzaville, Kinshasa | Avant notification des décisions | Référent modération, à nommer |
| [support.md](./support.md) | Questions sur le compte, la vidéo et le chat | Brazzaville, Kinshasa | Avant le lancement | Référent support, à nommer |
| [incidents.md](./incidents.md) | Gravité, décideur, coupure, journal, postmortem | Brazzaville, Kinshasa | Avant la première mise en ligne | Coordinateur des opérations, à nommer |
| [animation-createurs.md](./animation-createurs.md) | Recrutement et relance des créateurs pilotes | Brazzaville, Kinshasa | Avant la phase 1 | Référent ville, à nommer |
| [veille-arnaque.md](./veille-arnaque.md) | Avertissements du chat et signaux récurrents | Brazzaville, Kinshasa | Avant ouverture, pas après les premiers signalements | Référent confiance, à nommer |

Les fiches [incidents.md](./incidents.md) et [support.md](./support.md) lisent chaque situation avec la ville et la plateforme. Une panne limitée au client `desktop` est consignée comme telle, sans fusion avec `mobile` ou `web`. Les fiches [journee-type-moderation.md](./journee-type-moderation.md), [astreinte.md](./astreinte.md) et [montee-en-charge.md](./montee-en-charge.md) couvrent les trois clients dans l'exercice à blanc et dans la montée en charge. Les définitions de mesure sont dans [mesure.md](../Product/mesure.md), les arbitrages dans [decisions.md](../Product/decisions.md) et les contrôles dans [Technique](../Technique/README.md).

## Décisions à trancher avant ouverture

- Modèle bénévole ou salarié de la modération, sans le présenter comme déjà choisi.
- Budget CDN et coût maximal pour 1 000 vidéos vues, après arbitrage D-022 dans [decisions.md](../Product/decisions.md).
- Seuil de fil non vide, dans [lanceurs-metiers.md](../Growth/lanceurs-metiers.md).
- Ajout des avertissements arnaque à FS-07, dans [veille-arnaque.md](./veille-arnaque.md).

## Décision déjà écrite

Le recours du signalant visiteur est une **absence de recours écrite**, écrite dans [contestation.md](./contestation.md). Aucun recours anonyme n’est ouvert en parallèle.

## Première action

Jouer l’exercice à blanc décrit dans [astreinte.md](./astreinte.md) : signalement visiteur, ticket pseudonymé, priorité P1, relecture, notification d’auteur et validation du délai cible. Le résultat est consigné dans le canal unique avant tout lien public.
