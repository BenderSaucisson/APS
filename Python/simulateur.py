import getTime
import pandas

def erreurTemps():
  tempsSec = getTime.get_start_time_simulateur_s()
  #incrémentation de deux sur le temps en UNIX car le temps que nous donne le log n'est pas fidèle au csv
  tempsSec += 2
  #décrémentation de 67 car l'heure du pc sur lequel on a fait les tests n'était pas exactement à l'heure
  tempsSec -= 67
  return(tempsSec)

def ajustement():
