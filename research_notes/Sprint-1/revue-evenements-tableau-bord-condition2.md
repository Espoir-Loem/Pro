# Fiche de contrôle des événements canoniques et du tableau de bord, condition 2

**Statut** : préparée le 27 novembre 2026, aucun événement relevé, aucune tuile contrôlée, aucune porte levée  
**Sources canoniques** : [PRD, condition 2 de la section 11](../../docs/Product/prd.md), [Observation, événements canoniques](../../docs/Technique/observation.md), [Schéma de lecture du tableau de bord](../../docs/Product/tableau-de-bord.md), [Dictionnaire de mesures](../../docs/Product/mesure.md), [Confidentialité du visiteur](../../docs/Conformite/confidentialite-visiteur.md), [D-015 et D-020 au registre](../../docs/Product/decisions.md), [Revue de sortie de phase](../Planning/revue-sortie-phase.md)  
**Règle** : cette fiche décrit les points à vérifier et les preuves à archiver. Elle n'émet aucun événement, ne relève aucune mesure, ne contrôle aucune tuile et ne prononce pas la condition 2.

## 1. Ce qui est déjà écrit

La condition 2 de la section 11 du PRD exige que les événements prévus soient émis et visibles dans le tableau de bord. Les événements canoniques sont répartis en cinq familles : ouverture et fil, vidéo, conversion, social et modération, santé de la file. `signup_verified` désigne l'email vérifié en phase 1, ni la vérification N2 ni la vérification N3. Chaque ligne de `analytics_event` porte un identifiant, un type de la liste canonique, un horodatage, une plateforme, un `session_id` nullable et un `account_id` nullable. Les champs `city`, `trade` et `campaign_ref` sont optionnels. L'expiration est fixée à 30 jours sur les trois clients.

Aucun identifiant d'appareil permanent, aucun jeton push, aucun jeton de session brut ni aucune clé de pseudonymisation n'est écrit dans un événement. Le client `desktop` ne porte ni identifiant de machine, ni identifiant d'installation, ni empreinte matérielle. Aucun événement antérieur à `signup_verified` n'est réécrit ni rattaché à un compte. La lecture suit l'ordre du schéma : mesure canonique, formule, dénominateur, population, période, ventilation par `plateforme`, ville, métier et campagne, comparaison au seuil, alerte avec propriétaire, action et délai. Les sessions de fil et les comptes avec email vérifié restent deux populations distinctes. Aucune cohorte visiteur à sept jours n'est créée. Aucune tuile ne porte de nom canonique inventé ni de couleur substituée à une décision écrite. Aucun de ces points n'est présenté ici comme vérifié.

## 2. Points à vérifier et preuves à archiver

| Identifiant | Point à vérifier | Preuve à archiver | État |
|---|---|---|---|
| E1 | Types d'événements émis conformes à la liste canonique des cinq familles | Relevé des types présents dans `analytics_event` | À vérifier |
| E2 | Schéma de ligne complet, avec horodatage, plateforme, `session_id` et `account_id` nullable | Extrait du schéma et résultat du test d'intégration | À vérifier |
| E3 | Valeur de `plateforme` dans `mobile`, `web` et `desktop` seulement, sans fusion implicite | Relevé par plateforme | À vérifier |
| E4 | Champs optionnels `city`, `trade` et `campaign_ref` sans imputation des absences | Relevé des valeurs renseignées et de la rubrique explicite des non rattachés | À vérifier |
| E5 | Conservation à 30 jours vérifiée sur les trois clients, desktop compris | Journal de purge daté | À vérifier |
| E6 | Aucun identifiant d'appareil, de machine, d'installation ni d'empreinte matérielle dans les événements | Résultat du test de schéma, toutes plateformes | À vérifier |
| E7 | Aucun `account_id` sur un événement antérieur à `signup_verified` | Résultat du test de non rattachement | À vérifier |
| E8 | Signification de `signup_verified` limitée à l'email vérifié de phase 1 | Extrait de la définition canonique | À vérifier |
| E9 | Tuiles portant nom canonique, formule, dénominateur, population, période, dimensions, état, propriétaire et dernier relevé | Extrait du tableau de bord, sans valeur préremplie | À vérifier |
| E10 | Dénominateurs sessions de fil et comptes vérifiés distincts dans chaque lecture | Extrait des tuiles concernées | À vérifier |
| E11 | Ventilation par `plateforme`, ville, métier et campagne, avec agrégat nommé si besoin | Extrait d'une lecture ventilée | À vérifier |
| E12 | Alertes renseignées avec propriétaire, action et délai, dont le seuil D-022 lu par ville | Extrait de la règle d'alerte correspondante | À vérifier |

Aucune ligne n'est marquée comme réussie dans cette fiche. Aucun relevé, aucune valeur de tuile et aucun extrait ne sont préremplis. Une alerte sans propriétaire nommé n'est pas considérée comme traitée.

## 3. Champs à remplir au moment du contrôle

| Champ | Valeur |
|---|---|
| Date du contrôle | À renseigner |
| Client concerné | À renseigner pour `mobile`, `web` et `desktop` |
| Ville concernée | À renseigner séparément pour Brazzaville et Kinshasa |
| Points E1 à E12 vérifiés, un par un | À renseigner, aucune case cochée à l'avance |
| Liens vers les preuves archivées | À renseigner |
| Écarts constatés | À renseigner, ou aucun |
| Actions datées et responsables | À renseigner, ou aucune |
| Conclusion sur la condition 2 | À renseigner, aucune conclusion préremplie |
| Titulaire de la décision | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner |
| Archive du contrôle et historique | À renseigner |
| État | En attente de contrôle |

Une ligne sans preuve archivée n'est pas tenue pour vérifiée. Un écart reste une action datée et n'est pas transformé en réussite tacite. Le contrôle ne modifie ni les définitions de mesure, ni les seuils du registre, ni les conditions de la section 11.

## 4. Ce que cette fiche ne fait pas

Elle n'émet aucun événement, ne relève aucune mesure, ne contrôle aucune tuile, ne nomme aucun propriétaire de contrôle, ne prononce pas la condition 2, ne clôt aucune phase, ne lève aucune porte et ne contient aucun code applicatif.
