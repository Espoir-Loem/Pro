# Avenant préparation du dépôt Git

**Date.** 25 novembre 2026.
**Demande du porteur.** « prepar le depot ».
**Périmètre.** Dépôt local uniquement. Aucun dépôt distant n'est créé, aucune origine n'est associée, aucun code applicatif n'est écrit. Le porteur a confirmé l'usage de l'email Git global déjà configuré et le choix d'un dépôt local sans GitHub pour l'instant.

## Identité de commit

| Champ | Valeur |
|---|---|
| Nom | Espoir LOEMBA |
| Email | hopcy.forcy@gmail.com |
| Source | Configuration Git globale confirmée par le porteur |
| Login GitHub | @Espoir-Loem |

Aucun co-auteur de modèle n'est ajouté. Aucun trailer `Co-authored-by` n'est écrit dans les commits.

## Branches

- `main` : branche de référence, état initial du cadrage.
- `staging` : branche de préparation à la release, créée depuis `main`.
- `develop` : branche active d'intégration, créée depuis `main`. Tout travail futur part de `develop` avec `feature/*`, `bugfix/*` ou `refactor/*`.

Aucune protection de branche n'est posée, car aucun dépôt distant n'existe. Les règles de pull request, de Conventional Commits, de tags annotés et de releases générées par CI sont écrites dans `../AGENT.md`.

## Fichiers de configuration ajoutés

| Fichier | Rôle |
|---|---|
| `.gitignore` | Exclure dépendances, builds, couverture, secrets, journaux et fichiers locaux |
| `.gitattributes` | Forcer les fins de ligne LF et marquer les binaires |
| `.editorconfig` | UTF-8, LF, indentation deux espaces, préservation des espaces en fin de ligne Markdown |

## Commits initiaux

| Hash | Message | Contenu |
|---|---|---|
| `9bf19a1` | `chore: initialize repository hygiene` | Trois fichiers de configuration du dépôt |
| `382f6ab` | `docs: add product framing and agent guidance` | Cadrage produit, documentation, mémoires, rapports et notes de recherche, soit soixante-seize fichiers |
| `eb78d94` | `docs: record git repository preparation` | Présent avenant et pointeur dans `docs/README.md` |
| `45ee8ee` | `docs: remove phantom decision identifier` | Exemple `D-025` remplacé dans `docs/Product/arbitrage.md` par un renvoi au numéro attribué |
| Commit courant | `docs: record final repository verification` | Résultats détaillés des contrôles dans le présent avenant |

Chaque commit porte un changement logique. Aucun contenu de modèle n'est co-signé.

## Contrôles

| Contrôle | Périmètre | Attendu | Résultat |
|---|---|---|---|
| Initialisation | Dépôt local | Git présent | Conforme |
| Branches | Dépôt local | `main`, `staging` et `develop` présentes | Conforme |
| Branche active | Dépôt local | `develop` | Conforme |
| Origine distante | Dépôt local | Aucune origine | Conforme |
| Identité locale | Dépôt local | Espoir LOEMBA, hopcy.forcy@gmail.com | Conforme |
| Co-auteur de modèle | Messages des commits | Aucun trailer | Conforme |
| Typographie interdite | Quatre-vingts fichiers textuels | Aucune occurrence | Zéro occurrence, conforme |
| Caractères chinois, japonais ou coréens | Quatre-vingts fichiers textuels | Aucune occurrence | Zéro occurrence, conforme |
| Marqueurs de correction en attente | Quatre-vingts fichiers textuels | Aucune occurrence | Zéro occurrence, conforme |
| Liens relatifs | Soixante-neuf fichiers Markdown canoniques | Zéro lien cassé | 486 liens résolus, zéro cassé |
| Numérotation FS | Documentation canonique | FS-01 à FS-11 sans saut | 11 identifiants, conforme |
| Numérotation US | Documentation canonique | US-01 à US-17 sans saut | 17 identifiants, conforme |
| Numérotation D | Documentation canonique | D-001 à D-024 sans saut | 24 identifiants, conforme |
| Numérotation A | Documentation canonique | A-01 à A-13 sans saut | 13 identifiants, conforme |
| Blocs Mermaid | Fichiers Markdown canoniques | Aucun bloc ouvert | Zéro bloc ouvert, conforme |
| Fichiers de `docs/` | Dossier canonique | 59 fichiers | 59, conforme |
| Code applicatif | Arborescence | Aucun fichier de code | Conforme |
| Arbre de travail | Dépôt local | Propre après le dernier commit | Conforme |

Le contrôle des liens porte sur la racine, `docs/` et `reports/`, hors blocs de code et hors code en ligne. Les notes de recherche historiques sont exclues : elles contiennent des liens absolus de type `file:` vers la machine d'origine et un renvoi vers un fichier de compétence local, sans incidence sur la documentation livrée.

## Portes conservées

Phase 0, A-02 et D-022, A-03, A-04, A-05, A-06 à A-13, D-010 et D-011 restent ouverts. Les titulaires distincts du chef de projet restent à nommer. Aucun code n'est écrit avant la levée des portes du premier sprint décrites dans `../AGENT.md`.

## Conclusion

Le dépôt local est prêt, avec une identité humaine vérifiée, trois branches et une configuration de base sobre. La création du dépôt distant, la poussée des branches, la protection de `main` et `staging` et la mise en place de la CI se feront après décision du porteur, sans précipiter l'écriture de code. Cohérence confirmée, Error 0, warning 0.
