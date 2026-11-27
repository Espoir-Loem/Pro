# Modèle de décision de révision de D-022 après 30 jours d'exploitation

**Statut** : préparé le 27 novembre 2026, aucune exploitation mesurée, aucune date, aucun résultat, D-022 inchangée, aucune porte levée  
**Sources canoniques** : [D-022 au registre](../../docs/Product/decisions.md), [Arbitrage A-02](../../docs/Product/arbitrage.md), [Montée en charge](../../docs/Operations/montee-en-charge.md), [Trame de décision du fournisseur vidéo et du CDN](../Sprint-1/decision-fournisseur-video-CDN.md), [Décision d'ouverture publique](./decision-ouverture-publique.md), [A-05 au registre](../../docs/Product/decisions.md)  
**Règle** : ce modèle prépare une révision à écrire après exploitation. Il ne mesure rien, ne modifie pas D-022, n'avance aucun montant ni date de lancement et ne lève aucune porte.

## 1. Ce qui est déjà arrêté

D-022 fixe une enveloppe mensuelle de 1 000 USD pour le CDN et la modération, répartie en 500 USD pour Brazzaville et 500 USD pour Kinshasa. La devise est USD, la fenêtre est le mois civil et le seuil est de 0,001 USD par vue, lu séparément par ville. La décision est révisée après 30 jours d'exploitation. Le fournisseur CDN n'est pas choisi par cette décision. Aucun montant n'est présenté comme mesuré.

La montée en charge porte trois seuils actionnables distincts. S1 déclenche le palier CDN de secours quand `video_impression` dépasse 20 000 par jour sur une ville. S2 ajoute un modérateur et un relecteur quand `queue_depth` dépasse 20 ou que le p95 de `report_age` dépasse 4 heures. S3 réduit le préchargement, force le transcodage adaptatif et suspend la nouvelle campagne dans la ville quand le coût par vue dépasse 0,001 USD. Ces seuils sont lus par ville et aucun n'est transposé d'une ville à l'autre. S3 s'applique aussi au client `desktop` sans modifier D-022.

La révision après 30 jours d'exploitation n'est ni la revue de performance du 26 décembre 2026, ni une date de lancement selon A-05, ni une date d'ouverture effective. Les courbes de la montée en charge sont des hypothèses de planification, pas des mesures. Le fournisseur est choisi dans sa propre trame et l'hébergeur reste lié à la levée écrite de A-12.

## 2. Champs à remplir au moment de la révision

| Champ | Valeur |
|---|---|
| Date de fin de la fenêtre de 30 jours d'exploitation | À renseigner, aucune date préremplie |
| Date de la décision de révision | À renseigner, distincte de la fin de fenêtre |
| Ville | À renseigner séparément pour Brazzaville et Kinshasa |
| Plateforme | À renseigner pour `mobile`, `web` et `desktop` |
| Données de coût relevées | À renseigner, aucune valeur mesurée préremplie |
| Coût par vue lu séparément par ville | À renseigner, sans transposition entre villes |
| Consommation de l'enveloppe dans le mois civil | À renseigner, aucun montant avancé |
| Lecture du seuil de 0,001 USD par vue | À renseigner, sans réécriture du seuil |
| Seuils S1, S2 et S3 déclenchés pendant la fenêtre | À renseigner, ou aucun |
| Actions prises sous S1, S2 et S3 | À renseigner, ou aucune |
| Incidence sur la capacité de modération | À renseigner |
| Incidence sur le fournisseur CDN retenu | À renseigner, sans changer la trame de choix |
| Enveloppe mensuelle et répartition par ville | 1 000 USD, 500 USD par ville, D-022 inchangée |
| Version du registre après révision | À renseigner |
| Motif écrit de la révision | À renseigner |
| Propriétaire de la décision | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner |
| Portée exacte de la décision | À renseigner |
| Archive de la décision et historique | À renseigner |
| État | En attente d'exploitation et de révision |

Une ligne sans donnée relevée ni preuve archivée n'autorise aucune modification de D-022. Les montants et le seuil ne sont pas réécrits pour coller à un résultat supposé. Aucun dépassement n'est traité par transposition d'une ville vers l'autre.

## 3. Distinctions à conserver

Réviser D-022 ne revient pas à choisir un fournisseur, à engager une dépense, à ouvrir un lien public ou à modifier une autre décision retenue. La révision ne rouvre pas D-009, ne lève pas A-12, n'autorise ni région de stockage ni première migration. Elle ne fixe pas la date de lancement de A-05 et ne remplace pas la décision d'ouverture publique.

Le seuil S3 est un déclencheur d'action pendant l'exploitation. La révision porte sur la décision elle-même et demande une écriture distincte au registre avec date, motif, propriétaire, source liée, portée et historique. Aucune prévision de trafic n'est transformée en résultat et aucune valeur relevée chez un fournisseur n'est présentée comme un coût mesuré de Pro.

## 4. Ce que ce modèle ne fait pas

Il n'observe aucune exploitation, ne relève aucun coût, ne modifie pas les montants ni le seuil de D-022, ne choisit aucun fournisseur, ne fixe aucune date, ne lève pas A-12, ne lève aucune porte et ne contient aucun code applicatif.
