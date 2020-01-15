from .readstations import readStations
import csv

def csvWriter(file,trajecten):
    stations = readStations('data/StationsNationaal.csv')
    with open(file, mode="w") as file:
        csv_writer = csv.writer(file)
        for traject in trajecten:
            csv_writer.writerow(["Traject " + str(traject + 1)])
            for connectie in trajecten[traject].connections:
                csv_writer.writerow([connectie.origin, connectie.destination, stations[connectie.origin][0],stations[connectie.origin][1], stations[connectie.destination][0], stations[connectie.destination][1], str(connectie.time)])
            csv_writer.writerow(["Total time of " + str(trajecten[traject].time) + " minutes."])
