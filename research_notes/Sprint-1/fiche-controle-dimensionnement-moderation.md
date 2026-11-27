# Fiche de contrôle des hypothèses de dimensionnement de la modération

**Statut** : préparée le 27 novembre 2026, aucune mesure relevée, aucun effectif confirmé, aucune porte levée  
**Sources canoniques** : [Journée type de la modération](../../docs/Operations/journee-type-moderation.md), [Montée en charge](../../docs/Operations/montee-en-charge.md), [Astreinte](../../docs/Operations/astreinte.md), [Opérations](../../docs/Operations/README.md), [Dictionnaire de mesures](../../docs/Product/mesure.md), [A-09 au registre des arbitrages](../../docs/Product/arbitrage.md), [Fiche de contrôle de la condition 6](./fiche-controle-condition6.md)  
**Règle** : cette fiche prépare la confirmation des hypothèses après sept jours de mesure. Elle ne relève aucun volume, ne confirme aucun effectif et ne lève aucune porte.

## 1. Ce qui est déjà écrit

La journée type porte des volumes hypothétiques de signalements pour 1 000 sessions de fil, par ville et par motif. À Brazzaville : spam 4, contenu trompeur 3, harcèlement 2, contenu dangereux 1, autre 1, total 11. À Kinshasa : spam 5, contenu trompeur 4, harcèlement 2, contenu dangereux 1, autre 1, total 13. Ces chiffres sont des hypothèses de capacité écrites avant ouverture, pas des résultats de terrain et pas une extrapolation d'une ville vers l'autre. Les signalements sont lus par ville et par plateforme pour `mobile`, `web` et `desktop`, sans fusion entre les deux villes ni entre plateformes. Linux est différé.

La matrice de priorité écrit P1 pour contenu dangereux, harcèlement dès le premier signalement et demande d'argent ou de codes dans le chat, avec prise en charge en 15 minutes 24 h/24 par l'astreinte et décision en 1 heure. P2 couvre contenu trompeur ou spam à partir de deux signalements, avec prise en charge en 2 heures et décision en 8 heures ouvrées. P3 couvre l'autre et le signalement isolé sans urgence, avec prise en charge en 1 jour ouvré et décision en 2 jours ouvrés. La relecture est obligatoire avant retrait ou suspension pour P1 et avant retrait pour P2, et hebdomadaire par échantillon pour P3.

L'effectif minimal avant ouverture est d'un modérateur de garde et d'un relecteur joignable par ville, tous deux à nommer. A-09 retient le renfort bénévole coopté par le référent ville et encadré, avec couverture de 08:00 à 20:00 en heure locale et astreinte P1 hors plage. Les deux signaux actionnables sont `queue_depth` au delà de 20 tickets ouverts sur une ville pendant 15 minutes et `report_age` avec p95 supérieur à 4 heures sur une fenêtre glissante d'une heure, chacun avec destinataire et escalade à nommer. Un exercice à blanc est prévu pour chaque ville et chaque plateforme avant tout lien public, avec compte rendu dans le canal unique. Aucune mesure, aucun volume relevé, aucun effectif nommé et aucun résultat d'exercice ne sont fournis ici.

## 2. Points à contrôler après sept jours de mesure

Chaque ligne reste à renseigner au moment du contrôle. Aucune hypothèse n'est présentée comme confirmée ici.

| Point à contrôler | Ce qui est déjà écrit | Preuve à archiver | État |
|---|---|---|---|
| Volumes par ville et par motif | Hypothèses pour 1 000 sessions, distinctes par ville | À renseigner depuis les sept jours, sans valeur préremplie | En attente de mesure |
| Lecture par plateforme | `mobile`, `web` et `desktop`, sans fusion ni transposition | À renseigner séparément, avec lecture agrégée signalée si besoin | En attente de mesure |
| Unités de mesure | Signalements pour 1 000 sessions de fil, avec `feed_session_start` | À renseigner avec source datée, sans chiffre prérempli | En attente de mesure |
| Priorités appliquées | P1, P2 et P3 avec leurs motifs déclencheurs écrits | À renseigner, sans priorité préremplie | En attente de mesure |
| Délais de prise en charge et de décision | Cibles écrites par priorité, sans relevé prérempli | À renseigner avec horodatages, sans résultat avancé | En attente de mesure |
| Relecture obligatoire | Avant retrait ou suspension en P1, avant retrait en P2, échantillon hebdomadaire en P3 | À renseigner avec identifiant du relecteur, sans nom prérempli | En attente de mesure |
| Effectif minimal | Un modérateur de garde et un relecteur joignable par ville | À renseigner, sans titulaire prérempli | En attente de mesure |
| Renfort A-09 | Bénévole coopté par le référent ville et encadré | À renseigner avec engagement daté, ou aucun | En attente de mesure |
| Signaux actionnables | `queue_depth` et `report_age`, avec destinataire et escalade | À renseigner, sans valeur mesurée préremplie | En attente de mesure |
| Exercice à blanc du flux | Par ville et par plateforme, compte rendu dans le canal unique | À renseigner, sans délai relevé prérempli | En attente de mesure |

## 3. Champs à remplir au moment de la confirmation

| Champ | Valeur |
|---|---|
| Date de la confirmation | À renseigner |
| Fenêtre de mesure | Sept jours d'exploitation, à dater, aucune date préremplie |
| Ville concernée | À renseigner séparément pour Brazzaville et Kinshasa |
| Plateforme concernée | À renseigner pour `mobile`, `web` ou `desktop` |
| Volumes relevés | À renseigner par motif, aucun chiffre prérempli |
| Écart avec l'hypothèse | À renseigner, ou aucun |
| Priorités relevées | À renseigner, aucune priorité préremplie |
| Délais relevés | À renseigner, seules les cibles sont écrites |
| Effectif confirmé | À renseigner, sans nom prérempli |
| Renfort retenu | À renseigner, ou aucun |
| Décision d'ajustement | À renseigner, ou aucune |
| Motif écrit | À renseigner |
| Document modifié | À renseigner avec date et portée, sans modification silencieuse |
| Propriétaire de la décision | À renseigner |
| Approbateur nommé | À renseigner |
| Archive et historique | À renseigner |
| État | En attente de mesure |

Une hypothèse n'est pas une mesure et une cible n'est pas un relevé. Aucun écart n'est résorbé par réécriture silencieuse d'une hypothèse. Aucune ville n'est confirmée à partir de l'autre.

## 4. Distinctions à conserver

Une confirmation de dimensionnement ne valide aucune hypothèse H1 à H8, ne retient aucune opportunité O, ne modifie pas A-09 ni les seuils S1, S2 et S3, ne crée aucun titulaire, ne transpose pas une ville vers l'autre, ne remplace ni la condition 6 ni la fiche des seuils de bascule, ne fixe pas de date de lancement selon A-05 et ne lève aucune porte.

Les volumes écrits restent des hypothèses jusqu'à la mesure datée. Une relecture hebdomadaire par échantillon ne dispense pas de la relecture obligatoire avant retrait ou suspension. Le renfort reste coopté par le référent ville et encadré, sans nomination tacite.

## 5. Ce que cette fiche ne fait pas

Elle ne relève aucun volume, ne mesure aucun délai, ne confirme aucun effectif, ne nomme aucun titulaire, ne modifie aucune hypothèse ni seuil, ne remplace pas la journée type ni la fiche de contrôle de la condition 6, ne lève aucune porte et ne contient aucun code applicatif.
