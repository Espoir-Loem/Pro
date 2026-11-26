# Fiche de test D-021, sous-titres corrigés avant la première publication

**Statut** : préparée le 27 novembre 2026, aucune vidéo, aucun rendu, aucun test exécuté, aucune porte levée  
**Sources canoniques** : [D-021 dans le registre](../../docs/Product/decisions.md), [PRD, FS-02 et FS-05](../../docs/Product/prd.md), [Parcours B](../../docs/UX/userflow.md), [Carte de parcours](../../docs/UX/journey-map.md), [Experimentation](../../docs/Product/experimentation.md), [WCAG 2.2 SC 1.2.2](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html)  
**Règle** : cette fiche décrit les scénarios à rejouer et les preuves à archiver. Elle n'exécute aucun test, ne produit aucune vidéo, ne corrige aucun sous-titre et ne lève aucune porte.

La règle D-021 est retenue depuis le 25 novembre 2026. Les vidéos avec son du MVP disposent de sous-titres générés automatiquement et corrigés par l'auteur avant publication. Si la correction n'est pas faite, la vidéo reste en brouillon et n'est pas publiée. Le contrôle est écrit à deux endroits du parcours B : à la préparation de la vidéo en FS-02 et à la modération en FS-05. Le PRD attache le même critère d'acceptation aux deux histoires. La fiche de test manquante est préparée ici, sans anticiper un résultat.

## 1. Périmètre

Le test porte sur les vidéos avec son du MVP. Aucun cas supplémentaire n'est inventé pour les vidéos sans son au-delà de la règle écrite. Aucun seuil de qualité de transcription, aucun délai de correction et aucun outil de sous-titrage ne sont ajoutés : le service de transcription reste derrière son interface selon `adr-001-stack.md`, et la correction par l'auteur reste imposée par D-021.

Les trois clients `mobile`, `web` et `desktop` sont livrés ensemble selon D-004. Le contrôle est rejoué sur chacun quand un rendu existe, sans présumer un comportement identique ni transférer une preuve d'un client à un autre. Aucun email réel, aucun CV et aucune pièce d'identité ne sont demandés pour ce test.

## 2. Scénarios à rejouer

| Identifiant | Geste à rejouer | Résultat attendu | Preuve à archiver |
|---|---|---|---|
| T1 | Une vidéo avec son reçoit des sous-titres générés automatiquement, puis l'auteur les corrige avant de publier | La correction est enregistrée avant le passage à `pending_review` | Trace de l'état et de la correction datée, sans donnée personnelle |
| T2 | Une vidéo avec son reçoit des sous-titres générés automatiquement, l'auteur tente de publier sans correction | La vidéo reste en `draft` et n'est pas publiée | Trace de l'état, du refus de publication et de l'absence dans le fil et sur le profil |
| T3 | La modération contrôle une vidéo avec son avant sa mise en ligne | La présence des sous-titres corrigés est vérifiée avant toute publication | Extrait du journal de modération avec la date du contrôle |
| T4 | La modération demande une correction sur une vidéo avec son | La vidéo retourne en `draft` et n'apparaît pas dans le fil | Trace du retour d'état et de l'absence dans le fil |
| T5 | Le même contrôle est rejoué sur `mobile`, `web` et `desktop` quand les rendus existent | Chaque client montre le même respect de la règle, sans présomption d'équivalence technique | Une preuve par client, datée, sans transfert de preuve entre clients |
| T6 | Le journal de la session est lu après chaque scénario | État de la vidéo, date du contrôle et identifiant de règle `D-021` sont inscrits, sans nom ni email réel | Extrait du journal avec la date et le client concerné |

Aucun scénario n'est marqué comme réussi dans cette fiche. Aucun identifiant de participant, de machine ou de compte réel n'y est inscrit.

## 3. Moments du contrôle et responsabilité

Le contrôle de préparation intervient avant l'envoi et le contrôle de modération avant la mise en ligne, comme dans le parcours B. La fiche est à rejouer avant la première publication, puis en revue de sortie MVP avec l'identifiant du relecteur et la date.

Le cadrage est assuré par Espoir LOEMBA, intérimaire depuis le 25 novembre 2026 au titre de A-04. Le registre des décisions porte encore la mention « titulaire à nommer » pour D-021. Aucune nomination définitive n'est écrite ici, aucune délégation tacite n'est créée.

## 4. Ce que cette fiche ne fait pas

Elle ne contient aucun code applicatif, ne produit aucune vidéo ni fichier de sous-titres, n'exécute aucun contrôle, n'avance aucun résultat, n'ajoute aucun seuil ni outil, ne nomme aucun titulaire, ne remplace pas les critères d'acceptation du PRD et ne lève aucune porte.
