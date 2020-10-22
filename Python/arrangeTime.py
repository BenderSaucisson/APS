import csv
#importation du module pour savoir quand l'enregistrement a commencé (UNIX)
import getTime
import pandas as pd
import os

#fonction permettant de changer le temps de chaque csv en seconde UNIX
def arrangeTime(chemin):
  #on créé le csv voulu
  with open('../SortiePython/'+chemin+'_filtred_t.csv', 'w', newline='') as output:
    #création de la variable de sortie
    writer = csv.writer(output, delimiter=',')
    liste=[]
    #création d'un compteur pour ne pas prendre en compte la première ligne (ligne du nom des variables)
    lignecount = 0
    #on ouvre le csv voulu
    with open('../SortiePython/'+chemin+'_filtred.csv') as c:
      #création de la variable de lecture
      reader = csv.reader(c, delimiter=',')
      #on analyse toutes les lignes du csv
      for ligne in reader:
        #on modifie toutes les lignes sauf la première
        if lignecount != 0 :
          #on ajoute/soustraie avec les valeurs prises dans le json
          ligne[0] = float(ligne[0]) - getTime.get_start_time_synced_s() + getTime.get_start_time_system_s()
          liste.append(ligne)
        #on copie juste la première ligne
        else :
          liste.append(ligne)
        #incrémentation
        lignecount = lignecount+1
      #tout mettre dans la variable de sortie
      writer.writerows(liste)
  #supprime le dernier csv
  os.remove('../SortiePython/'+chemin+'_filtred.csv')



'''
TEST
def arrangeTime(chemin):
  filtre = pd.read_csv('../SortiePython/'+chemin+'.csv')
  print (filtre.loc[filtre['gaze_timestamp']])
  #filtre.loc[filtre['gaze_timestamp']] = filtre.loc[filtre['gaze_timestamp']] - getTime.get_start_time_synced_s() + getTime.get_start_time_system_s()
  filtre.to_csv('../SortiePython/'+chemin+'_t.csv',index=False)
  '''