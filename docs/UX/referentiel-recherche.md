# Pro : référentiel de recherche du cycle 1

**Statut** : version 1, 25 novembre 2026  
**Portée** : emplacements et règles de nommage prévus pour le cycle 1  
**Documents liés** : [Recherche UX](./ux-research.md), [Parcours](./userflow.md), [Décisions](../Product/decisions.md), [Grille de relecture](../Redaction/ia-defauts-et-tips.md)

Aucune donnée de participant n'est inventée dans ce document. Les dossiers et fichiers ci-dessous décrivent des emplacements prévus, pas des preuves recueillies. Aucun entretien n'a eu lieu à la date de rédaction. Les noms, emails, numéros de téléphone et identifiants de compte réels ne sont jamais stockés dans ce référentiel.

## 1. Emplacement prévu

Le référentiel est prévu sous `research_notes/Cycle-1/`. Le [kit d'exécution](../../research_notes/Cycle-1/README.md) y est préparé le 26 novembre 2026 avec les modèles et les protocoles décrits dans ce document. Les dossiers `participants/P.../` sont créés après J2, quand les douze personnes recrutées ont donné leur consentement. La ville, la situation et le secteur de chaque P sont inscrits alors, sans être devinés ici.

```text
research_notes/Cycle-1/
  participants/P1/ ... P12/
  sessionnels/
  stimuli/RQ1/
  stimuli/RQ3/
  guide/
  protocole/
  codage/
  consentements/
  citations/
  decisions/
```

Les emplacements sont prévus pour les trois livrables : application mobile, site web ou application desktop. La valeur de `plateforme` est `mobile`, `web` ou `desktop` selon la définition de la [recherche UX](./ux-research.md). Elle est consignée au moment de la session, sans être devinée ici.

## 2. Identifiants P1 à P12

| Identifiant | Dossier prévu | Sessions prévues | Contenu du dossier | État |
|---|---|---|---|---|
| P1 | `participants/P1/` | J4 ou J5 ou J6, J7 possible, J8 possible | Consentement, notes, citations, ordre des stimuli | Emplacement prévu, aucune donnée |
| P2 | `participants/P2/` | J4 à J6, J7 possible, J8 possible | Consentement, notes, citations, ordre des stimuli | Emplacement prévu, aucune donnée |
| P3 | `participants/P3/` | J4 à J6, J7 possible, J8 possible | Consentement, notes, citations, ordre des stimuli | Emplacement prévu, aucune donnée |
| P4 | `participants/P4/` | J4 à J6, J7 possible, J8 possible | Consentement, notes, citations, ordre des stimuli | Emplacement prévu, aucune donnée |
| P5 | `participants/P5/` | J4 à J6, J7 possible, J8 possible | Consentement, notes, citations, ordre des stimuli | Emplacement prévu, aucune donnée |
| P6 | `participants/P6/` | J4 à J6, J7 possible, J8 possible | Consentement, notes, citations, ordre des stimuli | Emplacement prévu, aucune donnée |
| P7 | `participants/P7/` | J4 à J6, J7 possible, J8 possible | Consentement, notes, citations, ordre des stimuli | Emplacement prévu, aucune donnée |
| P8 | `participants/P8/` | J4 à J6, J7 possible, J8 possible | Consentement, notes, citations, ordre des stimuli | Emplacement prévu, aucune donnée |
| P9 | `participants/P9/` | Réserve, J8 possible, H6 et H7 possibles | Consentement, notes, citations, ordre des stimuli | Emplacement prévu, aucune donnée |
| P10 | `participants/P10/` | Réserve, J8 possible, H6 et H7 possibles | Consentement, notes, citations, ordre des stimuli | Emplacement prévu, aucune donnée |
| P11 | `participants/P11/` | Réserve, J8 possible, H6 et H7 possibles | Consentement, notes, citations, ordre des stimuli | Emplacement prévu, aucune donnée |
| P12 | `participants/P12/` | Réserve, J8 possible, H6 et H7 possibles | Consentement, notes, citations, ordre des stimuli | Emplacement prévu, aucune donnée |

Les huit entretiens principaux et les deux réserves utilisées à J8 sont désignés après recrutement. Les cinq créateurs nécessaires à H6 et H7 sont choisis parmi les douze selon les situations enregistrées à J2, pas attribués par avance à un identifiant P. Aucune plateforme n'est attribuée à un identifiant P par avance.

## 3. Sessions et nommage

Les sessions J3, J4 à J6, J7, J8 et J10 sont prévues sur application mobile, site web ou application desktop. La plateforme réellement utilisée est inscrite dans la fiche de session, sans modifier l'identifiant de session ni présumer un usage équivalent de l'une à l'autre.

| Session | Identifiant de session | Fichier principal | Règle |
|---|---|---|---|
| Entretien contextuel J4 à J6 | `J4-P1` à `J6-P8` | `participants/P1/notes-J4-P1.md` | Une fiche par personne et par jour ; la ville et le secteur sont des champs obligatoires |
| Prototype J7 | `J7-P1` et suivants | `sessionnels/J7-P1-taches.md` | Consigne, tâches, gestes codés, critères de réussite |
| Formulations email J8 | `J8-P1` et suivants | `sessionnels/J8-P1-variante.md` | Variante A ou B, abandon ou non, dénominateur unique par variante |
| Test interne J3 | `J3-interne` | `sessionnels/J3-interne.md` | Aucun identifiant P ; contributeur interne non nommé |
| Restitution J10 | `J10-decisions` | `decisions/J10-decisions.md` | Décision, date, opportunité, hypothèse concernée |

Un enregistrement audio suit le nom `participants/P1/audio-J4-P1.m4a`. Il n'est créé que si la personne a accepté l'enregistrement. En cas de refus, la note manuscrite porte le même identifiant de session et la mention « enregistrement refusé ».

## 4. Stimuli

Chaque stimulus est prévu pour application mobile, site web ou application desktop. Une différence observée entre plateformes est consignée dans la fiche de session, sans être interprétée comme une preuve ni comme une absence de différence.

| Stimulus | Emplacement | Contenu prévu | Contrôle |
|---|---|---|---|
| Vidéos RQ1 | `stimuli/RQ1/logistique/v1/video-01.mp4` à `video-03.mp4` et `stimuli/RQ1/sante/v1/video-01.mp4` à `video-03.mp4` | Six fichiers, trois par secteur retenu | Variation contrôlée du geste visible, du contexte et du nom affiché ; un seul axe varie à la fois |
| Ordre de présentation | `participants/P1/ordre-RQ1-P1.md` | Ordre tiré au sort et consigné avant J4 | Reproduction possible du test |
| Messages RQ3 | `stimuli/RQ3/v1/message-neutre.md` et `message-suspect.md` | Scénario neutre et scénario suspect | Le scénario suspect mobilise les quatre signaux de R7, avec geste attendu préenregistré |
| Formulations J8 | `stimuli/J8/v1/variante-A.md` et `variante-B.md` | Deux phrases à l'étape email | Une seule mesure d'abandon par variante, aucun croisement de dénominateurs |
| Adresse de test | `stimuli/adresse-test.md` | Adresse fournie par l'équipe | Non conservée dans les notes, aucune adresse réelle demandée |

Les fichiers de stimuli ne contiennent aucune donnée de participant. Les versions sont incrémentées de `v1` à `v2` quand le stimulus change ; un changement de version est daté dans `stimuli/changelog.md`.

## 5. Notes, consentements et citations

| Objet | Nom de fichier | Règle de contenu |
|---|---|---|
| Note d'entretien | `notes-J4-P1.md` | Ville, secteur, situation, observations, friction, émotion hypothétique, identifiant H |
| Consentement | `consentements/consentement-P1.md` | Accord ou refus d'enregistrement, date, version du guide présentée |
| Citation anonymisée | `citations/citation-P1-01.md` | Ville et secteur seulement, aucun nom ni détail identifiant |
| Reliture de citation | `citations/citation-P1-01-relue.md` | Date de relecture par la personne participante ; sans relecture, la citation n'entre pas dans le PRD |
| Retrait | `citations/retrait-P1-01.md` | Date de retrait, possible jusqu'à J10 |

Les notes, les enregistrements et les citations suivent les durées de la section 13 de [ux-research.md](./ux-research.md). La base légale et le responsable du traitement des données de recherche y sont à nommer avant J2.

## 6. Grille de codage

La grille prévue est `codage/grille-codage-v1.md`. Elle contient les codes suivants, sans interprétation libre ajoutée après coup :

| Code | Ce qui est codé | Identifiant relié |
|---|---|---|
| `GESTE-JUGEMENT` | Geste observable avant l'opinion déclarée | H1, H2 |
| `FRICTION` | Blocage ou hésitation observé | H3, H4, H7 |
| `EMOTION` | Manifestation visible, jamais déduite d'un ton de voix seul | H1, H4, H5 |
| `SIGNAL` | Signal de confiance ou de suspicion cité par la personne | H2, H5, O4 |
| `REFUS` | Refus d'enregistrement, de code ou de variante | H4 |

Deux personnes codent la même fiche. Un désaccord est noté dans `codage/desaccords.md` avec les deux interprétations ; il n'est pas arbitré par le seul avis de la personne la plus ancienne dans l'équipe. Un constat entre dans le PRD seulement avec une citation relue ou une observation codée et une ville.

## 7. Versions du guide et du protocole

| Fichier | Version | Date prévue | Changement |
|---|---|---|---|
| `guide/guide-entretien-v1.md` | v1 | J1 | Guide initial, questions du vécu vers le produit |
| `guide/guide-entretien-v2.md` | v2 | J3 | Ajout des trois vidéos par secteur à la question 6 et du codage des gestes |
| `guide/changelog.md` | continu | J1 à J10 | Date, motif, personne responsable |
| `protocole/J7-taches-v1.md` | v1 | J3 | Consigne, tâches, critères de réussite, enregistrement des gestes |
| `protocole/J8-variantes-v1.md` | v1 | J3 | Deux formulations, dénominateur unique, définition de l'abandon |

Les modèles correspondants sont préparés dans le [kit d'exécution](../../research_notes/Cycle-1/README.md). Leur date de passation est renseignée au moment de J1, J3 ou J7 et J8. Aucune version du guide, du protocole ou du stimuli n'est datée rétroactivement.

Ces versions et les phases J1 à J10 qui les utilisent valent pour application mobile, site web ou application desktop. La plateforme de chaque phase est consignée dans la fiche de session, sans changement de version automatique entre plateformes.

Aucune version du guide n'est écrite rétroactivement. Une modification pendant le terrain est datée et consignée dans `guide/changelog.md` ; la fiche de session porte la version utilisée.

## 8. Ce que le référentiel ne contient pas

Il ne contient ni CV, ni pièce d'identité, ni preuve d'arnaque, ni email réel de participant, ni enregistrement au delà de trente jours, ni citation non relue, ni résultat de ville attribué à un identifiant P avant J2. Il ne sert pas à mesurer une prévalence et ne remplace pas le [dictionnaire de mesures](../Product/mesure.md).
