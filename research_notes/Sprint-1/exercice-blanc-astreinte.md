# Fiche de contrôle de l'exercice à blanc de l'astreinte

**Statut** : préparée le 27 novembre 2026, aucun exercice exécuté, aucun titulaire nommé, aucun délai mesuré, aucune porte levée  
**Sources canoniques** : [Astreinte](../../docs/Operations/astreinte.md), [A-09 au registre](../../docs/Product/decisions.md), [PRD, condition 6 de la section 11](../../docs/Product/prd.md), [Roadmap, Phase 1](../../docs/Product/roadmap.md), [Incidents](../../docs/Operations/incidents.md), [Opérations](../../docs/Operations/README.md)  
**Règle** : cette fiche décrit les scénarios à jouer et les preuves à archiver. Elle n'exécute aucun exercice, n'avance aucun délai relevé, ne nomme aucun titulaire et ne lève aucune porte.

## 1. Ce qui est déjà écrit

L'astreinte est armée quand les critères de sortie sont vrais, selon A-05, sans date de lancement fixée. L'exercice à blanc a lieu avant ouverture, puis chaque mois. Il est joué pour Brazzaville et pour Kinshasa, sur `mobile`, `web` et `desktop`. Le scénario va du signalement visiteur au ticket pseudonymé, à la priorité P1, à la relecture par une deuxième personne, à l'email canonique, au push neutre, au bandeau pour membre connecté, puis à `report_resolved`. Le délai cible de prise en charge est de 15 minutes et le délai cible de décision est de 1 heure. Un scénario complémentaire simule une coupure touchant le seul client `desktop` et vérifie l'ouverture d'un incident avec `plateforme=desktop`. L'écart constaté est inscrit comme action datée dans `incidents.md`.

Le canal `astreinte-pro` est le seul canal qui fait foi. Les discussions parallèles ne déclenchent aucune action. Les rôles sont coordinateur de garde, communication et opérations, par ville et pour le commun. Aucun nom ni numéro n'est supposé : chaque titulaire reste à nommer. La couverture A-09 est de 08:00 à 20:00 en heure locale, avec astreinte pour les P1 hors plage.

## 2. Scénarios à rejouer

| Identifiant | Ville et plateforme | Geste à rejouer | Résultat attendu | Preuve à archiver |
|---|---|---|---|---|
| E1 | Brazzaville et Kinshasa, `mobile`, `web`, `desktop` | Un visiteur signale un contenu | Un ticket pseudonymé est ouvert dans le canal unique, avec ville et plateforme | Extrait du ticket et du canal, sans nom de visiteur |
| E2 | Brazzaville et Kinshasa, chaque plateforme | Le ticket est qualifié en priorité P1 | Le coordinateur de garde décide et ouvre l'incident | Trace de la décision avec date et ville |
| E3 | Brazzaville et Kinshasa, chaque plateforme | Une deuxième personne relit la décision | La relecture est tracée avant tout effet visible | Trace de relecture avec identifiant du relecteur |
| E4 | Brazzaville et Kinshasa, chaque plateforme | L'email canonique est envoyé | Le message reste conforme au texte canonique, sans donnée inventée | Extrait de l'email envoyé |
| E5 | Brazzaville et Kinshasa, chaque plateforme | Le push neutre est envoyé | Le message reste neutre et ne révèle pas le motif du signalement | Extrait du push |
| E6 | Brazzaville et Kinshasa, chaque plateforme | Un membre connecté voit le bandeau | Le bandeau apparaît au membre concerné, sans exposition visiteur | Extrait du rendu pour le membre |
| E7 | Brazzaville et Kinshasa, chaque plateforme | L'incident est résolu | L'état passe à `report_resolved` avec date et ville | Trace de l'état final |
| E8 | Brazzaville et Kinshasa, `desktop` seul | Une coupure touchant uniquement le client `desktop` est simulée | Un incident est ouvert avec `plateforme=desktop`, sans transposition aux autres clients | Trace de l'incident avec la plateforme |

Aucun scénario n'est marqué comme réussi dans cette fiche. Aucun délai relevé, aucun nom de titulaire et aucun numéro d'urgence n'y sont inscrits.

## 3. Champs à remplir au moment de l'exercice

| Champ | Valeur |
|---|---|
| Date de l'exercice | À renseigner |
| Ville | À renseigner séparément pour Brazzaville et Kinshasa |
| Plateforme | À renseigner séparément pour `mobile`, `web` et `desktop` |
| Coordinateur de garde | À renseigner |
| Communication | À renseigner |
| Opérations | À renseigner |
| Relecteur | À renseigner |
| Canal unique utilisé | `astreinte-pro`, à confirmer à l'exercice |
| Délai de prise en charge | À renseigner, cible de 15 minutes, aucune valeur mesurée préremplie |
| Délai de décision | À renseigner, cible de 1 heure, aucune valeur mesurée préremplie |
| Incident ouvert | À renseigner, avec ville et plateforme |
| Écart constaté | À renseigner, ou aucun |
| Action datée dans `incidents.md` | À renseigner, ou aucune |
| Propriétaire du compte rendu | À renseigner |
| État | En attente d'exercice |

La cible n'est pas un résultat. Un écart reste une action datée et n'est pas transformé en réussite tacite.

## 4. Ce que cette fiche ne fait pas

Elle n'exécute aucun exercice, ne nomme aucun titulaire, ne crée aucun canal, n'envoie aucun email ni push, n'ouvre aucun incident, ne relève aucun délai, ne remplace pas les conditions 6 et 7 de la section 11 du PRD, ne lève aucune porte et ne contient aucun code applicatif.
