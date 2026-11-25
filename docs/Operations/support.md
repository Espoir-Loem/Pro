# Support

**Déclencheur.** Avant le lancement, avec une réponse prête par ville.  
**Dépendances.** [modération](./moderation-manuel.md), [contestation](./contestation.md), [veille arnaque](./veille-arnaque.md), [PRD](../Product/prd.md).  
**Propriétaire.** Référent support, à nommer, pour Brazzaville et pour Kinshasa.  
**Statut.** Réponses courtes écrites, escalades nommées, titulaires à nommer.

**Dimension de lecture.** Chaque question est lue avec la ville et la plateforme : `mobile` pour les applications natives iOS et Android, `web` pour le navigateur, `desktop` pour l'application exécutable Windows et macOS, rapide, sans lenteur. Linux est différé. Une réponse ou une panne peut concerner le client `desktop` seul. Les réponses ci-dessous valent pour les trois clients. Aucun titulaire n'est inventé, les propriétaires restent « à nommer ».

| Ville | Question reçue | Réponse courte | Escalade |
|---|---|---|---|
| Brazzaville | « Pourquoi me demande-t-on mon email ? » | « Pour conserver une vidéo ou envoyer un message. La lecture reste publique. » | Référent produit, à nommer |
| Brazzaville | « Ma vidéo n’apparaît pas encore. » | « Elle est en attente de modération avant publication. » | Référent modération, à nommer |
| Brazzaville | « Un message me demande de l’argent. » | « Ne réponds pas et signale le message depuis la conversation. » | Référent confiance, à nommer |
| Brazzaville | « Pourquoi l’application a changé sans mise à jour du store ? » | « Une règle ou un contenu a été servi à distance dans les limites autorisées. Les changements du binaire suivent les règles du store. » | Référent technique, à nommer |
| Kinshasa | « Puis-je payer pour être mieux classé ? » | « Non. Pro est gratuit pendant l’acquisition et aucun classement payant n’existe. » | Référent croissance, à nommer |
| Kinshasa | « Où trouver une offre d’emploi sur Pro ? » | « Le MVP montre des personnes faire leur métier. Il ne publie pas d’offres. » | Référent produit, à nommer |
| Kinshasa | « Comment contester une décision ? » | « Écrivez au lien reçu dans l’email canonique, dans les 30 jours. » | Référent modération, à nommer |
| Kinshasa | « Pourquoi l’application a changé sans mise à jour du store ? » | « Une règle ou un contenu a été servi à distance dans les limites autorisées. Les changements du binaire suivent les règles du store. » | Référent technique, à nommer |

## Règles de réponse

Aucune réponse ne promet un emploi, un salaire, une vérification N2 au MVP, un classement payant ou une offre d’emploi au MVP. La gratuité totale pendant l’acquisition est rappelée telle quelle. Si la question porte sur un signalement ou une décision, le support ouvre un ticket lié et n’interprète pas la décision à la place du modérateur.

Une question sur une arnaque est traitée avec les avertissements rédigés dans [veille-arnaque.md](./veille-arnaque.md). Une panne ou une file saturée bascule dans [incidents.md](./incidents.md) avec la ville et la plateforme concernées. Une panne propre au client `desktop` est ouverte avec `plateforme=desktop`, sans fusion avec `mobile` ou `web`.
