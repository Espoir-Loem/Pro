# Fiche de contrôle des seuils de bascule S1, S2 et S3

**Statut** : préparée le 27 novembre 2026, aucun seuil franchi constaté, aucune mesure relevée, aucune porte levée  
**Sources canoniques** : [Montée en charge](../../docs/Operations/montee-en-charge.md), [D-022 au registre](../../docs/Product/decisions.md), [Modèle de révision D-022](../../research_notes/Planning/revision-D022-apres-30-jours.md), [Dictionnaire de mesures](../../docs/Product/mesure.md), [Roadmap, Phase 1](../../docs/Product/roadmap.md), [Incidents](../../docs/Operations/incidents.md), [A-09](../../docs/Product/arbitrage.md)  
**Règle** : cette fiche prépare le contrôle des seuils déjà écrits. Elle ne relève aucune mesure, ne modifie aucun seuil ni D-022, ne déclenche aucune action et ne lève aucune porte.

## 1. Ce qui est déjà écrit

La fiche de montée en charge porte trois seuils de bascule. S1 trafic lit `video_impression` au delà de 20 000 par jour sur une ville et prévoit le palier CDN de secours avec la qualité réduite, sous 15 minutes, par le référent technique à nommer. S2 file lit `queue_depth` au delà de 20 ou un p95 de `report_age` supérieur à 4 heures et prévoit le passage à deux modérateurs et un relecteur dans la ville concernée, sous 30 minutes, par le coordinateur des opérations à nommer. S3 coût lit un coût par vue supérieur à 0,001 USD dans la ville selon D-022 et prévoit la réduction du préchargement, le transcodage adaptatif forcé et la suspension de la nouvelle campagne dans la ville, sous une heure, par le référent technique à nommer.

S1 est lu par ville et par plateforme quand les données le permettent. Quand la distinction n'est pas disponible, la lecture reste agrégée par ville et elle est signalée comme telle. S3 s'applique aussi au client `desktop` sans modifier D-022. D-022 fixe une enveloppe mensuelle de 1 000 USD, 500 USD par ville, sur le mois civil, avec un seuil de 0,001 USD par vue lu séparément par ville. Sa révision après 30 jours d'exploitation suit son propre modèle. Les courbes de sessions et de signalements de la fiche de montée en charge sont des hypothèses de planification, pas des mesures de terrain. Aucun relevé, aucun franchissement et aucun destinataire nommé ne sont fournis ici.

## 2. Points à contrôler

Chaque ligne reste à renseigner au moment du contrôle. Aucun seuil n'est marqué comme franchi ici.

| Seuil | Ville | Plateforme | Relevé à archiver | Action prévue à vérifier | Délai écrit | État |
|---|---|---|---|---|---|---|
| S1 trafic | À renseigner, Brazzaville et Kinshasa séparément | À renseigner, avec `mobile`, `web` et `desktop` quand les données le permettent | À renseigner depuis `video_impression`, sans valeur préremplie | Palier CDN de secours et qualité réduite, sans action déclarée | 15 minutes, telle qu'écrite | En attente de contrôle |
| S2 file | À renseigner, Brazzaville et Kinshasa séparément | À renseigner pour chaque plateforme concernée | À renseigner depuis `queue_depth` et `report_age`, sans valeur préremplie | Passage à deux modérateurs et un relecteur dans la ville concernée, sans titulaire prérempli | 30 minutes, telle qu'écrite | En attente de contrôle |
| S3 coût | À renseigner, Brazzaville et Kinshasa séparément | À renseigner, y compris `desktop` | À renseigner depuis le coût par vue, sans valeur préremplie | Préchargement réduit, transcodage adaptatif, campagne suspendue dans la ville, sans campagne préremplie | 1 heure, telle qu'écrite | En attente de contrôle |
| Lecture agrégée | À renseigner, par ville | À renseigner quand la distinction par plateforme n'est pas disponible | À renseigner, signalée comme agrégée | Aucune action nouvelle, lecture signalée comme telle | Sans objet | En attente de contrôle |

## 3. Champs à remplir au moment du contrôle

| Champ | Valeur |
|---|---|
| Date du contrôle | À renseigner |
| Ville concernée | À renseigner, sans transposition vers l'autre ville |
| Plateforme concernée | À renseigner, ou lecture agrégée signalée |
| Source datée du relevé | À renseigner |
| Valeur relevée | À renseigner, aucun chiffre prérempli |
| Seuil appliqué | À renseigner depuis `montee-en-charge.md`, sans réécriture |
| Franchissement constaté | À renseigner, ou aucun |
| Heure de déclenchement | À renseigner |
| Destinataire nommé | À renseigner |
| Action exécutée | À renseigner, ou aucune |
| Incident ouvert | À renseigner avec ville et plateforme, ou aucun |
| Écart constaté | À renseigner, ou aucun |
| Action datée et archivée | À renseigner, ou aucune |
| Motif écrit | À renseigner |
| Propriétaire du compte rendu | À renseigner |
| Approbateur nommé | À renseigner |
| Historique de la décision | À renseigner |
| État | En attente de contrôle |

Une cible de planification n'est pas un relevé. Un franchissement n'est pas déclaré sans source datée. Aucune action n'est présentée comme exécutée par cette fiche.

## 4. Distinctions à conserver

Un seuil franchi ne modifie ni D-022 ni son modèle de révision, ne valide aucune hypothèse H1 à H8, ne retient aucune opportunité O, ne crée aucun titulaire, ne transpose pas une ville vers l'autre, ne remplace ni la condition 6 ni la condition 7, ne fixe pas de date de lancement selon A-05 et ne lève aucune porte.

Un relevé agrégé par ville n'autorise aucune lecture par appareil, aucun identifiant permanent visiteur et aucune transposition entre villes. Le renfort de modération lié à S2 reste encadré selon A-09, sans nomination tacite. Les valeurs de planification restent des hypothèses écrites avant ouverture.

## 5. Ce que cette fiche ne fait pas

Elle ne relève aucune mesure, ne franchit aucun seuil, ne modifie aucun budget ni seuil, ne nomme aucun titulaire, ne déclenche aucune action, n'ouvre aucun incident, ne remplace pas la fiche de montée en charge ni le modèle de révision D-022, ne lève aucune porte et ne contient aucun code applicatif.
