# Avenant règles de code et outillage du dépôt

**Date.** 25 novembre 2026.
**Demande du porteur.** Ajouter une limite de dix lignes par logique, interdire la logique dans les TSX, limiter les appels à `.map()`, maximiser la réutilisation, interdire les commentaires sauf documentation, écrire le code en anglais, mettre en place la configuration de test et de formatage, le précommit et le préfixe `Pro[<name>]` pour les bots GitHub.
**Périmètre.** Règles documentaires, configuration d'outillage et contrôles locaux. Aucun code applicatif n'est écrit. La phase 0 et les portes du premier sprint restent ouvertes.

## Règles ajoutées

| Règle | Formulation retenue | Application |
|---|---|---|
| Taille des fonctions | Dix lignes de logique effective maximum, hors lignes vides, signatures et accolades seules | ESLint `max-lines-per-function` et Clippy `too-many-lines-threshold` |
| Logique dans les TSX | Interdite. Le composant ne fait que du rendu, la logique va dans un hook ou un module TypeScript dédié | Revue et `scripts/check_code_style.py` pour les commentaires et les appels à `.map()` |
| Appels à `.map()` | Un seul par fichier TSX, jamais imbriqué | `scripts/check_code_style.py`, blocage dès le deuxième appel |
| Réutilisation | Aucune duplication de logique, de fonction, de classe ou de fichier. Code partagé dans `packages/domain` | Revue obligatoire |
| Commentaires | Aucun commentaire sauf `/** ... */` en TypeScript et `///` ou `//!` en Rust | `scripts/check_code_style.py` et ESLint `no-inline-comments` |
| Langue du code | Identifiants, messages, chaînes techniques et noms de fichiers de code en anglais | Revue obligatoire |
| Documentation | Documentation produit et rapports en français | Règle existante confirmée |
| Bots GitHub | Tout automatisme contrôlé porte `Pro[CI]`, `Pro[Info]` ou `Pro[Release]` | Workflow, hooks et règles de release |

Les bots natifs de GitHub ne sont pas renommables. Leur activation éventuelle fera l'objet d'un avenant séparé.

## Configuration posée

| Fichier | Rôle |
|---|---|
| `package.json` et `package-lock.json` | Dépendances npm épinglées, scripts de contrôle, Node 26.13.0 validé |
| `tsconfig.json` | TypeScript strict, sans émission, cible ES2023 |
| `vitest.config.ts` | Tests sans échec tant qu'aucun test applicatif n'existe |
| `eslint.config.mjs` | Configuration plate, limite de dix lignes et commentaires en ligne interdits |
| `.prettierrc.json` et `.prettierignore` | Formatage TS et configuration, Markdown exclu |
| `pyproject.toml` | Ruff, ligne à cent caractères, Python 3.13 |
| `rustfmt.toml`, `clippy.toml`, `rust-toolchain.toml` | Rust 1.100.0, largeur cent, limite Clippy à dix lignes |
| `.pre-commit-config.yaml` | Hooks épinglés, noms préfixés `Pro[Info]`, contrôles documentaire et de style |
| `.github/workflows/documentation.yml` | Contrôle GitHub préfixé `Pro[CI]`, contrôles Python et npm |

Le workflow installe les dépendances avec `npm ci`, configure l'identité `Pro[CI]`, rejoue vingt-deux tests Python puis la chaîne `npm run check`. Les protections de `main` et `staging` exigent désormais le contrôle `Pro[CI]: documentation`.

## Contrôles

| Contrôle | Résultat |
|---|---|
| Tests Python | 22 tests, tous verts |
| `npm run check` | Formatage, lint, typecheck, tests Vitest, contrôle documentaire et contrôle de style, tous verts |
| Audit npm | Zéro vulnérabilité signalée |
| `pre-commit validate-config` | Conforme |
| `pre-commit run --all-files` | Tous les hooks verts après correction des sauts de ligne Markdown et du fichier sans ligne finale |
| Schéma YAML du workflow | Conforme |
| Configuration des protections | Contrôle `Pro[CI]: documentation` requis sur `main` et `staging` |
| Code applicatif | Aucun fichier créé |

Le premier passage des hooks a supprimé des sauts de ligne Markdown intentionnels. Le hook `trailing-whitespace` reçoit désormais l'argument `--markdown-linebreak-ext=md`, conformément à `.editorconfig`. Un fichier possédait une ligne vide supplémentaire en fin de document, corrigée et conservée.

## Limites conservées

La limite de dix lignes est appliquée par les linters pour TypeScript et Rust. La règle sur les TSX est vérifiée localement par un script déterministe, avec un seuil par fichier plus strict que le seuil par composant. Le contrôle des commentaires repose sur un analyseur simple qui ignore les chaînes de caractères.

La DI et le déploiement continu restent absents faute de code applicatif. Les titulaires, les cibles desktop et le niveau ASVS restent à nommer ou à arbitrer.

## Conclusion

Les règles demandées sont inscrites dans `../AGENT.md` et relayées par les outils locaux et la CI. Le dépôt dispose désormais d'une configuration de test, de formatage, de lint et de précommit rejouable sans contexte humain. Cohérence confirmée, Error 0, warning 0.
