# SEO du client web

**Version.** 1.
**Date.** 25 novembre 2026.
**Statut.** Règles de cadrage, sans code applicatif. Les valeurs de performance et les propriétaires restent à nommer.
**Périmètre.** Client web uniquement. Le mobile et le desktop suivent leurs propres règles de découverte.

## 1. Principes

Le référencement sert la lecture publique et la trouvabilité des profils, des vidéos, des offres d'emploi et des pages organisation. Chaque élément référencé est rattaché à une fonctionnalité, une histoire utilisateur ou une exigence d'accessibilité du [PRD](../Product/prd.md). Aucune page n'est créée seulement pour un moteur de recherche. Le français vient d'abord, selon le registre des décisions. Les langues suivantes ne sont pas datées ici. Aucun classement payant n'est prévu dans la recherche, conformément au registre des décisions.

La lecture publique sans compte est préservée pour les contenus indexables. Aucun identifiant visiteur permanent n'est écrit pour le référencement. Les données de recherche sont agrégées et suivent la durée de conservation écrite dans les fiches de conformité.

## 2. Checklist de cadrage

| Élément | Règle | Vérification | Propriétaire |
|---|---|---|---|
| Structure sémantique | Utiliser les balises de titre, de navigation et de contenu selon le rôle, jamais pour l'apparence | Revue DOM et audit accessible | À nommer |
| Titre et description | Un titre et une description uniques par page indexable, rédigés en français | Contrôle automatisé après le premier rendu | À nommer |
| URL canonique | Une URL canonique stable par contenu, sans paramètre de session ni identifiant visiteur | Contrôle de l'en-tête et du balisage | À nommer |
| Langues déclarées | Déclarer la langue du document, puis ajouter les variantes seulement après décision | Contrôle de l'attribut de langue | À nommer |
| Données structurées | Utiliser les types adaptés aux offres d'emploi, aux vidéos et aux organisations, sans donnée inventée | Validation du schéma | À nommer |
| Sitemap et robots | Publier un plan du site des pages publiques et des règles d'accès sans contenu privé | Contrôle du fichier et des chemins | À nommer |
| Signaux web essentiels | Mesurer le rendu, l'interaction et la stabilité sur données de terrain | Rapport périodique | À nommer |
| Images et médias | Fournir un texte alternatif utile et des sous-titres conformes à la règle D-021 | Revue de contenu | À nommer |
| Contenu dupliqué | Éviter la duplication entre variantes de ville et de langue par un contenu distinct justifié | Revue éditoriale | À nommer |
| Trafic payant | Aucun achat de position dans la recherche, aucune exception silencieuse | Revue du registre et des campagnes | À nommer |

## 3. Liens avec les KPI

Les mesures SEO sont définies dans [kpi.md](../Product/kpi.md) sous les identifiants SEO-01 et SEO-02. Elles ne fixent aucune cible chiffrée avant décision écrite. Le propriétaire des mesures et la fréquence d'extraction sont à nommer avant l'instrumentation du client web.

## 4. Règles de mise à jour

Toute modification du balisage public est revue avec le PRD, les principes de design et la fiche d'accessibilité. Une nouvelle règle SEO est inscrite ici avant d'être appliquée dans le code. Les sources utilisées pour justifier un choix sont archivées dans `memoires/`.
