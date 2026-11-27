# Fiche de contrôle des phrases d'invitation et des campagnes d'acquisition

**Statut** : préparée le 27 novembre 2026, aucune campagne lancée, aucune phrase retenue, aucun validateur nommé, aucune porte levée  
**Sources canoniques** : [Phrases d'invitation](../../docs/Growth/phrases-invitation.md), [Mesure des campagnes](../../docs/Growth/mesure-campagnes.md), [Acquisition Brazzaville](../../docs/Growth/acquisition-brazzaville.md), [Acquisition Kinshasa](../../docs/Growth/acquisition-kinshasa.md), [D-019 au registre](../../docs/Product/decisions.md), [A-05 au registre des arbitrages](../../docs/Product/arbitrage.md), [Dictionnaire de mesures](../../docs/Product/mesure.md)  
**Règle** : cette fiche prépare le contrôle des phrases et de la mesure des campagnes. Elle ne lance aucune campagne, ne retient aucune phrase, ne nomme aucun validateur et ne lève aucune porte.

## 1. Ce qui est déjà écrit

La liste des promesses interdites est fermée : emploi garanti, salaire garanti, vérification N2 au MVP, classement payant, offres d'emploi au MVP. Aucune autre promesse ne peut être ajoutée sans décision écrite au registre. D-019 interdit tout classement payant dans la recherche. Trois phrases autorisées sont écrites, sans promesse d'embauche, et valent pour `mobile`, `web` et `desktop`. La validation est distincte par ville : la phrase exacte, le validateur et la date sont écrits dans le canal de campagne de la ville. Une phrase validée à Brazzaville n'est pas valable à Kinshasa sans validation distincte.

Les fiches d'acquisition portent chacune leur cible propre, vérifiée avec `video_published` et le champ `city`. Aucune prévision n'est reprise d'une ville vers l'autre. Si un métier pilote n'a pas de vidéo modérée, le fil général de la ville concernée est servi immédiatement selon A-10, sans seuil chiffré, avec décision écrite ville, date et propriétaire. Le recrutement et les campagnes suivent les critères de sortie selon A-05, sans date de lancement fixée ni date de campagne inventée. Les partenaires restent à nommer.

La mesure des campagnes porte les événements canoniques avec les champs `city`, `trade`, `campaign_ref`, `plateforme` et un horodatage, avec conservation de 30 jours et aucun identifiant d'appareil permanent, y compris sur `desktop`. Les vues de tableau de bord séparent la découverte, la conversion, la publication, la modération, le chat et le push. Le dénominateur avant `signup_verified` et le dénominateur après `signup_verified` ne peuvent être fusionnés dans un graphique, un total ou un export. Les séries restent séparées par ville et par `plateforme`, sans fusion entre `mobile`, `web` et `desktop`. Aucun lien de campagne, aucun `campaign_ref`, aucun partenaire, aucun validateur et aucun résultat de mesure ne sont fournis ici.

## 2. Points à contrôler

Chaque ligne reste à renseigner au moment du contrôle. Aucune phrase n'est marquée comme retenue ici.

| Point à contrôler | Ce qui est déjà écrit | Preuve à archiver | État |
|---|---|---|---|
| Liste fermée des promesses | Cinq promesses interdites, aucune ajoutée sans décision écrite | À renseigner, sans promesse inventée | En attente de contrôle |
| Phrase autorisée | Une phrase parmi les trois écrites, sans promesse d'embauche | À renseigner avec la phrase exacte, sans phrase préremplie | En attente de contrôle |
| Validation par ville | Canal de campagne de la ville, phrase exacte, validateur et date | À renseigner séparément pour Brazzaville et Kinshasa, sans nom ni date préremplis | En attente de contrôle |
| Non transposition | Une phrase validée dans une ville ne vaut pas pour l'autre | À renseigner, décision distincte ou aucune | En attente de contrôle |
| Périmètre des clients | `mobile`, `web` et `desktop`, sans promesse d'emploi | À renseigner par plateforme, sans transfert de preuve | En attente de contrôle |
| Cible propre à la ville | `video_published` avec `city`, sans reprise de l'autre ville | À renseigner, sans valeur préremplie | En attente de contrôle |
| Repli A-10 | Fil général de la ville servi immédiatement, sans seuil chiffré | À renseigner avec ville, date et propriétaire, ou aucun | En attente de contrôle |
| Champs d'événement | `city`, `trade`, `campaign_ref`, `plateforme` et horodatage | À renseigner, aucun `campaign_ref` prérempli | En attente de contrôle |
| Non fusion des dénominateurs | Avant et après `signup_verified` séparés dans tout graphique, total ou export | À renseigner, extrait daté sans valeur préremplie | En attente de contrôle |
| Lecture par plateforme | `mobile`, `web` et `desktop` séparément | À renseigner, sans fusion | En attente de contrôle |
| Absence de traceur tiers | Aucun traceur tiers dans le parcours visiteur ni sur `desktop` | À renseigner, contrôle daté | En attente de contrôle |
| Partenaires à nommer | Catégories écrites, noms à nommer | À renseigner, aucun nom prérempli | En attente de contrôle |

## 3. Champs à remplir au moment du contrôle

| Champ | Valeur |
|---|---|
| Date du contrôle | À renseigner |
| Ville concernée | À renseigner séparément pour Brazzaville et Kinshasa |
| Plateforme concernée | À renseigner pour `mobile`, `web` ou `desktop` |
| Phrase validée | À renseigner, aucune phrase préremplie |
| Validateur nommé | À renseigner |
| Date de validation | À renseigner, aucune date préremplie |
| Canal de campagne utilisé | À renseigner, sans extrait prérempli |
| Référence de campagne | À renseigner, aucun `campaign_ref` prérempli |
| Partenaire concerné | À renseigner, aucun nom prérempli |
| Cible vérifiée | À renseigner, sans résultat prérempli |
| Repli éventuel | À renseigner avec ville, date et propriétaire, ou aucun |
| Relevé de mesure | À renseigner, sans chiffre prérempli |
| Dénominateurs séparés | À renseigner, sans fusion |
| Écart constaté | À renseigner, ou aucun |
| Action datée | À renseigner, ou aucune |
| Propriétaire du compte rendu | À renseigner |
| Approbateur nommé | À renseigner |
| Archive et historique | À renseigner |
| État | En attente de contrôle |

Une phrase sans validation écrite datée n'est pas retenue. Une mesure sans séparation des dénominateurs n'est pas conforme à la règle écrite. Aucune campagne n'est lancée par cette fiche.

## 4. Distinctions à conserver

Un contrôle de campagne ne valide aucune hypothèse H1 à H8, ne retient aucune opportunité O, ne modifie pas D-019 ni A-10, ne crée aucun partenaire ni validateur, ne transpose pas une ville vers l'autre, ne fusionne pas les populations visiteur et membre, ne fixe pas de date de lancement selon A-05, ne prononce pas l'ouverture publique et ne lève aucune porte.

Les phrases autorisées ne sont pas des phrases retenues. Une cible avant ouverture n'est pas un résultat de campagne. Aucun lien public n'est créé ici et aucune donnée de terrain n'est avancée.

## 5. Ce que cette fiche ne fait pas

Elle ne lance aucune campagne, ne choisit aucune phrase, ne nomme aucun validateur ni partenaire, ne crée aucun lien public, ne relève aucune mesure, ne modifie aucune décision, ne lève aucune porte et ne contient aucun code applicatif.
