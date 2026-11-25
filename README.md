# Pro

**Description.** Réseau social professionnel vidéo courte, chat, emplois et pages organisation, pour la République du Congo et la RDC.

**Statut.** Cadrage documentaire et préparation du dépôt. Aucun code applicatif n'est écrit. Les portes du premier sprint restent ouvertes.

## 1. Lire le projet

Commencer par la [vision](./docs/Product/vision.md), puis le [PRD](./docs/Product/prd.md) et la [feuille de route](./docs/Product/roadmap.md). L'index complet des documents est dans [docs/README.md](./docs/README.md). Les règles de travail sont dans [AGENT.md](./AGENT.md).

## 2. Périmètre

Les clients `mobile`, `web` et `desktop` sont livrés ensemble. La lecture publique fonctionne sans compte. L'identité est demandée au premier geste social. La vérification intervient seulement avec contrepartie. Les phases 1 à 4 restent gratuites. Aucun classement payant n'entre dans la recherche.

La République du Congo et la RDC sont traitées séparément, puis vient l'Afrique, puis le monde. Le français vient d'abord. Windows et macOS sont visés pour le desktop, Linux est différé.

## 3. Organisation GitHub

- Aucune pull request sans issue ouverte référencée dans son corps.
- Aucune revendication d'issue par `/take`. L'assignation est explicite.
- Les tâches et les sous-tâches sont tenues dans le GitHub Project et dans chaque issue.
- Les KPI bugs, UX, produit et SEO sont définis dans [kpi.md](./docs/Product/kpi.md).
- Les règles SEO du web sont dans [seo-web.md](./docs/Technique/seo-web.md).

Les bots que le projet contrôle portent les noms `Pro[CI]`, `Pro[Info]` et `Pro[Release]`. Les bots natifs de GitHub ne sont pas renommables.

## 4. Contrôles locaux

```bash
npm ci --ignore-scripts
npm run check
python3 -m unittest discover -s scripts -p "test_*.py"
uvx pre-commit run --all-files
```

Les versions sont épinglées dans `package.json`, `package-lock.json`, `pyproject.toml` et `rust-toolchain.toml`. Aucune version `latest`, `canary`, `beta`, `rc` ou alpha n'est acceptée. Zéro CVE connue et non traitée est requis au merge et à la release.

## 5. Règle de commit

Un seul fichier par commit. Le titre suit la forme [Conventional Commits](https://www.conventionalcommits.org/). Aucun trailer `Co-authored-by`. L'identité retenue est Espoir LOEMBA (`hopcy.forcy@gmail.com`).
