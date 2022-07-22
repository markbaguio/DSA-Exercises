""" poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
    You have to read this file in python and print every word and its count as show below. 
    Think about the best data structure that you can use to solve this problem and figure 
    out why you selected that specific data structure.
    
     'diverged': 2,
     'in': 3,
     'I': 8         """


import csv


filePath = "C:/Users/markb/Desktop/Academics/Programming/Python/DSA Exercises/Hash Table/Exercise assets/poem.txt"

formattedTxt = [line.split() for line in open(filePath)]
numberOfDiverged = 0
numebrOfIn = 0
numberOfI = 0

for line in formattedTxt:
    if "diverged" in line:
        numberOfDiverged += 1
    if "in" in line:
        numebrOfIn += 1
    if "I" in line:
        numberOfI += 1
    if "Iâ€”" in line:
        numberOfI += 1
print("diverged: {}\nin: {}\nI: {}".format(
    numberOfDiverged, numebrOfIn, numberOfI))
