# Fiche de contrôle du registre des incidents et du postmortem

**Statut** : préparée le 27 novembre 2026, aucun incident ouvert, aucun identifiant INC, aucun décideur nommé, aucune porte levée  
**Sources canoniques** : [Incidents](../../docs/Operations/incidents.md), [Astreinte](../../docs/Operations/astreinte.md), [Montée en charge](../../docs/Operations/montee-en-charge.md), [Opérations](../../docs/Operations/README.md), [Décisions produit](../../docs/Product/decisions.md), [Premier rendu signé](./fiche-premier-rendu-signe.md)  
**Règle** : cette fiche prépare le contrôle du registre et du postmortem. Elle n'ouvre aucun incident, n'écrit aucun identifiant, ne nomme aucun décideur et ne lève aucune porte.

## 1. Ce qui est déjà écrit

Le registre porte un identifiant `INC-AAAAMMJJ-NN` avec numéro séquentiel par jour, une gravité G1, G2 ou G3, une ville égale à Brazzaville, Kinshasa ou commun sans fusion des deux villes, et une plateforme égale à `mobile`, `web` ou `desktop` lue avec la ville. La fonction touchée est l'une des sept fonctions écrites : fil, publication, chat, modération, email, CDN, mise à jour. L'heure de début est un horodatage avec fuseau local UTC+1. Le décideur est le rôle titulaire de l'astreinte, à nommer. L'atténuation est écrite dans le canal unique `astreinte-pro`. Les liens vont aux tickets de modération ou aux contestations concernées.

G1 couvre un fil ou une modération indisponible plus de 30 minutes dans une ville, avec ouverture immédiate par le coordinateur de garde à nommer. G2 couvre une dégradation partielle, des tickets en attente ou un coût CDN au seuil S3, avec ouverture dans les 15 minutes par le référent ville à nommer. G3 couvre une anomalie limitée sans risque pour la confiance, avec ouverture dans le jour ouvré par le référent technique à nommer. La gravité est lue par ville et par plateforme : une coupure touchant le seul client `desktop` reste rattachée à `plateforme=desktop`.

Pendant l'incident, chaque action est horodatée dans le canal unique. La communication prépare des textes neutres, sans libellé de sanction sur écran verrouillé. Une bascule de modération vers le référent produit est tracée avec son heure et son destinataire à nommer. Une panne liée à une mise à jour est ouverte avec la plateforme concernée et la version appliquée, sans identifiant d'appareil ni de machine, et un échec de vérification entraîne le retour à la version précédente avant remise en service.

Le postmortem est obligatoire pour G1 et G2. Il relate les faits, la chronologie, les causes et les mesures prises, sans recherche de coupable ni faute individuelle. Chaque action corrective porte un propriétaire et une échéance chiffrée avec la ville et la plateforme : J+2 pour une atténuation, J+7 pour une correction, J+30 pour un changement structurel. Le document est relisible par les trois rôles de l'astreinte et clos seulement quand les actions datées sont vérifiées. Aucun incident, aucun identifiant, aucun horodatage et aucun nom ne sont fournis ici.

## 2. Points à contrôler

Chaque ligne reste à renseigner au moment du contrôle. Aucun incident n'est déclaré par cette fiche.

| Point à contrôler | Ce qui est déjà écrit | Preuve à archiver | État |
|---|---|---|---|
| Identifiant séquentiel | `INC-AAAAMMJJ-NN`, numéro par jour | À renseigner, aucun identifiant prérempli | En attente de contrôle |
| Gravité appliquée | G1, G2 ou G3, avec leur définition et leur délai d'ouverture | À renseigner, sans gravité préremplie | En attente de contrôle |
| Ville et plateforme | Ville égale à Brazzaville, Kinshasa ou commun, plateforme lue avec la ville | À renseigner séparément, sans transposition | En attente de contrôle |
| Coupure propre à `desktop` | Rattachée à `plateforme=desktop`, sans fusion avec `mobile` ou `web` | À renseigner avec heures de début et de rétablissement | En attente de contrôle |
| Fonction touchée | Une des sept fonctions écrites | À renseigner, sans fonction préremplie | En attente de contrôle |
| Heure de début | Horodatage et fuseau local UTC+1 | À renseigner, aucune date préremplie | En attente de contrôle |
| Décideur et canal | Rôle titulaire de l'astreinte à nommer, canal unique `astreinte-pro` | À renseigner, sans nom prérempli | En attente de contrôle |
| Journal d'action | Heure de chaque action dans le canal unique | À renseigner, sans extrait prérempli | En attente de contrôle |
| Panne liée à une mise à jour | Plateforme et version appliquées, sans identifiant d'appareil ni de machine | À renseigner, sans version préremplie | En attente de contrôle |
| Postmortem G1 et G2 | Faits, chronologie, causes, mesures, sans blâme | À renseigner, sans faute individuelle | En attente de contrôle |
| Actions correctives | Propriétaire et échéance J+2, J+7 ou J+30 avec ville et plateforme | À renseigner, sans propriétaire prérempli | En attente de contrôle |
| Clôture du postmortem | Relisible par les trois rôles de l'astreinte, clos après vérification des actions datées | À renseigner, sans clôture préremplie | En attente de contrôle |

## 3. Champs à remplir au moment du contrôle

| Champ | Valeur |
|---|---|
| Date du contrôle | À renseigner |
| Identifiant de l'incident | À renseigner, aucun identifiant prérempli |
| Gravité | À renseigner depuis la table écrite |
| Ville concernée | À renseigner, sans fusion des deux villes |
| Plateforme concernée | À renseigner pour `mobile`, `web` ou `desktop` |
| Fonction touchée | À renseigner |
| Heure de début et fuseau | À renseigner, UTC+1 tel qu'écrit |
| Décideur | À renseigner |
| Heure d'ouverture | À renseigner, sans délai relevé prérempli |
| Atténuation écrite | À renseigner depuis le canal unique |
| Liens vers tickets ou contestations | À renseigner, sans identifiant réel prérempli |
| Postmortem requis | À renseigner pour G1 et G2, ou sans objet |
| Actions correctives datées | À renseigner, ou aucune |
| Vérification des actions | À renseigner, aucune vérification préremplie |
| Propriétaire du compte rendu | À renseigner |
| Approbateur nommé | À renseigner |
| Archive et historique | À renseigner |
| État | En attente de contrôle |

Une ligne sans horodatage ni preuve n'est pas un incident contrôlé. Aucun délai n'est mesuré ici et aucune action n'est présentée comme exécutée.

## 4. Distinctions à conserver

Un contrôle d'incident ne valide aucune hypothèse H1 à H8, ne retient aucune opportunité O, ne modifie pas la gravité écrite, ne crée aucun titulaire, ne transpose pas une ville vers l'autre, ne modifie pas les seuils S1, S2 et S3, ne remplace ni la condition 6 ni la condition 7, ne fixe pas de date de lancement selon A-05 et ne lève aucune porte.

Une panne propre au client `desktop` n'est ni `mobile` ni `web`. Une bascule vers le référent produit n'efface pas l'action tracée dans le canal unique. Une action corrective sans échéance chiffrée ne clôt pas le postmortem. Aucun identifiant d'appareil ni de machine n'est ajouté.

## 5. Ce que cette fiche ne fait pas

Elle n'ouvre aucun incident, n'écrit aucun identifiant ni horodatage, ne nomme aucun décideur ni propriétaire, n'envoie aucun message dans le canal unique, n'écrit aucun postmortem, ne modifie aucune gravité ni délai, ne lève aucune porte et ne contient aucun code applicatif.
