from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.randomize import randomize
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal
from code.algorithms.randomize import randomize
from code.algorithms.vrijdag import test
from code.algorithms.hillclimb import HillClimber
from code.visualisation.visualise import visualise

if __name__ == "__main__":
    trains = 20
    timeframe = 180
    p = 0
    file = 'data/ConnectiesNationaal.csv'
    output = 'dienstregeling.csv'
    stations, cdict, clist, clist2= readConnections(file)
    # trajecten,p,score = test(file,timeframe,stations,cdict,trains)
    # print(trajecten)
    # test(file,timeframe,stations)
    # count = 0
    # while p != 1:
    #     trajecten, p,minutes = fastestOption(stations, cdict, clist,clist2, trains, time)
    #     count +=1
    #     print(count)

    # csvWriter(output,trajecten)
    # # score = 10000*p -(trains*100+minutes)
    # print("Fastest",score)

    # Kruskal 
    # trajecten,p,score = kruskal("data/ConnectiesHolland.csv",7,120)
    # print("Kruskal",score)
    
    # hillclimb = HillClimber("data/ConnectiesHolland.csv",p,trajecten)
    # hillclimb.improve(10)
    # csvWriter('dienstregeling.csv',trajecten)
    # 
    # 

    while True:
        trajecten,scorerandom,p,train_used = randomize(cdict, clist, trains, timeframe)
        if scorerandom > 5600:
            break

    print("Random",scorerandom, p,train_used)
    csvWriter('dienstregeling.csv',trajecten)
    visualise(train_used)
    #6256.561797752809