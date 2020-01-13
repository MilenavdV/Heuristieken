import csv

def readStations(file):
    stations = {}

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            stations[row[0]] = [row[1], row[2]]

    return stations