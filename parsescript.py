import matplotlib.pyplot as plt

import csv
from statistics import mean
from itertools import zip_longest
import pandas as pd
import numpy as np
from numpy import genfromtxt

#The purpose of this analysis is to compare the completion times and accuracies of 5 participants clicking 6 different targets. Each participant does 10 trials of 6
#tasks and their times and accuracies for each task is recorded. There are two differnt interaction techniques tested and each participant does the experiment
#for both techniques, yielding 10 trials (of 6 tasks) or 60 tasks per participant and 300 total data entries per technique. There are 50 trial files per technique.
# This data was collected from my COSC 341 class where I conducted this experiment to compare the statistical differences between the two techniques. 
#Expanding Targets: https://drive.google.com/drive/folders/1K6Z-y_Ezpw867EhPz68OYXb3zOlDRD25?usp=sharing
#Order BY Frequency: https://drive.google.com/drive/folders/1xm9GQHjsv6jAZON4f9e6R1_hlOuswZ6v?usp=sharing


#Expanding Targets
with open("ParsedExpandingTargets.csv", "w") as csvfile:
    out = csv.writer(csvfile)
    for i in range(0,50):
        with open('./expanding_targets/ExpandingTargets'+str(i)+'.csv', 'r') as csv_file:
            infile = csv.reader(csv_file)
            for line in infile:
                if (line[1] != line[2]):
                    line.append(0)
                else:
                    line.append(1)
                out.writerow(line)
            
#Order By Frequency
with open("ParsedOrderFrequency.csv", "w", newline='') as csvfile2:
    out2 = csv.writer(csvfile2)
    for i in range(0,50):
        with open('./order_frequency/OrderFrequency'+str(i)+'.csv', 'r') as csv_file2:
            infile2 = csv.reader(csv_file2)
            for line in infile2:
                if (line[1] != line[2]):
                    line.append(0)
                else:
                    line.append(1)
                out2.writerow(line)

of = open("ParsedOrderFrequency.csv", "r")
et = open("ParsedExpandingTargets.csv", "r")
oftime = list()
ettime = list()
infile4 = csv.reader(of)
infile5 = csv.reader(et)
for line in infile4:
    oftime.append(int(line[3]))
for line in infile5:
    ettime.append(int(line[3]))
oftime2 = np.array(oftime)
steps = 60
oftime3 = list()
for i in range(0, len(oftime2), steps):
    avg = np.average(oftime2[i:i+steps])
    oftime3.append(avg)
ettime2 = np.array(ettime)
steps = 60
ettime3 = list()
for i in range(0, len(ettime2), steps):
    avg = np.average(ettime2[i:i+steps])
    ettime3.append(avg)
participant = [1,2,3,4,5]
d = [participant,oftime3, ettime3]
export_data = zip_longest(*d, fillvalue = '')
with open('AverageTimes.csv', 'w', encoding="ISO-8859-1", newline='') as csvfile3:
    wr = csv.writer(csvfile3)
    wr.writerow(("OrderFrequency", "ExpandingTargets"))
    wr.writerows(export_data)
of.close()
et.close()

of = open("ParsedOrderFrequency.csv", "r")
et = open("ParsedExpandingTargets.csv", "r")
ofacc = list()
etacc = list()
infile4 = csv.reader(of)
infile5 = csv.reader(et)
for line in infile4:
    ofacc.append(int(line[4]))
for line in infile5:
    etacc.append(int(line[4]))
ofacc2 = np.array(ofacc)
steps = 60
ofacc3 = list()
for i in range(0, len(ofacc2), steps):
    avg = np.average(ofacc2[i:i+steps])
    ofacc3.append(avg*100)
etacc2 = np.array(etacc)
steps = 60
etacc3 = list()
for i in range(0, len(etacc2), steps):
    avg = np.average(etacc2[i:i+steps])
    etacc3.append(avg*100)
d = [ofacc3, etacc3]
exportdata = zip_longest(*d, fillvalue = '')
with open('AverageAccuracy.csv', 'w', encoding="ISO-8859-1", newline='') as csvfile4:
    wr = csv.writer(csvfile4)
    wr.writerow(("OrderFrequency", "ExpandingTargets"))
    wr.writerows(exportdata)


# acc = genfromtxt('AverageAccuracy.csv', delimiter=',')
# time = genfromtxt('AverageTimes.csv', delimiter=',')
df = pd.read_csv("AverageAccuracy.csv")
df2 = pd.read_csv("AverageTimes.csv")

plt.plot(df)
plt.show()
plt.plot(df2)
plt.show()
