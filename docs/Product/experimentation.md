# Pro : fiche d'expérimentation

**Statut** : version 2, 26 novembre 2026  
**Rôle** : définir comment un test produit est décidé avant son lancement. Aucun résultat n'est déclaré sans cette fiche écrite et datée.  
**Documents liés** : [Mesure](./mesure.md), [Vision, section 8](./vision.md), [Décisions](./decisions.md), [Tableau de bord](./tableau-de-bord.md)

**Plateformes.** La dimension `plateforme` prend les valeurs `mobile`, `web` et `desktop`, définies ainsi :

- `mobile` : applications natives iOS et Android sur téléphone.
- `web` : site responsive dans un navigateur, utilisé sur ordinateur et tablette.
- `desktop` : application exécutable installée sur Windows et macOS. Linux est différé et non spécifié en phase 1.

## Test 1 : parcours ouvert contre mur de connexion au lancement

| Champ | Contenu |
|---|---|
| Hypothèse | Le parcours qui laisse le visiteur accéder directement au fil augmente les inscriptions avec email vérifié pour 1 000 sessions de fil par rapport à un mur de connexion au lancement, sans dégrader les garde-fous de confiance |
| Origine de l'hypothèse | [Vision, sections 3 et 4](./vision.md), opportunité O2 de la recherche UX, décision D-001 |
| Unité de randomisation | Session de fil courte, identifiée par le jeton décrit dans `../Technique/README.md`. Aucun identifiant d'appareil permanent, aucune correspondance entre appareils. Pour un test réservé aux membres, l'unité est le compte avec email vérifié |
| Population | Visiteurs qui émettent `feed_session_start` sur `mobile`, `web` et `desktop` dans les deux Congo, ventilés par `plateforme`, `city`, `trade` et `campaign_ref`. Les comptes avec email vérifié forment une population distincte, jamais confondue avec les sessions. Chaque lecture porte une valeur `mobile`, `web` ou `desktop`, ou un agrégat explicitement nommé « toutes plateformes » |
| Durée | Fenêtre à nommer avant le lancement, avec date de début et date de fin écrites dans le registre. Aucune durée n'est avancée dans ce cadrage |
| Effectif et effet minimal détectable | À nommer avant le lancement par le responsable produit, avec la méthode de calcul. Aucun chiffre n'est inventé ici |
| Métrique primaire | Inscriptions avec email vérifié pour 1 000 sessions de fil, formule `signup_verified / feed_session_start * 1000`, telle que définie dans `./mesure.md` |
| Garde-fous | Vidéos vues par session, part des membres qui publient, signalements, comptes suspects, délai de première décision de modération, taux de contestation et taux de renversement. Leur base est relevée pendant la Phase 0 ou les deux premières semaines ; le seuil relatif et la fenêtre sont inscrits au registre avant le test |
| Règle d'arrêt | Arrêt immédiat si un garde-fou franchit le seuil inscrit au registre, avec journalisation de la mesure, de la dimension, de la fenêtre et de l'action. Sinon, arrêt à la date de fin nommée avant le lancement. Aucune lecture partielle ne déclenche une décision |
| Décision | Écrite au registre avec date, propriétaire, variante retenue et documents touchés. Le parcours ouvert devient le parcours par défaut seulement si la métrique primaire progresse sans dégradation des garde-fous |
| Responsable | Responsable produit, à nommer avant le lancement. Revue par les quatre fonctions : produit, design, développement et modération |

## Règles applicables à tout test

1. Une hypothèse est une phrase que l'on accepte de voir contredite. Les hypothèses infirmées sont écrites au registre avec leur preuve.
2. La métrique primaire et chaque garde-fou portent le nom canonique de `./mesure.md`. Aucune formule parallèle n'est autorisée.
3. Les événements utilisés sont ceux de FS-11 du [PRD](./prd.md), conservés 30 jours. Ils portent `plateforme` avec une valeur parmi `mobile`, `web` et `desktop`, puis `city`, `trade` et `campaign_ref` comme dimensions facultatives distinctes.
4. Aucune cohorte visiteur à sept jours n'est calculée, conformément à D-020. Le retour à sept jours porte sur les comptes avec email vérifié.
5. Les seuils, l'effectif, la durée et l'effet minimal détectable sont inscrits au registre avant le premier envoi d'événement de test.
6. Aucune mesure ne fusionne les plateformes sans le dire : une lecture par plateforme porte `mobile`, `web` ou `desktop`, et une lecture agrégée est nommée « toutes plateformes ». Les dimensions `city`, `trade` et `campaign_ref` restent séparées de `plateforme`.
7. Le test est lu dans le [tableau de bord](./tableau-de-bord.md) ; l'instrumentation précède le test, pas l'inverse.

## Tests à cadrer plus tard

| Sujet | Phase | État |
|---|---|---|
| Cibles de revue du client desktop, arbitrage A-03 et PRD section 9.1 | Phase 1 | Arbitrées le 26 novembre 2026, cinq cibles sur machine modeste, revue prévue le 26 décembre 2026, aucune valeur présentée comme mesurée |
| Portée mobile modifiable hors binaire natif, arbitrage A-13 | Phase 1 | Arbitrée le 26 novembre 2026, six catégories servies sans binaire natif, contrôle de non interruption de session à cadrer avant FS-01 selon la section 10.1 du PRD |
| Sous-titres corrigés des vidéos avec son, règle D-021 | Phase 1 | Règle retenue, fiche de test à nommer avant la première publication |
| Règle N2 pour les candidatures, décision D-010 | Phase 2, hors MVP | Décision retenue le 26 novembre 2026, aucun test lancé avant la phase 2 |
| Niveau organisations payant, décision D-011 | Phase 5 | Nom et privilèges définis le 26 novembre 2026, aucun test lancé |
