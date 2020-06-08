from SimulatedAnnealing import SA
from HRH_AG_RS import HRH_RS
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
        for iteration in range(2):
            log(iteration+1, end=" ")
            # Randomize the order of the items in the item list.
            shuffle(items)
            thing = HRH_RS(capacity, items)
            start_time = datetime.now()
            sa = thing.run()
            execution_time = datetime.now() - start_time

            # Record the relevant data for analysis
            summary = {
                "execution_time": str(execution_time),
                "num_bins": len(sa.bins),
            }
            dataset["results"].setdefault("HRH_RS", []).append(summary)
            #dataset["results"].setdefault("SA", []).append(summary)
    # Write the captured data to disk.
    with open("./HRH_RS.json", "w") as file:
        file.write(json.dumps(datasets, indent=2))
