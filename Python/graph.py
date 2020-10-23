#module pour le tracé de graph
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
#importation du module d'animation pour gaze_position.csv
import animationM

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
  else :
    print('csv non reconnu')

#fonction de représenter plusieurs graphe
#i étant le nombre de graphe à plot, liste étant la liste des graph à plot
def grapheMultiple(i , liste):
  #variable compteur
  count = 0
  while count < i :
    #on crée un nombre de subplot logique pour que ce soit le plus lisible possible
    plt.subplot(i, 1, count+1)
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
  #on ouvre le csv fixations
  with open('../SortiePython/blinks_filtred_t_a.csv') as c:
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
        ligne1 = float(ligne[1])
        #un peu compliqué à expliquer mais facile à comprendre si l'on fait un dessin de ce qui se passe petit à petit
        #à chaque instant ou il y aura un front (montant ou descendant) on choppe la valeur des temps juste avant/après cet instant
        #à cette valeur de temps on lui associe un état. Ce qui premettra un bon tracé
        f.append(0)
        tempsf.append(ligne0-eps)
        f.append(1)
        tempsf.append(ligne0)
        f.append(1)
        tempsf.append(ligne0+ligne1)
        f.append(0)
        tempsf.append(ligne0+ligne1+eps)
      #incrémentation
      count += 1
    plt.plot(tempsf, f)

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

