# Fiche de contrôle des réponses support par ville et par plateforme

**Statut** : préparée le 27 novembre 2026, aucune question reçue, aucun ticket ouvert, aucun référent nommé, aucune porte levée  
**Sources canoniques** : [Support](../../docs/Operations/support.md), [Modération](../../docs/Operations/moderation-manuel.md), [Contestation](../../docs/Operations/contestation.md), [Veille arnaque](../../docs/Operations/veille-arnaque.md), [Incidents](../../docs/Operations/incidents.md), [PRD](../../docs/Product/prd.md), [D-019 au registre](../../docs/Product/decisions.md)  
**Règle** : cette fiche prépare le contrôle des réponses support. Elle ne reçoit aucune question, n'ouvre aucun ticket, ne nomme aucun référent et ne lève aucune porte.

## 1. Ce qui est déjà écrit

La fiche support porte huit questions courtes, quatre par ville, avec une réponse courte et une escalade vers un référent à nommer. Chaque question est lue avec la ville et la plateforme : `mobile` pour les applications natives iOS et Android, `web` pour le navigateur, `desktop` pour l'application exécutable Windows et macOS. Linux est différé. Une réponse ou une panne peut concerner le client `desktop` seul. Les réponses écrites valent pour les trois clients et aucun propriétaire n'est inventé.

Les règles de réponse interdisent toute promesse d'emploi, de salaire, de vérification N2 au MVP, de classement payant ou d'offre d'emploi au MVP. La gratuité totale pendant l'acquisition est rappelée telle quelle. D-019 interdit tout classement payant dans la recherche. Si la question porte sur un signalement ou une décision, le support ouvre un ticket lié et n'interprète pas la décision à la place du modérateur. Une question sur une arnaque est traitée avec les avertissements rédigés dans `veille-arnaque.md`. Une panne ou une file saturée bascule dans `incidents.md` avec la ville et la plateforme concernées, et une panne propre au client `desktop` est ouverte avec `plateforme=desktop`, sans fusion avec `mobile` ou `web`.

La contestation porte un délai unique de 30 jours à compter de l'horodatage de réception de l'email canonique, avec deuxième relecteur par ville. Les textes d'avertissement restent une proposition opérationnelle tant que la décision de leur ajout à FS-07 n'est pas écrite. Aucune question réelle, aucun ticket, aucun email, aucun nom de référent et aucune panne ne sont fournis ici.

## 2. Points à contrôler

Chaque ligne reste à renseigner au moment du contrôle. Aucune question n'est supposée reçue ici.

| Point à contrôler | Ce qui est déjà écrit | Preuve à archiver | État |
|---|---|---|---|
| Lecture par ville et par plateforme | Ville et plateforme lues ensemble, `desktop` non fusionné | À renseigner pour `mobile`, `web` et `desktop`, sans transposition | En attente de contrôle |
| Réponse courte | Huit réponses écrites dans `support.md`, valables pour les trois clients | À renseigner avec la question réellement reçue, sans réponse préremplie | En attente de contrôle |
| Absence de promesse | Aucun emploi, salaire, N2 au MVP, classement payant ni offre au MVP | À renseigner, contrôle daté sans extrait prérempli | En attente de contrôle |
| Gratuité rappelée | Gratuité totale pendant l'acquisition, D-019 inchangée | À renseigner, sans classement payant | En attente de contrôle |
| Signalement ou décision | Ticket lié ouvert, aucune interprétation à la place du modérateur | À renseigner avec référence pseudonyme, sans identifiant réel | En attente de contrôle |
| Contestation | Lien de l'email canonique, délai unique de 30 jours | À renseigner, sans lien ni date préremplis | En attente de contrôle |
| Question sur une arnaque | Avertissements de `veille-arnaque.md`, décision FS-07 à écrire | À renseigner, sans texte retenu prérempli | En attente de contrôle |
| Panne ou file saturée | Bascule dans `incidents.md` avec ville et plateforme | À renseigner, sans identifiant INC prérempli | En attente de contrôle |
| Escalade | Référent à nommer selon la question écrite | À renseigner, sans nom prérempli | En attente de contrôle |

## 3. Champs à remplir au moment du contrôle

| Champ | Valeur |
|---|---|
| Date du contrôle | À renseigner |
| Ville concernée | À renseigner, sans transposition vers l'autre ville |
| Plateforme concernée | À renseigner pour `mobile`, `web` ou `desktop` |
| Question reçue | À renseigner, aucune question préremplie |
| Réponse fournie | À renseigner depuis les réponses écrites, sans extrait prérempli |
| Ticket lié | À renseigner, ou aucun |
| Référent d'escalade | À renseigner |
| Délai de contestation rappelé | 30 jours, tel qu'écrit, sans date préremplie |
| Avertissement concerné | À renseigner, ou aucun |
| Incident ouvert | À renseigner avec ville et plateforme, ou aucun |
| Écart constaté | À renseigner, ou aucun |
| Action datée | À renseigner, ou aucune |
| Propriétaire du compte rendu | À renseigner |
| Approbateur nommé | À renseigner |
| Archive et historique | À renseigner |
| État | En attente de contrôle |

Une ligne sans question réelle ni trace datée n'est pas une réponse contrôlée. Aucune réponse n'est créée et aucune promesse n'est ajoutée par cette fiche.

## 4. Distinctions à conserver

Un contrôle de support ne valide aucune hypothèse H1 à H8, ne retient aucune opportunité O, ne modifie pas D-019, ne retient aucun texte d'avertissement, ne nomme aucun référent, ne transpose pas une ville vers l'autre, ne remplace ni la fiche de contestation ni le registre des incidents, ne fixe pas de date de lancement selon A-05 et ne lève aucune porte.

Une réponse ne décide pas à la place du modérateur. Une panne propre au client `desktop` reste distincte de `mobile` et de `web`. Aucune donnée personnelle de visiteur n'est recopiée dans la preuve archivée.

## 5. Ce que cette fiche ne fait pas

Elle ne reçoit aucune question, n'écrit aucune réponse, n'ouvre aucun ticket ni incident, ne nomme aucun titulaire, ne retient aucun avertissement, ne modifie aucune décision, ne lève aucune porte et ne contient aucun code applicatif.
