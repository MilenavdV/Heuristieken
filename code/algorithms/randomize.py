from .readconnections import readConnections
from .readstations import readStations
from .csvwriter import csvWriter
from ..classes.connection import Connection
from ..classes.traject import Traject
import random
import csv
import os

# connections = {}
# connectionslist = []

""" Function for finding possible connections from given startpoint(origin) 
    while excluding the previous station """

def findConnections(origin, previous_station, connections):
    options = []
    for i in connections:
        if origin == connections[i].origin and connections[i].destination != previous_station:
            options.append(i)
    return options

def usefulConnections(origin, options, connections_used, traject_time, timeframe, connections):
    useful_options = []
    origin = origin
    for i in options:
        destinations_options = findConnections(connections[i].destination, origin, connections)
        if i not in connections_used and changeDirection(i) not in connections_used and connections[i].time + traject_time < timeframe:
            useful_options.append(i)
        for j in destinations_options:
            destinations_destinations_options = findConnections(connections[j].destination, origin, connections)
            if j not in connections_used and changeDirection(j) not in connections_used and connections[i].time + connections[j].time + traject_time < timeframe:
                useful_options.append(i)
            for k in destinations_destinations_options:
                destinations_destinations_destinations_options = findConnections(connections[k].destination, origin, connections)
                if k not in connections_used and changeDirection(k) not in connections_used and connections[i].time + connections[j].time + connections[k].time + traject_time < timeframe:
                    useful_options.append(i)
                for l in destinations_destinations_destinations_options:
                    if l not in connections_used and changeDirection(k) not in connections_used and connections[i].time + connections[j].time + connections[k].time + traject_time < timeframe:
                        useful_options.append(i)
    return useful_options

def fastestConnection(origin, previous_station, connections):
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

def randomize(cdict, clist, trains):
    # initialize list of connections for usage of random.choice function
    connectionslist = clist

    connections = cdict

    # total amount of connections where a to b and b to a are considered as te same
    total = len(clist) / 2
    
    while True:
        # save traject objects in dictionairy
        trajecten = {}

        # keep track of the connections used in the whole timetable
        connections_used = []

        # keep track of the total time of the traject object
        total_minutes = 0

        # create a new traject object for the amount of trains allowed
        for i in range(0, trains):
            
            traject = Traject()

            # initialize starting point
            start = random.choice(connectionslist)

            # add starting connection to the traject
            traject.addConnection(connections[start], connections[start].time)

            # ugly for-loop that adds connections to the traject object 
            for j in range(0,20):
                # find the current station of the traject
                new_origin = traject.connections[-1].destination

                # find the previous station of the traject
                previous_station = traject.connections[-1].origin
<<<<<<< HEAD

                # options = findConnections(new_origin, previous_station, connections)
=======
                options = findConnections(new_origin, previous_station, connections)
>>>>>>> bf7f7495c59cd0accb240d2fdc10a7a1e2ae712b
                useful_options = usefulConnections(new_origin, options, connections_used, traject.time, traject.timeframe, connections)
                
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

<<<<<<< HEAD
                if score > 9100:
=======
                if score < 9100:
>>>>>>> bf7f7495c59cd0accb240d2fdc10a7a1e2ae712b
                    return trajecten
