# Performance : budgets et profil de référence

**Propriétaire.** à nommer. **Statut.** proposée, valeurs à confirmer. **Date.** 25 novembre 2026.

## Profil de référence

Le PRD dit « réseau mobile correct ». Ce n'est pas mesurable. Le profil R1 ci-dessous est proposé et sert de grille de revue commune à `architecture.md` et `video.md`.

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

## Profil R2 desktop à définir

Machine de référence à confirmer, sur Windows et sur macOS. Les versions de système, le processeur, la mémoire et le disque de référence sont à confirmer. Aucune mesure de Pro n'est disponible : les valeurs ci-dessous sont des cibles proposées, à confirmer.

Pour le client desktop, la référence de perception : application de messagerie légère citée par le porteur. Elle n'est ni une mesure relevée, ni une promesse d'égalité de performance, ni une cible contractuelle.

| Paramètre | Valeur proposée | Statut |
|---|---|---|
| Systèmes | Windows et macOS, versions à confirmer | à confirmer |
| Machine de référence | processeur, mémoire et disque à confirmer | à confirmer |
| Réseau pour la première image vidéo | profil R1 | à confirmer |

| Mesure | Cible proposée | Condition | Statut |
|---|---|---|---|
| Démarrage à froid jusqu'au fil interactif | moins de 2 secondes | machine de référence R2 à confirmer, Windows et macOS séparés | à confirmer |
| Changement de vue locale | moins de 100 ms | machine de référence R2 à confirmer | à confirmer |
| Première image vidéo | moins de 300 ms | profil R1, cache froid et cache chaud séparés | à confirmer |
| Mémoire au repos | moins de 150 Mo | machine de référence R2 à confirmer | à confirmer |
| Installateur | moins de 80 Mo | Windows et macOS séparés | à confirmer |

Aucun de ces seuils n'est présenté comme mesuré. La confirmation passe par une machine de référence écrite et par des traces jointes aux revues de `architecture.md`, `video.md` et `responsabilites.md`.

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

Ce document précède `architecture.md` et `video.md`. Tout changement du profil R1 entraîne une relecture de `architecture.md` et de `video.md`. La confirmation du profil R2 déclenche la revue de performance desktop inscrite dans `responsabilites.md`.
