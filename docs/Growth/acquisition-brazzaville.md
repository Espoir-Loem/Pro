# Acquisition à Brazzaville

**Déclencheur.** Avant ouverture du MVP.  
**Dépendances.** [phrases d’invitation](./phrases-invitation.md), [partenariats](./partenariats.md), [lanceurs de métiers](./lanceurs-metiers.md), [mesure des campagnes](./mesure-campagnes.md), [PRD](../Product/prd.md), [Recherche UX](../UX/ux-research.md).  
**Propriétaire.** Référent ville Brazzaville, à nommer.  
**Statut.** Cible et catégories de partenaires écrites, noms à nommer, validation écrite à obtenir.

**Périmètre.** République du Congo, ville de Brazzaville. Aucune prévision n’est reprise de Kinshasa. Gratuité totale pendant l’acquisition. Le recrutement est déclenché par les critères de sortie selon A-05, sans date de lancement fixée ni date de campagne inventée dans cette fiche.

## Cible propre à Brazzaville

| Ville | Métiers pilotes | Cible avant ouverture | Vérification |
|---|---|---|---|
| Brazzaville | Artisanat, commerce, santé | 3 créateurs actifs, 9 vidéos publiées et modérées | `video_published` avec `city=Brazzaville` |

La phrase d’invitation retenue est choisie dans [phrases-invitation.md](./phrases-invitation.md) puis validée par écrit pour Brazzaville. Aucune promesse d’emploi, de salaire, de vérification N2 au MVP, de classement payant ou d’offre d’emploi au MVP n’est autorisée. Les messages et les liens couvrent les trois clients de la dimension `plateforme` : `mobile` pour les applications natives iOS et Android, `web` pour le navigateur, `desktop` pour l'application exécutable Windows et macOS, rapide, sans lenteur, et restent sans promesse d'emploi. Linux est différé. La cible propre à Brazzaville ne change pas. Si un métier pilote n’a pas de vidéo modérée à Brazzaville, le fil général de Brazzaville est servi immédiatement selon A-10, sans seuil chiffré. La décision de repli est écrite avec la ville, la date et le propriétaire, sans transposition vers Kinshasa.

## Partenaires à nommer

| Ville | Partenaire à nommer | Rôle pour la campagne | Propriétaire |
|---|---|---|---|
| Brazzaville | Cabinet de formation professionnelle à Brazzaville, à nommer | Diffuser l’invitation auprès de personnes en recherche d’emploi | à nommer |
| Brazzaville | Média local de Brazzaville, à nommer | Expliquer le principe du fil vidéo sans promesse d’embauche | à nommer |

Le circuit de validation est décrit dans [partenariats.md](./partenariats.md). Chaque partenaire signe une phrase autorisée avant publication de tout lien.

## Mesure

Les liens portent `campaign_ref=BRAZZAVILLE`, `city=Brazzaville` et `plateforme` avec une des trois valeurs `mobile`, `web` ou `desktop`. La lecture et la conversion sont mesurées avant `signup_verified` avec les sessions visiteurs, sans fusion avec les événements de compte. Le détail est dans [mesure-campagnes.md](./mesure-campagnes.md).
