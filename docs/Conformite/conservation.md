# Conservation des données

**Source primaire.** [RGPD article 5](https://eur-lex.europa.eu/eli/reg/2016/679/oj) pour la limitation de conservation, [PRD section 10](../Product/prd.md) pour les trente jours d'événements.
**Propriétaire de validation.** à nommer. **Statut.** proposée, valeurs à confirmer. **Date.** 25 novembre 2026.
**Portée.** Cette fiche est la source unique de la politique de conservation. [../Technique/donnees.md](../Technique/donnees.md) en est la traduction technique et ne fixe aucune durée nouvelle. Les durées et les règles valent pour les trois plateformes de la dimension `plateforme` : `mobile` pour les applications natives iOS et Android, `web` pour le navigateur, `desktop` pour l'application exécutable Windows et macOS, rapide, sans lenteur. Linux est différé. Cette extension de périmètre ne modifie aucune durée ni aucune décision déjà prise, sous réserve des arbitrages de [decisions.md](../Product/decisions.md). La lecture des événements conservés reste celle de [mesure.md](../Product/mesure.md).

| Objet | Déclencheur | Durée proposée | Motif | Propriétaire de l'exception | Mécanisme d'exécution |
|---|---|---|---|---|---|
| `analytics_event` | Horodatage de l'événement | 30 jours | Mesure d'audience sans identifiant permanent | à nommer | Purge quotidienne journalisée |
| `guest_session` | Création du jeton | 15 minutes, à confirmer | Session visiteur courte | à nommer | Expiration et rotation du jeton |
| Vidéo `published` | Publication | Jusqu'au retrait ou à la suppression du compte | Contenu public | à nommer | Suppression de l'objet et du manifeste |
| Vidéo `removed` | Décision de retrait | 30 jours après le retrait, le temps de la contestation écrite dans [contestation.md](../Operations/contestation.md) | Possibilité de recours | à nommer | Suppression après expiration de `appeal` |
| `appeal` | Décision rendue | 30 jours, à confirmer | Preuve de traitement de la contestation | à nommer | Purge du texte, empreinte conservée selon la règle retenue |
| `push_subscription` | Révocation ou suppression du compte | Suppression immédiate | Jeton fournisseur lié au compte | à nommer | Révocation auprès du fournisseur |
| Profil public | Compte `deleted` | Suppression immédiate | Retrait du contenu public | à nommer | Masquage puis suppression |
| Messages et signalements | Suppression du compte | à trancher | À définir avec le conseil local | à nommer | Aucune suppression automatique avant arbitrage |
| Journal d'audit | Écriture de la ligne | à confirmer par conseil local | Traçabilité des décisions | à nommer | Ajout seul, masquage des données personnelles |

## Exceptions documentées

La formule « sauf obligation légale contraire documentée » n'est pas une porte ouverte. Toute exception est écrite ici avec texte source, pays, date, propriétaire à nommer et objet concerné. Aucune obligation locale n'est affirmée dans cette fiche : voir [droit-congolais.md](droit-congolais.md).

## Vérification

Un test de purge vérifie qu'aucun `analytics_event` n'excède trente jours, qu'aucun objet vidéo retiré ne reste après le délai retenu et qu'aucune ligne de contestation expirée n'est consultable. Le test est joué sur `mobile`, `web` et `desktop`, avec la dimension `plateforme` en lecture, sans changer les durées ci-dessus. Les durées marquées « à confirmer » ne sont pas appliquées comme des faits juridiques. La [fiche de contrôle des durées de conservation](../../research_notes/Planning/controle-durees-conservation.md) prépare ces vérifications, sans test exécuté ni durée ajoutée.
