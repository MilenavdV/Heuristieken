from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal
from code.algorithms.randomize import randomize

if __name__ == "__main__":
    stations, cdict, clist, clist2= readConnections('data/ConnectiesNationaal.csv')
    trains = 20
    timeframe = 180
    p = 0
    time = 180

    count = 0
    while p != 1:
        trajecten, p,minutes = fastestOption(stations, cdict, clist,clist2, trains, time)
        count +=1
        print(count)

    csvWriter('dienstregeling.csv',trajecten)
    score = 10000*p -(trains*100+minutes)
    print("Fastest",score,count)

    # # Kruskal 
    # trajecten,p,score = kruskal("data/ConnectiesHolland.csv",trains,timeframe)
    # print("Kruskal",score)
    # # print(trajecten)
    # # csvWriter('dienstregeling.csv',trajecten)
    

    # # # Random
    # while p != 1:
    #     trajecten,scorerandom,p,countr = randomize(cdict, clist, trains, timeframe)
    #     # countr +=1
    # print("Random",scorerandom,countr)
    # csvWriter('dienstregeling.csv',trajecten)
