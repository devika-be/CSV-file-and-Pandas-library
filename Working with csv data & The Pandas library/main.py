import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp" :
            temperatures.append(int(row[1]))
    print(temperatures)

#OR
#By using Pandas:

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)


data = pandas.read_csv("weather_data.csv")
print(data["temp"])

