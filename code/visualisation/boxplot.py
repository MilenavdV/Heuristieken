from code.algorithms.readconnections import readConnections
from code.algorithms.kruskal import kruskal
from code.algorithms.fastestoption import fastestOption
from code.algorithms.randomize import randomize
from code.algorithms.oldrandomize import oldrandomize
from code.algorithms.connectioncount import connectionCount

import numpy
import pandas as pd
import matplotlib.pyplot as plt

class Vergelijking:
    """Creates a boxplot of the different algorithms"""

    def __init__(self, sims, file, trains, timeframe):
        self.file = file
        self.sims = sims
        self.trains = trains
        self.timeframe = timeframe

    def run(self):
        """ Runs the algorithms and creates boxplot """
        p = 0
        stations, cdict, clist, clist2 = readConnections(self.file)
        plt.close('all')
        
        scoreslist = {}
        for i in range(self.sims):
            trajecten, p, score = oldrandomize(self.file)
            scoreslist[i] = score
        df = pd.DataFrame(scoreslist.values(), columns = ['random'],index = scoreslist.keys())
        print('Random klaar')

        for i in range(self.sims):
            trajecten, p, total_minutes, score = fastestOption(stations, cdict, clist, clist2, self.trains, self.timeframe)
            scoreslist[i] = score
        df['greedy']  = scoreslist.values()
        print('greedy klaar')

        for i in range(self.sims):
            score = kruskal(self.file, self.trains, self.timeframe)
            scoreslist[i] = score
        df['kruskal'] = scoreslist.values()
        print('Kruskal klaar')

        for i in range(self.sims):
            trajecten, p, score, train_used = connectionCount(self.file, self.timeframe, stations, cdict, self.trains)
            scoreslist[i] = score
        df['least connections'] = scoreslist.values()
        print('least connections klaar')

        for i in range(self.sims):
            trajecten,score,p,trains_used = randomize(cdict, clist, self.trains, self.timeframe)
            scoreslist[i] = score
        df['Greedy lookahead'] = scoreslist.values()
        print('Greedy lookahead klaar')
        plt.figure()
        boxplot = df.boxplot()
        fig = boxplot.get_figure()
        plt.show()

