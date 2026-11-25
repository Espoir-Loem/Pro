# ADR 001 : stack TypeScript retenue

Décision retenue : tout TypeScript pour les interfaces, les règles partagées et le backend. Rust reste limité à la coque desktop signée.

## Titre

Stack `mobile`, `web`, `desktop` et backend pour Pro.

## Statut

retenue, D-009 au registre produit

## Contexte

Le PRD fixe le périmètre MVP et interdit de choisir la stack dans le produit. Le registre des décisions porte désormais D-009, inscrite le 25 novembre 2026 après l'arbitrage A-01. Le porteur demande une rigueur de production, un client desktop léger et rapide sans lenteur perceptible, des mises à jour automatiques selon D-024 et une correction qui n'attende pas un cycle de store pour ce qui est servi hors binaire natif. Le périmètre juridique A-12 et le budget D-022 restent ouverts : ils conditionnent l'hébergeur, la région de stockage et le fournisseur vidéo, pas les familles de technologie ci-dessous. La note `../../memoires/2026-11-25-stack-typescript.md` garde les pistes de raisonnement et les sources, sans dupliquer le registre.

## Options

| Axe | Options examinées | Retenu |
|---|---|---|
| Organisation du code | Clients séparés avec API commune ; base de code partagée sur les trois clients ; hybride avec `mobile` natif | Règles et contrats partagés dans `packages/domain`, clients séparés par cible, API commune |
| Client `web` | Rendu DOM avec React ; rendu canvas | React et TypeScript avec rendu DOM, pour l'accessibilité WCAG 2.2 AA |
| Client `mobile` | Natif Kotlin et Swift ; React Native via Expo managé ; React Native CLI nu ; Flutter | React Native via Expo managé, sous réserve de la liste A-13 |
| Client `desktop` | Electron ; Tauri avec coque Rust minimale | React et TypeScript dans Tauri, coque Rust minimale pour la signature, l'installateur et la mise à jour |
| Backend | Go ; NestJS et TypeScript | NestJS, TypeScript, Postgres et Prisma |
| Données et fichiers | Stockage relationnel et objet séparés ; stockage unique | Postgres pour l'état, stockage objet compatible S3 et CDN derrière une interface |
| Hébergement | Offre gérée avec région contractuelle ; auto-hébergement | À trancher avec A-12 et D-022, sans choix dans cet ADR |

Aucun fournisseur d'hébergement, de CDN ni de transcription n'est nommé ici. Le service de transcription reste derrière une interface et la correction par l'auteur avant publication reste imposée par D-021.

## Décision

La base de compilation est Node 26 LTS. Node 27 est en phase alpha et reste interdit en production. Le minimum retenu est Node 22.13.x pour Expo SDK 58. Aucune dépendance en `latest`, `canary`, `beta`, `rc` ou alpha n'est acceptée. Les lockfiles sont commités.

Le client `web` utilise React et TypeScript avec rendu DOM. Le client `desktop` utilise le même front React dans Tauri, avec une coque Rust minimale pour Windows et macOS, un paquet signé, une vérification avant installation et un retour à la version précédente en cas d'échec. Le client `mobile` utilise React Native via Expo managé, SDK 58 et React Native 0.88 ; la part modifiable hors binaire natif est limitée à la liste fermée du point A-13. Le backend utilise NestJS, TypeScript, Postgres et Prisma, avec chemin de lecture et chemin d'écriture séparés et file asynchrone durable.

Le stockage objet compatible S3 et le CDN sont derrière une interface, avec fournisseur après D-022. Les contrats entre clients et backend sont typés dans `packages/domain`. Aucune mise à jour ne coupe une session en cours, ne crée d'identifiant d'appareil, d'installation ou de machine, et ne modifie une décision de modération sans trace.

Toute dépendance est évaluée avant ajout sur le mainteneur, l'historique de sécurité, la licence, l'OSSF Scorecard et les dépendances transitives. Le seuil opposable est zéro CVE connue et non traitée au merge et à la release. Un SBOM CycloneDX signé est produit à chaque release. Les scans SCA, SAST, secrets et licences passent sur chaque pull request. Une exception est bornée avec propriétaire, contrôle compensatoire, date d'expiration et statut VEX.

Historique : proposée le 25 novembre 2026, retenue le 25 novembre 2026.

## Conséquences

- Le monorepo utilise `packages/domain`, `packages/api`, `apps/web`, `apps/mobile` et `apps/desktop`. Le dossier canonique du client mobile est `apps/mobile`.
- Le développement suit TDD, rouge puis vert puis refactor, avec SOLID et KISS en revue, injection de dépendances et aucune duplication de logique.
- Les tests unitaires, d'intégration, de contrat, de bout en bout et crossplateforme couvrent les trois clients, avec la preuve de signature, de retour arrière et de non interruption de session pour D-024.
- A-12 et D-022 bloquent le choix de l'hébergeur, de la région de stockage, du fournisseur CDN et de la première migration. Ils ne rouvrent pas les familles de technologie retenues ici.
- A-13 livre avant le sprint 1 la liste fermée de ce qui est modifiable hors binaire natif sur `mobile`. Aucune règle de store n'est affirmée sans preuve écrite.
- A-03 confirme ou révise les cibles de taille, de démarrage, de mémoire et de latence du client `desktop` avant le sprint 1.
- Toute reprise de cet ADR conserve le modèle unique, ajoute une ligne d'historique datée et suit la procédure de réouverture de `../Product/decisions.md`.

## Propriétaire

Équipe produit et technique, titulaire à nommer.

## Date

25 novembre 2026
