"""
iterativedeepening.py

This algorithm looks three steps ahead of the current situation, after finding the best path
it makes one move forward and repeats the process. 

Author: 0505 + Wouter

"""
from code.algorithms.readconnections import Read
from code.classes.connection import Connection
from code.algorithms.helpers import formula, changeDirection, bestConnection
from code.classes.traject import Traject
import random
import csv
import os

class Lookahead:
    """A class using a iterativedeepening algorithm to solve a train planning problem."""

    def __init__(self,file,trains, timeframe, failed_attemps):
        """Initializes the objects needed for the algorithm"""

        self.trains = trains
        self.timeframe = timeframe
        read = Read(file)
        self.stations, self.connections, self.clist, self.clist2 = read.readConnections()
        self.failed_attemps = failed_attemps


    def run(self):
        """Returns an efficient solution"""
        
        # keep track of how many trains will be used
        trains_used = 0
        
        # total amount of connections 
        total = len(self.clist)

        # save track objects in dictionairy
        trajecten = {}

        # keep track of the connections used in the whole timetable
        connections_used = []

        # keep track of the total time of all the track object
        total_minutes = 0

        # when current score is lower then previous score, it will be considered as failed attemp
        failed_attemps = 0

        while True:
            # ratio connection used to total in current state
            current_p = (len(connections_used)) / total
            
            # current score
            current_score = formula(current_p, trains_used , total_minutes)

            # how many connections, that are not used before, will the new track have
            count_new_connections = 0
            
            traject = Traject()
            while True:
                # choose random begin connection
                start = random.choice(self.clist)

                # however, make sure that this connenction is not used before
                if start not in connections_used and changeDirection(start) not in connections_used:
                    break

            # add starting connection to the traject
            traject.addConnection(self.connections[start], self.connections[start].time, self.timeframe)

            while True:
                # find the current station of the traject
                new_origin = traject.connections[-1].destination

                # keep track how much time is left within the track
                time_left = self.timeframe - traject.time

                # save the current connections made in a list
                traject_connections = []
                for each in traject.connections:
                    traject_connections.append(each.text())
                    traject_connections.append(changeDirection(each.text()))

                # check which connection is the best to be made
                best_option = bestConnection(new_origin, time_left, self.connections, connections_used, traject_connections)

                # if connection is found, add to track
                if best_option != None:
                    traject.addConnection(self.connections[best_option], self.connections[best_option].time, self.timeframe)
                else:
                    break
            
            # count how many unused connections are found in the new track
            for k in traject.connections:
                if k.text() not in connections_used: 
                    count_new_connections += 1
                    
            # with new connections found, the new p:
            possible_p = (len(connections_used) + count_new_connections) / total
            
            # calculate the possible score
            score = formula(possible_p, trains_used + 1, total_minutes + traject.time)
            
            # when the score is indeed higher than before, add the track
            if score > current_score and trains_used != self.trains:
                trajecten[trains_used] = traject
                trains_used += 1
                total_minutes += traject.time
                for k in traject.connections:
                    if k.text() not in connections_used:
                        connections_used.append(k.text())
                        connections_used.append(changeDirection(k.text()))

            # otherwise the track won't be added and a the programs tries to find a better one  
            else:
                failed_attemps +=1
            
            # if, after 10 failed attemps, no track is found that improves the score we stop
            if failed_attemps == self.failed_attemps:
                break
        
        # final p and score
        p = len(connections_used) / total
        score = formula(p, trains_used, total_minutes)
        return trajecten, p, score, trains_used            