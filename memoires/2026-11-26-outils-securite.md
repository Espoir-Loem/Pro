# Note du 26 novembre 2026 : outils de la chaîne de contrôles

**Objet.** Conserver les sources et les versions vérifiées avant l'inscription des contrôles dans `docs/Technique/securite.md`.
**Méthode.** Versions lues le 26 novembre 2026 sur les publications officielles des projets, sans canal `latest`, `canary`, `beta`, `rc` ni alpha. Les étiquettes marquées comme préversion ont été écartées. Les actions GitHub sont épinglées à l'empreinte du commit résolu depuis l'étiquette stable.

| Contrôle | Outil | Version vérifiée | Source officielle |
|---|---|---|---|
| SCA | `osv-scanner` | 2.7.1 | https://github.com/google/osv-scanner/releases/tag/v2.7.1 |
| SAST | `semgrep` | 1.187.0 | https://pypi.org/project/semgrep/1.187.0/ |
| Secrets | `gitleaks` | 8.30.1 | https://github.com/gitleaks/gitleaks/releases/tag/v8.30.1 |
| Licences npm | `license-checker-rseidelsohn` | 5.0.1 | https://www.npmjs.com/package/license-checker-rseidelsohn/v/5.0.1 |
| SBOM | `syft` | 1.57.2 | https://github.com/anchore/syft/releases/tag/v1.57.2 |
| Action SBOM | `anchore/sbom-action` | 0.24.4 | https://github.com/anchore/sbom-action/releases/tag/v0.24.4 |
| Signature | `cosign` | 3.1.6 | https://github.com/sigstore/cosign/releases/tag/v3.1.6 |
| Action signature | `sigstore/cosign-installer` | 4.1.4 | https://github.com/sigstore/cosign-installer/releases/tag/v4.1.4 |
| VEX et SBOM | spécification CycloneDX | 1.7.2 | https://github.com/CycloneDX/specification/releases/tag/1.7.2 |

## Vérifications locales rejouées

- `npm audit` sur le dépôt courant : aucune vulnérabilité déclarée au 26 novembre 2026.
- `gitleaks detect --no-git --redact` avec la version 8.30.1 : aucune correspondance signalée.
- `license-checker-rseidelsohn` en mode production avec la liste fermée retenue : aucune licence interdite sur les dépendances npm de production.
- `semgrep` en version 1.187.0 avec les règles locales : aucune règle déclenchée sur les fichiers courants.
- Somme de contrôle du binaire vérifiée avant exécution pour `gitleaks`.

## Empreintes des actions retenues

| Action | Version | Empreinte du commit |
|---|---|---|
| `anchore/sbom-action` | 0.24.4 | `dfcb83b97731532d72be422cbc51ee64adb6fd56` |
| `sigstore/cosign-installer` | 4.1.4 | `881c63bd87e38389154debd8331404ce7ca8a3ab` |

## Limites

Cette note conserve une vérification datée, pas une garantie permanente. Une nouvelle publication d'un outil, une nouvelle CVE ou un changement de règles de licence déclenche une revue écrite avant mise à jour des versions épinglées. Aucun résultat de scan n'est présenté comme une preuve d'absence définitive de vulnérabilité.
