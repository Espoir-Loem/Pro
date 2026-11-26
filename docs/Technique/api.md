# API : points d'accès, réponses et limites

**Propriétaire.** à nommer. **Statut.** proposée. **Date.** 25 novembre 2026.
**Dépendances.** `architecture.md`, `adr-002-identite-session.md`.

## Points d'accès utiles au MVP

| Endpoint | Chemin | Règle principale |
|---|---|---|
| Fil public | `GET /feed` | Lecture sans compte, filtrée par `decision_visibilite` |
| Vidéo | `GET /video/{id}` | Réponse sans email, téléphone ni données de vérification |
| Recherche | `GET /search` | Uniquement des champs publics du profil |
| Dépôt vidéo | `POST /video` | Compte requis, état `draft` puis `uploading` |
| Signalement | `POST /report` | Visiteur autorisé, référence pseudonyme dérivée de la clé de modération |
| Contestation | `POST /appeal/{jeton}` | Jeton à usage unique, empreinte vérifiée dans `appeal` |
| Messages | `GET /messages`, `POST /messages` | Compte requis, contrôle de `block` avant envoi |
| Inscription vérifiée | `POST /signup/verify` | Émet `signup_verified`, aucun rattachement rétroactif |

Les noms de chemins sont des propositions. Le framework est retenu en D-009 : NestJS et TypeScript, avec validation des contrats partagés dans `packages/domain`. Le format de sérialisation est fixé par ces contrats. L'hébergeur dépend de A-12 et le fournisseur CDN reste dans le cadre du budget D-022, sans choix dans cette fiche.

## Données absentes des réponses

Aucune réponse publique ne contient : email, téléphone, jeton push, jeton de session brut, identifiant d'appareil, donnée de vérification N2 ou N3. Le profil public suit la visibilité choisie par la personne, selon FS-04 et `../UX/userflow.md`. Les messages d'erreur restent neutres : ils n'indiquent pas si un compte ou une vidéo existe. Ces règles valent pour les trois clients, y compris le client desktop : aucune réponse ne contient d'identifiant de machine ou d'installation.

## Limites

| Flux | Limite | Source |
|---|---|---|
| Lecture | 200 requêtes par minute | PRD section 10 |
| Authentification | 5 tentatives par minute et par adresse | PRD section 10 |
| Follow et like | vitesse surveillée, pénalité sur erreurs répétées | PRD section 10 |
| Téléversement | quota et taille définis dans `menaces.md` | `menaces.md` |

## Vérification

Un test d'API parcourt chaque point d'accès depuis les trois clients, `mobile`, `web` et `desktop`, avec un jeton visiteur expiré, un jeton rotaté et un jeton de compte. Il échoue si une donnée privée apparaît dans une réponse, si un jeton visiteur obtient un abonnement push, ou si un lien de contestation est accepté deux fois.
