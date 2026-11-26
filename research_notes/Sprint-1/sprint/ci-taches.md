# Tâches de contrôle du sprint 1

**Statut** : préparées le 26 novembre 2026, aucun nouveau contrôle écrit  
**Source** : [flux de documentation](../../../../.github/workflows/documentation.yml), [AGENT.md](../../../../AGENT.md) section 8 et [sécurité](../../../docs/Technique/securite.md)  
**Règle** : les contrôles existants sont rejoués sur chaque pull request. Cette fiche ne modifie aucune version épinglée et n'ajoute aucun outil.

## Contrôles sur chaque pull request

| Contrôle | Outil ou commande | Version épinglée | Ce qui est vérifié |
|---|---|---|---|
| Documentation et style | `npm run check` | Node 26.13.0, Python 3.13 | Format, lint, typecheck, tests, documentation, KPI, style de code |
| Hooks locaux | `uvx pre-commit run --all-files` | Configuration du dépôt | Espace final, fin de fichier, YAML, JSON, conflits, clés privées, fin de ligne |
| Tests Python | `python3 -m unittest discover` | Python 3.13 | Scripts de contrôle déterministes |
| Couverture KPI | `python3 scripts/check_kpi.py` | Python 3.13 | Identifiants et propriétaires de mesures |
| Référence d'issue | `python3 scripts/check_pr_issue.py` | Python 3.13 | Première référence d'issue ouverte dans le corps de la pull request |
| Secrets | `gitleaks detect` | 8.30.1 | Aucun secret dans le dépôt, avec somme de contrôle vérifiée |
| Dépendances connues | `osv-scanner scan` | 2.7.1 | Zéro CVE connue et non traitée au merge |
| Analyse statique | `semgrep scan` | 1.187.0 | Règles du dépôt, sans métrique externe |
| Licences | `license-checker-rseidelsohn` | 5.0.1 | Liste fermée des licences autorisées sur les dépendances npm de production |
| SBOM | `anchore/sbom-action` | 0.24.4 | CycloneDX JSON à chaque pull request, sans téléversement |

## Contrôles à chaque release

| Contrôle | Outil | Ce qui est vérifié |
|---|---|---|
| Signature du SBOM | `cosign` 3.1.6 installé par `cosign-installer` 4.1.4 | Bundle Sigstore joint au digest |
| VEX | CycloneDX daté | Document daté, signé, relié à l'artefact |
| Notes et preuve de passe | CI | Notes générées et preuve de réussite des contrôles |

## Règles de dépôt à rejouer en revue

Un seul fichier par commit. Tous les temporaires sous `.tmp/`. Aucune version `latest`, `canary`, `beta`, `rc` ou alpha. Aucun co-auteur de modèle, aucun trailer `Co-authored-by`. Aucun commentaire dans le code sauf documentation TypeScript et Rust. Aucune logique dans les fichiers TSX et un seul appel à `.map()` par fichier TSX, jamais imbriqué. Aucune fonction de plus de dix lignes de logique effective. Le code partagé va dans `packages/domain`.

## Ce qui reste à exécuter plus tard

L'issue #11 demande une checklist SEO sur un rendu web réel. Elle ne peut pas être passée avant l'existence d'un rendu. La preuve de signature, de retour arrière et de non interruption de session attend le premier rendu signé des trois clients. La liste fermée de licences ne couvre aujourd'hui que les dépendances npm de production ; elle est à étendre avant tout lockfile Python ou Rust. Aucune mesure de performance n'est présentée comme relevée avant la revue prévue par A-03.

Cette fiche ne crée aucun fichier de configuration et ne déclenche aucun contrôle. Elle sert de liste de vérification pour la revue du premier commit de code, le jour où les portes seront levées.
