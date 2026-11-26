# Tâches d'architecture avant le code

**Statut** : préparées le 26 novembre 2026, titulaires intérimaires nommés le 26 novembre 2026, aucune autre tâche exécutée  
**Source** : [Fiches techniques](../../../docs/Technique/README.md) et [ADR 001](../../../docs/Technique/adr-001-stack.md)  
**Règle** : l'ordre suit les dépendances documentées. Aucune tâche n'est marquée terminée sans preuve archivée. Aucun titulaire n'est inventé.

| Ordre | Tâche | Dépendance | Critère de sortie | Titulaire |
|---|---|---|---|---|
| 1 | Nommer les titulaires des fiches marquées « à nommer » : identité de session, menaces, architecture, API, données, observation, responsabilités | A-04 sur le porteur intérimaire | Chaque fiche porte un titulaire explicite dans le tableau de bord technique | Espoir LOEMBA, intérimaire, nommé le 26 novembre 2026 |
| 2 | Finaliser `adr-002-identite-session.md` sur les principes retenus, avant FS-01 et la première migration | Performance et mesure | Le jeton visiteur court, la rotation et l'absence de rattachement rétroactif sont écrits, avec propriétaire | Espoir LOEMBA, intérimaire |
| 3 | Porter `menaces.md` de proposée à prête, avant sécurité et architecture | Identité de session | Les quatre questions OWASP et les six menaces priorisées sont validées avec date | Espoir LOEMBA, intérimaire |
| 4 | Porter `architecture.md` à prête, après menaces et performance, avant vidéo et API | Menaces, performance | Le conteneur `client_desktop`, la lecture séparée de l'écriture et l'invalidation de cache sont arrêtés | Espoir LOEMBA, intérimaire |
| 5 | Porter `video.md` et `api.md` à prêtes, après architecture | Architecture, D-022 pour le budget | Octets, bitrates et coût pour 1 000 vues écrits d'un côté ; endpoints et réponses sans données privées de l'autre | Espoir LOEMBA, intérimaire |
| 6 | Porter `donnees.md` à prête, après conservation et identité de session, avant la première migration | Conformité conservation, A-12 pour la migration | Tables, états, transitions et durées de conservation écrits, sans choix d'hébergeur | Espoir LOEMBA, intérimaire |
| 7 | Rejouer `securite.md` avant FS-07 et FS-09 | Menaces, identité de session | Outils épinglés, ASVS 2 et contrôles de la coque desktop opposables | Espoir LOEMBA, intérimaire |
| 8 | Porter `observation.md` à prête avant FS-11 | Mesure, identité de session | Schéma d'événement et test de refus des champs d'appareil écrits, sans formule nouvelle | Espoir LOEMBA, intérimaire |
| 9 | Porter `responsabilites.md` à prête avant la revue de sortie MVP | Toutes les fiches, A-03 et A-13 | RACI complet, revue de performance et signature réparties | Espoir LOEMBA, intérimaire |
| 10 | Conserver `performance.md` comme référence de revue, sans valeur mesurée avant mesure | A-03 | Cinq cibles de revue, 30 lancements par système, p75 et traces jointes, revue prévue le 26 décembre 2026 | Espoir LOEMBA, intérimaire |

La ligne 1 est satisfaite le 26 novembre 2026 : les sept fiches portent Espoir LOEMBA comme titulaire intérimaire depuis le 25 novembre 2026 au titre de A-04. Les fiches et le tableau de bord technique servent de preuve. Les lignes 2 à 10 gardent leur critère de sortie et ne sont pas marquées terminées.

## Blocages qui ne relèvent pas de l'ordre des fiches

A-12 bloque l'hébergeur, la région de stockage et la première migration. Le conseil local externe n'est pas désigné et aucun hébergeur n'est arrêté. Les prestataires du client `desktop` sont à nommer avant le premier commit de code de stack, selon A-04, et la [grille de vérification](../prestataires-desktop.md) prépare cette nomination sans désigner personne. La Phase 0 doit écrire l'opportunité retenue avant qu'une histoire entre dans le sprint. Le dénominateur de H1 reste à trancher par décision écrite avant J7.

## Ce qui n'est pas une tâche d'architecture

Le choix d'un fournisseur CDN, le choix d'un service de transcription et le choix d'un hébergeur ne sont pas pris ici. Le client `mobile` reste dans le périmètre des six catégories de A-13, sans téléchargement de code exécutable. Aucune migration, aucun lockfile et aucun fichier de code n'est produit par ces tâches de préparation.
