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
    
    while True:
        trajecten,scorerandom,p,trains_used = randomize(cdict, clist, trains, timeframe)
        if scorerandom > 6780:
            break

    print("Random",scorerandom, p)
    csvWriter('dienstregeling.csv',trajecten)
    #visualise(train_used)
    