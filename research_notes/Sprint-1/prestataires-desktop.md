# Nommer les prestataires du client desktop, grille de vérification

**Statut** : préparée le 26 novembre 2026, aucun prestataire désigné, aucune décision  
**Sources** : [A-04 dans la grille d'arbitrage](../../docs/Product/arbitrage.md), [D-023 et D-024 dans le registre](../../docs/Product/decisions.md), [Roadmap, Phase 1](../../docs/Product/roadmap.md), [Dossier sprint 1](./README.md)  
**Règle** : cette grille prépare la vérification. Elle ne désigne personne, ne choisit aucun prestataire, ne fixe aucun montant et ne lève aucune porte.

Le client `desktop` est un exécutable installé sur Windows et sur macOS, livré en même temps que `mobile` et `web` selon D-023 et D-004. Le point A-04 impose que ses prestataires soient nommés par écrit avant le premier commit de code de stack. Deux vérifications distinctes sont nécessaires, une pour Windows et une pour macOS, afin que les capacités de l'un ne soient pas prêtées à l'autre. La coque Rust du desktop ne porte que la signature, l'installateur et la mise à jour, selon D-009. Le fournisseur CDN reste une question séparée, dans le cadre de D-022.

## 1. points à vérifier avant nomination

Toutes les valeurs sont à renseigner au moment de la vérification. Aucune n'est présumée ici.

| Point vérifié | Windows | macOS | État |
|---|---|---|---|
| Identité légale, adresse et coordonnées confirmées sur une source récente | À renseigner | À renseigner | À vérifier |
| Expérience vérifiable de l'installateur et de la mise à jour sur le système visé | À renseigner | À renseigner | À vérifier |
| Capacité de signature de code avec certificat adapté au système visé | À renseigner | À renseigner | À vérifier |
| Gestion des clés de signature par le titulaire du projet, sans délégation tacite | À renseigner | À renseigner | À vérifier |
| Procédure de distribution écrite et conforme aux règles en vigueur pour le système visé | À renseigner | À renseigner | À vérifier |
| Notarisation et distribution hors store, pour macOS seulement | Sans objet | À renseigner | À vérifier |
| Procédure de retour arrière écrite et rejouable | À renseigner | À renseigner | À vérifier |
| Capacité à montrer la non interruption de session pendant une mise à jour | À renseigner | À renseigner | À vérifier |
| Capacité à tenir la machine de référence A-03, 2 cœurs, 4 Go de RAM et SSD, et la méthode de 30 lancements à froid avec p75 et traces jointes | À renseigner | À renseigner | À vérifier |
| Disponibilité avant le premier commit de code de stack | À renseigner | À renseigner | À vérifier |
| Déclaration écrite de conflits d'intérêts | À demander | À demander | À vérifier |
| Modalités de facturation annoncées par écrit avant acceptation | À demander | À demander | À vérifier |
| Limite de portée confirmée : aucune règle modifiée par téléchargement de code exécutable sur `mobile` selon A-13 et D-024 | À confirmer | À confirmer | À vérifier |

Aucune piste publique, aucun nom et aucun résultat de vérification ne sont inscrits dans ce tableau. Le titulaire intérimaire du projet est Espoir LOEMBA depuis le 25 novembre 2026 au titre de A-04, et aucun autre titulaire n'est ajouté ici.

## 2. écriture de la nomination

Au moment où les deux prestataires sont retenus, une nomination distincte est écrite pour chacun avec les champs suivants. Aucun de ces champs n'est rempli par avance.

| Champ | Windows | macOS |
|---|---|---|
| Nom du prestataire retenu | À renseigner | À renseigner |
| Date de la nomination | À renseigner | À renseigner |
| Motif écrit, lié aux vérifications de la section 1 | À renseigner | À renseigner |
| Portée exacte confiée | À renseigner | À renseigner |
| Propriétaire de la nomination | Espoir LOEMBA, intérimaire | Espoir LOEMBA, intérimaire |
| Sources vérifiées et dates | À renseigner | À renseigner |
| Historique de la nomination | À renseigner | À renseigner |

La nomination est datée et conservée avec les preuves de vérification. Elle ne remplace pas un avis juridique et n'autorise ni hébergeur, ni région de stockage, ni première migration tant que A-12 reste ouverte.

## 3. preuve attendue après la nomination

La preuve de signature, de retour arrière et de non interruption de session est attendue au premier rendu signé des trois clients, selon D-024 et la porte 6 du dossier sprint 1. Cette grille ne la produit pas. Aucune valeur de performance n'est présentée comme mesurée avant la revue prévue le 26 décembre 2026 au titre de A-03.

## 4. ce que cette grille ne fait pas

Elle ne désigne aucun prestataire, ne choisit pas de stratégie de distribution au-delà de ce qui est déjà écrit, ne recommande ni hébergeur ni région de stockage, ne lève aucune porte, ne remplace pas les deux avis juridiques externes attendus au titre de A-12 et ne contient aucun code applicatif.
