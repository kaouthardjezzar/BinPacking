# coding=utf-8
#!/usr/bin/python
###############################################################################
# This script is the command that is executed every run.
# Check the examples in examples/
#
# This script is run in the execution directory (execDir, --exec-dir).
#
# PARAMETERS:
# argv[1] is the candidate configuration number
# argv[2] is the instance ID
# argv[3] is the seed
# argv[4] is the instance name
# The rest (argv[5:]) are parameters to the run
#
# RETURN VALUE:
# This script should print one numerical value: the cost that must be minimized.
# Exit with 0 if no error, with 1 in case of error
###############################################################################


import os.path
import re
import subprocess
import sys

sys.path.insert(1, 'C:\\Users\\kaout\\OneDrive\\Bureau\\BinPacking')


from tabu_search import TabuSearch
from item import Item
from random import shuffle
from datetime import datetime
import json

## This a dummy example that shows how to parse the parameters defined in
## parameters.txt and does not need to call any other software.

if __name__=='__main__':
    if len(sys.argv) < 5:
        print("\nUsage: ./target-runner.py <configuration_id> <instance_id> <seed> <instance_path_name> <list of parameters>\n")
        sys.exit(1)

    # Get the parameters as command line arguments.
    configuration_id = sys.argv[1]
    instance_id = sys.argv[2]
    seed = sys.argv[3]
    instance = sys.argv[4]
    cand_params = sys.argv[5:]

    # Default values (if any)
    MAX_COMBINATION_LENGTH = None
    MAX_ITERATIONS = None
    MAX_NO_CHANGE = None
    # Parse parameters

    with open(instance, 'r') as file:
        data = file.read().splitlines()
        num_items, capacity, items = int(data[0]), int(data[1]), data[2:]
    items = [Item(size=int(i)) for i in items]
    
    while cand_params:
        # Get and remove first and second elements.
        strr = cand_params.pop(0)
        strr = strr.split("=", 1)
        param = strr[0]
        value = strr[1]
        if param == "--MAX_COMBINATION_LENGTH":
            MAX_COMBINATION_LENGTH = int(value)
        if param == "--MAX_ITERATIONS":
            MAX_ITERATIONS = int(value)
        if param == "--MAX_NO_CHANGE":
            MAX_NO_CHANGE = int(value)
                              
    


    shuffle(items)
    thing = TabuSearch (capacity, items, MAX_COMBINATION_LENGTH , MAX_ITERATIONS ,MAX_NO_CHANGE)

    start_time = datetime.now()
    total_iterations, stagnation, combination = thing.run()
    execution_time = datetime.now() - start_time

    print(str(len(thing.bins)) + "\n")# retourner le cost vers Irace
   
    sys.exit(0)