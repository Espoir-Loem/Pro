# KPI de suivi du produit

**Version.** 1.
**Date.** 25 novembre 2026.
**Statut.** Définitions ouvertes, cibles et propriétaires à nommer avant le premier tableau de bord.
**Périmètre.** Bugs, UX, produit et SEO web. Aucune cible chiffrée n'est inventée dans cette fiche.

## 1. Principes

Chaque mesure possède un identifiant, un nom, une formule, une source, un propriétaire et une cible. Les identifiants sont stables et ne sont pas réutilisés. Une mesure sans source datée n'est pas publiée. Les mesures produit reprennent les événements canoniques décrits dans [mesure.md](./mesure.md). Les mesures UX s'appuient sur les hypothèses de [ux-research.md](../UX/ux-research.md). Aucun classement payant n'entre dans ces mesures, conformément au registre des décisions.

## 2. Bugs

| Identifiant | Nom | Formule | Source | Propriétaire | Cible |
|---|---|---|---|---|---|
| BUG-01 | Bugs ouverts | Nombre d'issues ouvertes avec le libellé `type/bug` | GitHub Issues, horodatage de l'extraction | À nommer | À nommer |
| BUG-02 | Délai de tri | Médiane entre l'ouverture et l'ajout d'un libellé de priorité | Historique GitHub Issues | À nommer | À nommer |
| BUG-03 | Taux de réouverture | Bugs rouverts divisés par bugs fermés sur la période | Historique GitHub Issues | À nommer | À nommer |

## 3. UX

| Identifiant | Nom | Formule | Source | Propriétaire | Cible |
|---|---|---|---|---|---|
| UX-01 | Réussite de tâche | Tâches terminées divisées par tâches tentées | Protocole de test enregistré | À nommer | À nommer |
| UX-02 | Temps de tâche | Médiane en secondes sur la tâche critique | Protocole de test enregistré | À nommer | À nommer |
| UX-03 | Confiance déclarée | Note déclarée après l'usage, échelle à nommer | Questionnaire daté | À nommer | À nommer |

## 4. Produit

| Identifiant | Nom | Formule | Source | Propriétaire | Cible |
|---|---|---|---|---|---|
| PRD-01 | Acquisition vérifiée | `signup_verified / feed_session_start * 1000` | Événements canoniques | À nommer | À nommer |
| PRD-02 | Complétion vidéo | `video_complete / video_start` | Événements canoniques | À nommer | À nommer |

## 5. SEO web

| Identifiant | Nom | Formule | Source | Propriétaire | Cible |
|---|---|---|---|---|---|
| SEO-01 | Couverture d'indexation | Pages indexées divisées par pages publiable | Données de recherche, extrait daté | À nommer | À nommer |
| SEO-02 | Signaux web essentiels | Part des URL qui passent les trois signaux de terrain | Données de terrain, extrait daté | À nommer | À nommer |

## 6. Règles de mise à jour

Toute nouvelle mesure reçoit un identifiant de groupe, une formule écrite et une source datée avant d'entrer dans le tableau de bord. La suppression d'une mesure conserve son identifiant avec la date d'arrêt et le motif. Le script `scripts/check_kpi.py` vérifie la présence des identifiants et des sections avant chaque fusion. Les cibles, les seuils d'alerte et les propriétaires sont nommés par décision écrite, jamais déduits d'une valeur observée.
