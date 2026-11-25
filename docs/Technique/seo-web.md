# SEO du client web

**Version.** 1.
**Date.** 25 novembre 2026.
**Statut.** Règles de cadrage, sans code applicatif. Les cibles, les sources et les fréquences sont arrêtées le 26 novembre 2026 à titre intérimaire.
**Périmètre.** Client web uniquement. Le mobile et le desktop suivent leurs propres règles de découverte.

## 1. Principes

Le référencement sert la lecture publique et la trouvabilité des profils, des vidéos, des offres d'emploi et des pages organisation. Chaque élément référencé est rattaché à une fonctionnalité, une histoire utilisateur ou une exigence d'accessibilité du [PRD](../Product/prd.md). Aucune page n'est créée seulement pour un moteur de recherche. Le français vient d'abord, selon le registre des décisions. Les langues suivantes ne sont pas datées ici. Aucun classement payant n'est prévu dans la recherche, conformément au registre des décisions.

La lecture publique sans compte est préservée pour les contenus indexables. Aucun identifiant visiteur permanent n'est écrit pour le référencement. Les données de recherche sont agrégées et suivent la durée de conservation écrite dans les fiches de conformité.

## 2. Checklist de cadrage

| Élément | Règle | Vérification | Propriétaire |
|---|---|---|---|
| Structure sémantique | Utiliser les balises de titre, de navigation et de contenu selon le rôle, jamais pour l'apparence | Revue DOM et audit accessible | Espoir LOEMBA, intérimaire |
| Titre et description | Un titre et une description uniques par page indexable, rédigés en français | Contrôle automatisé après le premier rendu | Espoir LOEMBA, intérimaire |
| URL canonique | Une URL canonique stable par contenu, sans paramètre de session ni identifiant visiteur | Contrôle de l'en-tête et du balisage | Espoir LOEMBA, intérimaire |
| Langues déclarées | Déclarer la langue du document, puis ajouter les variantes seulement après décision | Contrôle de l'attribut de langue | Espoir LOEMBA, intérimaire |
| Données structurées | Utiliser les types adaptés aux offres d'emploi, aux vidéos et aux organisations, sans donnée inventée | Validation du schéma | Espoir LOEMBA, intérimaire |
| Sitemap et robots | Publier un plan du site des pages publiques et des règles d'accès sans contenu privé | Contrôle du fichier et des chemins | Espoir LOEMBA, intérimaire |
| Signaux web essentiels | Mesurer le rendu, l'interaction et la stabilité sur données de terrain | Rapport périodique | Espoir LOEMBA, intérimaire |
| Images et médias | Fournir un texte alternatif utile et des sous-titres conformes à la règle D-021 | Revue de contenu | Espoir LOEMBA, intérimaire |
| Contenu dupliqué | Éviter la duplication entre variantes de ville et de langue par un contenu distinct justifié | Revue éditoriale | Espoir LOEMBA, intérimaire |
| Trafic payant | Aucun achat de position dans la recherche, aucune exception silencieuse | Revue du registre et des campagnes | Espoir LOEMBA, intérimaire |

## 3. Liens avec les KPI

Les mesures SEO sont définies dans [kpi.md](../Product/kpi.md) sous les identifiants SEO-01 et SEO-02. Le porteur unique cumule la propriété de ces mesures de manière intérimaire depuis le 25 novembre 2026. Les cibles, les sources et les fréquences ci-dessous sont arrêtées le 26 novembre 2026. Aucune valeur n'est présentée comme relevée avant la première extraction datée.

| Identifiant | Source datée | Fréquence d'extraction | Format de l'extrait | Cible intérimaire |
|---|---|---|---|---|
| SEO-01 | Google Search Console, vue Performance, filtrée sur les pages publiables du domaine | Hebdomadaire, lundi à 09:00 UTC | JSON avec `date`, `source`, `scope`, `pages_publiables`, `pages_indexees`, `ratio` | Au moins 90 % des pages publiables indexées sous 30 jours |
| SEO-02 | Chrome UX Report via l'API PageSpeed Insights, sur les URL publiques du domaine | Mensuelle, le 1er du mois à 09:00 UTC | JSON avec `date`, `source`, `url`, `metric`, `pass_rate` | Au moins 90 % des URL qui passent les trois signaux de terrain |

Chaque extrait est archivé dans `memoires/` avec la date d'extraction, la date de la donnée et la portée. Aucun extrait n'est publié sans ces trois champs. Aucun achat de position dans la recherche n'est utilisé pour améliorer ces mesures, conformément à D-019. La première extraction sert de base de lecture, pas de cible relevée.

## 4. Règles de mise à jour

Toute modification du balisage public est revue avec le PRD, les principes de design et la fiche d'accessibilité. Une nouvelle règle SEO est inscrite ici avant d'être appliquée dans le code. Les sources utilisées pour justifier un choix sont archivées dans `memoires/`.
