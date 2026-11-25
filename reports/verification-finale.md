# Vérification finale de la documentation Pro

**Date** : 25 novembre 2026
**Périmètre** : racine `/home/espoir-loemba/work/Projects/pro`. Cinquante-huit fichiers sous `docs/`, dont `README.md`, et deux fichiers sous `reports/`, dont le présent rapport. Toutes les commandes sont exécutées depuis la racine.
**Méthode** : les commandes 3 et 4 sont reproduites avec des classes de caractères équivalentes, afin de ne pas réintroduire dans ce rapport les chaînes qu'elles recherchent. Le motif CJK de la commande 4 n'est pas reproduit ; il a été exécuté tel quel.

## Contrôles mécaniques

| N° | Commande | Résultat |
|---:|---|---|
| 1 | `grep -rnP '\x{2014}\|\x{2013}' docs reports` | Vide, 0 ligne. Vert. |
| 2 | `grep -rnP '[\x{3400}-\x{9FFF}\x{3040}-\x{30FF}\x{AC00}-\x{D7AF}]' docs reports` | Vide, 0 ligne. Vert. |
| 3 | `grep -rniE 'T[O]DO\|F[I]XME\|T[B]D\|X[X]X' docs reports` | Vide, 0 ligne. Vert. |
| 4 | `grep -rniE 'Correct[i]on appliquée\|writ[e]s down\|[motif CJK de la consigne]\|hypoth[eè]ses tu[eé]es\|une hypoth[eè]se est tu[eé]e\|tr[i]o\|ADR d.architectur[e]\|d[eé]cision produit : quatre niveaux\|anglais d[eè]s que possible\|v[eé]rifications finalis[eé]es pour 1 000 sessions\|cohorte visiteur [àa] sept jo[u]rs\|co[eû]t par vid[eé]o vue compris dans le budget\|messager[i]e\.md\|acquisition-cong[o]\.md\|d[eé]cions' docs reports` | Dix-huit lignes brutes, sept sous `docs/` et onze sous `reports/`. Vert avec exceptions documentées : aucune coquille dans `docs/`, sept lignes sont des formulations canoniques de la règle J7 exigées par le contrôle de cohérence, onze lignes sont des citations historiques de l'audit. Un contrôle complémentaire sur `docs/`, sans le motif de la règle J7, est vide. |
| 5 | `grep -rnEo '\]\([^)]+' docs reports \| while IFS=: read -r f l m; do p=${m#](}; p=${p%%#*}; case "$p" in http*\|\#*) continue;; esac; test -e "$(dirname "$f")/$p" \|\| echo "$f:$l $p"; done` | Zéro lien relatif cassé. Vert. |
| 6 | `grep -oE 'FS-[0-9]{2}' docs/Product/prd.md \| sort -u` ; idem pour `US-[0-9]{2}` dans `docs/UX/userstories.md` et `D-[0-9]{3}` dans `docs/Product/decisions.md` ; `grep -oE '\bH[0-9]\b\|\bO[0-9]\b' docs/UX/ux-research.md \| sort -u` | FS-01 à FS-11, US-01 à US-16 et D-001 à D-022 présents sans saut. H1 à H8 et O1 à O5 présents. Vert. |
| 7 | `grep -c '^```mermaid'` et `grep -c '^```'` sur les douze fichiers désignés | Au moins un bloc Mermaid dans chacun des douze fichiers ; nombre de délimiteurs toujours pair, donc blocs fermés par trois backticks. Vert. |
| 8 | `find docs -name '*.md' \| while read -r f; do [ "$(wc -l < "$f")" -ge 12 ] \|\| echo "$f"; done` | Zéro fichier court après correction. `docs/UX/usertories.md` avait cinq lignes et en contient désormais vingt. Vert. |

## Contrôles de cohérence canonique

| Contrôle | Résultat |
|---|---|
| Formulation langues exacte dans `vision.md`, `manifeste.md`, `prd.md`, `decisions.md`, `ux-research.md`, `userflow.md` | Présente dans les six fichiers. `userflow.md` a été complété. Vert. |
| Règle de sous-titrage D-021 exacte dans `decisions.md`, `prd.md`, `userflow.md`, `ux-research.md` | Présente dans les quatre fichiers. Vert. |
| Règle J7 exacte dans `decisions.md` et `mesure.md` | Présente dans les deux fichiers. `mesure.md` a été alignée. Vert. |
| Métrique et formule dans `vision.md`, `manifeste.md`, `mesure.md` | Nom canonique et formule présents dans les trois fichiers. `manifeste.md` et `mesure.md` ont été complétés. Vert. |
| D-005 phases 1 à 4, Phase 5 payante non définie, aucun classement payant dans la recherche | Formulation cohérente dans `decisions.md`, `roadmap.md`, `vision.md`, `manifeste.md` et `prd.md`. Vert. |
| Dix-huit événements canoniques, champs de dimension et conservation dans `mesure.md` et `observation.md` | Dix-huit événements présents dans les deux fichiers ; `city`, `trade`, `campaign_ref` et 30 jours présents. `observation.md` utilisait une écriture en toutes lettres, désormais alignée. Vert. |
| Dix champs de `appeal` dans `prd.md` et `donnees.md` | Les dix champs sont listés à l'identique dans les deux fichiers. Vert. |
| WCAG 2.2 AA, 24 sur 24 CSS px minimum, 44 pixels comme objectif | Présent dans `prd.md` et `userflow.md`, les deux fichiers qui portent des cibles d'interface. Les fiches `securite.md` et `confidentialite-visiteur.md` ne portent pas de cible tactile, donc aucun écart. Vert. |
| `docs/README.md` liste tous les fichiers présents | Cinquante-huit fichiers recensés, y compris les nouveaux artefacts et les alias. Vert. |

## Corrections appliquées

- `docs/UX/userflow.md` : ajout de la formulation canonique sur les langues, absente du fichier.
- `docs/Product/mesure.md` : formulation exacte de la règle J7, nom canonique de la métrique d'acquisition et formule ajoutés aux règles communes.
- `docs/Product/manifeste.md` : formule canonique de la métrique d'acquisition ajoutée à la liste des mesures suivies.
- `docs/Technique/observation.md` : durée de conservation des événements écrite « 30 jours » au lieu de la forme en toutes lettres, pour aligner le schéma sur le dictionnaire.
- `docs/UX/usertories.md` : fichier de cinq lignes étendu à vingt lignes avec le rôle de l'alias, le contenu du backlog canonique, la règle de mise à jour et les liens. La mention de l'ancien nom est conservée.
- `docs/README.md` : liste exhaustive des cinquante-huit fichiers, ajout des nouveaux artefacts, mise à jour de la section d'état et des règles de mise à jour.
- `reports/audit-cadrage-pro.md` : typo corrigée, checklist de numérotation D portée à D-022, section « État après remédiation » ajoutée.

Aucune modification n'a été apportée aux research_notes.

## Décisions humaines encore ouvertes

- D-009 : stack mobile et web à trancher dans l'ADR unique, avant le premier sprint.
- D-010 : règle de vérification N2 pour les candidatures, avant la Phase 2.
- D-011 : nom et privilèges du niveau organisations payant, avant la Phase 5.
- D-022 : budget CDN et modération, avec seuil de coût par vue, avant la Phase 3.
- Effectif, durée du MVP et date de lancement à confirmer par le planning.
- Responsables à nommer pour la produit, le design, la technique, la modération, le support et chaque ville, ainsi que les titulaires de l'astreinte et le numéro d'urgence.
- Cibles, seuils, propriétaires de mesure, durée de conservation des agrégats et ratio de contraste visé à inscrire au registre.
- Modèle bénévole ou salarié de la modération, second relecteur par ville et exercice à blanc de l'astreinte.
- Métiers confirmés par ville et seuil de fil non vide, avec repli vers le fil général.
- Durée de l'expérimentation, effectif et effet minimal détectable, ainsi que le seuil et la phase d'un éventuel plafond de lecture.

## Conclusion

Aucun défaut documentaire résiduel n'est constaté après les corrections ci-dessus. Le contrôle 4, exécuté à la lettre, n'est pas vide : ses dix-huit lignes sont sept formulations canoniques de la règle J7, exigées par le contrôle de cohérence, et onze citations historiques du rapport d'audit, conservées dans leur périmètre de modification. Ces occurrences sont documentées comme exceptions et ne sont pas des coquilles. Les autres contrôles sont verts sans exception.

Error 0, warning 0 pour la documentation livrée.
