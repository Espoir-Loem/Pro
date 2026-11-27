# Fiche de contrôle de la condition 6, file armée et astreinte nominée

**Statut** : préparée le 27 novembre 2026, aucune file armée constatée, aucun titulaire nommé, aucun exercice exécuté, aucune porte levée  
**Sources canoniques** : [PRD, condition 6 de la section 11](../../docs/Product/prd.md), [Roadmap, Phase 1](../../docs/Product/roadmap.md), [Opérations](../../docs/Operations/README.md), [Journée type de la modération](../../docs/Operations/journee-type-moderation.md), [Astreinte](../../docs/Operations/astreinte.md), [A-09 au registre](../../docs/Product/arbitrage.md), [Exercice à blanc de l'astreinte](./exercice-blanc-astreinte.md)  
**Règle** : cette fiche prépare la vérification de la condition 6. Elle n'arme aucune file, ne nomme aucun titulaire, n'ouvre aucun incident, n'exécute aucun exercice et ne lève aucune porte.

## 1. Ce qui est déjà écrit

La condition 6 de la définition de terminé demande une file de modération armée, une astreinte nominée et un test à blanc réussi du signalement visiteur jusqu'à la notification d'auteur. Le détail est renvoyé aux fiches opérationnelles. Brazzaville et Kinshasa sont deux villes distinctes : volumes, garde, incidents et mesures ne sont pas fusionnés, et aucune valeur de l'une n'est extrapolée vers l'autre. La dimension `plateforme` s'ajoute à la ville, avec `mobile`, `web` et `desktop`, Linux restant différé.

La journée type porte des hypothèses de volume pour 1 000 sessions de fil, par ville et par motif, les priorités P1 à P3, les délais de prise en charge et de décision, la relecture obligatoire et deux signaux actionnables, `queue_depth` et `report_age`. L'effectif minimal est d'un modérateur de garde et d'un relecteur joignable par ville, tous deux à nommer. L'astreinte porte les rôles par ville et pour le commun, le canal unique `astreinte-pro`, le numéro d'urgence à nommer, la rotation hebdomadaire et la passation du vendredi. A-09 retient la couverture de 08:00 à 20:00 en heure locale avec astreinte P1 hors plage, ainsi que le renfort bénévole coopté par le référent ville et encadré.

L'exercice à blanc est préparé dans sa propre fiche, avec les scénarios E1 à E8 joués par ville et par plateforme, du ticket pseudonymé jusqu'à `report_resolved`, plus une coupure touchant le seul client `desktop`. Aucun titulaire, aucun numéro d'urgence, aucun délai mesuré et aucun résultat d'exercice ne sont fournis à la date de préparation de cette fiche.

## 2. Points à vérifier avant tout lien public

Chaque point reste à vérifier sur pièce. Aucune ligne n'est marquée comme réussie ici.

| Point à vérifier | Ce qui est déjà écrit | Preuve à archiver | État |
|---|---|---|---|
| File de modération par ville | File ouverte séparément pour Brazzaville et Kinshasa, motifs fermés de FS-09, ticket pseudonyme avec ville et plateforme | À renseigner, extrait de file sans nom de visiteur | En attente de vérification |
| Effectif minimal par ville | Un modérateur de garde et un relecteur joignable, à nommer | À renseigner, écriture des nominations avec date | En attente de vérification |
| Priorités et délais | P1 à P3, cible de 15 minutes pour P1 et cible de 1 heure pour la décision, sans valeur mesurée préremplie | À renseigner, configuration datée | En attente de vérification |
| Astreinte nominée | Rôles par ville et pour le commun, numéro d'urgence à nommer, canal `astreinte-pro` | À renseigner, ligne datée dans `astreinte.md` | En attente de vérification |
| Couverture A-09 | 08:00 à 20:00 en heure locale, astreinte P1 hors plage | À renseigner, planning daté | En attente de vérification |
| Renfort bénévole | Coopté par le référent ville, encadré, engagement écrit et relecture obligatoire | À renseigner, engagement daté, ou aucun | En attente de vérification |
| Signaux actionnables | `queue_depth` et `report_age` avec destinataire nommé et délai d'escalade | À renseigner, configuration datée | En attente de vérification |
| Test à blanc | Scénarios E1 à E8 de la fiche dédiée, par ville et par plateforme, jusqu'à la notification d'auteur | À renseigner, compte rendu dans le canal unique, sans délai prérempli | En attente de vérification |
| Notification d'auteur | Email canonique, push neutre, bandeau pour membre connecté, lien de contestation | À renseigner, extraits datés | En attente de vérification |

## 3. Champs à remplir au moment de la vérification

| Champ | Valeur |
|---|---|
| Date de la vérification | À renseigner |
| Ville | À renseigner séparément pour Brazzaville et Kinshasa |
| Plateforme | À renseigner séparément pour `mobile`, `web` et `desktop` |
| Coordinateur des opérations | À renseigner |
| Modérateur de garde | À renseigner |
| Relecteur | À renseigner |
| Numéro d'urgence | À renseigner, aucun numéro prérempli |
| Canal unique utilisé | `astreinte-pro`, à confirmer à la vérification |
| Délai de prise en charge relevé | À renseigner, cible de 15 minutes, aucune valeur préremplie |
| Délai de décision relevé | À renseigner, cible de 1 heure, aucune valeur préremplie |
| Écart constaté | À renseigner, ou aucun |
| Action datée dans `incidents.md` | À renseigner, ou aucune |
| Propriétaire du compte rendu | À renseigner |
| Approbateur nommé | À renseigner |
| Archive de la vérification et historique | À renseigner |
| État | En attente de vérification |

Une cible n'est pas un relevé. Un écart reste une action datée et n'est pas transformé en réussite tacite.

## 4. Distinctions à conserver

Une file ouverte ne prouve pas la condition 6 sans astreinte nominée et sans test à blanc. Un exercice réussi sur une ville n'est pas transposé à l'autre, et une preuve lue sur un client n'est pas transférée aux deux autres. Une nomination ne remplace pas un avis juridique externe et ne lève pas A-12. Le renfort bénévole ne crée aucun titulaire tacite.

Cette vérification ne prononce pas l'ouverture publique, ne fixe pas de date de lancement selon A-05, ne remplace pas la condition 7 ni la revue de sortie MVP, ne valide aucune hypothèse H1 à H8 et ne lève aucune porte.

## 5. Ce que cette fiche ne fait pas

Elle n'arme aucune file, ne nomme aucun titulaire, ne crée aucun canal, n'envoie aucun email ni push, n'ouvre aucun incident, ne relève aucun délai, n'exécute aucun exercice, ne modifie aucune décision, ne lève aucune porte et ne contient aucun code applicatif.
