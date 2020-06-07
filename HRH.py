from genetic_algorithm import GeneticAlgorithm
from tabu_search import TabuSearch

class HRH:
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

        result2 = TabuSearch(self.bin_capacity, self.items)
        total_iterationsTB, stagnationTB, combinationTB = result2.run2(result1)

        return result1,result2,total_iterationsAG, stagnationAG, total_iterationsTB, stagnationTB, combinationTB

