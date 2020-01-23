"""
greedy.py

This script chooses a random begin station to start a track. 
After a begin station is chosen, it will select the connection 
with the shortest amount of minutes. This will continue untill the timeframe is exceeded.

Author: 05050 + Wouter

"""

from code.algorithms.readconnections import readConnections
from code.classes.traject import Traject
from code.classes.connection import Connection
from code.algorithms.functions import *
import random

class Greedy:
    """ A class using a greedy algorithm to solve a train planning problem. """
    def __init__(self, file, trains, timeframe):
        """ Initialises the problem. """
        self.stations, self.connections, self.connectionslist = readConnections(file)
        self.trains = trains
        self.timeframe = timeframe

    def run(self, verbose):
        """ Finds a solution for the problem by using a greedy algorithm that takes the fastest option. """
        
        # save traject objects in dictionairy
        trajecten = {}

        # total amount of connections where a to b and b to a are considered the same count of all the elements in list 
        total = len(self.connectionslist)/2 
        
        # a list which will be filled with the connections that are used in all tracks
        connections_used = []

        # total minutes of all the tracks together
        total_minutes = 0

        # create track object
        traject = Traject()

        # create a new track object for the amount of trains allowed
        for i in range(self.trains):
            
            # create track object
            traject = Traject()

            # initialize starting point, not a used connection
            while True:
                start = random.choice(self.connectionslist)
                if start not in connections_used:
                    break
            
            # add starting connection to the track
            traject.addConnection(self.connections[str(start)], self.connections[str(start)].time, self.timeframe)
            
            # for loop that adds connections to the track object 
            for j in range(0, 20):
                # find the current station of the track
                new_origin = traject.connections[-1].destination

                # find the previous station of the track
                previous_station = traject.connections[-1].origin

                # check whether there is an option to expand the track further 
                if fastestConnection(self.connections, new_origin, previous_station) != None:

                    # add the connection with the shortest time to the track
                    new_connection = fastestConnection(self.connections, new_origin, previous_station)
                    traject.addConnection(self.connections[new_connection], self.connections[new_connection].time, self.timeframe)
            
            # save track in the tracks dictionairy
            trajecten[i] = traject
            total_minutes += traject.time

            # update the list of connections used for every new connection that had not been used before
            for k in traject.connections:
                if k.text() not in connections_used and changeDirection(k.text()) not in connections_used:
                    connections_used.append(k.text())
            
            # calculate p
            p = len(connections_used) / total
            score = formula(p,self.trains,total_minutes)

        return trajecten, p,total_minutes,score
