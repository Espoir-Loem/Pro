# Avenant stack et fichiers d'agent

**Date.** 25 novembre 2026.
**Demande du porteur.** Utiliser uniquement des modules LTS et sans CVE, écrire tout code en TDD avec SOLID et KISS, faire des recherches de bonnes pratiques et lire la documentation ainsi que le code source d'une librairie avant de corriger un bug, créer `memoires/` pour garder les pistes de raisonnement, structurer `apps/mobile`, `apps/web`, `apps/desktop` et `packages/api` avec la rigueur d'une grande équipe, automatiser toute vérification déterministe par script et CI, garder un design pro et humain sans couleurs ni polices qui font IA, adopter un GitHub flow pro avec `main`, `staging` et `develop`, committer chaque changement logique, interdire tout co-auteur de modèle.
**Périmètre.** `docs/`, la racine du dépôt et `memoires/`. Les rapports historiques ne sont pas réécrits ; deux d'entre eux reçoivent seulement une note de lecture datée. Aucun code applicatif n'est écrit. Aucun commit n'est effectué.

## Décision inscrite

D-009 est passée de « question ouverte » à « décision retenue » dans `docs/Product/decisions.md`, avec date, motif, propriétaire, source liée, portée et historique. La stack retenue est tout TypeScript : React et TypeScript sur `web`, React et TypeScript dans Tauri avec coque Rust minimale sur `desktop`, React Native via Expo managé sur `mobile`, NestJS avec Postgres et Prisma sur `packages/api`. Rust reste la seule exception, limitée à la coque signée.

Node 26 LTS est la base de compilation. Node 27 est alpha et interdit. Expo SDK 58 et React Native 0.88 sont retenus, avec minimum Node 22.13.x. Les versions `latest`, `canary`, `beta`, `rc` et alpha sont interdites. Le seuil de sécurité est zéro CVE connue et non traitée au merge et à la release, avec SBOM CycloneDX signé, scans SCA, SAST, secrets, licences et exceptions VEX bornées.

Le point A-01 de `docs/Product/arbitrage.md` est clôturé et renvoie à D-009. L'échéance du point A-12 est ajustée : la qualification juridique conditionne désormais l'hébergeur, la région de stockage et la première migration, pas le choix des familles de technologie. A-13 reste ouvert et livre avant le sprint 1 la liste fermée de ce qui est modifiable hors binaire natif sur `mobile`.

## Fichiers créés

| Fichier | Rôle |
|---|---|
| `AGENT.md` | Source canonique unique : périmètre, sources de vérité, décisions, portes avant code, stack, invariants, règles TDD et SOLID, sécurité, Git flow, tests, design, automatisation |
| `CLAUDE.md` | Court renvoi vers `AGENT.md`, sans duplication de règle |
| `memoires/README.md` | Rôle du dossier, nommage, structure minimale et notes présentes |
| `memoires/modele-de-note.md` | Modèle de note datée avec question, sources, options, conclusion, conséquence et lien |
| `memoires/2026-11-25-stack-typescript.md` | Pistes de raisonnement et sources derrière D-009 |
| `reports/avenant-agent-et-stack.md` | Present rapport |

## Fichiers modifiés

| Fichier | Modification |
|---|---|
| `docs/Product/decisions.md` | D-009 inscrite avec historique, conséquences écrites, questions ouvertes réduites à trois, registre en version 4 |
| `docs/Product/arbitrage.md` | A-01 clôturé, A-12 réaligné, listes de décisions mises à jour, grille en version 3 |
| `docs/Product/prd.md` | Stack présentée comme retenue, risque et questions ouvertes mis à jour, PRD en version 4 |
| `docs/Product/roadmap.md` | Dépendance de Phase 1 alignée sur D-009 et l'ADR 001 |
| `docs/UX/ux-research.md` et `docs/UX/userstories.md` | D-009 retirée des questions ouvertes sans être transformée en histoire |
| `docs/Technique/adr-001-stack.md` | Statut retenu, options évaluées, décision détaillée, conséquences et propriétaire à nommer |
| `docs/Technique/README.md` | Stack retenue, dépendances A-12 et D-022 conservées, première action réécrite |
| `docs/Technique/responsabilites.md` | Statut de l'ADR 001 aligné sur D-009 |
| `docs/Technique/architecture.md` | Conteneurs C4 nommés avec les technologies retenues |
| `docs/Technique/api.md` et `docs/Technique/video.md` | Références à l'ADR ouvertes remplacées par les choix retenus et les portes restées ouvertes |
| `docs/Conformite/perimetre-juridique.md` et `docs/Conformite/README.md` | Stack retenue distinguée de l'hébergeur et de la région de stockage toujours ouverts |
| `docs/README.md` | Rôle de `Technique/` mis à jour, pointeur vers le présent avenant, index en version 5 |
| `reports/avenant-mises-a-jour.md` et `reports/verification-coherence.md` | Note de lecture indiquant qu'ils sont des snapshots antérieurs à D-009 |

Aucun fichier de `docs/` n'a été ajouté ni supprimé. Le dossier contient toujours cinquante-neuf fichiers.

## Contrôles

| Contrôle | Attendu | Résultat |
|---|---|---|
| Recherche des tirets interdits dans `docs`, `memoires`, `AGENT.md`, `CLAUDE.md` et les deux rapports mis à jour | Aucune occurrence | Vide, conforme |
| Recherche des caractères chinois, japonais ou coréens dans le même périmètre | Aucune occurrence | Vide, conforme |
| Recherche des marqueurs de correction en attente dans le même périmètre | Aucune occurrence | Vide, conforme |
| Résolution des liens relatifs | Zéro lien cassé | 453 liens résolus, 0 cassé sur 67 fichiers contrôlés |
| Numérotation FS, US, D et A | FS-01 à FS-11, US-01 à US-17, D-001 à D-024, A-01 à A-13 sans saut | Conforme |
| Blocs Mermaid | Tous fermés | Conforme |
| Fichiers dans `docs/` | Cinquante-neuf fichiers | 59, conforme |
| Décisions retenues | D-001 à D-009, D-012 à D-021, D-023 et D-024 | Conforme |
| Questions ouvertes | D-010, D-011 et D-022 | Conforme |
| Point A-01 | Clôturé avec renvoi vers D-009 | Conforme |
| Aucune règle de store inventée | A-13 reste à arbitrer avec preuve écrite | Conforme |
| Aucun identifiant d'appareil, d'installation ou de machine | D-012 et D-024 intactes | Conforme |
| Aucun co-auteur de modèle | Interdiction écrite dans `AGENT.md`, `CLAUDE.md` et le présent rapport | Conforme |
| Aucun code applicatif | Aucun fichier de code créé | Conforme |

## Sources consultées

Les sources sont archivées dans `memoires/2026-11-25-stack-typescript.md`. Les principales sont le calendrier officiel de Node.js, le changelog Expo SDK 58, les statuts de versions Expo, les cheat sheets OWASP sur la chaîne d'approvisionnement et les SBOM, NIST SP 800-204D, les éléments minimaux SBOM 2026, la spécification Conventional Commits et la documentation Git et GitHub sur les tags annotés et les releases.

## Portes restées ouvertes

Phase 0, A-02 et D-022, A-03, A-04, A-05, A-06 à A-13 selon leur échéance, ainsi que D-010 et D-011. Le propriétaire technique de la stack et les titulaires des revues restent à nommer. Aucun code n'est écrit avant la levée des portes du premier sprint décrites dans `AGENT.md`.

## Conclusion

La stack est maintenant opposable en D-009. Les deux fichiers d'agent sont en place, avec une seule source de vérité. Les pistes de raisonnement sont datées dans `memoires/`. Les contrôles mécaniques et sémantiques sont verts. Cohérence confirmée, Error 0, warning 0.
