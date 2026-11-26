# Technique : architecture, décisions et contrôles

**Métier.** Ingénierie `mobile`, `web`, `desktop`, backend et données.
**Statut.** Socle rédigé le 25 novembre 2026, A-03 et A-13 arbitrés le 26 novembre 2026. La stack est retenue en D-009 et détaillée dans `adr-001-stack.md`.
**Règle.** Le PRD ne choisit pas la stack. `adr-001-stack.md` couvre les trois clients livrés ensemble, `mobile`, `web` et `desktop`, et le backend. L'hébergeur et la région de stockage restent liés à A-12. Le fournisseur vidéo reste lié au budget D-022, inscrit le 26 novembre 2026.
**Modèle ADR unique.** Titre, Statut, Contexte, Options, Décision, Conséquences, Propriétaire, Date. Statuts admis : retenue, proposée, à trancher.
**Accessibilité.** WCAG 2.2 niveau AA visé. Cibles de 24 sur 24 pixels CSS au minimum AA, objectif de 44 pixels au-delà du minimum. Contraste AA vérifié : 4,5:1 pour le texte courant, 3:1 pour les grands textes et les composants. Sources : [SC 1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum) et [SC 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

## Dépendances des ADR et des fiches

```mermaid
flowchart LR
  P["PRD et parcours UX"] --> J["Conformite/perimetre-juridique.md"]
  J --> A1["adr-001-stack.md"]
  A1 --> PF["performance.md"]
  PF --> A2["adr-002-identite-session.md"]
  A2 --> M["menaces.md"]
  M --> AR["architecture.md"]
  AR --> V["video.md"]
  AR --> AP["api.md"]
  AR --> D["donnees.md"]
  M --> S["securite.md"]
  A2 --> O["observation.md"]
  AR --> R["responsabilites.md"]
```

Le client desktop est couvert par `adr-001-stack.md` pour les axes de stack, par `performance.md` pour le profil R2, par `architecture.md` pour le conteneur `client_desktop` et par `responsabilites.md` pour la revue de performance. Ces dépendances ne créent aucun ADR numéroté supplémentaire : `adr-001-stack.md` suffit pour les trois clients.

La mise à jour automatique est une contrainte transversale de D-024, décrite dans la section 10.1 du [PRD](../Product/prd.md) et contrôlée dans `securite.md`. Elle ne crée pas d'ADR numéroté supplémentaire. La part du `mobile` modifiable hors binaire natif est la liste fermée de six catégories arbitrée le 26 novembre 2026 au point A-13 de `../Product/arbitrage.md`, sans téléchargement de code exécutable.

| Fiche | Question traitée | Déclencheur | Dépendances | Propriétaire | Statut |
|---|---|---|---|---|---|
| [adr-001-stack.md](adr-001-stack.md) | Stack retenue `mobile`, `web`, `desktop` et backend, D-009 | Arbitrage A-01 atteint le 25 novembre 2026 | Décision D-009, note `../../memoires/2026-11-25-stack-typescript.md` | Espoir LOEMBA, intérimaire | retenue |
| [performance.md](performance.md) | Budgets de latence, bande passante, profil R1 proposé et profil R2 desktop arbitré | Avant `architecture.md` et `video.md` | PRD section 10, A-03 | Espoir LOEMBA, intérimaire | R2 arbitré le 26 novembre 2026, R1 proposé |
| [adr-002-identite-session.md](adr-002-identite-session.md) | Jeton visiteur court, clé par finalité, rotation, liaison à `signup_verified` | Avant FS-01 et la première migration | `performance.md`, `../Product/mesure.md` | Espoir LOEMBA, intérimaire | retenue sur les principes |
| [menaces.md](menaces.md) | Quatre questions OWASP et six menaces priorisées | Avant `securite.md` et `architecture.md` | `adr-002-identite-session.md` | Espoir LOEMBA, intérimaire | proposée |
| [architecture.md](architecture.md) | C4 conteneur, lecture séparée de l'écriture, invalidation de cache | Après `adr-001`, avant `video.md` et `api.md` | `menaces.md`, `performance.md` | Espoir LOEMBA, intérimaire | proposée |
| [video.md](video.md) | Octets, bitrates, coût pour 1 000 vues, EXIF | Avant FS-02 | `architecture.md`, D-022 retenue | Espoir LOEMBA, intérimaire | proposée, budget inscrit |
| [api.md](api.md) | Endpoints, réponses sans données privées, limites | Avant FS-04 et FS-08 | `architecture.md`, `adr-002-identite-session.md` | Espoir LOEMBA, intérimaire | proposée |
| [donnees.md](donnees.md) | Tables, états, transitions et traduction de la conservation | Avant la première migration | `../Conformite/conservation.md`, `adr-002-identite-session.md` | Espoir LOEMBA, intérimaire | proposée |
| [securite.md](securite.md) | Socle de contrôles, jetons, journal d'audit, outils épinglés et ASVS 2 | Avant FS-01 et FS-02, revue avant FS-07 et FS-09 | `menaces.md`, `adr-002-identite-session.md` | Espoir LOEMBA, intérimaire | opposée le 26 novembre 2026 |
| [observation.md](observation.md) | Événements canoniques, schéma, tableau de bord et alertes | Avant l'implémentation de FS-11 | `../Product/mesure.md`, `adr-002-identite-session.md` | Espoir LOEMBA, intérimaire | proposée |
| [responsabilites.md](responsabilites.md) | RACI des ADR, confidentialité, escalade, signature et budget | Avant la revue de sortie MVP | Toutes les fiches ci-dessus, A-03 et A-13 | Espoir LOEMBA, intérimaire | proposée, titulaires A-03 et A-13 nommés le 26 novembre 2026 |

## Liens de cadrage

[PRD](../Product/prd.md), [dictionnaire de mesures](../Product/mesure.md), [registre des décisions](../Product/decisions.md), [parcours UX](../UX/userflow.md), [Opérations](../Operations/README.md).

## Première action

Le propriétaire de `adr-001-stack.md` est Espoir LOEMBA, intérimaire. Il reste à obtenir la validation juridique A-12. Le budget D-022 est inscrit depuis le 26 novembre 2026. Les familles de technologie sont retenues en D-009. Tant qu'A-12 n'est pas écrit, aucun hébergeur ni région de stockage n'est arrêté. Le périmètre mobile hors binaire natif est arrêté depuis le 26 novembre 2026 par A-13, et aucun code n'est écrit avant la levée des portes du sprint 1. Le fournisseur CDN reste à choisir dans le cadre de D-022.
