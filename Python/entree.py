import graph
from pathlib import Path
import os


def checkFileExistance(name):
  filePath = "../EyeTracker/exports/"+str(name)
  try:
    with open(filePath, 'r') as f:
      return True
  except FileNotFoundError as e:
    os.system("clear") 
    print ("Mauvais dossier :" + str(e))
    variableFichierExport()
  except IOError as e:
    return False

def checkNombreSurfaceInt(value):
  try:
      nombreSurfaces = int(value)
      return nombreSurfaces
  except ValueError as e:
    os.system("clear") 
    print ("Nombre invalide :" + str(e))
    return variableNombreSurface()
  except IOError as e:
    return False

def checkFileSurface(name):
  filePath = "../EyeTracker/exports/000/surfaces/gaze_positions_on_surface_"+str(name)+".csv"
  try:
    with open(filePath, 'r') as f:
      return True
  except FileNotFoundError as e:
    os.system("clear") 
    print ("Mauvais nom de surface :" + str(e))
    return False
  except IOError as e:
    return False

def variableFichierExport():
  print("Votre nom de fichier d'export :")
  #on attend que l'utilisateur rentre la donnée du nom de dossier de l'export
  nomExport = input()
  checkFileExistance(nomExport)
  return (nomExport)

def variableNombreSurface():
  print("Combien de surfaces utilisées avez vous differencié avec Pupil Player :")
  #on attend que l'uilisateur rentre la donnée du nombre de surface utilisées
  nombreSurfaces = input()
  nombre = checkNombreSurfaceInt(nombreSurfaces)
  return (nombre)

def variableFichierSurface():
  #on attend que l'utilisateur rentre la donnée du nom de dossier de l'export
  print("Comment s'appelle vos surfaces :")
  nomSurface = input()
  if checkFileSurface(nomSurface) :
    return (nomSurface) 

#fonction récupérant des informations dans la console rentré par l'utilisateur, où se trouve son dossier d'enregistrement et le nombre/ nom des surfaces utilisées
def variableCmd() :
  nomExport = variableFichierExport()
  nombreSurfaces = variableNombreSurface()
  #compteur
  i = 0
  #liste stockant le noms des surfaces
  surfaces = []
  #on récupère le nom de toutes les surfaces utilisées
  while i < nombreSurfaces :
    #on rentre la donnée dans la liste surfaces
    entree = variableFichierSurface()
    print(entree)
    surfaces.append(entree)
    print(surfaces)
    i = i+1
  #création d'une liste avec les noms des différents csv à utiliser, les csv sont présent dans le dossier 'exports'
  sortie_e_t = ['gaze_positions','blinks','pupil_positions','fixations']
  sortie_e4 = ['ACC','BVP','EDA','HR','IBI','TEMP']
  i = 0
  while i < nombreSurfaces :
    sortie_e_t.append('gaze_positions_on_surface_'+ surfaces[i])
    i += 1
  return(nomExport, sortie_e_t,sortie_e4)

def variableNombreIntervales():
  print("Combien d'intervalles voulez vous examiner : ")
  nombreIntervalle = int(input())
  i = 0
  listeDebut = []
  listeFin = []
  while i < nombreIntervalle:
    print("Début de l'intervalle n°", i+1," en seconde :")
    listeDebut.append(int(input()))
    print("Fin de l'intervalle n°", i+1," en seconde :")
    listeFin.append(int(input()))
    i += 1
  return(nombreIntervalle, listeDebut, listeFin)



#fonction récupérant l'information de ce que veux grapher l'utilisateur
def plotCmd():
  #gros pavé explicatif
  print("Information Graphique Possible :\n[g] : Gaze_position : position du regard\n[p] : Pupil_position : diametre de la pupille\n[b] : Blinks : Clignement des yeux\n[f] : Fixations : Fixation du regard\n[Nom_Surface] : Surface : Position du regard par rapport au référentiel de la surface")
  print("Combien de graphique voulez vous afficher :")
  #combien de graphe l'utilisateur veut visualiser
  i = int(input())
  #compteur
  count = 0
  #liste pour savoir quel graphe il faut plot
  liste = []
  while count < i :
    print("Quel graphique voulez vous afficher :")
    entree = input()
    #on utilise seulement la première lettre de chaque graphique pour que ce soit moins embêtant à écrire dans la console pour l'utilisateur
    if entree == 'g' :
      liste.append('gaze_positions')
    elif entree == 'p' :
      liste.append('pupil_positions')
    elif entree == 'b' :
      liste.append('blinks')
    elif entree == 'f':
      liste.append('fixations')
    else :
      liste.append('gaze_positions_on_surface_'+entree)
    count += 1
  #on plot tout les graph simultanément sur différent subplot
  graph.grapheMultiple(len(liste),liste)
  return liste

