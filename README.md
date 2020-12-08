# APSAC
APSAC est un programme permettant d'analyser plusieurs fichiers (csv, json ...) afin d'en sortir plusieurs statistiques.

### Pourquoi ce projet ? Et comment ?
Ce sujet nous a été proposé comme sujet de Stage par un laboratoire de recherche, le CERV, associé à notre école, l'ENIB. Nous avons choisis de coder avec le language Python car, nous sommes à l'aise avec ce language, plusieurs bibliothèque comme pandas pourrons fortement nous simplifier le projet et ce language est plutôt simple d'utilisation.

### Explications Dossiers
- DataE4 : Dossier ayant les csv extrait de la montre empatica 
- EyeTracker : Dossier regroupant tous les csv de l'EyeTracker ainsi qu'un fichier info
- Python : Tous les modules python du programmes sont ici
- SimulateurIPG : Dossier avec toutes les info importantes venant du simulateur
- SortiePython : Tous les csv traités de part le programme python 
- imageTuto : Toutes les images utilisées par le wiki github

Pour voir cette explication complète : [cliquez ici](https://github.com/BenderSaucisson/APSAC/wiki/Explication-Dossiers-Github)

### Module Python
- Main.py : Toutes les fonctions principales du programme se font traités ici
- entree.py : Traite ce que doit écrire l'utilisateur
- filtre.py : Filtrere toutes les données voulu 
- arrangeTime.py : Convertit les timestamps des csv
- getTime.py : Récupère les données de commencement de la simulation
- confidence.py : Filtre les données non conforme
- aberrance.py : Filtre les données aberrantes 
- statistique.py : Création des statistques voulues

Pour voir cette explication complète : [cliquez ici](https://github.com/BenderSaucisson/APSAC/wiki/Explication-Module-Python)

### Matériels
- [EyeTracker](https://pupil-labs.com/products/core/)
- [Simulateur Voiture Autonome](https://ipg-automotive.com/fr/)
- [Montre Connectée](https://www.empatica.com/en-eu/research/e4/)

### Exemples
Après avoir télécharger notre archive du projet à partir de github, vous pouvez désormais constater qu'il y a déjà un jeu de valeur présent (tous les csv tels que blinks...) Essayer donc avant toute chose de tester la rubrique 'Marche à suivre' sur ce jeu de valeur, à partir de plusieurs images je montrerai ce qui est important d'observer pour voir si ces données sont utilisable.

Pour voir les multiples exemple de graph c'est [ici](https://github.com/BenderSaucisson/APSAC/wiki/Exemples)
Avant toute chose les graphiques présentés sur la page d'examples sont sans informations pendant certains intervalles, la raison est quand l'on veut utiliser notre application il faut renseigner des intervales d'études et si des valeurs sont en dehors de tous les intervalles d'études alors elles sont supprimés.

### Déplacement Dossier
- Empatica : Extraire et déplacer vos csv (ACC, BVP, EDA, HR, IBI, TEMP...) : tutoriel
- EyeTracker : Extraire et déplacer vos csv ainsi qu'un fichier json : [tutoriel](https://github.com/BenderSaucisson/APSAC/wiki/Fichiers-Eye-Tracker)
- SimulateurIPG : Déplacer le fichier texte de log de la simulation dans le dossier suivant "SimulateurIPG/Log" et le fichier csv des données exportée : [tutoriel](https://github.com/BenderSaucisson/APSAC/wiki/Fichiers-Simulateur-IPG)

### Marche à suivre
- Bien vous situer dans le dossier python de notre github puis lancer la console
- 'python Main.py'
"Votre nom de fichier d'export :"
- 'NomDuFichierExport'
"Combien de surfaces utilisées avez vous differencié avec Pupil Player :"
- 'NombreDeSurfacesUtilisés'
"Comment s'appelle vos surfaces :"
- 'NomDesSurfaces'
"Combien d'intervalles voulez vous examiner : "
- 'CombienIntervallesVousVoulez'
"Début de l'intervalle n°", i+1," en seconde :"
"Fin de l'intervalle n°", i+1," en seconde :"
- 'QuoiCommeIntervalles'
"Combien de graphique voulez vous afficher :"
- 'CombienDeGraphVousVoulez'
"Quel graphique voulez vous afficher :"
- 'QuoiGrapher'

### Statistique
A partir de chaque statistique que je vais citer nous pouvons obtenir le minimum, maximum moyenne et médiane.
Nous pouvons calculer grâce au programme : la fréquence de clignement, la dispersion du son regard, le diamètre pupillaire, la distance entre chaque fixations, le rythme cardiaque, la conductivité de la peau
