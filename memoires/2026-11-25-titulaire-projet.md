# Note de raisonnement, titulaire par défaut

**Date.** 25 novembre 2026.
**Sujet.** Identité du chef de projet et auteur par défaut des publications GitHub.

## Question

Quel nom humain utiliser par défaut pour la direction du projet, les commits, les tags annotés, les releases, les notes de release et les messages publiés sur GitHub ?

## Sources

- [API GitHub, utilisateur Espoir-Loem](https://api.github.com/users/Espoir-Loem). Consultée le 25 novembre 2026. Source primaire. Nom : Espoir LOEMBA. Identifiant : 108950035. Localisation : R.Congo, Brazzaville. Email public : absent. Bio : Product Engineer, Designer, Dev tools builder. Profil mis à jour le 15 novembre 2026.
- [Profil GitHub public](https://github.com/Espoir-Loem). Consulté le 25 novembre 2026. Source primaire. Login : @Espoir-Loem.

## Options examinées

| Option | Motif pour | Motif contre | Source |
|---|---|---|---|
| Inventer une adresse email de commit | Configuration git immédiate | Adresse fausse, contraire à l'interdiction d'inventer un titulaire | API GitHub, champ email vide |
| Utiliser seulement le login @Espoir-Loem | Vérifiable publiquement | Perd le nom complet demandé | Profil GitHub |
| Utiliser le nom complet et le login, puis valider l'adresse de signature avec le titulaire | Nom humain vérifiable, aucune donnée inventée | Adresse de signature encore absente | API GitHub et profil public |

## Conclusion

Espoir LOEMBA (`@Espoir-Loem`) est le chef de projet et l'auteur par défaut des commits, tags annotés, releases, notes de release et messages publiés sur GitHub. L'email public n'est pas renseigné sur le profil, donc aucune adresse n'est inventée. Une adresse de signature sera validée par le titulaire avant le premier commit. Aucun co-auteur de modèle n'est ajouté.

Le mot « post » est compris ici comme publication sur GitHub. Si le porteur visait les publications dans l'application Pro, cette portée reste à préciser et n'est pas inventée.

## Conséquence

Les fichiers touchés sont `../AGENT.md`, `../docs/Product/decisions.md`, `../docs/Technique/responsabilites.md`, `./README.md`, `../docs/README.md` et `../reports/avenant-titulaire-projet.md`. Les autres titulaires, notamment le propriétaire technique, la recherche, les villes, l'astreinte, les relecteurs, les mesures et la validation juridique locale, restent à nommer.

## Lien

- Source canonique des règles : [AGENT.md](../AGENT.md).
- Registre : [Décisions](../docs/Product/decisions.md).
- Matrice : [Responsabilités](../docs/Technique/responsabilites.md).
- Avenant : [Titulaire par défaut](../reports/avenant-titulaire-projet.md).
