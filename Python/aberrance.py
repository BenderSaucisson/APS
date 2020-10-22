#importation des modules
import csv
#le module pandas simplifie enormement l'utilisation des csv en python
import pandas as pd
#pour supprimer les dossiers antérieurs
import os

#fonction permettant d'automatiser le main
def aberrance(chemin):
  if chemin == 'gaze_positions' :
    aberranceGazePosition()
  #elif chemin == 'pupil_positions':
  #  aberrancePupilPosition()
  elif chemin == 'blinks':
    aberranceBlinks()
  elif 'gaze_positions_on_surface_' in chemin:
    aberranceSurface(chemin)
  else :
    print("erreur csv non reconnu")

#fonction permettant de trier les valeurs aberrantes sur le csv gaze_position, aussi bien le coordonnée x ou y
def aberranceGazePosition():
  #on récupère le csv
  filtre =  pd.read_csv('../SortiePython/gaze_positions_filtred_t_c.csv')
  #Pour chaque calcul on le fait deux fois, une pour la coordonée en x puis pour y
  #On calcule le quantile représentant 25% de la probabilité
  q1X = filtre['norm_pos_x'].quantile(.25)
  q1Y = filtre['norm_pos_y'].quantile(.25)
  #On calcule le quantile représentant 75% de la probabilité
  q3X = filtre['norm_pos_x'].quantile(.75)
  q3Y = filtre['norm_pos_y'].quantile(.75)
  #On calucle l'écart interquantile à partir des deux valeurs précédentes
  iq_rangeX = q3X - q1X
  iq_rangeY = q3Y - q1Y
  #On calcule la médiane, non pas la moyenne car justement la moyenne peut se faire biaiser à cause de valeurs aberrantes
  medianX = filtre['norm_pos_x'].median()
  medianY = filtre['norm_pos_y'].median()
  #On ne garde que les valeurs qui satisfont la condition suivante : mediane + 1.5*interquantile > valeur > mediane - 1.5*interquantile
  filtre = filtre[(filtre['norm_pos_x']<=(medianX + (1.5* iq_rangeX))) & (filtre['norm_pos_x']>=(medianX - (1.5* iq_rangeX)))]
  filtre = filtre[(filtre['norm_pos_y']<=(medianY + (1.5* iq_rangeY))) & (filtre['norm_pos_y']>=(medianY - (1.5* iq_rangeY)))]
  #timestamp : unité de temps, confidence : véracité de la valeur, diameter : diamètre de la pupille
  filtre.to_csv('../SortiePython/gaze_positions_filtred_t_c_a.csv',index=False)
  #supprime le fichier csv antérieur
  os.remove('../SortiePython/gaze_positions_filtred_t_c.csv')

#fonction permettant de trier les valeurs aberrantes sur le csv de surface, aussi bien la coordonnée x ou y
def aberranceSurface(surface):
  #On fait pareil ici, sauf que l'on change le nom des variables
  filtre =  pd.read_csv('../SortiePython/'+surface+'_filtred_t_c.csv')
  q1X = filtre['x_scaled'].quantile(.25)
  q1Y = filtre['y_scaled'].quantile(.25)
  q3X = filtre['x_scaled'].quantile(.75)
  q3Y = filtre['y_scaled'].quantile(.75)
  iq_rangeX = q3X - q1X
  iq_rangeY = q3Y - q1Y
  medianX = filtre['x_scaled'].median()
  medianY = filtre['y_scaled'].median()
  filtre = filtre[(filtre['x_scaled']<=(medianX + (1.5* iq_rangeX))) & (filtre['x_scaled']>=(medianX - (1.5* iq_rangeX)))]
  filtre = filtre[(filtre['y_scaled']<=(medianY + (1.5* iq_rangeY))) & (filtre['y_scaled']>=(medianY - (1.5* iq_rangeY)))]
  #timestamp : unité de temps, confidence : véracité de la valeur, diameter : diamètre de la pupille
  filtre.to_csv('../SortiePython/'+surface+'_filtred_t_c_a.csv',index=False)
  #supprime le fichier csv antérieur
  os.remove('../SortiePython/'+surface+'_filtred_t_c.csv')

#fonction permettant de trier les valeurs aberrantes dans le csv de blink, nottament celles avec un temps de blinks trop long
def aberranceBlinks():
  #On fait pareil ici, sauf que l'on change le nom des variables
  filtre =  pd.read_csv('../SortiePython/blinks_filtred_t.csv')
  q1 = filtre['duration'].quantile(.25)
  q3 = filtre['duration'].quantile(.75)
  iq_range = q3 - q1
  median = filtre['duration'].median()
  filtre = filtre[(filtre['duration']<=(median + (1.5* iq_range))) & (filtre['duration']>=(median - (1.5* iq_range)))]
  #timestamp : unité de temps, confidence : véracité de la valeur, diameter : diamètre de la pupille
  filtre.to_csv('../SortiePython/blinks_filtred_t_a.csv',index=False)
  #supprime le fichier csv antérieur
  os.remove('../SortiePython/blinks_filtred_t.csv')

#fonction permettant de trier les valeurs aberrantes dans le csv de pupil_positions, nottament celles qui on un diamètre trop élevé ou trop grand
'''def aberrancePupilPosition():
  #On fait pareil ici, sauf que l'on change le nom des variables
  filtre =  pd.read_csv('../SortiePython/pupil_positions_filtred_t_c.csv')
  q1 = filtre['diameter'].quantile(.25)
  q3 = filtre['diameter'].quantile(.75)
  iq_range = q3 - q1
  median = filtre['diameter'].median()
  filtre = filtre[(filtre['diameter']<=(median + (1.5* iq_range))) & (filtre['diameter']>=(median - (1.5* iq_range)))]
  #timestamp : unité de temps, confidence : véracité de la valeur, diameter : diamètre de la pupille
  filtre.to_csv('../SortiePython/pupil_positions_filtred_t_c_a.csv',index=False)
  #supprime le fichier csv antérieur
  os.remove('../SortiePython/pupil_positions_filtred_t_c.csv')'''