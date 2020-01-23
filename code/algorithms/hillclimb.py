import copy
import random
import fnmatch

from code.algorithms.readconnections import readConnections
from code.algorithms.functions import findConnections, fastestConnection, changeDirection, formula
# from code.classes.station import Station
from code.classes.traject import Traject
from code.classes.connection import Connection

class HillClimber:
    """
    The HillClimber class that takes one of the trains out of the schedule and tries to replan it
    """
    def __init__(self, file, p, traject):
        self.trains = copy.deepcopy(traject)
        self.stations, self.cdict, self.clist, self.clist2= readConnections(file)
        self.proportion = p

        if fnmatch.fnmatch(file,'data/ConnectiesHolland.csv'):
            self.timeframe = 120
        else:
            self.timeframe = 180

        # initialise time
        self.time = 0
        # adds time of all trains
        for train in self.trains.values():
            self.time += train.time

        self.score = formula(p,len(self.trains.keys()),self.time)
    
    def rerun_train(self):
        # chooses a random train from the planning
        key = random.choice(list(self.trains.keys()))
        train = self.trains[key]

        connections_used = []
        for traject in self.trains:
            if traject is not train:
                for connection in traject.connections:
                    if connection.text() not in connections_used and changeDirection(connection.text()) not in connections_used:
                        connections_used.append(connection.text())

        new_train = Traject()
        
        # find unused track to start the train on
        while True:
            start = random.choice(self.clist)
            # only stops looking when it finds an unused connection
            if start not in connections_used:
                break

        # add starting connection
        new_train.addConnection(self.cdict[str(start)], self.cdict[str(start)].time, self.timeframe)

        while True:
             # find the current station of the traject
            new_origin = new_train.connections[-1].destination

            # find the previous station of the traject
            previous_station = new_train.connections[-1].origin

            # check whether there is an option to expand the traject further 
            if fastestConnection(self.cdict, new_origin, previous_station) != None:

                # add the connection with the shortest time to the traject
                new_connection = fastestConnection(self.cdict, new_origin, previous_station)
                traject.addConnection(self.cdict[new_connection], self.cdict[new_connection].time, self.timeframe)
            
            # stops the process when done
            else:
                break
            
        for k in new_train.connections:
            if k.text() not in connections_used and changeDirection(k.text()) not in connections_used:
                connections_used.append(k.text)

        # define the alternative plan
        new_plan = copy.deepcopy(self.trains)
        # replace train with the new train
        new_plan[key] = new_train

        new_p = 2*len(connections_used)/len(self.clist)

        new_time = 0
        for train in new_plan:
            new_time += train.time
        
        new_score = formula(new_p, len(new_plan.keys()),new_time)

        if new_score > self.score:
            self.trains = copy.deepcopy(new_plan)
            self.score = new_score
            self.time = new_time
        
        return new_score

    def improve(self, iterations):
        print('Before hill climber the quality was', self.score)
        for i in range(iterations):
            self.rerun_train()
        print(f"After {iterations} iterations, HillClimber has improved the quality to {self.score}")