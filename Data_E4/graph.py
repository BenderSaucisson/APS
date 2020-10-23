#General_modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv




def show():
	plt.show()



def plotCmd():
	print("Information Graphique Possible :\n[ACC] : Accelèrometre\n[BVP] : Pression arterielle\n[EDA] : Conductance de la peau (sueur)\n[HR] : Rythme cardiaque\n[IBI] : Intervalle de pulsation\n[TEMP] : Température du capteur")
	print("Combien de graphique voulez vous afficher :")
 	#combien de graphe l'utilisateur veut visualiser
	i = int(input())
	#compteur
	count = 0
 	#liste pour savoir quel graphe il faut plot
	graph_list = []
	while count < i :

 		print("Quel graphique voulez vous afficher :")
 		name=input()
		#on utilise seulement la première lettre de chaque graphique pour que ce soit moins embêtant pour l'utilisateur
 		if name=='ACC':
 			graph_list.append('ACC')
 		elif name=='BVP':
 			graph_list.append('BVP')
 		elif name=='EDA':
 			graph_list.append('EDA')
 		elif name=='HR':
 			graph_list.append('HR')
 		elif name=='IBI':
 			graph_list.append('IBI')
 		elif name=='TEMP':
 			graph_list.append('TEMP')
 		else:
 			print('Mauvaise saisie : '+ name)
 			count=count-1
 		count=count+1
	multipleGraph(graph_list)
    	#on plot tout les graph simultanément sur différent subplot



def multipleGraph(graph_list):
	ok=0
	count=0
	i=len(graph_list)
	ok=1
	while count < i :
		plt.subplot(i, 1, count+1)
		graph(graph_list[count])
		count += 1

def graph(name):
	if name=='ACC':
		graphACC()
	elif name=='BVP':
		graphBVP()
	elif name=='EDA':
		graphEDA()
	elif name=='HR':
		graphHR()
	elif name=='IBI':
		graphIBI()
	elif name=='TEMP':
		graphTEMP()
	else :
		print('unknown csv : '+ name)

def graphACC():
	df = pd.read_csv('CSV_standard/ACC_standard_t0.csv')
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

def graphBVP():
	df = pd.read_csv('CSV_standard/BVP_standard_t0.csv')
	plt.plot(df['Time_stamp'],df['Value'],'.')
	plt.xlabel('Time (s)')
	plt.ylabel('Value')

def graphEDA():
	df = pd.read_csv('CSV_standard/EDA_standard_t0.csv')
	plt.plot(df['Time_stamp'],df['Electrodemal_activity (microsiemens)'],'.')
	plt.xlabel('Time (s)')
	plt.ylabel('Cond (microsiemens)')

def graphHR():
	df = pd.read_csv('CSV_standard/HR_standard_t0.csv')
	plt.plot(df['Time_stamp'],df['Av_heart_rate'],'.')
	plt.xlabel('Time (s)')
	plt.ylabel('Heart_rate (bpm)')


def graphIBI():
	df = pd.read_csv('CSV_standard/IBI_standard_t0.csv')
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
	#	(drawstyle='steps')?
	plt.xlabel('Time (s)')
	plt.ylabel('IBI interval (ms)')






def graphTEMP():
	df = pd.read_csv('CSV_standard/TEMP_standard_t0.csv')
	plt.plot(df['Time_stamp'],df['temperature (deg C)'],'.')
	plt.xlabel('Time (s)')
	plt.ylabel('Temp (C)')
