from code.algorithms.greedy import Greedy
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import Kruskal
from code.algorithms.lookahead_climber import Lookahead
from code.algorithms.randomize import Randomize
from code.algorithms.connectioncount import Count
from code.algorithms.hillclimb import HillClimber
from code.algorithms.connectioncount import Count
from code.visualisation.visualise import Visualise
from code.algorithms.readconnections import Read

import numpy
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    sims = 10
    trains = 20
    timeframe = 180
    station_file = 'data/StationsNationaal.csv'
    file = 'data/ConnectiesNationaal.csv'
    outputfile = 'test7101.csv'
    test = Lookahead(file,trains,timeframe)
    for i in range(1):
        trajecten, p, score,train_used = test.lookaheadClimber()
        print(score)
        # if round(score) == 6593:
        #     continue
        # if score > 7100:
        #     print("bijna",score)
        #     csvWriter(station_file,f"test{round(score)}.csv",trajecten)
        # if score > 7175:
        #     print("yas?",score)
        csvWriter(station_file,outputfile,trajecten)
    # vis = Visualise(10)
    # vis.map()
