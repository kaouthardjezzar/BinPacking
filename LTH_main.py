from tabu_search import TabuSearch
from item import Item
from random import shuffle
from datetime import datetime
import json
from LTH import LTH


def log(message, end=None):
    print(message, flush=True, end=end)


if __name__ == '__main__':
    datasets = [
    
     
        {"name": "HARD9.txt", "solution":56, "results": {}},
        {"name": "HARD0.txt", "solution":56, "results": {}},
        {"name": "HARD6.txt", "solution":57, "results": {}},
        {"name": "HARD7.txt", "solution":55, "results": {}},

        {"name": "N1C1W4_E.txt", "solution":35, "results": {}},
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
        log("  Iteration", end=" ")
        # Perform 30 independent iterations.
        for iteration in range(1):
            log(iteration+1, end=" ")
            # Randomize the order of the items in the item list.
            shuffle(items)
            thing = LTH(capacity, items)

            start_time = datetime.now()
            total_iterations, stagnation = thing.run()
            execution_time = datetime.now() - start_time
            execution_time_insec = execution_time.total_seconds()

            # Record the relevant data for analysis
            summary = {
                "execution_time": str(execution_time),
                "execution_time_in_seconds" : str(execution_time_insec),
                "num_bins": thing.best_solution.num_bins,
                "fitness": thing.best_solution.fitness,
                "iterations": total_iterations,
                "stagnation": stagnation,
                "combination": thing.best_solution.pattern,
            }
            dataset["results"].setdefault("LTH", []).append(summary)
    # Write the captured data to disk.
    with open("./results_LTH.json", "w") as file:
        file.write(json.dumps(datasets, indent=2))
