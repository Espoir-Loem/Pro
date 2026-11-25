# Avenant gouvernance avec porteur unique

**Date.** 25 novembre 2026.
**Demande du porteur.** Le porteur mène seul le projet pour l'instant et utilise des outils IA pour aller plus vite. Les titulaires hors chef de projet ne sont pas encore nommés et l'IA ne doit pas devenir un auteur des artefacts publiés.
**Périmètre.** Gouvernance intérimaire, arbitrages de principe, propriété des mesures et des contrôles. Aucun code applicatif n'est écrit. La phase 0 reste ouverte tant que l'avis juridique local n'est pas produit.

## 1. Rôles intérimaires

Espoir LOEMBA cumule depuis le 25 novembre 2026 les rôles suivants, à titre intérimaire :

- propriétaire technique et titulaire de la stack et de l'architecture ;
- responsable de la recherche et validateur des hypothèses H1 à H8 ;
- référent produit et référent technique pour Brazzaville et pour Kinshasa ;
- coordinateur de garde et relecteur par ville ;
- propriétaire des mesures et des alertes ;
- responsable d'extension par marché ;
- propriétaire des dix KPI et des mesures SEO ;
- propriétaire de la chaîne de contrôles de la chaîne d'approvisionnement.

L'avis juridique local reste externe et à nommer avant le choix de l'hébergeur et de la région de stockage. Aucune personne morale, aucun conseil et aucun cabinet n'est inventé. Toute délégation future est écrite, datée puis assignée explicitement dans GitHub.

## 2. Outils IA

Les outils IA sont des instruments d'accélération. Ils ne signent aucun commit, aucun tag annoté, aucune release et aucun message publié sur GitHub. Aucun trailer de co-auteur n'est accepté. L'identité Espoir LOEMBA (`hopcy.forcy@gmail.com`) reste l'auteur de tous les artefacts publiés.

Les outils sollicités sont utilisés pour la rédaction, la préparation des contrôles, la revue documentaire et l'accélération des tâches répétitives. Leur liste nominative, leur version et leur finalité précise restent à consigner dans un avenant séparé avant le premier code applicatif. Aucun outil IA ne porte de rôle de titulaire, de validateur ou de propriétaire.

## 3. Arbitrages intérimaires enregistrés

Les choix suivants sont inscrits dans `docs/Product/arbitrage.md` comme décisions intérimaires du porteur, datées du 25 novembre 2026. Ils ne ferment pas les questions dont les champs exacts restent à écrire.

| Référence | Choix intérimaire | Champ encore ouvert |
|---|---|---|
| A-02 et D-022 | Enveloppe mensuelle avec plafond par ville | Montant, devise, fenêtre, seuil de coût par vue |
| A-03 et D-023 | Les cinq cibles proposées sont retenues comme cibles | Machine de référence, méthode de mesure, date de revue |
| A-04 | Porteur unique appuyé par les outils IA, prestataires à nommer pour le desktop | Rôles et prestataires |
| A-05 | Jalons par critères, sans date fixe | Conséquence sur le recrutement et l'astreinte |
| A-06 et D-010 | Vérification seulement à la demande de l'employeur | Preuve acceptée, réversibilité du badge |
| A-07 et D-011 | Nom neutre avec statistiques avancées | Nom exact et liste fermée des privilèges |
| A-08 | Aucune autre langue avant la Phase 3 | Responsable d'une éventuelle extension |
| A-09 | Modèle de modération mixte retenu dans son principe | Noyau, renfort bénévole, couverture horaire |
| A-10 | Aucun seuil et repli immédiat vers le fil général | Règle de repli par ville |
| A-13 | Éléments servis côté serveur seulement | Liste fermée et règle par store prouvée par écrit |
| A-11 | Non tranché | Niveau OWASP ASVS |
| A-12 | Non tranché | Avis du conseil local, pays et date |

## 4. Mesures et contrôles

- `docs/Product/kpi.md` : les dix propriétés KPI sont attribuées à Espoir LOEMBA à titre intérimaire. Les cibles, la fréquence et les seuils d'alerte restent à nommer.
- `docs/Technique/seo-web.md` : les dix éléments de la checklist ont Espoir LOEMBA comme propriétaire intérimaire. Les sources datées et la fréquence d'extraction restent à nommer.
- `docs/Technique/securite.md` : SCA, SAST, secrets, licences, SBOM CycloneDX signé, VEX et exceptions bornées sont décrits comme contrôles requis. Les outils, versions et seuils restent à nommer.
- `docs/UX/ux-research.md` : H1 à H8 possèdent déjà formulation, dénominateur et condition d'infirmation. Espoir LOEMBA en est le validateur intérimaire. Aucun seuil n'est modifié.

## 5. GitHub

Les neuf issues ouvertes, numéros 4 à 12, sont assignées explicitement à Espoir LOEMBA. Aucune commande de revendication d'issue n'est utilisée. Le tableau de bord `Pro - Suivi du projet` conserve ses champs Statut, Priorité, Domaine et KPI. Les issues 4, 6, 8, 9, 10, 11 et 12 sont en cours. Les issues 5 et 7 restent bloquées tant que leurs valeurs exactes ne sont pas nommées.

## 6. Contrôles locaux

Chaque commit de cette branche touche un seul fichier. Les contrôles suivants sont rejoués avant la pull request : `npm run check`, les tests Python, `uvx pre-commit run --all-files` et la validation du schéma YAML du workflow. Le nombre attendu de fichiers canoniques dans `docs/` reste inchangé, aucune nouvelle fiche n'ayant été ajoutée dans ce dossier.

## 7. Limites conservées

La phase 0 n'est pas close. L'avis juridique local, les montants du budget, la machine de référence, le niveau ASVS, le nom exact du niveau payant, la liste fermée de la part mobile modifiable, les cibles KPI, les sources SEO et les outils de sécurité restent à nommer par décision écrite. Aucune valeur n'est déduite d'une observation ou inventée pour accélérer la clôture.

## 8. Conclusion

Le projet dispose désormais d'une gouvernance intérimaire explicite adaptée à un porteur unique, avec une frontière nette entre le porteur, les outils IA et l'avis juridique externe. Cohérence confirmée, Error 0, warning 0.
