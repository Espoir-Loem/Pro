# Vérification d'identité, niveau N2

**Source primaire.** [PRD section 3.2 et section 14](../Product/prd.md), décision D-010 dans [decisions.md](../Product/decisions.md), [EDPB 4/2019](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201904_dataprotection_by_design_and_by_default_v2.0_en.pdf) pour la minimisation des données de vérification.
**Propriétaire de validation.** à nommer. **Statut.** proposée, dépend d'un arbitrage. **Date.** 25 novembre 2026.

## Portée

La vérification d'identité N2 n'est pas dans le MVP. En phase 1, seule l'adresse email est vérifiée, avec l'événement `signup_verified`. La méthode N2 est décrite par la décision D-010, retenue le 26 novembre 2026 dans le registre produit : vérification à la demande de l'employeur, avec l'email vérifié comme seule preuve. Ce document n'ajoute pas de méthode.

## Ce que le badge peut et ne peut pas dire

| Le badge peut dire | Le badge ne peut pas dire |
|---|---|
| Une méthode définie a été suivie à une date enregistrée | Que la personne est digne de confiance |
| Le contrôle a été fait pour un usage professionnel précis | Que Pro a vérifié un employeur, sauf preuve distincte |
| La vérification peut être retirée et le badge révoqué | Que la vérification est permanente |

Aucune affirmation de valeur juridique locale n'est attachée au badge. Si un usage impose une preuve supplémentaire, la règle est ajoutée ici avec sa source et son pays, après validation par conseil local.

## Données et réversibilité

Les données de vérification sont minimales: méthode, date, résultat et référence de révocation. Le badge est réversible : une demande de retrait ou une décision de modération le retire sans réécrire l'historique, par une nouvelle ligne datée. La suppression des données de vérification suit [conservation.md](conservation.md).

## Déclencheur et vérification

Cette fiche est relue avant la phase emploi et tient compte de D-010, inscrite au registre le 26 novembre 2026. Un test vérifie qu'aucun badge N2 n'est affiché dans le MVP et que `signup_verified` ne produit pas de badge.
