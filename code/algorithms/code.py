from readconnections import readConnections
from classes import Traject, Connection
import random

connections = {}
connectionslist = []

trajecten = {}

""" Function for finding possible connections from given startpoint(origin) 
    while excluding the previous station """

def findConnections(origin, previous_station):
    options = []
    for i in connections:
        if origin == connections[i].origin and connections[i].destination != previous_station:
            options.append(i)
    return options

def changeDirection(verbinding):
    newB = str(verbinding)[:str(verbinding).find("-")]
    newA = str(verbinding)[str(verbinding).find("-") + 1:]
    bToA = newA + "-" + newB
    return bToA

def formula(p, t, min):
    score = p*10000 - (t*100 + min)
    return score

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
    
    for i in connections:
        connectionslist.append(i)

    total = len(connectionslist) / 2
    
    while True:
        connections_used = []
        total_minutes = 0
        for i in range(0, 7):
            
            traject = Traject()
        
            start = random.choice(connectionslist)
            traject.addConnection(connections[start], connections[start].time)

            for j in range(0,30):
                new_origin = traject.connections[-1].destination
                previous_station = traject.connections[-1].origin
                options = findConnections(new_origin, previous_station)

                if len(options) != 0:
                    new_connection = random.choice(options)
                    traject.addConnection(connections[new_connection], connections[new_connection].time)
               
            trajecten[i] = traject
            total_minutes += traject.time

            for k in traject.connections:
                if k.print() not in connections_used and changeDirection(k.print()) not in connections_used:
                    connections_used.append(k.print())
            
            p = len(connections_used) / total
            
            print(traject)
            print(f"{len(connections_used)} connections used so far.")
            print(p)

            if p == 1.0:
                print(trajecten)
                print(i + 1)
                print(p)
                print(connections_used)
                print(formula(p, i + 1, total_minutes))
                if formula(p, i + 1, total_minutes) > 9050:
                    return True
        
    

if __name__ == "__main__":
    main()