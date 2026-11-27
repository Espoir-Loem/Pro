# Définition de prêt du sprint 1

**Statut** : préparée le 26 novembre 2026, aucune histoire encore prête  
**Source des critères d'acceptation** : [PRD](../../../docs/Product/prd.md), section 7. Ce fichier ne les recopie pas. La [grille de validation de la condition 1](./grille-validation-criteres-FS.md) enregistre les preuves à archiver par FS et par plateforme, sans recopier les critères ni case cochée.  
**Règle** : une histoire qui échoue à une condition reste au backlog. Aucune implémentation partielle n'ouvre la porte du code.

| Condition | Ce qui est vérifié | Source |
|---|---|---|
| 1. Identifiant | L'histoire porte O1 à O5 ou H1 à H9 | [Histoires](../../../docs/UX/userstories.md), règle 3 |
| 2. Critères lus | Les critères d'acceptation sont lus dans le PRD, sans reformulation locale | PRD section 7 |
| 3. Seuil de terrain | Le seuil ou la condition d'infirmation vient de la Phase 0, avec date et ville. S'il n'existe pas, l'absence est écrite | [Recherche UX](../../../docs/UX/ux-research.md), section 7 |
| 4. Dénominateur | Un seul dénominateur par test, sans mélange entre 8, 10, 6 et 5. Le point H1 est tranché par écrit avant J7 | [Registre Cycle 1](../../Cycle-1/hypotheses/registre-H1-H8.md) |
| 5. Plateformes | `mobile`, `web` et `desktop` sont traités ensemble, sans présumer des usages identiques. La plateforme réellement utilisée est consignée dans la fiche de session | [Recherche UX](../../../docs/UX/ux-research.md), section 2 |
| 6. Mesure | Le nom canonique et la formule sont lus dans le dictionnaire. La cible reste à nommer après la Phase 0 | [Mesure](../../../docs/Product/mesure.md) |
| 7. Fiche technique | La fiche dépendante est au statut prêt pour implémentation, avec un propriétaire nommé | [Fiches techniques](../../../docs/Technique/README.md) |
| 8. Contrat typé | Le contrat est identifié dans l'[inventaire](./contrats-typés.md). Aucun nouveau nom n'est créé sans source canonique | PRD sections 8 et 9, observation, API |
| 9. Contrôles | Les contrôles de chaque pull request sont prévus : typecheck, lint, tests, SCA, SAST, secrets, licences et référence d'issue ouverte | [Tâches CI](./ci-taches.md) |
| 10. Preuve | Le fichier de preuve est désigné avant l'implémentation : test, trace d'audit ou compte rendu de revue | [Définition de terminé](../../../docs/Product/prd.md), section 11 |

## Définition de terminé

La définition de terminé reste celle de la section 11 du PRD, avec ses sept conditions. Elle n'est pas réécrite ici. Les conditions 6 et 7 de cette section portent respectivement sur la file de modération armée et sur la preuve de signature, de retour arrière et de non interruption de session sur les trois clients.

## Refus d'entrée en sprint

Une histoire est refusée si son opportunité n'est pas écrite, si son seuil vient d'une hypothèse non validée, si son propriétaire technique est marqué « à nommer », si son contrat n'a pas de source canonique ou si la porte du premier commit n'est pas levée. Un refus est daté et motivé dans le compte rendu de préparation, sans modification silencieuse du backlog canonique.
