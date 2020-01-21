from code.algorithms.connectioncount import Count
from code.algorithms.lookahead_climber import Lookahead
from code.algorithms.kruskal import Kruskal
from code.algorithms.oldrandomize import Randomize
from code.algorithms.hillclimb import HillClimber

import numpy
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    sims = 10
    trains = 20
    timeframe = 180
    p = 0
    station_file = 'data/StationsNationaal.csv'
    file = 'data/ConnectiesNationaal.csv'
    output = 'dienstregeling.csv'
    plt.close('all')



    test = Randomize(file,trains,timeframe)
    trajecten,p,score,train_used = test.randomize()
    print(score)

