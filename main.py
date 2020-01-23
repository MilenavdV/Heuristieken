from code.algorithms.greedy import Greedy
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import Kruskal
from code.algorithms.lookahead_climber import Lookahead
from code.algorithms.oldrandomize import Randomize
from code.algorithms.connectioncount import Count
from code.algorithms.hillclimb import HillClimber
from code.algorithms.connectioncount import Count
from code.visualisation.visualise import Visualise

import numpy
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # # # sims = 10
    trains = 20
    timeframe = 180
    station_file = 'data/StationsNationaal.csv'
    file = 'data/ConnectiesNationaal.csv'
    output = 'dienstregeling3.csv'
    functie = Lookahead(file,trains,timeframe)
    while True:
        trajecten, p, score, trains_used = functie.lookaheadClimber()
        if score >7000 or p ==1:
            print('YAS')
            csvWriter(station_file,f"dienstregeling{round(score)}T.csv",trajecten)

    # # csvWriter(station_file,output,trajecten)
    vis = Visualise(10)  
    vis.map()


