# Modèle de décision de la conservation des agrégats et de leur finalité

**Statut** : préparé le 27 novembre 2026, aucune durée ni finalité retenue, aucune mesure effectuée, aucune porte levée  
**Sources canoniques** : [D-015 au registre](../../docs/Product/decisions.md), [Schéma de lecture du tableau de bord](../../docs/Product/tableau-de-bord.md), [Dictionnaire de mesures](../../docs/Product/mesure.md), [PRD, section 10 et FS-11](../../docs/Product/prd.md), [Confidentialité du visiteur](../../docs/Conformite/confidentialite-visiteur.md), [D-020 au registre](../../docs/Product/decisions.md)  
**Règle** : ce modèle prépare une écriture au registre avant la première mesure. Il ne fixe aucune durée, ne choisit aucune finalité, ne modifie pas D-015 et ne lève aucune porte.

## 1. Ce qui est déjà écrit

D-015 fixe la conservation des événements de session à 30 jours, décision retenue le 25 novembre 2026. Les agrégats sont conservés pour la finalité de mesure inscrite au registre, avec une durée à nommer avant la première mesure. Cette règle est reprise dans le schéma de lecture du tableau de bord, dans le dictionnaire de mesures, en FS-11 et dans la section 10 du PRD. Aucune durée ni finalité n'est avancée à la date de préparation de ce modèle. La [fiche de contrôle des durées de conservation](../Planning/controle-durees-conservation.md) prépare la vérification des durées écrites, sans résultat de purge ni valeur préremplie.

Les agrégats portent sur les mesures canoniques du dictionnaire : inscriptions avec email vérifié pour 1 000 sessions de fil, vidéos vues par session, part des membres qui publient, retour à sept jours des comptes vérifiés, délai de première décision de modération, taux de contestation et taux de renversement. Le taux de sauvegarde, les messages envoyés et les signalements sont lus comme des événements sources, avec la même règle de conservation. Aucune nouvelle mesure n'est créée ici.

Aucune mesure n'est présentée comme une preuve de confiance : la confiance se lit aussi dans les décisions de modération tracées. Aucune donnée n'est affichée par appareil, par identifiant publicitaire ou par traceur tiers. Une lecture agrégée est nommée « toutes plateformes » et les dimensions `plateforme`, `city`, `trade` et `campaign_ref` restent séparées. Les événements non rattachés à une campagne sont regroupés sous une rubrique explicite, sans attribution par défaut. D-020 interdit toute cohorte visiteur à sept jours.

Les garde-fous relatifs sont définis à partir d'une base relevée pendant la Phase 0 ou les deux premières semaines d'observation, puis journalisés au registre. Aucune base de cette nature n'est fournie à la date de préparation de ce modèle. Le choix de durée et de finalité reste à écrire avec date, motif, propriétaire, source liée, portée et historique. Aucune ligne n'est préremplie avec une pratique supposée d'un autre produit.

## 2. Champs à remplir avant la première mesure

| Champ | Valeur |
|---|---|
| Date de la décision | À renseigner, avant la première mesure |
| Nom canonique de la mesure agrégée | À renseigner, sans nom inventé |
| Finalité de conservation inscrite au registre | À renseigner, aucune finalité préremplie |
| Durée de conservation de l'agrégat | À renseigner, aucune durée préremplie |
| Conservation des événements de session | 30 jours, D-015 inchangée |
| Base de garde-fou utilisée | À renseigner, Phase 0 ou deux premières semaines, sans valeur préremplie |
| Événement source et formule | À renseigner depuis `mesure.md` |
| Dénominateur et population | À renseigner, sans fusion des dénominateurs |
| Dimensions de lecture | À renseigner, `plateforme`, `city`, `trade` et `campaign_ref` séparées |
| Nom de la tuile | À renseigner, agrégation nommée si plusieurs plateformes |
| Lecture « toutes plateformes » | À renseigner sans fusion implicite des plateformes |
| Absence de donnée par appareil, identifiant publicitaire ou traceur tiers | À confirmer, sans résultat prérempli |
| Cohorte visiteur à sept jours | Aucune, D-020 inchangée |
| Lien vers la décision au registre et historique | À renseigner |
| Propriétaire de la décision | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner |
| État | En attente de décision |

Une ligne sans date ni motif n'est pas une décision inscrite. La durée et la finalité ne sont pas déduites de la durée des événements ni d'une lecture implicite du tableau de bord. Aucune agrégation n'est créée pour contourner l'absence d'identifiant permanent visiteur.

## 3. Distinctions à conserver

Inscrire une durée et une finalité pour un agrégat ne modifie pas D-015, n'autorise pas à conserver des événements au delà de 30 jours, ne crée pas de cohorte visiteur et ne change ni les définitions de mesure ni les seuils du registre. Cette écriture ne remplace pas la revue de confidentialité de la condition 5, ne prononce aucune autre condition de la section 11, ne clôt aucune phase et ne fixe pas de date de lancement selon A-05.

Une lecture agrégée n'autorise ni transposition d'une ville vers l'autre, ni fusion des sessions de fil avec les comptes vérifiés, ni lecture par appareil. Une mesure présentée comme preuve de confiance contredit le schéma de lecture du tableau de bord. Aucune valeur relevée pendant la Phase 0 n'est réécrite pour faire passer une durée choisie après coup.

## 4. Ce que ce modèle ne fait pas

Il ne fixe aucune durée, ne choisit aucune finalité, n'effectue aucune mesure, ne modifie pas la conservation des événements de session, ne crée aucune mesure, ne change aucun seuil, ne lève aucune porte et ne contient aucun code applicatif.
