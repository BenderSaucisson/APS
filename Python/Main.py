#importation des modules

#importation du module visant à rendre utilisable la variable temps (en UNIX)
import arrangeTime
#importation du module pour filtrer les variables non désirés présentes dans les csv
import filtre
#importation du module de filtrage par rapport à la confidence, si confidence trop basse alors la ligne est effacée
import confidence
import graph
import entree
import aberrance
import statistique
import getTime
import pytz

oui = getTime.get_start_time_simulateur_s()
print(oui)

nomExport, surfaces = entree.variableCmd()

#création d'une liste avec les noms des différents csv à utiliser, les csv sont présent dans le dossier 'exports'

nombreIntervalles, debutIntervalle, finIntervalle = entree.variableNombreIntervales()


for i in surfaces :
  filtre.filtreIntervalle(nombreIntervalles, debutIntervalle, finIntervalle, i, nomExport)
  #fonction principale du module filtre
  filtre.filtre(i)
  #fonction principale du module arrangeTime
  arrangeTime.arrangeTime(i)
  #Cela ne sert à rien d'utiliser le module confidence sur le blink car cela à été préalablement fait par l'application
  if i != 'blinks':
    #fonction principale du module confidence
    confidence.confidence(i)
  #Pas besoin d'analyser les valeurs d'aberrance du module de fixations car préalablement fait par l'application
  if (i != 'fixations') & (i != 'pupil_positions'):
    #fonction principale du module d'aberrance
    aberrance.aberrance(i)

statistique.statistique(nombreIntervalles, debutIntervalle, finIntervalle)

entree.plotCmd()
graph.show()
