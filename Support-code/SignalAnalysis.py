import numpy as np
import matplotlib.pyplot as plt
from json import loads
from datetime import datetime, timedelta
import dateutil.parser


dev_id = "keypad"
date = "13.11.2018"
gateway = "trt-olav-loragw01"
 
somedate = datetime

Datarates = ["SF12BW125", "SF11BW125", "SF10BW125","SF9BW125", "SF8BW125", "SF7BW125"]





def binary_search(arr, val, start, end): 
    # we need to distinugish whether we should insert 
    # before or after the left boundary. 
    # imagine [0] is the last step of the binary search 
    # and we need to decide where to insert -1 
    if start == end: 
        if arr[start] > val: 
            return start 
        else: 
            return start+1
  
    # this occurs if we are moving beyond left's boundary 
    # meaning the left boundary is the least position to 
    # find a number greater than val 
    if start > end: 
        return start 
  
    mid = int((start+end)/2)
    if arr[mid] < val: 
        return binary_search(arr, val, mid+1, end) 
    elif arr[mid] > val: 
        return binary_search(arr, val, start, mid-1) 
    else: 
        return mid 
  
def insertion_sort(arr, arr2, arr3): 
    for i in range(len(arr)): 
        val = arr[i] 
        val2 = arr2[i]
        val3 = arr3[i]
        j = binary_search(arr, val, 0, i-1) 
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
        arr2 = arr2[:j] + [val2] + arr2[j:i] + arr2[i+1:]
        arr3 = arr3[:j] + [val3] + arr3[j:i] + arr3[i+1:]   
    return arr, arr2, arr3


def MetadataListFromLog(dev_id, gateway, date):
    # Returns a list wich contains all metadata from given gateway at a given date.
    temp = []
    try:
        Log = open('Logs '+dev_id+"/"+gateway+" "+date+".txt",'r')
        for line in Log:
            #Load each line from Json:
            temp.append(loads(line))
        Log.close()
        return temp
    except FileNotFoundError:
        print("File not found...")
        return temp


def MakeArrays(metadatalist):
    # Takes in metadatalist, returns:
    DRarray = []
    # Time array is filled with datetime objects.
    timearray = []
    rssiarray = []
    snrarray = []
    for i in range(len(metadatalist)):
        for n in range(len(Datarates)):
            if Datarates[n] == metadatalist[i][0]:
                DRarray.append(n)
        timearray.append(dateutil.parser.parse(metadatalist[i][3]))
        rssiarray.append(metadatalist[i][5])
        snrarray.append(metadatalist[i][6])
    return DRarray, timearray, rssiarray, snrarray

def GetMean(IntegerList):
    temp = 0
    for i in range(len(IntegerList)):
        temp = temp + IntegerList[i]
    try:
        return float(temp)/len(IntegerList)
    except ZeroDivisionError:
        return temp


def PlotRSSI_SNR(x, y, z, xlabel, ylabel, leg):
    temp = 0
    numPlots = 0
    for i in range(len(x)):
        # If the timedifference is bigger than 2 minutes
        if x[i]-x[i-1] > timedelta(0,30,0):
            if len(x[temp:i-1])>4:
                numPlots = numPlots + 1
                mean = GetMean(y[temp:i-1])
                mean = [mean]*len(y[temp:i-1])
                pltx = np.array(x[temp:i-1])
                plty = np.array(y[temp:i-1])
                pltz = np.array(z[temp:i-1])
                pltmean = np.array(mean)
                temp = i
                plt.figure(numPlots)
                plt.plot(pltx,plty,'bo', pltx, pltmean, 'r')
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                plt.legend([leg,'','mean'])
                for i,j in zip(pltx,plty):
                    plt.annotate(str(j),xy=(i,j))
            
            
        else:
            pass
    plt.show()
    
def PlotMeanDR(x, y, DR):
    temp = 0
    numPlots = 0
    DR_tmp, x_temp, y_temp = insertion_sort(DR, x, y)
    for i in range(len(DR_tmp)):
        # If the timedifference is bigger than 2 minutes
        if x[i]-x[i-1] > timedelta(0,600,0):
            temp = i
            numPlots = numPlots + 1
            for i in range(4):
                n = 0
                while DR_tmp[n] == i:
                    n=n+1
                mean = GetMean(y[temp:n])
                mean = [mean]*len(y[temp:n])
                pltmean = np.array(mean)
                pltx = np.array(x[temp:n])
                plty = np.array(y[temp:n])
                plt.figure(numPlots)
                plt.plot(pltx,plty,'bo', pltx, pltmean, 'r')
    plt.show()


something = MetadataListFromLog("keypad", gateway , date)

yourdate = dateutil.parser.parse(something[0][3])

a,b,c,d = MakeArrays(something)
some = b[2]-b[1]
some1 = b[3]-b[2]
#PlotRSSI_SNR(b,c,a, "Time", "RSSI dBm", "hello")

PlotMeanDR(b, c, a)
#meta Format ["trt-vm-loragw01", True, 1040756148, "2018-11-08T11:39:10Z", 0, -120, -8.75, 1, 63.42883, 10.385698, 20]



meta = ["trt-vm-loragw01", True, 1040756148, "2018-11-08T11:39:10Z", 0, -120, -8.75, 1, 63.42883, 10.385698, 20]
