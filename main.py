from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal
from code.algorithms.randomize import randomize
from code.algorithms.vrijdag import test

if __name__ == "__main__":
    trains = 20
    timeframe = 180
    p = 0
    time = 180
    file = 'data/ConnectiesNationaal.csv'
    output = 'dienstregeling.csv'
    stations, cdict, clist, clist2= readConnections(file)

    trajecten,p,score = test(file,timeframe,stations,cdict,trains)
    # print(trajecten)
    # count = 0
    # while p != 1:
    #     trajecten, p,minutes = fastestOption(stations, cdict, clist,clist2, trains, time)
    #     count +=1
    #     print(count)

    csvWriter(output,trajecten)
    # score = 10000*p -(trains*100+minutes)
    print("Fastest",score)

    # # Kruskal 
    # trajecten,p,score = kruskal("data/ConnectiesHolland.csv",trains,timeframe)
    # print("Kruskal",score)
    # # print(trajecten)
    # # csvWriter('dienstregeling.csv',trajecten) 

    # # Random
    # # while p != 1:
    # #     trajecten,scorerandom,p,countr = randomize(cdict, clist, trains, timeframe)
    # #     # countr +=1
    # # print("Random",scorerandom,countr)
    # # csvWriter('dienstregeling.csv',trajecten)
