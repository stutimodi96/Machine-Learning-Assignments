# 15IE10029
# Stuti Modi
# Assignment 3

import csv
import numpy as np

filename = 'data3.csv'
lines = csv.reader(open(filename, "r"))
dataset = list(lines)
for i in range(len(dataset)):
	dataset[i] = [float(x) for x in dataset[i]]

#print (np.shape(dataset))

points = np.shape(dataset)[0]
target = np.shape(dataset)[1]-1
totcount1, totcount0 = 0, 0

for i in range(points):
    if dataset[i][target] == 1:
        totcount1 +=1
    else:
        totcount0 +=1

p1 = totcount1/points
p0 = totcount0/points

#print(p1,p0)

conditional = np.zeros(32)
conditional = np.reshape(conditional,(16,2))

#print (conditional)

for  i in range(target):
     count0= [0,0]
     count1 = [0,0]
     for j in range (points):
         if dataset[j][i] == 0 and dataset[j][target] == 0:
             count0[0] += 1
         elif dataset[j][i] == 0 and dataset[j][target] == 1:
             count0[1] += 1
         elif dataset[j][i] == 1 and dataset[j][target] == 0:
             count1[0] += 1   
         else :
             count1[1] += 1 
     conditional[2*i][0] = (count0[0] + 1.0)/(totcount0 + 2.0)
     conditional[2*i][1] = (count0[1] + 1.0)/(totcount1 + 2.0)
     conditional[2*i+1][0] = (count1[0] + 1.0)/(totcount0 + 2.0)
     conditional[2*i+1][1] = (count1[1] + 1.0)/(totcount1 + 2.0)

# print (conditional) 	

filename = 'test3.csv'
lines = csv.reader(open(filename, "r"))
testset = list(lines)
for i in range(len(testset)):
	testset[i] = [float(x) for x in testset[i]]

# print (testset)

res = []

for j in range(np.shape(testset)[0]):
    prob0, prob1 = p0, p1
    for i in range( np.shape(testset)[1]):
        ind = int(testset[j][i])
        #print(ind)
        prob0 = prob0*conditional[2*i + ind][0]
        prob1 = prob1*conditional[2*i + ind][1]
    if prob1 > prob0:
        res.append(1)
    else:
        res.append(0)
f1 = open('15IE10029_3.out','w+')
f1.write(' '.join(map(str,res)))
f1.close()

# print( res)