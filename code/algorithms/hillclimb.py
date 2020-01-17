import copy
import random

from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.classes import station, traject, connection

class HillClimber:
    """
    The HillClimber class that takes one of the trains out of the schedule and tries to replan it
    """
    def __init__(self, file, p, traject):
        self.trains = copy.deepcopy(traject)
        self.stations, self.cdict, self.clist, self.clist2= readConnections(file)
        self.proportion = p
        

    def score(self):
        # initialise time
        self.time = 0
        # adds time of all trains
        for train in self.trains:
            self.time += train.time
        # calculates score
        score = 10000 * p - (100 * len(self.trains.keys()) + self.time)
        return score

    def rerun_train(self):
        key = random.choice(self.trains.keys())
        train = self.trains[key]

        new_train
        