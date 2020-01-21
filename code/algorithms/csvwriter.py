'''
csvwriter.py saves the tracks that are made with a certain algorithm in csv file.
So it could be easily used the visualise the solution
'''

from .readstations import readStations
import csv


def csvWriter(station_file,file,trajecten):
    """Returns a csv file with all the tracks"""

    stations = readStations(station_file)
    with open(file, mode="w") as file:
        csv_writer = csv.writer(file)
        for traject in trajecten:

            # track number
            csv_writer.writerow(["Traject " + str(traject)])
            for connectie in trajecten[traject].connections:
                
                # origin,destination, coordinates_origin, coordinates_destianation, time
                csv_writer.writerow([connectie.origin, connectie.destination, stations[connectie.origin][0],stations[connectie.origin][1], stations[connectie.destination][0], stations[connectie.destination][1], str(connectie.time)])
            
            # the total time a track cost
            csv_writer.writerow(["Total time of " + str(trajecten[traject].time) + " minutes."])
