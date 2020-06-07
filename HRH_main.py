from HRH import HRH
from item import Item
from random import shuffle
from datetime import datetime
import json


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
        for iteration in range(4):
            log(iteration+1, end=" ")
            # Randomize the order of the items in the item list.
            shuffle(items)
            thing = HRH(capacity, items)
            start_time = datetime.now()
            result1, result2, total_iterationsAG, stagnationAG, total_iterationsTB, stagnationTB, combinationTB = thing.run()
            execution_time = datetime.now() - start_time
            # Record the relevant data for analysis
            print(result1.best_solution.num_bins,len(result2.bins))
            summary = {
                "execution_time": str(execution_time),
                "num_bins": len(result2.bins),
            }
            dataset["results"].setdefault("HRH", []).append(summary)
    # Write the captured data to disk.
    with open("results_HRH_search.json", "w") as file:
        file.write(json.dumps(datasets, indent=2))
