# Règles de modération

**Source primaire.** [PRD FS-09](../Product/prd.md), [DSA articles 17 et 20](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) cités sous condition dans [union-europeenne.md](union-europeenne.md).
**Propriétaire de validation.** à nommer. **Statut.** proposée. **Date.** 25 novembre 2026.

**Portée des plateformes.** Motifs, priorités, délais, actions et journal valent pour les trois plateformes de la dimension `plateforme` : `mobile` pour les applications natives iOS et Android, `web` pour le navigateur, `desktop` pour l'application exécutable Windows et macOS, rapide, sans lenteur. Linux est différé. Cette extension ne change aucune décision déjà prise, sous réserve du registre [decisions.md](../Product/decisions.md). La lecture des signalements reste celle de [mesure.md](../Product/mesure.md), avec le socle décrit dans [Technique](../Technique/README.md).

## Motifs et priorités

Les motifs sont fermés : spam, contenu trompeur, harcèlement, contenu dangereux, autre.

| Priorité | Motifs | Délai de première décision proposé | Statut |
|---|---|---|---|
| P1 | Contenu dangereux, harcèlement | 1 heure | à confirmer avec [Opérations](../Operations/README.md) |
| P2 | Spam, contenu trompeur | 6 heures | à confirmer |
| P3 | Autre | 24 heures | à confirmer |

La priorisation tient compte du motif et du nombre de signalements. Le volume, l'âge médian et le p95 de la file sont observés dans [../Technique/observation.md](../Technique/observation.md).

## Actions et journal

Actions possibles : conserver, masquer, retirer, suspendre le compte. Chaque action est journalisée avec acteur `system`, `moderateur` ou `auteur`, motif codé, horodatage et référence de règles, selon [../Technique/adr-003-porte-publication.md](../Technique/adr-003-porte-publication.md). Le journal est en ajout seul. Aucun identifiant de modérateur n'est inventé pour une décision automatique.

## Contestation

Le retrait d'une vidéo ouvre une contestation par lien à usage unique. Le délai est de 30 jours à compter de l'horodatage de réception de l'email canonique, comme décision déjà écrite dans [contestation.md](../Operations/contestation.md). La décision finale passe par une deuxième personne avant notification, selon la même fiche. La table `appeal` stocke l'empreinte du jeton, le texte, la décision, le motif et l'utilisateur qui a statué. Le jeton expire après décision. Une seconde utilisation est refusée.

Le signalant visiteur n'a pas de notification nominative : c'est une décision déjà écrite. Le recours anonyme n'est pas ouvert en parallèle, comme dans [contestation.md](../Operations/contestation.md). Si l'Union européenne est desservie, la compatibilité avec l'article 20 du DSA est à valider par conseil. Aucune obligation actuelle pour les deux Congo n'est affirmée ici.

## Vérification

Un test à blanc couvre le signalement visiteur jusqu'à la notification de l'auteur et l'ouverture de la contestation, sur `mobile`, `web` et `desktop`. Il échoue si un motif vide, un acteur inconnu ou un lien réutilisé apparaît.
