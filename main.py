# from code.algorithms.readconnections import readConnections
# from code.algorithms.fastestoption import fastestOption
# from code.algorithms.csvwriter import csvWriter
# from code.algorithms.kruskal import kruskal
# from code.algorithms.lookahead_climber import lookaheadClimber
# from code.algorithms.oldrandomize import oldrandomize
# from code.algorithms.connectioncount import Count
# from code.algorithms.hillclimb import HillClimber
# from code.visualisation.visualise import visualise
# from code.visualisation.boxplot import Vergelijking
from code.algorithms.connectioncount import Count
from code.algorithms.lookahead_climber import Lookahead
from code.algorithms.kruskal import Kruskal
from code.algorithms.oldrandomize import Randomize
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
    # stations, cdict, clist, clist2 = readConnections(file)
    plt.close('all')

    test = Randomize(file,trains,timeframe)
    trajecten,p,score,train_used = test.randomize()
    print(score)

