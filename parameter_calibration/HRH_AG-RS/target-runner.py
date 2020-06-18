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
import numpy as np

sys.path.insert(1, 'C:\\Users\\kaout\\OneDrive\\Bureau\\BinPacking')

from HRH_AG_RS import HRH_RS
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
    POPULATION_SIZE = None 
    MAX_GENERATIONS = None
    MAX_NO_CHANGE = None
    TOURNAMENT_SIZE = None
    MUTATION_RATE = None
    CROSSOVER_RATE = None
    
    ALPHA = None 
    T0 = None
    T_TARGET = None
    NB_ITER = None
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
        if param == "--POPULATION_SIZE":
            POPULATION_SIZE = int(value)
        if param == "--MAX_GENERATIONS":
            MAX_GENERATIONS = int(value)
        if param == "--MAX_NO_CHANGE":
            MAX_NO_CHANGE = int(value)
        if param == "--TOURNAMENT_SIZE":
            TOURNAMENT_SIZE = int(value)
        if param == "--MUTATION_RATE":
            MUTATION_RATE = float(value)
        if param == "--CROSSOVER_RATE":
            CROSSOVER_RATE = float(value)
        if param == "--ALPHA":
            ALPHA = float(value)
        if param == "--T0":
            T0 = int(value)
        if param == "--T_TARGET":
            T_TARGET = int(value)
        if param == "--NB_ITER":
            NB_ITER = int(value)                       
    


    shuffle(items)
    thing = HRH_RS(capacity, items, POPULATION_SIZE ,MAX_GENERATIONS,MAX_NO_CHANGE ,TOURNAMENT_SIZE ,MUTATION_RATE,CROSSOVER_RATE , ALPHA, T0, T_TARGET, NB_ITER)
    start_time = datetime.now()
    sa = thing.run()
    execution_time = datetime.now() - start_time

    print(str(len(sa.bins)) + "\n")# retourner le cost vers Irace
   
    sys.exit(0)