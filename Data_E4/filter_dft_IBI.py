#General_modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

def filter_dft_IBI():
	df = pd.read_csv('CSV_standard/IBI_standard_t0.csv')
	dt=0.1
	x= df['IBI']
	t= df['Time_stamp']
	print('oui')
	plt.subplot(211)
	plt.plot(t,x)


	a= np.fft.ifftshift(x)
	A=np.fft.fft(a)
	X=dt*np.fft.fftshift(A)

	n=t.size
	freq = np.fft.fftfreq(n, d=dt)
	f=np.fft.fftshift(freq)

	plt.subplot(212)
	x=np.append(f,f[0])
	z=np.append(X,X[0])
	X=np.array([x,x])

	y0 = np.zeros(len(x))
	y=np.abs(z)
	Y=np.array([y0,y])

	Z=np.array([z,z])
	C=np.angle(Z)

	plt.plot(x,y,'k')