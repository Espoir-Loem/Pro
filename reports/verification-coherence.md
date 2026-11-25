# Vérification finale de cohérence de la documentation Pro

**Date.** 25 novembre 2026.
**Lecture.** Ce rapport est un snapshot de la version précédente, avant l'inscription de D-009. L'état courant figure dans [avenant-agent-et-stack.md](./avenant-agent-et-stack.md).
**Périmètre.** `docs/` uniquement pour les corrections. Aucun rapport historique dans `reports/` n'a été modifié. Seul `reports/verification-coherence.md` est créé.

## Contrôles mécaniques

| Commande | Attendu | Résultat |
|---|---|---|
| Recherche des tirets interdits dans `docs` | Aucune occurrence | Vide, conforme |
| Recherche des caractères chinois, japonais ou coréens dans `docs` | Aucune occurrence | Vide, conforme |
| Recherche des marqueurs de correction en attente dans `docs` | Aucune occurrence | Vide, conforme |
| Recherche des formulations réduites à deux plateformes dans `docs` | Aucune occurrence | Vide, conforme |
| `python3 /tmp/opencode/check_links.py` | Zéro lien relatif cassé | 434 liens relatifs résolus, 0 cassé |
| `python3 /tmp/opencode/check_ids.py` | FS-01 à FS-11, US-01 à US-17, D-001 à D-023, sans saut | 11 FS, 17 US, 23 D, aucun saut |
| `python3 /tmp/opencode/check_mermaid.py` | Tous les blocs fermés | 13 fichiers avec Mermaid, 0 bloc ouvert |
| `find docs -type f \| wc -l` | 59 fichiers | 59, conforme |
| `grep -n 'cinquante-neuf fichiers' docs/README.md` | Annonce dans le README | 1 occurrence, conforme |

## Contrôles sémantiques

| Contrôle | Résultat |
|---|---|
| Décisions retenues et questions ouvertes | Conforme après correction. Retenues : D-001 à D-008, D-012 à D-021, D-023. Ouvertes : D-009, D-010, D-011, D-022. Aucune question ouverte n'est présentée comme tranchée. |
| Trois plateformes et Linux différé | Conforme. `mobile`, `web`, `desktop`. Aucune phrase ne réduit le périmètre à deux plateformes. |
| Règle des langues D-008 | Conforme. Français d'abord, langues suivantes validées marché par marché, aucune autre langue datée. |
| Règle des sous-titres D-021 | Conforme. Sous-titres générés puis corrigés par l'auteur avant publication, sinon brouillon non publié. |
| Règle J7 D-020 | Conforme après correction de `Technique/adr-002-identite-session.md`. Retour à sept jours sur comptes avec email vérifié, aucune cohorte visiteur. |
| Métrique d'acquisition | Conforme. `signup_verified / feed_session_start * 1000` dans le dictionnaire, le PRD, la vision, le manifeste et l'expérimentation. |
| Gratuité des phases 1 à 4 | Conforme dans le registre, la vision, le PRD et la roadmap. |
| Interdiction du classement payant | Conforme dans le registre, le manifeste, le PRD, la roadmap, les opérations et la croissance. |
| Conservation à 30 jours | Conforme après correction des fiches `Conformite/`. Événements et vidéos retirées suivent 30 jours. |
| Grille d'arbitrage | Conforme après correction. `arbitrage.md` ne choisit aucune option et renvoie vers `decisions.md`. |
| Jalons D-009, D-010, D-011 et D-022 | Conforme après correction de `decisions.md` et `prd.md`. D-022 est placé avant `video.md` et FS-02. |
| Contestation | Conforme après correction. Le délai de 30 jours et la deuxième relecture restent une décision déjà écrite. |
| Lanceurs de métiers | Conforme. Le seuil de fil non vide reste le point A-10 à arbitrer ; les cibles de semis restent écrites. |

## Corrections appliquées dans `docs/`

- `docs/Product/arbitrage.md` : l'opposabilité globale D-001 à D-023 est remplacée par la liste des décisions retenues ; les questions ouvertes sont explicitement hors sprint ; la phrase finale sur la réouverture vise désormais les seules décisions retenues.
- `docs/Product/decisions.md` : D-022 passe de Phase 3 à Phase 1, avant FS-02, avec échéance avant le gel de `video.md` et la montée en charge.
- `docs/Product/prd.md` : le jalon D-022 de la table des questions ouvertes est aligné sur Phase 1, avant FS-02.
- `docs/Conformite/moderation-regles.md` : délai de contestation fixé à 30 jours et deuxième relecture maintenus comme décision déjà écrite ; le recours anonyme n'est plus renvoyé en arbitrage.
- `docs/Conformite/confidentialite-visiteur.md` : le recours anonyme est écrit comme décision déjà prise, sans option à trancher.
- `docs/Conformite/conservation.md` : la vidéo retirée est conservée 30 jours, avec renvoi à `contestation.md` ; l'ancien délai de sept jours à confirmer est supprimé.
- `docs/Technique/adr-002-identite-session.md` : le retour à sept jours porte sur les comptes vérifiés selon D-020 ; l'hypothèse de panel visiteur consenti est retirée.

## Points restant à arbitrer

- D-009, stack `mobile`, `web` et `desktop`, point A-01.
- D-022, budget CDN et modération, point A-02.
- D-023, cibles numériques du client `desktop` et machine de référence, point A-03.
- Équipe et effectif, point A-04.
- Date de lancement et calendrier, point A-05.
- D-010, règle N2, point A-06.
- D-011, nom et privilèges du niveau organisations payant, point A-07.
- Langues après le français, point A-08.
- Modèle de modération, point A-09.
- Seuil de fil non vide, point A-10.
- Niveau OWASP ASVS visé, point A-11.
- Qualification juridique et périmètre RGPD, point A-12.
- Valeurs à confirmer sans choix préalable : profils R1 et R2, seuils d'alerte, éventuel plafond de lecture, durées marquées à confirmer dans `Conformite/conservation.md`, titulaires à nommer et validation juridique par conseil local.

## Conclusion

Tous les contrôles demandés sont verts après correction. Cohérence confirmée, Error 0, warning 0.
