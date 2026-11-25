# KPI de suivi du produit

**Version.** 2.
**Date.** 26 novembre 2026.
**Statut.** Cibles, fréquences et alertes arrêtées à titre intérimaire le 26 novembre 2026. Aucune valeur n'est présentée comme mesurée.
**Périmètre.** Bugs, UX, produit et SEO web. Les cibles sont des décisions intérimaires du porteur unique, révisables après trente jours de mesure datée.

## 1. Principes

Chaque mesure possède un identifiant, un nom, une formule, une source, un propriétaire, une cible, une fréquence et un seuil d'alerte. Les identifiants sont stables et ne sont pas réutilisés. Une mesure sans source datée n'est pas publiée. Les mesures produit reprennent les événements canoniques décrits dans [mesure.md](./mesure.md). Les mesures UX s'appuient sur les hypothèses de [ux-research.md](../UX/ux-research.md). Aucun classement payant n'entre dans ces mesures, conformément au registre des décisions.

Les chiffres ci-dessous sont des cibles intérimaires écrites le 26 novembre 2026. Ils ne constituent pas un résultat relevé, une promesse contractuelle ou une déduction d'une observation. Leur révision suit la procédure de décision écrite du registre, avec date, motif, propriétaire et historique. Le porteur unique cumule les dix propriétés de manière intérimaire depuis le 25 novembre 2026.

## 2. Bugs

| Identifiant | Nom | Formule | Source | Propriétaire | Cible | Fréquence | Alerte |
|---|---|---|---|---|---|---|---|
| BUG-01 | Bugs ouverts | Nombre d'issues ouvertes avec le libellé `type/bug` | GitHub Issues, horodatage de l'extraction | Espoir LOEMBA, intérimaire | 0 bug bloquant ou critique ouvert, au plus 2 bugs ouverts | Quotidienne à 09:00 UTC | 1 bug bloquant ou critique, ou plus de 2 bugs ouverts |
| BUG-02 | Délai de tri | Médiane entre l'ouverture et l'ajout d'un libellé de priorité | Historique GitHub Issues | Espoir LOEMBA, intérimaire | Au plus 1 jour ouvré | Quotidienne à 09:00 UTC | Plus de 2 jours ouvrés |
| BUG-03 | Taux de réouverture | Bugs rouverts divisés par bugs fermés sur la période | Historique GitHub Issues | Espoir LOEMBA, intérimaire | Au plus 5 % | Hebdomadaire, lundi à 09:00 UTC | Plus de 10 % |

## 3. UX

| Identifiant | Nom | Formule | Source | Propriétaire | Cible | Fréquence | Alerte |
|---|---|---|---|---|---|---|---|
| UX-01 | Réussite de tâche | Tâches terminées divisées par tâches tentées | Protocole de test enregistré | Espoir LOEMBA, intérimaire | Au moins 80 % | À chaque cycle de test, au minimum mensuel | Moins de 70 % |
| UX-02 | Temps de tâche | Médiane en secondes sur la tâche critique | Protocole de test enregistré | Espoir LOEMBA, intérimaire | Au plus 60 secondes | À chaque cycle de test, au minimum mensuel | Plus de 90 secondes |
| UX-03 | Confiance déclarée | Note moyenne déclarée après l'usage, échelle de 1 à 5 | Questionnaire daté | Espoir LOEMBA, intérimaire | Au moins 4 sur 5 | À chaque cycle de test, au minimum mensuel | Moins de 3,5 sur 5 |

## 4. Produit

| Identifiant | Nom | Formule | Source | Propriétaire | Cible | Fréquence | Alerte |
|---|---|---|---|---|---|---|---|
| PRD-01 | Acquisition vérifiée | `signup_verified / feed_session_start * 1000` | Événements canoniques | Espoir LOEMBA, intérimaire | Au moins 20 pour 1 000 sessions | Quotidienne à 09:00 UTC, fenêtre glissante de 30 jours | Moins de 10 pour 1 000 sessions |
| PRD-02 | Complétion vidéo | `video_complete / video_start` | Événements canoniques | Espoir LOEMBA, intérimaire | Au moins 60 % | Quotidienne à 09:00 UTC, fenêtre glissante de 30 jours | Moins de 45 % |

## 5. SEO web

| Identifiant | Nom | Formule | Source | Propriétaire | Cible | Fréquence | Alerte |
|---|---|---|---|---|---|---|---|
| SEO-01 | Couverture d'indexation | Pages indexées divisées par pages publiables | Google Search Console, extrait daté et archivé | Espoir LOEMBA, intérimaire | Au moins 90 % des pages publiables indexées sous 30 jours | Hebdomadaire, lundi à 09:00 UTC | Moins de 75 % |
| SEO-02 | Signaux web essentiels | Part des URL qui passent les trois signaux de terrain | Chrome UX Report via l'API PageSpeed Insights, extrait daté et archivé | Espoir LOEMBA, intérimaire | Au moins 90 % des URL qui passent les trois signaux | Mensuelle, le 1er du mois à 09:00 UTC | Moins de 75 % |

## 6. Règles de mise à jour

Toute nouvelle mesure reçoit un identifiant de groupe, une formule écrite, une source datée, une cible, une fréquence et un seuil d'alerte avant d'entrer dans le tableau de bord. La suppression d'une mesure conserve son identifiant avec la date d'arrêt et le motif. Le script `scripts/check_kpi.py` vérifie la présence des identifiants et des sections avant chaque fusion.

Les cibles, fréquences et alertes ci-dessus sont arrêtées le 26 novembre 2026 par décision intérimaire du porteur unique. Elles ne sont pas déduites d'une valeur observée. Aucune cible n'est présentée comme atteinte avant la première mesure datée. Toute révision est écrite dans [decisions.md](./decisions.md) avec date, motif, propriétaire et historique, puis rejouée par `scripts/check_kpi.py`.
