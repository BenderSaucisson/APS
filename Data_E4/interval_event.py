#general modules
import csv
import pandas as pd



def interval_data(name,timers):
  with open('CSV_intervals/'+name+'_events.csv','w',newline='') as output:
    writer =csv.writer(output,delimiter=',')
    output_list=[]
    countLine=0

    df = pd.read_csv('CSV_standard/'+name+'_standard_t0.csv')
    events=events_t(df['Time_stamp'],sorted(timers))
    event=0
    with open('CSV_standard/'+name+'_standard_t0.csv') as csvfile:
    	reader=csv.reader(csvfile,delimiter=',')
    	for e in events:
    		event+=1
    		output_event=['Event_'+str(event)]
    		for line in reader:
    			if countLine>=e[0] and countLine<e[1]:
    				#print('non')
    				output_event.append(line[1])
    			else :
    				#print('oui')
    				pass
    			countLine+=1
    	   output_list.append(output_event)
    writer.writerows(output_list)


def events_t(t_list,timers):
	events_t=[]
	event_start=1
	for t in timers:
		event_end_index=t_list[t_list==t].index
		event_end=event_end_index[0]
		events_t.append([event_start,event_end])
		event_start=event_end
	events_t.append([event_start,len(t_list)-1])
	print(events_t)
	return events_t