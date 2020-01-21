from code.algorithms.functions import *
from code.classes.traject import Traject


def connectionCount(file,timeframe,stations,connections,trains):
    traject = Traject()
    connections_used =[]
    stationsvalues = {}
    trajecten ={}
    total_minutes = 0
    
    for station in stations:
        # how many connections does a certain station have
        con_values = len(stations[station])
        if station not in stationsvalues:
            stationsvalues[station] = []
        # save this value is a dictionary, with the station being the key
        stationsvalues[station].append(con_values)     
    
    # after making this dictionary, sort it with the lowest amount of connections first
    sort_con = sorted(stationsvalues.items(),key = lambda kv:(kv[1], kv[0]))

    # used 18 trains because this provides the best solution
    for i in range(0,18):
        traject = Traject()
        while True:
            check = f"{sort_con[0][0]}-{stations[sort_con[0][0]][0][0]}"
            if check in connections_used or changeDirection(check) in connections_used:
                sort_con.pop(0)
            else:
                break
        origin = sort_con[0][0]
        destination = stations[origin][0][0]
        traject.addConnection(connections[f"{origin}-{destination}"],stations[origin][0][1],timeframe)
        connections_used.append(f"{origin}-{destination}")
        sort_con.pop(0)  
    
        while True:   
            new_connection = fastestConnection(connections,destination,origin)
            # options = findConnections(destination,origin,connections)
            
            if new_connection != None:
                if connections[new_connection] in traject.connections:
                    break         
                traject.addConnection(connections[new_connection],connections[new_connection].time,timeframe)    
                if new_connection not in connections_used:
                    connections_used.append(new_connection)
            else: 
                break
            destination = traject.connections[-1].destination
            origin = traject.connections[-1].origin   
            if traject.time + connections[new_connection].time > timeframe:
                break 
        total_minutes +=traject.time
        trajecten[i] = traject
        train_used = i
        p = len(connections_used)/89
        score = formula(p,train_used,total_minutes)
    return trajecten,p,score, train_used


