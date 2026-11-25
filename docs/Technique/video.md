# Vidéo : octets, coût et pipeline

**Propriétaire.** à nommer. **Statut.** proposée, budget ouvert. **Date.** 25 novembre 2026.

## Octets et bitrates

Échelle proposée, à confirmer avec `performance.md`. Les valeurs servent au calcul, pas à un engagement de qualité.

| Rendu | Bitrate cible | Octets pour 60 secondes | Usage |
|---|---:|---:|---|
| 240p | 0,3 Mbit/s | environ 2,2 Mo | profil R1 dégradé, faible consommation |
| 360p | 0,6 Mbit/s | environ 4,5 Mo | défaut mobile proposé |
| 480p | 1,0 Mbit/s | environ 7,5 Mo | défaut web proposé et défaut desktop proposé |
| 720p | 1,8 Mbit/s | environ 13,5 Mo | réseau rapide, compte ou visiteur selon budget |

Le défaut desktop proposé est 480p, soit 1,0 Mbit/s et environ 7,5 Mo pour 60 secondes. Il reste cohérent avec les bitrates ci-dessus et avec le budget du fil de `performance.md`. Sur profil R1 ou sur réseau limité, le client desktop ne force pas la haute qualité : la qualité s'adapte vers 360p ou 240p selon la règle de qualité automatique. Le rendu 720p n'est servi que lorsque le réseau et le budget le permettent, sans choix entre compte et visiteur hors arbitrage D-022.

Le transcodage se fait dans la file asynchrone. Le téléversement ne dépose que l'objet source. Le retrait des métadonnées EXIF, y compris GPS, est appliqué avant le stockage de toute version consultable. Test : un fichier source contenant une coordonnée GPS produit un objet sans cette coordonnée.

## Coût pour 1 000 vues

Formule à remplir avec le tarif retenu :

`cout pour 1 000 vues = (octets factures par vue x 1 000 / 1 000 000 000) x tarif convenu par Go + part du transcodage + part du stockage`

Le tarif, le fournisseur, la région et la période de facturation ne sont pas connus. Le budget CDN reste une décision ouverte inscrite au registre produit sous [D-022](../Product/decisions.md). Aucun ordre de grandeur externe n'est présenté comme un coût de Pro.

| Mesure | Cible proposée | Statut |
|---|---|---|
| Octets facturés par 1 000 vues | à mesurer sur le profil R1 | à confirmer |
| Coût pour 1 000 vues | à calculer après D-022 | à trancher |
| Taux de hit cache | au moins 85 % | à confirmer |
| Part des vues en qualité réduite | au plus 20 % sur le profil R1 | à confirmer |

## Règles de service

Le préchargement s'arrête à dix vidéos. Le mode faible consommation désactive le préchargement et plafonne la qualité, selon `performance.md`. Le chemin de lecture applique `decision_visibilite` avant de servir un segment, selon `architecture.md`. Ces règles s'appliquent aux trois clients, y compris le client desktop.

## Déclencheur

Cette fiche précède FS-02. Elle ne choisit ni fournisseur ni format de manifeste : `adr-001-stack.md` retient le stockage objet compatible S3 et le CDN derrière une interface, tandis que le fournisseur et le coût dépendent de D-022. Aucune valeur n'est présentée comme mesurée.
