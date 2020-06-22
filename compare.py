from tabu_search import TabuSearch
from SimulatedAnnealing import SA
from genetic_algorithm import GeneticAlgorithm
from HRH import HRH
from HRH_AG_RS import HRH_RS
from LTH import LTH
from LTH2 import LTH2
from HTH import *
from item import Item
from random import shuffle
from datetime import datetime
import json
import matplotlib.pyplot as plt

def execute_algo(name,capacity,items):
    if(name == 'SA'):
        sa = SA(0.7,capacity,items,500,10,8)
        start_time = datetime.now()
        sa.run()
        execution_time = datetime.now() - start_time
        bins_algo = len(sa.bins)
        time_algo = execution_time.total_seconds()
    elif(name == 'RT'):
        thing = TabuSearch(capacity, items)
        start_time = datetime.now()
        total_iterations, stagnation, combination = thing.run()
        execution_time = datetime.now() - start_time
        bins_algo = len(thing.bins)
        time_algo = execution_time.total_seconds() 
    elif(name == 'GA'):
        thing = GeneticAlgorithm(capacity, items)
        start_time = datetime.now()
        total_iterations, stagnation = thing.run()
        execution_time = datetime.now() - start_time
        time_algo = execution_time.total_seconds()
        bins_algo = thing.best_solution.num_bins
    elif(name == 'HRH'):
        thing = HRH(capacity, items)
        start_time = datetime.now()
        result1, result2, total_iterationsAG, stagnationAG, total_iterationsTB, stagnationTB, combinationTB = thing.run()
        execution_time = datetime.now() - start_time
        time_algo = execution_time.total_seconds()
        bins_algo = len(result2.bins)
    elif(name == 'HRH_RS'):
        thing = HRH_RS(capacity, items)
        start_time = datetime.now()
        sa = thing.run()
        execution_time = datetime.now() - start_time
        time_algo = execution_time.total_seconds()
        bins_algo = len(sa.bins)
    elif(name == 'LTH'):
        thing = LTH(capacity, items)
        start_time = datetime.now()
        total_iterations, stagnation = thing.run()
        execution_time = datetime.now() - start_time
        time_algo = execution_time.total_seconds()
        bins_algo = thing.best_solution.num_bins
    elif(name == 'LTH2'):
        thing = LTH2(capacity, items)
        start_time = datetime.now()
        total_iterations, stagnation = thing.run()
        execution_time = datetime.now() - start_time
        time_algo = execution_time.total_seconds()
        bins_algo = thing.best_solution.num_bins
    elif(name == 'HTH'):
        thing = HTH(capacity, items)
        start_time = datetime.now()
        sa = thing.run()
        execution_time = datetime.now() - start_time
        time_algo = execution_time.total_seconds()
        bins_algo = [len(a) for a in sa]
    

    return bins_algo,time_algo

def compare(algo1,algo2,datasets):
    names = [algo1,algo2]

    X = []
    Y_bins_algo1 = []
    Y_bins_algo2 = []
    Y_time_algo1 = []
    Y_time_algo2 = []

    # Loop through each data set.
    for dataset in datasets:
        # Read the data into memory
        with open('datasets/{}'.format(dataset["name"]), 'r') as file:
            data = file.read().splitlines()
            num_items, capacity, items = int(data[0]), int(data[1]), data[2:]

        X.append(dataset["name"].split('.')[0])

        items = [Item(size=int(i)) for i in items]
        shuffle(items)

        bins_algo, time_algo = execute_algo(names[0],capacity,items)
        Y_bins_algo1.append(bins_algo)
        Y_time_algo1.append(time_algo)
        bins_algo, time_algo = execute_algo(names[1],capacity,items)
        Y_bins_algo2.append(bins_algo)
        Y_time_algo2.append(time_algo)

    f1 = plt.figure(1)
    plt.plot(X,Y_bins_algo1,Y_bins_algo2)
    plt.ylabel("Nombre de Bin")
    plt.xlabel("Instance")
    plt.legend(names)
    plt.savefig('graphs/bins_number_'+names[0]+'_VS_'+names[1]+'.png')
    f2 = plt.figure(2)
    plt.plot(X,Y_time_algo1,Y_time_algo2)    
    plt.ylabel("Temps d'exécution")
    plt.xlabel("Instance")
    plt.legend(names)
    plt.savefig('graphs/execution_time_'+names[0]+'_VS_'+names[1]+'.png')
    

if __name__ == '__main__':
    # Algo to compare : array of two names
    datasets = [
        # {"name": "HARD9.txt", "solution":56, "results": {}},
        # {"name": "HARD0.txt", "solution":56, "results": {}},
        # {"name": "HARD6.txt", "solution":57, "results": {}},
        # {"name": "HARD7.txt", "solution":55, "results": {}},

        {"name": "N1C1W4_E.txt", "solution":35, "results": {}},
        {"name": "N1C2W2_H.txt", "solution":23, "results": {}},
        # {"name": "N1C3W1_C.txt", "solution":17, "results": {}},
        # {"name": "N2C1W1_G.txt", "solution":60, "results": {}},
        # {"name": "N2C2W1_F.txt", "solution":49, "results": {}},
        # {"name": "N2C3W1_Q.txt", "solution":34, "results": {}},
        # {"name": "N3C1W1_K.txt", "solution":102, "results": {}},

        # {"name": "N1W4B2R3.txt", "solution":6, "results": {}},
        # {"name": "N2W1B3R8.txt", "solution":34, "results": {}}, 
        # {"name": "N3W3B3R1.txt", "solution":27, "results": {}}, 
        # {"name": "N4W4B3R9.txt", "solution":56, "results": {}},   
    ]

    compare('SA','RT',datasets)