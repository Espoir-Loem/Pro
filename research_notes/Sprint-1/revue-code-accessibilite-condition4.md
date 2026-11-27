# Fiche de contrôle des revues de code et d'accessibilité, condition 4

**Statut** : préparée le 27 novembre 2026, aucune revue tenue, aucun relecteur nommé, aucun résultat avancé, aucune porte levée  
**Sources canoniques** : [PRD, condition 4 de la section 11](../../docs/Product/prd.md), [Roadmap, Phase 1](../../docs/Product/roadmap.md), [Principes de design](../../docs/UX/design-principles.md), [Parcours utilisateur](../../docs/UX/userflow.md), [Fiche technique et accessibilité](../../docs/Technique/README.md), [Performance](../../docs/Technique/performance.md), [D-021 au registre](../../docs/Product/decisions.md), [Revue de sortie de phase](../Planning/revue-sortie-phase.md)  
**Règle** : cette fiche décrit les points à vérifier et les traces à archiver. Elle ne tient aucune revue, ne nomme aucun relecteur, ne relève aucun résultat et ne prononce pas la condition 4.

## 1. Ce qui est déjà écrit

La condition 4 de la section 11 du PRD exige que la revue de code et la revue d'accessibilité soient passées. La roadmap demande que la trace des deux revues soit archivée avec l'identifiant du relecteur et la date. Les critères d'acceptation sont vérifiés sur les trois clients livrés ensemble : `mobile` pour les applications natives iOS et Android, `web` pour le navigateur, `desktop` pour l'application exécutable Windows et macOS. Linux est différé. Aucun client n'est revu à la place d'un autre.

Le web vise WCAG 2.2 niveau AA. Les cibles tactiles mesurent au moins 24 sur 24 pixels CSS selon SC 2.5.8, avec 44 pixels comme objectif produit au delà du minimum. Le contraste AA est vérifié à 4,5:1 pour le texte courant et à 3:1 pour les grands textes et les composants. Lecteur d'écran, ordre de focus, contraste et mouvement réduit sont vérifiés avant revue de code sur le web. Le client `desktop` suit les API d'accessibilité natives Windows et macOS, avec ordre de focus clavier et souris, contraste, mouvement réduit et taille de cible. WCAG n'est pas présenté comme une règle directe pour une application native. Les vidéos avec son du MVP portent des sous-titres générés automatiquement et corrigés par l'auteur avant publication, selon D-021, FS-02 et FS-05. Le ratio de contraste visé reste à confirmer lors de la revue d'accessibilité. Aucun de ces points n'est présenté ici comme vérifié.

## 2. Points à vérifier et traces à archiver

| Identifiant | Point à vérifier | Trace à archiver | État |
|---|---|---|---|
| R1 | Revue de code passée sur chaque client livré | Compte rendu daté avec identifiant du relecteur et périmètre relu | À vérifier |
| R2 | Critères d'acceptation de chaque FS vérifiés sur `mobile`, `web` et `desktop` | Grille de revue par FS et par plateforme | À vérifier |
| R3 | Cas d'erreur du parcours correspondant couverts par la revue | Liste des cas relus, sans cas supposé | À vérifier |
| R4 | Porte de publication et acteur `system` conformes à la règle écrite | Extrait de la revue de code sur la porte de publication | À vérifier |
| A1 | Cibles web d'au moins 24 sur 24 pixels CSS, objectif 44 pixels | Mesures relevées sur les écrans du web | À vérifier |
| A2 | Contraste web à 4,5:1 pour le texte courant et 3:1 pour les grands textes et composants | Relevé des ratios, sans valeur préremplie | À vérifier |
| A3 | Lecteur d'écran et ordre de focus vérifiés sur le web | Compte rendu de parcours au clavier et au lecteur d'écran | À vérifier |
| A4 | Mouvement réduit respecté sur le web, sans lecture automatique forcée | Extrait du contrôle de préférence de mouvement | À vérifier |
| A5 | API natives d'accessibilité et ordre de focus vérifiés sur Windows et macOS, sans transposition de WCAG en règle native | Compte rendu par système | À vérifier |
| A6 | Sous-titres corrigés avant publication pour les vidéos avec son | Preuve de correction liée à FS-02 et FS-05, selon D-021 | À vérifier |
| A7 | Ratio de contraste visé confirmé en revue d'accessibilité | Décision datée inscrite au registre si le ratio évolue | À vérifier |

Aucune ligne n'est marquée comme réussie dans cette fiche. Aucun nom de relecteur, aucune mesure et aucun extrait ne sont préremplis. Un budget dépassé n'autorise pas une réduction des exigences d'accessibilité.

## 3. Champs à remplir au moment des revues

| Champ | Valeur |
|---|---|
| Date de la revue de code | À renseigner |
| Date de la revue d'accessibilité | À renseigner |
| Client et FS concernés | À renseigner pour `mobile`, `web` et `desktop` |
| Relecteur de code | À renseigner |
| Relecteur d'accessibilité | À renseigner |
| Points R1 à R3 et A1 à A7 vérifiés, un par un | À renseigner, aucune case cochée à l'avance |
| Liens vers les traces archivées | À renseigner |
| Écarts constatés | À renseigner, ou aucun |
| Actions datées et responsables | À renseigner, ou aucune |
| Conclusion sur la condition 4 | À renseigner, aucune conclusion préremplie |
| Titulaire de la décision | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner |
| Archive de la revue et historique | À renseigner |
| État | En attente de revue |

Une ligne sans trace archivée ni relecteur nommé n'est pas tenue pour vérifiée. Un écart reste une action datée et n'est pas transformé en réussite tacite. Les revues ne modifient ni les critères d'acceptation, ni les seuils du registre, ni les conditions de la section 11.

## 4. Ce que cette fiche ne fait pas

Elle ne tient aucune revue de code ni revue d'accessibilité, ne nomme aucun relecteur, ne relève aucune mesure, ne prononce pas la condition 4, ne clôt aucune phase, ne lève aucune porte et ne contient aucun code applicatif.
