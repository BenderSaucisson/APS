#General_modules
import csv

def arrangeTime(name):
  with open('CSV_standard/'+name+'_standard.csv', 'w', newline='') as output:
    writer = csv.writer(output, delimiter=',')
    legend=['Time_stamp']
    output_list=[]
    countLine = 0
    if name=='TEMP':
      legend.append('temperature (deg C)')
    elif name=='EDA':
      legend.append('Electrodemal_activity (microsiemens)')
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
        legend.append('Value')

    with open('CSV_ori/'+name+'.csv') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for line in reader:
        if countLine==0:
          timeStart=float(line[0])
          timeIt=timeStart
          for i in range(len(line)):
            line[i]=legend[i]
          if name !='IBI':
            line.append(legend[len(line)])
          output_list.append(line)
        elif name=='IBI' :
            line[0]=timeStart+float(line[0])
            output_list.append(line)
        elif countLine==1 :
          freq=float(line[0])
          period=1/freq
        else :
          line.append(line[len(line)-1])
          for i in range(len(line)):
            line[len(line)-1-i]=line[len(line)-2-i]
          line[0]=timeIt
          timeIt=timeIt+period
          output_list.append(line)
        countLine=countLine+1
      writer.writerows(output_list)


def arrangeTime_t0(name):
  with open('CSV_standard/'+name+'_standard_t0.csv','w',newline='') as output:
    writer =csv.writer(output,delimiter=',')
    output_list=[]
    countLine=0


    if name!='IBI':
      with open('CSV_standard/'+name+'_standard.csv') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        for line in reader :
          if countLine==0:
            output_list.append(line)
          elif countLine==1:
            timeStart=float(line[0])
            line[0]=float(line[0])-timeStart
            output_list.append(line)
          else :
            line[0]=float(line[0])-timeStart
            output_list.append(line)
          countLine=countLine+1
        writer.writerows(output_list)

    else:
      with open('CSV_ori/'+name+'.csv') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        for line in reader:
          if countLine==0:
            line[0]='Time_stamp'
            line[1]='IBI'
            line.append('Error?')
            output_list.append(line)
          elif countLine==1:
            timeFinish=float(line[0])+float(line[1])
            output_list.append(line)
          else:
            if timeFinish>=float(line[0]):
              line.append(1)
            else :
              line.append(0)
            output_list.append(line)
            timeFinish=float(line[0])+float(line[1])
          countLine=countLine+1
        writer.writerows(output_list)
