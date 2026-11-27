# Fiche de contrôle de la première publication réelle

**Statut** : préparée le 27 novembre 2026, aucune vidéo, aucun compte, aucune publication, aucune porte levée  
**Sources canoniques** : [D-014 et D-021 au registre](../../docs/Product/decisions.md), [PRD, FS-02, FS-05, FS-09 et section 11](../../docs/Product/prd.md), [Parcours B](../../docs/UX/userflow.md), [Fiche de test D-021](./test-sous-titres-D021.md), [A-10 au registre des arbitrages](../../docs/Product/arbitrage.md), [Décision d'ouverture publique](../Planning/decision-ouverture-publique.md)  
**Règle** : cette fiche prépare les points à vérifier au premier contenu réellement publié. Elle ne publie aucun contenu, ne crée aucun compte, n'écrit aucune citation et ne lève aucune porte.

## 1. Ce qui est déjà écrit

D-014 retient la modération en deux temps : texte vérifiable avant publication, vidéo en `pending_review`, signalement ouvert aux visiteurs. La publication vidéo doit être réversible et toute action doit laisser une trace. D-021 impose des sous-titres générés automatiquement puis corrigés par l'auteur avant publication pour les vidéos avec son du MVP. Si la correction n'est pas faite, la vidéo reste en `draft` et n'est pas publiée. Le même critère est attaché à FS-02 et à FS-05 dans le PRD, et la fiche de test D-021 prépare les scénarios T1 à T6 sans les exécuter.

La publication est réservée aux comptes N1 et plus, avec une légende de 150 caractères maximum et jusqu'à trois mots-clés. Le journal de publication porte l'acteur `moderateur` ou l'acteur `system`, avec un identifiant de règle quand l'acteur est `system`. Aucun identifiant de modérateur n'est inventé pour une décision automatique. A-10 fixe qu'aucun seuil de fil non vide n'est appliqué : si un métier n'a pas de vidéo modérée dans une ville, le fil général de cette ville est servi immédiatement, sans transposer une ville vers l'autre. D-004 impose que `mobile`, `web` et `desktop` soient livrés ensemble, avec une preuve par client sans transfert entre clients.

Aucune vidéo, aucun compte réel, aucun email, aucun CV, aucune pièce d'identité, aucune citation et aucune date de publication ne sont fournis à la date de préparation de cette fiche.

## 2. Points à vérifier au premier contenu publié

Chaque ligne reste à renseigner au moment de la publication. Aucun point n'est marqué comme réussi ici.

| Point à vérifier | Règle lue | Preuve à archiver | État |
|---|---|---|---|
| État avant publication | Vidéo en `pending_review` selon D-014, publication réversible | À renseigner, journal d'état daté | En attente de publication |
| Sous-titres corrigés | Correction par l'auteur avant publication selon D-021, sinon maintien en `draft` | À renseigner depuis T1 à T4, sans extrait de vidéo prérempli | En attente de publication |
| Décision de modération | Action tracée avec date, acteur, action et motif | À renseigner, extrait du journal sans identifiant de compte prérempli | En attente de publication |
| Décision automatique | Acteur `system` et identifiant de règle, aucun modérateur supposé | À renseigner, extrait du journal | En attente de publication |
| Notification d'auteur | Email canonique, push neutre, bandeau pour membre connecté, lien de contestation | À renseigner, extraits datés | En attente de publication |
| Visibilité dans le fil | Ville et plateforme concernées, sans transposition | À renseigner, extrait du fil daté | En attente de publication |
| Repli A-10 | Fil général de la ville servi immédiatement si aucun contenu modéré pour un métier | À renseigner, décision avec ville, date et propriétaire, ou aucun repli | En attente de publication |
| Lecture sur les trois clients | Une preuve par client pour `mobile`, `web` et `desktop` | À renseigner, extraits datés par client | En attente de publication |
| Absence de donnée visiteur exposée | Aucun identifiant permanent, aucun email réel dans la preuve archivée | À renseigner, contrôle de masquage daté | En attente de publication |

## 3. Champs à remplir au moment de la publication

| Champ | Valeur |
|---|---|
| Date de la publication | À renseigner, aucune date préremplie |
| Ville concernée | À renseigner, sans transposition |
| Plateforme concernée | À renseigner pour `mobile`, `web` ou `desktop` |
| Référence du contenu pseudonymisée | À renseigner, aucun identifiant réel prérempli |
| État avant la publication | À renseigner depuis le journal, sans état prérempli |
| État après la publication | À renseigner depuis le journal, sans état prérempli |
| Décision de modération | À renseigner, aucune action préremplie |
| Règle appliquée | À renseigner, sans règle inventée |
| Acteur de la décision | À renseigner, `moderateur` ou `system`, sans nom prérempli |
| Correction des sous-titres | À renseigner, sans résultat prérempli |
| Notification envoyée | À renseigner, sans extrait prérempli |
| Repli éventuel | À renseigner avec ville, date et propriétaire, ou aucun |
| Preuves archivées | À renseigner avec chemin réel et date |
| Relecteur identifié | À renseigner |
| Motif écrit | À renseigner |
| Propriétaire de l'archive | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner |
| État | En attente de publication |

Une ligne sans preuve archivée datée n'est pas un constat. Aucun contenu n'est publié par cette fiche et aucun état n'y est écrit à l'avance.

## 4. Distinctions à conserver

Une première publication ne valide aucune hypothèse H1 à H8, ne retient aucune opportunité O, ne clôt ni la Phase 0 ni la Phase 1, ne prononce pas l'ouverture publique selon A-05, ne lève pas A-12, ne choisit pas d'hébergeur ni de région de stockage et ne lève aucune porte. Elle ne modifie ni D-014 ni D-021, ne remplace pas la fiche de test D-021 ni la condition 6, et ne prouve pas à elle seule la condition 7.

Un contenu publié dans une ville ne justifie aucune transposition vers l'autre. Une preuve lue sur un client ne dispense pas des preuves attendues sur les deux autres. Aucune donnée de terrain n'est créée ici.

## 5. Ce que cette fiche ne fait pas

Elle ne produit aucun rendu, aucune vidéo, aucun sous-titre, aucun compte ni aucun email. Elle n'exécute aucun test, n'écrit aucune citation, n'archive aucune preuve, ne nomme aucun titulaire, ne modifie aucune décision, ne lève aucune porte et ne contient aucun code applicatif.
