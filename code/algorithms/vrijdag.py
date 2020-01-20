from code.algorithms.functions import fastestConnection, findConnections,formula
from code.classes.traject import Traject


def test(file,timeframe,stations,connections,trains):
    traject = Traject()
    connections_used =[]
    count = 0
    stationsvalues = {}
    trajecten ={}
    total_minutes = 0
    
    for station in stations:
        con_values = len(stations[station])
        if station not in stationsvalues:
            stationsvalues[station] =[]
        stationsvalues[station].append(con_values)     
    sort_con = sorted(stationsvalues.items(),key = lambda kv:(kv[1], kv[0]))
    p = 0
    trains = 1
    # while True:
    #     trains +=1
    for i in range(0,20):
        traject = Traject()
        while True:
            check = f"{sort_con[0][0]}-{stations[sort_con[0][0]][0][0]}"
            if check in connections_used:
                sort_con.pop(0)
            else:
                break
        origin = sort_con[0][0]
        destination = stations[origin][0][0]
        traject.addConnection(connections[f"{origin}-{destination}"],stations[origin][0][1],timeframe)
        connections_used.append(f"{origin}-{destination}")
        count +=1
        sort_con.pop(0)  
    
        while True:   
            new_connection = fastestConnection(connections,destination,origin)                
            if new_connection != None:
                traject.addConnection(connections[new_connection],connections[new_connection].time,timeframe)    
                if new_connection not in connections_used:
                    connections_used.append(new_connection)
                    count +=1
            else: 
                break
            destination = traject.connections[-1].destination
            origin = traject.connections[-1].origin   
            if traject.time + connections[new_connection].time > timeframe:
                break 
        total_minutes +=traject.time
        trajecten[i] = traject
        # print(traject)


        p = count/89
        print(count,p, total_minutes,trains)
        score = formula(p,trains,total_minutes)
        train_used= i
        
    return trajecten,p,score, train_used

