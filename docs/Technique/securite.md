# Sécurité : socle de contrôles

**Propriétaire.** Espoir LOEMBA, intérimaire depuis le 25 novembre 2026. **Statut.** proposée. **Date.** 25 novembre 2026.
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

Les contrôles suivants sont requis au merge et à la release. Le porteur unique en est le propriétaire intérimaire. Les outils, leurs versions et leurs seuils restent à nommer par décision écrite, conformément aux points A-03 à A-09 et à l'issue 12 du tableau de bord.

| Contrôle | Règle | Preuve attendue | État |
|---|---|---|---|
| SCA | Analyser les dépendances avant le merge et bloquer toute CVE connue et non traitée | Rapport horodaté, identifiant de la CVE, décision de traitement | Outillage à nommer |
| SAST | Analyser le code source avant le merge et bloquer toute faille retenue | Rapport horodaté avec règle, fichier et correction | Outillage à nommer |
| Secrets | Détecter tout secret avant le merge et bloquer toute correspondance | Rapport horodaté sans valeur sensible divulguée | Outillage à nommer |
| Licences | Vérifier la compatibilité des licences avant le merge et bloquer toute licence interdite | Rapport horodaté et registre des licences retenues | Outillage à nommer |
| SBOM | Produire un SBOM CycloneDX signé à chaque release | Fichier signé joint à la release, avec empreinte vérifiable | Outillage à nommer |
| VEX | Publier un document VEX daté qui justifie chaque non application | Document daté lié à la release et aux exceptions | Format à nommer |
| Exceptions | Toute exception est bornée dans le temps, avec motif, propriétaire et date d'expiration | Ligne datée dans le registre des exceptions | À écrire |

Aucun contrôle n'est déclaré opérationnel tant que son outil, sa version épinglée et son seuil ne sont pas écrits. Aucune CVE connue et non traitée n'est acceptée au merge ou à la release.

## Journal de publication

Toute transition de vidéo porte acteur `system`, `moderateur` ou `auteur`, avec `rule_id` quand l'acteur est `system`, selon `adr-003-porte-publication.md`. Aucun identifiant de modérateur n'est inventé pour une décision automatique.

## Niveau visé

Le niveau [OWASP ASVS](https://owasp.org/projects/asvs) visé reste à trancher et figure dans `responsabilites.md`. En attendant, les contrôles ci-dessus font partie de la définition de terminé et sont exécutés en intégration sur les trois clients livrés ensemble, y compris le client desktop.
