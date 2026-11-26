# Pro : principes de design

**Statut** : version 3, 26 novembre 2026  
**Usage** : ces principes sont opposables en revue d'interface. Toute déviation est écrite avec son motif, sa date et son propriétaire dans le registre de décisions.  
**Documents liés** : [Décisions](../Product/decisions.md), [Recherche UX](./ux-research.md), [Parcours](./userflow.md), [Grille de relecture](../Redaction/ia-defauts-et-tips.md)

La page Apple *Design principles* donne huit principes généraux. Six servent ici de grille de critique : finalité, liberté d'action, responsabilité, familiarité, souplesse et plaisir. Ils ne sont pas recopiés comme règles Pro. Les principes ci-dessous sont propres au produit et se vérifient sur un écran précis.

## 1. Voir avant de s'identifier

**Énoncé.** Trois vidéos sont consultables avant toute demande de compte. Le premier geste social explique en une phrase pourquoi l'identité est utile, puis demande seulement l'email. Les suggestions de métier et de ville restent modifiables.

**Contre-exemple.** Un écran de bienvenue plein cadre avec formulaire complet dès l'ouverture, ou une sauvegarde locale qui déclenche un profil à remplir avant d'afficher la vidéo.

**Lien.** [D-001](../Product/decisions.md), [O2](./ux-research.md), H4.

## 2. La preuve de travail avant le badge

**Énoncé.** Le geste visible, le métier affiché et la ville constituent la preuve principale. Le badge lié à l'email vérifié reste discret et ne remplace pas la vidéo.

**Contre-exemple.** Un badge « vérifié » mis en avant sur un profil sans vidéo, ou une vignette soignée dont le geste de travail est invisible.

**Lien.** [O1](./ux-research.md), H2, D-001.

## 3. L'identité au geste social

**Énoncé.** La fenêtre de composition affiche qui écrit et à qui, avant le premier caractère. Aucun CV n'est demandé au MVP. Le signalement et le blocage restent accessibles dans la conversation.

**Contre-exemple.** Une fenêtre de message ouverte avec un pseudonyme seul, ou un bouton « Envoyer » actif vers soi-même.

**Lien.** [O4](./ux-research.md), H5, FS-07 du [PRD](../Product/prd.md).

## 4. Session courte, identifiant nul

**Énoncé.** Le visiteur garde ses choix de métier et de ville le temps de la session seulement. Aucun identifiant permanent, aucune empreinte d'appareil et aucun traceur tiers ne sont introduits pour le visiteur.

**Contre-exemple.** Un cookie durable posé au premier chargement, ou un événement visiteur rattaché au compte créé plus tard sans règle explicite.

**Lien.** [D-012](../Product/decisions.md), [O2](./ux-research.md), FS-11 du [PRD](../Product/prd.md).

## 5. Sous-titres corrigés avant publication

**Énoncé.** Toute vidéo avec son du MVP dispose de sous-titres générés automatiquement et corrigés par l'auteur. Sans correction, la vidéo reste en brouillon et n'est pas publiée. Le contrôle est répété en modération.

**Contre-exemple.** Une vidéo avec son publiée avec des sous-titres automatiques non relus, ou une file de modération qui valide le son sans vérifier les sous-titres.

**Lien.** D-021 dans le [registre](../Product/decisions.md), [parcours B](./userflow.md), [O1](./ux-research.md).

## 6. Accessibilité par défaut

**Énoncé.** Le site web vise WCAG 2.2 AA. Chaque cible web mesure au moins 24 sur 24 CSS px, avec 44 pixels comme objectif au delà du minimum. Lecteur d'écran, ordre de focus et contraste sont vérifiés avant revue de code. La lecture automatique respecte le mouvement réduit. L'application desktop suit les directives natives de Windows et macOS : API natives, ordre de focus clavier et souris, contraste, mouvement réduit et taille de cible. WCAG n'est pas présenté comme une règle directe pour une application native.

**Contre-exemple.** Une cible de 20 pixels, un ordre de focus qui saute la correction des sous-titres, une vidéo qui démarre malgré la préférence de mouvement réduit, ou un écran desktop qui transpose WCAG comme cahier des charges natif.

**Lien.** Section 10 du [PRD](../Product/prd.md), [O1](./ux-research.md), [parcours A](./userflow.md).

## 7. Pas de personnalisation par historique

**Énoncé.** Le fil dépend du métier et de la ville choisis dans la session, ou de la vidéo en cours. Aucun historique conservé ne sert à recommander une personne au MVP.

**Contre-exemple.** Une section «vous aimerez aussi » calculée à partir des vidéos vues la semaine précédente, ou un fil trié par un score opaque.

**Lien.** Section 3.2 du [PRD](../Product/prd.md), [O3](./ux-research.md), H3.

## 8. Toute sanction est tracée et contestable

**Énoncé.** Une action de modération porte un motif, une date et un acteur. L'auteur reçoit une notification avec un lien de contestation par email relié au ticket d'origine. Le signalant visiteur reste pseudonyme.

**Contre-exemple.** Une vidéo retirée sans motif visible, ou une contestation par simple lien public sans rattachement au ticket.

**Lien.** [O4](./ux-research.md), [parcours D](./userflow.md), FS-09 du [PRD](../Product/prd.md).

## 9. Réactivité sans attente perceptible

**Énoncé.** Sur application mobile, site web ou application desktop, aucun geste n'entraîne d'attente perceptible avant un retour visible. Chaque geste reçoit un feedback immédiat, y compris quand le résultat arrive plus tard. Aucun chargement spéculatif inutile n'est déclenché pour devancer un geste que la personne n'a pas fait. L'application desktop s'ouvre sur le fil sans écran d'attente, comme l'exige US-17 dans les [histoires utilisateur](./userstories.md). Les cinq cibles de revue du desktop sont arrêtées le 26 novembre 2026 par A-03, sur machine modeste, avec revue prévue le 26 décembre 2026 ; aucune valeur n'est présentée comme mesurée.

**Contre-exemple.** Un bouton qui reste sans réponse après un appui, un écran de démarrage desktop avant le fil, ou un préchargement large lancé au lancement sans lien avec le geste suivant.

**Lien.** FS-01 et FS-11 du [PRD](../Product/prd.md), [O2](./ux-research.md), [US-17](./userstories.md), [parcours A](./userflow.md), A-03 de l'[arbitrage](../Product/arbitrage.md), [performance](../Technique/performance.md).

## 10. Une correction n'attend pas le store

**Énoncé.** Sur application mobile, site web ou application desktop, une correction peut être livrée sans dépendre d'un cycle de validation de store quand le changement est servi hors binaire natif. Le web change à la navigation suivante, le desktop applique un paquet signé au redémarrage ou au lancement suivant, et le mobile suit les six catégories fermées arbitrées le 26 novembre 2026 au point A-13 de la [grille d'arbitrage](../Product/arbitrage.md) : règles, contenus, textes et traductions, taxonomies, indicateurs de fonctionnalité et valeurs de configuration. Aucun code exécutable n'est téléchargé. Aucune mise à jour ne coupe une session en cours, ne crée d'identifiant d'appareil et ne modifie une décision de modération sans trace.

**Contre-exemple.** Un utilisateur qui attend une validation externe pour voir une correction de règles, une mise à jour desktop installée sans vérification de signature, ou une session interrompue au milieu d'un message.

**Lien.** D-024 dans le [registre](../Product/decisions.md), section 10.1 du [PRD](../Product/prd.md), [sécurité](../Technique/securite.md), A-13 de l'[arbitrage](../Product/arbitrage.md).

## Revue d'interface

En revue, chaque écran est parcouru avec les dix principes. Une réponse « conforme » sans fait observable ne suffit pas : la personne qui relit nomme l'élément vérifié et l'état du parcours correspondant. Une déviation acceptée est inscrite au [registre](../Product/decisions.md) avec date, motif et portée. Le vocabulaire et la mise en forme suivent la [grille de relecture](../Redaction/ia-defauts-et-tips.md), appliquée à tous les documents de `docs`.
