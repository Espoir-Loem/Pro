# Contrôle des mises à jour avant FS-01, protocole de préparation

**Statut** : préparé le 26 novembre 2026, aucun rendu signé, aucun contrôle exécuté, aucune porte levée  
**Sources** : [PRD, section 10.1 et condition 7 de la section 11](../../docs/Product/prd.md), [Sécurité, contrôle de mise à jour](../../docs/Technique/securite.md), [Responsabilités](../../docs/Technique/responsabilites.md), [Porte 6 du sprint 1](./README.md)  
**Règle** : ce protocole décrit comment le contrôle sera mené et quelles preuves seront archivées. Il n'exécute aucun contrôle, n'avance aucun résultat, ne produit aucune signature et ne lève aucune porte.

La recherche UX porte une mention de cadrage pour ce contrôle avant FS-01. Le PRD fixe le chemin de mise à jour par client et la condition 7 de sa définition de terminé exige la preuve de signature, de retour arrière et de non interruption de session sur les trois clients. Le présent protocole rend ces exigences lisibles avant l'existence d'un rendu. Aucune valeur n'est présentée comme mesurée.

## 1. Périmètre par client

| Client | Moment d'application | Limite écrite |
|---|---|---|
| `web` | Déploiement côté serveur, visible à la navigation suivante | La session en cours continue sur la version chargée, sans perte de sauvegarde ni de message en cours |
| `desktop` | Paquet signé téléchargé en arrière-plan, appliqué au redémarrage ou au lancement suivant | Signature et intégrité vérifiées avant installation, retour à la version précédente si la vérification échoue |
| `mobile` | Six catégories servies côté serveur selon A-13 | Aucun code exécutable téléchargé, retour au binaire natif et circuit du store si une règle de store change |

Les règles communes sont reprises sans modification : aucune mise à jour ne coupe une session en cours, aucune ne modifie une décision de modération ni ne contourne la porte de publication, aucune ne crée d'identifiant d'appareil, d'installation ou de machine, et aucune ne joint un tel identifiant à `signup_verified`. Le journal technique porte la version appliquée, le résultat de la vérification et le retour arrière éventuel, sans rattachement à une personne.

## 2. Scénarios à rejouer

Chaque scénario est exécuté sur le rendu concerné. La colonne preuve désigne ce qui est archivé, sans anticiper le résultat.

| Identifiant | Client | Geste à rejouer | Résultat attendu | Preuve à archiver |
|---|---|---|---|---|
| C1 | `web` | Ouvrir une session, rédiger un message, déclencher un déploiement puis naviguer | La session en cours reste sur la version chargée et le message en cours n'est pas perdu | Trace de la session, du déploiement et du message conservé |
| C2 | `desktop` | Présenter un paquet signé, vérifier avant installation, redémarrer | Signature et intégrité vérifiées avant installation | Trace de la vérification et de la version appliquée |
| C3 | `desktop` | Présenter un paquet non signé ou altéré | Mise à jour refusée, version précédente active | Trace du refus et de la version restée active |
| C4 | `desktop` | Déclencher un échec de vérification puis un retour arrière | Retour à la version précédente sans perte de session | Trace du retour arrière et de la version restaurée |
| C5 | `mobile` | Modifier une traduction et une valeur de configuration servies côté serveur | Aucun code exécutable téléchargé, aucune règle de store contournée | Trace des catégories servies et de l'absence de binaire téléchargé |
| C6 | Les trois | Lire le journal technique après chaque scénario | Version appliquée, résultat de vérification et retour arrière éventuel inscrits, sans identifiant machine | Extrait du journal avec date et client |
| C7 | Les trois | Tenter de modifier une décision de modération par une mise à jour | Décision inchangée et porte de publication respectée, transition journalisée avec acteur `system` et identifiant de règle | Extrait du journal et de la décision de modération |

Aucun scénario n'est marqué comme réussi dans ce document. Aucun identifiant de participant, de machine ou de compte réel n'y est inscrit.

## 3. Responsabilité et moments du contrôle

Le titulaire intérimaire des fiches techniques concernées est Espoir LOEMBA depuis le 25 novembre 2026 au titre de A-04. Il cadre le protocole et exécute le premier passage avant FS-01, sans délégation tacite. Le contrôle est rejoué en revue de sortie MVP avec l'identifiant du relecteur et la date, conformément à la roadmap et à `responsabilites.md`.

La preuve attendue au titre de la porte 6 du sprint 1 reste liée au premier rendu signé des trois clients. Ce protocole ne la remplace pas. La [fiche de préparation du premier rendu signé](./fiche-premier-rendu-signe.md) prépare l'archivage de cette preuve par client, sans signature ni résultat préremplis. Aucune signature de release, aucun tag et aucun résultat de contrôle ne sont avancés ici.

## 4. Ce que ce protocole ne fait pas

Il ne contient aucun code applicatif, ne produit aucun paquet signé, ne déclare aucun contrôle opérationnel, n'ajoute aucun seuil, ne nomme aucun prestataire ni hébergeur, ne choisit aucune région de stockage, ne modifie aucune décision de modération et ne lève aucune porte.
