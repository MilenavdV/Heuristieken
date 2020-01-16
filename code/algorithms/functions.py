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
    
def changeDirection(connection):
    newB = str(connection)[:str(connection).find("-")]
    newA = str(connection)[str(connection).find("-") + 1:]
    bToA = newA + "-" + newB
    return bToA

def formula(p, t, min):
    score = p*10000 - (t*100 + min)
    return score

def findConnections(origin, previous_station, connections):
    options = []
    for i in connections:
        if origin == connections[i].origin and connections[i].destination != previous_station:
            options.append(i)
    return options

def usefulConnections(origin, options, connections_used, traject_time, timeframe, connections):
    useful_options = []
    origin = origin
    for i in options:
        destinations_options = findConnections(connections[i].destination, origin, connections)
        if i not in connections_used and changeDirection(i) not in connections_used and connections[i].time + traject_time < timeframe:
            useful_options.append(i)
        for j in destinations_options:
            destinations_destinations_options = findConnections(connections[j].destination, origin, connections)
            if j not in connections_used and changeDirection(j) not in connections_used and connections[i].time + connections[j].time + traject_time < timeframe:
                useful_options.append(i)
            for k in destinations_destinations_options:
                destinations_destinations_destinations_options = findConnections(connections[k].destination, origin, connections)
                if k not in connections_used and changeDirection(k) not in connections_used and connections[i].time + connections[j].time + connections[k].time + traject_time < timeframe:
                    useful_options.append(i)
                for l in destinations_destinations_destinations_options:
                    if l not in connections_used and changeDirection(k) not in connections_used and connections[i].time + connections[j].time + connections[k].time + traject_time < timeframe:
                        useful_options.append(i)
    return useful_options
