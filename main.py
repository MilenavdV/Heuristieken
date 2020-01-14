from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.csvwriter import csvWriter

if __name__ == "__main__":
    cdict, clist = readConnections('data/ConnectiesHolland.csv')
    trains = 7
    p = 0
    while p != 1:
        trajecten, p = fastestOption(cdict,clist,trains)

    csvWriter('dienstregeling.csv',trajecten)
