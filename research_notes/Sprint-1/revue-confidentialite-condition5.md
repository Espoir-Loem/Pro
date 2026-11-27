# Fiche de contrôle de la revue de confidentialité, condition 5

**Statut** : préparée le 27 novembre 2026, aucune revue tenue, aucun rendu contrôlé, aucun résultat avancé, aucune porte levée  
**Sources canoniques** : [Confidentialité du visiteur](../../docs/Conformite/confidentialite-visiteur.md), [PRD, condition 5 de la section 11](../../docs/Product/prd.md), [Décisions D-012 et D-020](../../docs/Product/decisions.md), [ADR identité et session](../../docs/Technique/adr-002-identite-session.md), [Registre H1 à H8](../Cycle-1/hypotheses/registre-H1-H8.md), [Revue de sortie de phase](../Planning/revue-sortie-phase.md)  
**Règle** : cette fiche décrit les points à vérifier et les preuves à archiver. Elle ne tient aucune revue, n'invente aucun résultat, ne nomme aucun propriétaire et ne prononce pas la condition 5.

## 1. Ce qui est déjà écrit

La condition 5 de la section 11 du PRD exige que la revue de confidentialité confirme qu'aucun identifiant permanent n'a été introduit pour un visiteur. Le vocabulaire impose de parler de visiteur non connecté, jamais d'utilisateur anonyme. Les contrôles couvrent les trois clients de la dimension `plateforme` : `mobile` pour les applications natives iOS et Android, `web` pour le navigateur, `desktop` pour l'application exécutable Windows et macOS. Linux est différé. Aucune jointure avec `signup_verified` n'est introduite pour le visiteur, quelle que soit la plateforme.

La durée proposée du jeton de session est de 15 minutes, à confirmer dans l'ADR identité et session. Aucun identifiant d'appareil n'est stocké, calculé ou transmis, aucun traceur tiers n'est admis dans le parcours du visiteur, aucune correspondance entre appareils n'est recherchée. Les pseudonymes relèvent de clés distinctes par finalité. Aucun jeton push visiteur n'est prévu : l'abonnement est réservé au compte. Les événements sont conservés trente jours, avec les champs optionnels `city`, `trade`, `campaign_ref` et `plateforme`. Les métadonnées vidéo sont retirées avant stockage. Le signalement visiteur porte une référence pseudonyme issue de la clé de modération. Le mécanisme de mise à jour automatique ne crée aucun identifiant d'appareil, d'installation ou de machine et le journal technique ne porte pas de rattachement à une personne.

Le recours anonyme par jeton n'est pas ouvert en parallèle, selon `contestation.md`. Si l'Union européenne est desservie, la question est à soumettre à conseil avec l'article 20 du DSA, sans en déduire une règle actuelle. La durée de conservation des agrégats et leur finalité sont inscrites au registre avant la première mesure. Aucune de ces lignes n'est présentée ici comme vérifiée.

## 2. Points à vérifier et preuves à archiver

| Identifiant | Point à vérifier | Preuve à archiver | État |
|---|---|---|---|
| C1 | Durée du jeton de visiteur confirmée dans l'ADR et expiration refusée sur les trois clients | Extrait de l'ADR daté et extrait du refus du jeton expiré | À vérifier |
| C2 | Aucun identifiant d'appareil stocké, calculé ou transmis sur `mobile`, `web` et `desktop` | Relevé des champs de `analytics_event` par plateforme | À vérifier |
| C3 | Aucun traceur tiers dans le parcours du visiteur, client `desktop` compris | Analyse réseau datée sur les trois clients | À vérifier |
| C4 | Aucune correspondance entre deux sessions distinctes, sur chaque plateforme et entre plateformes | Compte rendu du test à deux sessions | À vérifier |
| C5 | Clés de pseudonymisation distinctes par finalité et conservées séparément | Extrait de la revue des clés, sans valeur secrète | À vérifier |
| C6 | Aucune ligne `push_subscription` sans compte | Relevé de la table, sans identifiant de visiteur | À vérifier |
| C7 | Purge quotidienne des événements journalisée à trente jours | Journal daté de la purge | À vérifier |
| C8 | Métadonnées EXIF et GPS retirées avant stockage | Objet consultable sans coordonnée | À vérifier |
| C9 | Signalement visiteur rattaché à la clé de modération, sans jointure avec `signup_verified` | Extrait du chemin du signalement | À vérifier |
| C10 | Mise à jour automatique sans identifiant d'installation ni jointure avec `signup_verified` | Revue du journal technique, zéro identifiant d'installation | À vérifier |
| C11 | Agrégats, durée de conservation et finalité inscrits au registre avant la première mesure | Extrait du registre daté | À vérifier |
| C12 | Vocabulaire de visiteur non connecté respecté dans les rendus contrôlés | Extrait des écrans ou des textes relus | À vérifier |

Aucune ligne n'est marquée comme réussie dans cette fiche. Aucun rendu n'est décrit, aucun extrait n'est produit et aucun écart n'est résolu à l'avance.

## 3. Champs à remplir au moment de la revue

| Champ | Valeur |
|---|---|
| Date de la revue | À renseigner |
| Phase et brique concernées | À renseigner |
| Propriétaire de validation | À renseigner |
| Revueuse ou relecteur | À renseigner |
| Clients contrôlés | À renseigner pour `mobile`, `web` et `desktop` |
| Points C1 à C12 vérifiés, un par un | À renseigner, aucune case cochée à l'avance |
| Liens vers les preuves archivées | À renseigner |
| Écarts constatés | À renseigner, ou aucun |
| Actions datées et responsables | À renseigner, ou aucune |
| Conclusion sur la condition 5 | À renseigner, aucune conclusion préremplie |
| Titulaire de la décision | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner |
| Archive de la revue et historique | À renseigner |
| État | En attente de revue |

Un point sans preuve archivée n'est pas tenu pour vérifié. Un écart reste une action datée et n'est pas transformé en réussite tacite. La revue ne modifie ni les contrôles de la fiche confidentialité, ni les seuils du registre, ni les conditions de la section 11.

## 4. Ce que cette fiche ne fait pas

Elle ne tient aucune revue, ne contrôle aucun rendu, ne produit aucun extrait, ne nomme aucun propriétaire de validation, ne prononce pas la condition 5, ne clôt aucune phase, ne lève aucune porte et ne contient aucun code applicatif.
