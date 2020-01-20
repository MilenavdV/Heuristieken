import random
import csv
import os
import fnmatch

from code.algorithms.readconnections import readConnections
from code.algorithms.functions import findConnections, usefulConnections, fastestConnection, changeDirection, formula
from code.classes.connection import Connection
from code.classes.traject import Traject

connections = {}
connectionslist = []

def oldrandomize(file):
    """ Makes a random solution for the problem. """
    # create Connection objects
    if fnmatch.fnmatch(file,'data/ConnectiesHolland.csv'):
        timeframe = 120
        trains = 7
    else:
        timeframe = 180
        trains = 20

    for station in readConnections(file)[0]:
        destinations = readConnections(file)[0][station]
        
        for optie in destinations:
            destination = optie[0]
            time = optie[1]
            connection = Connection(station, destination, int(time))
            key = connection.origin + "-" + connection.destination
            connections[key] = connection
    
    for i in connections:
        connectionslist.append(i)

    total = len(connectionslist) / 2
    
    while True:
        trajecten = {}
        connections_used = []
        total_minutes = 0
        randtrains = random.randrange(trains)

        for i in range(0, randtrains):
            
            traject = Traject()
        
            start = random.choice(connectionslist)
            traject.addConnection(connections[start], connections[start].time, timeframe)

            for j in range(0,20):
                new_origin = traject.connections[-1].destination
                previous_station = traject.connections[-1].origin
                options = findConnections(new_origin, previous_station, connections)
                useful_options = usefulConnections(new_origin, options, connections_used, traject.time, timeframe, connections)
                
                if len(useful_options) != 0 :
                    new_connection = random.choice(useful_options)
                    traject.addConnection(connections[new_connection], connections[new_connection].time, timeframe)
               
            trajecten[i] = traject
            total_minutes += traject.time

            for k in traject.connections:
                if k.text() not in connections_used and changeDirection(k.text()) not in connections_used:
                    connections_used.append(k.text())
            
        p = len(connections_used) / total

    
        # print(p)
        score = formula(p, randtrains, total_minutes)
            # print(score)

            # if score > 0:
            #     os.remove('dienstregeling.txt')
            #     with open('dienstregeling.txt', mode="w") as file:
            #         for traject in trajecten:
            #             file.write("Traject " + str(traject + 1) + ":")
            #             file.write("\n")
            #             for connectie in trajecten[traject].connections:
            #                 file.write((connectie.origin + "-" + connectie.destination + " " + str(connectie.time) + "\n"))
            #             file.write("\n")
            #             file.write(("Total time of " + str(trajecten[traject].time) + " minutes." + "\n"))
            #             file.write("\n")
            #         file.write(("Total score of: " + str(score) + "\n"))
                
        return trajecten, p, score
