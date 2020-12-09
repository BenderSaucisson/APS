#importation des modules
import stat
import getTime
import neurokit2 as nk
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

#fonction principale du module statistique
def statistique(ID,nombre, listeDebut, listeFin,stat):
  #variable compteur
  i = 0
  #boucle jusqua ce que le compteur atteigne la valeur du nombre d'intervalle que l'utilisateur veut analyser
  while i < nombre :
    #On ajoute la ligne fraichement crée
    stat = stat.append(ligneStatistique(ID,listeDebut,listeFin,i), ignore_index=True)
    #incrémentation
    i += 1
  return stat
  #plt.show()


def ligneStatistique(ID,listeDebut,listeFin,i):
  '''#création de liste pour stocker les résultats et ensuite les plot
        listeFreqClign = []
        listeDispersion = []
        listeMoyenneDiametrePupille = []
        listeMaxDiametrePupille = []
        listeMinDiametrePupille = []
        listeMouvementFixation = []
        listeMoyenneRythmeCardiaque = []
        listeMaxRythmeCardiaque = []
        listeMinRythmeCardiaque = []
        listeVariationRythmeCardiaque= []
        listeConductivitePeau = []
        listeMoyenneConductivitePeau = []
        listeMaxConductivitePeau = []
        listeFrequenceConductivitePeau = []'''
  debut=listeDebut[i]
  duration=listeFin[i] - listeDebut[i]
  #On ajoute chaque statistique une par une dans chaque liste
  listeFreqClign=freqClignement(ID,debut,duration)
  #listeDispersion.append(dispersion(listeDebut[i],listeFin[i]-listeDebut[i]))
  listeDiametrePupille=DiametrePupille(ID,debut,duration)
  listeMoyenneDiametrePupille=listeDiametrePupille[0]
  listeMaxDiametrePupille=listeDiametrePupille[1]
  listeMinDiametrePupille=listeDiametrePupille[2]
  #listeMouvementFixation.append(mouvementFixation(listeDebut[i],listeFin[i]-listeDebut[i]))
  listeRythmeCardiaque=RythmeCardiaque(ID,debut,duration)
  listeMoyenneRythmeCardiaque=listeRythmeCardiaque[0]
  listeMaxRythmeCardiaque=listeRythmeCardiaque[1]
  listeMinRythmeCardiaque=listeRythmeCardiaque[2]
  #listeVariationRythmeCardiaque.append(VariationRythmeCardiaque(listeDebut[i],listeFin[i]-listeDebut[i]))
  #listeMaxVariationRythmeCardiaque.append(VariationRythmeCardiaque(listeDebut[i],listeDebut[i]+listeFin[i])[1])
  #listeMinVariationRythmeCardiaque.append(VariationRythmeCardiaque(listeDebut[i],listeDebut[i]+listeFin[i])[2])
  listeConductivitePeau = ConductivitePeau(debut,duration)
  listeMoyenneConductivitePeau=listeConductivitePeau[0]
  listeMaxConductivitePeau=listeConductivitePeau[1]
  listeFrequenceConductivitePeau=listeConductivitePeau[2]
  #Quelque chose de plus jolie pour mieux représenter l'intervalle
  txt = str(listeDebut[i])+'/'+str(listeFin[i])
  #Création de la ligne à partir des autres listes
  newRow =  {'ID':ID,'Debut/Fin':txt,'FrequenceClignement':str(listeFreqClign)+' Hz','MoyenneDiametrePupille':listeMoyenneDiametrePupille,'MaxDiametrePupille':listeMaxDiametrePupille,'MinDiametrePupille':listeMoyenneDiametrePupille,'MoyenneRythmeCardiaque':listeMoyenneRythmeCardiaque,'MaxRythmeCardiaque':listeMaxRythmeCardiaque,'MinRythmeCardiaque':listeMinRythmeCardiaque,'MoyenneConductivitePeau':listeMoyenneConductivitePeau,'MaxConductivitePeau':listeMaxConductivitePeau,'FrequenceConductivitePeau':listeFrequenceConductivitePeau}
  return newRow
   
def statistiquecsv(stat):
  #création du csv
  stat.to_csv('../SortiePython/statistique.csv', index = False)

#calcul de tout les stats par rapport au diamètre de la pupille
def DiametrePupille(ID,debut, duration):
  #lecture csv
  df = pd.read_csv('../SortiePython/pupil_positions_filtred_t_c.csv')
  #on récupère la valeur en seconde de quand à commencer l'enregistrement des données sur le simulateur
  startTimeUnix = getTime.get_start_time_simulateur_s(ID)
  #On ne prends que les valeurs situées dans l'intervalle
  df = df[(df['pupil_timestamp']>=(debut+startTimeUnix)) & (df['pupil_timestamp']<=(debut+duration+startTimeUnix))]
  #calcul des valeurs intéressantes
  moyenneDiametrePupille = df['diameter'].mean()
  maxDiametrePupille = df['diameter'].max()
  minDiametrePupille = df['diameter'].min()
  #On arrondis les valeurs pour rendre ça plus beau
  moyenneDiametrePupille = np.around(moyenneDiametrePupille, decimals=1)
  maxDiametrePupille = np.around(maxDiametrePupille, decimals=1)
  minDiametrePupille = np.around(minDiametrePupille, decimals=1)
  #création de la liste regroupant les valeurs intéressantes
  diametrePupille = [moyenneDiametrePupille, maxDiametrePupille, minDiametrePupille]
  return(diametrePupille)


#fonction permettant de calculer la fréquence de clignement des yeux sur un intervalle donné
#debut : instant t ou commence l'analyse, duration : durée de l'analyse
def freqClignement(ID,debut, duration):
  #lecture du csv voulu
  df =  pd.read_csv('../SortiePython/blinks_filtred_t_a.csv')
  #on récupère la valeur en seconde de quand à commencer l'enregistrement des données sur le simulateur
  startTimeUnix = getTime.get_start_time_simulateur_s(ID)
  #on récupère chaque index correspondant à un clignement se situant entre le moment on l'on commence l'analyse jusque sa fin
  index = df[(df['start_timestamp'] > (debut+startTimeUnix)) & (df['start_timestamp'] < (debut+startTimeUnix+duration))].index.tolist()
  #Calcule de la fréquence
  fréquence = len(index)/duration
  fréquence = np.around(fréquence, decimals=1)
  #print('Il a eu ' , len(index) , ' clignement(s) depuis la seconde ' , debut , ' pendant ' , duration , ' seconde(s)\nPour une fréquence de : ' , fréquence , ' Hz' )
  return(fréquence)

#fonction permettant de calculer le pourcentage de temps passé à regarder les surfaces enregistrées
def pourcentageSurface():
  #lecture du csv voulu
  df = pd.read_csv('../EyeTracker/exports/000/surfaces/surface_gaze_distribution.csv')
  #on récupère les colonnes du csv pour avoir le nombre total de regard récupéré par l'application
  columns = df.columns  
  #totalité : nombre total de regard récupéré par l'application, utile pour le calcul de la fréquence
  totalite = float(columns[1])
  #variable compteur
  count = 0
  #création des listes pour les noms des surfaces ainsi que toutes les fois correspondantes où l'on regarde cette surface.
  nomSurface = []
  nombreRegard = []
  #on parcours le csv
  for label, row in df.iterrows():
    #ne pas prendre la première ligne car ce ne sont pas ces données que nou voulons
    if count != 0 :
      #on récupère le nom de la surface
      nomSurface.append(row[0])
      #ainsi que le nombre d'instant récupéré lié à cette surface
      nombreRegard.append(float(row[1]))
    #incrémentation
    count += 1
  #encore une variable de compteur
  i = 0
  #on passe la liste en array pour pouvoir la manipuler plus facilement grace à numpy
  arrayNombreRegard = np.array(nombreRegard)
  #Calcule du pourcentage de temps passé à regarder la surface
  nombreRegard = (arrayNombreRegard * 100)/totalite
  #on arrondi les valeurs présentent dans la liste pour que ce soit plus visible
  nombreRegard = np.around(nombreRegard, decimals=1)
  #Affichage
  while i < len(nomSurface) :
    #print('La surface '+nomSurface[i]+' a été regardé pendant ', nombreRegard[i],'pourcents du temps')
    i += 1

def dispersion(ID,debut, duration):
  #lecture du csv
  df = pd.read_csv('../SortiePython/fixations_filtred_t_c.csv')
  #on récupère la valeur en seconde de quand à commencer l'enregistrement des données sur le simulateur
  startTimeUnix = getTime.get_start_time_simulateur_s(ID)
  #On ne prends que les valeurs situées dans l'intervalle
  df = df[(df['start_timestamp']>=(debut+startTimeUnix)) & (df['start_timestamp']<=(debut+duration+startTimeUnix))]
  #calcul des valeurs intéressantes
  moyenneDispersion = df['dispersion'].mean()
  #on arrondie les valeurs précédentes
  moyenneDispersion = np.around(moyenneDispersion, decimals=1)
  #print('La moyenne de la dispersion du regard est de' , moyenneDispersion, 'depuis la seconde ' , debut , ' pendant ' , duration , 'seconde(s)' )
  return(moyenneDispersion)

def mouvementFixation(ID,debut, duration):
  df = pd.read_csv('../SortiePython/fixations_filtred_t_c.csv')
  #on récupère la valeur en seconde de quand à commencer l'enregistrement des données sur le simulateur
  startTimeUnix = getTime.get_start_time_simulateur_s(ID)
  df = df[(df['start_timestamp']>=(debut+startTimeUnix)) & (df['start_timestamp']<=(debut+duration+startTimeUnix))]
  listeNorme = []
  i = 0
  #print('PLOOOOOOOOOP    ',df.loc[df.index[0],'norm_pos_x'])
  while i < len(df)-1 :
    deplacementX = abs(df.loc[df.index[i],'norm_pos_x']-df.loc[df.index[i+1],'norm_pos_x'])
    deplacementY = abs(df.loc[df.index[i],'norm_pos_y']-df.loc[df.index[i+1],'norm_pos_y'])
    norme = math.sqrt((deplacementX**2)+(deplacementY**2))
    listeNorme.append(norme)
    i += 1
  #On calcule le quantile représentant 25% de la probabilité
  q1 = np.quantile(listeNorme,.25)
  #On calcule le quantile représentant 75% de la probabilité
  q3 = np.quantile(listeNorme,.75)
  plt.boxplot(listeNorme)
  plt.show()
  iq_range = q3 - q1
  iq_range = np.around(iq_range, decimals=3)
  return(iq_range)


def RythmeCardiaque(ID,debut, duration):
  #lecture csv
  df = pd.read_csv('../Data_E4/CSV_standard/HR_standard.csv')
  #on récupère la valeur en seconde de quand à commencer l'enregistrement des données sur le simulateur
  startTimeUnix = getTime.get_start_time_simulateur_s(ID)
  #On ne prend que les valeurs situées dans l'intervalle
  df = df[(df['Time_stamp']>=(debut+startTimeUnix)) & (df['Time_stamp']<=(debut+duration+startTimeUnix))]
  #calcul des valeurs intéressantes
  moyenneRythmeCardiaque = df['Av_heart_rate'].mean()
  maxRythmeCardiaque = df['Av_heart_rate'].max()
  minRythmeCardiaque = df['Av_heart_rate'].min()
  #On arrondis les valeurs pour rendre ça plus beau
  '''moyenneDiametrePupille = np.around(moyenneDiametrePupille, decimals=1)
  maxDiametrePupille = np.around(maxDiametrePupille, decimals=1)
  minDiametrePupille = np.around(minDiametrePupille, decimals=1)'''
  #création de la liste regroupant les valeurs intéressantes
  rythmeCardiaque = [moyenneRythmeCardiaque, maxRythmeCardiaque, minRythmeCardiaque]
  return(rythmeCardiaque)

def VariationRythmeCardiaque(ID,debut, duration):
  #lecture csv
  df = pd.read_csv('../Data_E4/CSV_standard/IBI_standard.csv')
  #on récupère la valeur en seconde de quand à commencer l'enregistrement des données sur le simulateur
  startTimeUnix = getTime.get_start_time_simulateur_s(ID)
  #On ne prends que les valeurs situées dans l'intervalle
  df = df[(df['Time_stamp']>=(debut+startTimeUnix)) & (df['Time_stamp']<=(debut+duration+startTimeUnix))]
  #calcul des valeurs intéressantes
  moyenneVariationRythmeCardiaque = df['IBI'].mean()
  #On arrondis les valeurs pour rendre ça plus beau
  moyenneVariationRythmeCardiaque = np.around(moyenneVariationRythmeCardiaque, decimals= 3)
  #print('La moyenne de durée entre les battements de coeur est de' , moyenneVariationRythmeCardiaque, 'depuis la seconde ' , debut , ' pendant ' , duration , 'seconde(s)' )
  return(moyenneVariationRythmeCardiaque)

def ConductivitePeau(debut, duration):
  #lecture csv
  df= pd.read_csv('../SortiePython/EDA_a.csv')
  #Bibliothèque neurokit2
  eda_signal=df['Electrodermal_activity']
  # Process du signal EDA brut
  signals, info = nk.eda_process(eda_signal, sampling_rate=8)
  # Filter phasic and tonic components
  data = nk.eda_phasic(nk.standardize(eda_signal), sampling_rate=8)
  #Index de début d'intervalle
  dataDebut=debut*4
  #Index de fin d'intervalle
  dataFin=(debut+duration)*4
  moyenneRaw=signals['EDA_Raw'][dataDebut:dataFin].mean()
  maxRaw=signals['EDA_Raw'][dataDebut:dataFin].max()
  totalPeaks=signals['SCR_Peaks'][dataDebut:dataFin].sum()
  nbData=len(signals['EDA_Raw'][dataDebut:dataFin])/4
  freqPeak=totalPeaks/nbData
  #print("Entre ", debut ," et ", duration+debut ,"secondes, il y a eu ",totalPeaks," Pics en pour ",duration,"sec et donc une fréquence de ",freqPeak," Hz")
  conductivitePeau = [moyenneRaw,maxRaw,freqPeak]
  return conductivitePeau
