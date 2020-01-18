import os
import numpy as np
import matplotlib.pyplot as plt
from json import loads
from datetime import datetime, timedelta
import csv
import dateutil.parser as dp

dev_id = "keypad"

somedate = datetime

Datarates = ["SF12BW125", "SF11BW125", "SF10BW125","SF9BW125", "SF8BW125", "SF7BW125"]
Timetable = [40,30,46,26,43,9,1,11,22,32,38,46]
places = ["Student Hytta", "Graakallen", "Utkikk-parkering", "Utsikten", "Stiftsgaarden", "Sentralstasjon"]



def LogToCsv(dev_id):
    for filename in os.listdir('Logs '+dev_id):
        # Returns a list wich contains all metadata from given gateway at a given date.
        i=0
        try:
            Log = open('Logs '+dev_id+"/"+filename,'r')
            resultFile = open(filename+".csv",'w')
            wr = csv.writer(resultFile)
            for line in Log:
                #Load each line from Json:
                temp2 = loads(line)
                DR = Datarates.index(temp2[0])
                measrtime =  dp.parse(str(temp2[3]))
                temp1 = [[DR, int(measrtime.timestamp()), temp2[5], temp2[6]] ]
                wr.writerows(temp1)
            Log.close()


        except FileNotFoundError:
            print(filename+" File not found...")
    


LogToCsv(dev_id)
