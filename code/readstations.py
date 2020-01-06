import csv

stations = {}

with open('data/StationsNationaal.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        stations[row[0]] = [row[1], row[2]]

print(stations)
