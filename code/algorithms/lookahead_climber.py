from code.algorithms.readconnections import Read
# from code.algorithms.readstations import readStations
from code.algorithms.csvwriter import csvWriter
from code.classes.connection import Connection
from code.algorithms.functions import *
from code.classes.traject import Traject
import random
import csv
import os


class Lookahead:

    def __init__(self,file,trains,timeframe):
        self.trains = trains
        self.timeframe = timeframe
        read = Read(file)
        self.stations, self.connections, self.clist, self.clist2 = read.readConnections()

    def lookaheadClimber(self):
        
        # initialize list of connections for usage of random.choice function
        trains_used = 0
        
        # total amount of connections where a to b and b to a are considered as te same
        total = len(self.clist)
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
                count_new_connections = 0
                
                traject = Traject()
                while True:
                    # initialize starting point
                    start = random.choice(self.clist)
                    if start not in connections_used and changeDirection(start) not in connections_used:
                        break

                # add starting connection to the traject
                traject.addConnection(self.connections[start], self.connections[start].time, self.timeframe)

                # loop that adds connections to the traject object 
                while True:
                    # find the current station of the traject
                    new_origin = traject.connections[-1].destination

                    # find the previous station of the traject                   
                    time_left = self.timeframe - traject.time

                    traject_connections = []
                    for each in traject.connections:
                        traject_connections.append(each.text())
                        traject_connections.append(changeDirection(each.text()))

                    best_option = best(new_origin, time_left, self.connections, connections_used, traject_connections)

                    if best_option != None:
                        traject.addConnection(self.connections[best_option], self.connections[best_option].time, self.timeframe)
                    else:
                        break


                while True:
                    if traject.connections[-1] in traject.connections[:-1]:
                        traject.time = traject.time - traject.connections[-1].time
                        traject.connections.pop()
                    else:
                        break
                new_connections = []

                for k in traject.connections:
                    if k.text() not in connections_used and k.text() not in new_connections:
                        new_connections.append(k.text())
                        new_connections.append(changeDirection(k.text()))
                        count_new_connections += 1
                        
                possible_p = (len(connections_used) + count_new_connections) / total
                
                score = formula(possible_p, trains_used + 1, total_minutes + traject.time)
                

                if score > current_score and trains_used != self.trains:
                    trajecten[trains_used] = traject
                    trains_used += 1
                    total_minutes += traject.time
                    for k in traject.connections:
                        if k.text() not in connections_used:
                            connections_used.append(k.text())
                            connections_used.append(changeDirection(k.text()))

                else:
                    failed_attemps +=1
                
                if failed_attemps == 10:
                    break

            p = len(connections_used) / total
            score = formula(p, trains_used, total_minutes)
            return trajecten, p, score, trains_used            