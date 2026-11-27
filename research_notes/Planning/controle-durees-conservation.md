# Fiche de contrôle des durées de conservation

**Statut** : préparée le 27 novembre 2026, aucun test de purge exécuté, aucune durée ajoutée, aucune porte levée  
**Sources canoniques** : [Conservation](../../docs/Conformite/conservation.md), [D-015 au registre](../../docs/Product/decisions.md), [Modèle de décision des agrégats](../Sprint-1/decision-conservation-agregats.md), [Confidentialité du visiteur](../../docs/Conformite/confidentialite-visiteur.md), [Dictionnaire de mesures](../../docs/Product/mesure.md), [PRD, section 10](../../docs/Product/prd.md), [Droit congolais](../../docs/Conformite/droit-congolais.md)  
**Règle** : cette fiche prépare le contrôle des durées écrites. Elle n'exécute aucun test, ne confirme aucune durée proposée et ne lève aucune porte.

## 1. Ce qui est déjà écrit

La fiche conservation est la source unique de la politique de conservation. `donnees.md` en est la traduction technique et ne fixe aucune durée nouvelle. D-015 fixe à 30 jours la conservation des événements de session, sans modification ici. Le modèle de décision des agrégats prépare la durée et la finalité à inscrire avant la première mesure, sans valeur préremplie.

La table de conservation porte des durées écrites et des durées en attente. `analytics_event` est à 30 jours, avec purge quotidienne journalisée. `guest_session` est à 15 minutes, à confirmer. Une vidéo `published` est conservée jusqu'au retrait ou à la suppression du compte. Une vidéo `removed` est conservée 30 jours après le retrait, le temps de la contestation. `appeal` est à 30 jours, à confirmer. `push_subscription` et le profil public d'un compte supprimé sont effacés immédiatement. Les messages et signalements portent « à trancher », sans suppression automatique avant arbitrage. Le journal d'audit est « à confirmer par conseil local ». Aucune obligation locale n'est affirmée dans cette fiche et toute exception est écrite avec texte source, pays, date, propriétaire à nommer et objet concerné.

Le test de purge vérifie qu'aucun `analytics_event` n'excède trente jours, qu'aucun objet vidéo retiré ne reste après le délai retenu et qu'aucune ligne de contestation expirée n'est consultable. Il est joué sur `mobile`, `web` et `desktop`, avec la dimension `plateforme` en lecture, sans changer les durées. Les durées marquées « à confirmer » ne sont pas appliquées comme des faits juridiques. Aucun résultat de purge, aucun horodatage, aucune exception écrite et aucun propriétaire nommé ne sont fournis ici.

## 2. Points à contrôler

Chaque ligne reste à renseigner au moment du contrôle. Aucune durée n'est confirmée par cette fiche.

| Point à contrôler | Ce qui est déjà écrit | Preuve à archiver | État |
|---|---|---|---|
| `analytics_event` | 30 jours, D-015 inchangée, purge quotidienne journalisée | À renseigner, extrait de purge daté sans résultat prérempli | En attente de contrôle |
| `guest_session` | 15 minutes, à confirmer | À renseigner, durée retenue à écrire, sans valeur préremplie | En attente de contrôle |
| Vidéo `published` | Jusqu'au retrait ou à la suppression du compte | À renseigner, état daté sans référence réelle préremplie | En attente de contrôle |
| Vidéo `removed` | 30 jours après le retrait, temps de la contestation | À renseigner, extrait du journal daté | En attente de contrôle |
| `appeal` | 30 jours, à confirmer, empreinte conservée selon la règle retenue | À renseigner, sans texte de contestation prérempli | En attente de contrôle |
| `push_subscription` | Suppression immédiate à la révocation ou à la suppression du compte | À renseigner, trace datée sans jeton réel | En attente de contrôle |
| Profil public | Suppression immédiate pour compte `deleted` | À renseigner, trace datée sans identifiant réel | En attente de contrôle |
| Messages et signalements | À trancher avec le conseil local, aucune suppression automatique | À renseigner, arbitrage écrit ou aucun | En attente de contrôle |
| Journal d'audit | À confirmer par conseil local, ajout seul, masquage des données personnelles | À renseigner, sans confirmation préremplie | En attente de contrôle |
| Exceptions documentées | Texte source, pays, date, propriétaire à nommer, objet | À renseigner, aucune exception préremplie | En attente de contrôle |
| Test de purge par client | `mobile`, `web` et `desktop`, lecture par `plateforme` | À renseigner séparément par client, sans transfert de preuve | En attente de contrôle |

## 3. Champs à remplir au moment du contrôle

| Champ | Valeur |
|---|---|
| Date du contrôle | À renseigner |
| Objet concerné | À renseigner depuis la table de conservation |
| Ville concernée | À renseigner, sans transposition |
| Plateforme concernée | À renseigner pour `mobile`, `web` ou `desktop` |
| Durée appliquée | À renseigner, seules les durées écrites sont rappelées |
| Durée à confirmer | À renseigner, sans valeur préremplie |
| Résultat du test de purge | À renseigner, aucun résultat prérempli |
| Exception éventuelle | À renseigner avec texte source, pays, date et propriétaire, ou aucune |
| Propriétaire de l'exception | À renseigner |
| Propriétaire du compte rendu | À renseigner |
| Approbateur nommé | À renseigner |
| Décision écrite au registre | À renseigner avec date et portée, ou aucune |
| Archive et historique | À renseigner |
| État | En attente de contrôle |

Une durée marquée « à confirmer » n'est pas appliquée comme un fait. Une purge sans trace datée n'est pas une preuve. Aucune durée n'est modifiée et aucune obligation locale n'est affirmée par cette fiche.

## 4. Distinctions à conserver

Un contrôle de conservation ne modifie pas D-015, ne remplace pas le modèle de décision des agrégats, ne retient aucune opportunité O, ne valide aucune hypothèse H1 à H8, ne nomme aucun propriétaire de validation, ne transpose pas une ville vers l'autre, ne modifie pas les durées de la fiche conservation, ne fixe pas de date de lancement selon A-05 et ne lève aucune porte.

La lecture par `plateforme` n'ajoute aucune durée propre à un client. Une preuve lue sur `web` ne dispense pas de la preuve attendue sur `desktop` ou sur `mobile`. Le silence d'une exception n'en crée aucune. Aucun conseil local n'est désigné ici.

## 5. Ce que cette fiche ne fait pas

Elle n'exécute aucun test de purge, ne confirme aucune durée, n'écrit aucune exception, ne nomme aucun propriétaire ni conseil, ne modifie aucune décision, ne lève A-12, ne lève aucune porte et ne contient aucun code applicatif.
