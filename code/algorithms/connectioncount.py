'''
connectioncount.py

This script is focused on where a train should start his track.
It chooses a station with the least connections and that isn't used in another track yet.

Author: 0505 + Wouter

'''

from code.algorithms.functions import *
from code.classes.traject import Traject
from code.algorithms.readconnections import Read
import operator


class Count:
    def __init__(self,file,trains,timeframe):
        """Initializes the values needed for the algorithm"""
        self.timeframe = timeframe
        self.trains = trains
        read = Read(file)
        self.stations, self.connections, self.clist, self.clist2 = read.readConnections()

    def connectionCount(self):
        """Returns the tracks that are covered, p, score and amount of trais used"""

        # a list which will be filled with the connections that are used
        connections_used = []

        # a dictionary, with the key being the station and the value is the amount of connections of this station
        stationsvalues = {}

        # a dictionary filled with the tracks that are made
        trajecten = {}

        # total minutes of all the tracks together
        total_minutes = 0

        # amount of connections possible, used for calculating p
        total_connections = len(self.connections)/2
        
        # fills the stationsvalues dictionary
        for station in self.stations:
            con_values = len(self.stations[station])
            if station not in stationsvalues:
                stationsvalues[station] = []
            stationsvalues[station].append(con_values)     
        
        # sorts the stationvalues dictionary in ascending order
        sort_con = sorted(stationsvalues.items(),key = lambda kv:(kv[1], kv[0]))

        scorelist = {}
        
        for i in range(1,self.trains):
            traject = Traject()

            # searches for a station with the least connections and not used yet
            while True:
                try:
                    check = f"{sort_con[0][0]}-{self.stations[sort_con[0][0]][0][0]}"
                except:
                    check = 'not valid'
                    break
                # if the connection is used, drop this connection from the dictionary
                if check in connections_used or changeDirection(check) in connections_used:
                    sort_con.pop(0)

                # otherwise use this connection
                else:
                    break
            if check == 'not valid':
                break
            # add the connection to the track
            origin = sort_con[0][0]
            destination = self.stations[origin][0][0]
            traject.addConnection(self.connections[f"{origin}-{destination}"],self.stations[origin][0][1],self.timeframe)
            
            # append track of the used connections, so it won't be used a second time
            connections_used.append(f"{origin}-{destination}")

            # delete the connection from the sorted dictionary, so it wont be used a second time as a start connection
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
                
                # extracts destination and origin from the connection object
                destination = traject.connections[-1].destination
                origin = traject.connections[-1].origin

                # if the total time of the track is bigger than the allowed timeframe, stop the current track  
                if traject.time + self.connections[new_connection].time >= self.timeframe:
                    break 

            # update the total minutes
            total_minutes += traject.time

            # save track
            trajecten[i + 1] = traject

            # save amount of trains used
            train_used = i + 1

            # calculate p
            p = (len(connections_used)-i)/total_connections

            # score after track is added
            score_i = formula(p,train_used,total_minutes)
            if i not in scorelist:
                scorelist[i] = []
            scorelist[i].append(score_i)

        train_used= max(scorelist.items(), key=operator.itemgetter(1))[0]
        score = max(scorelist.values())[0]
        return trajecten, p, score, train_used
