#module pour le tracé de graph
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
#importation du module d'animation pour gaze_position.csv
import animationM
#Importation modules EDA
import neurokit2 as nk
import matplotlib.pyplot as plt
#%matplotlib inline



#va nous servir pour stoquer les valeurs post lissage
listexy = []

def show():
  plt.show()

#fonction regroupant les autres fonctions
def graphe(chemin):
  if chemin == 'gaze_positions' :
    grapheGazePosition()
  elif chemin == 'pupil_positions' :
    graphePupilPosition()
  elif chemin == 'blinks' :
    grapheBlink()
  elif chemin == 'fixations' :
    grapheFixations()
  elif 'gaze_positions_on_surface_' in chemin :
    grapheSurface(chemin)
  elif chemin=='ACC':
    grapheACC()
  elif chemin=='BVP':
    grapheBVP()
  elif chemin=='EDA':
    grapheEDA()
  elif chemin=='HR':
    grapheHR()
  elif chemin=='IBI':
    grapheIBI()
  elif chemin=='TEMP':
    grapheTEMP()
  else :
    print('csv non reconnu :'+chemin)

#fonction de représenter plusieurs graphe
#i étant le nombre de graphe à plot, liste étant la liste des graph à plot
def grapheMultiple(i , liste):
  #variable compteur
  count = 0
  ax0=plt.subplot(i, 1, count+1)
  while count < i :
    #on crée un nombre de subplot logique pour que ce soit le plus lisible possible
    if count != 0 :
      plt.subplot(i, 1, count+1, sharex=ax0)
    #plus qu'à plot ce qu'on veut
    graphe(liste[count])
    count += 1

#fonction prenant les 'p' termes autour de chaque point pour lui faire un moyenne glissante
def lissage(Lx,Ly,p):
  #les sorties
  Lxout=[]
  Lyout=[]
  #on ne prendra pas les premiers et derniers termes car inutilisable au vu qu'il faut des termes avant et après le point en cours de traitement
  Lxout = Lx[p: -p]
  for index in range(p, len(Ly)-p):
    #calcul de la moyenne glissante
    average = sum(Ly[index-p : index+p+1]) / (2*p + 1)
    Lyout.append(average)
  return Lxout,Lyout

#fonction permettant de grapher le csv de gaze position avec et sans l'animation
def grapheGazePosition():
  #on va lire le csv voulu
  df = pd.read_csv('../SortiePython/gaze_positions_filtred_t_c_a.csv')
  #puis on trace ce qu'on veut
  plt.plot(df['norm_pos_x'], df['norm_pos_y'],'.')
  #légende des axes
  plt.xlabel('position_x')
  plt.ylabel('position_y')
  animationM.animationGlobale(df['norm_pos_x'],df['norm_pos_y'])

#fonction permetant de grapher l'évolution du diamètre de la pupille en fonction du temps
def graphePupilPosition():
  #lecture du csv
  df = pd.read_csv('../SortiePython/pupil_positions_filtred_t_c.csv')
  #on appelle la fonction de lissage, on peut changer le dernier paramètre pour faire varier si l'on veut lisser plus ou moins la courbe
  listexy = lissage(df['pupil_timestamp'], df['diameter'],30)
  plt.plot(listexy[0],listexy[1])
  #légende des axes
  plt.xlabel('temps (s)')
  plt.ylabel('diamètre pupille (mm)')

#fonction permettant de grapher un graph booléen de si oui ou non l'oeil est fermé
def grapheBlink():
  #lecture du csv
  df = pd.read_csv('../SortiePython/blinks_filtred_t_a.csv')
  f=[]
  tempsf=[]
  eps=0.000000001
  count=0
  for time in df['start_timestamp']:
    f.append(0)
    tempsf.append(time-eps)
    f.append(1)
    tempsf.append(time)
    f.append(1)
    tempsf.append(time+df['duration'][count])
    f.append(0)
    tempsf.append(time+df['duration'][count]+eps)
    count+=1
  plt.plot(tempsf,f)
    


#fonctions permettant de grapher un graph booléen de si oui ou non l'oeil fixe quelque chose
def grapheFixations():
  #on ouvre le csv fixations
  with open('../SortiePython/fixations_filtred_t_c.csv') as c:
    #on le met en lecture
    reader = csv.reader(c, delimiter=',')
    #création de la liste de variable d'état
    f = []
    #création de la liste associé à f pour le temps
    tempsf =[]
    #très petite valeur
    eps = 0.0000001
    #compteur
    count = 0
    for ligne in reader :
      if count != 0 :
        #on change de type, de str à float (c'est le temps du début de la fixations)
        ligne0 = float(ligne[0])
        #on divise par 1000 pour convertir les millisecondes en secondes (c'est le temps de la durée de la fixation)
        ligne1 = float(ligne[1])/1000
        #un peu compliqué à expliquer mais facile à comprendre si l'on fait un dessin de ce qui se passe petit à petit
        #à chaque instant ou il y aura un front (montant ou descendant) on choppe la valeur des temps juste avant/après cet instant
        #à cette valeur de temps on lui associe un état. Ce qui premettra un bon tracé
        f.append(False)
        tempsf.append(ligne0-eps)
        f.append(True)
        tempsf.append(ligne0)
        f.append(True)
        tempsf.append(ligne0+ligne1)
        f.append(False)
        tempsf.append(ligne0+ligne1+eps)
      #incrémentation
      count += 1
    plt.plot(tempsf,f)

#fonction permettant de graph la position du regard sur le référentiel de la surface
def grapheSurface(surface):
  #ouverture du csv
  df = pd.read_csv('../SortiePython/'+surface+'_filtred_t_c_a.csv')
  plt.plot(df['x_scaled'], df['y_scaled'],'.')
  plt.xlabel('x_scaled')
  plt.ylabel('y_scaled')

def grapheACC():
  df = pd.read_csv('../Data_E4/CSV_standard/ACC_standard_t0.csv')
  plt.subplot(3,1,1)
  plt.plot(df['Time_stamp'],df['X'],'--')
  plt.xlabel('Time')
  plt.ylabel('Acc_X')
  plt.subplot(3,1,2)
  plt.plot(df['Time_stamp'],df['Y'],'--')
  plt.xlabel('Time')
  plt.ylabel('Acc_Y')
  plt.subplot(3,1,3)
  print(df)
  plt.plot(df['Time_stamp'],df['Z'],'--')
  plt.xlabel('Time')
  plt.ylabel('Acc_Z')

def grapheBVP():
  df = pd.read_csv('../Data_E4/CSV_standard/BVP_standard_t0.csv')
  plt.plot(df['Time_stamp'],df['Value'],'.')
  plt.xlabel('Time (s)')
  plt.ylabel('Value')

def grapheEDA():
  df= pd.read_csv('../SortiePython/EDA_a.csv')
  eda_signal=df['Electrodermal_activity']
  # Process the raw EDA signal
  eda_signals, info = nk.eda_process(eda_signal, sampling_rate=8)
  #print(signals)  #'EDA_Raw'/'EDA_Clean'/'EDA_Tonic'/'EDA_Phasic'/'SCR_Onsets'/'SCR_Peaks'/'SCR_Height'/'SCR_Amplitude'/'SCR_RiseTime'/'SCR_Recovery'/'SCR_RecoveryTime'
  #print(info)     #'SCR_Onsets'/'SCR_Peaks'/'SCR_Height'/'SCR_Amplitude'/'SCR_RiseTime'/'SCR_Recovery'/'SCR_RecoveryTime'
  #plot=plt.plot(df["Time_stamp"],signals["EDA_Raw"])
  # Plot EDA signal
  #plot = nk.eda_plot(signals)
  sampling_rate=8
  peaks = np.where(eda_signals["SCR_Peaks"] == 1)[0]
  onsets = np.where(eda_signals["SCR_Onsets"] == 1)[0]
  half_recovery = np.where(eda_signals["SCR_Recovery"] == 1)[0]

  fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, ncols=1, sharex=True)

  # Determine unit of x-axis.
  last_ax = fig.get_axes()[-1]
  if sampling_rate is not None:
    last_ax.set_xlabel("Seconds")
    x_axis = np.linspace(0, len(eda_signals) / sampling_rate, len(eda_signals))
  else:
    last_ax.set_xlabel("Samples")
    x_axis = np.arange(0, len(eda_signals))

  plt.subplots_adjust(hspace=0.2)

  # Plot cleaned and raw respiration as well as peaks and troughs.
  ax0.set_title("Raw and Cleaned Signal")
  fig.suptitle("Electrodermal Activity (EDA)", fontweight="bold")
  ax0.plot(x_axis, eda_signals["EDA_Raw"], color="#B0BEC5", label="Raw", zorder=1)
  ax0.plot(x_axis, eda_signals["EDA_Clean"], color="#9C27B0", label="Cleaned", linewidth=1.5, zorder=1)
  ax0.legend(loc="upper right")

  # Plot skin cnoductance response.
  ax1.set_title("Skin Conductance Response (SCR)")

  # Plot Phasic.
  ax1.plot(x_axis, eda_signals["EDA_Phasic"], color="#E91E63", label="Phasic Component", linewidth=1.5, zorder=1)

  '''# Mark segments.
        risetime_coord, amplitude_coord, halfr_coord = _eda_plot_dashedsegments(
          eda_signals, ax1, x_axis, onsets, peaks, half_recovery
        )
      
        risetime = matplotlib.collections.LineCollection(risetime_coord, colors="#FFA726", linewidths=1, linestyle="dashed")
        ax1.add_collection(risetime)
      
        amplitude = matplotlib.collections.LineCollection(
          amplitude_coord, colors="#1976D2", linewidths=1, linestyle="solid"
        )
        ax1.add_collection(amplitude)
      
        halfr = matplotlib.collections.LineCollection(halfr_coord, colors="#FDD835", linewidths=1, linestyle="dashed")
        ax1.add_collection(halfr)'''
  ax1.legend(loc="upper right")

  # Plot Tonic.
  ax2.set_title("Skin Conductance Level (SCL)")
  ax2.plot(x_axis, eda_signals["EDA_Tonic"], color="#673AB7", label="Tonic Component", linewidth=1.5)
  ax2.legend(loc="upper right")
  plt.show()


def grapheHR():
  df = pd.read_csv('../Data_E4/CSV_standard/HR_standard_t0.csv')
  df=df[df["Time_stamp"]>=0] 
  plt.plot(df['Time_stamp'],df['Av_heart_rate'],'.')
  plt.xlabel('Time (s)')
  plt.ylabel('Heart_rate (bpm)')

def grapheIBI():
  df = pd.read_csv('../SortiePython/IBI_intervalle_filtred_t.csv')
  '''g=[0]
  time_g=[0]
  eps=0.00000000001
  qrsTime=0.080
  for line in range(len(df['Time_stamp'])):
    time_s=df['Time_stamp'][line]
    duration=df['IBI'][line]
    g.append(0)
    time_g.append(time_s-qrsTime-eps)
    g.append(1)
    time_g.append(time_s-qrsTime)
    g.append(1)
    time_g.append(time_s-eps)
    g.append(0)
    time_g.append(time_s)
    g.append(0)
    time_g.append(time_s+duration)
  plt.plot(time_g,g)'''
  plt.plot(df['Time_stamp'],df['IBI'],drawstyle='steps')
  # (drawstyle='steps')?
  plt.xlabel('Time (s)')
  plt.ylabel('IBI interval (ms)')
  
def grapheTEMP():
  df = pd.read_csv('../Data_E4/CSV_standard/TEMP_standard_t0.csv')
  df=df[df["Time_stamp"]>=0]  
  plt.plot(df['Time_stamp'],df['temperature'],'.')
  plt.xlabel('Time (s)')
  plt.ylabel('Temp (C)')
