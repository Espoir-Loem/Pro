# Fiche de contrôle de la revue de performance desktop, A-03

**Statut** : préparée le 27 novembre 2026, revue non tenue, aucune mesure relevée, aucune cible révisée, aucune porte levée  
**Sources canoniques** : [A-03 dans la grille d'arbitrage](../../docs/Product/arbitrage.md), [Performance, profil R2](../../docs/Technique/performance.md), [D-023 au registre](../../docs/Product/decisions.md), [Architecture](../../docs/Technique/architecture.md), [Vidéo](../../docs/Technique/video.md), [Responsabilités](../../docs/Technique/responsabilites.md), [Roadmap, Phase 1](../../docs/Product/roadmap.md)  
**Règle** : cette fiche prépare la revue prévue le 26 décembre 2026. Elle ne tient pas la revue, ne relève aucune mesure, ne révise aucune cible et ne lève aucune porte.

## 1. Ce qui est déjà arbitré

A-03 est arbitrée le 26 novembre 2026 : les cinq cibles proposées pour le client `desktop` sont retenues comme cibles de revue, pas comme résultats. La machine de référence est arrêtée à 2 cœurs, 4 Go de RAM et un disque SSD, sur Windows 11 et macOS en version supportée, ces deux systèmes étant traités séparément. La méthode retenue est de 30 lancements à froid par système, avec p75 et traces jointes. La revue est prévue le 26 décembre 2026. Aucune mesure de Pro n'est disponible à la date de préparation de cette fiche.

Les cinq cibles de revue portent sur le démarrage à froid jusqu'au fil interactif sous 2 secondes, le changement de vue locale sous 100 millisecondes, la première image vidéo sous 300 millisecondes sur le profil R1 avec cache froid et cache chaud séparés, la mémoire au repos sous 150 Mo et l'installateur sous 80 Mo. Les cibles autres que la première image vidéo sont lues sur la machine R2, la première image vidéo relevant du profil R1. Le profil R1 reste proposé et à confirmer : ses valeurs ne sont pas présentées comme arrêtées. L'application de messagerie légère citée comme référence de perception n'est ni une mesure relevée, ni une promesse d'égalité, ni une cible contractuelle. Aucun budget dépassé n'autorise une réduction des exigences d'accessibilité.

## 2. Points à vérifier et traces à archiver

| Identifiant | Point à vérifier | Trace à archiver | État |
|---|---|---|---|
| P1 | Machine de référence conforme à 2 cœurs, 4 Go de RAM et SSD, par système | Description de la machine utilisée, Windows et macOS séparés | À vérifier |
| P2 | Systèmes retenus séparément, Windows 11 et macOS en version supportée | Relevé des versions, sans transposition d'un système à l'autre | À vérifier |
| P3 | Trente lancements à froid par système, avec p75 calculé | Traces des lancements et du calcul du p75 | À vérifier |
| P4 | Démarrage à froid jusqu'au fil interactif sous 2 secondes | Trace par système, valeur à renseigner | À vérifier |
| P5 | Changement de vue locale sous 100 millisecondes | Trace par système, valeur à renseigner | À vérifier |
| P6 | Première image vidéo sous 300 millisecondes sur le profil R1, cache froid et chaud séparés | Trace par système et par état de cache | À vérifier |
| P7 | Mémoire au repos sous 150 Mo | Relevé par système, valeur à renseigner | À vérifier |
| P8 | Installateur sous 80 Mo | Taille relevée par système | À vérifier |
| P9 | Profil R1 confirmé ou signalé comme encore proposé | Décision écrite, ou mention de proposition inchangée | À vérifier |
| P10 | Traces jointes à `architecture.md`, `video.md` et `responsabilites.md` | Liens vers les trois pièces jointes | À vérifier |
| P11 | Exigences d'accessibilité maintenues quel que soit le budget | Extrait de la revue d'accessibilité liée | À vérifier |

Aucune ligne n'est marquée comme réussie dans cette fiche. Aucune valeur de performance, aucune p75 et aucune taille d'installateur ne sont préremplies. Les cibles ne sont pas présentées comme des promesses contractuelles.

## 3. Champs à remplir au moment de la revue

| Champ | Valeur |
|---|---|
| Date de la revue | 26 décembre 2026, date prévue, aucun résultat inscrit |
| Date effective de la revue | À renseigner |
| Système concerné | À renseigner séparément pour Windows et macOS |
| Points P1 à P11 vérifiés, un par un | À renseigner, aucune case cochée à l'avance |
| Valeurs relevées | À renseigner, aucune valeur préremplie |
| Écarts constatés | À renseigner, ou aucun |
| Cibles révisées, avec motif et date | À renseigner, ou aucune |
| Actions datées et responsables | À renseigner, ou aucune |
| Conclusion sur la revue | À renseigner, aucune conclusion préremplie |
| Propriétaire de la revue | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner |
| Archive de la revue et historique | À renseigner |
| État | En attente de revue |

Une ligne sans trace jointe n'est pas tenue pour vérifiée. Un écart reste une action datée et n'est pas transformé en réussite tacite. La révision d'une cible demande une écriture datée et ne modifie pas A-03 par silence.

## 4. Ce que cette fiche ne fait pas

Elle ne tient aucune revue, ne relève aucune mesure, ne calcule aucun p75, ne joint aucune trace, ne révise aucune cible, ne modifie pas A-03, ne lève aucune porte et ne contient aucun code applicatif.
