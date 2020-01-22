from code.algorithms.readconnections import readConnections
from code.classes.traject import Traject
from code.classes.connection import Connection
from code.classes.station import Station
from code.algorithms.functions import *
import random
import csv

class Kruskal:

    def __init__(self,file,trains,timeframe):
        self.trains = trains
        self.timeframe = timeframe
        self.stations, self.connections, self.clist, self.clist2 = readConnections(file)


    def shortest(self, usefulOptions, connections):
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

    def kruskal(self):
        # stations, connections, connectionlist, connectionlist2 = readConnections(file)
        # connectionlist3 =[]

        trajecten = {}
        total_minutes = 0
        total_connections = len(self.clist) / 2
        connections_used = []

        # with open(file, mode='r') as csv_file:
        #     csv_reader = csv.reader(csv_file, delimiter=',')
        #     for row in csv_reader:
        #         connectionlist3.append([row[0],row[1],int(row[2])])
    
        graph = sorted(self.clist2, key=lambda item: item[2])

        for i in range(0, self.trains):
            u,v,w = graph[0]
            traject = Traject()
            traject.addConnection(self.connections[f"{u}-{v}"], w, self.timeframe)
            connections_used.append(self.connections[f"{u}-{v}"])
            graph.remove([u, v, w])
            graph.remove([v, u, w])
            while True:
                new_origin = traject.connections[-1].destination
                previous_station = traject.connections[-1].origin
                
                options = findConnections(new_origin, previous_station, self.connections)
                useful_options = usefulConnections(new_origin, options, connections_used, traject.time, self.timeframe, self.connections)
                new_connection = self.shortest(useful_options, self.connections)
                try:
                    time_new_connection = self.connections[new_connection].time
                except:
                    pass
                
                if new_connection != None:
                    traject.addConnection(self.connections[new_connection], time_new_connection, self.timeframe)
                    
                    if new_connection not in connections_used and changeDirection(new_connection) not in connections_used:
                        connections_used.append(new_connection)
                    
                    try:
                        graph.remove([new_origin, traject.connections[-1].destination, int(time_new_connection)])
                        graph.remove([traject.connections[-1].destination,new_origin,int(time_new_connection)])
                    except:
                        pass    
                else:
                    break
                if traject.time + time_new_connection> self.timeframe:
                    break

            graph = sorted(graph, key=lambda item: item[2])
            trajecten[i + 1] = traject
            total_minutes += traject.time
            trains_used = i
        
        p = (len(connections_used)-trains_used) / total_connections
        score = formula(p, self.trains, total_minutes)
        return trajecten,p,score,trains_used
