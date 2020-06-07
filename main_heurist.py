from bin import Bin
from item import Item
from heuristics import BestFit, FirstFit, NextFit, WorstFit , FirstFitDec, NextFitDec, BestFitDec, WorstFitDec
from random import shuffle
from datetime import datetime
import json


def log(message, end=None):
    print(message, flush=True, end=end)


if __name__ == '__main__':
    datasets = [
        {"name": "N1C1W4_E.txt", "results": {}},
        {"name": "N1C2W2_H.txt", "results": {}},
        {"name": "N1C3W1_C.txt", "results": {}},
        {"name": "N2C1W1_G.txt", "results": {}},
        {"name": "N2C2W1_F.txt", "results": {}},
        {"name": "N2C3W1_Q.txt", "results": {}},
        {"name": "N3C1W1_K.txt", "results": {}},
        {"name": "N3C2W2_M.txt", "results": {}},
        {"name": "N3C3W4_O.txt", "results": {}},
        {"name": "N4C1W1_N.txt", "results": {}},
        {"name": "N4C2W2_L.txt", "results": {}},
        {"name": "N4C3W1_F.txt", "results": {}},
        {"name": "N1W4B2R3.txt", "results": {}},
        {"name": "N2W1B3R8.txt", "results": {}},
        {"name": "N3W3B3R1.txt", "results": {}},
        {"name": "N4W4B3R9.txt", "results": {}},
        {"name": "HARD0.txt", "results": {}},
        {"name": "HARD7.txt", "results": {}},
        {"name": "HARD9.txt", "results": {}},
        
    ]
    heuristic_list = [FirstFit, NextFit, WorstFit, BestFit ]
    DecHeuristic_list = [FirstFitDec, NextFitDec, BestFitDec, WorstFitDec]
    # Loop through each data set.
    for dataset in datasets:
        # Read the data into memory
        with open('datasets/{}'.format(dataset["name"]), 'r') as file:
            data = file.read().splitlines()
            num_items, capacity, items = int(data[0]), int(data[1]), data[2:]
            log("\n\nDATASET {}: num_items {} capacity {} items_read {}".format(dataset["name"], num_items, capacity, len(items)))
        items = [Item(size=int(i)) for i in items]
        log("  Iteration", end=" ")
        # Perform 30 independent iterations.
        for iteration in range(1):
            log(iteration+1, end=" ")
            # Randomize the order of the items in the item list.
            shuffle(items)
            # Apply each heuristic to the list.
            for h in heuristic_list:
                start_time = datetime.now()
                # There is always at least one bin.
                bins = [Bin(capacity=capacity)]
                for item in items:
                    bins = h.apply(item, bins)
                execution_time = datetime.now() - start_time
                # Record the relevant data for analysis
                summary = {
                    "execution_time": str(execution_time),
                    "num_bins": len(bins),
                    "fitness": sum(b.fitness() for b in bins) / len(bins),
                }
                dataset["results"].setdefault(h.__name__, []).append(summary)
            for h in DecHeuristic_list:
                start_time = datetime.now()
                # There is always at least one bin.
                bins = [Bin(capacity=capacity)]
                item_sort = sorted (items, key=lambda x: x.size, reverse=True)
                for item in item_sort:
                    bins = h.apply(item, bins)
                execution_time = datetime.now() - start_time
                # Record the relevant data for analysis
                summary = {
                    "execution_time": str(execution_time),
                    "num_bins": len(bins),
                    "fitness": sum(b.fitness() for b in bins) / len(bins),
                }
                dataset["results"].setdefault(h.__name__, []).append(summary)
    # Write the captured data to disk.
    with open("results_low_level.json", "w") as file:
        file.write(json.dumps(datasets, indent=2))