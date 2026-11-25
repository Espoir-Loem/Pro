# Avenant au rapport d'audit : élargissement de Pro à trois clients

**Date.** 25 novembre 2026.

**Objet.** Contrôle final de l'élargissement de Pro aux clients `mobile`, `web` et `desktop`.

**Périmètre.** Uniquement `docs/`. Les rapports historiques de `reports/` n'ont pas été réécrits ; le présent avenant y est ajouté.

## Demande du porteur

Le porteur demande la livraison conjointe en Phase 1 de trois clients, selon D-004 révisée et D-023 du 25 novembre 2026. Le client `desktop` est une application exécutable Windows et macOS, légère et rapide, sans attente perceptible. La référence de rapidité citée est celle d'une messagerie légère, sans chiffre recopié ni résultat revendiqué. Le porteur n'impose ni langage, ni cadre applicatif, ni outil d'empaquetage. Linux reste différé et non spécifié en phase 1.

## Définition canonique des trois plateformes

Source : `docs/Product/prd.md`, section 2. La même définition est reprise dans les documents produit, technique, UX et conformité.

- `mobile` : applications natives iOS et Android sur téléphone.
- `web` : site responsive dans un navigateur, utilisé sur ordinateur et tablette.
- `desktop` : application exécutable installée sur Windows et macOS. Linux est différé et non spécifié en phase 1.

Aucune mesure ne fusionne ces valeurs sans le dire. Un agrégat est nommé explicitement « toutes plateformes ». Les dimensions `city`, `trade` et `campaign_ref` restent distinctes de `plateforme`.

## Tableau des contrôles

| N. | Contrôle | Attendu | Résultat | Correction |
|---|---|---|---|---|
| 1 | Recherche des tirets longs et demi-cadratins dans `docs` | Vide | Conforme | Aucune |
| 2 | Recherche des plages CJK dans `docs` | Vide | Conforme | Aucune |
| 3 | Recherche des marqueurs temporaires dans `docs` | Vide | Conforme | Aucune |
| 4 | Recherche des formulations réduisant le périmètre à deux clients | Vide | Non conforme avant correction : 35 occurrences dans 15 fichiers | 35 occurrences remplacées par la notation canonique à valeurs codées |
| 5 | Résolution des liens relatifs depuis leur fichier | Zéro lien cassé | Conforme : 420 liens résolus, 0 cassé | Aucune |
| 6 | Numérotation FS, US et D | FS-01 à FS-11, US-01 à US-17, D-001 à D-023, sans saut | Conforme | Aucune |
| 7 | `client_desktop` dans `docs/Technique/architecture.md` | Présence et relations vers lecture et écriture | Conforme : relations `Lit` et `Ecrit` présentes | Aucune |
| 8 | Cibles desktop dans `docs/Technique/performance.md` et `docs/Product/prd.md` | Démarrage à froid, changement de vue, première image vidéo, mémoire au repos, installateur ; aucune valeur mesurée | Conforme : cinq cibles marquées à confirmer | Aucune |
| 9 | Dimension `plateforme` dans les cinq fichiers désignés | Valeurs `mobile`, `web`, `desktop` | Conforme dans les cinq fichiers | Aucune |
| 10 | D-004 révisée et D-023 | Date, motif, source, portée, historique | Conforme | Aucune |
| 11 | US-17 et phrase canonique dans `docs/UX/userflow.md` | Présence | Conforme | Aucune |
| 12 | Blocs Mermaid | Tous fermés | Conforme : 12 fichiers concernés, aucun bloc ouvert | Aucune |

Le point 9 couvre `docs/Product/mesure.md`, `docs/Product/tableau-de-bord.md`, `docs/Technique/donnees.md`, `docs/Technique/observation.md` et `docs/Growth/mesure-campagnes.md`.

## Corrections appliquées

- 35 occurrences de l'ancienne énumération à deux termes remplacées par la notation canonique à valeurs codées dans les fichiers suivants : `docs/README.md`, `docs/Product/manifeste.md`, `docs/Product/tableau-de-bord.md`, `docs/Product/prd.md`, `docs/Product/experimentation.md`, `docs/Product/roadmap.md`, `docs/Product/vision.md`, `docs/Product/mesure.md`, `docs/Product/decisions.md`, `docs/Technique/README.md`, `docs/Technique/responsabilites.md`, `docs/Technique/api.md`, `docs/Technique/adr-001-stack.md`, `docs/UX/ux-research.md` et `docs/Growth/README.md`.
- `docs/Growth/README.md` : libellé Mermaid normalisé en `mobile / web / desktop`.
- `docs/Technique/adr-001-stack.md` : phrase restructurée pour expliciter les trois clients sans abréviation à deux termes.

Aucune autre correction n'a été nécessaire. Aucun rapport historique n'a été modifié.

## Fichiers vérifiés

58 fichiers sous `docs/` :

- Racine : `docs/README.md`.
- `docs/Conformite/` : `confidentialite-visiteur.md`, `conservation.md`, `droit-congolais.md`, `moderation-regles.md`, `organisation-verification.md`, `perimetre-juridique.md`, `README.md`, `union-europeenne.md`, `verification-identite.md`.
- `docs/Growth/` : `acquisition-brazzaville.md`, `acquisition-kinshasa.md`, `extension-afrique.md`, `lanceurs-metiers.md`, `mesure-campagnes.md`, `partenariats.md`, `phrases-invitation.md`, `README.md`.
- `docs/Operations/` : `animation-createurs.md`, `astreinte.md`, `contestation.md`, `incidents.md`, `journee-type-moderation.md`, `moderation-manuel.md`, `montee-en-charge.md`, `README.md`, `support.md`, `veille-arnaque.md`.
- `docs/Product/` : `decisions.md`, `experimentation.md`, `manifeste.md`, `mesure.md`, `prd.md`, `roadmap.md`, `tableau-de-bord.md`, `vision.md`.
- `docs/Redaction/` : `ia-defauts-et-tips.md`.
- `docs/Technique/` : `adr-001-stack.md`, `adr-002-identite-session.md`, `adr-003-porte-publication.md`, `api.md`, `architecture.md`, `donnees.md`, `menaces.md`, `observation.md`, `performance.md`, `README.md`, `responsabilites.md`, `securite.md`, `video.md`.
- `docs/UX/` : `design-principles.md`, `journey-map.md`, `personas.md`, `referentiel-recherche.md`, `userflow.md`, `userstories.md`, `usertories.md`, `ux-research.md`.

## Décisions ouvertes restantes

| Identifiant | Question ouverte | Phase |
|---|---|---|
| D-009 | Stack à trancher dans un ADR unique | Phase 1, avant le premier sprint |
| D-010 | Règle N2 : vérification du profil pour toutes les candidatures ou à la demande de l'employeur | Phase 2, hors MVP |
| D-011 | Nom et privilèges du niveau organisations payant | Phase 5 |
| D-022 | Budget CDN et modération, avec seuil de coût par vue | Phase 3 |

Autres arbitrages signalés sans inscription au registre : application du RGPD au démarrage dans les deux Congo (`docs/Conformite/perimetre-juridique.md`), plafond éventuel de lecture et son seuil (`docs/Product/prd.md`, section 10), date de lancement et modèle bénévole ou salarié de la modération (`docs/Product/prd.md`, section 13). Les cibles desktop et le profil R2 restent à confirmer avant le sprint 1 (`docs/Product/prd.md`, section 9.1 ; `docs/Technique/performance.md`).

## Conclusion

Verdict final : conforme après correction. Les douze contrôles sont satisfaits. Les seules modifications apportées à `docs/` portent sur la formulation des trois plateformes. Les rapports historiques sont intacts et le présent avenant est le seul fichier créé dans `reports/`. Les décisions ouvertes listées restent hors sprint jusqu'à leur arbitrage.
