# Fiche de préparation du premier rendu signé des trois clients

**Statut** : préparée le 27 novembre 2026, aucun rendu signé, aucun tag, aucune signature, aucune porte levée  
**Sources canoniques** : [PRD, section 10.1 et condition 7 de la section 11](../../docs/Product/prd.md), [Sécurité](../../docs/Technique/securite.md), [Responsabilités](../../docs/Technique/responsabilites.md), [D-004 au registre](../../docs/Product/decisions.md), [Porte 6 du sprint 1](./README.md), [Protocole des mises à jour](./controle-mises-a-jour.md)  
**Règle** : cette fiche prépare l'archivage des preuves au premier rendu signé. Elle n'exécute aucun contrôle, ne produit aucune signature, n'avance aucun résultat et ne lève aucune porte.

## 1. Ce qui est déjà écrit

La condition 7 de la définition de terminé exige la mise à jour automatique vérifiée sur `mobile`, `web` et `desktop`, avec la preuve du contrôle de signature, du retour arrière et de la non interruption de session. La section 10.1 fixe le chemin par client : déploiement côté serveur pour `web`, paquet signé téléchargé en arrière-plan puis appliqué au redémarrage pour `desktop`, six catégories servies côté serveur selon A-13 pour `mobile`. La [fiche de sécurité](../../docs/Technique/securite.md) ajoute que le paquet est vérifié avant installation, que la version précédente revient en cas d'échec, qu'aucune session n'est interrompue et qu'aucun identifiant de machine ou d'installation n'est écrit.

La chaîne d'approvisionnement porte des contrôles à rejouer au merge et à la release. La signature du SBOM et le document VEX sont prévus sur le premier tag de version, sans tag avancé ici. D-004 impose que les trois clients soient livrés ensemble. La porte 6 du sprint 1 attend sa preuve au premier rendu signé des trois clients. Le [protocole des mises à jour](./controle-mises-a-jour.md) décrit les scénarios C1 à C7 et précise qu'il ne remplace pas cette preuve.

Le titulaire intérimaire des fiches techniques concernées est Espoir LOEMBA depuis le 25 novembre 2026 au titre de A-04. Les prestataires `desktop` Windows et macOS restent à nommer avant le premier commit de code de stack. Aucun rendu signé, aucun digest, aucun certificat, aucun tag et aucun résultat de contrôle ne sont fournis à la date de préparation de cette fiche.

## 2. Preuves à archiver par client

Chaque ligne reste à remplir au moment du premier rendu signé. Une preuve lue sur un client n'est jamais transférée à un autre.

| Client | Ce qui est vérifié | Preuve à archiver | État |
|---|---|---|---|
| `web` | Déploiement côté serveur, session en cours maintenue, message en cours conservé | À renseigner depuis les scénarios C1 et C6, sans résultat prérempli | En attente de rendu signé |
| `desktop` | Paquet signé, intégrité vérifiée avant installation, retour à la version précédente, session non interrompue | À renseigner depuis les scénarios C2, C3, C4 et C6, sans signature ni résultat préremplis | En attente de rendu signé |
| `mobile` | Six catégories servies côté serveur, aucun code exécutable téléchargé, aucune règle de store contournée | À renseigner depuis les scénarios C5 et C6, sans résultat prérempli | En attente de rendu signé |

## 3. Champs communs à remplir au premier rendu signé

| Champ | Valeur |
|---|---|
| Date du rendu | À renseigner, aucune date préremplie |
| Identifiant de version | À renseigner, aucun tag prérempli |
| Digest du paquet | À renseigner, aucun digest prérempli |
| Signature et certificat | À renseigner, aucune signature préremplie |
| Résultat de la vérification | À renseigner, aucun résultat prérempli |
| Retour arrière éventuel | À renseigner, ou aucun |
| Non interruption de session | À renseigner par client, sans résultat prérempli |
| Absence d'identifiant machine, d'installation ou d'appareil | À renseigner par client, sans résultat prérempli |
| Signature du SBOM et document VEX du premier tag | À renseigner depuis `securite.md`, sans résultat prérempli |
| Extrait du journal technique | À renseigner avec date et client, sans rattachement à une personne |
| Relecteur identifié | À renseigner |
| Date de la revue | À renseigner |
| Motif écrit | À renseigner |
| Preuve archivée et historique | À renseigner |
| Propriétaire de l'archive | Espoir LOEMBA, intérimaire |
| Approbateur nommé | À renseigner |
| État | En attente de rendu signé |

Aucune ligne sans rendu signé daté n'est une preuve. Un scénario du protocole reste à rejouer avant d'être marqué, et cette fiche ne marque aucun scénario.

## 4. Distinctions à conserver

Un rendu signé ne prouve la condition 7 qu'après archivage des preuves par client. Il ne remplace pas le protocole des mises à jour, ne prononce pas la porte 6 du sprint 1, ne nomme pas les prestataires `desktop`, ne choisit pas d'hébergeur ni de région de stockage, ne lève pas A-12, ne fixe pas de date de lancement selon A-05 et ne lève aucune porte.

Les contrôles de la chaîne d'approvisionnement restent ceux de `securite.md`, lus tels qu'ils y sont écrits. Aucune signature ni aucun résultat n'est déduit du silence d'un journal. Aucune preuve lue sur `web` ne dispense de la preuve attendue sur `desktop` ou sur `mobile`.

## 5. Ce que cette fiche ne fait pas

Elle ne produit aucun paquet signé, n'exécute aucun contrôle, ne relève aucun résultat, n'ajoute aucun seuil, ne nomme aucun prestataire ni relecteur, ne modifie aucune décision, ne remplace pas le protocole des mises à jour, ne lève aucune porte et ne contient aucun code applicatif.
