#General_modules
import csv
import getTime


#Fonction de création de csv standardisé en temps Unix
def arrangeTime(ID,name):
  #On crée le csv voulu
  with open('../Data_E4/CSV_standard/'+name+'_standard.csv', 'w', newline='') as output:
    writer = csv.writer(output, delimiter=',')
    legend=['Time_stamp']
    #Liste qui va stocker le csv à créer
    output_list=[]
    countLine = 0
    #On crée la légende en fonction du fichier
    if name=='TEMP':
      legend.append('temperature')
    elif name=='EDA':
      legend.append('Electrodermal_activity')
    elif name=='BVP':
      legend.append('Value')
    elif name=='HR':
      legend.append('Av_heart_rate')
    elif name=='ACC':
      legend.append('X')
      legend.append('Y')
      legend.append('Z')
    elif name=='IBI':
      legend.append('IBI')
    else :
      print('csv non reconnu')
      legend.append('Value')
    #On ouvre le csv à lire
    with open('../Data_E4/CSV_ori/cache_ID'+ID+'/'+name+'.csv') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for line in reader:
        #Paramétrage de la 1ere ligne (légendes)
        if countLine==0:
          timeStart=float(line[0])
          timeIt=timeStart
          for i in range(len(line)):
            line[i]=legend[i]
          if name !='IBI':
            line.append(legend[len(line)])
          output_list.append(line)
        #IBI n'a pas de période sur son capteur
        elif name=='IBI' :
            line[0]=timeStart+float(line[0])
            output_list.append(line)
        #On récupère la période de prise de donnée des capteurs pour le Time_stamp
        elif countLine==1 :
          freq=float(line[0])
          period=1/freq
        else :
          #On décale tout à droite pour faire de la place pour le Time_stamp
          line.append(line[len(line)-1])
          for i in range(len(line)):
            line[len(line)-1-i]=line[len(line)-2-i]
          #On ajoute le Time_stamp
          line[0]=timeIt
          timeIt=timeIt+period
          output_list.append(line)
        countLine=countLine+1
      writer.writerows(output_list)

#Fonction de création de csv standardisé en temps depuis le début de la simulation
def arrangeTime_t0(ID,name):
  #On créer le csv voulu
  with open('../Data_E4/CSV_standard/'+name+'_standard_t0.csv','w',newline='') as output:
    writer =csv.writer(output,delimiter=',')
    output_list=[]
    countLine=0
    #On prend le temps de début de la simulation
    timeStart=getTime.get_start_time_simulateur_s(ID)

    if name!='IBI':
      #On ouvre le csv à lire
      with open('../Data_E4/CSV_standard/'+name+'_standard.csv') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        for line in reader :
          if countLine==0:
            output_list.append(line)
          elif countLine==1:
            line[0]=float(line[0])-timeStart
            output_list.append(line)
          else :
            line[0]=float(line[0])-timeStart
            output_list.append(line)
          countLine=countLine+1
        writer.writerows(output_list)

    else:
      #On ouvre le csv à lire
      with open('../Data_E4/CSV_ori/cache_ID'+ID+'/'+name+'.csv') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        for line in reader:
          #On écrit la légende et on récupère le temps du début de l'enregistrement de l'E4
          if countLine==0:
            timeStart_E4=float(line[0])
            line[0]='Time_stamp'
            line[1]='IBI'
            output_list.append(line)
          #On écrit le temps écoulé depuis le début de l'enregistrement du simulateur
          else:
            line[0]=float(line[0])+timeStart_E4-timeStart
            output_list.append(line)
          countLine=countLine+1
        writer.writerows(output_list)

