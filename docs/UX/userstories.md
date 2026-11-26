# Pro : histoires utilisateur

**Statut** : version 2, 25 novembre 2026  
**Documents liés** : [PRD](../Product/prd.md), [Décisions](../Product/decisions.md), [Parcours](./userflow.md), [Recherche UX](./ux-research.md), [Mesure](../Product/mesure.md)

Ce fichier sert de backlog lisible. Les critères d'acceptation détaillés restent dans le [PRD](../Product/prd.md). Aucune histoire FS-01 à FS-11 n'entre dans un sprint sans identifiant O1 à O5 ou H1 à H9.

**Priorités.** P0 : obligatoire pour le MVP. P1 : phase suivante, à préparer hors sprint MVP. Une histoire liée à une décision ouverte n'a pas de priorité tant que la décision n'est pas retenue.

## Phase 1, MVP

| Identifiant | Histoire | Pourquoi | Priorité | Opportunité ou hypothèse | Lien PRD |
|---|---|---|---|---|---|
| US-01 | En tant que visiteur, je veux voir le fil sans créer de compte, afin de juger si Pro me concerne | La découverte précède l'identification | P0 | O2, H1 | FS-01 |
| US-02 | En tant que créateur, je veux envoyer une vidéo depuis mon téléphone, afin de publier sans logiciel externe | La preuve de travail doit être simple à produire | P0 | O5, H7 | FS-02 |
| US-03 | En tant que visiteur, je veux choisir mon métier et ma ville, afin de voir des vidéos proches de mon travail | Le fil général est utile, le fil proche l'est davantage | P0 | O3, H3 | FS-03 |
| US-04 | En tant que membre, je veux un profil public lisible sans compte, afin qu'on sache qui je suis avant de m'écrire | L'identité est visible avant le contact | P0 | O1, H2 | FS-04 |
| US-05 | En tant que membre, je veux publier une vidéo avec sous-titres corrigés, afin de montrer mon travail même sans audio | La publication est le geste central du créateur | P0 | O1, O5, H6 | FS-05, D-021 |
| US-06 | En tant que membre, je veux aimer, commenter, suivre et sauvegarder, afin de retrouver pendant la session ce qui m'a intéressé | Les interactions identifiées créent la valeur sociale, sans personnalisation à partir d'un historique conservé | P0 | O3, H3 | FS-06 |
| US-07 | En tant que membre, je veux écrire à une personne dont j'ai vu le travail, afin d'engager une conversation professionnelle | Le chat est la sortie du parcours de découverte | P0 | O4, H5 | FS-07 |
| US-08 | En tant que visiteur, je veux chercher par métier ou par ville, afin de trouver des personnes sans m'inscrire | La recherche sert autant la découverte que l'inscription | P0 | O3, H3 | FS-08 |
| US-09 | En tant que personne qui voit un contenu problématique, je veux le signaler, afin que la plateforme prenne une décision tracée | La confiance exige une voie de recours | P0 | O4, H5 | FS-09 |
| US-10 | En tant que membre, je veux être informé d'une réponse ou d'une décision, afin de revenir au bon moment | La notification sert le retour, pas l'engagement artificiel | P0 | O2, H4 | FS-10 |
| US-11 | En tant qu'équipe produit, je veux des événements propres, afin de mesurer la découverte sans pistage intrusif | La mesure doit respecter le visiteur | P0 | O2, H4 | FS-11 |
| US-17 | En tant que professionnel sur ordinateur, je veux une application desktop légère qui s'ouvre vite, afin de rester dans le fil sans attendre un navigateur | L'ouverture rapide évite une attente perceptible avant la découverte | P0 | O2, H1 | FS-01, FS-11 |

US-17 concerne l'application exécutable Windows et macOS ; FS-01 définit le fil sans compte et FS-11 fournit les événements d'observation, dont `app_open`. Aucune autre histoire du backlog n'est priorisée différemment.

US-06 ne promet pas de fil personnalisé : la sauvegarde est un geste volontaire du membre, limité à la session pour le visiteur, et aucune recommandation n'utilise un historique conservé au MVP. La règle de sous-titres D-021 est écrite dans le [parcours B](./userflow.md), à la préparation de la vidéo et à la modération.

## Phase 2, emploi et pages gratuites

| Identifiant | Histoire | Pourquoi | Priorité | Opportunité ou hypothèse | Lien PRD |
|---|---|---|---|---|---|
| US-12 | En tant que demandeuse d'organisation, je veux faire vérifier mon entité, afin d'ouvrir une page publique crédible | La vérification précède l'autorité publique | P1, hors sprint MVP | O1, H2 | Section 14.3 |
| US-13 | En tant que propriétaire, je veux créer une page département ou antenne, afin de représenter chaque équipe | Toutes les pages ont les mêmes capacités | P1, hors sprint MVP | O1, H2 | Section 14.1 |
| US-14 | En tant que propriétaire, je veux nommer un administrateur, afin de répartir la gestion sans partager de mot de passe | Les rôles sont propres à chaque page | P1, hors sprint MVP | O5, H6 | Section 14.2 |
| US-15 | En tant que recruteur, je veux publier une offre au nom d'une page, afin d'atteindre les personnes qui ont vu le travail de l'équipe | Les offres arrivent avec la phase emploi | P1, hors sprint MVP | O4, H5 | Section 14 |
| US-16 | En tant que membre vérifié, je veux postuler avec un dossier, afin que l'employeur sache qui je suis | La règle N2 est cadrée par D-010 | Non priorisée, D-010 retenue | O4, H5, selon D-010 | Section 13 |

US-16 reste sans priorité dans le MVP, D-010 étant retenue au [registre](../Product/decisions.md). Le recruteur et les candidatures sont hors MVP.

## Règles d'écriture d'une nouvelle histoire

1. Commencer par « En tant que », puis préciser le rôle réel, pas un personnage fictif.
2. Dire l'action, puis le bénéfice observable.
3. Renseigner la colonne Opportunité ou hypothèse avec O1 à O5 ou H1 à H9. Une histoire sans identifiant n'entre pas dans un sprint.
4. Vérifier la limite du dénominateur associé dans [ux-research.md](./ux-research.md) avant d'écrire un seuil.
5. Ajouter les critères d'acceptation dans le PRD, pas ici, pour garder une seule source de vérité.
6. Ne pas transformer une décision retenue en priorité : D-010 et D-011 restent hors sprint ; D-009 est retenue et n'entre pas dans une histoire sans FS rattachée.
