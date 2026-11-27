# Trame de décision du fournisseur vidéo et du CDN, D-022

**Statut** : préparée le 27 novembre 2026, aucun fournisseur désigné, aucun tarif relevé, D-022 inchangée, aucune porte levée  
**Sources canoniques** : [D-022 dans le registre](../../docs/Product/decisions.md), [Arbitrage A-02](../../docs/Product/arbitrage.md), [Fiche vidéo](../../docs/Technique/video.md), [ADR de stack](../../docs/Technique/adr-001-stack.md), [Montée en charge](../../docs/Operations/montee-en-charge.md), [PRD, services extérieurs](../../docs/Product/prd.md)  
**Règle** : cette trame prépare une décision future. Elle ne recommande aucun acteur, n'ajoute aucun montant, ne modifie pas D-022, ne choisit ni hébergeur ni région de stockage et ne lève aucune porte.

## 1. Ce qui est déjà arrêté

D-022 fixe une enveloppe mensuelle de 1 000 USD pour le CDN et la modération, répartie en 500 USD pour Brazzaville et 500 USD pour Kinshasa, sur le mois civil. Le seuil est de 0,001 USD par vue, lu séparément par ville. La décision est révisée après 30 jours d'exploitation. Le fournisseur CDN n'est pas choisi par cette décision. Aucun montant n'est présenté comme mesuré.

L'ADR de stack retient le stockage objet compatible S3 et le CDN derrière une interface. Les familles de technologie sont arrêtées en D-009 et cette trame ne les rouvre pas. Le PRD annonce quatre services extérieurs : stockage d'objets, CDN avec transcoding adaptatif, notifications push et envoi d'emails de vérification. Le budget D-022 conditionne ces choix sans les faire à leur place. Les bitrates de la fiche vidéo sont des propositions à confirmer, pas un engagement de qualité. Le périmètre juridique A-12 reste ouvert pour l'hébergeur et la région de stockage.

## 2. Champs à remplir au moment du choix

| Champ | Valeur |
|---|---|
| Identifiant de la décision au registre | À renseigner |
| Date de la décision | À renseigner |
| Fournisseur du stockage objet compatible S3 | À renseigner, aucun nom prérempli |
| Fournisseur du CDN avec transcoding adaptatif | À renseigner, aucun nom prérempli |
| Preuve que l'interface interchangeable est respectée | À renseigner |
| Tarif convenu par Go et part du transcoding et du stockage | À renseigner, aucun tarif prérempli |
| Coût calculé pour 1 000 vues | À renseigner, aucune valeur mesurée avancée |
| Lecture du seuil de 0,001 USD par vue, séparément par ville | À renseigner, sans confusion Brazzaville et Kinshasa |
| Enveloppe mensuelle et répartition par ville | 1 000 USD, 500 USD par ville, D-022 inchangée |
| Hébergeur et région de stockage | À renseigner après la levée écrite de A-12, aucun lieu prérempli |
| Service de notifications push | À renseigner, choix distinct |
| Service d'envoi d'emails de vérification | À renseigner, choix distinct |
| Motif écrit lié au seuil et à l'enveloppe | À renseigner |
| Propriétaire de la décision | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner |
| Portée exacte de la décision | À renseigner |
| Date de la révision après 30 jours d'exploitation | À renseigner, pas une date de lancement |
| Archive de la décision et historique | À renseigner |
| État | En attente de décision |

Une ligne sans tarif convenu ni preuve d'interface n'autorise aucun engagement de dépense. Le seuil de 0,001 USD par vue et l'enveloppe de 1 000 USD par mois ne sont pas réécrits pour faire passer un fournisseur. Le [modèle de révision après 30 jours d'exploitation](../Planning/revision-D022-apres-30-jours.md) prépare la décision séparée qui suivra, sans date ni résultat préremplis.

## 3. Distinctions à conserver

Le fournisseur du CDN et du stockage objet n'est pas l'hébergeur au sens de A-12. Son choix ne lève pas A-12 et n'autorise ni région de stockage ni première migration. La région reste à écrire dans la trame dédiée, après réception et confrontation des deux avis locaux. Le service vidéo, le service push et le service d'emails restent des choix distincts, même si le budget D-022 les cadre tous.

Aucune valeur relevée chez un fournisseur n'est présentée comme un coût mesuré de Pro. Aucune prévision de trafic n'est transformée en résultat. Les deux villes restent séparées dans la lecture du seuil. La révision après 30 jours d'exploitation n'est pas une date de lancement selon A-05. Le fournisseur n'est pas choisi dans la fiche vidéo ni dans la montée en charge.

## 4. Ce que cette trame ne fait pas

Elle ne désigne aucun fournisseur, ne demande aucun devis, n'engage aucune dépense, ne relève aucun tarif, ne modifie pas D-022, ne rouvre pas D-009, ne choisit ni hébergeur ni région de stockage, ne lève pas A-12, ne fixe pas de date de lancement et ne contient aucun code applicatif.
