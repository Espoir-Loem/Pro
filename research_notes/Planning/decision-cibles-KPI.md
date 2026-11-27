# Modèle de décision des cibles KPI après la Phase 0

**Statut** : préparé le 27 novembre 2026, cibles intérimaires inchangées, aucune valeur relevée, aucune cible confirmée, aucune porte levée  
**Sources canoniques** : [KPI, version 2](../../docs/Product/kpi.md), [Dictionnaire de mesures](../../docs/Product/mesure.md), [Tableau de bord](../../docs/Product/tableau-de-bord.md), [Registre des décisions](../../docs/Product/decisions.md), [Roadmap, Phase 0](../../docs/Product/roadmap.md), [Décisions J10](../Cycle-1/decisions/J10-decisions.md)  
**Règle** : ce modèle prépare la confirmation ou la révision des cibles après la Phase 0. Il ne modifie pas les cibles intérimaires du 26 novembre 2026, n'avance aucun chiffre et ne prononce aucune mesure.

## 1. Ce qui est déjà écrit

Le fichier `kpi.md`, version 2 du 26 novembre 2026, porte dix identifiants stables : BUG-01 à BUG-03, UX-01 à UX-03, PRD-01 et PRD-02, SEO-01 et SEO-02. Les cibles, fréquences et alertes sont arrêtées à titre intérimaire, révisables après trente jours de mesure datée. Aucun chiffre n'est présenté comme un résultat relevé, une promesse contractuelle ou une déduction d'une observation. Toute révision suit la procédure de décision écrite du registre, avec date, motif, propriétaire et historique, puis est rejouée par `scripts/check_kpi.py`. Le porteur unique cumule les dix propriétés de manière intérimaire depuis le 25 novembre 2026.

Le dictionnaire de mesures précise que chaque cible est nommée après la sortie de la Phase 0, puis inscrite au registre avec sa date et son propriétaire. Les garde-fous relatifs sont définis à partir d'une base relevée pendant la Phase 0 ou les deux premières semaines d'observation, puis journalisés au registre. Aucune base de cette nature n'est fournie à la date de préparation de ce modèle.

Les mesures UX s'appuient sur les hypothèses de la recherche UX et les mesures produit reprennent les événements canoniques. Aucun classement payant n'entre dans ces mesures. Les dénominateurs ne sont pas fusionnés : la mesure à sept jours porte sur les comptes vérifiés, jamais sur les visiteurs. Les lectures restent ventilées par `plateforme` et par ville, sans transposition d'une ville vers l'autre. Aucune cible n'est présentée comme atteinte avant la première mesure datée.

## 2. Champs à remplir après la Phase 0

| Champ | Valeur |
|---|---|
| Date de la décision | À renseigner, après la Phase 0 |
| Identifiant KPI concerné | À renseigner parmi les dix identifiants stables |
| Cible intérimaire en vigueur | À renseigner depuis `kpi.md`, sans modification silencieuse |
| Décision | À renseigner, confirmation ou révision |
| Valeur de la cible retenue | À renseigner, aucun chiffre prérempli |
| Fréquence retenue | À renseigner, sans inventer de rythme |
| Seuil d'alerte retenu | À renseigner, sans inventer de seuil |
| Base relevée utilisée | À renseigner, Phase 0 ou deux premières semaines, sans valeur préremplie |
| Source datée et archivée | À renseigner |
| Ville et plateforme concernées | À renseigner séparément pour Brazzaville et Kinshasa et pour chaque plateforme |
| Dénominateur et population | À renseigner, sans fusion des dénominateurs |
| Motif écrit | À renseigner |
| Propriétaire de la décision | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner |
| Inscription au registre | À renseigner avec date et portée |
| Rejeu de `scripts/check_kpi.py` | À renseigner |
| Historique de la mesure | À renseigner, identifiant stable conservé |
| État | En attente de Phase 0 et de mesure datée |

Une ligne sans date ni source datée n'autorise ni confirmation ni révision. Une cible révisée ne réécrit pas l'historique de la mesure et ne réutilise pas son identifiant pour une autre mesure. Aucun seuil n'est déduit d'une observation supposée ni d'une transposition entre villes.

## 3. Distinctions à conserver

Nommer une cible ne modifie ni le nom canonique ni la formule du dictionnaire, ne crée pas de nouvelle mesure et ne change pas les conditions d'infirmation H1 à H8. Une cible confirmée ne valide aucune hypothèse et ne prouve pas qu'une mesure est atteinte. Aucune mesure du tableau de bord n'est une preuve de confiance.

Cette décision ne fixe pas de date de lancement selon A-05, ne lève pas A-12, n'autorise ni hébergeur ni migration et ne lève aucune porte. Elle ne remplace pas la revue de sortie de phase ni le compte rendu de J10.

## 4. Ce que ce modèle ne fait pas

Il ne relève aucune mesure, ne confirme aucune cible, ne révise aucun seuil, ne valide aucune hypothèse, ne modifie pas `kpi.md`, ne lève aucune porte et ne contient aucun code applicatif.
