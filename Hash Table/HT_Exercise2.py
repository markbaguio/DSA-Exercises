"""2. nyc_weather.csv contains new york city weather for first few days in the month of January.
     Write a program that can answer following,
    ->What was the temperature on Jan 9?
    ->What was the temperature on Jan 4?

    Ans: I will utilize a Hash Table or dictionary. A list can also be used as both Hash Table and list have a
        a time complexity of O(1) or constant-time when accessing an element."""

import csv
from Hash_Table_Chaining import HashTable

filePath = "C:/Users/markb/Desktop/Academics/Programming/Python/DSA Exercises/Hash Table/Exercise assets/nyc_weather.csv"
ht = HashTable()
with open(filePath, "r") as file:
    csvReader = csv.reader(file)
    next(csvReader)

    for line in csvReader:
        ht[line[0]] = line[1]

# What was the temperature on Jan 9?
print("The temperature on Jan 9 is: {}".format(ht["Jan 9"]))
# What was the temperature on Jan 4?
print("The temperature on Jan 4 is: {}".format(ht["Jan 4"]))
