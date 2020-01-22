<<<<<<< HEAD
from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal
from code.algorithms.royspartytent import randomize
from code.algorithms.vrijdag import test
from code.algorithms.hillclimb import HillClimber
from code.visualisation.visualise import visualise
from code.algorithms.csvreader import checkScore
=======
from code.algorithms.greedy import Greedy
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import Kruskal
from code.algorithms.lookahead_climber import Lookahead
from code.algorithms.oldrandomize import Randomize
from code.algorithms.connectioncount import Count
from code.algorithms.hillclimb import HillClimber
# from code.visualisation.boxplot import Vergelijking
from code.algorithms.connectioncount import Count
from code.visualisation.visualise import Visualise

import numpy
import pandas as pd
import matplotlib.pyplot as plt

>>>>>>> b96cdd9d485cf98e65a9c05213e6aaac9953cd64

if __name__ == "__main__":
    # # # sims = 10
    trains = 20
    timeframe = 180
    station_file = 'data/StationsNationaal.csv'
    file = 'data/ConnectiesNationaal.csv'
<<<<<<< HEAD
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
    
=======
    output = 'dienstregeling3.csv'
    functie = Lookahead(file,trains,timeframe)
    # while True:
    #     trajecten, p, score, trains_used = functie.lookaheadClimber()
    #     print(score,p*178)
    #     if score >7000 or p ==1:
    #         print('YAS')
    #         csvWriter(station_file,f"dienstregeling{round(score)}T.csv",trajecten)

    # # csvWriter(station_file,output,trajecten)
    vis = Visualise(10)  
    vis.map()


>>>>>>> b96cdd9d485cf98e65a9c05213e6aaac9953cd64
