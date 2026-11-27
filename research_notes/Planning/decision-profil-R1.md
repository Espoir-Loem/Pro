# Modèle de décision du profil réseau R1

**Statut** : préparé le 27 novembre 2026, profil R1 encore proposé, aucune valeur retenue, aucune mesure relevée, aucune porte levée  
**Sources canoniques** : [Performance](../../docs/Technique/performance.md), [Architecture](../../docs/Technique/architecture.md), [Vidéo](../../docs/Technique/video.md), [Responsabilités](../../docs/Technique/responsabilites.md), [PRD, section 10](../../docs/Product/prd.md), [A-03 dans la grille d'arbitrage](../../docs/Product/arbitrage.md), [Fiche de contrôle de la revue A-03](./revue-performance-desktop-A03.md)  
**Règle** : ce modèle prépare une décision à écrire. Il ne retient aucune valeur, ne modifie pas les propositions de `performance.md`, ne révise pas A-03 et ne lève aucune porte.

## 1. Ce qui est déjà écrit

Le PRD parle de « réseau mobile correct », ce qui n'est pas mesurable. Le profil R1 de `performance.md` est proposé et sert de grille de revue commune à `architecture.md` et `video.md`. Ses paramètres portent tous la mention « à confirmer » : accès 4G LTE, débit descendant 1,5 Mbit/s, débit montant 0,5 Mbit/s, latence aller-retour 150 ms, perte de paquets 1 %, appareil à 4 cœurs et 2 Go de RAM avec navigateur récent, méthode en p75 sur 100 sessions par ville avec Brazzaville et Kinshasa séparées. Aucune de ces valeurs n'est retenue ici.

Le profil R1 sert les deux autres clients et la première image vidéo du client `desktop`. Le profil R2 est arbitré et réservé au `desktop`. Tout changement du profil R1 entraîne une relecture de `architecture.md` et de `video.md`. Les budgets de `performance.md` et les bitrates de `video.md` dépendent de R1 sans que leurs valeurs deviennent des mesures de Pro.

La revue de performance desktop du 26 décembre 2026 porte sur la machine R2 et lit la première image vidéo sur le profil R1. Le profil R1 n'est pas une cible contractuelle tant que sa décision n'est pas écrite. Aucune mesure de terrain n'est fournie à la date de préparation de ce modèle et aucune proposition n'est traitée comme un résultat.

## 2. Champs à remplir au moment de la décision

| Champ | Valeur |
|---|---|
| Date de la décision | À renseigner |
| Paramètres examinés | Ceux de `performance.md`, statut « à confirmer », aucune valeur retenue ici |
| Accès | À renseigner, proposition inchangée dans `performance.md` |
| Débit descendant | À renseigner, proposition inchangée dans `performance.md` |
| Débit montant | À renseigner, proposition inchangée dans `performance.md` |
| Latence aller-retour | À renseigner, proposition inchangée dans `performance.md` |
| Perte de paquets | À renseigner, proposition inchangée dans `performance.md` |
| Appareil de référence | À renseigner, proposition inchangée dans `performance.md` |
| Méthode de mesure | À renseigner, avec les villes traitées séparément |
| Motif écrit | À renseigner |
| Villes concernées | À renseigner séparément pour Brazzaville et Kinshasa |
| Clients concernés | À renseigner pour `mobile`, `web` et `desktop` |
| Incidence sur les budgets de `performance.md` | À renseigner |
| Incidence sur les bitrates de `video.md` | À renseigner |
| Relecture de `architecture.md` et de `video.md` | À renseigner avec date et liens |
| Incidence sur la revue A-03 du 26 décembre 2026 | À renseigner, sans réécrire A-03 |
| Propriétaire de la décision | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner |
| Historique de la décision | À renseigner |
| État | En attente de décision |

Une ligne sans date ni motif ne fixe pas le profil. Les propositions ne sont pas transformées en valeurs retenues par silence. Aucune valeur relevée chez un fournisseur ni aucune mesure supposée n'est présentée comme une mesure de Pro.

## 3. Distinctions à conserver

Confirmer le profil R1 ne modifie pas A-03, ne révise pas les cibles de revue de la machine R2, ne choisit pas de fournisseur CDN selon D-022, ne choisit pas d'hébergeur ni de région de stockage tant que A-12 reste ouverte, ne fixe pas de date de lancement selon A-05 et ne lève aucune porte.

Un profil confirmé ne prouve pas qu'une cible de performance est atteinte. Les budgets de `performance.md` restent des cibles de revue vérifiées sur des rendus réels. Un budget dépassé n'autorise pas une réduction des exigences d'accessibilité.

## 4. Ce que ce modèle ne fait pas

Il ne retient aucune valeur, ne relève aucune mesure, ne modifie pas `performance.md`, ne réécrit pas `architecture.md` ni `video.md`, ne révise pas A-03, ne lève aucune porte et ne contient aucun code applicatif.
