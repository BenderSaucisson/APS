# APSAC
APSAC est un programme permettant d'analyser plusieurs fichiers (csv, json ...) afin d'en sortir plusieurs statistiques.

### Explications Dossiers
Pour voir cette explication [cliquez ici](https://github.com/BenderSaucisson/APSAC/wiki/Explication-Dossiers-Github)

### Module Python
Pour voir cette explication [cliquez ici](https://github.com/BenderSaucisson/APSAC/wiki/Explication-Module-Python)

### Matériels
- [EyeTracker](https://pupil-labs.com/products/core/)
- [Simulateur Voiture Autonome](https://ipg-automotive.com/fr/)
- [Montre Connectée](https://www.empatica.com/en-eu/research/e4/)

### Statistique
A partir de chaque statistique que je vais citer nous pouvons obtenir le minimum, maximum moyenne et médiane.
Nous pouvons calculer grâce au programme : la fréquence de clignement, la dispersion du son regard, le diamètre pupillaire, la distance entre chaque fixations, le rythme cardiaque, la conductivité de la peau

### Exemples
Après avoir télécharger notre archive du projet à partir de github, vous pouvez désormais constater qu'il y a déjà un jeu de valeur présent (tous les csv tels que blinks...) Essayer donc avant toute chose de tester la rubrique 'Marche à suivre' sur ce jeu de valeur, à partir de plusieurs images je montrerai ce qui est important d'observer pour voir si ces données sont utilisable.

Pour voir les multiples exemple de graph c'est [ici](https://github.com/BenderSaucisson/APSAC/wiki/Examples)
Avant toute chose les graphiques présentés sur la page d'examples sont sans informations pendant certains intervalles, la raison est quand l'on veut utiliser notre application il faut renseigner des intervales d'études et si des valeurs sont en dehors de tous les intervalles d'études alors elles sont supprimés.

### Déplacement Dossier
- Empatica : Extraire et déplacer vos csv (ACC, BVP, EDA, HR, IBI, TEMP...) : tutoriel
- EyeTracker : Extraire et déplacer vos csv ainsi qu'un fichier json : [tutoriel](https://github.com/BenderSaucisson/APSAC/wiki/Fichiers-Eye-Tracker)
- SimulateurIPG : Déplacer le fichier texte de log de la simulation dans le dossier suivant "SimulateurIPG/Log" et le fichier csv des données exportée : [tutoriel](https://github.com/BenderSaucisson/APSAC/wiki/Fichiers-Simulateur-IPG)

### Marche à suivre
- Bien vous situer dans le dossier python de notre github puis lancer la console
- 'python Main.py'
- 'NomDuFichierExport'
- 'NombreDeSurfacesUtilisés'
- 'NomDesSurfaces'
- 'CombienIntervallesVousVoulez'
- 'QuoiCommeIntervalles'
- 'CombienDeGraphVousVoulez'
- 'QuoiGrapher'


