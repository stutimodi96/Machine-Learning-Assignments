# 15IE10029
# Stuti Modi
#Assignment 1
import csv
import sys

if len(sys.argv)>1:
    filename = sys.argv[1]
else:
    filename = "data1.csv"
    
data = []
data1 = []
c = 1
with open(filename,'r') as f:
    reader = csv.reader(f)
    for row in reader:
        for i in range(len(row)):
            if row[i] not in (',',' ','\n'):
                data1.append(int(row[i]))
        data.append(data1)
        data1 = []
# print (data)
                
hyp = []
yInd = len(data[0])-1

for row in data:
    if row[yInd] == 1:
        if len(hyp) == 0:
            hyp = row
        else:
            for i in range(yInd):
                if(hyp[i] != row[i]):
                    hyp[i]= "?"
#print (hyp)
finalHyp = []
for i in range(yInd):
    if hyp[i]==1:
        finalHyp.append(i+1)
    elif hyp[i] == 0:
        finalHyp.append(-1*(i+1))

print(len(finalHyp),',',', '.join(map(str, finalHyp)))

                
      