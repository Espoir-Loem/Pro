# Pro : schéma de lecture du tableau de bord

**Statut** : version 1, 25 novembre 2026  
**Rôle** : décrire comment les mesures du [dictionnaire canonique](./mesure.md) sont lues, ventilées et alertées. Les seuils des dix KPI sont dans [kpi.md](./kpi.md) depuis le 26 novembre 2026. Les autres seuils opérationnels ci-dessous sont arrêtés à la même date. Aucun résultat n'est présenté comme mesuré.  
**Documents liés** : [Mesure](./mesure.md), [Expérimentation](./experimentation.md), [Décisions](./decisions.md), [Opérations](../Operations/README.md), [Croissance](../Growth/README.md), [Observation technique](../Technique/README.md)

**Plateformes.** La dimension `plateforme` prend les valeurs `mobile`, `web` et `desktop`, définies ainsi :

- `mobile` : applications natives iOS et Android sur téléphone.
- `web` : site responsive dans un navigateur, utilisé sur ordinateur et tablette.
- `desktop` : application exécutable installée sur Windows et macOS. Linux est différé et non spécifié en phase 1.

## Schéma de lecture

Chaque lecture suit le même ordre, du plus général au plus actionnable :

1. Choisir la mesure par son nom canonique dans `./mesure.md`, jamais par un alias.
2. Vérifier la formule, le dénominateur et la population affichés sur la tuile.
3. Lire la période, limitée par la conservation des événements à 30 jours.
4. Lire la valeur globale, étiquetée « toutes plateformes » quand elle couvre `mobile`, `web` et `desktop`, puis la ventiler par `plateforme`, ville, métier et campagne.
5. Comparer au seuil inscrit au registre et à la base relevée pendant la Phase 0 ou les deux premières semaines.
6. Déclencher une alerte avec propriétaire, action et délai si le seuil est franchi.
7. Consigner la lecture et la décision dans le registre lorsque la mesure sert à trancher une hypothèse ou une question ouverte.

Une tuile ne peut pas être lue sans son dénominateur. Les sessions de fil et les comptes avec email vérifié restent deux populations distinctes, conformément à la règle de non fusion des dénominateurs de `./mesure.md` et à D-020.

## Contenu des tuiles

| Champ de la tuile | Contenu attendu |
|---|---|
| Nom canonique | Celui de `./mesure.md`, identique dans la vision, le manifeste et le PRD |
| Formule et dénominateur | Rappelés en clair, avec l'événement source |
| Population et période | Sessions de fil ou comptes vérifiés sur `mobile`, `web` et `desktop`, fenêtre de 30 jours glissants ; lecture par plateforme ou agrégat nommé « toutes plateformes » |
| Dimensions | Plateforme avec les valeurs `mobile`, `web` et `desktop`, ville, métier, campagne, avec la valeur « non renseignée » distincte d'une absence de donnée |
| État | Comparaison au seuil inscrit au registre, sans couleur substituée à une décision écrite |
| Propriétaire | Espoir LOEMBA, intérimaire, pour le produit et la modération |
| Dernier relevé | Date et heure du calcul, séparées de la date de la donnée |
| Action | Lien vers la règle d'alerte correspondante |

Les tuiles correspondent aux mesures suivantes, sans en créer de nouvelles : inscriptions avec email vérifié pour 1 000 sessions de fil, vidéos vues par session, part des membres qui publient, retour à sept jours des comptes vérifiés, délai de première décision de modération, taux de contestation et taux de renversement. Le taux de sauvegarde, les messages envoyés et les signalements sont lus comme des événements sources, avec la même règle de conservation.

## Dimensions de lecture

| Dimension | Champ d'événement | Définition | Limite |
|---|---|---|---|
| Plateforme | `plateforme` | Valeurs `mobile`, `web` et `desktop` définies dans la section 2 du [PRD](./prd.md) | Aucune fusion implicite : une lecture agrégée est nommée « toutes plateformes », et une lecture par plateforme porte une seule valeur |
| Ville | `city` | Ville déclarée dans la session ou le compte, selon la taxonomie D-017 calibrée sur Brazzaville et Kinshasa | Aucune extrapolation d'une ville à l'autre sans comparaison documentée |
| Métier | `trade` | Métier choisi à l'entrée ou renseigné sur le profil, selon la taxonomie D-017 | Aucune catégorie de proximité non définie ; la taxonomie est la seule source |
| Campagne | `campaign_ref` | Référence de campagne décrite dans `../Growth/README.md` | Aucun traceur tiers, aucun identifiant d'appareil permanent, aucune correspondance entre appareils |

Toute mesure peut être ventilée par une à quatre de ces dimensions. La dimension `plateforme` garde `mobile`, `web` et `desktop` distincts : aucune mesure ne fusionne les plateformes sans le dire dans le nom de la tuile et dans la population. Les dimensions `plateforme`, `city`, `trade` et `campaign_ref` restent séparées les unes des autres. Une ventilation n'introduit jamais d'identifiant visiteur permanent et ne crée pas de cohorte visiteur à sept jours. Les valeurs absentes sont affichées comme telles et ne sont pas imputées. Les événements non rattachés à une campagne sont regroupés sous une rubrique explicite, sans être attribués à une campagne par défaut.

## Règles d'alerte

Les seuils chiffrés sont ceux de [kpi.md](./kpi.md), arrêtés le 26 novembre 2026 à titre intérimaire. Le seuil de coût vidéo est de 0,001 USD par vue, inscrit en D-022 et lu séparément par ville. Une alerte n'est actionnable que si les cinq champs ci-dessous sont renseignés.

| Alerte | Condition de déclenchement | Destination | Action | Délai |
|---|---|---|---|---|
| Acquisition vérifiée en baisse | Moins de 20 inscriptions avec email vérifié pour 1 000 sessions de fil, sur 30 jours glissants, lues par `plateforme` | Espoir LOEMBA, intérimaire, responsable produit | Vérifier l'instrumentation `signup_verified` et `feed_session_start`, puis relire l'expérimentation en cours | 1 jour ouvré |
| Fil moins consulté | Complétion vidéo sous 45 %, par `plateforme`, par ville et par métier | Espoir LOEMBA, intérimaire, responsable produit | Contrôler le fil, la taxonomie D-017 et le profil réseau de référence | 1 jour ouvré |
| Publication en baisse | Part des membres qui publient sous 10 %, sur les comptes avec email vérifié | Espoir LOEMBA, intérimaire, responsable produit | Vérifier la chaîne FS-02 et FS-05, y compris la correction des sous-titres | 2 jours ouvrés |
| Retour des comptes en baisse | Retour à sept jours des comptes vérifiés sous 20 % | Espoir LOEMBA, intérimaire, responsable produit | Contrôler que la cohorte ne contient aucun visiteur et que `signup_verified` est bien l'email vérifié | 2 jours ouvrés |
| File de modération sous tension | Délai de première décision supérieur à 4 heures, ou `queue_depth` supérieur à 50, ou `report_age` supérieur à 24 heures | Espoir LOEMBA, intérimaire, astreinte | Appliquer la matrice de priorité et escalader selon la journée type | 4 heures |
| Contestations en hausse | Taux de contestation supérieur à 5 % ou taux de renversement supérieur à 10 % | Espoir LOEMBA, intérimaire, relecteur | Relire les motifs de décision et la table `appeal` ; prévoir un second relecteur | 1 jour ouvré |
| Coût vidéo hors cadre | Coût par vue supérieur à 0,001 USD, seuil D-022 lu par ville puis par marché | Espoir LOEMBA, intérimaire, responsable technique | Appliquer la montée en charge décrite dans `../Operations/README.md` et le profil vidéo de `../Technique/README.md` | 1 jour ouvré |

Une alerte franchie pendant un test déclenche la règle d'arrêt de `./experimentation.md` avant toute lecture de la métrique primaire. Une alerte sans propriétaire nommé n'est pas considérée comme traitée.

## Conservation et limites

- Les événements sont conservés 30 jours, comme dans FS-11 du [PRD](./prd.md) et D-015.
- Les agrégats sont conservés pour la finalité de mesure inscrite au registre, avec une durée à nommer avant la première mesure. Le [modèle de décision](../../research_notes/Sprint-1/decision-conservation-agregats.md) prépare cette écriture, sans durée ni finalité préremplies.
- Aucune donnée n'est affichée par appareil, par identifiant publicitaire ou par traceur tiers.
- Aucune mesure du tableau de bord n'est présentée comme une preuve de confiance : la confiance se lit aussi dans les décisions de modération tracées, décrites dans `../Conformite/README.md`.
