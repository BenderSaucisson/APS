#importation des modules

#importation du module visant à rendre utilisable la variable temps (en UNIX)
import arrangeTime
import arrangeTime_e4
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

listeID,nomExport, surfaces, e4, stat = entree.variableCmd()
nombreIntervalles, debutIntervalle, finIntervalle = entree.variableNombreIntervales()

for d in listeID:
  #Opérations sur les csv du pupil eye
  for i in surfaces :
    #fonction principale des module arrangeTime
    arrangeTime.arrangeTime(d,i,nomExport)
    filtre.filtreIntervalle(d,nombreIntervalles, debutIntervalle, finIntervalle, i)
    #fonction principale du module filtre
    filtre.filtre(i)
  
    #Cela ne sert à rien d'utiliser le module confidence sur le blink car cela à été préalablement fait par l'application
    if i != 'blinks':
      #fonction principale du module confidence
      confidence.confidence(i)
    #Pas besoin d'analyser les valeurs d'aberrance du module de fixations car préalablement fait par l'application
    if (i != 'fixations') & (i != 'pupil_positions'):
      #fonction principale du module d'aberrance
      aberrance.aberrance(i)

  #Opérations sur les csv de la montre Empatica_4
  for f in e4 :
    arrangeTime_e4.arrangeTime(d,f)
    arrangeTime_e4.arrangeTime_t0(d,f)
    filtre.filtreIntervalle(d,nombreIntervalles, debutIntervalle, finIntervalle, f)
    filtre.filtre(f)
    if (f== 'EDA'):
      aberrance.aberrance(f)

  #stat=statistique.statistique(d,nombreIntervalles, debutIntervalle, finIntervalle,stat)
  entree.plotCmd(d)
  graph.show()

#statistique.statistiquecsv(stat)

'''#Opérations sur les csv du pupil eye
for i in surfaces :
  #fonction principale des module arrangeTime
  arrangeTime.arrangeTime(i,nomExport)
  filtre.filtreIntervalle(nombreIntervalles, debutIntervalle, finIntervalle, i)
  #fonction principale du module filtre
  filtre.filtre(i)
  
  #Cela ne sert à rien d'utiliser le module confidence sur le blink car cela à été préalablement fait par l'application
  if i != 'blinks':
    #fonction principale du module confidence
    confidence.confidence(i)
  #Pas besoin d'analyser les valeurs d'aberrance du module de fixations car préalablement fait par l'application
  if (i != 'fixations') & (i != 'pupil_positions'):
    #fonction principale du module d'aberrance
    aberrance.aberrance(i)

#Opérations sur les csv de la montre Empatica_4
for f in e4 :
  arrangeTime_e4.arrangeTime(f)
  arrangeTime_e4.arrangeTime_t0(f)
  filtre.filtreIntervalle(nombreIntervalles, debutIntervalle, finIntervalle, f)
  filtre.filtre(f)
  if (f== 'EDA'):
    aberrance.aberrance(f)


statistique.statistique(nombreIntervalles, debutIntervalle, finIntervalle)
entree.plotCmd()
graph.show()'''

