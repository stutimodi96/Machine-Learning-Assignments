# 15IE10029
# Stuti Modi
# Assignment 4

import csv
import math
import operator

def distance(point1, point2, length):
    distance = 0
    for x in range(0,length):
        distance += pow((int(point1[x]) - int(point2[x])), 2)                
    return math.sqrt(distance)
	
def main():
    trainingSet=[]
    testSet=[]
    
    filename = 'data4.csv'
    lines = csv.reader(open(filename, "r"))
    trainingSet = list(lines)
    for i in range(len(trainingSet)):
        trainingSet[i] = [float(x) for x in trainingSet[i]]     
    
    #print(trainingSet)
    filename = 'test4.csv'
    lines = csv.reader(open(filename, "r"))
    testSet = list(lines)
    for i in range(len(testSet)):
        testSet[i] = [float(x) for x in testSet[i]]
    #print(testSet)    
    predictions=[]
    k = 5  
    for x in range(len(testSet)):
        neighbours = []
        distances = []
        length = len(testSet[x])
        for i in range(len(trainingSet)):
            dist = distance(testSet[x], trainingSet[i], length)
            distances.append((trainingSet[i], dist))
        #print (distances)
        distances.sort(key=operator.itemgetter(1))
        for i in range(k):
            neighbours.append(distances[i][0])
        #print (neighbours)
        classVotes = {}
        for i in range(len(neighbours)):
            response = neighbours[i][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        predictions.append(int(sortedVotes[0][0]))
    
    #print( predictions)
    
    f1 = open('15IE10029_4.out','w+')
    f1.write(' '.join(map(str,predictions)))
    f1.close()
	
main()