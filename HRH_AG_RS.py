from genetic_algorithm import GeneticAlgorithm
from tabu_search import TabuSearch
from SimulatedAnnealing import SA

class HRH_RS:
    def __init__(self, capacity, items):
        """
        Creates an instance that can run the tabu search algorithm .
        :param capacity: The capacity of a bin.
        :param items: The items that have to be packed in bins.
        """
        self.bin_capacity = capacity
        self.items = items

    def run(self):
        result1 = GeneticAlgorithm(self.bin_capacity, self.items)
        total_iterationsAG, stagnationAG = result1.run()

        sa = SA(0.9,self.bin_capacity, self.items,100,10,10)
        sa.run_for_hrh(result1.best_solution.generate_solution)

        return sa

