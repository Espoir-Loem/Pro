# Performance : budgets et profil de référence

**Propriétaire.** Espoir LOEMBA, intérimaire. **Statut.** profil R2 arbitré le 26 novembre 2026, profil R1 encore proposé. **Date.** 26 novembre 2026.

## Profil de référence

Le PRD dit « réseau mobile correct ». Ce n'est pas mesurable. Le profil R1 ci-dessous est proposé et sert de grille de revue commune à `architecture.md` et `video.md`. Le [modèle de décision du profil R1](../../research_notes/Planning/decision-profil-R1.md) prépare l'écriture de ce choix, sans valeur préremplie ni mesure avancée.

| Paramètre | Valeur proposée | Statut |
|---|---|---|
| Accès | 4G LTE | à confirmer |
| Débit descendant | 1,5 Mbit/s | à confirmer |
| Débit montant | 0,5 Mbit/s | à confirmer |
| Latence aller-retour | 150 ms | à confirmer |
| Perte de paquets | 1 % | à confirmer |
| Appareil | 4 cœurs, 2 Go de RAM, navigateur récent | à confirmer |
| Méthode | p75 sur 100 sessions par ville, Brazzaville et Kinshasa séparées | à confirmer |

Le profil R1 sert les deux autres clients. Le profil R2 ci-dessous est réservé au client desktop.

## Profil R2 desktop arbitré

A-03 est arbitrée le 26 novembre 2026 : machine modeste retenue pour Windows 11 et macOS en version supportée, avec 2 cœurs, 4 Go de RAM et un disque SSD. Aucune mesure de Pro n'est disponible : les valeurs ci-dessous sont des cibles de revue, pas des résultats.

Pour le client desktop, la référence de perception : application de messagerie légère citée par le porteur. Elle n'est ni une mesure relevée, ni une promesse d'égalité de performance, ni une cible contractuelle.

| Paramètre | Valeur retenue | Statut |
|---|---|---|
| Systèmes | Windows 11 et macOS en version supportée, séparés | arbitré le 26 novembre 2026 |
| Machine de référence | 2 cœurs, 4 Go de RAM, SSD | arbitré le 26 novembre 2026 |
| Réseau pour la première image vidéo | profil R1 | proposition inchangée |
| Méthode | 30 lancements à froid par système, p75, traces jointes | arbitré le 26 novembre 2026 |
| Revue | 26 décembre 2026 | arbitré le 26 novembre 2026 |

| Mesure | Cible de revue | Condition |
|---|---|---|
| Démarrage à froid jusqu'au fil interactif | moins de 2 secondes | machine R2, Windows et macOS séparés, p75 sur 30 lancements |
| Changement de vue locale | moins de 100 ms | machine R2, Windows et macOS séparés |
| Première image vidéo | moins de 300 ms | profil R1, cache froid et cache chaud séparés |
| Mémoire au repos | moins de 150 Mo | machine R2, Windows et macOS séparés |
| Installateur | moins de 80 Mo | Windows et macOS séparés |

Aucun de ces seuils n'est présenté comme mesuré. La revue du 26 décembre 2026 joint les traces à `architecture.md`, `video.md` et `responsabilites.md`, et révise les cibles si la machine modeste les rend irréalistes. La [fiche de contrôle de cette revue](../../research_notes/Planning/revue-performance-desktop-A03.md) prépare les points et les traces à archiver, sans mesure ni cible révisée préremplie.

## Budgets

| Mesure | Budget proposé | Condition | Vérification |
|---|---|---|---|
| Première vidéo affichée | moins de 3 secondes, p75 | profil R1, cache froid et cache chaud séparés | trace de chargement enregistrée par ville |
| Démarrage après toucher | moins de 1,5 seconde, p75 | profil R1 | mesure client jointe à `video_impression` |
| Premier lot de recherche | moins de 500 ms, p95 | profil R1, requête déjà indexée | measure serveur et client |
| Défilement | au moins 45 images par seconde, p5 | appareil de référence | enregistrement de défilement |
| Bande passante du fil | 12 Mo au plus pour 10 vidéos | profil R1, qualité automatique | octets comptés côté CDN |
| Mode faible consommation | 6 Mo au plus pour 10 vidéos | préchargement désactivé, qualité plafonnée | test avec préférence activée |

Aucun téléchargement spéculatif au-delà de dix vidéos. Les budgets sont des seuils de revue, pas des promesses contractuelles tant que leur statut n'est pas confirmé.

## Accessibilité associée

WCAG 2.2 niveau AA visé. Cibles de 24 sur 24 pixels CSS au minimum AA, objectif de 44 pixels au-delà du minimum. Le contraste AA est vérifié pour les textes et les composants interactifs. Un budget dépassé n'autorise pas une réduction de ces exigences.

## Déclencheur

Ce document précède `architecture.md` et `video.md`. Tout changement du profil R1 entraîne une relecture de `architecture.md` et de `video.md`. Le profil R2 est arrêté ; la revue de performance desktop du 26 décembre 2026 est inscrite dans `responsabilites.md`.
