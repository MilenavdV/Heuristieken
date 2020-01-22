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

def Options(origin, time_left, connections):
    origin = origin
    time_left = time_left
    connections = connections

    options = []

    for i in connections:
        if connections[i].origin == origin and connections[i].time <= time_left:
            options.append(i)
    
    return options

def best(origin, time_left, connections, used_connections, traject_connections):
    origin = origin
    time_left = time_left
    connections = connections
    used_connections = used_connections
    traject_connections = traject_connections

    options = Options(origin, time_left, connections)
    
    max_scores = []
    for i in options:
        all_scores_this_i = []
       
        if i in used_connections or i in traject_connections:
            score_i = - connections[i].time
        else:
            score_i = (10000/89) - connections[i].time
        all_scores_this_i.append(score_i)

        
        time_left_i = time_left - connections[i].time
       
        options_i = Options(connections[i].destination, time_left_i, connections)
       
        for j in options_i:

            if j in used_connections or j in traject_connections or j == i or j == changeDirection(i):
                score_j = score_i - connections[j].time
            else:
                score_j = score_i + (10000/89) - connections[j].time
            all_scores_this_i.append(score_j)     
        
            time_left_j = time_left_i - connections[j].time

            options_j = Options(connections[j].destination, time_left_j, connections)
           
            for k in options_j:
                if k in used_connections or k in traject_connections or k == i or k == changeDirection(i) or k == j or k == changeDirection(j):
                    score_k = score_j - connections[k].time
                else:
                    score_k = score_j + (10000/89) - connections[k].time  
                all_scores_this_i.append(score_k)
                
            
                time_left_k = time_left_j - connections[k].time

                options_k = Options(connections[k].destination, time_left_k, connections)

                for l in options_k:
                    if l in used_connections or l in traject_connections or l == i or l == changeDirection(i) or l == j or l == changeDirection(j) or l == k or l == changeDirection(k): 
                        score_l = score_k - connections[l].time
                    else:
                        score_l = score_k + (10000/89) - connections[l].time
                    all_scores_this_i.append(score_l)
                    
                    # time_left_l = time_left_k - connections[l].time

                    # options_l = Options(connections[l].destination, time_left_l, connections)

                    # for m in options_l:
                    #     if m in used_connections or m in traject_connections or m == i or m == changeDirection(i) or m == j or m == changeDirection(j) or m == k or m == changeDirection(k) or m == l or m == changeDirection(l):
                    #         score_m = score_l - connections[m].time
                    #     else:
                    #         score_m = score_l + (10000/89) - connections[m].time
                    #     all_scores_this_i.append(score_m)

                    #     time_left_m = time_left_l - connections[m].time

                        #options_m = Options(connections[m].destination, time_left_m, connections)

                        # for n in options_m:
                        #     if n in used_connections or n in traject_connections or n == i or n == changeDirection(i) or n == j or n == changeDirection(j) or n == k or n == changeDirection(k) or n == l or n == changeDirection(l) or n == m or n == changeDirection(m):
                        #         score_n = score_m - connections[n].time
                        #     else:
                        #         score_n = score_m + (10000/89) - connections[n].time
                        #     all_scores_this_i.append(score_n)

                        #     time_left_n = time_left_m - connections[n].time

                        #     options_n = Options(connections[n].destination, time_left_n, connections)

                        #     for o in options_n:
                        #         if o in used_connections or o in traject_connections or o == i or o == changeDirection(i) or o == j or o == changeDirection(j) or o == k or o == changeDirection(k) or o == l or o == changeDirection(l) or o == m or o == changeDirection(m) or o == n or o == changeDirection(n):
                        #             score_o = score_n - connections[o].time
                        #         else:
                        #             score_o = score_n + (10000/89) - connections[o].time
                        #         all_scores_this_i.append(score_o)
                        
                    
        max_scores.append(max(all_scores_this_i))
   
    try:
        highest_score = max(max_scores)
    except:
        return None

    if highest_score <= 0:
        return None

    count = 0
    for score in max_scores:
        if score == highest_score:
            position = count
            #print(score)
            return options[position]
        count += 1


    


    