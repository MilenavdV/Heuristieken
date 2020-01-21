from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal
<<<<<<< HEAD
from code.algorithms.lookahead_climber import lookaheadClimber
=======
>>>>>>> 0c27465c3ba08837c7703743e22a84262d1e11b7
from code.algorithms.oldrandomize import oldrandomize
from code.algorithms.connectioncount import connectionCount
from code.algorithms.hillclimb import HillClimber
from code.visualisation.visualise import visualise

import numpy
import pandas as pd
import matplotlib.pyplot as plt
<<<<<<< HEAD
=======


>>>>>>> 0c27465c3ba08837c7703743e22a84262d1e11b7

if __name__ == "__main__":
    sims = 10
    trains = 7
    timeframe = 120
    p = 0
<<<<<<< HEAD
    station_file = 'data/StationsNationaal.csv'
    file = 'data/ConnectiesNationaal.csv'
=======
    file = 'data/ConnectiesHolland.csv'
>>>>>>> 0c27465c3ba08837c7703743e22a84262d1e11b7
    output = 'dienstregeling.csv'
    stations, cdict, clist, clist2 = readConnections(file)
    plt.close('all')
    daf = pd.DataFrame()
    scoreslist = {}
<<<<<<< HEAD
    for j in range(4):
        for i in range(5):
            trajecten, p, score = oldrandomize(file)
            scoreslist[i] = score
        if j == 0:
            df = pd.DataFrame({j: scoreslist.values()}, index = scoreslist.keys())
        else:
            df.assign(j = scoreslist, index = scoreslist.keys())
=======
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
>>>>>>> 0c27465c3ba08837c7703743e22a84262d1e11b7
    plt.figure()
    boxplot = df.boxplot()
    fig = boxplot.get_figure()
    plt.show()
<<<<<<< HEAD



    # print(scoreslist)
    # trajecten,p,score,train_used = connectionCount(file,timeframe,stations,cdict,trains)
    # print(score,p,train_used)
    
    # # for i in range(0,500):
    # #     trajecten, p,minutes,score = fastestOption(stations, cdict, clist,clist2, trains, time)
    # #     count +=1
    # #     print(score)
    # #     if score >= 100:
    # #         break
    # # print(trajecten)
    # # csvWriter(output,trajecten)
    # # # score = 10000*p -(trains*100+minutes)
    # # print("Fastest",score)

    # # Kruskal 
    # trajecten,p,score = kruskal(file,trains,timeframe)
    # print("Kruskal",score)
    
    # # while True:
    # #     trajecten,scorerandom,p,trains_used = lookaheadClimber(cdict, clist, trains, timeframe)
    # #     if scorerandom > 6780:
    # #         break

    # # print("Random",scorerandom, p)
    # # csvWriter(station_file,output,trajecten)
    train_used =12
    visualise(train_used)
    
=======
>>>>>>> 0c27465c3ba08837c7703743e22a84262d1e11b7
