# Sécurité : socle de contrôles

**Propriétaire.** à nommer. **Statut.** proposée. **Date.** 25 novembre 2026.
**Déclenchement.** Socle avant FS-01 et FS-02, revue complémentaire avant FS-07 et FS-09. `menaces.md` précède cette fiche.

## Contrôles

| Contrôle | Règle | Test |
|---|---|---|
| Jeton visiteur | Court, non durable, rotatif, jamais identifiant d'appareil | Un jeton expiré ou rotaté est refusé |
| Pseudonymisation | Clé distincte par finalité : modération, analyse, contestation | Aucune jointure possible entre pseudonymes de finalités différentes |
| Push | Aucun abonnement visiteur, jeton fournisseur réservé au compte | Aucune création de `push_subscription` sans `account_id` |
| Journal d'audit | Ajout seul, horodatage fiable, accès limité aux rôles autorisés | Tentative de modification d'une ligne refusée |
| Motifs de modération | Codes fermés, masquage des données personnelles dans le texte libre | Analyse automatique des motifs écrits |
| Contestation | Empreinte du jeton, usage unique, expiration, révocation après décision | Deuxième usage refusé avec 410 |
| Limites de débit | 5 tentatives d'authentification par minute et par adresse, 200 requêtes de lecture par minute | Les deux seuils retournent 429 |
| Téléversement | Quota, validation du type, retrait EXIF avant stockage | Objet stocké sans coordonnée GPS |
| Cache | Revalidation de visibilité à chaque réponse, purge sur `visibility_changed` | Test T1 de `architecture.md` |
| Client desktop | Aucun identifiant de machine ou d'installation, cache local sans décision de visibilité, mêmes contrôles que les deux autres clients | Test T1 de `architecture.md` rejoué depuis le client desktop |
| Secrets | Clés de pseudonymisation conservées séparément des pseudonymes, rotation journalisée | Une clé remplacée est tracée et les anciennes valeurs restent lisibles selon `conservation.md` |
| Mise à jour automatique | Paquet signé et vérifié avant installation sur `desktop`, retour à la version précédente en cas d'échec, aucune interruption de session, aucun identifiant d'appareil ou d'installation | Une mise à jour non signée est refusée ; la version précédente reste active ; la session en cours n'est pas coupée ; aucun identifiant machine n'est écrit dans `analytics_event` |

## Journal de publication

Toute transition de vidéo porte acteur `system`, `moderateur` ou `auteur`, avec `rule_id` quand l'acteur est `system`, selon `adr-003-porte-publication.md`. Aucun identifiant de modérateur n'est inventé pour une décision automatique.

## Niveau visé

Le niveau [OWASP ASVS](https://owasp.org/projects/asvs) visé reste à trancher et figure dans `responsabilites.md`. En attendant, les contrôles ci-dessus font partie de la définition de terminé et sont exécutés en intégration sur les trois clients livrés ensemble, y compris le client desktop.
