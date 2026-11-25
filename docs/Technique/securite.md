# Sécurité : socle de contrôles

**Propriétaire.** Espoir LOEMBA, intérimaire depuis le 25 novembre 2026. **Statut.** opposée. **Date.** 26 novembre 2026, sur la base de la fiche proposée le 25 novembre 2026.
**Déclenchement.** Socle avant FS-01 et FS-02, revue complémentaire avant FS-07 et FS-09. `menaces.md` précède cette fiche.

## Contrôles

| Contrôle | Règle | Test |
|---|---|---|
| Jeton visiteur | Court, non durable, rotatif, jamais identifiant d'appareil | Un jeton expiré ou rotaté est refusé |
| Pseudonymisation | Clé distincte par finalité : modération, analyse, contestation | Aucune jointure possible entre pseudonymes de finalités différentes |
| Push | Aucun abonnement visiteur, jeton fournisseur réservé au compte | Aucune création de `push_subscription` sans `account_id` |
| Journal d'audit | Ajout seul, horodatage fiable, accès limité aux rôles autorisés | Tentative de modification d'une ligne refusée |
| Motifs de modération | Codes fermés, masquage des données personnelles dans le texte libre | Analyse automatique des motifs écrits |
| Contestation | Empreinte du jeton, usage unique, expiration, révocation après décision | Deuxième usage refusé avec 410 |
| Limites de débit | 5 tentatives d'authentification par minute et par adresse, 200 requêtes de lecture par minute | Les deux seuils retournent 429 |
| Téléversement | Quota, validation du type, retrait EXIF avant stockage | Objet stocké sans coordonnée GPS |
| Cache | Revalidation de visibilité à chaque réponse, purge sur `visibility_changed` | Test T1 de `architecture.md` |
| Client desktop | Aucun identifiant de machine ou d'installation, cache local sans décision de visibilité, mêmes contrôles que les deux autres clients | Test T1 de `architecture.md` rejoué depuis le client desktop |
| Secrets | Clés de pseudonymisation conservées séparément des pseudonymes, rotation journalisée | Une clé remplacée est tracée et les anciennes valeurs restent lisibles selon `conservation.md` |
| Mise à jour automatique | Paquet signé et vérifié avant installation sur `desktop`, retour à la version précédente en cas d'échec, aucune interruption de session, aucun identifiant d'appareil ou d'installation | Une mise à jour non signée est refusée ; la version précédente reste active ; la session en cours n'est pas coupée ; aucun identifiant machine n'est écrit dans `analytics_event` |

## Chaîne d'approvisionnement

Les contrôles suivants sont requis au merge et à la release. Ils sont décidés le 26 novembre 2026 par le porteur unique. Les versions sont épinglées, vérifiées le 26 novembre 2026 sur les dépôts officiels et archivées dans `../../memoires/2026-11-26-outils-securite.md`. Aucun canal `latest`, `canary`, `beta`, `rc` ou alpha n'est accepté.

La source canonique des alertes de vulnérabilité est OSV, complétée par la base d'avis GitHub pour les écosystèmes couverts. Le seuil opposable est zéro CVE connue et non traitée au merge et à la release. Une CVE connue bloque le merge jusqu'à correction ou jusqu'à une exception bornée avec statut VEX.

| Contrôle | Outil épinglé | Règle | Preuve attendue | État |
|---|---|---|---|---|
| SCA | `osv-scanner` 2.7.1 | Analyser les lockfiles avant le merge et bloquer toute vulnérabilité connue non traitée | Rapport horodaté avec identifiant OSV ou CVE et décision | rejoué par `Pro[CI]: documentation` |
| SAST | `semgrep` 1.187.0 avec les règles locales de `scripts/semgrep-rules.yml` | Analyser le code avant le merge et bloquer toute règle déclenchée | Rapport horodaté avec règle, fichier et correction | rejoué par `Pro[CI]: documentation` |
| Secrets | `gitleaks` 8.30.1 | Détecter tout secret avant le merge et bloquer toute correspondance, avec sortie masquée | Rapport horodaté sans valeur sensible divulguée | rejoué par `Pro[CI]: documentation` |
| Licences | `license-checker-rseidelsohn` 5.0.1 | Autoriser MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC, Unlicense et CC0-1.0 pour les dépendances npm de production, puis étendre la liste avant tout lockfile Python ou Rust | Rapport horodaté et registre des licences retenues | rejoué par `Pro[CI]: documentation` |
| SBOM | `syft` 1.57.2 via `anchore/sbom-action` 0.24.4 | Produire un SBOM CycloneDX JSON à chaque merge et à chaque release | Fichier `sbom.cdx.json` horodaté, conforme à la spécification CycloneDX 1.7.2 | généré par `Pro[CI]: documentation` |
| Signature SBOM | `cosign` 3.1.6 via `sigstore/cosign-installer` 4.1.4 | Signer le SBOM à chaque release et lier la signature au digest | Signature et certificat joints à la release | rejouée sur le premier tag de version |
| VEX | Python 3.13 et CycloneDX 1.7.2 | Produire un document VEX CycloneDX daté, avec une entrée par exception ouverte | `vex.cdx.json` joint à la release et lié au registre des exceptions | rejoué sur le premier tag de version |
| Exceptions | registre ci-dessous | Toute exception est bornée dans le temps, avec motif, propriétaire, contrôle compensatoire et date d'expiration | Ligne datée dans le registre des exceptions | aucune exception ouverte |

Aucun contrôle n'est déclaré opérationnel avant d'avoir été rejoué par la CI. Les contrôles de merge sont rejoués sur chaque pull request. La signature SBOM et le document VEX sont rejoués sur le premier tag de version. Aucune CVE connue et non traitée n'est acceptée au merge ou à la release.

### Registre des exceptions

| Identifiant | Composant | Motif | Contrôle compensatoire | Propriétaire | Date d'expiration | Statut VEX |
|---|---|---|---|---|---|---|
| Aucune ligne ouverte | | | | | | |

L'ajout d'une ligne est une décision écrite datée. Une ligne expirée rouvre la CVE concernée et bloque le merge suivant.

## Journal de publication

Toute transition de vidéo porte acteur `system`, `moderateur` ou `auteur`, avec `rule_id` quand l'acteur est `system`, selon `adr-003-porte-publication.md`. Aucun identifiant de modérateur n'est inventé pour une décision automatique.

## Niveau visé

Le niveau [OWASP ASVS](https://owasp.org/projects/asvs) visé est le niveau 2, arbitré le 26 novembre 2026 au point A-11. La portée couvre le backend, les trois clients livrés ensemble et le conteneur `client_desktop`. Le propriétaire de la revue est Espoir LOEMBA, intérimaire. Les contrôles ci-dessus font partie de la définition de terminé et sont exécutés en intégration sur `mobile`, `web` et `desktop`.
