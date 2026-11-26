# Lanceurs de métiers

**Déclencheur.** Avant le fil public et avant toute campagne liée.  
**Dépendances.** [Recherche UX](../UX/ux-research.md), [PRD](../Product/prd.md), [Dictionnaire de mesures](../Product/mesure.md), [animation des créateurs](../Operations/animation-createurs.md).  
**Propriétaire.** Référent croissance, à nommer. Référent ville par ville, à nommer.  
**Statut.** Cibles chiffrées écrites comme hypothèses de planification, seuil de fil non vide tranché par A-10 : aucun seuil et repli immédiat vers le fil général de la ville concernée, métiers à confirmer par écrit.

**Périmètre des plateformes.** Les messages, les liens et les relances couvrent les trois clients de la dimension `plateforme` : `mobile` pour les applications natives iOS et Android, `web` pour le navigateur, `desktop` pour l'application exécutable Windows et macOS, rapide, sans lenteur, et restent sans promesse d'emploi. Linux est différé. Les cibles par ville restent des hypothèses de planification. Le seuil de fil non vide est tranché par A-10 : aucun seuil.

## Semis par ville

| Ville | Métiers pilotes, trois au maximum | Cible vérifiée avec `video_published` | Propriétaire |
|---|---|---|---|
| Brazzaville | Artisanat, commerce, santé | 3 créateurs, 9 vidéos publiées et modérées | à nommer |
| Kinshasa | Logistique, enseignement, tech | 4 créateurs, 12 vidéos publiées et modérées | à nommer |

Les libellés viennent de la liste de secteurs du plan de terrain de la [recherche UX](../UX/ux-research.md), section 8. Ils ne sont pas des résultats d’entretiens et n’annoncent aucune prévalence. La personne qui mène la recherche les confirme par écrit avant recrutement. Aucun quatrième métier n’est ajouté sans décision écrite.

## Seuil de fil non vide

Aucun seuil minimal de vidéos visibles par métier ou par ville n'est fixé, selon A-10 arbitrée le 26 novembre 2026 et inscrite au registre. Les cibles ci-dessus restent un semis contrôlé, pas une preuve que le fil est suffisant.

Si un métier n'a pas de vidéo modérée dans une ville, le fil général de cette ville est servi immédiatement, sans écran vide et sans attente. Le repli est écrit avec la ville, la date et le propriétaire. Aucune valeur ni décision de repli n'est transposée à l'autre ville.

## Engagement et relance

| Ville | Engagement minimal sur deux semaines | Relances | Propriétaire |
|---|---|---|---|
| Brazzaville | 1 vidéo par créateur et par semaine, publiée et modérée | J-7 puis J-3 | à nommer |
| Kinshasa | 1 vidéo par créateur et par semaine, publiée et modérée | J-7 puis J-3 | à nommer |

Le calendrier détaillé est dans [animation-createurs.md](../Operations/animation-createurs.md). La mesure utilise `video_published` et `video_complete`, avec `city`, `trade` et `plateforme`, sans fusion avec les sessions visiteurs décrites dans [mesure-campagnes.md](./mesure-campagnes.md).
