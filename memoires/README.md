# Mémoires de raisonnement

**Statut.** ouvert le 25 novembre 2026.
**Rôle.** Conserver les pistes de raisonnement datées, les sources consultées et les conséquences, pour qu'un autre agent reprenne sans refaire la même recherche.
**Règle.** Ce dossier ne remplace pas `../docs/Product/decisions.md`. Le registre porte la décision opposable. Une note porte le chemin qui y mène, les options écartées et les sources. Aucune note ne crée de décision à elle seule.

## Nommage

Une note porte le nom `AAAA-MM-JJ-sujet-court.md`. Le modèle s'appelle `modele-de-note.md`. Une note n'est pas renommée après coup : une correction est ajoutée avec sa date, ou une nouvelle note est créée avec un lien vers la précédente.

## Structure minimale

Toute note contient, dans cet ordre :

1. la date et le sujet ;
2. une seule question vérifiable ;
3. les sources datées, avec distinction entre source primaire et avis ;
4. les options examinées, avec motif pour et motif contre ;
5. la conclusion, avec ce qui est retenu et ce qui est écarté ;
6. la conséquence, avec les fichiers touchés, les portes restées ouvertes et le propriétaire à nommer ;
7. le lien vers la décision, la question ou l'ADR concerné.

## Usages

- Écrire une note avant un arbitrage structurant, pas après avoir commencé le code.
- Garder les sources dans la note, pas seulement dans le chat.
- Ne pas recopier le registre des décisions. Le lien suffit.
- Ne pas écrire de marqueur de correction en attente. Utiliser « à nommer » ou « à trancher » quand un titulaire ou un choix manque.
- Aucun tiret cadratin, aucun tiret demi-cadratin, aucun caractère chinois, japonais ou coréen, aucun emoji.

## Notes présentes

- [2026-11-25-stack-typescript.md](./2026-11-25-stack-typescript.md), raisonnement derrière D-009.
- [2026-11-25-titulaire-projet.md](./2026-11-25-titulaire-projet.md), identité du chef de projet et auteur par défaut des publications GitHub.
- [2026-11-25-outillage-depot.md](./2026-11-25-outillage-depot.md), versions vérifiées de l'outillage du dépôt.
- [2026-11-26-outils-securite.md](./2026-11-26-outils-securite.md), versions vérifiées des contrôles SCA, SAST, secrets, licences, SBOM et VEX.
- [modele-de-note.md](./modele-de-note.md), modèle à recopier pour une nouvelle note.
