from code.algorithms.greedy import Greedy
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import Kruskal
from code.algorithms.lookahead_climber import Lookahead
from code.algorithms.randomize import Randomize
from code.algorithms.connectioncount import Count
from code.algorithms.hillclimb import HillClimber
from code.algorithms.connectioncount import Count
from code.visualisation.visualise import Visualise

import numpy
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    sims = 10
    trains = 20
    timeframe = 180
    station_file = 'data/StationsNationaal.csv'
    file = 'data/ConnectiesNationaal.csv'
    output = 'dienstregeling.csv'
    stations, cdict, clist, clist2 = readConnections(file)
    time = 180
    
    high = 0
    while True:

        trajecten,scorerandom,p,trains_used = randomize(cdict, clist, trains, timeframe)
        #print(scorerandom)
        if scorerandom > high:
            print(scorerandom, ">", high)
            high = scorerandom
            
        if scorerandom > 7143 and scorerandom == high:
            csvWriter('dienstregeling2.csv',trajecten)
            print("update csv")

  

    
    #csvWriter('dienstregeling.csv',trajecten)
    # result = 'dienstregeling2.csv'
    # print(checkScore(result, clist))

    # visualise(train_used)
    
