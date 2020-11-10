import csv
import pandas as pnd
import plotly.express as px
import math




with open('105data.csv', newline = '') as file :
    reader = csv.reader(file)
    fileData = list(reader)
print(fileData[3])
newData = []
for i in range(len(fileData)):
    nextNum = fileData[i][0]
    newData.append(float(nextNum))
print(newData)
dataLength = len(newData)
total = 0
for i in newData:
    total += i
mean = total/dataLength
print("Mean Value = " + str(mean))

data = fileData
sq1 = []
for num in newData:
    val = (float(num)- mean)
    sq1.append(val)

sum = 0
for i in sq1:
    sum = sum+i
n = sum/(dataLength-1)

sd = math.sqrt(n)

print(sd)
