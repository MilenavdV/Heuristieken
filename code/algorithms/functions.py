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
        if i not in connections_used and connections[i].time + traject_time < timeframe:
            useful_options.append(i)
        for j in destinations_options:
            destinations_destinations_options = findConnections(connections[j].destination, connections[j].origin, connections)
            if j not in connections_used and connections[i].time + connections[j].time + traject_time < timeframe:
                useful_options.append(i)
            for k in destinations_destinations_options:
                destinations_destinations_destinations_options = findConnections(connections[k].destination, connections[k].origin, connections)
                if k not in connections_used and connections[i].time + connections[j].time + connections[k].time + traject_time < timeframe:
                    useful_options.append(i)
                for l in destinations_destinations_destinations_options:
                    if l not in connections_used and connections[i].time + connections[j].time + connections[k].time + traject_time < timeframe:
                        useful_options.append(i)
    return useful_options


def bestOption(origin, options, connections_used, traject_time, timeframe, connections):
    useful_options = []
   
    origin = origin

    max_score_per_option = []
    
    for i in options:
        
        possible_scores_per_option = []
        
        destinations_options = findConnections(connections[i].destination, origin, connections)
        if i not in connections_used and connections[i].time + traject_time < timeframe:
            useful_options.append(i)
            added_score = 112 - connections[i].time
        else:
            added_score = - connections[i].time
        #print("i", i, added_score) 
        possible_scores_per_option.append(added_score)

        for j in destinations_options:
            
            destinations_destinations_options = findConnections(connections[j].destination, origin, connections)
            if j != i and changeDirection(j) != i and j not in connections_used and connections[i].time + connections[j].time + traject_time < timeframe:
                useful_options.append(i)
                added_score_child = added_score + 112 - connections[j].time
            else:
                added_score_child = added_score - connections[j].time
            
            possible_scores_per_option.append(added_score_child)
            #print("j", j, added_score_child) 
            for k in destinations_destinations_options:
               
                destinations_destinations_destinations_options = findConnections(connections[k].destination, origin, connections)
                if k != i and changeDirection(k) != i  and k != j and changeDirection(k) != j and k not in connections_used and connections[i].time + connections[j].time + connections[k].time + traject_time < timeframe:
                    useful_options.append(i)
                    added_score_child_k = added_score_child + 112 - connections[k].time
                else:
                    added_score_child_k = added_score_child - connections[k].time

                possible_scores_per_option.append(added_score_child_k)
                #print("k", k, added_score_child_k) 
                for l in destinations_destinations_destinations_options:
                    
                    if l != i and changeDirection(l) != i  and l != j and changeDirection(l) != j and l != k and changeDirection(l)!= k and l not in connections_used and connections[i].time + connections[j].time + connections[k].time + connections[l].time + traject_time < timeframe:
                        useful_options.append(i)
                        added_score_child_l = added_score_child_k + 112 - connections[l].time
                    else:
                        added_score_child_l = added_score_child_k - connections[l].time
                    possible_scores_per_option.append(added_score_child_l)
                    #print("l", l, added_score_child_l) 
        max_score_per_option.append(max(possible_scores_per_option))

    if len(useful_options) == 0:
        return None
    
    highest_score = max(max_score_per_option)
    count = 0
    for m in max_score_per_option:
        if m == highest_score:
            position = count
            return options[position]
        count += 1
