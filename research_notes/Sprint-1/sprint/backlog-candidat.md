# Backlog candidat du sprint 1

**Statut** : préparé le 26 novembre 2026, sélection finale en attente  
**Règle** : un sprint traite une seule opportunité O1 à O5, selon la section 12 de la [recherche UX](../../docs/UX/ux-research.md). La Phase 0 n'a pas encore écrit l'opportunité retenue. Ce tableau est donc un candidat, pas un sprint figé.

Aucune histoire n'entre dans le sprint sans identifiant O1 à O5 ou H1 à H9, conformément au [backlog canonique](../../docs/UX/userstories.md). Les critères d'acceptation restent dans le [PRD](../../docs/Product/prd.md), section 7. Ce fichier ne les recopie pas. La [grille de validation de la condition 1](./grille-validation-criteres-FS.md) porte les preuves à archiver par FS et par plateforme, sans recopier les critères ni case cochée.

## Histoires P0 classées par opportunité

| Opportunité | Histoire | Spécification | Pourquoi | Dépendance de Phase 0 |
|---|---|---|---|---|
| O1, croire ce que l'on voit | US-04, profil public lisible sans compte | FS-04, section 7 | L'identité est visible avant le contact | Résultat de H2 |
| O1, croire ce que l'on voit | US-05, publication avec sous-titres corrigés | FS-05, section 7, D-021 | La preuve de travail reste publiable sans audio | Résultat de H2 et H6 |
| O2, données demandées trop tôt | US-01, fil sans compte | FS-01, section 7 | La découverte précède l'identification | Résultat de H1 |
| O2, données demandées trop tôt | US-10, notification d'une réponse ou d'une décision | FS-10, section 7 | Le retour sert la conversation, pas l'engagement artificiel | Résultat de H4 |
| O2, données demandées trop tôt | US-11, événements propres | FS-11, section 7 | Mesurer sans identifiant permanent visiteur | Dénominateur de H4 |
| O3, par où commencer | US-03, choix du métier et de la ville | FS-03, section 7 | Le fil proche suit le premier réflexe | Résultat de H3 |
| O3, par où commencer | US-06, interactions sociales | FS-06, section 7 | Geste volontaire, sans historique conservé | Résultat de H3 |
| O3, par où commencer | US-08, recherche sans inscription | FS-08, section 7 | La recherche sert la découverte | Résultat de H3 |
| O4, peur du faux recruteur | US-07, chat 1:1 | FS-07, section 7 | Le message est la sortie du parcours | Résultat de H5 |
| O4, peur du faux recruteur | US-09, signalement | FS-09, section 7 | La confiance exige une voie de recours | Résultat de H5 |
| O5, exposition à l'employeur | US-02, envoyer une vidéo depuis le téléphone | FS-02, section 7 | La preuve de travail doit être simple à produire | Résultat de H7 |

## Histoires transversales

| Histoire | Périmètre | Règle |
|---|---|---|
| US-17, client desktop | FS-01 et FS-11 | Windows et macOS livrés avec `mobile` et `web`. Aucun binaire natif pour les six catégories de A-13. Aucune valeur de performance présentée comme mesurée avant la revue A-03. |
| FS-11, événements | [Dictionnaire des mesures](../../docs/Product/mesure.md) | Émis sur les trois plateformes, avec `plateforme`, `city`, `trade` et `campaign_ref` distincts. Aucun identifiant permanent visiteur. |

## Règle de sélection à J10

1. Lire l'opportunité O écrite dans le compte rendu de J10 et son identifiant.
2. Retenir les histoires du tableau qui portent cet identifiant.
3. Ajouter US-17 et l'instrumentation FS-11 nécessaire aux mesures de cette opportunité.
4. Laisser toutes les autres histoires au backlog de Phase 1, sans les supprimer.
5. Vérifier chaque histoire retenue avec la [définition de prêt](./definition-of-ready.md) avant le premier commit.

Aucune sélection n'est écrite ici. Aucun nouveau seuil, aucune nouvelle histoire et aucune priorité différente de P0 ne sont introduits. Les histoires US-12 à US-16 restent en Phase 2, hors sprint MVP.
