# AGENT.md

**Rôle.** Source canonique unique pour tout agent qui travaille sur Pro. `CLAUDE.md` renvoie ici et ne duplique aucune règle.
**Langue.** Français. Le ton est humain, direct, sans texte robotique.
**Typographie.** Aucun tiret cadratin, aucun tiret demi-cadratin, aucun caractère chinois, japonais ou coréen, aucun emoji, aucun marqueur de correction en attente. Quand un titulaire ou un choix manque, écrire « à nommer » ou « à trancher ».
**Règle d'or.** Ne pas coder pour coder. Optimiser, mesurer, sécuriser, documenter. Un code rapide et sûr vaut mieux qu'un code écrit vite.
**Titulaire par défaut.** Espoir LOEMBA, `@Espoir-Loem`, chef de projet et auteur par défaut des commits, tags annotés, releases, notes de release et messages publiés sur GitHub. Profil vérifié le 25 novembre 2026 : https://github.com/Espoir-Loem. L'email public n'est pas renseigné ; l'adresse de signature sera validée par le titulaire avant le premier commit. Aucun autre nom n'est inventé.

## 1. Périmètre et posture

Pro est un réseau social professionnel de vidéo courte, avec chat, emplois et pages d'organisation.

- La lecture est publique sans compte. L'identité est demandée au premier geste social. La vérification n'arrive qu'avec une contrepartie.
- Les phases 1 à 4 sont gratuites. Aucun classement payant n'existe dans la recherche.
- Les deux premiers marchés sont la République du Congo et la RDC, traités séparément, puis l'Afrique, puis le monde. Le français vient d'abord.
- Les clients `mobile`, `web` et `desktop` sont livrés ensemble. Le desktop est un exécutable Windows et macOS, léger et rapide, sans lenteur perceptible. Linux est différé.
- Aucun code n'est écrit avant la sortie de la Phase 0 et la levée des portes écrites à la section 4.
- Aucun élément d'interface n'est ajouté pour décorer. Chaque élément est rattaché à une FS, une US, un O, un H ou une exigence d'accessibilité. Sinon il est retiré.

## 2. Sources de vérité

| Fichier | Rôle |
|---|---|
| `docs/README.md` | Index de la documentation et règles de mise à jour |
| `docs/Product/vision.md` | Pourquoi Pro existe |
| `docs/Product/prd.md` | Périmètre MVP, FS, définition de terminé à sept conditions, section 10.1 sur D-024 |
| `docs/Product/decisions.md` | Registre canonique des décisions retenues et des questions ouvertes |
| `docs/Product/arbitrage.md` | Grille A-01 à A-13 et procédure d'inscription d'un arbitrage |
| `docs/Product/roadmap.md` | Phases, dépendances et critères de sortie |
| `docs/Technique/adr-001-stack.md` | Stack retenue en D-009 |
| `docs/Technique/README.md` | Fiches techniques et modèle ADR unique |
| `docs/UX/userstories.md`, `docs/UX/userflow.md`, `docs/UX/design-principles.md` | Histoires, parcours et principes opposables en revue d'interface |
| `docs/Redaction/ia-defauts-et-tips.md` | Voix humaine et tics de rédaction automatique à éviter |
| `memoires/` | Pistes de raisonnement datées, sources et conséquences |

Ordre de prévalence en cas de divergence : `docs/Product/decisions.md`, puis `docs/Product/prd.md`, puis l'ADR concerné, puis les fiches techniques, puis `memoires/`. Les rapports de `reports/` sont des snapshots datés et ne font pas foi sur l'état courant. Toute divergence est corrigée dans la source de vérité, puis tracée dans un avenant.

## 3. Décisions opposables et questions ouvertes

Décisions retenues : D-001 à D-024. Arbitrages inscrits au registre sans numéro D : A-04, A-05, A-08, A-09 et A-10.

Questions ouvertes au registre : aucune au 26 novembre 2026. Point A-12 à lever selon `docs/Product/arbitrage.md` ; A-01 à A-11 et A-13 sont arbitrés. A-04, A-05, A-08, A-09 et A-10 sont inscrits dans la section des arbitrages du registre, sans numéro D supplémentaire. A-09 retient une couverture de 08:00 à 20:00 en heure locale avec astreinte P1 hors plage, et un renfort bénévole coopté par le référent ville avec engagement écrit et relecture obligatoire. Le point A-13 précise la portée mobile de D-024 sans rouvrir D-024.

Aucune question ouverte n'entre dans un sprint avant son inscription au registre avec date, motif, propriétaire, source liée, portée et historique.

Le porteur unique cumule temporairement les rôles de propriétaire technique, de recherche, de responsable des villes, d'astreinte, de relecteur et de responsable des mesures. Cette accumulation est une décision intérimaire datée du 25 novembre 2026, inscrite au registre le 26 novembre 2026 au point A-04. L'effectif du PRD reste une référence de planification, pas un engagement. Les prestataires du client `desktop` sont à nommer avant le premier commit de code de stack. L'avis juridique local reste externe et à nommer avant le choix de l'hébergeur et de la région de stockage. Toute délégation future est écrite puis assignée explicitement.

Les outils IA sont des outils d'accélération, jamais des auteurs. Ils ne signent aucun commit, aucune release et aucun message publié. Aucun trailer de co-auteur n'est accepté. L'identité Espoir LOEMBA reste l'auteur de tout artefact publié. Les outils sollicités, leur finalité et leurs limites sont consignés dans un avenant distinct.

Toute demande qui contredit une décision retenue impose une réouverture écrite avec la nouvelle preuve, la date, la décision remplacée, les documents touchés et la ligne d'historique. Aucune modification silencieuse n'est acceptée.

## 4. Portes avant le premier commit de code

1. Phase 0 terminée : dix jours ouvrés, huit entretiens, quatre réserves, Brazzaville et Kinshasa distincts, H1 à H8 validés avec seuils chiffrés, validateur nommé, preuves archivées et opportunité O écrite.
2. D-009 inscrite et ADR 001 à jour, avec propriétaire technique nommé.
3. A-03 arbitrée le 26 novembre 2026 : cinq cibles de revue, machine modeste Windows 11 et macOS supportés à 2 cœurs et 4 Go de RAM avec SSD, 30 lancements à froid par système, p75 et traces jointes, revue le 26 décembre 2026. Aucune valeur n'est présentée comme mesurée sans mesure.
4. A-04 et A-05 arbitrés et inscrits le 26 novembre 2026 : porteur unique intérimaire, outils IA jamais auteurs, prestataires `desktop` à nommer avant le premier commit de code de stack, aucun lancement daté et jalons par critères de sortie.
5. A-12 : qualification juridique écrite par un conseil local. L'hébergeur et la région de stockage ne sont arrêtés qu'après.
6. D-022 inscrite le 26 novembre 2026 : 1 000 USD par mois, 500 USD par ville, mois civil, seuil de 0,001 USD par vue.
7. A-13 arbitrée le 26 novembre 2026 : six catégories servies sans binaire natif sur `mobile`, à savoir règles, contenus, textes et traductions, taxonomies, indicateurs de fonctionnalité et valeurs de configuration. Aucun code exécutable téléchargé, retour au binaire natif et au circuit du store si une règle change, preuves Apple et Google consultées le 26 novembre 2026 et propriétaire intérimaire Espoir LOEMBA.

Avant toute ouverture publique, les points A-06 à A-11 sont arbitrés depuis le 26 novembre 2026, la file de modération est armée, l'astreinte est nominée et le test à blanc du signalement visiteur jusqu'à la notification d'auteur est réussi. La condition 7 de la définition de terminé exige la preuve de signature, de retour arrière et de non interruption de session sur les trois clients.

## 5. Stack retenue, D-009

| Couche | Choix | Contrainte |
|---|---|---|
| Base de compilation | Node 26 LTS, minimum Node 22.13.x | Node 27 est alpha et interdit. Aucune version `latest`, `canary`, `beta`, `rc` ou alpha |
| `web` | React et TypeScript, rendu DOM | Accessibilité WCAG 2.2 AA, déploiement côté serveur selon D-024 |
| `mobile` | React Native via Expo managé, SDK 58 et React Native 0.88 | Périmètre hors binaire natif limité aux six catégories de A-13 |
| `desktop` | React et TypeScript dans Tauri, coque Rust minimale | Windows et macOS, paquet signé, vérification avant installation, retour arrière, Linux différé |
| `api` | NestJS, TypeScript, Postgres et Prisma | Lecture et écriture séparées, file asynchrone durable |
| Règles partagées | `packages/domain` | Contrats typés, règles de visibilité, noms d'événements, constantes de décision |
| Médias | Stockage objet compatible S3 et CDN derrière une interface | Fournisseur dans le cadre du budget D-022, retrait EXIF avant stockage |
| Sous-titres | Service de transcription derrière une interface | Générés puis corrigés par l'auteur avant publication selon D-021 |

Rust est la seule exception à tout TypeScript, et uniquement pour la coque desktop signée. L'interface, le backend et les règles partagées restent en TypeScript. Les lockfiles sont commités. Les mises à jour de dépendances passent par un outil automatisé et une CI complète.

## 6. Invariants techniques

- D-016 : séparation du chemin de lecture et du chemin d'écriture. Un cache n'est jamais une autorisation. `decision_visibilite` est appliquée au moment de la lecture, malgré le cache et le CDN.
- D-012 : aucun identifiant permanent pour le visiteur, aucun identifiant d'appareil, d'installation ou de machine. Jeton visiteur court, non durable, rotatif.
- D-013 : notifications push réservées aux niveaux N1 et suivants. Aucun `push_subscription` sans `account_id`.
- D-015 : événements de session conservés trente jours. La dimension `plateforme` prend `mobile`, `web` et `desktop`, distincte de `city`, `trade` et `campaign_ref`.
- D-020 : la mesure à sept jours porte seulement sur les comptes avec email vérifié. Aucune cohorte visiteur à sept jours.
- D-019 : aucun classement payant dans la recherche.
- D-021 : une vidéo avec son reste en brouillon si la correction des sous-titres n'est pas faite par l'auteur.
- D-024 : `web` mis à jour côté serveur avec session préservée, `desktop` par paquet signé avec retour arrière, `mobile` par les six catégories de A-13 servi sans binaire natif. Aucune mise à jour ne coupe une session, ne contourne la modération, ne change une décision sans trace dans le journal avec acteur `system` et identifiant de règle.
- D-014 : modération en deux temps, texte vérifiable avant publication, vidéo en `pending_review`, signalement ouvert aux visiteurs. Journal d'audit en ajout seul.
- Acteurs réservés : `system`, `moderateur`, `auteur`. Aucune réponse publique ne contient email, téléphone, jeton push, jeton de session brut ou donnée de vérification. Les messages d'erreur restent neutres.
- Zéro CVE connue et non traitée au merge et à la release.

## 7. Règles d'écriture du code

- TDD obligatoire : écrire le test qui échoue, écrire le minimum qui le fait passer, puis refactoriser. Le test et le code sont dans le même commit logique.
- Un commit par changement logique ou par algorithme. Une fonction fait un traitement. Une classe porte une intention. Aucune duplication de logique, de fonction, de classe ou de fichier. Le code partagé va dans `packages/domain`.
- SOLID et KISS sont opposables en revue. Injection de dépendances et inversion de contrôle obligatoires. Aucun état global caché. Aucune abstraction spéculative.
- Production ready dès le premier commit. Pas de raccourci temporaire, pas de configuration locale seule, pas de secret dans le dépôt.
- Avant de corriger un bug, lire la documentation et le code source de la librairie concernée. Écrire un test qui reproduit le bug avant la correction. Si le raisonnement vaut la peine d'être gardé, écrire une note dans `memoires/`.
- Utiliser de vraies librairies évaluées : mainteneur, historique de sécurité, licence, OSSF Scorecard et dépendances transitives. Aucune librairie inventée, aucun paquet choisi pour son apparence.
- Toute vérification déterministe devient un script dans `scripts/` et une étape CI. Les tokens sont réservés aux échecs, aux arbitrages et au jugement de conception.
- Aucune fonction, méthode ou composant ne dépasse dix lignes de logique effective. Les lignes vides, les lignes de signature et les accolades seules ne comptent pas. Le seuil est appliqué par ESLint et Clippy.
- Aucune logique dans les fichiers TSX. Un composant ne fait que du rendu. Toute logique va dans un hook ou un module TypeScript dédié.
- Un seul appel à `.map()` par fichier TSX, jamais imbriqué. Le deuxième appel est bloqué par `scripts/check_code_style.py`.
- La réutilisation et la factorisation sont prioritaires. Aucune duplication de logique, de fonction, de classe ou de fichier. Le code partagé va dans `packages/domain`.
- Aucun commentaire dans le code, sauf les commentaires de documentation `/** ... */` en TypeScript et `///` ou `//!` en Rust. Les commentaires en ligne sont interdits.
- Tout code est en anglais : identifiants, messages, chaînes techniques et noms de fichiers de code. La documentation produit et les rapports restent en français.

## 8. Sécurité, versions et chaîne d'approvisionnement

- Le seuil est zéro CVE connue et non traitée au merge et à la release. Ce n'est pas une promesse d'absence absolue dans le temps. Un monitoring continu réévalue chaque nouvelle alerte.
- Sur chaque pull request : revue du lockfile, scan SCA, SAST, recherche de secrets, contrôle des licences, typecheck, lint, tests unitaires, d'intégration et de contrat.
- À chaque release : SBOM CycloneDX signé avec `cosign` 3.1.6, VEX CycloneDX daté, reliés au digest de l'artefact, notes générées par CI et preuve de passe CI. Une exception est bornée avec propriétaire, contrôle compensatoire, date d'expiration et statut VEX.
- Niveau OWASP ASVS 2 visé depuis l'arbitrage A-11 du 26 novembre 2026. Les outils épinglés et les contrôles de `docs/Technique/securite.md` s'appliquent dès maintenant et sont rejoués sur les trois clients.
- Desktop : signature et intégrité vérifiées avant installation, retour à la version précédente en cas d'échec, session en cours non interrompue, aucun identifiant machine écrit.
- Aucun co-auteur de modèle. Aucun trailer `Co-authored-by` pour Claude, freecode, opencode ou tout autre modèle. Les commits sont signés par un humain nommé.

## 9. Structure du dépôt

```
apps/mobile/
apps/web/
apps/desktop/
packages/api/
packages/domain/
scripts/
memoires/
docs/
reports/
```

Le dossier canonique du client mobile est `apps/mobile`. Chaque application garde ses tests locaux. Les règles partagées et les contrats typés restent dans `packages/domain`. Les scripts déterministes restent dans `scripts/`.

## 10. Git, branches, commits et releases

- Branches permanentes : `main`, `staging`, `develop`. Aucun push direct.
- Branches de travail : `feature/*`, `bugfix/*`, `refactor/*` depuis `develop` ; `hotfix/*` depuis `main`.
- Chemin : pull request vers `develop`, puis `develop` vers `staging`, puis `staging` vers `main`. Un hotfix retourne ensuite dans `staging` et `develop`.
- Conventional Commits validés par commitlint et hook local. `feat` donne une version mineure, `fix` une corrective, `BREAKING CHANGE` une majeure.
- Chaque changement logique ou algorithme a son commit, avec son test. Chaque fonction a un traitement, chaque classe une intention.
- Tags annotés `vX.Y.Z` sur `main`. GitHub Release généré par CI, jamais à la main, avec notes issues des commits, SBOM signé, artefacts signés et preuve CI.
- Aucun co-auteur de modèle, aucun trailer `Co-authored-by`. L'auteur par défaut des commits, tags annotés, releases, notes de release et messages publiés sur GitHub est Espoir LOEMBA (`@Espoir-Loem`), chef de projet. L'adresse email de signature est validée par le titulaire avant le premier commit.
- Tout automatisme que nous contrôlons sur GitHub porte un nom de la forme `Pro[<Name>]`. La liste fermée est `Pro[CI]` pour les contrôles et les commits de CI, `Pro[Info]` pour les commentaires et messages informatifs, `Pro[Release]` pour les releases. Aucun bot générique n'est laissé sans préfixe. Les bots natifs de GitHub ne sont pas renommables et leur usage doit être documenté dans un avenant.
- Un seul fichier par commit, sans exception. Un changement qui touche plusieurs fichiers est découpé en autant de commits que de fichiers.
- Aucune pull request sans issue ouverte référencée dans son corps avec `Closes #<numéro>`. Le contrôle bloque toute référence absente, fermée ou divergente.
- Aucune revendication d'issue par commande de prise en charge. L'assignation est explicite et décidée par le porteur ou le propriétaire désigné.
- Chaque issue contient un objectif, des sous-tâches vérifiables, une définition de terminé, un KPI associé ou la mention absent, et un propriétaire nommé ou la mention à nommer.
- Le GitHub Project `Pro - Suivi du projet` est la source de vérité de l'avancement. Ses champs sont Statut, Priorité, Domaine et KPI. Toute issue créée y est ajoutée comme item avec ses champs renseignés.
- Les KPI bugs, UX, produit et SEO sont définis dans `docs/Product/kpi.md`. Toute cible, tout propriétaire et tout seuil d'alerte sont nommés par décision écrite avant publication.

## 11. Tests et CI

- Tests unitaires, d'intégration, de contrat, de bout en bout et crossplateforme sur `mobile`, `web` et `desktop`.
- Le test de non régression T1 est rejoué sur les trois clients.
- Le contrôle D-024 de signature, retour arrière et non interruption de session est exécuté avant FS-01 et rejoué en revue de sortie MVP.
- Accessibilité WCAG 2.2 AA : cibles de 24 sur 24 pixels CSS au minimum, objectif 44 pixels, contraste 4,5:1 pour le texte courant et 3:1 pour les grands textes et composants.
- Performance desktop : taille installateur, démarrage à froid, changement de vue, mémoire au repos et latence de navigation selon A-03, mesurés sur la machine de référence modeste. Aucune valeur inventée.
- La CI bloque le merge sur toute erreur de typecheck, lint, test, accessibilité, scan de sécurité ou CVE connue non traitée. Les trois clients sont compilés et testés sur chaque pull request.
- Le contrôle `scripts/check_pr_issue.py` vérifie qu'une pull request référence une issue ouverte et rejette toute référence divergente.
- Le contrôle `scripts/check_kpi.py` vérifie les sections et les dix identifiants de `docs/Product/kpi.md` avant chaque fusion.

## 12. Design et contenu

- Aucune UI décorative. Chaque élément est rattaché à une FS, une US, un O, un H ou une exigence d'accessibilité.
- Le design est professionnel, propre, réfléchi et humain. Pas de couleurs ni de polices qui font IA. Pas de palette par défaut. Pas d'emoji, pas de faux icônes.
- Une seule famille typographique justifiée par écrit. Les tokens de couleur sont documentés avec leur contraste AA. Les sources sont archivées dans `memoires/`.
- Tailwind ou tout autre outil reste un détail d'implémentation, jamais une source de style.
- Avant de produire une interface, rechercher en profondeur les directives WCAG 2.2 et les guides natifs Windows et macOS. Si le doute reste, rechercher encore avant de générer.
- Éviter le texte robotique. Suivre `docs/Redaction/ia-defauts-et-tips.md`.

## 13. Automatisation et économie de tokens

- Toute vérification déterministe devient un script puis une étape CI.
- Le contrôle documentaire est porté par `scripts/check_docs.py`, testé par `scripts/test_check_docs.py` et rejoué par `.github/workflows/documentation.yml` sur chaque push et chaque pull request.
- Le contrôle de style est porté par `scripts/check_code_style.py`, testé par `scripts/test_check_code_style.py` et rejoué par les mêmes étapes.
- La configuration est épinglée dans `package.json`, `package-lock.json`, `tsconfig.json`, `vitest.config.ts`, `eslint.config.mjs`, `.prettierrc.json`, `pyproject.toml`, `rustfmt.toml`, `clippy.toml`, `rust-toolchain.toml` et `.pre-commit-config.yaml`.
- Les commandes `npm run check` et `pre-commit run --all-files` rejouent l'ensemble des contrôles locaux avant toute pull request.
- Un script est nommé clairement, documenté, idempotent et exécutable sans contexte humain.
- Si un audit ou un modèle ne sait pas faire une vérification de façon fiable, écrire le script plutôt que de deviner.
- Les tokens servent aux échecs, aux arbitrages et au jugement. Ils ne servent pas à refaire à la main ce qu'un script peut rejouer.

## 14. Conduite en cas de contradiction

Arrêter l'action. Vérifier l'ordre de prévalence de la section 2. Si la demande contredit une décision retenue, proposer une réouverture écrite et attendre un humain nommé. Si le doute porte sur un titulaire, une règle de store, une obligation juridique ou une cible chiffrée, poser une question plutôt que d'inventer. Aucune règle de store n'est affirmée sans preuve écrite. Aucun titulaire n'est inventé, sauf Espoir LOEMBA nommé plus haut et vérifié sur GitHub.

## 15. Mise à jour documentaire

- Après tout changement structurant, mettre à jour le registre, la grille d'arbitrage, l'ADR, les fiches touchées, l'index `docs/README.md` et une note de `memoires/` si le raisonnement vaut la peine d'être gardé.
- Écrire un avenant ou un rapport avec la date, le périmètre, les fichiers modifiés, les contrôles et la conclusion.
- Avant de terminer, vérifier : typographie interdite, liens relatifs résolus, numérotation FS, US et D sans saut, blocs Mermaid fermés, listes de décisions retenues et ouvertes à jour.
- `CLAUDE.md` reste un court renvoi vers ce fichier. Aucune règle n'est dupliquée ailleurs.
