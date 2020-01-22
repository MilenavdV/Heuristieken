from code.algorithms.readconnections import readConnections
from code.algorithms.fastestoption import fastestOption
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import kruskal
from code.algorithms.royspartytent import randomize
from code.algorithms.vrijdag import test
from code.algorithms.hillclimb import HillClimber
from code.visualisation.visualise import visualise
from code.algorithms.csvreader import checkScore

if __name__ == "__main__":
    trains = 20
    timeframe = 180
    p = 0
    file = 'data/ConnectiesNationaal.csv'
    output = 'dienstregeling.csv'
    stations, cdict, clist, clist2 = readConnections(file)
    time = 180
    
    high = 0
    while True:

        trajecten,scorerandom,p,trains_used = randomize(cdict, clist, trains, timeframe)
        #print(scorerandom)
        if scorerandom > high:
            print(scorerandom, ">", high)
            high = scorerandom
            
        if scorerandom > 7143 and scorerandom == high:
            csvWriter('dienstregeling2.csv',trajecten)
            print("update csv")

  

    
    #csvWriter('dienstregeling.csv',trajecten)
    # result = 'dienstregeling2.csv'
    # print(checkScore(result, clist))

    # visualise(train_used)
    
