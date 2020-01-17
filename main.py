from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.randomize import randomize
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal

if __name__ == "__main__":
    stations, cdict, clist, list2 = readConnections('data/ConnectiesNationaal.csv')
    trains = 20
    # p = 0
    # while p != 1:
    #     trajecten, p = fastestOption(cdict,clist,trains)

    csvWriter('dienstregeling.csv', randomize(cdict, clist, trains))
