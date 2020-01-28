from code.algorithms.greedy import Greedy
from results.csvwriter import csvWriter
from code.algorithms.kruskal import Kruskal
from code.algorithms.iterativedeepening import Lookahead
from code.algorithms.randomize import Randomize
from code.algorithms.leastconnections import Count
from code.algorithms.hillclimb import HillClimber
from code.algorithms.leastconnections import Count
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

    
    print(summary,"\n")
    output_file = 'results/dienstregeling.csv'
    station_files = ['data/stationsHolland.csv','data/stationsNationaal.csv']
    i = 0
    print('Which file do you want to use for all the stations:')
    for option in station_files:
        print(i,':',option)
        i += 1
    file_options = int(input('Choose the number\n'))

    station_file = station_files[file_options]

    connection_files = ['data/connectiesHolland.csv','data/connectiesNationaal.csv']
    print('Which file do you want to use for all the connections:')
    i = 0
    for option in connection_files:
        print(i,':',option)
        i += 1
    connection_file = int(input('Choose the number\n'))
    file = connection_files[connection_file]


    trains = int(input('How many trains, max, do you want to use? \n'))
    timeframe =  int(input('How many minutes is a train allowed to ride? \n'))
    visualise = input('Do you want the answer to be visualised? \n')
    	
    while visualise.lower() != 'no' or visualise.lower() != 'yes':
        print('please answer with a simple yes or no')
        visualise = input('') 
        if visualise.lower() == 'yes' or visualise.lower() == 'no':
            break

    while True:            
        options = ['Random', 'Greedy', 'Kruskal', 'LeastConnections', 'Iterativedeepening']
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
                trajecten,p,score,train_used = alg.run()
                print('Using the Random algorithm the following score is found:',score)
                print('With a p of: ',p,f'and {train_used} trains are used')
            if visualise.lower() =='yes':
                print(train_used)
                csvWriter(station_file,output_file,trajecten)
                vis = Visualise(train_used)
                vis.map()
            again = input('Do you want to try a different algorithm?')
            if again.lower() == 'yes':
                pass
            else:
                break

        if algorithm == 1:
            sims = int(input('How many simulations do you want?'))
            alg = Greedy(file,trains,timeframe)
            for i in range(0,sims):
                trajecten, p,total_minutes,score,train_used= alg.run()
                print('Using the Greedy algorithm the following score is found:',score)
                print('With a p of: ',p)
            again = input('Do you want to try a different algorithm?')
            if visualise.lower() =='yes':
                csvWriter(station_file,output_file,trajecten)
                print(train_used)
                vis = Visualise(train_used)
                vis.map()
            if again.lower() == 'yes':
                pass
            else:
                break

        if algorithm == 2:
            alg = Kruskal(file,trains,timeframe)
            trajecten, p, score, trains_used= alg.run()
            print('Using the Kruskal algorithm the following score is found:',score)
            print('With a p of: ',p)
            if visualise.lower() =='yes':
                csvWriter(station_file,output_file,trajecten)
                vis = Visualise(trains_used)
                vis.map()
            again = input('Do you want to try a different algorithm?')
            if again.lower() == 'yes':
                pass
            else:
                break

        if algorithm == 3:
            alg = Count(file,trains,timeframe)
            trajecten, p, score, train_used= alg.run()
            print('Using the connectioncount algorithm the following score is found:',score)
            print('With a p of: ',p, f'and {train_used} are used.')
            if visualise.lower() =='yes':
                csvWriter(station_file,file,trajecten)
                vis = Visualise(train_used)
                vis.map()
            again = input('Do you want to try a different algorithm?')
            if again.lower() == 'yes':
                pass
            else:
                break

        if algorithm == 4:
            sims = int(input('How many simulations do you want?'))
            alg = Lookahead(file,trains,timeframe,sims)
            for i in range(0,sims):
                trajecten, p, score, train_used= alg.run()
                print('Using the lookahead algorithm the following score is found:',score)
                print('With a p of: ',p, f'and {train_used} trains are used.')
            if visualise.lower() =='yes':
                csvWriter(station_file,file,trajecten)
                print('Using the lookahead algorithm the following score is found:',score)
                print('With a p of: ',p, f'and {train_used} trains are used.')
            if visualise.lower() =='yes':
                csvWriter(station_file,file,trajecten)
                print('Using the lookahead algorithm the following score is found:',score)
                print('With a p of: ',p, f'and {train_used} trains are used.')
            if visualise.lower() =='yes':
                csvWriter(station_file,file,trajecten)
                vis = Visualise(train_used)
                vis.map()
            again = input('Do you want to try a different algorithm?')
            if again.lower() == 'yes':
                pass
            else:
                break



