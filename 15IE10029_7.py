
# 15IE10029
# Stuti Modi
# Assignment 7

import csv
import math
import random

filename = 'data7.csv'
lines = csv.reader(open(filename, "r"))
trainingSet = list(lines)
for i in range(len(trainingSet)):
    trainingSet[i] = [float(x) for x in trainingSet[i]]

#print (trainingSet)
cm1 =[] #cm1 and cm2 are random centroids
cm2 =[]
k1 = random.randint(0,20)
k2 = random.randint(0,20)
for i in range(len(trainingSet[k1])):
    cm1.append(trainingSet[1][i]) #can use k1 in place of 10
    cm2.append(trainingSet[11][i]) #can use k2 in place of 11
# k1 and k2 are for random data points to be chosen however do not give consistent results for 10 iterations of the code hence has been tested with specific numbers for consistent results

for n in range(len(trainingSet)):
    trainingSet[n].append(0) #addtional column for label
#print (cm1, cm2)


for i in range (10): #Results for iterations are not consistent if cm1 and cm2 are randomly generated for only 10 iterations
    for n in range(len(trainingSet)):    
        dist1,dist2 = 0.0, 0.0 
        for x in range(len(cm1)):
            dist1 = float (dist1 + (cm1[x]-trainingSet[n][x])*(cm1[x]-trainingSet[n][x])) 
        dist1 = math.sqrt(dist1)
        
        for x in range(len(cm2)):
            dist2 = float (dist2 + (cm2[x]-trainingSet[n][x])*(cm2[x]-trainingSet[n][x])) 
        dist2 = math.sqrt(dist2)
        #print(dist1, dist2)
         
        if abs(dist1) > abs(dist2): #comparing to label as 1 or 2
            trainingSet[n][8] = 2
        else:
            trainingSet[n][8] = 1
    c1 = 0 #counter to keep track of number to average out  new value of cm1 and cm2
    c2 = 0
    
    for n in range(len(trainingSet)):
        if trainingSet[n][8] == 2:
            for x in range(len(cm2)):
                cm2[x] = cm2[x] + trainingSet[n][x]
            c2 = c2 +1
        else : 
            for x in range(len(cm1)):
                cm1[x] = cm1[x] + trainingSet[n][x]
            c1 = c1 +1
    for x in range(len(cm1)):
        if c1 != 0:
            cm1[x] = cm1[x]/c1
        if c2 != 0:
            cm2[x] = cm2[x]/c2

predictions = []
for n in range(len(trainingSet)):
    predictions.append(trainingSet[n][8])

#print (predictions)
f1 = open('15IE10029_7.out','w+')
f1.write(' '.join(map(str,predictions)))
f1.close()