"""
randomize.py

A random begin station and random amount of trains is chosen.
From begin station it keeps on choosing a random connection untill it exceeds the given timeframe

Author: 0505 + Wouter

"""


from code.algorithms.readconnections import Read
from code.algorithms.helpers import findConnections,changeDirection,formula
from code.classes.connection import Connection
from code.classes.traject import Traject

import random


class Randomize:
    
    
    def __init__(self,file,trains,timeframe):
        """Initializes the objects needed for the algorithm"""
        self.trains = trains
        self.timeframe = timeframe
        read = Read(file)
        self.stations, self.connections, self.clist, self.clist2 = read.readConnections()
    
    
    def randomize(self):
        """Returns a random solution for the problem"""

        # how many connections are there in total
        total = len(self.clist) / 2
        
        while True:
            # a dictionary filled with the tracks that are made
            trajecten = {}

            # a list which will be filled with the connections that are used
            connections_used = []

            # total minutes of all the tracks together
            total_minutes = 0

            # chooses a random amount of trains within the given boundries
            randtrains = random.randrange(self.trains)

            for i in range(0, randtrains):
                
                traject = Traject()

                # choose a random begin connection
                start = random.choice(self.clist)

                # add the connection to the current track
                traject.addConnection(self.connections[start], self.connections[start].time, self.timeframe)

                # new beginning point
                new_origin = traject.connections[-1].destination
                previous_station = traject.connections[-1].origin

                # possible connections from the current origin
                options = findConnections(new_origin, previous_station, self.connections)

                # choos a random connection and add this to the track, if there are any options available
                if len(options) != 0:
                    new_connection = random.choice(options)
                    traject.addConnection(self.connections[new_connection], self.connections[new_connection].time, self.timeframe)
                
                # save the track
                trajecten[i] = traject

                # add the amount of minutes
                total_minutes += traject.time

                # for each connection used, add to list connection_used, if connection wasn't used before
                for k in traject.connections:
                    if k.text() not in connections_used and changeDirection(k.text()) not in connections_used:
                        connections_used.append(k.text())
                
            # calculate p
            p = len(connections_used) / total

            # calculate score
            score = formula(p, randtrains, total_minutes)                
            return trajecten, p, score,randtrains
