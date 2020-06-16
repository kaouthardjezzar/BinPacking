from SimulatedAnnealing import SA
from item import Item
from random import shuffle
from datetime import datetime
import numpy as np
import json
import matplotlib.pyplot as plt

def log(message, end=None):
    print(message, flush=True, end=end)

def generate_random_params(min_T0,max_T0,min_tt,max_tt,min_iter,max_iter):
    return np.random.randint(min_T0,high=max_T0),np.random.randint(min_tt,high=max_tt),np.random.randint(min_iter,high=max_iter)



if __name__ == '__main__':
    nb_iter_values = [int(i/2)+1 for i in range(100) ]
    t0_values = [(i+1)*20 for i in range(50) ]
    t_target_values = [i+1 for i in range(50) ]
    alpha_values = [0.5 + i / 100 for i in range(50) ]
    x = []
    y_bins = []
    y_time = []
    datasets = [
        {"name": "HARD9.txt", "solution":56, "results": {}},
        {"name": "HARD0.txt", "solution":56, "results": {}},
        {"name": "HARD6.txt", "solution":57, "results": {}},
        {"name": "HARD7.txt", "solution":55, "results": {}},
        # {"name": "N1C1W4_E.txt", "solution":0, "results": {}}, 
        # {"name": "N1C2W2_H.txt", "solution":0, "results": {}},
        # {"name": "N1C3W1_C.txt", "solution":0, "results": {}},
        # {"name": "N2C1W1_G.txt", "solution":0, "results": {}},
        # {"name": "N2C2W1_F.txt", "solution":0, "results": {}},
        # {"name": "N2C3W1_Q.txt", "solution":0, "results": {}},
        # {"name": "N3C1W1_K.txt", "solution":0, "results": {}},
    ]

    # Loop through each data set.
    log("  Iteration", end=" ")
    for global_i in range(50):
        log(global_i+1, end=" ")
        cost = 0
        t = 0
        for dataset in datasets:
            # Read the data into memory
            with open('datasets/{}'.format(dataset["name"]), 'r') as file:
                data = file.read().splitlines()
                num_items, capacity, items = int(data[0]), int(data[1]), data[2:]
                #log("\n\nDATASET {}: num_items {} capacity {} items_read {}".format(dataset["name"], num_items, capacity, len(items)))
            items = [Item(size=int(i)) for i in items]
            #log("  Iteration", end=" ")
            # Perform 30 independent iterations.
            for iteration in range(1):
                #log(iteration+1, end=" ")
                # Randomize the order of the items in the item list.
                shuffle(items)
                t0, t_target, nb_iter =500,10,10
                sa = SA(0.9,capacity,items,t0_values[global_i],5,5)
                start_time = datetime.now()
                sa.run()
                execution_time = datetime.now() - start_time

                
                cost += len(sa.bins) - dataset["solution"]
                t += execution_time.total_seconds()
                

                # Record the relevant data for analysis
                summary = {
                    "execution_time": str(execution_time),
                    "t0" : t0,
                    "t_target" : t_target,
                    "nb_iter" : nb_iter_values[iteration],
                    "num_bins": len(sa.bins),
                }
                dataset["results"].setdefault("SA", []).append(summary)
                #dataset["results"].setdefault("SA", []).append(summary)
        x.append(t0_values[global_i])
        y_bins.append(cost)
        y_time.append(t / len(dataset))
    # Write the captured data to disk.
    with open("./results/results_sa.json", "w") as file:
        file.write(json.dumps(datasets, indent=2))
    
    f1 = plt.figure(1)
    plt.plot(x,y_bins)
    plt.ylabel("Nb of bins")
    plt.xlabel("T0")
    f2 = plt.figure(2)
    plt.plot(x,y_time)    
    plt.ylabel("Time")
    plt.xlabel("T0")
    plt.show()
    input()