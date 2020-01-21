from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.randomize import randomize
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal
from code.algorithms.oldrandomize import oldrandomize
from code.algorithms.connectioncount import connectionCount
from code.algorithms.hillclimb import HillClimber
from code.visualisation.visualise import visualise

import numpy
import pandas as pd
import matplotlib.pyplot as plt



if __name__ == "__main__":
    sims = 10
    trains = 7
    timeframe = 120
    p = 0
    file = 'data/ConnectiesHolland.csv'
    output = 'dienstregeling.csv'
    stations, cdict, clist, clist2 = readConnections(file)
    plt.close('all')
    daf = pd.DataFrame()
    scoreslist = {}
    for i in range(sims):
        trajecten, p, score = oldrandomize(file)
        scoreslist[i] = score
    df = pd.DataFrame(scoreslist.values(), columns = ['random'],index = scoreslist.keys())
    print('Random klaar')

    for i in range(sims):
        trajecten, p, total_minutes, score = fastestOption(stations, cdict, clist, clist2, trains, timeframe)
        scoreslist[i] = score
    df['greedy']  = scoreslist.values()
    print('greedy klaar')

    for i in range(sims):
        score = kruskal(file, trains, timeframe)
        scoreslist[i] = score
    df['kruskal'] = scoreslist.values()
    print('Kruskal klaar')

    for i in range(sims):
        trajecten, p, score, train_used = connectionCount(file, timeframe, stations, cdict, trains)
        scoreslist[i] = score
    df['least connections'] = scoreslist.values()
    print('least connections klaar')

    for i in range(sims):
        trajecten,score,p,trains_used = randomize(cdict, clist, trains, timeframe)
        print(i)
        scoreslist[i] = score
    df['Greedy lookahead'] = scoreslist.values()
    print('Greedy lookahead klaar')
    print(df)
    plt.figure()
    boxplot = df.boxplot()
    fig = boxplot.get_figure()
    plt.show()
