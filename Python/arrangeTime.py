'''
Un problème dans l'utilisation du matériel tel que l'EyeTracker est que le temps est relative au système, elle n'a donc aucun sens si nous la prenons tel quel. 
Il est donc nécessaire de la réajuster à l'aide d'un autre module, 'getTime' (que l'on expliquera plus tard). Pour cela il faut prendre la valeur du csv et lui faire subi des opérations pour arriver au temps UNIX. 
Ce qui est beaucoup plus simple pour travailler avec plusieurs appareil/système en simultané dans un programme.
'''

import csv
#importation du module pour savoir quand l'enregistrement a commencé (UNIX)
import getTime
import pandas as pd
import os

#fonction permettant de changer le temps de chaque csv en seconde UNIX
def arrangeTime(chemin,nomExport):
  if 'gaze_positions_on_surface_' in chemin:
    route = '../EyeTracker/exports/'+nomExport+'/surfaces/'+chemin+'.csv'
    colonne = 2
  elif ((chemin == 'gaze_positions') | (chemin == 'pupil_positions')) :
    route = '../EyeTracker/exports/'+nomExport+'/'+chemin+'.csv'
    colonne = 0
  elif ((chemin == 'fixations') | (chemin == 'blinks')):
    route = '../EyeTracker/exports/'+nomExport+'/'+chemin+'.csv'
    colonne = 1
  else :
    print('CSV non reconnu')
  #on créé le csv voulu
  with open('../SortiePython/'+chemin+'_t.csv', 'w', newline='') as output:
    #création de la variable de sortie
    writer = csv.writer(output, delimiter=',')
    liste=[]
    #création d'un compteur pour ne pas prendre en compte la première ligne (ligne du nom des variables)
    lignecount = 0
    #on ouvre le csv voulu
    with open(route) as c:
      #création de la variable de lecture
      reader = csv.reader(c, delimiter=',')
      #on analyse toutes les lignes du csv
      for ligne in reader:
        #on modifie toutes les lignes sauf la première
        if lignecount != 0 :
          #on ajoute/soustraie avec les valeurs prises dans le json
          ligne[colonne] = float(ligne[colonne]) - getTime.get_start_time_synced_s() + getTime.get_start_time_system_s()
          liste.append(ligne)
        #on copie juste la première ligne
        else :
          liste.append(ligne)
        #incrémentation
        lignecount = lignecount+1
      #tout mettre dans la variable de sortie
      writer.writerows(liste)
  #supprime le dernier csv
  #os.remove(route)



'''
TEST
def arrangeTime(chemin):
  filtre = pd.read_csv('../SortiePython/'+chemin+'.csv')
  print (filtre.loc[filtre['gaze_timestamp']])
  #filtre.loc[filtre['gaze_timestamp']] = filtre.loc[filtre['gaze_timestamp']] - getTime.get_start_time_synced_s() + getTime.get_start_time_system_s()
  filtre.to_csv('../SortiePython/'+chemin+'_t.csv',index=False)
  '''
