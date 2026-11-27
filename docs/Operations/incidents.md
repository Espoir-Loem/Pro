# Incidents

**Déclencheur.** Avant la première mise en ligne, avec registre et postmortem prêts.  
**Dépendances.** [astreinte](./astreinte.md), [montée en charge](./montee-en-charge.md), [Technique](../Technique/README.md), [Décisions produit](../Product/decisions.md).  
**Propriétaire.** Coordinateur des opérations, à nommer.  
**Statut.** Schéma et gravité écrits, décideurs à nommer, postmortem sans blâme obligatoire.

## Schéma du registre

| Champ | Règle |
|---|---|
| Identifiant | `INC-AAAAMMJJ-NN`, numéro séquentiel par jour |
| Gravité | G1, G2 ou G3 selon la table ci-dessous |
| Ville | Brazzaville, Kinshasa ou commun, jamais les deux fusionnées |
| Plateforme | `mobile`, `web` ou `desktop`, lu avec la ville ; `desktop` désigne l'application exécutable Windows et macOS |
| Fonction touchée | Fil, publication, chat, modération, email, CDN, mise à jour |
| Heure de début | Horodatage et fuseau local, UTC+1 |
| Décideur | Rôle titulaire de l’astreinte, à nommer |
| Action | Atténuation écrite dans le canal unique `astreinte-pro` |
| Liens | Tickets de modération ou contestations concernées |
| Postmortem | Obligatoire pour G1 et G2, sans blâme, avec actions datées |

## Gravité

| Gravité | Définition | Décideur | Ouverture |
|---|---|---|---|
| G1 | Fil ou modération indisponible plus de 30 minutes dans une ville | Coordinateur de garde, à nommer | Immédiate |
| G2 | Dégradation partielle, tickets en attente ou coût CDN au seuil S3 | Référent ville, à nommer | Dans les 15 minutes |
| G3 | Anomalie limitée, sans risque pour la confiance | Référent technique, à nommer | Dans le jour ouvré |

La gravité est lue par ville et par plateforme : une coupure peut toucher le client `desktop` seul et reste alors rattachée à `plateforme=desktop`, sans être confondue avec `mobile` ou `web`. Les seuils ci-dessus ne changent pas et aucun titulaire n'est inventé.

## Journal et décision

Pendant l’incident, le coordinateur de garde écrit l’heure de chaque action dans le canal unique. La communication prépare les textes neutres, sans libellé de sanction sur écran verrouillé. Les opérations appliquent la coupure ou le rétablissement d’une fonction. Une bascule de modération vers le référent produit est tracée avec son heure et son destinataire, à nommer. Toute coupure propre au client `desktop` est écrite avec sa plateforme dans le canal unique, avec son heure de début et de rétablissement. Une panne liée à une mise à jour est ouverte avec la plateforme concernée et la version appliquée, sans identifiant d'appareil ni de machine. Un échec de vérification entraîne le retour à la version précédente avant toute remise en service.

## Postmortem sans blâme

Le postmortem relate les faits, la chronologie, les causes et les mesures prises. Il ne cherche pas de coupable et ne nomme pas de faute individuelle. Chaque action corrective porte un propriétaire et une échéance chiffrée, avec la ville et la plateforme concernées : J+2 pour une atténuation, J+7 pour une correction, J+30 pour un changement structurel. Le document est relisible par les trois rôles de l’astreinte et clos seulement quand les actions datées sont vérifiées. La [fiche de contrôle du registre et du postmortem](../../research_notes/Sprint-1/fiche-controle-registre-incidents.md) prépare ces vérifications, sans identifiant INC ni décideur préremplis.
