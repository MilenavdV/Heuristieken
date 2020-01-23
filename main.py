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
    test = Lookahead(file,trains,timeframe)
    while True:
        trajecten, p, score,train_used = test.lookaheadClimber()
        print(score)
        if score > 7000:
            print("bijna",score)
        if score > 7100:
            print("yas?",score)
            csvWriter(station_file,f"test{round(score)}.csv",trajecten)
