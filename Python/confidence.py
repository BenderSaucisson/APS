import pandas as pd
import csv
import os

#fonction permettant de filtrer chaque csv pour qu'il n'y ai plus de valeurs avec une confidence inférieur à 0.6
def confidence(chemin):
  filtre = pd.read_csv('../SortiePython/'+chemin+'_filtred_t.csv')
  #on filtre le csv par rapport à la confidence, si trop faible alors on supprime
  filtre1 = filtre.query('confidence > 0.6')
  filtre1.to_csv('../SortiePython/'+chemin+'_filtred_t_c.csv',index=False)
  #supprime le fichier csv antérieur
  os.remove('../SortiePython/'+chemin+'_filtred_t.csv')

