# Contrôle SEO du premier rendu web, protocole de préparation

**Statut** : préparé le 26 novembre 2026, aucun rendu web réel, aucun contrôle exécuté, aucune extraction, aucune porte levée  
**Sources canoniques** : [Fiche SEO web](../../docs/Technique/seo-web.md), [PRD, référencement et tableau des contrôles](../../docs/Product/prd.md), [KPI SEO-01 et SEO-02](../../docs/Product/kpi.md), [Issue #11](https://github.com/Espoir-Loem/Pro/issues/11), [Porte 7 du sprint 1](./README.md)  
**Règle** : ce protocole décrit comment le contrôle sera mené et quelles preuves seront archivées. Il n'exécute aucun contrôle, n'avance aucun résultat, ne publie aucun extrait et ne lève aucune porte.

La fiche SEO web fixe la checklist et les sources. L'issue #11 demande de la passer sur un rendu public réel. Le PRD précise le moment de chaque contrôle et la preuve attendue. Le présent protocole rend ces exigences lisibles avant l'existence du client web. Aucune valeur n'est présentée comme mesurée, aucun extrait n'est publié sans date d'extraction, date de donnée et portée.

## 1. Périmètre

Le protocole porte sur le client `web` uniquement. Le `mobile` et le `desktop` suivent leurs propres règles de découverte et ne sont pas concernés par ces contrôles. La lecture publique sans compte reste intacte pour les contenus indexables. Aucune page n'est créée pour un moteur de recherche, aucun classement payant n'est introduit, aucun identifiant visiteur permanent n'est écrit pour le référencement.

Les éléments à contrôler sont repris de la fiche SEO web sans ajout de seuil ni de règle nouvelle : structure sémantique, titre et description uniques, URL canonique sans paramètre de session ni identifiant visiteur, langue déclarée, données structurées conformes au contenu réel, plan du site et règles d'accès, signaux web essentiels, images et médias avec texte alternatif et sous-titres selon D-021, contenu dupliqué entre variantes de ville et de langue, trafic payant absent.

## 2. Vérifications à rejouer sur le rendu réel

Chaque vérification est exécutée sur le rendu public concerné. La colonne preuve désigne ce qui est archivé, sans anticiper le résultat.

| Identifiant | Vérification | Moment selon le PRD | Résultat attendu | Preuve à archiver |
|---|---|---|---|---|
| V1 | Structure sémantique des pages publiques | Revue DOM et audit accessible | Balises de titre, de navigation et de contenu utilisées selon le rôle, jamais pour l'apparence | Extrait du rendu et compte rendu de l'audit |
| V2 | Titre et description | Avant la revue de chaque page publique | Un titre et une description uniques par page indexable, rédigés en français | Extrait du rendu et de l'en-tête, avec l'URL concernée |
| V3 | URL canonique | Avant la revue de chaque page publique | Une URL canonique stable par contenu, sans paramètre de session ni identifiant visiteur | Extrait de l'en-tête et du balisage, avec l'URL concernée |
| V4 | Langue déclarée | Contrôle de l'attribut de langue | Langue du document déclarée, sans variante ajoutée avant décision | Extrait de l'attribut de langue |
| V5 | Données structurées | Avant la publication d'une offre, d'une vidéo ou d'une organisation | Types adaptés au contenu réel, sans donnée inventée | Rapport de validation du schéma et contenu concerné |
| V6 | Plan du site et règles d'accès | Avant le déploiement web | Plan des pages publiques, règles sans contenu privé, chemins vérifiés | Fichiers publiés et trace des chemins vérifiés |
| V7 | Signaux web essentiels | Après chaque mise en production web | Mesure sur données de terrain, sans seuil nouveau avancé ici | Rapport de terrain daté avec source et portée |
| V8 | Images et médias | Revue de contenu avant publication | Texte alternatif utile et sous-titres conformes à la règle D-021 | Extrait du contenu et état des sous-titres |
| V9 | Contenu dupliqué | Revue éditoriale avant publication | Contenu distinct justifié entre variantes de ville et de langue | Extrait comparatif et motif éditorial |
| V10 | Trafic payant et identifiant visiteur | Revue du registre et des campagnes | Aucun achat de position, aucun identifiant permanent écrit pour le référencement | Extrait du registre et des campagnes |

Aucune vérification n'est marquée comme réussie dans ce document. Aucun identifiant de participant, de machine ou de compte réel n'y est inscrit.

## 3. Extractions datées SEO-01 et SEO-02

Les deux sources, les fréquences, les formats d'extrait et les cibles intérimaires sont ceux de la fiche SEO web. Ils sont repris sans modification.

| Identifiant | Source et fréquence | Champs de l'extrait | Ce qui est archivé |
|---|---|---|---|
| SEO-01 | Google Search Console, vue Performance filtrée sur les pages publiables du domaine, chaque lundi à 09:00 UTC | `date`, `source`, `scope`, `pages_publiables`, `pages_indexees`, `ratio` | Extrait JSON avec date d'extraction, date de la donnée et portée |
| SEO-02 | Chrome UX Report via l'API PageSpeed Insights, sur les URL publiques du domaine, le 1er du mois à 09:00 UTC | `date`, `source`, `url`, `metric`, `pass_rate` | Extrait JSON avec date d'extraction, date de la donnée et portée |

La première extraction sert de base de lecture, pas de cible relevée. Chaque extrait est archivé dans `memoires/` avec les trois champs obligatoires. Aucun extrait n'est publié sans ces champs. Les cibles intérimaires, au moins 90 % d'indexation sous 30 jours et au moins 90 % d'URL qui passent les trois signaux de terrain, sont des décisions arrêtées le 26 novembre 2026. Le présent protocole ne les modifie pas et ne prétend pas les avoir atteintes. Aucun achat de position dans la recherche n'est utilisé pour améliorer ces mesures, selon D-019.

## 4. Responsabilité et moments du contrôle

Le titulaire intérimaire des mesures SEO et des contrôles est Espoir LOEMBA depuis le 25 novembre 2026. Il cadre le protocole et exécute le premier passage sur le rendu réel, sans délégation tacite. Le contrôle est rejoué en revue de sortie MVP avec l'identifiant du relecteur et la date, conformément à la roadmap.

La porte 7 du dossier sprint 1 reste liée à l'existence d'un rendu web réel. Ce protocole ne la remplace pas. Aucun tag, aucun rapport de mesure et aucun résultat d'extraction ne sont avancés ici.

## 5. Ce que ce protocole ne fait pas

Il ne contient aucun code applicatif, ne produit aucun rendu, n'exécute aucun contrôle, ne publie aucun extrait, n'ajoute aucun seuil, ne crée aucune page pour un moteur, n'introduit aucun classement payant ni identifiant visiteur permanent, ne remplace aucun avis juridique externe et ne lève aucune porte.
