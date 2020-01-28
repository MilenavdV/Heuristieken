from code.algorithms.greedy import Greedy
from code.algorithms.kruskal import Kruskal
from code.algorithms.iterativedeepening import Lookahead
from code.algorithms.randomize import Randomize
from code.algorithms.leastconnections import Count
from code.algorithms.hillclimb import HillClimber
from code.visualisation.visualise import Visualise
from code.algorithms.readconnections import Read

import numpy
import pandas as pd
import matplotlib.pyplot as plt

class Vergelijking:
    """Creates a boxplot of the different algorithms"""

    def __init__(self, file, sims, trains, timeframe):
        self.file = file
        self.sims = sims
        self.trains = trains
        self.timeframe = timeframe

    def run(self):
        """ Runs the algorithms and creates boxplot """
        plt.close('all')
        
        scoreslist = {}
        rand = Randomize(self.file, self.trains, self.timeframe)
        for i in range(self.sims):
            score = rand.run()[2]
            scoreslist[i] = score
        df = pd.DataFrame(scoreslist.values(), columns = ['random'],
        index = scoreslist.keys())
        print('Random klaar')

        greed = Greedy(self.file, self.trains, self.timeframe)
        for i in range(self.sims):
            score = greed.run()[3]
            scoreslist[i] = score
        df['greedy']  = scoreslist.values()
        print('Greedy klaar')

        krusk = Kruskal(self.file, self.trains, self.timeframe)
        for i in range(self.sims):
            score = krusk.run()[2]
            scoreslist[i] = score
        df['kruskal'] = scoreslist.values()
        print('Kruskal klaar')

        count = Count(self.file, self.trains, self.timeframe)
        for i in range(self.sims):
            score = count.run()[2]
            scoreslist[i] = score
        df['least connections'] = scoreslist.values()
        print('count klaar')

        look = Lookahead(self.file, self.trains, self.timeframe, 50)
        for i in range(self.sims):
            score = look.run()[2]
            print(i, score)
            scoreslist[i] = score
        df['iterative deepening'] = scoreslist.values()
        print('iterative deepening klaar')
        plt.figure()
        boxplot = df.boxplot()
        fig = boxplot.get_figure()
        plt.show()