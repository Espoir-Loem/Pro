# Avenant de cadrage du 26 novembre 2026

**Date.** 26 novembre 2026.
**Porteur.** Espoir LOEMBA, chef de projet et titulaire intérimaire de tous les rôles sauf l'avis juridique local.
**Demande.** Finaliser les valeurs manquantes avec des choix par défaut assumés et documentés, sans écrire de code applicatif et sans inventer de mesure, de montant ou de preuve externe.
**Effet.** Cet avenant complète l'avenant de gouvernance du 25 novembre 2026. Les champs marqués comme ouverts dans ce dernier sont fermés ici lorsqu'une décision intérimaire suffit. Les champs qui exigent une preuve externe ou un montant restent ouverts.

## 1. KPI et tableau de bord

`docs/Product/kpi.md` passe en version 2. Chacun des dix identifiants reçoit une cible chiffrée, une fréquence d'extraction et un seuil d'alerte. Les valeurs sont des décisions intérimaires du 26 novembre 2026, pas des résultats relevés.

| Groupe | Cibles retenues |
|---|---|
| Bugs | 0 bug bloquant ou critique ouvert et au plus 2 bugs ouverts, tri en 1 jour ouvré, réouverture au plus 5 % |
| UX | Réussite au moins 80 %, temps médian au plus 60 secondes, confiance au moins 4 sur 5 |
| Produit | Acquisition vérifiée au moins 20 pour 1 000 sessions, complétion vidéo au moins 60 % |
| SEO | Indexation au moins 90 % des pages publiables, signaux de terrain réussis sur au moins 90 % des URL |

`docs/Product/tableau-de-bord.md` reprend ces seuils et nomme le propriétaire et le délai de chaque alerte. Le seuil de coût vidéo reste lié à D-022 et n'est pas inventé.

## 2. SEO web

`docs/Technique/seo-web.md` nomme les sources et la fréquence :

- SEO-01 : Google Search Console, extraction hebdomadaire le lundi à 09:00 UTC ;
- SEO-02 : Chrome UX Report via l'API PageSpeed Insights, extraction mensuelle le 1er du mois à 09:00 UTC.

Chaque extrait est archivé dans `memoires/` avec la date d'extraction, la date de la donnée et la portée. Aucune position payante dans la recherche n'est utilisée pour améliorer ces mesures.

## 3. Sécurité et chaîne d'approvisionnement

`docs/Technique/securite.md` devient opposable le 26 novembre 2026. Les versions sont vérifiées le même jour et archivées dans `memoires/2026-11-26-outils-securite.md`.

| Contrôle | Outil épinglé |
|---|---|
| SCA | `osv-scanner` 2.7.1, source canonique OSV |
| SAST | `semgrep` 1.187.0 avec les règles locales de `scripts/semgrep-rules.yml` |
| Secrets | `gitleaks` 8.30.1, sortie masquée |
| Licences npm | `license-checker-rseidelsohn` 5.0.1 avec liste fermée |
| SBOM | `syft` 1.57.2 via `anchore/sbom-action` 0.24.4, CycloneDX JSON |
| Signature SBOM | `cosign` 3.1.6 via `sigstore/cosign-installer` 4.1.4 |
| VEX | Python 3.13 et CycloneDX 1.7.2 |

Le niveau OWASP ASVS visé est le niveau 2, arbitré au point A-11. La portée couvre le backend et les trois clients livrés ensemble. Espoir LOEMBA en est le propriétaire de revue.

Les contrôles de merge sont rejoués dans `Pro[CI]: documentation` : secrets, SCA, SAST, licences et génération du SBOM. La signature du SBOM, le document VEX et la publication des actifs sont conditionnés au premier tag de version. Le registre des exceptions reste vide. Aucune ligne expirée ou non datée n'est acceptée.

## 4. Décisions D-010 et D-011

- D-010 est retenue : vérification N2 seulement à la demande de l'employeur en phase 2, preuve limitée à l'email vérifié de D-018, badge réversible avec trace, événement `n2_requested` sans identifiant visiteur permanent.
- D-011 est retenue : niveau payant nommé `Organisation Avancée` en phase 5, avec statistiques agrégées avancées, export mensuel et alertes de suivi définies par l'organisation. Aucun classement payant et aucun privilège d'administration supplémentaire.

Les questions ouvertes du registre se limitent désormais à D-022.

## 5. Contrôles locaux rejoués

- `npm audit` : aucune vulnérabilité déclarée au 26 novembre 2026.
- `gitleaks detect --no-git --redact` en 8.30.1 : aucune correspondance.
- `semgrep` 1.187.0 avec les règles locales : aucune règle déclenchée.
- `license-checker-rseidelsohn` 5.0.1 en production avec la liste fermée : aucune licence interdite.
- Validation YAML du workflow et sommes de contrôle des binaires téléchargés : réussies.

## 6. Limites conservées

L'avis juridique local, les montants de D-022, la machine de référence R2, la liste fermée de la part mobile modifiable au point A-13 et la preuve des règles de store restent externes ou non écrits. Aucun code applicatif n'est écrit. Aucune PR n'est ouverte sans issue référencée. Aucune valeur n'est déduite d'une observation pour accélérer une clôture.

## 7. Conclusion

Les cibles KPI, les sources SEO, les outils de sécurité, le niveau ASVS et les décisions D-010 et D-011 sont désormais écrits et datés. Les contrôles rejoués sont verts au 26 novembre 2026. La phase 0 reste ouverte sur les points externes nommés ci-dessus.
