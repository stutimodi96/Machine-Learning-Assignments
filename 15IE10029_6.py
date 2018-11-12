#15IE10029
#Stuti Modi
#Assignment 6


import numpy as np
import csv


#Load dataset
filename = 'data6.csv'
lines = csv.reader(open(filename, "r"))
trainingSet = list(lines)
for i in range(len(trainingSet)):
    trainingSet[i] = [float(x) for x in trainingSet[i]]     
#print(trainingSet)
filename = 'test6.csv'
lines = csv.reader(open(filename, "r"))
testSet = list(lines)
for i in range(len(testSet)):
    testSet[i] = [float(x) for x in testSet[i]]
#print (testSet)
    

wt1 = np.random.randn()
wt2 = np.random.randn()
wt3 = np.random.randn()
wt4 = np.random.randn()
wt5 = np.random.randn()
wt6 = np.random.randn()
wt7 = np.random.randn()
wt8 = np.random.randn()
bias = np.random.randn()

learnRate = 0.1

def sigmoid(x) :
    return 1/(1 + np.exp(-x))


for i in range(1000) : #Results for 10 epochs were inconsistent each time and hence I ran for 1000
    
    for random in range(len(trainingSet)):
    #random = np.random.randint(len(trainingSet))
        label = trainingSet[random ][8]
        val = trainingSet[random ][0] * wt1 + trainingSet[random ][1] * wt2 + trainingSet[random ][2] * wt3 + trainingSet[random ][3] * wt4 + trainingSet[random ][4] * wt5 + trainingSet[random][5] * wt6 + trainingSet[random][6] * wt7 + trainingSet[random][7] * wt8 + bias
        
        predict = sigmoid(val)
    
        cost = sigmoid(val)*(1-sigmoid(val))*(predict - label)*2
    
    
        #update weights
        bias = bias - cost * learnRate    
        wt1 = wt1 - cost * learnRate * trainingSet[random][0]
        wt2 = wt2 - cost * learnRate * trainingSet[random][1]
        wt3 = wt3 - cost * learnRate * trainingSet[random][2]
        wt4 = wt4 - cost * learnRate * trainingSet[random][3]
        wt5 = wt5 - cost * learnRate * trainingSet[random][4]
        wt6 = wt6 - cost * learnRate * trainingSet[random][5]
        wt7 = wt7 - cost * learnRate * trainingSet[random][6]
        wt8 = wt8 - cost * learnRate * trainingSet[random][7]
    
predictions =[]

for i in range(len(testSet)):
    val = testSet[i][0] * wt1 + testSet[i][1] * wt2 + testSet[i][2] * wt3 + testSet[i][3] * wt4 + testSet[i][4] * wt5 + testSet[i][5] * wt6 + testSet[i][6] * wt7 + testSet[i][7] * wt8 + bias
    
    predict = sigmoid(val)
    if predict > 0.5:
        result = 1
    else:
        result = 0
    predictions.append(result)

#print (predictions)

f1 = open('15IE10029_6.out','w+')
f1.write(' '.join(map(str,predictions)))
f1.close()
