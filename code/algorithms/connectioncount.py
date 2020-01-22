'''
connectioncount.py is focused on where a train should start.
It chooses a station with the least connections and that isn't used in another track yet.

'''

from code.algorithms.functions import *
from code.classes.traject import Traject
from code.algorithms.readconnections import readConnections

class Count:

    def __init__(self,file,trains,timeframe):
        self.timeframe = timeframe
        self.trains = trains
        self.stations, self.connections, self.clist, self.clist2 = readConnections(file)

    def connectionCount(self):
        """Returns the tracks that are covered, p, score and amount of train used"""

        connections_used =[]
        stationsvalues = {}
        trajecten ={}
        total_minutes = 0
        total_connections = len(self.connections)/2
        
        # counts on how many connection each station has
        for station in self.stations:
            con_values = len(self.stations[station])
            if station not in stationsvalues:
                stationsvalues[station] = []
            # save this value is a dictionary, with the station being the key
            stationsvalues[station].append(con_values)     
        
        # after making this dictionary, sort it with the lowest amount of connections first
        sort_con = sorted(stationsvalues.items(),key = lambda kv:(kv[1], kv[0]))

        # used 18 trains because this provides the best solution
        # trains_used = 1
        # score2 = 0
        for i in range(1,10):
            # trains_used += 1
            traject = Traject()

            # searches for a station with the least connection and not used
            while True:
                check = f"{sort_con[0][0]}-{self.stations[sort_con[0][0]][0][0]}"

                # if the connection is used, drop this connection from the dictionary
                if check in connections_used or changeDirection(check) in connections_used:
                    sort_con.pop(0)

                # otherwise use this connection
                else:
                    break

            # add the connection to the track
            origin = sort_con[0][0]
            destination = self.stations[origin][0][0]
            traject.addConnection(self.connections[f"{origin}-{destination}"],self.stations[origin][0][1],self.timeframe)
            
            # keeps track of the used connections
            connections_used.append(f"{origin}-{destination}")

            # make sure the connection is not in the dictonary anymore
            sort_con.pop(0)  
        
            # after the first connection is found, finish the track
            while True:   
                # we pick the fastest connection
                new_connection = fastestConnection(self.connections,destination,origin)          
                if new_connection != None:

                    # if the connection is already in the current track, stop the train
                    if self.connections[new_connection] in traject.connections:
                        break   

                    # otherwise add the connection to the current track      
                    traject.addConnection(self.connections[new_connection],self.connections[new_connection].time,self.timeframe)    
                    if new_connection not in connections_used:
                        connections_used.append(new_connection)

                # if there is no new connection stop the current track
                else: 
                    break
                destination = traject.connections[-1].destination
                origin = traject.connections[-1].origin

                # if the total time of the track is bigger than the allowed timeframe, stop the current track  
                if traject.time + self.connections[new_connection].time >= self.timeframe:
                    break 

            # data we keep track of to calculate the final score
            total_minutes += traject.time
            trajecten[i] = traject
            train_used = i
            p = (len(connections_used)-i)/total_connections
            score = formula(p,train_used,total_minutes)
        return trajecten, p, score, train_used

