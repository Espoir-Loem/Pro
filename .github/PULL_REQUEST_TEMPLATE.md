## Issue liée

Référence obligatoire : `Closes #<numéro>`. La pull request est bloquée sans issue ouverte référencée.

## Objet

Décrire le changement en une phrase.

## Contrôles

- [ ] Un seul fichier par commit
- [ ] Titre conventional commit
- [ ] Aucun co-auteur de modèle
- [ ] `npm run check` vert
- [ ] `python3 -m unittest discover -s scripts -p "test_*.py"` vert
- [ ] `uvx pre-commit run --all-files` vert
- [ ] Aucun code applicatif avant la levée des portes du premier sprint
