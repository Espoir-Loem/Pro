# Note outillage du dépôt

**Date.** 25 novembre 2026.
**Décision associée.** Ajout des règles de code, de formatage, de tests et de préfixe des bots demandées par le porteur.
**Méthode.** Versions vérifiées sur les registres officiels, licences lues via l'API GitHub ou le registre npm, score OSSF interrogé quand une entrée existe, empreintes des actions GitHub vérifiées par l'API.

## Outils retenus

| Outil | Version | Licence | Source | Observation |
|---|---|---|---|---|
| `pre-commit` | 4.7.0, exécuté via `uvx` | MIT, projet pre-commit | `uvx pre-commit validate-config` | Configuration validée localement, hooks rejoués sur tout le dépôt |
| `pre-commit/pre-commit-hooks` | v6.0.0 | MIT | API GitHub et scorecard OSSF | Score 5,6 au 2 novembre 2026, maintenance active, licence reconnue, politiques de permissions à surveiller |
| `astral-sh/ruff-pre-commit` | v0.17.6 | Apache-2.0 | API GitHub | Aucune entrée dans l'API scorecard au moment du contrôle, projet actif, empreinte épinglée |
| `compilerla/conventional-pre-commit` | v4.5.0 | Apache-2.0 | API GitHub | Aucune entrée dans l'API scorecard au moment du contrôle, projet actif, empreinte épinglée |
| TypeScript | 6.0.3 | Apache-2.0 | registre npm | Version stable retenue pour rester compatible avec `typescript-eslint` 8.74.0 |
| `typescript-eslint` | 8.74.0 | MIT | registre npm | La version 7 de TypeScript n'est pas encore dans la plage de compatibilité déclarée |
| ESLint | 10.15.0 | MIT | registre npm | Configuration plate, zéro avertissement à l'exécution |
| Prettier | 3.10.1 | MIT | registre npm | Markdown exclu pour préserver la rédaction canonique |
| Vitest | 5.1.2 | MIT | registre npm | Exécution sans fichier de test autorisée en attendant le premier code |
| `@types/node` | 26.6.10 | MIT | registre npm | Aligné sur Node 26.13.0 présent dans l'environnement |
| Rust | 1.100.0 | Apache-2.0 ou MIT | `rustc --version` | Outil local, composants `rustfmt` et `clippy` requis |

## Raisons des choix

TypeScript 7.0.2 est disponible, mais `typescript-eslint` 8.74.0 déclare une compatibilité strictement inférieure à 6.1.0. Le projet retient donc TypeScript 6.0.3, version stable et compatible, plutôt que de mélanger un compilateur non couvert par l'analyse statique.

Les actions GitHub sont épinglées par empreinte complète afin d'éviter un changement de code exécuté sans revue. Les dépendances npm sont épinglées dans `package.json` et le lockfile est commité. L'audit npm ne signale aucune vulnérabilité au 25 novembre 2026.

Le score OSSF de `pre-commit/pre-commit-hooks` n'est pas maximal. Les points faibles concernent surtout les autorisations de ses propres workflows et l'épinglage de ses actions internes. Ces faiblesses ne concernent pas le code du hook tel qu'il est exécuté ici, mais elles sont conservées comme risque résiduel et seront revues à chaque montée de version.

## Limites

Les bots natifs de GitHub ne peuvent pas être renommés. La règle `Pro[<Name>]` s'applique donc aux automatismes que le projet contrôle. Si Dependabot ou un autre bot natif est activé, un avenant devra en consigner le nom réel et la raison.

Les cibles numériques du desktop, le niveau ASVS et les titulaires nommés restent ouverts. Aucune configuration n'invente ces valeurs.
