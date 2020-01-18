from code.algorithms.readconnections import readConnections
from code.algorithms.readstations import readStations
from code.algorithms.csvwriter import csvWriter
from code.classes.connection import Connection
from code.algorithms.functions import *
from code.classes.traject import Traject
import random
import csv
import os

def randomize(cdict, clist, trains, timeframe):
    # initialize list of connections for usage of random.choice function
    connectionslist = clist
    timeframe = timeframe
    connections = cdict
    count = 0
    max_trains = trains
    trains_used = 0
    # total amount of connections where a to b and b to a are considered as te same
    total = len(clist) / 2
    while True:
        # save traject objects in dictionairy
        trajecten = {}

        # keep track of the connections used in the whole timetable
        connections_used = []

        # keep track of the total time of the traject object
        total_minutes = 0

        failed_attemps = 0

        # create a new traject object for the amount of trains allowed
        while True:
            current_p = (len(connections_used)) / total
            
            current_score = formula(current_p, trains_used , total_minutes)
            #print(current_p, trains_used, total_minutes, current_score)
            count_new_connections = 0
            
            traject = Traject()

            while True:
                # initialize starting point
                start = random.choice(connectionslist)
                if start not in connections_used:
                    break

            # add starting connection to the traject
            traject.addConnection(connections[start], connections[start].time, timeframe)

            # ugly for-loop that adds connections to the traject object 
            while True:
                # find the current station of the traject
                new_origin = traject.connections[-1].destination

                # find the previous station of the traject
                previous_station = traject.connections[-1].origin
                options = findConnections(new_origin, previous_station, connections)
                useful_options = usefulConnections(new_origin, options, connections_used, traject.time, timeframe, connections)
                
                if len(useful_options) != 0 :
                    new_connection = random.choice(useful_options)
                    traject.addConnection(connections[new_connection], connections[new_connection].time,timeframe)
                else:
                    break
            new_connections = []
            for k in traject.connections:
                if k.text() not in connections_used and changeDirection(k.text()) not in connections_used and k.text() not in new_connections and changeDirection(k.text()) not in new_connections:
                    new_connections.append(k.text())
                    count_new_connections += 1
                    
            p = (len(connections_used) + count_new_connections) / total
            
            score = formula(p, trains_used + 1, total_minutes + traject.time)
            
            #print(p, trains_used + 1, total_minutes + traject.time , score)

            if score > current_score and trains_used != max_trains:
                trajecten[trains_used] = traject
                trains_used += 1
                total_minutes += traject.time
                for k in traject.connections:
                    if k.text() not in connections_used and changeDirection(k.text()) not in connections_used:
                        connections_used.append(k.text())
                #print("Train Added")
            else:
                failed_attemps +=1
            
            if failed_attemps == 75:
                print(round(score))
                break

            #print(traject)
            # print(f"{len(connections_used)} connections used so far.")
            # print(current_p)
        score = formula(p, trains_used + 1, total_minutes)
        return trajecten,score,p,trains_used
