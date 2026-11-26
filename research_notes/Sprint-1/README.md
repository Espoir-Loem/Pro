# Pro : préparation du sprint 1 sans code

**Statut** : préparé le 26 novembre 2026, aucun code applicatif  
**Portée** : organisation du premier sprint de la Phase 1, avant le premier commit de stack  
**Sources canoniques** : [PRD](../../docs/Product/prd.md), [Roadmap](../../docs/Product/roadmap.md), [Stack D-009](../../docs/Technique/adr-001-stack.md), [Histoires](../../docs/UX/userstories.md), [Fiches techniques](../../docs/Technique/README.md), [Décisions](../../docs/Product/decisions.md)

Ce dossier rend le sprint 1 prêt à être ouvert sans écrire une ligne de code applicatif. Il ne choisit pas l'opportunité retenue, il ne fixe aucun seuil nouveau et il ne nomme aucun titulaire inventé. Les faits qui viennent du terrain restent à apporter par la Phase 0.

## Ce qui est prêt

| Élément | Emplacement | État |
|---|---|---|
| Backlog candidat | [backlog-candidat.md](./sprint/backlog-candidat.md) | Histoires P0 classées par opportunité, sélection finale en attente de J10 |
| Définition de prêt | [definition-of-ready.md](./sprint/definition-of-ready.md) | Conditions d'entrée en sprint, aucun seuil inventé |
| Inventaire des contrats typés | [contrats-typés.md](./sprint/contrats-typés.md) | Noms et sources canoniques, aucun fichier de code |
| Tâches architecture | [architecture-taches.md](./sprint/architecture-taches.md) | Ordre d'exécution des fiches, titulaires à nommer signalés |
| Tâches CI | [ci-taches.md](./sprint/ci-taches.md) | Contrôles à rejouer sur chaque pull request et à chaque release |
| Grille des prestataires `desktop` | [prestataires-desktop.md](./prestataires-desktop.md) | Points à vérifier avant de nommer les prestataires Windows et macOS, aucun nom avancé |
| Protocole des mises à jour | [controle-mises-a-jour.md](./controle-mises-a-jour.md) | Scénarios et preuves à rejouer avant FS-01, aucun contrôle exécuté |

## Portes avant le premier commit de code

1. Phase 0 terminée : dix jours ouvrés, huit entretiens, quatre réserves, Brazzaville et Kinshasa traités séparément, H1 à H8 validés, preuves archivées et opportunité O écrite. Issues #4 et #9.
2. Dénominateur de H1 tranché par décision écrite avant J7. La méthode est confirmée, le choix n'est pas encore écrit.
3. A-12 levée par un avis local écrit d'un conseil externe avant hébergeur, région de stockage et première migration.
4. Prestataires `desktop` Windows et macOS nommés avant le premier commit de code de stack, selon A-04. La [grille de vérification](./prestataires-desktop.md) prépare cette nomination sans désigner personne.
5. Titulaires des fiches techniques : Espoir LOEMBA, intérimaire depuis le 25 novembre 2026 au titre de A-04, inscrit le 26 novembre 2026 dans les sept fiches, identité de session, menaces, architecture, API, données, observation et responsabilités. Cette porte est levée. Une nomination définitive reste à écrire sans créer de nouvelle porte.
6. Preuve de signature, de retour arrière et de non interruption de session attendue au premier rendu signé des trois clients. Le [protocole de contrôle](./controle-mises-a-jour.md) prépare les scénarios à rejouer avant FS-01, sans exécuter ni déclarer de contrôle.
7. Contrôle SEO de l'issue #11 à passer sur un rendu web réel, donc après l'existence d'un rendu.

## Ce que ce dossier ne fait pas

Il ne remplace ni le PRD pour les critères d'acceptation, ni le registre des décisions pour les décisions opposables, ni `mesure.md` pour les formules, ni les fiches techniques pour les choix d'ingénierie. Il ne contient aucun fichier TypeScript, JavaScript ou Rust, aucun lockfile et aucune migration. Aucun changement ici n'ouvre la porte du code.
