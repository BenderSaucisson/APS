#importation des modules
import csv
#le module pandas simplifie enormement l'utilisation des csv en python
import pandas as pd
#pour supprimer les dossiers antérieurs
import os
#importation du module getTime pour chopper le temps où l'enregistrement des csv ont commencés
import getTime

#fonction regroupant les autres fonctions pour que ce soit automatisé
def filtre(chemin):
  if chemin == 'gaze_positions' :
    filtreGazePosition()
  elif chemin == 'blinks' :
    filtreBlink()
  elif chemin == 'pupil_positions' :
    filtrePupilPosition()
  elif chemin == 'fixations' :
    filtreFixations()
  elif 'gaze_positions_on_surface_' in chemin:
    filtreSurface(chemin)
  elif chemin == 'ACC':
    filtreACC()
  elif chemin == 'BVP':
    filtreBVP()
  elif chemin == 'EDA':
    filtreEDA()
  elif chemin == 'HR':
    filtreHR()
  elif chemin == 'IBI':
    filtreIBI()
  elif chemin == 'TEMP':
    filtreTEMP()
  else :
    print("erreur csv non reconnu")

def filtreIntervalle(nombre, debut, fin,chemin):
  if(('gaze_positions_on_surface_' in chemin) | (chemin=='gaze_positions')):
    filtre = pd.read_csv('../SortiePython/'+chemin+'_t.csv')
    colonne = 'gaze_timestamp'
  elif ((chemin == 'fixations') | (chemin == 'blinks')):
    filtre = pd.read_csv('../SortiePython/'+chemin+'_t.csv')
    colonne = 'start_timestamp'
  elif chemin == 'pupil_positions':
    filtre = pd.read_csv('../SortiePython/'+chemin+'_t.csv')
    colonne = 'pupil_timestamp'
  elif chemin == 'ACC' or chemin=='BVP' or chemin=='EDA' or chemin=='HR' or chemin=='IBI' or chemin=='TEMP':
    filtre = pd.read_csv('../Data_E4/CSV_standard/'+chemin+'_standard.csv')
    colonne ='Time_stamp'
  else :
    print("erreur filtreIntervalle")
  i = 0
  reqd_IndexTot = []
  while i < nombre:
    reqd_Index = filtre[(filtre[colonne]>=debut[i]+getTime.get_start_time_simulateur_s()) & (filtre[colonne]<=getTime.get_start_time_simulateur_s()+fin[i])].index.tolist()
    reqd_IndexTot += reqd_Index
    i += 1
  filtre1 = filtre.loc[reqd_IndexTot]
  filtre1.to_csv('../SortiePython/'+chemin+'_intervalle_t.csv',index=False)
  #on retire les derniers .csv sauf ceux de l'E4
  if colonne != 'Time_stamp':
    os.remove('../SortiePython/'+chemin+'_t.csv')
    
#fonction permettant de filtrer les colonnes voulu du gaze_position.csv
def filtreGazePosition():
  #on va dans le dossier où se trouvent les csv pour les lirent
  filtre =  pd.read_csv('../SortiePython/gaze_positions_intervalle_t.csv')
  #timestamp : unité de temps, confidence : véracité de la valeur, norm_pos : position du regard sur l'image de la caméra frontale (world)
  filtre1 = filtre[['gaze_timestamp','confidence','norm_pos_x','norm_pos_y']]
  #on enregistre le nouveau csv dans un fichier plus "près"
  filtre1.to_csv('../SortiePython/gaze_positions_filtred_t.csv',index=False)
  os.remove('../SortiePython/gaze_positions_intervalle_t.csv')

#fonction permettant de filtrer les colonnes voulu du blinks.csv
def filtreBlink():
  filtre =  pd.read_csv('../SortiePython/blinks_intervalle_t.csv')
  #timestamp : temps où le clignement a commencé, duration durée du clignement
  filtre1 = filtre[['start_timestamp','duration']]
  filtre1.to_csv('../SortiePython/blinks_filtred_t.csv',index=False)
  os.remove('../SortiePython/blinks_intervalle_t.csv')

#fonction qui permet de chopper les intervalles où les yeux sont fermés 
def intervalleBlink():
  #on crée une liste pour stocker les intervalles où les yeux sont fermés 
  listeIntervalle = []
  with open('../SortiePython/blinks_filtred_t_a.csv') as c:
    #création de la variable de lecture
    reader = csv.reader(c, delimiter=',')
    #variable de compteur
    count = 0
    #pour chaque ligne dans le blink.csv
    for ligne in reader :
      #on ne prend pas la première ligne car elle représente les noms des colonnes 
      if count != 0 :
        #on passe de str a float les valeurs
        ligne0 = float(ligne[0])
        ligne1 = float(ligne[1])
        #premier terme : début du temps haut, deuxième terme : fin du temps haut
        listeIntervalle.append([ligne0,ligne0+ligne1])
      #incrémentation
      count += 1
    return listeIntervalle

#fonction permettant de filtrer les colonnes voulu du pupil_positions.csv
#Mais aussi de filtrer les valeurs non voulu si la personne ferme les yeux 
def filtrePupilPosition():
  #lecture du csv voulu
  filtre =  pd.read_csv('../SortiePython/pupil_positions_intervalle_t.csv')
  #on récupère les intervalles où la personne ferme les yeux
  listeIntervalle = intervalleBlink()

  i = 1
  liste = []
  diametre = 0
  while i<len(filtre) :
    diametre += filtre['diameter'][i]
    if i%4 == 0 :
      diametre /= 4
      filtre.loc[i,'diameter']=diametre
      diametre = 0
    else :
      liste.append(i)
    i += 1
  filtre.drop(liste, inplace = True)

  for intervalle in listeIntervalle :
    #on vérifie si une valeur du tableur des pas dans un intervalle où les yeux sont fermés, si oui données inutilisable
    reqd_Index = filtre[(filtre['pupil_timestamp']>=intervalle[0]) & (filtre['pupil_timestamp']<=intervalle[1])].index.tolist()
    #Si donnée inutilisable alors on enlève la ligne
    filtre.drop(reqd_Index, inplace = True)
  #timestamp : unité de temps, confidence : véracité de la valeur, diameter : diamètre de la pupille
  filtre1 = filtre[['pupil_timestamp','confidence','diameter']]
  filtre1.to_csv('../SortiePython/pupil_positions_filtred_t.csv',index=False)
  os.remove('../SortiePython/pupil_positions_intervalle_t.csv')

#fonction permettant de filtrer les colonnes voulu du fixations.csv
def filtreFixations():
  filtre =  pd.read_csv('../SortiePython/fixations_intervalle_t.csv')
  #timestamp : temps où la fixation a commencé, duration : durée de la fixation,norm_pos : position du regard sur l'image de la caméra frontale, confidence : véracité de la valeur
  filtre1 = filtre[['start_timestamp','duration','norm_pos_x','norm_pos_y','confidence','dispersion']]
  filtre1.to_csv('../SortiePython/fixations_filtred_t.csv',index=False)
  os.remove('../SortiePython/fixations_intervalle_t.csv')

#fonction permettant de filtrer les colonnes voulu du ..._surface.csv
def filtreSurface(chemin):
  filtre =  pd.read_csv('../SortiePython/'+chemin+'_intervalle_t.csv')
  #timestamp : temps où la fixation a commencé, x_scaled : position du regard sur la surface et son référentiel, on_surf : regard sur la surface ou non, confidence : véracité de la valeur
  filtre1 = filtre[['gaze_timestamp','x_scaled','y_scaled','on_surf','confidence']]
  filtre1.to_csv('../SortiePython/'+chemin+'_filtred_t.csv',index=False)
  os.remove('../SortiePython/'+chemin+'_intervalle_t.csv')
 

def filtreACC():
  filtre= pd.read_csv('../SortiePython/ACC_intervalle_t.csv')
  filtre.to_csv('../SortiePython/ACC_intervalle_filtred_t.csv',index=False)
  os.remove('../SortiePython/ACC_intervalle_t.csv')

def filtreBVP():
  filtre= pd.read_csv('../SortiePython/BVP_intervalle_t.csv')
  filtre.to_csv('../SortiePython/BVP_intervalle_filtred_t.csv',index=False)
  os.remove('../SortiePython/BVP_intervalle_t.csv')

def filtreEDA():
  filtre= pd.read_csv('../SortiePython/EDA_intervalle_t.csv')
  filtre.to_csv('../SortiePython/EDA_intervalle_filtred_t.csv',index=False)
  os.remove('../SortiePython/EDA_intervalle_t.csv')
'''
  filtre= pd.read_csv('../Data_E4/CSV_standard/EDA_standard_t0.csv')
  q1=np.quantile(filtre['Electrodermal_activity'],.25)
  q3=np.quantile(filtre['Electrodermal_activity'],.75)
  filtre1=filtre[(filtre['Electrodermal_activity']>=(q1-1.5*(q3-q1))) & (filtre['Electrodermal_activity']<=(q3+1.5*(q3+q1)))]
  filtre1.to_csv('../Data_E4/CSV_standard/EDA_standard_filtre_t0.csv',index=False)
  os.remove('../Data_E4/CSV_standard/EDA_standard_t0.csv')
'''

def filtreHR():
  filtre= pd.read_csv('../SortiePython/HR_intervalle_t.csv')
  filtre.to_csv('../SortiePython/HR_intervalle_filtred_t.csv',index=False)
  os.remove('../SortiePython/HR_intervalle_t.csv')

def filtreIBI():
  filtre= pd.read_csv('../SortiePython/IBI_intervalle_t.csv')
  filtre.to_csv('../SortiePython/IBI_intervalle_filtred_t.csv',index=False)
  os.remove('../SortiePython/IBI_intervalle_t.csv')

def filtreTEMP():
  filtre= pd.read_csv('../SortiePython/TEMP_intervalle_t.csv')
  filtre.to_csv('../SortiePython/TEMP_intervalle_filtred_t.csv',index=False)
  os.remove('../SortiePython/TEMP_intervalle_t.csv')
