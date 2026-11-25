# Avenant suivi GitHub du projet

**Date.** 25 novembre 2026.
**Demande du porteur.** Mieux gérer le projet sur GitHub avec les outils natifs, créer des issues et des tâches, interdire toute pull request sans issue ouverte, interdire la revendication d'issue par commande, suivre les KPI bugs, UX, produit et SEO, ajouter la description du dépôt et respecter un seul fichier par commit.
**Périmètre.** Organisation du dépôt, gabarits, libellés, jalons, issues, sous-tâches, GitHub Project et contrôles associés. Aucun code applicatif n'est écrit. La phase 0 et les portes du premier sprint restent ouvertes.

## 1. État du dépôt

La description posée sur le dépôt public est la suivante : Réseau social professionnel vidéo courte, chat, emplois et pages organisation, pour la République du Congo et la RDC.

Les branches permanentes restent `main`, `staging` et `develop`. La branche de travail utilisée pour cet avenant est `feature/github-project-management`. Les protections de `main` et `staging` exigent déjà une pull request, le contrôle `Pro[CI]: documentation`, l'interdiction de poussée forcée, l'absence d'exemption pour les administrateurs et la résolution des conversations.

## 2. Gabarits et contrôles de saisie

| Fichier | Rôle |
|---|---|
| `README.md` | Présentation publique du dépôt, règle d'issue et commandes de contrôle local |
| `.github/PULL_REQUEST_TEMPLATE.md` | Référence obligatoire `Closes #<numéro>` et liste des contrôles à passer |
| `.github/ISSUE_TEMPLATE/config.yml` | Renvoi vers l'index documentaire avant toute issue de périmètre |
| `.github/ISSUE_TEMPLATE/tache.yml` | Objectif, sous-tâches, KPI associé et définition de terminé |
| `.github/ISSUE_TEMPLATE/bug.yml` | Observation, attendu, KPI associé et reproduction |

Le contrôle `scripts/check_pr_issue.py` lit le corps de la pull request, extrait la référence d'issue, vérifie qu'elle correspond à l'issue attendue et exige l'état ouvert. Il est rejoué par la CI sur chaque pull request avec `GH_TOKEN` et le numéro fourni par l'événement GitHub.

## 3. Libellés et jalons

Trente et un libellés ont été créés ou confirmés. Ils couvrent les types, les priorités, les états, les domaines géographiques et de plateforme, ainsi que les dix identifiants KPI. Les libellés par défaut de GitHub restent disponibles.

Quatre jalons sont ouverts : Phase 0, Portes du sprint 1, Phase 1 MVP et SEO web. Aucune date n'est présentée comme validée : les échéances saisies dans GitHub sont des repositions de travail à confirmer par décision écrite.

## 4. Issues et sous-tâches

Dix issues ont été créées. Aucune n'est assignée, aucune ne porte de commande de revendication et chacune contient des sous-tâches vérifiables.

| Numéro | Titre | Jalon | KPI associé |
|---|---|---|---|
| 3 | Préparer la gestion GitHub du projet et les contrôles de fusion | Portes du sprint 1 | Aucun |
| 4 | Clore la phase 0 et nommer les titulaires | Phase 0 | UX-01, UX-02, UX-03 |
| 5 | Lever A-02 et D-022 sur les cibles desktop et la signature | Portes du sprint 1 | Aucun |
| 6 | Lever A-03 à A-09 sur les versions et la sécurité | Portes du sprint 1 | Aucun |
| 7 | Lever A-10 à A-13 sur la part mobile modifiable | Portes du sprint 1 | Aucun |
| 8 | Trancher D-010 et D-011 | Portes du sprint 1 | Aucun |
| 9 | Valider les hypothèses H1 à H8 avec seuils et validateurs | Phase 0 | UX-01, UX-02, UX-03 |
| 10 | Nommer les cibles et les propriétaires des KPI | Portes du sprint 1 | Les dix KPI |
| 11 | Préparer le premier contrôle du rendu public web | SEO web | SEO-01, SEO-02 |
| 12 | Mettre en place la chaîne de contrôles SCA, SAST, secrets et licences | Portes du sprint 1 | Aucun |

L'issue 3 est celle que la pull request de cet avenant référence. Les issues 4 à 12 ne sont pas fermées et ne portent aucune assignation.

## 5. GitHub Project

Le tableau `Pro - Suivi du projet` est créé sous le compte `Espoir-Loem` et lié au dépôt. Son URL est `https://github.com/users/Espoir-Loem/projects/7`.

Les champs suivants sont en place :

| Champ | Type | Valeurs |
|---|---|---|
| Statut | Sélection unique | À faire, En cours, En revue, Bloqué, Terminé |
| Priorité | Sélection unique | Haute, Moyenne, Basse |
| Domaine | Sélection unique | République du Congo, RDC, Afrique, Monde, Mobile, Web, Desktop, Transverse |
| KPI | Sélection unique | BUG-01 à BUG-03, UX-01 à UX-03, PRD-01, PRD-02, SEO-01, SEO-02, Aucun |

Les dix issues sont ajoutées comme items et leurs quatre champs sont renseignés. L'issue 3 est en cours, les issues 5, 6 et 7 sont bloquées par des décisions à lever, les autres sont à faire. Aucun item n'est marqué terminé.

## 6. KPI

La fiche `docs/Product/kpi.md` définit dix identifiants : BUG-01, BUG-02, BUG-03, UX-01, UX-02, UX-03, PRD-01, PRD-02, SEO-01 et SEO-02. Chaque identifiant possède une formule et une source. Les cibles et les propriétaires restent à nommer et font l'objet de l'issue 10. Aucune cible chiffrée n'est inventée.

La fiche `docs/Technique/seo-web.md` porte la checklist SEO du client web et le PRD reprend cette checklist dans ses exigences non fonctionnelles. Le contrôle `scripts/check_kpi.py` vérifie les sections et les identifiants, puis est rejoué par `npm run check`, par le précommit et par la CI.

## 7. Règle d'un fichier par commit

Chaque commit de la branche `feature/github-project-management` touche un seul fichier. La règle est inscrite dans `AGENT.md` et dans le README racine. Les opérations GitHub sur les libellés, les jalons, les issues et le tableau ne produisent pas de commit dans le dépôt.

## 8. Contrôles

| Contrôle | Résultat |
|---|---|
| Tests Python | 33 tests, tous verts |
| `npm run check` | Formatage, lint, typecheck, Vitest, contrôle documentaire, contrôle KPI et contrôle de style |
| `uvx pre-commit validate-config` | Conforme |
| `uvx pre-commit run --all-files` | Tous les hooks verts |
| Schéma YAML du workflow | Conforme |
| Description du dépôt | Posée et relue via l'API GitHub |
| Libellés | 41 libellés présents, dont 31 créés ou confirmés pour le projet |
| Jalons | Quatre jalons ouverts |
| Issues | Dix issues ouvertes, non assignées, avec sous-tâches |
| GitHub Project | Dix items liés, quatre champs renseignés par item |
| Code applicatif | Aucun fichier créé |

## 9. Limites conservées

Les bots natifs de GitHub ne sont pas renommables. La règle `Pro[<Name>]` ne s'applique qu'aux automatismes contrôlés par le projet. Les titulaires, les cibles KPI, les seuils d'alerte, les dates réelles des jalons et les portes A-02 à A-13, D-010, D-011 et D-022 restent ouverts. Aucune assignation n'est posée tant que le titulaire n'est pas nommé par décision explicite.

## 10. Conclusion

Le dépôt dispose désormais d'un dispositif de gestion complet : description, gabarits, libellés, jalons, issues avec sous-tâches, tableau de bord, KPI et contrôles de fusion opposables. Cohérence confirmée, Error 0, warning 0.
