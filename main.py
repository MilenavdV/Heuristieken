from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.randomize import randomize
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal
from code.algorithms.randomize import randomize
from code.algorithms.vrijdag import test

if __name__ == "__main__":
    trains = 7
    timeframe = 120
    p = 0
    time = 180
    file = 'data/ConnectiesNationaal.csv'
    output = 'dienstregeling.csv'
    stations, cdict, clist, clist2= readConnections(file)

    test(file,timeframe,stations)
    # count = 0
    # while p != 1:
    #     trajecten, p,minutes = fastestOption(stations, cdict, clist,clist2, trains, time)
    #     count +=1
    #     print(count)

    # csvWriter(output,trajecten)
    # score = 10000*p -(trains*100+minutes)
    # print("Fastest",score,count)

    # # Kruskal 
    # trajecten,p,score = kruskal("data/ConnectiesHolland.csv",trains,timeframe)
    # print("Kruskal",score)
    # # print(trajecten)
    # # csvWriter('dienstregeling.csv',trajecten) 

<<<<<<< HEAD
    csvWriter('dienstregeling.csv', randomize(cdict, clist, trains))
=======
    # # Random
    # # while p != 1:
    # #     trajecten,scorerandom,p,countr = randomize(cdict, clist, trains, timeframe)
    # #     # countr +=1
    # # print("Random",scorerandom,countr)
    # # csvWriter('dienstregeling.csv',trajecten)
>>>>>>> 9ae4982cfc86e94e5f68b2abcaf17d237a05cb41
