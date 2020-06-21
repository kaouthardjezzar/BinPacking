from tabu_search import TabuSearch
from SimulatedAnnealing import SA
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

    return bins_algo,time_algo
if __name__ == '__main__':
    # Algo to compare : array of two names
    names = ['SA', 'RT']

    datasets = [
        # {"name": "HARD9.txt", "solution":56, "results": {}},
        # {"name": "HARD0.txt", "solution":56, "results": {}},
        # {"name": "HARD6.txt", "solution":57, "results": {}},
        # {"name": "HARD7.txt", "solution":55, "results": {}},

        {"name": "N1C1W4_E.txt", "solution":35, "results": {}},
        {"name": "N1C2W2_H.txt", "solution":23, "results": {}},
        {"name": "N1C3W1_C.txt", "solution":17, "results": {}},
        {"name": "N2C1W1_G.txt", "solution":60, "results": {}},
        {"name": "N2C2W1_F.txt", "solution":49, "results": {}},
        {"name": "N2C3W1_Q.txt", "solution":34, "results": {}},
        {"name": "N3C1W1_K.txt", "solution":102, "results": {}},

        # {"name": "N1W4B2R3.txt", "solution":6, "results": {}},
        # {"name": "N2W1B3R8.txt", "solution":34, "results": {}}, 
        # {"name": "N3W3B3R1.txt", "solution":27, "results": {}}, 
        # {"name": "N4W4B3R9.txt", "solution":56, "results": {}},   
    ]

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
    # plt.show()
    plt.savefig('graphs/execution_time_'+names[0]+'_VS_'+names[1]+'.png')
    # input()
