""" Engr. Mark Godwin C. Baguio
    July 21, 2022
    Exercise: Hash Table
    
    1. nyc_weather.csv contains new york city weather for first few days in the month of January. 
    Write a program that can answer following,
    ->What was the average temperature in first week of Jan
    ->What was the maximum temperature in first 10 days of Jan
    
    2. nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
    ->What was the temperature on Jan 9?
    ->What was the temperature on Jan 4?
    
    3. poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
    You have to read this file in python and print every word and its count as show below. 
    Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure."""


from Hash_Table_Chaining import HashTable
import csv


if __name__ == "__main__":
    """ 1. nyc_weather.csv contains new york city weather for first few days in the month of January. 
        Write a program that can answer following,
        ->A. What was the average temperature in first week of Jan
        ->B. What was the maximum temperature in first 10 days of Jan """

    filePath = "C:/Users/markb/Desktop/Academics/Programming/Python/DSA Exercises/Hash Table/Exercise assets/nyc_weather.csv"

    hashtable = HashTable(20)

    with open(filePath, "r") as file:
        reader = csv.reader(file)
        total = 0
        averageTemp = 0
        numberOfDays = 7
        intTemp = []

        next(reader)
        for line in reader:
            # print(line)
            hashtable[line[0]] = line[1]
            intTemp.append(int(line[1]))
        """A. What was the average temperature in first week of Jan"""
        for indx, temp in enumerate(intTemp):
            # print(indx, temp)
            total += temp

            if indx == 6:
                averageTemp = total / numberOfDays
                break

        print("The average temperature in the first week of Jan is: {}°C".format(
            averageTemp))
