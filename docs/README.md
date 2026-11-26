# Documentation Pro

**Statut** : structure version 5, 25 novembre 2026
**Règle typographique** : aucun tiret cadratin ni demi-cadratin dans les fichiers du dossier
**Langue** : Français d'abord. Le français est la seule langue des phases 0, 1 et 2 selon A-08, arbitrée le 26 novembre 2026. Toute langue ajoutée à partir de la Phase 3 est inscrite au registre avec date, responsable et marché avant le premier contenu dans cette langue. Les langues suivantes sont validées marché par marché, avec date et responsable inscrits au registre. Aucune autre langue n'est datée dans ce cadrage.

Cette architecture range les documents par métier, pour que chaque personne sache quel fichier elle utilise et lequel elle met à jour. La liste ci-dessous recense les cinquante-neuf fichiers présents, y compris ce README.

## Organisation

| Dossier | Métier concerné | Fichiers présents | Rôle |
|---|---|---|---|
| Racine de `docs/` | Navigation | `README.md` | Entrée unique de la documentation et règles de mise à jour |
| `Product/` | Produit | `vision.md`, `manifeste.md`, `prd.md`, `roadmap.md`, `decisions.md`, `arbitrage.md`, `mesure.md`, `kpi.md`, `experimentation.md`, `tableau-de-bord.md` | Dire pourquoi Pro existe, ce qui est livré sur `mobile`, `web` et `desktop`, dans quel ordre, comment on le mesure, ce qui reste à trancher et pourquoi tel choix a été fait |
| `UX/` | Recherche et design | `ux-research.md`, `personas.md`, `userflow.md`, `userstories.md`, `usertories.md`, `design-principles.md`, `journey-map.md`, `referentiel-recherche.md` | Comprendre les gens, représenter les parcours, transformer les constats en histoires |
| `Redaction/` | Rédaction et contenu | `ia-defauts-et-tips.md` | Garder une voix humaine et éviter les tics de rédaction automatique |
| `Technique/` | Ingénierie | `README.md`, `adr-001-stack.md`, `adr-002-identite-session.md`, `adr-003-porte-publication.md`, `architecture.md`, `api.md`, `donnees.md`, `menaces.md`, `observation.md`, `performance.md`, `responsabilites.md`, `securite.md`, `video.md`, `seo-web.md` | Décrire la stack retenue `mobile`, `web` et `desktop`, les données, la performance, la sécurité et l'observation |
| `Conformite/` | Juridique, confidentialité, sûreté | `README.md`, `confidentialite-visiteur.md`, `conservation.md`, `droit-congolais.md`, `moderation-regles.md`, `organisation-verification.md`, `perimetre-juridique.md`, `union-europeenne.md`, `verification-identite.md` | Cadrer les obligations avant qu'elles deviennent urgentes |
| `Operations/` | Modération et support | `README.md`, `animation-createurs.md`, `astreinte.md`, `contestation.md`, `incidents.md`, `journee-type-moderation.md`, `moderation-manuel.md`, `montee-en-charge.md`, `support.md`, `veille-arnaque.md` | Faire vivre la file de modération, le support et les incidents |
| `Growth/` | Acquisition | `README.md`, `acquisition-brazzaville.md`, `acquisition-kinshasa.md`, `extension-afrique.md`, `lanceurs-metiers.md`, `mesure-campagnes.md`, `partenariats.md`, `phrases-invitation.md` | Attirer les premiers utilisateurs dans les deux Congo, puis au-delà |

Dans `UX/`, `usertories.md` est l'ancien nom conservé pour les liens historiques. Le nom courant est `userstories.md`. Aucun préfixe numérique n'est ajouté aux noms de fichiers : les sections sont numérotées, ce qui suffit à fixer l'ordre de lecture.

## Par où commencer

1. Lire `Product/vision.md` pour le pourquoi.
2. Lire `Product/prd.md` pour le périmètre du MVP.
3. Lire `UX/ux-research.md` pour ce qui est prouvé, supposé ou encore inconnu.
4. Utiliser `UX/userflow.md` et `UX/userstories.md` pour le travail quotidien de design et de développement.
5. Consulter `Product/decisions.md` avant de rouvrir une question déjà tranchée.
6. Consulter `Product/arbitrage.md` avant de demander une décision, puis y inscrire le choix retenu avant de modifier le registre.
7. Consulter `Product/mesure.md` avant toute instrumentation ou lecture de résultat.
8. Lire `Product/experimentation.md` avant tout test et `Product/tableau-de-bord.md` pour la lecture quotidienne.
9. Lire `Technique/menaces.md` avant `Technique/architecture.md` et `Technique/securite.md`.
10. Lire `Operations/journee-type-moderation.md`, `Operations/astreinte.md` et `Operations/montee-en-charge.md` avant toute ouverture publique.

## Règles de mise à jour

- Un changement de périmètre se note dans le PRD, puis dans la roadmap. Un changement de plateforme se note dans la section 2 du PRD avec les définitions de `mobile`, `web` et `desktop`, puis dans la roadmap, le registre des décisions, `mesure.md`, `experimentation.md` et `tableau-de-bord.md`.
- Un changement de compréhension utilisateur se note dans la recherche UX, puis dans les personas, les flows et les histoires.
- Une décision structurante se note dans `Product/decisions.md` avec sa date, son motif, son propriétaire, sa source liée et son historique.
- Une question ouverte reste dans la table « Questions ouvertes » du registre jusqu'à son arbitrage ; elle n'entre pas dans un sprint avant d'être passée en décision retenue.
- Aucune fonctionnalité n'entre dans un sprint sans histoire utilisateur rattachée à une opportunité de la recherche. La Phase 1 dépend de la sortie de la Phase 0.
- Les revues de sortie associent quatre fonctions : produit, design, développement et modération, avec un responsable nommé.
- Les documents de phase 2 restent séparés du MVP. Le modèle de pages d'organisation est dans le PRD, pas dans les histoires du premier sprint.
- Le nom canonique d'une mesure est défini dans `Product/mesure.md` et n'est pas redéfini ailleurs. Sa dimension `plateforme` distingue explicitement `mobile`, `web` et `desktop`, séparément de `city`, `trade` et `campaign_ref`. Le niveau organisations payant relève de la Phase 5 ; aucun classement payant n'est introduit dans la recherche.
- Une fiche technique porte son propriétaire, son statut et sa date. Un ADR suit le modèle unique décrit dans `Technique/README.md`.

## État des dossiers

Les huit dossiers listés ci-dessus contiennent chacun leurs fichiers et ne sont plus vides. La question encore à arbitrer reste identifiée dans `Product/decisions.md`, sous la table « Questions ouvertes », et préparée dans `Product/arbitrage.md`. Le détail des contrôles livrés figure dans `../reports/verification-finale.md`, l'avenant trois plateformes dans `../reports/avenant-plateformes.md`, le contrôle de cohérence dans `../reports/verification-coherence.md`, l'avenant sur les mises à jour automatiques dans `../reports/avenant-mises-a-jour.md`, l'avenant sur la stack et les fichiers d'agent dans `../reports/avenant-agent-et-stack.md` l'avenant sur le titulaire par défaut dans `../reports/avenant-titulaire-projet.md` et l'avenant sur la préparation du dépôt dans `../reports/avenant-depot-git.md`, et l'avenant sur GitHub et la CI dans `../reports/avenant-github-ci.md`, et l'avenant sur les règles de code et l'outillage dans `../reports/avenant-regles-code-outillage.md`, et l'avenant sur le suivi GitHub dans `../reports/avenant-suivi-github.md`, et l'avenant sur la gouvernance avec porteur unique dans `../reports/avenant-gouvernance-porteur-unique.md`, et l'avenant de cadrage du 26 novembre 2026 dans `../reports/avenant-cadrage-26-novembre-2026.md`. Les rapports antérieurs sont des snapshots datés ; l'état courant est celui du registre des décisions et du dernier avenant.
