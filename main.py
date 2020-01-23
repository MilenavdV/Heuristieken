from code.algorithms.readconnections import readConnections
# from code.algorithms.fastestoption import fastestOption
from code.algorithms.csvwriter import csvWriter
# from code.algorithms.kruskal import kruskal
from code.algorithms.royspartytent import randomize
# from code.algorithms.vrijdag import test
from code.algorithms.hillclimb import HillClimber
# from code.visualisation.visualise import visualise
# from code.algorithms.csvreader import checkScore
from code.algorithms.connectioncount import Count

if __name__ == "__main__":
    # # # sims = 10
    trains = 20
    timeframe = 180
    station_file = 'data/StationsNationaal.csv'
    file = 'data/ConnectiesNationaal.csv'
    output = 'dienstregeling.csv'
    stations, cdict, clist, clist2 = readConnections(file)
    time = 18
    test = Count(file,trains,timeframe)
    trajecten,p,score,train_used = test.connectionCount()
    print(score)
