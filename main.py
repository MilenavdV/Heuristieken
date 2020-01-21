# from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import Kruskal
from code.algorithms.lookahead_climber import lookaheadClimber
from code.algorithms.oldrandomize import Randomize
from code.algorithms.connectioncount import Count
from code.algorithms.hillclimb import HillClimber
# from code.visualisation.visualise import visualise
from code.visualisation.boxplot import Vergelijking
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
    # station_file = 'data/StationsNationaal.csv'
    file = 'data/ConnectiesNationaal.csv'
    # output = 'dienstregeling.csv'
    test = Vergelijking(sims,file,trains,timeframe)
    test.run()