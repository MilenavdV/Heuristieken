"""
functions.py

All the functions that are used by multiple algorithms.

Authors: 0505 + Wouter

"""

def fastestConnection(connections, origin, previous_station):
    """ Finds the fastest connection from a specific station that isn't the station the train arrived from """
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
    """ Reverses the direction of a connection """
    newB = str(connection)[:str(connection).find("-")]
    newA = str(connection)[str(connection).find("-") + 1:]
    bToA = newA + "-" + newB
    return bToA

def formula(p, t, min):
    """ Takes the proportion, amount of trains and minutes and returns score """
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
    """ Finds the possible options given a certain station and the time that is left """
    origin = origin
    time_left = time_left
    connections = connections

    # initialize list to save optoins
    options = []

    # save connection as option when it meets the conditions
    for i in connections:
        if connections[i].origin == origin and connections[i].time <= time_left:
            options.append(i)
    
    return options

def best(origin, time_left, connections, used_connections, traject_connections):
    """ Return the connection that could lead to the highest added score 
        by looking three steps ahead """

    origin = origin
    time_left = time_left
    connections = connections

    # save connections that have been used in other trajects so far
    used_connections = used_connections

    # save connections that have been added so far to this particular traject
    traject_connections = traject_connections

    # find the possible connections by calling the Options function
    options = Options(origin, time_left, connections)
    
    # initialize list to keep track of maximum scores per possible connection from the origin
    max_scores = []

    # loop over the connections that are possible from the origin
    for i in options:

        # save all the scores that are achievable per possible connection from the origin
        all_scores_this_i = []

        # check if the connection has been used already
        if i in used_connections or i in traject_connections:
            
            # added score of adding this connection is equal to minus the time of the connection
            score_i = - connections[i].time
        
        # when the connection has not been used already
        else:

            # added score of adding this connection is equal to:
            # 1 out of 89 connections times the score of 10000 minus the time of the connection
            score_i = (10000/89) - connections[i].time

        # save the score in the score list   
        all_scores_this_i.append(score_i)

        # update the time that is left for this traject
        time_left_i = time_left - connections[i].time

        # find the possible connections starting from the first connections destination
        options_i = Options(connections[i].destination, time_left_i, connections)

        # loop over the connections that are possible from the new origin
        for j in options_i:
            
            # when the connection has been used so far 
            # or when the connection is the same as the connection of the previous loop
            if j in used_connections or j in traject_connections or j == i or j == changeDirection(i):

                # added score of adding this connection is equal to minus the time of the connection
                score_j = score_i - connections[j].time
            
            # when the connection has not been used already
            else:

                # added score of adding this connection is equal to:
                # 1 out of 89 connections times the score of 10000 minus the time of the connection
                score_j = score_i + (10000/89) - connections[j].time
            
            # save the score in the score list
            all_scores_this_i.append(score_j)     

            # update the time that is left for this traject
            time_left_j = time_left_i - connections[j].time

            # find the possible connections starting from the second connections destination
            options_j = Options(connections[j].destination, time_left_j, connections)
            
            # print(j, 'j', score_j)

            # loop over the connections that are possible from the new origin
            for k in options_j:

                # when the connection has been used so far 
                # or when the connection is the same as the connections of the previous loops
                if k in used_connections or k in traject_connections or k == i or k == changeDirection(i) or k == j or k == changeDirection(j):
                    
                    # added score of adding this connection is equal to minus the time of the connection
                    score_k = score_j - connections[k].time
                
                # when the connection has not been used already
                else:

                    # added score of adding this connection is equal to:
                    # 1 out of 89 connections times the score of 10000 minus the time of the connection
                    score_k = score_j + (10000/89) - connections[k].time  
                
                # save the score in the score list
                all_scores_this_i.append(score_k)
        
        # save the highest added score possible from the connection 
        max_scores.append(max(all_scores_this_i))
    
    # find maximum possible added score unless there are no possible connections
    if len(max_scores) != 0:
        highest_score = max(max_scores)
    
    # there is no possible next connection to add to the traject
    else:
        return None

    # when the maximum added score is negative do not add any connection to the traject
    if highest_score <= 0:
        return None

    # find and return corresponding connection by the highest added score
    count = 0
    for score in max_scores:
        if score == highest_score:
            position = count
            return options[position]
        count += 1


    


    