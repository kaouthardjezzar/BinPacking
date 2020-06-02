from tabu_search import TabuSearch
from item import Item
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
      
    ]

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
        for iteration in range(2):
            log(iteration+1, end=" ")
            # Randomize the order of the items in the item list.
            shuffle(items)
            thing = TabuSearch(capacity, items)

            start_time = datetime.now()
            total_iterations, stagnation, combination = thing.run()
            execution_time = datetime.now() - start_time

            # Record the relevant data for analysis
            summary = {
                "execution_time": str(execution_time),
                "num_bins": len(thing.bins),
                "fitness": sum(b.fitness() for b in thing.bins) / len(thing.bins),
                "iterations": total_iterations,
                "stagnation": stagnation,
                "combination": combination,
                "tabu_list": list(thing.tabu_list)
            }
            dataset["results"].setdefault("TabuSearch", []).append(summary)
    # Write the captured data to disk.
    with open("results_tabu_search.json", "w") as file:
        file.write(json.dumps(datasets, indent=2))
