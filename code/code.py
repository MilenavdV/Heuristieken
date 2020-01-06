from readconnections import readConnections
from classes import Traject, Connection
import random

connections = {}
trajecten = {}

""" Function for finding possible connections from given startpoint(origin) 
    while excluding the previous station """

def findConnections(origin, previous_station):
    options = []
    for i in connections:
        if origin == connections[i].origin and connections[i].destination != previous_station:
            options.append(i)
    return options


def main():
    # create Connection objects
    for station in readConnections():
        destinations = readConnections()[station]
        
        for optie in destinations:
            destination = optie[0]
            time = optie[1]
            connection = Connection(station, destination, int(time))
            key = connection.origin + "-" + connection.destination
            connections[key] = connection

    # create Traject departing from Den Helder
    traject = Traject()
    traject.addConnection(connections["Den Helder-Alkmaar"], connections["Den Helder-Alkmaar"].time)

    for i in range(0,50):
        new_origin = traject.connections[-1].destination
        previous_station = traject.connections[-1].origin
        options = findConnections(new_origin, previous_station)

        if len(options) != 0:
            new_connection = random.choice(options)
       
        traject.addConnection(connections[new_connection], connections[new_connection].time)
    
    print(traject)

if __name__ == "__main__":
    main()