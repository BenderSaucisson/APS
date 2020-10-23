import matplotlib.animation as animation
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#fonction permettant d'animer une courbe, peut être utile pour le déplacement du regard avec le gaze_positions.csv
def animationGlobale(x,y):
  # Création de la figure et de l'axe

  fig, ax = plt.subplots()

  # Création de la ligne qui sera mise à jour au fur et à mesure
  line, = ax.plot([],[], color='blue')
  point, = ax.plot([], [], ls="none", marker="o")

  #Gestion des limites de la fenêtre
  ax.set_xlim([1.05*np.min(x), 1.05*np.max(x)])
  ax.set_ylim([1.05*np.min(y), 1.05*np.max(y)])

  print(type(line))
  print(type(point))
  # Création de la function qui sera appelée à "chaque nouvelle image"
  def animate(k):
    i = min(k, x.size)
    line.set_data(x[:i], y[:i])
    point.set_data(x[i], y[i])
    return line, point

  # Génération de l'animation, frames précise les arguments numérique reçus par func (ici animate), 
  # interval est la durée d'une image en ms, blit gère la mise à jour
  ani = animation.FuncAnimation(fig=fig, func=animate, frames=range(x.size), interval=0.01, blit=True)

  # Création du fichier, dpi : résolution, fps : images par secondes

  #ani.save(filename="courbe.mp4", dpi =80, fps=200)

  plt.show()

