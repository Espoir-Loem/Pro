# Astreinte

**Déclencheur.** Avant la première mise en ligne, pour donner un destinataire aux alertes du [PRD](../Product/prd.md). La [trame de décision d'ouverture publique](../../research_notes/Planning/decision-ouverture-publique.md) prépare cette étape sans date ni lien public préremplis.  
**Dépendances.** [journée type](./journee-type-moderation.md), [incidents](./incidents.md), [Technique](../Technique/README.md), [Conformité](../Conformite/README.md).  
**Propriétaire.** Coordinateur des opérations, à nommer.  
**Statut.** Rôles et règles écrits, titulaires à nommer, numéro d’urgence à nommer, exercice à blanc à passer. L’astreinte est armée quand les critères de sortie sont vrais, selon A-05, sans date de lancement fixée.

**Périmètre des plateformes.** L'astreinte lit les alertes avec la ville et la plateforme : `mobile` pour les applications natives iOS et Android, `web` pour le navigateur, `desktop` pour l'application exécutable Windows et macOS, rapide, sans lenteur. Linux est différé. Une coupure peut toucher le client `desktop` seul. Aucun nom de titulaire n'est supposé.

## Rôles par ville

| Ville | Coordinateur de garde | Communication | Opérations | Numéro d’urgence | Canal unique |
|---|---|---|---|---|---|
| Brazzaville | à nommer | à nommer | à nommer | à nommer | `astreinte-pro`, à créer |
| Kinshasa | à nommer | à nommer | à nommer | à nommer | `astreinte-pro`, à créer |
| Commun | à nommer | à nommer | à nommer | à nommer | `astreinte-pro`, à créer |

Le canal `astreinte-pro` est le seul canal qui fait foi. Les discussions parallèles ne déclenchent aucune action. Le numéro d’urgence est renseigné dans ce document avant la première mise en ligne.

Le coordinateur de garde décide et ouvre l’incident. La communication prépare les textes neutres. Les opérations appliquent l’atténuation et tiennent le journal de travail. Aucun nom n’est supposé : chaque titulaire reste « à nommer » tant qu’il n’est pas fourni.

La couverture retenue en A-09 est de 08:00 à 20:00 en heure locale des deux villes. Le modérateur de garde et le relecteur forment le noyau joignable dans cette plage. Une P1 hors de la plage déclenche l'astreinte. Le renfort est bénévole, coopté par le référent ville et encadré, avec engagement écrit et relecture obligatoire. Aucun nom ni numéro n'est inventé.

## Rotation hebdomadaire

| Période | Ville | Coordinateur | Communication | Opérations |
|---|---|---|---|---|
| Semaine S | Brazzaville | à nommer | à nommer | à nommer |
| Semaine S | Kinshasa | à nommer | à nommer | à nommer |
| Semaine S+1 | Brazzaville | à nommer | à nommer | à nommer |
| Semaine S+1 | Kinshasa | à nommer | à nommer | à nommer |

La rotation court du lundi 08:00 au lundi suivant 08:00, en heure locale des deux villes, UTC+1.

```mermaid
flowchart LR
  A["Semaine S titulaires a nommer"] --> B["Passation vendredi 17h"]
  B --> C["Semaine S plus un titulaires a nommer"]
  C --> D["Exercice a blanc avant ouverture puis chaque mois"]
  D --> E["Compte rendu dans le canal unique astreinte-pro"]
  E --> A
```

## Passation

La passation a lieu chaque vendredi à 17:00 dans le canal unique. Le titulaire sortant écrit dix lignes maximum : tickets ouverts par ville, priorités P1 en cours, contestations en attente, incidents ouverts, état du CDN, décisions à trancher. Le titulaire entrant confirme la prise en charge par écrit dans le même canal.

## Exercice à blanc

Avant ouverture, puis chaque mois, un scénario est joué pour Brazzaville et pour Kinshasa, sur `mobile`, `web` et `desktop` : signalement visiteur, ticket pseudonymé, priorité P1, relecture par une deuxième personne, email canonique, push neutre, bandeau pour membre connecté, puis `report_resolved`. Le délai cible de prise en charge est 15 minutes et le délai cible de décision est 1 heure. Un scénario complémentaire simule une coupure touchant le seul client `desktop` et vérifie l'ouverture d'un incident avec `plateforme=desktop`, sans inventer de titulaire. L’écart constaté est inscrit comme action datée dans [incidents.md](./incidents.md). Une [fiche de contrôle](../../research_notes/Sprint-1/exercice-blanc-astreinte.md) prépare cet exercice sans l'exécuter ni avancer de délai mesuré.
