from code.algorithms.readconnections import readConnections
from code.classes.traject import Traject
from code.classes.connection import Connection
from code.classes.station import Station
from code.algorithms.functions import *
import random
import csv

def shortest(usefulOptions, connections):
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

def kruskal(file,trains,timeframe):
    stations, connections, connectionlist, connectionlist2 = readConnections(file)
    connectionlist3 =[]

    trajecten = {}
    total_minutes = 0
    total_connections = len(connectionlist) / 2
    connections_used = []

    if 'Den Helder' in connectionlist2:
        print('yes')
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            connectionlist3.append([row[0],row[1],int(row[2])])
 

    # print(graph)
    graph = sorted(connectionlist2, key=lambda item: item[2])

    # begin, eind, tijd
    for i in range(0, trains):
        u,v,w = graph[0]
        traject = Traject()
        timeframe = timeframe   
        traject.addConnection(connections[f"{u}-{v}"], w, timeframe)
        connections_used.append(connections[f"{u}-{v}"])
        graph.remove([u, v, w])
        graph.remove([v, u, w])
        while True:
            new_origin = traject.connections[-1].destination
            previous_station = traject.connections[-1].origin
            
            options = findConnections(new_origin, previous_station, connections)
            useful_options = usefulConnections(new_origin, options, connections_used, traject.time, timeframe, connections)

            new_connection = shortest(useful_options, connections)
            try:
                time_new_connection = connections[new_connection].time
            except:
                pass
            
            if new_connection != None:
                traject.addConnection(connections[new_connection], time_new_connection, timeframe)
                
                if new_connection not in connections_used and changeDirection(new_connection) not in connections_used:
                    connections_used.append(new_connection)
                
                try:
                    graph.remove([new_origin, traject.connections[-1].destination, int(time_new_connection)])
                    graph.remove([traject.connections[-1].destination,new_origin,int(time_new_connection)])
                except:
                    pass    
            else:
                break
            if traject.time + time_new_connection> timeframe:
                break

        graph = sorted(graph, key=lambda item: item[2])
        trajecten[i + 1] = traject
        total_minutes += traject.time
       
    trains = trains
    # print(total_connections)
    p = (len(connections_used)-trains) / total_connections
    score = formula(p, trains, total_minutes)
    return trajecten,p,score
