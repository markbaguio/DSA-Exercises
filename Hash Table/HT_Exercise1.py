"""1. nyc_weather.csv contains new york city weather for first few days in the month of January. 
        Write a program that can answer following,
        ->A. What was the average temperature in first week of Jan
        ->B. What was the maximum temperature in first 10 days of Jan"""


import csv

filePath = "C:/Users/markb/Desktop/Academics/Programming/Python/DSA Exercises/Hash Table/Exercise assets/nyc_weather.csv"
tempList = []
total = 0
averageTemp = 0

with open(filePath, "r") as file:
    csvReader = csv.reader(file)

    next(csvReader)
    for line in csvReader:
        # print(line[1])
        tempList.append(int(line[1]))

for indx, temp in enumerate(tempList):
    total += temp
    if indx == 6:
        averageTemp = total / 7
        break
# A. What was the average temperature in first week of Jan
print("The average temperature in the first week of Jan is: {}°C".format(averageTemp))

# B. What was the maximum temperature in first 10 days of Jan
maxTemp = max(tempList)
print("The maximum temperature in the first 10 days of Jan is: {}".format(maxTemp))
