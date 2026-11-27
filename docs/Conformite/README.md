# Conformité : périmètre, confidentialité et preuves

**Métier.** Juridique, confidentialité et sûreté.
**Source primaire.** Textes listés dans chaque fiche, sans obligation locale affirmée avant validation par conseil.
**Propriétaire de validation.** à nommer. **Statut.** socle rédigé, à valider. **Date.** 25 novembre 2026.
**Règle.** Ne pas affirmer une obligation locale sans source vérifiée par un conseil du pays concerné. Chaque fiche porte Source primaire, Propriétaire de validation, Statut et Date.

## Glossaire des phases

Phase 1 est le MVP. Phase 2 introduit les organisations et pages. La phase emploi introduit la vérification N2 et les candidatures, selon la décision D-010 retenue le 26 novembre 2026 dans [decisions.md](../Product/decisions.md). Une ouverture dans l'Union européenne est une éventualité distincte, non une phase du démarrage.

| Fiche | Question traitée | Déclencheur | Dépendances | Propriétaire | Statut |
|---|---|---|---|---|---|
| [perimetre-juridique.md](perimetre-juridique.md) | Pays, établissement, droit applicable, région de stockage | Avant `adr-001-stack.md` et la première migration | [PRD](../Product/prd.md), conseil local à nommer | à nommer | proposée, conseil à nommer |
| [confidentialite-visiteur.md](confidentialite-visiteur.md) | Session courte, aucun identifiant permanent, aucun traceur tiers | Avant mise en ligne du fil public | [Technique/adr-002-identite-session.md](../Technique/adr-002-identite-session.md) | à nommer | proposée |
| [conservation.md](conservation.md) | Durées par objet, vidéos retirées, comptes supprimés | Avant la première migration | [PRD](../Product/prd.md), conseil local à nommer | à nommer | proposée, valeurs à confirmer |
| [moderation-regles.md](moderation-regles.md) | Motifs, priorités, actions, contestation | Avant FS-09 | [Opérations](../Operations/README.md), [union-europeenne.md](union-europeenne.md) | à nommer | proposée |
| [verification-identite.md](verification-identite.md) | Portée de N2, limites du badge, réversibilité | Avant la phase emploi | D-010 dans [decisions.md](../Product/decisions.md) | Espoir LOEMBA, intérimaire | opposée, conforme à D-010 |
| [organisation-verification.md](organisation-verification.md) | Domaine, document légal, révocation N3 | Avant la phase 2 | [PRD](../Product/prd.md) section 14 | à nommer | proposée |
| [union-europeenne.md](union-europeenne.md) | Articles DSA visés sous condition | Avant toute ouverture européenne | [perimetre-juridique.md](perimetre-juridique.md) | à nommer | proposée, conditionnelle |
| [droit-congolais.md](droit-congolais.md) | Points à valider pour Brazzaville et Kinshasa | Avant le lancement dans chaque pays | conseil local à nommer | à nommer | proposée, sources à collecter |

## Liens de cadrage

[PRD](../Product/prd.md), [dictionnaire de mesures](../Product/mesure.md), [registre des décisions](../Product/decisions.md), [parcours UX](../UX/userflow.md), [Opérations](../Operations/README.md).

## Première action

Faire valider `perimetre-juridique.md` par un conseil local, puis nommer les propriétaires de validation. La [fiche de contrôle des durées de conservation](../../research_notes/Planning/controle-durees-conservation.md) prépare la vérification des durées déjà écrites, sans confirmation avancée. La stack est retenue en D-009 et décrite dans `../Technique/adr-001-stack.md`. Tant que cette validation manque, aucun hébergeur ni région de stockage n'est arrêté et la première migration est différée. Aucune affirmation de droit congolais n'est ajoutée entre-temps.
