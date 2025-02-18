import csv
#importation du module pour savoir quand l'enregistrement a commencé (UNIX)
import getTime
import pandas as pd
import os
import sys

csv.field_size_limit(1000000000)

#fonction permettant de changer le temps de chaque csv en seconde UNIX
def arrangeTime(ID,chemin,nomExport):
  if 'gaze_positions_on_surface_' in chemin:
    route = '../EyeTracker/cache_ID'+ID+'/exports/'+nomExport+'/surfaces/'+chemin+'.csv'
    colonne = 2
  elif ((chemin == 'gaze_positions') | (chemin == 'pupil_positions')) :
    route = '../EyeTracker/cache_ID'+ID+'/exports/'+nomExport+'/'+chemin+'.csv'
    colonne = 0
  elif ((chemin == 'fixations') | (chemin == 'blinks')):
    route = '../EyeTracker/cache_ID'+ID+'/exports/'+nomExport+'/'+chemin+'.csv'
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
          ligne[colonne] = float(ligne[colonne]) - getTime.get_start_time_synced_s(ID) + getTime.get_start_time_system_s(ID)
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
