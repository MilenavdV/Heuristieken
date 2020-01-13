<<<<<<< HEAD
from code.algorithms.readconnections import readConnections
from code.classes.traject import Traject
from code.classes.connection import Connection
=======
from .readconnections import readConnections
from .readstations import readStations
from ..classes.connection import Connection
from ..classes.traject import Traject
>>>>>>> 7a3cd8599005339dc298b0870cd7010ad9054b6e
import random
import csv
import os

connections = {}
connectionslist = []

""" Function for finding possible connections from given startpoint(origin) 
    while excluding the previous station """

def findConnections(origin, previous_station):
    options = []
    for i in connections:
        if origin == connections[i].origin and connections[i].destination != previous_station:
            options.append(i)
    return options

def usefulConnections(origin, options, connections_used, traject_time, timeframe):
    useful_options = []
    origin = origin
    for i in options:
        destinations_options = findConnections(connections[i].destination, origin)
        if i not in connections_used and changeDirection(i) not in connections_used and connections[i].time + traject_time < timeframe:
            useful_options.append(i)
        for j in destinations_options:
            destinations_destinations_options = findConnections(connections[j].destination, origin)
            if j not in connections_used and changeDirection(j) not in connections_used and connections[i].time + connections[j].time + traject_time < timeframe:
                useful_options.append(i)
            for k in destinations_destinations_options:
                if k not in connections_used and changeDirection(k) not in connections_used and connections[i].time + connections[j].time + connections[k].time + traject_time < timeframe:
                    useful_options.append(i)
                
    return useful_options

def fastestConnection(origin, previous_station):
    options = []
    time_of_options = []
    for i in connections:
        if origin == connections[i].origin and connections[i].destination != previous_station:
            options.append(i)
            time_of_options.append(connections[i].time)
    try:
        shortest_time = min(time_of_options)
        count = 0
        
        for j in time_of_options:
            if j == shortest_time:
                position = count
                return options[position]
            count += 1
    except:
        return None
    
def changeDirection(verbinding):
    newB = str(verbinding)[:str(verbinding).find("-")]
    newA = str(verbinding)[str(verbinding).find("-") + 1:]
    bToA = newA + "-" + newB
    return bToA

def formula(p, t, minutes):
    score = p*10000 - (t*100 + minutes)    
    return score

def randomize(file):
    # create Connection objects
    for station in readConnections(file):
        destinations = readConnections(file)[station]
        
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
        for i in range(0, 7):
            
            traject = Traject()
        
            start = random.choice(connectionslist)
            traject.addConnection(connections[start], connections[start].time)

            for j in range(0,20):
                new_origin = traject.connections[-1].destination
                previous_station = traject.connections[-1].origin
                options = findConnections(new_origin, previous_station)
                useful_options = usefulConnections(new_origin, options, connections_used, traject.time, traject.timeframe)
                
                if len(useful_options) != 0 :
                    new_connection = random.choice(useful_options)
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

            if p == 1.00:
                print(trajecten)
                print(f"{i + 1} treinen gebruikt")
                print(len(connectionslist), connectionslist)
                print(len(connections_used), connections_used)
                print(p)
                score = formula(p, i + 1, total_minutes)
                print(formula(p, i + 1, total_minutes))

                if score > 9100:
                    stations = readStations('data/StationsNationaal.csv')
                    with open('dienstregeling.csv', mode="w") as file:
                        csv_writer = csv.writer(file)
                        for traject in trajecten:
                            csv_writer.writerow(["Traject " + str(traject + 1)])
                            csv_writer.writerow([])
                            for connectie in trajecten[traject].connections:
                                csv_writer.writerow([connectie.origin, connectie.destination, stations[connectie.origin], stations[connectie.destination], str(connectie.time)])
                            csv_writer.writerow([])
                            csv_writer.writerow(["Total time of " + str(trajecten[traject].time) + " minutes."])
                            csv_writer.writerow([])
                        csv_writer.writerow(["Total score of: " + str(score)])
                    
                    return True
