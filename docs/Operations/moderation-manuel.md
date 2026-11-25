# Manuel de modération

**Déclencheur.** Avant FS-09 du [PRD](../Product/prd.md).  
**Dépendances.** [journée type](./journee-type-moderation.md), [contestation](./contestation.md), [veille arnaque](./veille-arnaque.md), [Conformité](../Conformite/README.md).  
**Propriétaire.** Référent modération, à nommer, pour Brazzaville et pour Kinshasa.  
**Statut.** Procédure écrite, priorités P1 à P3 opposables, relecture obligatoire avant retrait ou suspension.

## Traitement d’un ticket

| Ville | Étape | Action attendue | Trace |
|---|---|---|---|
| Brazzaville | Lire le ticket | Motif, ville, référence pseudonyme, âge du signalement, nombre de signalements | `report_created`, `report_age` |
| Brazzaville | Classer | Appliquer P1, P2 ou P3 de la [journée type](./journee-type-moderation.md) | priorité inscrite au ticket |
| Brazzaville | Décider | Conserver, masquer, retirer ou suspendre | `moderation_action` avec identifiant, motif, date |
| Kinshasa | Lire le ticket | Motif, ville, référence pseudonyme, âge du signalement, nombre de signalements | `report_created`, `report_age` |
| Kinshasa | Classer | Appliquer P1, P2 ou P3 de la [journée type](./journee-type-moderation.md) | priorité inscrite au ticket |
| Kinshasa | Décider | Conserver, masquer, retirer ou suspendre | `moderation_action` avec identifiant, motif, date |

Un retrait ou une suspension demande une relecture par une deuxième personne avant application. Le modérateur d’origine ne juge pas seul sa propre décision. Un masquage P1 peut être immédiat, la décision définitive reste soumise à la relecture.

## Canal de décision

1. **Email canonique.** Il fait foi. Il contient la décision, le motif, le délai unique de contestation de 30 jours et le lien unique de contestation. Il reste le seul canal fiable si le compte est suspendu.
2. **Push neutre.** Texte : « Une mise à jour concerne votre compte. Ouvrez Pro pour la consulter. » Aucun libellé de sanction sur écran verrouillé. Le lien mène à l’élément concerné, pas à la contestation.
3. **Bandeau pour membre connecté.** Texte : « Une décision vous concerne. Le détail est dans votre email. » Aucun motif de sanction dans le bandeau.

Ces trois canaux sont complémentaires. Le push et le bandeau ne remplacent jamais l’email canonique.

## Sort du contenu

Une vidéo retirée reste stockée pendant le délai de contestation de 30 jours. Elle n’est pas supprimée avant l’échéance. Le sort final est écrit dans [contestation.md](./contestation.md). Le signalant visiteur n’a pas de recours écrit : cette règle est tranchée dans la même fiche et vaut pour les deux villes.
