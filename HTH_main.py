import math
from item import Item
from random import shuffle
from datetime import datetime
import json
from genetic_algorithm_elite import GeneticAlgorithm
from HTH import *

def log(message, end=None):
    print(message, flush=True, end=end)


if __name__ == '__main__':
    datasets = [
        {"name": "HARD9.txt", "solution":56, "results": {}},
        {"name": "HARD0.txt", "solution":56, "results": {}},
        {"name": "HARD6.txt", "solution":57, "results": {}},
        {"name": "HARD7.txt", "solution":55, "results": {}},

        {"name": "N1C1W4_E.txt", "solution":38, "results": {}},
        {"name": "N1C2W2_H.txt", "solution":23, "results": {}},
        {"name": "N1C3W1_C.txt", "solution":17, "results": {}},
        {"name": "N2C1W1_G.txt", "solution":60, "results": {}},
        {"name": "N2C2W1_F.txt", "solution":49, "results": {}},
        {"name": "N2C3W1_Q.txt", "solution":34, "results": {}},
        {"name": "N3C1W1_K.txt", "solution":102, "results": {}},

        {"name": "N1W4B2R3.txt", "solution":6, "results": {}},
        {"name": "N2W1B3R8.txt", "solution":34, "results": {}}, 
        {"name": "N3W3B3R1.txt", "solution":27, "results": {}}, 
        {"name": "N4W4B3R9.txt", "solution":56, "results": {}}, 

        
      
    ]

    # Loop through each data set.
    for dataset in datasets:
        # Read the data into memory
        with open('datasets/{}'.format(dataset["name"]), 'r') as file:
            data = file.read().splitlines()
            num_items, capacity, items = int(data[0]), int(data[1]), data[2:]
            log("\n\nDATASET {}: num_items {} capacity {} items_read {}".format(dataset["name"], num_items, capacity, len(items)))
        items = [Item(size=int(i)) for i in items]
        
        nbthread = 6
        # Perform 30 independent iterations.
        
        # Randomize the order of the items in the item list.
        shuffle(items)
        thing = HTH(capacity, items,nbthread,100,60,60,20,0.1,0.7)
        print("Recherche des solutions en cours ,nombre de threads actifs: " + str(nbthread))
        start_time = datetime.now()
        solutions = thing.run()
        execution_time = datetime.now() - start_time
        # Record the relevant data for analysis
        for s in solutions:
            summary = {
                "execution_time": str(s[1]),
                "num_bins": s[0].num_bins,
                "combination": s[0].pattern,
            }
            dataset["results"].setdefault("HTH", []).append(summary)
            #dataset["results"].setdefault("SA", []).append(summary)
    # Write the captured data to disk.
    with open("./resultats/HTH.json", "w") as file:
        file.write(json.dumps(datasets, indent=2))
