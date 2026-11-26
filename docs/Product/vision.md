# Pro : Document de vision

**Mission.** Organiser le travail des professionnels et le rendre visible, vérifiable et utile à tous.

**Vision.** Un réseau où l'on reconnaît les compétences à ce que les gens montrent, pas à ce qu'ils déclarent.

**Statut** : version 2, proposition de travail, 25 novembre 2026  
**Document associé** : [Manifeste Pro](./manifeste.md)  
**Documents de cadrage** : [Décisions](./decisions.md), [Mesure](./mesure.md), [Expérimentation](./experimentation.md), [Tableau de bord](./tableau-de-bord.md)

## 1. Le problème

LinkedIn a rendu le CV consultable. Nous faisons l'hypothèse qu'un fil vidéo peut rendre le travail visible : c'est précisément ce que la Phase 0 doit tester, avec H1 et H2.

Un professionnel passe des heures à rédiger une section « Expérience » que personne ne lit, puis à parcourir des offres où tout le monde se ressemble. Une entreprise publie une annonce que personne ne croit, parce qu'elle ne montre rien de son quotidien. Pendant ce temps, la preuve existe déjà : dans la vidéo d'un atelier, dans une explication de trente secondes, dans une conversation entre deux personnes qui font le même métier.

Pro part de là. Le fil vidéo n'est pas un divertissement collé sur un réseau professionnel. C'est le support de la preuve, sous réserve de validation sur le terrain.

Trois contraintes structurent le produit :

- un visiteur doit pouvoir voir sans s'inscrire ;
- une interaction doit toujours pouvoir être attribuée à quelqu'un ;
- la vérification doit rester rare et méritée.

## 2. La question posée

Comment ouvrir l'accès à tous sans ouvrir la porte à l'irresponsabilité ?

La réponse ne peut pas être binaire. « Tout le monde se connecte avant de voir quoi que ce soit » tue la découverte. « Personne ne se connecte jamais » tue la confiance. La vraie question est la suivante : à quel moment précis l'identité devient-elle nécessaire, et pourquoi ?

## 3. Ce que font les plateformes installées

**TikTok.** Hypothèse à tester : un visiteur non connecté peut parcourir le fil, chercher et regarder des vidéos sur le web, tandis que le like, le commentaire, le suivi et la publication demandent un compte. La politique de confidentialité précise que le contenu d'un compte public peut être consulté par des personnes sans compte et apparaître dans les moteurs de recherche [1]. Un guide tiers décrit le même comportement dans l'application [2] ; cette source secondaire doit être confirmée par test manuel avant d'être présentée comme un fait. Si l'hypothèse tient, l'accès sans compte sert à l'acquisition et la conversion intervient au premier geste d'interaction, pas à l'ouverture.

**LinkedIn.** Le profil public est une version simplifiée, avec des interrupteurs section par section, et les visiteurs non connectés peuvent être invités à se connecter pour voir le profil complet [3]. Une observation technique rapportée par un blog tiers indique que le mur d'authentification est déclenché selon l'adresse IP, le referrer, la vitesse des requêtes et la forme de l'URL [4]. Cette observation est non vérifiée et non reproductible dans notre cadrage : elle n'est pas présentée comme une règle établie. Les coordonnées, les messages et InMail restent fermés. Le mur est posé sur la page, pas sur l'action, avec un effet irrégulier sur l'expérience du visiteur.

TikTok et LinkedIn traitent l'identité comme un prérequis ou comme un filtre technique. Pro peut faire un autre choix. Traiter l'identité comme un **contrat d'action** : l'expliquer, la demander au bon endroit, et la proportionner à ce qui est en jeu.

## 4. Ce que disent les données disponibles

Les travaux publiés convergent, avec des réserves de terrain.

Une étude contrôlée présentée à CHI en 2016 a comparé inscription obligatoire et participation libre avec possibilité de revendiquer sa contribution ensuite. Supprimer l'obligation d'inscription a augmenté de **62 %** le nombre de personnes contribuant, sans dégradation de la qualité [5]. Ces résultats soutiennent l'hypothèse d'interface suivante, reliée à H4 : ne pas faire de l'enregistrement une barrière à la participation immédiate.

Nielsen Norman Group recommande depuis 1999 de repousser l'inscription le plus tard possible dans le parcours. Sur QuickenMortgage, le report de l'enregistrement après l'entrée dans le produit a fait doubler l'utilisation [6]. En 2014, le même groupe décrit le coût d'interaction des murs de connexion et rappelle que, sur mobile, il n'y a souvent pas de deuxième visite [7].

FT Strategies et Google News Initiative décrivent le passage du Financial Times d'une inscription obligatoire à une collecte progressive de l'information [8]. Le rapport cité ne permet pas d'attribuer directement ce changement à une baisse des revenus publicitaires. Rest of World, en 2026, a fait passer son seuil de cinq articles gratuits à trois et observé un comportement stable : **87 %** des personnes qui commencent l'inscription la terminent, et environ trois sur cinq passent par Google Sign-In [9]. Leur conclusion est utile : supprimer toute gêne n'est pas toujours le bon principe ; la gêne doit être proportionnée à la valeur reçue.

Les chiffres de l'écosystème éditorial appellent de la prudence. Piano rapporte un taux de conversion à l'abonnement d'environ 0,2 % chez les visiteurs non connectés contre environ 10 % chez les inscrits, mais seulement 3 % des inscrits convertissent au cours de leur première année [10]. Ce sont des données de presse, pas de réseau professionnel. Elles soutiennent une idée, pas une recette : la relation se construit dans la durée, et capturer une identité trop tôt ne garantit rien.

Le cadre européen est direct. Le Comité européen de la protection des données rappelle qu'une personne non connectée peut être une personne concernée au sens du RGPD dès lors qu'elle est identifiable [11]. Les identifiants d'appareil sont des données personnelles ; une pseudonymisation par fonction de hachage avec clé, la clé étant conservée séparément des pseudonymes, est recommandée lorsque le suivi est nécessaire [12][13]. « Sans compte » ne veut donc pas dire « sans données ». Les textes juridiques et les écrans d'interface parleront de **visiteur non connecté**, jamais d'utilisateur anonyme.

## 5. Décisions produit : quatre niveaux d'accès

| Niveau | Déclencheur | Autorisations | Données conservées |
|---|---|---|---|
| **N0 : Visiteur** | Aucun compte | Fil public, vidéos, profils publics, recherche | Session à courte durée, aucun identifiant permanent, agrégats uniquement |
| **N1 : Membre** | Email vérifié en phase 1. Téléphone et connexion sociale en phase 2, non spécifiés | Publication, like, commentaire, suivi, sauvegarde, chat 1:1 | Identifiant de compte, nom affiché, métier, ville, email vérifié |
| **N2 : Profil vérifié, phase 2, hors MVP** | Vérification à la demande de l'employeur, selon D-010 retenue le 26 novembre 2026 | **Phase 2 :** contact par les recruteurs, candidature avec dossier, badge « vérifié », visibilité accrue dans la recherche | Données de vérification minimales, avec date et méthode |
| **N3 : Organisation, phase 2** | Vérification de l'entreprise | Page entreprise, publication d'offres, messagerie recruteur, statistiques | Identité légale, domaine, documents de vérification |

Le mur n'est pas à l'entrée. Il est placé au premier geste qui crée une trace sociale ou juridique.

**Phase 2, hors MVP.** Le badge « vérifié », la candidature avec dossier et le message lié à N2 ne sont pas livrés dans la première version. Leur méthode, leur réversibilité et leur événement de mesure sont écrits dans D-010, retenue le 26 novembre 2026.

**Gratuité par phase.** Les phases 1 à 4 sont gratuites, conformément à D-005. La Phase 5 introduit un niveau organisations payant dont le nom et les privilèges sont définis par D-011, retenue le 26 novembre 2026. Aucun classement payant dans la recherche. Les offres signalées éventuelles restent hors recherche et relèvent de la Phase 5.

**Ancrage géographique.** Pro commence par les deux Congo : la République du Congo (Brazzaville) et la RDC (Kinshasa) forment le premier marché. Le reste de l'Afrique vient ensuite, puis le monde. Français d'abord. Le français est la seule langue des phases 0, 1 et 2 selon A-08, arbitrée le 26 novembre 2026. Toute langue ajoutée à partir de la Phase 3 est inscrite au registre avec date, responsable et marché avant le premier contenu dans cette langue. Les langues suivantes sont validées marché par marché, avec date et responsable inscrits au registre. Aucune autre langue n'est datée dans ce cadrage.

Les moments de conversion ne sont pas des interstitiels plein écran. Ce sont des phrases courtes, liées à une action, avec un marqueur de phase :

- **Phase 1.** « Connectez-vous pour retrouver cette vidéo plus tard. » après trois à cinq vidéos vues, au moment où la personne essaie de sauvegarder ou de suivre ;
- **Phase 1.** « Un compte permet à l'autre personne de savoir qui lui écrit. » au premier message ;
- **Phase 2, hors MVP.** « Les employeurs demandent un profil vérifié pour les candidatures. » au moment de postuler ;
- **Phase 2, hors MVP.** « Vérifiez votre profil pour continuer cette conversation. » quand un recruteur répond.

Chaque déclencheur de phase 1 est relié à `guest_save_attempt`, `signup_start` ou `message_sent` dans le [dictionnaire de mesures](./mesure.md).

Mode d'inscription : email vérifié en phase 1. Téléphone et connexion sociale en phase 2, non spécifiés. Le métier, la ville et la photo viennent ensuite, au fil de l'usage. La vérification arrive seulement quand une contrepartie existe : être contacté par un recruteur, postuler avec un dossier, publier une offre. Ces trois situations relèvent de la phase 2, sauf la publication d'offres qui relève des organisations.

Le chat oblige à identifier les deux parties. C'est la raison d'être du niveau N1. Une conversation professionnelle dans laquelle on ne sait pas qui écrit n'a pas de valeur professionnelle.

## 6. Règles de conception

**La lecture n'a pas de porte.** Le premier écran montre des vidéos. Aucun écran de création de compte bloquant avant le contenu.

**L'identité suit l'impact.** Regarder est libre. Répondre est identifié. Recruter est vérifié en phase 2.

**Chaque demande est expliquée.** Une phrase suffit. Aucun formulaire de neuf champs au premier lancement.

**Le contenu public reste public.** Les profils et vidéos ouverts sont accessibles aux moteurs de recherche, avec des réglages par section côté créateur. Pro ne reproduit pas le mur d'authentification de LinkedIn sur les pages publiques.

**Le visiteur n'est pas pisté.** Pas d'empreinte d'appareil, pas d'identifiant publicitaire, pas de traceur tiers dans le parcours non connecté. Les mesures d'audience sont agrégées.

**Le mode visiteur reste léger.** Bitrate adaptatif, compression forte, pas de chargement spéculatif inutile. La bande passante est un coût réel, surtout sur mobile et sur les réseaux du premier marché. La réactivité du client desktop est exigée dès la Phase 1, sans chiffre mesuré avancé ici (D-023).

**Les trois clients sont livrés ensemble.** Les clients `mobile`, `web` et `desktop` partagent la même promesse. La dimension `plateforme` prend les valeurs `mobile`, `web` et `desktop`, définies ainsi :

- `mobile` : applications natives iOS et Android sur téléphone.
- `web` : site responsive dans un navigateur, utilisé sur ordinateur et tablette.
- `desktop` : application exécutable installée sur Windows et macOS. Linux est différé et non spécifié en phase 1.

**Le terrain précède l'extrapolation.** Brazzaville et Kinshasa sont deux marchés distincts, avec des usages et des contraintes différents. Un constat observé dans l'une n'est pas présenté comme valable pour l'autre sans comparaison.

**La gratuité précède la monétisation.** Aucun privilège payant n'est introduit pendant les phases 1 à 4. Les pages et les rôles sont ouverts à tous. Le niveau organisations de la Phase 5 est distinct du réseau, ne modifie pas l'accès public et n'introduit aucun classement payant dans la recherche.

**Le fil se personnalise sans profil.** Pour un visiteur non connecté, la pertinence vient du métier ou de la ville choisie en début de parcours, pas d'un historique conservé. L'historique reste sur l'appareil et n'est attaché à un compte qu'après inscription.

**Une vidéo avec son est sous-titrée.** Les vidéos avec son du MVP disposent de sous-titres générés automatiquement et corrigés par l'auteur avant publication. Si la correction n'est pas faite, la vidéo reste en brouillon et n'est pas publiée. Règle D-021, écrite en FS-02 et FS-05 du PRD.

## 7. Architecture et confidentialité

Le chemin de lecture doit être séparé du chemin d'écriture dès le début [14]. Les vidéos du fil sont servies depuis un cache ou un CDN, avec des listes de candidats précalculées. Chaque réponse applique néanmoins les règles de visibilité courantes au moment de la lecture : blocage, suppression, confidentialité, signalement, région. Un cache ne doit jamais être considéré comme une autorisation.

La limitation de débit est différenciée par type d'abus : quelques tentatives par minute sur l'authentification, une limite haute mais bornée sur la lecture, une détection de vitesse sur les follows et les likes, une pénalité sur les erreurs répétées pour épuiser rapidement le budget d'un scanner.

La modération fonctionne en deux temps. Le texte peut être vérifié avant publication ; la vidéo passe toujours par un état `pending_review` et n'est publiée qu'après traitement asynchrone. Les signalements sont ouverts aux visiteurs. Chaque action de modération laisse une trace, avec notification et voie de recours. Si Pro dessert l'Union européenne, le régime applicable est à valider par conseil local dans `../Conformite/README.md` ; les articles cités n'imposent pas par eux-mêmes une relecture préalable dans le cadrage actuel.

Le visiteur non connecté reçoit un jeton de session à courte durée. Si un suivi est nécessaire, on emploie un identifiant non permanent haché avec clé, la clé étant conservée séparément des pseudonymes. Aucun identifiant d'appareil permanent n'est stocké. Aucune correspondance n'est faite entre appareils.

Les notifications push sont réservées aux niveaux N1 et suivants (D-013). C'est un choix de conception, pas une limite technique : un visiteur sans compte ne peut pas recevoir la réponse à quelque chose qu'il n'a pas publié.

## 8. Mesure et expérimentation

Le premier test oppose deux parcours : accès direct au fil contre mur de connexion au lancement. Son unité de randomisation, sa population sur `mobile`, `web` et `desktop`, sa durée, sa métrique primaire, ses garde-fous et sa règle d'arrêt sont écrits dans la [fiche d'expérimentation](./experimentation.md). Aucun effectif ni effet minimal détectable n'est avancé dans ce cadrage.

Les indicateurs sont définis une seule fois dans le [dictionnaire de mesures](./mesure.md) et lus dans le [tableau de bord](./tableau-de-bord.md). Ils comprennent :

- **inscriptions avec email vérifié pour 1 000 sessions de fil**, formule `signup_verified / feed_session_start * 1000`, qui remplace l'ancienne mesure sans événement source fondée sur des vérifications d'identité non instrumentées ;
- **vidéos vues par session**, calculées sur `video_impression`, sans confusion avec `video_complete` ;
- **part des membres qui publient**, calculée sur les comptes avec email vérifié ;
- **retour à sept jours**, calculé sur les comptes avec email vérifié ;
- **délai de première décision de modération**, **taux de contestation** et **taux de renversement** ;
- taux de sauvegarde, messages envoyés et signalements.

La mesure à sept jours est encadrée par D-020 : « La mesure à sept jours porte sur les comptes ayant un email vérifié. Aucune cohorte visiteur à sept jours n'est calculée, puisqu'aucun identifiant permanent visiteur n'est conservé. »

Les garde-fous sont les suivants : pas de hausse des signalements, pas de hausse des comptes suspects, pas de plainte liée aux données du visiteur, pas de dégradation du taux de publication chez les membres. Leur base est relevée pendant la Phase 0 ou les deux premières semaines d'observation ; le seuil relatif et la fenêtre sont inscrits au registre avant le premier test. Aucun seuil chiffré n'est inventé ici.

Règle de décision anticipée : si le parcours ouvert augmente les inscriptions avec email vérifié pour 1 000 sessions de fil sans dégrader les garde-fous, il devient le parcours par défaut. Une baisse des inscriptions au premier jour n'est pas un échec si la mesure d'acquisition vérifiée progresse. La décision finale est écrite au registre avec sa date et son propriétaire.

## 9. Limites de cette proposition

Les études citées viennent surtout de la presse, du commerce en ligne et de la science citoyenne. Leur transposabilité à un fil vidéo professionnel reste à vérifier. Aucune ne décrit précisément les deux marchés congolais. Le cycle de recherche UX prévu à Brazzaville et Kinshasa sert à combler ce vide avant toute extension régionale.

Le visiteur non connecté consomme de la bande passante sans générer de compte immédiat. Le modèle économique n'est pas fixé dans cette version : la gratuité totale est un choix d'acquisition, surtout pour les personnes en recherche d'emploi. Le coût sera couvert plus tard, par un plafond de lecture dont le seuil et la phase restent à trancher, par des offres signalées hors recherche en Phase 5, ou par le niveau organisations payant de la Phase 5. Aucun de ces leviers ne transforme l'accès public en parcours publicitaire hostile.

Un fil public est aussi un fil gratuit pour les robots de collecte. Les limites de débit et les règles pour les crawlers doivent être calibrées avant la croissance, pas après.

Le mot « vérifié » engage la plateforme. Un badge décerné trop vite sur un profil professionnel cause plus de tort qu'un profil non vérifié. La méthode de vérification N2 est décrite dans D-010, retenue le 26 novembre 2026, et doit être documentée et réversible.

Le risque de fond reste le même que pour tout réseau : sans créateurs pour alimenter le fil au départ, l'algorithme n'a rien à recommander. L'ouverture au grand public ne remplace pas une animation ciblée des premiers métiers, décrite dans `../Growth/README.md`.

## 10. Références

1. TikTok, *Privacy Policy*, mise à jour annoncée le 15 juillet 2026, date non vérifiée lors de l'audit : https://www.tiktok.com/legal/page/us/privacy-policy/en
2. *Watch TikTok Without App - Complete Guide (2026)*, source secondaire, hypothèse à confirmer par test manuel, consulté le 25 novembre 2026 : https://itechpulsehub.com/watch-tiktok-without-app-complete-guide-2026
3. LinkedIn Help, *LinkedIn public profile visibility* et *Control your public LinkedIn profile*, consulté le 25 novembre 2026 : https://www.linkedin.com/help/linkedin/answer/a518980 et https://www.linkedin.com/help/linkedin/answer/a528138
4. LinkedViewer, *LinkedIn "Sign In to View Full Profile"*, observation technique non vérifiée, source secondaire, consulté le 25 novembre 2026 : https://linkedviewer.com/blog/linkedin-sign-in-to-view-full-profile
5. Caroline Jay, Robert Dunne, David Gelsthorpe, Markel Vigo, *To Sign Up, or not to Sign Up?*, CHI 2016, DOI 10.1145/2858036.2858319 : https://doi.org/10.1145/2858036.2858319
6. Nielsen Norman Group, *Web Research: Believe the Data*, 1999 : https://www.nngroup.com/articles/web-research-believe-the-data/
7. Nielsen Norman Group, *Login Walls Stop Users in Their Tracks*, 2014 : https://www.nngroup.com/articles/login-walls/
8. FT Strategies et Google News Initiative, *Turning Anonymous Visitors into Known Users: The Power of Registration*, date de publication non vérifiée, accès le 25 novembre 2026 : https://programmes.ftstrategies.com/insights/turning-anonymous-visitors-into-known-users-the-power-of-registration
9. Rest of World, *What we learned in the first 3 months with a registration wall*, 10 septembre 2026 : https://restofworld.org/inside/learned-in-first-months-registration-wall/
10. Digiday, *Publishers use registration walls as subscription bridges*, 21 juillet 2022, données Piano : https://digiday.com/media/media-briefing-publishers-use-registration-walls-as-subscription-bridges/
11. EDPB, *Guidelines 8/2020 on the targeting of social media users*, consulté le 25 novembre 2026 : https://www.edpb.europa.eu/system/files/documents/2021-04/edpb_guidelines_082020_on_the_targeting_of_social_media_users_en.pdf
12. EDPB, *Guidelines 4/2019 on Article 25 Data Protection by Design and by Default*, version 2.0, 2019, consulté le 25 novembre 2026 : https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201904_dataprotection_by_design_and_by_default_v2.0_en.pdf
13. ENISA, *Recommendations on shaping technology according to GDPR provisions*, 2018, consulté le 25 novembre 2026 : https://www.enisa.europa.eu/sites/default/files/publications/WP2018%20O.2.2.5%20-%20Recomendations%20on%20shaping%20technology%20according%20to%20GDPR%20provisions%20-%20Part%201.pdf
14. Stream, *How to Build a Social Media App: Architecture, Data Model, and Scaling Guide*, 26 mars 2026 : https://getstream.io/blog/build-a-social-media-app/

*Note de forme.* La structure de ce document et du manifeste associé suit la tradition des documents publics de Google : une mission courte, des principes énoncés sans détour, des décisions reliées à des mesures. Les formulations sont propres à Pro. La référence de style est https://about.google/company-info/philosophy/ .
