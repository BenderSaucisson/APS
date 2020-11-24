# APSAC
APSAC est un programme permettant d'analyser plusieurs fichiers (csv, json ...) afin d'en sortir plusieurs statistiques.

### Matériels
- [EyeTracker](https://pupil-labs.com/products/core/)
- [Simulateur Voiture Autonome](https://ipg-automotive.com/fr/)
- [Montre Connectée](https://www.empatica.com/en-eu/research/e4/)

### Préambule
- Empatica : Extraire et déplacer vos csv (ACC, BVP, EDA, HR, IBI, TEMP...) : tutoriel
- EyeTracker : Extraire et déplacer vos csv ainsi qu'un fichier json : [tutoriel](https://github.com/BenderSaucisson/APSAC/wiki/Fichiers-Eye-Tracker)
- SimulateurIPG : Déplacer le fichier texte de log de la simulation dans le dossier suivant "SimulateurIPG/Log" et le fichier csv des données exportée : [tutoriel](https://github.com/BenderSaucisson/APSAC/wiki/Fichiers-Simulateur-IPG)

### Explications Dossiers
- Data_E4 : Ce dossier comprend deux autres dossiers, un qui récapitule tous les csv exportés depuis la montre empatica 'CSV_ori'. Ils ne sont pas traités contrairement aux autres csv présents dans l'autre dossier 'CSV_standard'. De base il y a 6 csv à l'origine : 'ACC' représentant les données de l'accéléromètre cela indique si l'utilisateur bouge son bras et dans quelle direction, 'BVP' représentant les données photopléthysmographique, 'EDA' représentant l'activité électrodermal en microsiemens, 'HR' quand à lui calcule le rythme cardiaque 'IBI' correspond à l'écart entre chaque battement de coeur et 'TEMP' représentant la température que perçoit le capteur en degrées C°.
  Tous ces csv vont donc passer dans un filtre pour se faire standardiser, aussi bien au niveau du format du csv (bien avoir une première ligne décrivant le contenu du csv) qu'au niveau des timestamps (que tous les csv commencent au bon moment). 
- EyeTracker : Ce dossier comprend un fichier json qui n'aura qu'une seule utilité, savoir les timestamps à laquelle commence l'enregistrement des csv venant de l'EyeTracker. Dans le dossier exporté (export) il y aura tout les csv exporté venant de l'EyeTracker : blinks.csv pour les données concernant le clignement des yeux, fixations.csv pour savoir quand est ce que l'utilisateur fixe quelque chose et où, gaze_positions.csv pour savoir où est ce que l'utilisateur regarde et pupil_positions.csv pour savoir comment se comporte les yeux de l'utilisateur (diamètre pupillaire...)
  Si durant l'enregistrement de l'EyeTracker le plugin de surface à été utilisé alors, un autre csv est présent dans le dossier surface qui est lui même dans le dossier d'export. Il s'appelle gaze_positions_on_surface_NomDeVotreSurface.csv et à toutes les données nécessaire liée à la surface
- Python : Ce dossier contient tout le code nécessaire pour que le programme fonctionne. Comme le nom du dossier le fait comprendre, le programme est codé en Pyhton. Je ne détaillerais pas plus le fonctionnement du code ici, je le ferais dans une autre rubrique.
- SimulateurIPG : Dedans on retrouve deux sous-dossier, il y a 'Donnée' un dossier dans lequel est présent le csv exporté à partir de l'application du simulateurIPG. Il y a aussi le sous-dossier 'Log'. Dans celui ci se trouve un fichier txt qui représente les logs de la session d'enregistrement son unique utilité est de donné au programme le temps où la simulation a commencé.
- SortiePython : Ce dossier récapitule tous les csv passant en entrée du programme après avoir subis un ensemble de filtre propre à chacun. Il y a nottament des filtres par rapport à l'aberrance des valeurs, par rapport au changement de timestamp, selon un intervalle, selon la confidence...
- imageTuto : Dossier utile uniquement pour la création du tutoriel. Ce dossier est utilisé comme espace de stockage des images afin de les faire référencer ensuite dans le tutoriel

### Module Python
L'ordre dans lequel je vais présenter les modules seront en fonction de leurs moment d'apparition dans le code. Logiquement le 'Main.py' sera le premier.

- Main.py :
Module principale par où se lance le programme, il réunit toutes les fonctions principales des autres modules et les mets dans le bon ordre pour que l'execution se passe bien. On importe tout les autres modules dans celui ci pour utiliser leurs fonctions. Dans ce module l'ordre des fonctions est important en effet après le passage d'un csv dans un filtre il ne porte plus le même nom donc si les étapes sont faites dans le désordre plus possible de se repérer. Il est aussi important de faire certains filtres avant d'autres pour des questions de cohérence.

- entree.py :
Ce module gère tout ce que l'utilisateur devra rentrer dans la console comme (dans l'ordre :) la localisation du fichier d'exportation des données, le nombre de surface enregistrées dans pupil player, leurs noms, le nombre d'intervalle à examiner, leurs débuts et commencements, ainsi que le nombre et contenu de graph à afficher.
Il va aussi gérer si l'utilisateur écris des valeurs qui n'ont aucun sens comme un entier au lieu d'un texte, en renvoyant une erreur précisant pourquoi il n'a pas le droit de faire ça.

- filtre.py :
Ce module comme beaucoup d'autres va filtrer un csv pour en creer un autre. La difference avec les autres modules de filtrage c'est que celui ci va filtrer de façon plus large le csv. Il ne va garder seulement les colonnes qui on un intérêt pour nous, tout ça en fonction du nom du csv. Si le csv s'appelle 'blink' alors il sera filtré d'une certaine façon, ce qui sera complètement différent du csv 'gaze_position'. Il va aussi supprimer certaines lignes qui ne nous intéressent pas en fonction de ce qu'on a rentrée comme intervalle en entrée dans la console. Dans le filtre de pupil_position on rajoute le fait qu'on doit moyenner la valeur des deux yeux pour avoir un diamètre pupillaire correcte.

- arrangeTime.py :
Un problème dans l'utilisation du matériel tel que l'EyeTracker est que le temps est relative au système, elle n'a donc aucun sens si nous la prenons tel quel. Il est donc nécessaire de la réajuster à l'aide d'un autre module, 'getTime' (que l'on expliquera plus tard). Pour cela il faut prendre la valeur du csv et lui faire subi des opérations pour arriver au temps UNIX. Ce qui est beaucoup plus simple pour travailler avec plusieurs appareil/système en simultané dans un programme.

- getTime.py :
On récupère la valeur de temps relative et absolu de commencement de l'enregistrement des données. On les récupère dans le fichier 'info.player.json'.

- confidence.py :
Ce module va filtrer toutes les lignes qui n'ont pas une confidence supérieur à 0.6. La confidence est la valeur de confiance envers la donnée que nous donne le logiciel. 0 = Médiocre, 1 = Très bonne. Nous avons choisis 0.6 car le site le conseillait. Bien entendu il ne faut pas appliquer ce filtre sur 'blink.csv' car le principe du clignement est qui'il y a une chute brute dans la confidence pour qu'il soit considéré comme tel.

- aberrance.py :
La encore un module de filtrage, il permet d'effacer les lignes qui sont des valeurs aberrantes. Une valeur aberrante est considérée comme tel quand elle est inférieur a : quantile(25%)-(ecartInterquantile*1.5) ou quand elle est supérieur a : quantile(75%)-(ecartInterquantile*1.5) ces valeurs ne sont pas du tout arbitraire c'est un référentile en terme de statistique.

- statistique.py :
Gros module regroupant toutes les stats à faire. Contrairement au module de grah, toutes les statistique possible nous les faisons et les stockons dans un fichier csv. Chaque statistique sera associé à un intervalle. Nous urons donc chaque statistique pour chaque intervalles different. Il sera ensuite lié au module de graph pour que l'on graph ces données.


### Statistique
