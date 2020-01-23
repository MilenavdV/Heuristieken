from code.algorithms.greedy import Greedy
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import Kruskal
from code.algorithms.lookahead_climber import Lookahead
from code.algorithms.randomize import Randomize
from code.algorithms.connectioncount import Count
from code.algorithms.hillclimb import HillClimber
from code.algorithms.connectioncount import Count
from code.visualisation.visualise import Visualise
<<<<<<< HEAD
from code.algorithms.readconnections import Read
=======
from code.algorithms.royspartytent import randomize
from code.algorithms.readconnections import readConnections
from code.algorithms.functions import *
from code.algorithms.csvreader import *
>>>>>>> 867cd5a1db0c5beca3b7ce10e8a4c6f3efa8cae6

import numpy
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    sims = 10
    trains = 20
    timeframe = 180
    station_file = 'data/StationsNationaal.csv'
    file = 'data/ConnectiesNationaal.csv'
<<<<<<< HEAD
    test = Lookahead(file,trains,timeframe)
    while True:
        trajecten, p, score,train_used = test.lookaheadClimber()
        print(score)
        if score > 7000:
            print("bijna",score)
        if score > 7100:
            print("yas?",score)
            csvWriter(station_file,f"test{round(score)}.csv",trajecten)
=======
    output = 'dienstregeling.csv'

    stations, cdict, clist, clist2 = readConnections(file)
    time = 180
    
    high = 0
    while True:

        trajecten,scorerandom,p,trains_used = randomize(cdict, clist, trains, timeframe)
        if scorerandom > high:
            print(scorerandom, ">", high)
            high = scorerandom
            
        if scorerandom > 7186 and scorerandom == high:
            csvWriter(station_file, 'dienstregeling2.csv', trajecten)
            print("update csv")


    #print(best('Zutphen', 180, cdict, [], ['Apeldoorn-Zutphen', 'Zutphen-Apeldoorn']))
  

    
    #csvWriter('dienstregeling.csv',trajecten)
    # result = 'dienstregeling2.csv'
    # print(checkScore(result, clist))
    
    # vis = Visualise(10)
    # vis.map()
    
    # stations, cdict, clist, clist2 = readConnections(file)
    test = Count(file,trains,timeframe)
    trajecten,p,score,train_used = test.connectionCount()

    print("a")
    improvement = HillClimber(file,p,trajecten)
    improvement.improve(5)

    print(score)
>>>>>>> 867cd5a1db0c5beca3b7ce10e8a4c6f3efa8cae6
