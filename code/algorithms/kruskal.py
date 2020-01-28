"""
kruskal.py

Kruskal algorithm tries to find the shortest connections and build an allowed track.
This happens untill all trains are used.

Author: 0505 + Wouter

"""


from code.algorithms.readconnections import Read
from code.classes.traject import Traject
from code.classes.connection import Connection
from code.algorithms.helpers import usefulConnections, findConnections, changeDirection, formula
import random
import csv


class Kruskal:
    """A class using a Kruskal algorithm to solve a train planning problem."""

    def __init__(self,file,trains,timeframe):
        """Initializes the objects needed for the algorithm"""
        self.trains = trains
        self.timeframe = timeframe
        read = Read(file)
        self.stations, self.connections, self.clist, self.clist2 = read.readConnections()


    def shortest(self, usefulOptions, connections):
        """Tries to find the shortest connection from all possible connections"""

        # save the time of all the connections
        time_of_options = []

        for i in usefulOptions:
            time_of_options.append(connections[i].time)
        try:
            # find minimum travel time of the options 
            shortest_time = min(time_of_options)

            # find corresponding connection to the minimum time
            count = 0
            for j in time_of_options:
                if j == shortest_time:
                    position = count
                    return usefulOptions[position]
                count += 1
        except:
            return None

    def run(self):
        """Returns the tracks, p, score and trains that are used, found with the help of Kruskal"""

        # dictionary that will be filled with the tracks that are made
        trajecten = {}

        # total minutes of all the tracks together
        total_minutes = 0

        # amount of connections available
        total_connections = len(self.clist) / 2

        # a list which will be filled with the connections that are used in all tracks
        connections_used = []

        # the connection list sorted by time in ascending order
        graph = sorted(self.clist2, key=lambda item: item[2])

        for i in range(0, self.trains):
            # origin, destination, time
            u,v,w = graph[0]

            # create track object
            traject = Traject()

            # add first, with the least time, connection
            traject.addConnection(self.connections[f"{u}-{v}"], w, self.timeframe)

            connections_used.append(self.connections[f"{u}-{v}"])

            # remove from graph so it won't be used again
            graph.remove([u, v, w])
            graph.remove([v, u, w])

            while True:
                # build the track from first given connection
                new_origin = traject.connections[-1].destination
                previous_station = traject.connections[-1].origin
                
                # find options that are allowed to use
                options = findConnections(new_origin, previous_station, self.connections)
                useful_options = usefulConnections(new_origin, options, connections_used, traject.time, self.timeframe, self.connections)

                # with the found options, find shortest option
                new_connection = self.shortest(useful_options, self.connections)
                try:
                    time_new_connection = self.connections[new_connection].time
                except:
                    pass
                
                if new_connection != None:
                    # add connection to the current track
                    traject.addConnection(self.connections[new_connection], time_new_connection, self.timeframe)
                    
                    # update the list of connections used for every new connection that had not been used before
                    if new_connection not in connections_used and changeDirection(new_connection) not in connections_used:
                        connections_used.append(new_connection)
                    
                    try:
                        # if newconnection is still in graph, remove this from graph
                        graph.remove([new_origin, traject.connections[-1].destination, int(time_new_connection)])
                        graph.remove([traject.connections[-1].destination,new_origin,int(time_new_connection)])
                    except:
                        pass    
                else:
                    break

                # keep adding connections untill track is at the maximum of timeframe
                if traject.time + time_new_connection> self.timeframe:
                    break
            
            # update the situation
            graph = sorted(graph, key=lambda item: item[2])
            trajecten[i + 1] = traject
            total_minutes += traject.time
            trains_used = i
        
        # calculate the score in the final situation
        p = (len(connections_used)-trains_used) / total_connections
        score = formula(p, self.trains, total_minutes)
        return trajecten,p,score,trains_used
