from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal

if __name__ == "__main__":
    stations, cdict, clist, clist2= readConnections('data/ConnectiesHolland.csv')
    trains = 7
    p = 0
    time = 120
    while p != 1:
        trajecten, p = fastestOption(stations, cdict, clist,clist2, trains, time)

    # csvWriter('dienstregeling.csv',trajecten)
    # kruskal("data/ConnectiesHolland.csv")
    # csvWriter('dienstregeling.csv',trajecten)
