# Avenant mises à jour automatiques

**Date.** 25 novembre 2026.  
**Portée.** Ce rapport est un snapshot de l'état après l'ajout de D-024, avant l'inscription de D-009. L'état courant figure dans [avenant-agent-et-stack.md](./avenant-agent-et-stack.md).  
**Demande du porteur.** « il faut aussi ajouter le principe de mise à jour automatique pour les application histoire de ne pas depondre à jour mise à jours du store ».  
**Périmètre.** `docs/` uniquement pour les modifications. Les rapports historiques ne sont pas réécrits. Le rapport `verification-coherence.md` reste le contrôle de la version précédente. Le présent avenant couvre l'ajout de D-024 et du point A-13.

## Principe ajouté

La règle retenue est D-024 : mise à jour automatique des clients, sans dépendance à un cycle de validation de store pour ce qui peut être servi hors binaire natif. Elle est opposable sur `mobile`, `web` et `desktop`.

Le périmètre mobile hors binaire natif n'est pas inventé. Il est préparé au point A-13 de `docs/Product/arbitrage.md`, avec une liste fermée, une règle par store, une date de validation et un propriétaire à nommer. Aucune règle de store n'est affirmée sans preuve écrite. Tout changement de binaire natif suit le circuit du store.

Le principe s'énonce ainsi dans les documents :

- `web` : déploiement côté serveur, visible à la navigation suivante, session en cours préservée ;
- `desktop` : paquet signé, vérifié avant installation, appliqué au redémarrage ou au lancement suivant, retour à la version précédente en cas d'échec ;
- `mobile` : règles, contenus et éléments d'interface autorisés servis côté serveur, le reste soumis au circuit du store validé en A-13 ;
- règle commune : aucune interruption de session, aucune modification de décision de modération sans trace, aucun identifiant d'appareil, d'installation ou de machine.

## Fichiers modifiés

| Fichier | Ajout |
|---|---|
| `docs/Product/decisions.md` | D-024 créée avec date, motif, propriétaire, source liée, portée et historique. Conséquences écrites. Registre en version 3 |
| `docs/Product/prd.md` | Section 10.1 avec le chemin par plateforme et les cinq règles communes. D-024 dans les décisions héritées, le périmètre MVP, les risques et les questions ouvertes. Définition de terminé portée à sept conditions, dont la vérification de mise à jour |
| `docs/Product/roadmap.md` | Critères de sortie Phase 1 alignés sur les sept conditions et sur la condition 7, avec la portée mobile validée en A-13 |
| `docs/Product/arbitrage.md` | Point A-13 ajouté avant le sprint 1. Liste des décisions retenues mise à jour. Numérotation des points classée par échéance |
| `docs/Product/manifeste.md` | Conviction 13, sans décalage des convictions 1 à 12 |
| `docs/UX/design-principles.md` | Principe 10, revue d'interface portée à dix principes |
| `docs/Technique/README.md` | Contrainte transversale de D-024, sans ADR numéroté supplémentaire |
| `docs/Technique/securite.md` | Contrôle de mise à jour : signature, retour arrière, session non interrompue, zéro identifiant machine |
| `docs/Technique/responsabilites.md` | Revue de la condition 7 et titulaire du point A-13, sans nom inventé |
| `docs/Conformite/confidentialite-visiteur.md` | Contrôle de confidentialité appliqué au mécanisme de mise à jour |
| `docs/Operations/incidents.md` | Mise à jour ajoutée aux fonctions touchées et au journal d'incident |
| `docs/Operations/support.md` | Réponse courte ajoutée à Brazzaville et à Kinshasa, sans promesse hors périmètre |
| `docs/README.md` | Pointeur vers le présent avenant |

Aucun fichier n'a été créé ni supprimé dans `docs/`. Aucun code n'a été écrit.

## Contrôles

| Commande ou contrôle | Attendu | Résultat |
|---|---|---|
| `grep -rnP '\x{2014}\|\x{2013}' docs` | Aucune occurrence | Vide, conforme |
| `grep -rnP '[\x{3400}-\x{9FFF}\x{3040}-\x{30FF}\x{AC00}-\x{D7AF}]' docs` | Aucune occurrence | Vide, conforme |
| Recherche des marqueurs temporaires dans `docs` | Aucune occurrence | Vide, conforme |
| Recherche des formulations réduites à deux plateformes dans `docs` | Aucune occurrence | Vide, conforme |
| Recherche des anciens décomptes de conditions et de principes dans `docs` | Aucune occurrence résiduelle | Vide, conforme |
| Résolution des liens relatifs dans `docs` | Zéro lien cassé | 443 liens résolus, 0 cassé |
| Numérotation FS, US et D | FS-01 à FS-11, US-01 à US-17, D-001 à D-024 sans saut | Conforme |
| Blocs Mermaid | Tous fermés | Conforme |
| `find docs -type f \| wc -l` | 59 fichiers | 59, conforme |
| Décisions retenues | D-001 à D-008, D-012 à D-021, D-023 et D-024 | Conforme |
| Questions ouvertes | D-009, D-010, D-011 et D-022 | Conforme, inchangées |
| Portée mobile | Aucune affirmation de contournement des règles des stores | Conforme, A-13 reste à arbitrer |
| D-012 | Aucun identifiant d'appareil, d'installation ou de machine ajouté | Conforme |
| D-016 | Aucune dérogation à la porte de publication ni au contrôle de visibilité | Conforme |

## Points restant à arbitrer

Les douze points déjà ouverts restent ouverts. Le point A-13 s'ajoute pour la portée mobile de D-024 :

- A-01 à A-05 et A-13 avant le sprint 1 ;
- A-06 à A-08 avant la Phase 2 ;
- A-09 à A-12 avant ouverture publique ;
- D-009, D-010, D-011 et D-022 restent les quatre questions ouvertes du registre.

Le point A-13 précise l'application de D-024 sans rouvrir D-024. Toute modification de la règle elle-même suit la procédure de réouverture du registre.

## Conclusion

Les contrôles mécaniques et sémantiques sont verts après ajout. Le principe de mise à jour automatique est inscrit au registre, dans le cahier des charges, dans les principes de design et dans les contrôles techniques et opérationnels. La part mobile hors binaire natif reste à valider par écrit avant le sprint 1. Cohérence confirmée, Error 0, warning 0.
