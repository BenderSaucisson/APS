#General_modules
#import csv

#My_modules
import arrangeTime
import graph
import filter_dft_IBI
#import interval_event

#ACC/BVP/EDA/HR/IBI/TEMP/(tags)
files = ['ACC','BVP','EDA','HR','IBI','TEMP']
events=[13,20,25]
for name in files :
	arrangeTime.arrangeTime(name)
	arrangeTime.arrangeTime_t0(name)
	#interval_event.interval_data(name,events)
	for i in range(5):
		print(i)


filter_dft_IBI.filter_dft_IBI()
graph.plotCmd()

graph.show()