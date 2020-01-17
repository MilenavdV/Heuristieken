from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal
from code.algorithms.randomize import randomize
from code.algorithms.vrijdag import test
from code.algorithms.hillclimb import HillClimber

if __name__ == "__main__":
    trains = 7
    timeframe = 120
    p = 0
    time = 120

    # test(file,timeframe,stations)
    # count = 0
    # while p != 1:
    #     trajecten, p,minutes = fastestOption(stations, cdict, clist,clist2, trains, time)
    #     count +=1
    #     print(count)

    # csvWriter(output,trajecten)
    # score = 10000*p -(trains*100+minutes)
    # print("Fastest",score,count)

    # Kruskal 
    trajecten,p,score = kruskal("data/ConnectiesHolland.csv",7,120)
    print("Kruskal",score)
    
    hillclimb = HillClimber("data/ConnectiesHolland.csv",p,trajecten)
    hillclimb.improve(10)
    # csvWriter('dienstregeling.csv',trajecten)
    

    # # Random
    # # while p != 1:
    # #     trajecten,scorerandom,p,countr = randomize(cdict, clist, trains, timeframe)
    # #     # countr +=1
    # # print("Random",scorerandom,countr)
    # # csvWriter('dienstregeling.csv',trajecten)
