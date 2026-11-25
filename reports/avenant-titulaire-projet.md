# Avenant titulaire par défaut

**Date.** 25 novembre 2026.
**Demande du porteur.** « le chef de Projet et pour les post c'est par defaut moi vas voir sur gh : Espoir LOEMBA ».
**Périmètre.** `AGENT.md`, `docs/Product/decisions.md`, `docs/Technique/responsabilites.md`, `memoires/`, `docs/README.md` et le présent rapport. Aucun code applicatif n'est écrit. Aucun commit n'est effectué, car le répertoire n'est pas encore un dépôt Git.

## Identité vérifiée

| Champ | Valeur observée | Source |
|---|---|---|
| Nom affiché | Espoir LOEMBA | API GitHub, 25 novembre 2026 |
| Login | @Espoir-Loem | API GitHub et profil public |
| Identifiant | 108950035 | API GitHub |
| Profil | https://github.com/Espoir-Loem | API GitHub |
| Localisation | R.Congo, Brazzaville | API GitHub |
| Email public | absent | API GitHub, champ vide |
| Activité affichée | Product Engineer, Designer, Dev tools builder | API GitHub |

Aucune adresse email n'est déduite ni inventée. Le champ reste à valider par le titulaire avant le premier commit.

## Rôle par défaut

Espoir LOEMBA est le chef de projet et l'auteur par défaut des commits, tags annotés, releases, notes de release et messages publiés sur GitHub. Cette règle est inscrite dans `AGENT.md` et dans la matrice des responsabilités. Aucun co-auteur de modèle n'est accepté, aucun trailer `Co-authored-by` n'est ajouté.

Le mot « post » est traité comme publication sur GitHub. Si le porteur visait les publications dans l'application Pro, cette portée reste à préciser et n'est pas inventée dans ce rapport.

Les autres titulaires restent à nommer : propriétaire technique, recherche, villes, astreinte, relecteurs, mesures et validation juridique locale. Leur absence n'est pas comblée par défaut.

## Fichiers modifiés

| Fichier | Modification |
|---|---|
| `AGENT.md` | Titulaire par défaut ajouté en tête, règle de signature précisée à la section Git, règle de non invention ajustée |
| `docs/Product/decisions.md` | Note de titulaire par défaut ajoutée, registre en version 5 |
| `docs/Technique/responsabilites.md` | Direction projet et auteur Git par défaut attribués, autres rôles laissés à nommer |
| `memoires/README.md` | Note sur le titulaire ajoutée à la liste |
| `docs/README.md` | Pointeur vers le présent avenant ajouté |
| `memoires/2026-11-25-titulaire-projet.md` | Raison du choix, sources et conséquence |
| `reports/avenant-titulaire-projet.md` | Présent rapport |

## Contrôles

| Contrôle | Attendu | Résultat |
|---|---|---|
| Recherche des tirets interdits | Aucune occurrence | Vide, conforme |
| Recherche des caractères chinois, japonais ou coréens | Aucune occurrence | Vide, conforme |
| Recherche des marqueurs de correction en attente | Aucune occurrence | Vide, conforme |
| Résolution des liens relatifs | Zéro lien cassé | 458 liens résolus, 0 cassé sur 69 fichiers contrôlés |
| Numérotation FS, US, D et A | Sans saut | Conforme |
| Blocs Mermaid | Tous fermés | Conforme |
| Décisions retenues et questions ouvertes | D-001 à D-009, D-012 à D-021, D-023, D-024 retenues ; D-010, D-011, D-022 ouvertes | Conforme |
| Email de commit | Aucune adresse inventée | Conforme, à valider par le titulaire |
| Co-auteur de modèle | Aucun trailer de modèle | Conforme |

## Conclusion

Le chef de projet est nommé et vérifié sur GitHub. L'auteur Git par défaut est cadré sans inventer d'email ni ajouter de co-auteur de modèle. Le reste des titulaires demeure explicite et à nommer. Cohérence confirmée, Error 0, warning 0.
