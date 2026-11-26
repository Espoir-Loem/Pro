# Pro : grille d'arbitrage

**Statut** : version 6, 26 novembre 2026  
**Règle** : ce document prépare les choix, il ne les prend pas. Une option arbitrée porte sa date et son numéro de décision, sinon aucune option ci-dessous n'est retenue. Un arbitrage devient opposable seulement après inscription dans [decisions.md](./decisions.md) avec date, motif, propriétaire, source liée, portée et historique.  
**Documents liés** : [Registre des décisions](./decisions.md), [ADR stack](../Technique/adr-001-stack.md), [Performance](../Technique/performance.md), [Mesure](./mesure.md), [Roadmap](./roadmap.md), [Contestation](../Operations/contestation.md), [Lanceurs de métiers](../Growth/lanceurs-metiers.md), [Périmètre juridique](../Conformite/perimetre-juridique.md), [Responsabilités](../Technique/responsabilites.md).

Les décisions retenues D-001 à D-024 sont opposables, y compris D-010, D-011 et D-022 inscrites le 26 novembre 2026. Aucune question ouverte ne reste au registre. Les points A-01 à A-11 et A-13 sont arbitrés et renvoient aux décisions ou aux fiches techniques concernées. Les points A-04, A-05, A-08, A-09 et A-10 sont inscrits au registre le 26 novembre 2026 sans créer de décision numérotée supplémentaire. A-09 retient la couverture de 08:00 à 20:00 en heure locale avec astreinte P1 hors plage, et le renfort bénévole coopté et encadré. Le point A-13 précise la portée mobile de D-024 sans rouvrir cette décision. Le point A-12 reste à lever. Toute réouverture suit la procédure écrite à la fin de `decisions.md`.

## Mode d'emploi

1. Choisir une option par ligne, ou écrire une option nouvelle avec son motif.
2. Inscrire le choix dans `decisions.md` avec date, motif, propriétaire, source liée, portée et historique.
3. Mettre à jour les documents touchés indiqués dans le tableau.
4. Si le choix modifie le périmètre `mobile`, `web` ou `desktop`, appliquer la règle de la section 2 du PRD avant toute autre modification.
5. Tant qu'une ligne n'est pas passée en décision retenue, elle n'entre dans aucun sprint.
6. Les références A-01 à A-13 sont classées par échéance, pas par ordre numérique. Le point A-13 concerne le sprint 1 et figure dans la première table.

```mermaid
flowchart LR
  A["Périmètre juridique et budget"] --> B["Stack mobile, web, desktop"]
  B --> C["ADR unique puis architecture"]
  C --> D["Sprint 1"]
  E["Sortie Phase 0"] --> F["Règle N2 et langues par marché"]
  F --> G["Phase 2"]
  H["Modération et montée en charge"] --> I["Ouverture publique"]
```

## 1. Arbitrage avant le premier sprint

| Réf. | À arbitrer | Options ouvertes | Ce qu'il faut écrire | Documents touchés | Responsable | Échéance |
|---|---|---|---|---|---|---|
| A-01 | D-009 : stack `mobile`, `web` et `desktop`, arbitrée le 25 novembre 2026, voir D-009 | Clôturée. Option retenue : tout TypeScript, détaillée dans `../Technique/adr-001-stack.md` | Option retenue, versions LTS, familles de langages ou cadres, hébergeur après A-12, fournisseur CDN dans le cadre de D-022, propriétaire, date. Outils inscrits dans l'ADR unique. | `adr-001-stack.md`, `architecture.md`, `video.md`, `performance.md`, `roadmap.md` | Équipe produit et technique, titulaire à nommer | Atteinte le 25 novembre 2026 |
| A-02 | D-022 : budget CDN et modération | Arbitrée le 26 novembre 2026 : enveloppe mensuelle de 1 000 USD, 500 USD par ville, mois civil, seuil de 0,001 USD par vue. | Montant, devise, fenêtre, seuil et révision après 30 jours sont inscrits en D-022. Le fournisseur CDN n'est pas choisi par cet arbitrage. | `video.md`, `montee-en-charge.md`, `mesure.md`, `roadmap.md` | Espoir LOEMBA, intérimaire | Atteinte le 26 novembre 2026 |
| A-03 | D-023 : cibles numériques du client `desktop` | Arbitrée le 26 novembre 2026 : option 1, les cinq cibles proposées sont retenues comme cibles de revue. | Machine de référence arrêtée : Windows 11 et macOS en version supportée, 2 cœurs, 4 Go de RAM, SSD. Méthode : 30 lancements à froid par système, p75, traces jointes. Revue le 26 décembre 2026. Aucune valeur n'est présentée comme mesurée. | `prd.md` section 9, `performance.md`, `mesure.md`, définition de terminé | Espoir LOEMBA, intérimaire | Atteinte le 26 novembre 2026 |
| A-04 | Équipe et effectif | Arbitrée le 26 novembre 2026 : porteur unique et intérimaire appuyé par les outils IA, jamais auteurs. | L'effectif du PRD reste une référence de planification, pas un engagement. Aucune phase n'est raccourcie ni allongée par cet effectif. Les prestataires du client `desktop` sont à nommer avant le premier commit de code de stack. Toute délégation est écrite puis assignée explicitement. | `prd.md`, `roadmap.md`, `decisions.md`, `../Technique/responsabilites.md` | Espoir LOEMBA, intérimaire | Atteinte le 26 novembre 2026 |
| A-05 | Date de lancement et calendrier | Arbitrée le 26 novembre 2026 : jalons par critères de sortie, sans date de lancement fixée. | Aucune date de lancement n'est inventée. La date est à nommer avant le planning. Le recrutement des créateurs et l'astreinte sont déclenchés par les critères de sortie, pas par une date. La revue de performance du 26 décembre 2026 et la révision de D-022 après 30 jours d'exploitation ne sont pas des dates de lancement. | `roadmap.md`, `acquisition-brazzaville.md`, `acquisition-kinshasa.md`, `astreinte.md` | Espoir LOEMBA, intérimaire | Atteinte le 26 novembre 2026 |
| A-13 | Portée mobile de D-024, mise à jour sans cycle de store | Arbitrée le 26 novembre 2026 : option 1, éléments servis côté serveur seulement, liste fermée ci-dessous. | Six catégories servies sans binaire natif : règles, contenus, textes et traductions, taxonomies, indicateurs de fonctionnalité, valeurs de configuration. Aucun code exécutable n'est téléchargé. Retour au binaire natif et au circuit du store si une règle change. Preuves des deux stores ci-dessous. | `prd.md` section 10.1, `adr-001-stack.md`, `securite.md`, `confidentialite-visiteur.md`, définition de terminé | Espoir LOEMBA, intérimaire | Atteinte le 26 novembre 2026 |

## 2. Arbitrage avant la Phase 2

| Réf. | À arbitrer | Options ouvertes | Ce qu'il faut écrire | Documents touchés | Responsable | Échéance |
|---|---|---|---|---|---|---|
| A-06 | D-010 : règle N2 pour les candidatures | Arbitrée le 26 novembre 2026 : vérification seulement à la demande de l'employeur, voir D-010. | Règle, preuve acceptée, réversibilité du badge et événement dédié sont inscrits en D-010. | `prd.md` section 14, `verification-identite.md`, `userstories.md` US-16, `mesure.md` | Espoir LOEMBA, intérimaire | Atteinte le 26 novembre 2026 |
| A-07 | D-011 : nom et privilèges du niveau organisations payant | Arbitrée le 26 novembre 2026 : `Organisation Avancée`, avec statistiques avancées, voir D-011. | Nom, liste fermée des privilèges et phase d'entrée sont inscrits en D-011. D-019 interdit tout classement payant dans la recherche. | `roadmap.md` phase 5, `manifeste.md`, `prd.md` section 14.5, `decisions.md` | Espoir LOEMBA, intérimaire | Atteinte le 26 novembre 2026 |
| A-08 | Langues après le français | Arbitrée le 26 novembre 2026 : français seul jusqu'à la Phase 3. | Le français est la seule langue des phases 0, 1 et 2 et du terrain du cycle 1. Toute langue ajoutée à partir de la Phase 3 est inscrite au registre avec date, responsable et marché avant le premier contenu dans cette langue, selon D-008. Aucune date de langue n'est inventée ici. | `vision.md`, `prd.md`, `manifeste.md`, `decisions.md`, `ux-research.md` | Espoir LOEMBA, intérimaire | Atteinte le 26 novembre 2026 |

## 3. Arbitrage avant ouverture publique

| Réf. | À arbitrer | Options ouvertes | Ce qu'il faut écrire | Documents touchés | Responsable | Échéance |
|---|---|---|---|---|---|---|
| A-09 | Modèle de modération | Arbitrée le 26 novembre 2026 : noyau de 1 modérateur de garde et 1 relecteur par ville, renfort bénévole coopté par le référent ville et encadré, couverture de 08:00 à 20:00 en heure locale avec astreinte P1 hors plage. | Couverture, renfort, engagement écrit et relecture obligatoire sont écrits dans les documents d'opérations. Lien avec D-022 maintenu dans `montee-en-charge.md` par l'enveloppe par ville et le coût par vue. | `Operations/README.md`, `astreinte.md`, `montee-en-charge.md`, `journee-type-moderation.md`, `decisions.md` | Espoir LOEMBA, intérimaire | Atteinte le 26 novembre 2026 |
| A-10 | Seuil de fil non vide | Arbitrée le 26 novembre 2026 : aucun seuil, repli immédiat vers le fil général. | Aucun nombre minimal de vidéos par métier ou par ville n'est fixé. Si un métier n'a pas de vidéo modérée dans une ville, le fil général de cette ville est servi immédiatement. Aucun seuil ni repli n'est transposé d'une ville à l'autre. Chaque repli est écrit avec la ville, la date et le propriétaire. Les cibles de semis restent des hypothèses de planification. | `lanceurs-metiers.md`, `mesure.md`, `acquisition-brazzaville.md`, `acquisition-kinshasa.md`, `../Growth/README.md`, `../Operations/README.md`, `../Operations/animation-createurs.md` | Espoir LOEMBA, intérimaire | Atteinte le 26 novembre 2026 |
| A-11 | Niveau OWASP ASVS visé | Arbitrée le 26 novembre 2026 : niveau 2, sur le backend et les trois clients livrés ensemble. | Niveau, portée et propriétaire de la revue sont inscrits dans `securite.md` et `responsabilites.md`. | `securite.md`, `responsabilites.md`, définition de terminé | Espoir LOEMBA, intérimaire | Atteinte le 26 novembre 2026 |
| A-12 | Qualification juridique et périmètre RGPD | En attente d'avis externe. Aucune obligation n'est tranchée dans ce document. | Avis du conseil local, pays concernés et date restent à nommer. | `perimetre-juridique.md`, `union-europeenne.md`, `confidentialite-visiteur.md`, `adr-001-stack.md` | conseil local, à nommer | avant le choix de l'hébergeur, la région de stockage et la première migration |

## 4. À nommer sans arbitrage de principe

Ces champs sont des titulaires à désigner, pas des options à départager. Le porteur unique les cumule de manière intérimaire depuis le 25 novembre 2026, sauf l'avis juridique local qui reste externe. Toute délégation future est écrite puis assignée explicitement.

| Champ | Document | Jalons | Titulaire intérimaire |
|---|---|---|---|
| Titulaire de la stack et de l'architecture | `responsabilites.md`, `adr-001-stack.md` | avant le sprint 1 | Espoir LOEMBA |
| Validateur des hypothèses H1 à H8 | `ux-research.md`, `roadmap.md` | avant la Phase 0 | Espoir LOEMBA |
| Référent produit et référent technique par ville | `Operations/README.md`, `Growth/README.md` | avant ouverture | Espoir LOEMBA |
| Coordinateur de garde et relecteur par ville | `astreinte.md`, `contestation.md` | avant tout lien public | Espoir LOEMBA |
| Propriétaire des mesures et des alertes | `mesure.md`, `tableau-de-bord.md` | avant instrumentation de FS-11 | Espoir LOEMBA |
| Responsable d'extension par marché | `extension-afrique.md`, `decisions.md` | avant la Phase 3 | Espoir LOEMBA |
| Avis juridique local | `perimetre-juridique.md`, `confidentialite-visiteur.md` | avant le choix de l'hébergeur et de la région de stockage | conseil local, à nommer |

## 5. Preuves de store pour A-13

Deux textes officiels fondent la liste fermée ci-dessus. Ils sont cités tels qu'ils existent, sans étendre leur portée.

- Apple App Store Review Guidelines, règle 2.5.2 : `https://developer.apple.com/app-store/review/guidelines/`, texte mis à jour le 16 octobre 2026, consulté le 26 novembre 2026.
- Google Play Device and Network Abuse : `https://support.google.com/googleplay/android-developer/answer/16559646`, consulté le 26 novembre 2026.

Ces textes interdisent le téléchargement de code exécutable hors du circuit du store et n'autorisent pas un changement de fonctionnalité par ce moyen. Les six catégories retenues sont des données servies, pas du code. Si une règle de store change, le porteur réécrit cette section avant toute mise à jour mobile concernée et repasse par le binaire natif et le circuit du store pour ce qui ne peut plus être servi.

## 6. Après un arbitrage

Une ligne arbitrée change de statut et porte sa date dans cette grille. Lorsqu'elle modifie une décision numérotée existante, elle est inscrite dans la table des décisions retenues de `decisions.md` et reçoit une mention du type « arbitrée le date, voir le numéro attribué dans `decisions.md` ». Le numéro de décision est attribué dans l'ordre, sans saut. Lorsqu'elle ne modifie aucune décision numérotée, comme A-04, A-05, A-08 et A-10, elle est inscrite dans la section des arbitrages du registre avec date, motif, propriétaire, source liée, portée et historique, sans numéro D supplémentaire.

Aucun arbitrage ne modifie en silence une décision déjà retenue. Si un choix contredit une décision retenue (D-001 à D-024 ou un point A arbitré), la procédure de réouverture de `decisions.md` s'applique avec la nouvelle preuve, la date, la décision remplacée et la liste des documents touchés. Une question ouverte suit la grille, puis l'inscription au registre, sans passer par la réouverture. Le point A-13 est une précision de portée de D-024, pas une réouverture.
