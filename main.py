from code.algorithms.greedy import Greedy
from code.algorithms.csvwriter import csvWriter
from code.algorithms.kruskal import Kruskal
from code.algorithms.lookahead_climber import Lookahead
from code.algorithms.randomize import Randomize
from code.algorithms.connectioncount import Count
from code.algorithms.hillclimb import HillClimber
from code.algorithms.connectioncount import Count
from code.visualisation.visualise import Visualise
from code.algorithms.readconnections import Read

import numpy
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    summary = 'Welcome to our algorithm sources for the rail problem, first of all make sure that you donwloaded the requirements.\n' \
            + 'All these algorithms are focused on maxizmizing the function: K = 10.000*p -(T*100 - MIN) \n'\
            + 'Where k is the quality, p is the proportions of all available connections covered, T amount of train used '\
            + 'and finally the MIN stands for the sum of all the connections made in the solution.'

    while True:
        print(summary)
        station_file =input('Which file do you want to use for all the stations: \n')
        file = input('Which file do you want to use for all the connections: \n')
        trains = int(input('How many trains, max, do you want to use? \n'))
        timeframe =  int(input('How many minutes is a train allowed to ride? \n'))
        visualise = input('Do you want the answer to be visualised?')

        while visualise.lower() != 'no' or visualise.lower() != 'yes':
            print('please answer with a simple yes or no')
            visualise = input('') 
            if visualise.lower() == 'yes' or visualise.lower() == 'no':
                break
        options = ['Random', 'Greedy', 'Kruskal', 'ConnectionCount', 'hillClimber', 'Lookahead']
        print('possible algorithms:')
        i = 0
        for option in options:
            print(i,':',option)
            i += 1

        algorithm = int(input('which algorithm do you want to use?\n'))

        if algorithm == 0:
            sims = int(input('How many simulations do you want?'))
            alg = Randomize(file,trains,timeframe)
            for i in range(0,sims):
                trajecten,p,score,train_used = alg.randomize()
                print('Using the Random algorithm the following score is found:',score)
                print('With a p of: ',p,f'and {train_used} trains are used')
            again = input('Do you want to try a different algorithm?')
            if again.lower() == 'yes':
                pass
            else:
                break

        if algorithm == 1:
            sims = int(input('How many simulations do you want?'))
            alg = Greedy(file,trains,timeframe)
            for i in range(0,sims):
                trajecten,p,score,train_used = alg.run()
                print('Using the Greedy algorithm the following score is found:',score)
                print('With a p of: ',p,f'and {train_used} trains are used')
            break