# Modèle de nomination des prestataires `desktop`, Windows et macOS

**Statut** : préparé le 27 novembre 2026, aucun prestataire désigné, aucun contact, aucun montant, aucune porte levée  
**Sources canoniques** : [Grille de vérification](./prestataires-desktop.md), [Shortlist documentée](./shortlist-prestataires-desktop.md), [A-04 dans la grille d'arbitrage](../../docs/Product/arbitrage.md), [D-023 et D-024 au registre](../../docs/Product/decisions.md), [Roadmap, Phase 1](../../docs/Product/roadmap.md), [Responsabilités](../../docs/Technique/responsabilites.md), [Dossier sprint 1](./README.md)  
**Règle** : ce modèle prépare deux écritures distinctes. Il ne désigne personne, ne contacte personne, ne fixe aucun montant et ne lève aucune porte.

## 1. Ce qui est déjà écrit

Le client `desktop` est un exécutable installé sur Windows et sur macOS, livré en même temps que `mobile` et `web` selon D-023 et D-004. A-04 impose que ses prestataires soient nommés par écrit avant le premier commit de code de stack. Deux nominations distinctes sont nécessaires, une pour Windows et une pour macOS, afin que les capacités de l'un ne soient pas prêtées à l'autre. La coque Rust du desktop ne porte que la signature, l'installateur et la mise à jour, selon D-009. Le fournisseur CDN reste une question séparée, dans le cadre de D-022.

La grille de vérification porte treize points par système, dont l'identité légale confirmée sur une source récente, l'expérience de l'installateur et de la mise à jour, la signature de code, la gestion des clés par le titulaire du projet, la distribution, la notarisation pour macOS, le retour arrière, la non interruption de session, la machine de référence A-03, la disponibilité avant le premier commit, les conflits d'intérêts, la facturation et la limite de portée selon A-13 et D-024. La shortlist documentée classe des pistes publiques datées par système, sans désignation ni contact. Le titulaire intérimaire du projet est Espoir LOEMBA depuis le 25 novembre 2026 au titre de A-04, et aucun autre titulaire n'est ajouté ici.

## 2. Champs à remplir au moment de la nomination

| Champ | Windows | macOS |
|---|---|---|
| Prestataire désigné | À renseigner, aucun nom prérempli | À renseigner, aucun nom prérempli |
| Responsable de mission | À renseigner, si connu | À renseigner, si connu |
| Date de la nomination | À renseigner | À renseigner |
| Motif écrit lié aux points vérifiés | À renseigner | À renseigner |
| Portée exacte confiée | À renseigner | À renseigner |
| Treize points de la grille vérifiés | À renseigner, aucune case cochée à l'avance | À renseigner, aucune case cochée à l'avance |
| Sources publiques vérifiées et dates | À renseigner | À renseigner |
| Conflits d'intérêts déclarés par écrit | À renseigner | À renseigner |
| Facturation annoncée par écrit avant acceptation | À renseigner, aucun montant prérempli | À renseigner, aucun montant prérempli |
| Disponibilité confirmée avant le premier commit de code de stack | À renseigner | À renseigner |
| Coordinateurs de la signature et des clés | À renseigner | À renseigner |
| Propriétaire de la nomination | Espoir LOEMBA, intérimaire | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner | À renseigner |
| Historique de la nomination | À renseigner | À renseigner |
| État | En attente de nomination | En attente de nomination |

Une ligne sans date ni motif n'est pas une nomination. Chaque nomination est conservée avec les preuves de vérification et inscrite au registre avec date, motif, propriétaire, source liée, portée et historique. Une ligne sans approbateur nommé n'autorise ni engagement ni premier commit de code de stack.

## 3. Ce que la nomination ne fait pas

Nommer un prestataire ne produit pas la preuve de signature, de retour arrière et de non interruption de session attendue au premier rendu signé des trois clients selon D-024. Elle ne remplace pas un avis juridique, ne choisit pas d'hébergeur ni de région de stockage, n'autorise aucune première migration tant que A-12 reste ouverte, ne choisit pas le fournisseur CDN et ne fixe aucune date de lancement selon A-05.

## 4. Ce que ce modèle ne fait pas

Il ne propose aucun nom, n'envoie aucun message, ne vérifie aucune capacité, n'engage aucune dépense, ne lève pas A-04, ne lève pas A-12, ne lève aucune porte et ne contient aucun code applicatif.
