import random
import csv
import os
import fnmatch

from code.algorithms.readconnections import readConnections
from code.algorithms.functions import findConnections, usefulConnections, fastestConnection, changeDirection, formula
from code.classes.connection import Connection
from code.classes.traject import Traject

class Randomize():
    
    def __init__(self,file,trains,timeframe):
        self.trains = trains
        self.timeframe = timeframe
        self.stations, self.connections, self.clist, self.clist2 = readConnections(file)
    
    
    def randomize(self):
        """ Makes a random solution for the problem. """

        total = len(self.clist) / 2
        
        while True:
            trajecten = {}
            connections_used = []
            total_minutes = 0
            randtrains = random.randrange(self.trains)

            for i in range(0, randtrains):
                
                traject = Traject()
            
                start = random.choice(self.clist)
                traject.addConnection(self.connections[start], self.connections[start].time, self.timeframe)

                new_origin = traject.connections[-1].destination
                previous_station = traject.connections[-1].origin
                options = findConnections(new_origin, previous_station, self.connections)

                if len(options) != 0:
                    new_connection = random.choice(options)
                    traject.addConnection(self.connections[new_connection], self.connections[new_connection].time, self.timeframe)
                
                trajecten[i] = traject
                total_minutes += traject.time

                for k in traject.connections:
                    if k.text() not in connections_used and changeDirection(k.text()) not in connections_used:
                        connections_used.append(k.text())
                
            p = len(connections_used) / total
            score = formula(p, randtrains, total_minutes)                
            return trajecten, p, score,randtrains
