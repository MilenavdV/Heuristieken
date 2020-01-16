from code.algorithms.readconnections import readConnections
from code.classes.traject import Traject
from code.classes.connection import Connection
from code.algorithms.functions import *
import random

def fastestOption(stations,cdict, clist, clist2, trains, timeframe):
    # initialize list of connections for usage of random.choice function
    #strins lijst
    connectionslist = clist

    # rare object lijst
    connections = cdict

    # save traject objects in dictionairy
    trajecten = {}

    # total amount of connections where a to b and b to a are considered as te same
    # total = len(connectionslist) / 2
    # count of all the elements in list 
    total = len([ele for sub in stations.values() for ele in sub])/2 
    
    connections_used = []

    # keep track of the total time of the traject object
    total_minutes = 0

    # create traject object
    traject = Traject()

    # add starting connection to the traject    
    traject.addConnection(connections["Den Helder-Alkmaar"], connections["Den Helder-Alkmaar"].time, timeframe)

    # ugly for-loop that adds connections to the traject object
    for j in range(0,20):
        # find the current station of the traject
        new_origin = traject.connections[-1].destination

        # find the previous station of the traject
        previous_station = traject.connections[-1].origin

        # check whether there is an option to expand the traject further 
        if fastestConnection(connections, new_origin, previous_station) != None:

            # add the connection with the shortest time to the traject
            new_connection = fastestConnection(connections, new_origin, previous_station)
            traject.addConnection(connections[new_connection], connections[new_connection].time, timeframe)

    # save traject in the trajecten dictionairy
    trajecten[0] = traject
    total_minutes += traject.time

    # update the list of connections used for every new connection that had not been used before
    for k in traject.connections:
        if k.text() not in connections_used and changeDirection(k.text()) not in connections_used:
            connections_used.append(k.text())
    
    # print(traject)
    # create a new traject object for the amount of trains allowed
    for i in range(1, trains):
        
        # create traject object
        traject = Traject()

        # # initialize starting point, not a used connection
        while True:
            start = random.choice(connectionslist)
            if start not in connections_used:
                break
        # print(">>>>>",connections_used)
        # graph = sorted(clist2, key=lambda item: item[2])
        # # while True:
        # for station in graph:
        #     start = f"{station[1]}-{station[0]}"
        #     start2 = f"{station[0]}-{station[1]}"
        #     if start not in connections_used and start2 not in connections_used:
        #         break
        

        # print(graph)
        # add starting connection to the traject
        traject.addConnection(connections[str(start)], connections[str(start)].time, timeframe)
        
        # ugly for-loop that adds connections to the traject object 
        for j in range(0, 20):
            # find the current station of the traject
            new_origin = traject.connections[-1].destination

            # find the previous station of the traject
            previous_station = traject.connections[-1].origin

            # check whether there is an option to expand the traject further 
            if fastestConnection(connections, new_origin, previous_station) != None:

                # add the connection with the shortest time to the traject
                new_connection = fastestConnection(connections, new_origin, previous_station)
                traject.addConnection(connections[new_connection], connections[new_connection].time, timeframe)
        
        # save traject in the trajecten dictionairy
        trajecten[i] = traject
        total_minutes += traject.time

        # update the list of connections used for every new connection that had not been used before
        for k in traject.connections:
            if k.text() not in connections_used and changeDirection(k.text()) not in connections_used:
                connections_used.append(k.text())
        
        # calculate p
        p = len(connections_used) / total
        
    #     print(traject)
    #     print(f"{len(connections_used)} connections used so far.")
    #     print(p)

    # print(connections_used)
    # print(i + 1)
    # print(p)
    # print(formula(p, i + 1, total_minutes))
    return trajecten, p,total_minutes
