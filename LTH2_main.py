from tabu_search import TabuSearch
from item import Item
from random import shuffle
from datetime import datetime
import json
from LTH2 import LTH2


def log(message, end=None):
    print(message, flush=True, end=end)


if __name__ == '__main__':
    datasets = [
         {"name": "N1C1W4_E.txt", "results": {}},
      
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
        for iteration in range(1):
            log(iteration+1, end=" ")
            # Randomize the order of the items in the item list.
            shuffle(items)
            thing = LTH2(capacity, items)

            start_time = datetime.now()
            total_iterations, stagnation = thing.run()
            execution_time = datetime.now() - start_time

            # Record the relevant data for analysis
            summary = {
                "execution_time": str(execution_time),
                "num_bins": thing.best_solution.num_bins,
                "fitness": thing.best_solution.fitness,
                "iterations": total_iterations,
                "stagnation": stagnation,
                "combination": thing.best_solution.pattern,
            }
            dataset["results"].setdefault("LTH2", []).append(summary)
    # Write the captured data to disk.
    with open("./results_LTH2.json", "w") as file:
        file.write(json.dumps(datasets, indent=2))
