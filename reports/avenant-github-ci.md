# Avenant GitHub et intégration continue

**Date.** 25 novembre 2026.
**Demande du porteur.** « est-ce que tout prêt et configuer avec la CI et DI et avec la gh ».
**Périmètre.** Mise en ligne du dépôt, première CI documentaire et protections de branches. Aucun code applicatif n'est écrit. La phase 0 et les portes du premier sprint restent ouvertes.

## Dépôt GitHub

| Élément | Valeur |
|---|---|
| Dépôt | `Espoir-Loem/Pro` |
| URL | https://github.com/Espoir-Loem/Pro |
| Visibilité initiale | Privée, créée sur décision du porteur |
| Visibilité courante | Publique, changement demandé par le porteur pour activer les protections |
| Origine locale | `https://github.com/Espoir-Loem/Pro.git` |
| Branche par défaut | `main` |
| Branches poussées | `main`, `staging`, `develop` |
| Outil utilisé | `gh` version 2.103.3, compte `Espoir-Loem`, protocole HTTPS |

Le dépôt a d'abord été créé en privé. GitHub refuse les protections de branches sur un dépôt privé d'un compte gratuit. Le porteur a choisi le passage en public pour obtenir ces protections. Le contenu du cadrage est donc désormais accessible à tous.

## Protections de branches

Appliquées à `main` et `staging` via l'API GitHub.

| Paramètre | Valeur |
|---|---|
| Contrôle requis | `documentation` |
| Contrôle strict | Actif, la branche doit être à jour avant le merge |
| Pull request obligatoire | Oui |
| Approbations requises | Zéro, aucun second relecteur humain n'est nommé |
| Conversations résolues | Obligatoire |
| Poussée forcée | Interdite |
| Suppression de branche | Interdite |
| Contournement par administrateur | Interdit |

Le nombre d'approbations reste à zéro tant qu'un second humain nommé n'est pas désigné. Il devra être porté à un dès cette nomination. La règle de pull request est également écrite dans `../AGENT.md`.

## Intégration continue

Le workflow `.github/workflows/documentation.yml` est déclenché sur chaque push vers `main`, `staging` et `develop`, sur chaque pull request et à la demande. Le job porte l'identifiant `documentation`, repris par les protections.

| Élément | Choix | Motif |
|---|---|---|
| Runner | `ubuntu-24.04` | Version supportée, aucun mot de cycle instable |
| Python | `3.13` | Version en support actif |
| `actions/checkout` | Épinglé au commit de `v7.0.1` | Reproductibilité et revue du code exécuté |
| `actions/setup-python` | Épinglé au commit de `v7.1.0` | Reproductibilité et revue du code exécuté |
| Permissions | `contents: read` | Minimum nécessaire |

Les actions sont épinglées par empreinte complète, pas par un tag flottant. Aucune valeur `latest`, `canary`, `beta`, `rc` ou alpha n'est utilisée.

## Script déterministe

`scripts/check_docs.py` centralise les contrôles déjà rejoués à la main. `scripts/test_check_docs.py` les couvre par onze tests unitaires. La séquence rouge a été constatée avant l'implémentation, puis les tests sont verts après refactorisation.

| Contrôle | Portée |
|---|---|
| Typographie interdite et caractères CJK | Fichiers textuels de l'arborescence, hors `.git` |
| Marqueurs de correction en attente | Fichiers textuels de l'arborescence, hors `.git` |
| Liens relatifs | Racine, `docs/` et `reports/`, hors blocs de code et code en ligne |
| Numérotation FS, US, D et A | Documentation canonique, sans saut ni identifiant hors périmètre |
| Blocs de code | Tous les délimiteurs doivent être fermés |
| Nombre de fichiers sous `docs/` | Cinquante-neuf fichiers attendus |

Le script est idempotent, sans dépendance externe et exécutable par `python3 scripts/check_docs.py`. Il imprime un relevé chiffré et retourne un code d'erreur en cas d'écart. La CI rejoue aussi les tests du script avant les contrôles.

## Injection de dépendances et déploiement continu

Aucun des deux n'est en place. Il n'existe aucune ligne de code applicatif, donc aucun conteneur d'injection, aucune inversion de contrôle et aucun artefact à déployer. Les règles sont écrites dans `../AGENT.md`, sections 7 et 11.

La mise en place interviendra avec le premier commit applicatif, après la levée des portes du premier sprint. Le déploiement continu sera branché sur les releases générées par CI, avec SBOM signé, artefacts signés et preuve de passe. Aucune cible chiffrée n'est inventée ici.

## Contrôles

| Contrôle | Résultat |
|---|---|
| Tests du script | 11 tests, tous verts |
| Exécution du script | 82 fichiers textuels, 69 fichiers Markdown canoniques, 486 liens vérifiés, zéro échec |
| Présence du workflow | Conforme |
| Empreintes des actions | Conformes, vérifiées par l'API GitHub |
| Protections `main` et `staging` | Conformes, contrôle `documentation` requis |
| Origine et branches | Conformes, trois branches poussées |
| Code applicatif | Aucun fichier créé |

## Conclusion

GitHub et la première CI sont opérationnels. Le dépôt est public, les branches permanentes sont protégées et le contrôle documentaire bloque le merge. La DI et le déploiement continu restent des chantiers du premier code, sans anticiper les décisions encore ouvertes. Cohérence confirmée, Error 0, warning 0.
