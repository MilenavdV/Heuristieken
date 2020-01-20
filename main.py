from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.randomize import randomize
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal
from code.algorithms.randomize import randomize
from code.algorithms.oldrandomize import oldrandomize
from code.algorithms.vrijdag import test
from code.algorithms.hillclimb import HillClimber
from code.visualisation.visualise import visualise

import numpy

if __name__ == "__main__":
    trains = 20
    timeframe = 180
    p = 0
    file = 'data/ConnectiesNationaal.csv'
    output = 'dienstregeling.csv'
    stations, cdict, clist, clist2= readConnections(file)
    time = 180
    # scoreslist = []
    # for i in range(100):
    #     trajecten, p, score = oldrandomize(file)
    #     scoreslist.append(score)
    # print(scoreslist)
    # print("Gemiddelde: ", sum(scoreslist)/len(scoreslist))
    # print("Maximum: ", max(scoreslist))
    # print("Minimum: ", min(scoreslist))
    trajecten,p,score,train_used = test(file,timeframe,stations,cdict,trains)
    print(score,p,train_used)
    # test(file,timeframe,stations)
    # count = 0
    # for i in range(0,500):
    #     trajecten, p,minutes,score = fastestOption(stations, cdict, clist,clist2, trains, time)
    #     count +=1
    #     print(score)
    #     if score >= 100:
    #         break
    # print(trajecten)
    # csvWriter(output,trajecten)
    # # score = 10000*p -(trains*100+minutes)
    # print("Fastest",score)

    # Kruskal 
    # trajecten,p,score = kruskal(file,trains,timeframe)
    # print("Kruskal",score)
    
    # while True:
    #     trajecten,scorerandom,p,trains_used = randomize(cdict, clist, trains, timeframe)
    #     if scorerandom > 6780:
    #         break

    # print("Random",scorerandom, p)
    csvWriter('dienstregeling.csv',trajecten)
    visualise(train_used)
    
