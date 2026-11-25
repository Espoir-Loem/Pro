# Note de raisonnement, stack TypeScript

**Date.** 25 novembre 2026.
**Sujet.** Choix des familles de technologie pour `mobile`, `web`, `desktop` et le backend.

## Question

Quelles familles de technologie retenir pour livrer ensemble trois clients et un backend, avec une exigence de production, de performance desktop sans lenteur perceptible, de mise à jour automatique et de zéro CVE connue non traitée au merge et à la release ?

## Sources

- [Node.js Release Working Group, calendrier des versions](https://github.com/nodejs/release). Source primaire. Node 26 est en LTS active depuis le 28 octobre 2026, avec fin de vie prévue en avril 2029. Node 27 est en phase alpha depuis le 28 octobre 2026.
- [Expo, SDK 58](https://expo.dev/changelog/sdk-58). Source primaire. SDK 58 publié le 15 octobre 2026, construit pour React Native 0.88. Le minimum Node est 22.13.x.
- [Expo, statuts des versions](https://docs.expo.dev/more/release-statuses). Source primaire. Le support d'un SDK suit une fenêtre limitée, donc la montée de version doit être planifiée.
- [Expo, versions de SDK obsolètes](https://github.com/expo/fyi/blob/main/outdated-sdk-versions.md). Source primaire. Un SDK dépassé impose une migration avant de continuer les correctifs.
- [OWASP, Software Supply Chain Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html). Source de pratiques. Évaluation du fournisseur, de la maturité, de l'historique de sécurité, de la licence et des dépendances avant intégration.
- [OWASP, Dependency Graph and SBOM Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Dependency_Graph_SBOM_Cheat_Sheet.html). Source de pratiques. SBOM, assurance de l'intégrité et suivi continu.
- [NIST SP 800-204D, Software Supply Chain Security in DevSecOps CI/CD Pipelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204D.pdf). Source primaire. Contrôles de la chaîne d'approvisionnement dans les pipelines d'intégration et de livraison.
- [Cyber Security Centre Australia, 2026 Minimum Elements for a Software Bill of Materials](https://www.cyber.gov.au/publication/2026-minimum-elements-for-a-software-bill-of-materials-sbom). Source publique. Empreinte, licence et identifiants minimaux du SBOM.
- [Conventional Commits, spécification 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). Source de pratiques. Messages de commit lisibles et versionnement sémantique.
- [Git, documentation de git tag](https://git-scm.com/docs/git-tag). Source primaire. Tags annotés pour les releases.
- [GitHub, gestion des releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository). Source primaire. Génération des releases par CI.

## Options examinées

| Option | Motif pour | Motif contre | Source |
|---|---|---|---|
| Natif Kotlin et Swift pour le mobile | Accès natif complet, cycle de mise à jour maîtrisé par plateforme | Deux langages de plus, donc deux contextes de maintenance ; diverge de la direction tout TypeScript choisie par le porteur | Demande du porteur du 25 novembre 2026 |
| React Native via Expo CLI nu | Contrôle natif plus fin | Charge de maintenance iOS et Android plus lourde ; cycle de mise à jour JavaScript plus complexe | Expo, statuts des versions |
| React Native via Expo managé | Un seul langage pour les règles et l'interface, SDK supporté, cycle JavaScript documenté | La part modifiable hors binaire natif dépend des règles des stores, à valider en A-13 | Expo SDK 58, demande du porteur |
| Flutter sur les trois clients | Une seule base de code | Rendu web moins adapté à l'accessibilité DOM visée ; direction écartée par le porteur | Demande du porteur du 25 novembre 2026 |
| Electron pour le desktop | Interface TypeScript sans coque séparée | Taille installateur et mémoire au repos à revoir avec les cibles D-023 et A-03 | PRD section 9, A-03 |
| Tauri avec coque Rust minimale | Interface TypeScript, installateur léger, paquet signé, mémoire maîtrisée | Rust est une seconde famille de langage, limitée à la coque | PRD section 9, D-023, D-024 |
| NestJS, Postgres et Prisma pour le backend | Structure normative, schéma typé, adaptée à une équipe qui grandit | Plus de couches qu'une API minimale | Demande du porteur du 25 novembre 2026 |
| Go pour le backend | Binaire simple et sobre | Change la famille de langage et augmente le nombre de contextes | Demande du porteur du 25 novembre 2026 |

## Conclusion

La direction tout TypeScript est retenue. Le client `web` utilise React avec rendu DOM. Le client `desktop` utilise le même front React dans Tauri, avec Rust uniquement pour la coque signée, l'installateur Windows et macOS et la mise à jour. Le client `mobile` utilise React Native via Expo managé, SDK 58 et React Native 0.88. Le backend utilise NestJS, TypeScript, Postgres et Prisma. Node 26 LTS est la base de compilation ; Node 27 est interdit car alpha.

Le seuil de sécurité retenu est zéro CVE connue et non traitée au moment du merge et de la release. Ce n'est pas une garantie absolue dans le temps : un monitoring continu et une réévaluation à chaque alerte sont nécessaires. Toute dépendance est évaluée avant ajout sur le mainteneur, l'historique de sécurité, la licence, l'OSSF Scorecard et les dépendances transitives. Un SBOM CycloneDX signé est produit par release.

Les options écartées sont Flutter, le natif Kotlin et Swift comme socle unique, React Native CLI nu, Electron, et Go pour le backend. Le stockage objet compatible S3 et le CDN restent derrière une interface. Le fournisseur n'est pas choisi ici.

## Conséquence

Cette note alimente D-009 et l'ADR 001. Les fichiers touchés sont `../docs/Product/decisions.md`, `../docs/Product/arbitrage.md`, `../docs/Technique/adr-001-stack.md`, `../docs/Technique/README.md`, `../docs/Product/prd.md` et `../docs/README.md`. La grille A-01 est clôturée.

Les portes restées ouvertes sont A-12 pour la qualification juridique, D-022 pour le budget CDN et le fournisseur, A-13 pour la liste mobile hors binaire natif, A-03 pour les cibles numériques du desktop et A-02 pour le budget de modération. Aucun code n'est écrit avant leur levée, ainsi que celle de la Phase 0. Le propriétaire technique de la stack reste à nommer.

## Lien

- Décision : [D-009 dans le registre](../docs/Product/decisions.md).
- Question arbitrée : [A-01 dans la grille](../docs/Product/arbitrage.md).
- ADR : [ADR 001 stack](../docs/Technique/adr-001-stack.md).
