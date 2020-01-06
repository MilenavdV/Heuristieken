import csv

stations = {}

<<<<<<< HEAD
with open('code/data/StationsNationaal.csv', mode='r') as csv_file:
=======
with open('data/StationsNationaal.csv', mode='r') as csv_file:
>>>>>>> cbe357a35c4a7b10fd6688a64c5bdc202d4f8038
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        stations[row[0]] = [row[1], row[2]]

print(stations)