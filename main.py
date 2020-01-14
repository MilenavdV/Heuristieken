from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal

if __name__ == "__main__":
    # stations,cdict, clist = readConnections('data/ConnectiesHolland.csv')
    # trains = 7
    # p = 0
    # while p != 1:
    #     trajecten, p = fastestOption(cdict,clist,trains)

<<<<<<< HEAD
    # csvWriter('dienstregeling.csv',trajecten)
    kruskal("data/ConnectiesHolland.csv")
=======
    csvWriter('dienstregeling.csv',trajecten)
>>>>>>> bf7f7495c59cd0accb240d2fdc10a7a1e2ae712b
