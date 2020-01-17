from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.randomize import randomize
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal
from code.algorithms.randomize import randomize
from code.algorithms.vrijdag import test
from code.algorithms.hillclimb import HillClimber

if __name__ == "__main__":
    trains = 20
    timeframe = 180
    p = 0
<<<<<<< HEAD
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
    
=======

    file = 'data/ConnectiesNationaal.csv'
    output = 'dienstregeling.csv'
    stations, cdict, clist, clist2= readConnections(file)

    while True:
        trajecten,scorerandom,p = randomize(cdict, clist, trains, timeframe)
        if scorerandom > 6200:
            break
>>>>>>> af7dfcede7aa511fb2e4c4c25539a1ca171eca38

    print("Random",scorerandom, p)
    csvWriter('dienstregeling.csv',trajecten)
    #6256.561797752809