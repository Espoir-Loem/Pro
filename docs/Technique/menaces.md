# Menaces : modélisation avant architecture

**Propriétaire.** à nommer. **Statut.** proposée. **Date.** 25 novembre 2026.
**Source.** [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling), [OWASP ASVS](https://owasp.org/projects/asvs).

## Les quatre questions OWASP

1. **Quoi ?** Le fil public, le téléversement vidéo, le chat 1:1, la modération, la contestation et les notifications push.
2. **Que peut-il se passer ?** Les six menaces classées ci-dessous.
3. **Que faire ?** Les mitigations et les tests associés, puis les contrôles de `securite.md`.
4. **Avons-nous bien travaillé ?** Chaque test est exécuté en intégration et rejoué après tout changement d'architecture ou de jeton.

## Menaces priorisées

| Rang | Menace | Mitigation | Test de vérification |
|---:|---|---|---|
| 1 | Abus de téléversement : fichiers massifs, types trompeurs, stockage saturé | Quota par compte, limite de taille, validation du type réel, transcodage asynchrone, retrait EXIF avant stockage | 100 téléversements hors quota retournent 429 et aucun objet n'est créé ; un fichier avec GPS est stocké sans métadonnée |
| 2 | Rejeu de jeton visiteur : ancien jeton réutilisé après rotation | Jeton court non durable, rotation, empreinte du jeton, expiration vérifiée à chaque requête | Un jeton rotaté puis rejoué est refusé ; aucun identifiant d'appareil n'est écrit dans `analytics_event`, y compris depuis le client desktop |
| 3 | Gratage du fil : lecture automatisée à haut débit | Limite de 200 requêtes par minute, pagination bornée, pénalité des erreurs répétées, cache avec contrôle de visibilité | 500 requêtes par minute donnent 429 ; le budget diminue plus vite après erreurs |
| 4 | Abus du lien de contestation : lien deviné, rejoué ou utilisé après décision | Jeton à usage unique, empreinte dans `appeal`, expiration courte, limite de tentatives, révocation après décision | Une seconde utilisation retourne 410 ; un lien expiré est refusé avant lecture du texte |
| 5 | Harcèlement en chat : envoi forcé après blocage, messages répétés | Contrôle de `block` avant ouverture de la fenêtre et avant envoi, limitation de cadence, signalement, états de livraison séparés de la modération | Un message vers une personne bloquée n'est pas livré et l'erreur reste neutre |
| 6 | Fuite du jeton push : jeton exposé dans une réponse, un journal ou un événement | `push_subscription` réservé au compte, aucun jeton dans les réponses publiques, les journaux ni `analytics_event`, révocation à la demande | Analyse automatique des réponses, journaux et événements : zéro occurrence du jeton ; aucun opt-in visiteur possible |

## Revue

La revue est déclenchée avant `securite.md` et `architecture.md`, puis avant FS-07 et FS-09. Les six menaces et leurs tests couvrent les trois clients livrés ensemble, y compris le client desktop. Aucune particularité de l'installateur, des mises à jour ou du cache local ne crée d'exception : la visibilité est revalidée à chaque réponse et aucun identifiant d'appareil permanent n'est écrit, y compris sur desktop. Le niveau ASVS visé reste à trancher et est inscrit dans `responsabilites.md`.
