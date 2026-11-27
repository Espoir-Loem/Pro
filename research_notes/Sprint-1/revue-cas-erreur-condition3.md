# Fiche de contrôle des cas d'erreur par parcours, condition 3

**Statut** : préparée le 27 novembre 2026, aucun cas rejoué, aucune trace archivée, aucune porte levée  
**Sources canoniques** : [PRD, condition 3 de la section 11](../../docs/Product/prd.md), [Roadmap, Phase 1](../../docs/Product/roadmap.md), [Parcours utilisateur](../../docs/UX/userflow.md), [Recherche UX, H9](../../docs/UX/ux-research.md), [D-021 au registre](../../docs/Product/decisions.md), [Fiche de contrôle de la condition 4](./revue-code-accessibilite-condition4.md), [Revue de sortie de phase](../Planning/revue-sortie-phase.md)  
**Règle** : cette fiche décrit les cas à rejouer et les traces à archiver. Elle ne rejoue aucun cas, n'ajoute aucune règle au PRD et ne prononce pas la condition 3.

## 1. Ce qui est déjà écrit

La condition 3 de la section 11 du PRD exige que les cas d'erreur décrits dans le parcours correspondant aient été testés. La roadmap demande que la trace de la revue des cas d'erreur soit archivée avec l'identifiant du relecteur et la date. Les cas sont lus sur les trois clients livrés ensemble : `mobile` pour les applications natives iOS et Android, `web` pour le navigateur, `desktop` pour l'application exécutable Windows et macOS. Linux est différé.

Les embranchements déjà décrits dans les parcours portent notamment sur la lecture automatique refusée, la demande d'autorisation push refusée après la première action significative, la correction de sous-titres absente qui laisse la vidéo en brouillon non publiée selon D-021, un refus avant publication qui mène à `rejected` avec motif et contestation, un retrait après publication qui mène à `removed` avec notification et voie de contestation, un destinataire bloqué avant l'ouverture dont l'envoi est refusé sans préciser qui a bloqué qui, la limite de 2 000 caractères avec compteur restant, et la distinction entre « autre » et « aucun motif sélectionné » dans le signalement. Le blocage après réception est inscrit comme hypothèse H9, pas comme règle du PRD : il n'est rejoué comme règle que si une décision écrite l'inscrit dans FS-07. Aucun cas n'est supposé ici et aucun libellé d'erreur n'est inventé.

## 2. Cas à rejouer et traces à archiver

| Identifiant | Cas décrit dans le parcours | Trace à archiver | État |
|---|---|---|---|
| X1 | Lecture automatique refusée lors de la découverte du fil | Extrait du rendu et du réglage de préférence, par client | À rejouer |
| X2 | Autorisation push refusée après la première action significative, parcours poursuivi | Extrait du parcours sans notification, par client | À rejouer |
| X3 | Correction de sous-titres absente, vidéo maintenue en brouillon non publiée | Extrait de l'état `draft` et de la porte de publication, selon D-021 | À rejouer |
| X4 | Refus avant publication, état `rejected` avec motif et contestation | Extrait de l'état, du motif et du chemin de contestation | À rejouer |
| X5 | Retrait après publication, état `removed`, notification et voie de contestation | Extrait de l'état et de la notification d'auteur | À rejouer |
| X6 | Destinataire bloqué avant l'ouverture, envoi refusé sans précision sur le blocage | Extrait du refus, sans identité de blocage dévoilée | À rejouer |
| X7 | Limite de 2 000 caractères atteinte dans le chat, compteur restant affiché | Extrait du compteur et du refus d'envoi au delà de la limite | À rejouer |
| X8 | Motif « autre » distinct de « aucun motif sélectionné » dans le signalement | Extrait du parcours de signalement avec les deux états distingués | À rejouer |
| X9 | Blocage après réception, seulement si H9 a été validée et inscrite dans FS-07 par décision écrite | Décision écrite et extrait du comportement, ou sans objet | À rejouer si décision écrite |

Aucun cas n'est marqué comme réussi dans cette fiche. Aucun libellé d'erreur, aucun compteur relevé et aucun extrait ne sont préremplis. Un cas sans description dans le parcours correspondant n'est pas ajouté à cette liste.

## 3. Champs à remplir au moment de la revue

| Champ | Valeur |
|---|---|
| Date de la revue des cas d'erreur | À renseigner |
| Client et parcours concernés | À renseigner pour `mobile`, `web` et `desktop` |
| Relecteur des cas d'erreur | À renseigner |
| Cas X1 à X9 rejoués, un par un | À renseigner, aucune case cochée à l'avance |
| Liens vers les traces archivées | À renseigner |
| Écarts constatés | À renseigner, ou aucun |
| Actions datées et responsables | À renseigner, ou aucune |
| Conclusion sur la condition 3 | À renseigner, aucune conclusion préremplie |
| Titulaire de la décision | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner |
| Archive de la revue et historique | À renseigner |
| État | En attente de revue |

Une ligne sans trace archivée ni relecteur nommé n'est pas tenue pour vérifiée. Un écart reste une action datée et n'est pas transformé en réussite tacite. La revue ne crée aucune règle nouvelle et ne modifie ni les critères d'acceptation, ni la condition 3.

## 4. Ce que cette fiche ne fait pas

Elle ne rejoue aucun cas, n'écrit aucun libellé d'erreur, ne nomme aucun relecteur, ne valide pas H9, ne prononce pas la condition 3, ne clôt aucune phase, ne lève aucune porte et ne contient aucun code applicatif.
