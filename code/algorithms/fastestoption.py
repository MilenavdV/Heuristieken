from code.algorithms.readconnections import readConnections
from code.classes.traject import Traject
from code.classes.connection import Connection
import random

def fastestConnection(connections, origin, previous_station):
    # initialize lists to keep track of options and the corresponding time
    options = []
    time_of_options = []

    # check which options there are given the origin
    for i in connections:
        if origin == connections[i].origin and connections[i].destination != previous_station:
            # save the option
            options.append(i)

            # save the travel time of the option
            time_of_options.append(connections[i].time)
    # find the fastest option if there are options
    try:
        # find minimum travel time of the options 
        shortest_time = min(time_of_options)

        # find corresponding connection to the minimum time
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

def formula(p, t, min):
    score = p*10000 - (t*100 + min)
    return score

def fastestOption(cdict, clist, trains):
    # initialize list of connections for usage of random.choice function
    connectionslist = clist

    connections = cdict

    # save traject objects in dictionairy
    trajecten = {}

    # total amount of connections where a to b and b to a are considered as te same
    total = len(connectionslist) / 2
    
    # keep track of the connections used in the whole timetable
    connections_used = []

    # keep track of the total time of the traject object
    total_minutes = 0

    # create traject object
    traject = Traject()

    # add starting connection to the traject
    traject.addConnection(connections["Den Helder-Alkmaar"], connections["Den Helder-Alkmaar"].time)

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
            traject.addConnection(connections[new_connection], connections[new_connection].time)

    # save traject in the trajecten dictionairy
    trajecten[0] = traject
    total_minutes += traject.time

    # update the list of connections used for every new connection that had not been used before
    for k in traject.connections:
        if k.text() not in connections_used and changeDirection(k.text()) not in connections_used:
            connections_used.append(k.text())
    
    print(traject)

    # create a new traject object for the amount of trains allowed
    for i in range(1, trains):
        
        # create traject object
        traject = Traject()

        # initialize starting point
        start = random.choice(connectionslist)

        # add starting connection to the traject
        traject.addConnection(connections[start], connections[start].time)
        
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
                traject.addConnection(connections[new_connection], connections[new_connection].time)
        
        # save traject in the trajecten dictionairy
        trajecten[i] = traject
        total_minutes += traject.time

        # update the list of connections used for every new connection that had not been used before
        for k in traject.connections:
            if k.text() not in connections_used and changeDirection(k.text()) not in connections_used:
                connections_used.append(k.text())
        
        # calculate p
        p = len(connections_used) / total
        
        print(traject)
        print(f"{len(connections_used)} connections used so far.")
        print(p)

    print(trajecten)
    print(i + 1)
    print(p)
    print(formula(p, i + 1, total_minutes))
    return trajecten, p
