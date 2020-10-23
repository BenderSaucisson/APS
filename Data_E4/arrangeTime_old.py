import csv

def arrangeTime(chemin):
  with open('CSV_standard/'+chemin+'_standard.csv', 'w', newline='') as output:
    writer = csv.writer(output, delimiter=',')
    if chemin=='TEMP':
      legend='temperature (deg C)'
    elif chemin=='EDA':
      legend='Electrodemal_activity (microsiemens)'
    elif chemin=='HR':
       legend='Av_heart_rate'
    else :
        legend='Value'
    line_list=[]
    countLine = 0
    with open('CSV_ori/'+chemin+'.csv') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      if chemin=='ACC':
        for line in reader:
          if countLine==0:
            timeStart=float(line[0])
            timeIt=timeStart
            line[0]='Time_stamp'
            line[1]='X'
            line[2]='Y'
            line.append('Z')
            line_list.append(line)
          elif countLine==1:
            freq=float(line[0])
            period=1/freq
          else :
            line.append(line[2])
            line[2]=line[1]
            line[1]=line[0]
            line[0]=timeIt
            timeIt=timeIt+period
            line_list.append(line)
          countLine=countLine+1
      elif chemin=='IBI':
        for line in reader:
          if countLine==0:
            timeStart=float(line[0])
            line[0]='Time_stamp'
            line_list.append(line)
          else :
            line[0]=timeStart+float(line[0])
            line_list.append(line)
          countLine=countLine+1
      else:
        for line in reader:
          if countLine==0:
            timeStart=float(line[0])
            timeIt=timeStart
            line[0]='Time_stamp'
            line.append(legend)
            line_list.append(line)
          elif countLine==1:
            freq=float(line[0])
            period=1/freq
          else :
            line.append(line[0])
            line[0]=timeIt
            timeIt=timeIt+period
            line_list.append(line)
          countLine=countLine+1
      writer.writerows(line_list)






