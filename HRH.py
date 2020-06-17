from genetic_algorithm import GeneticAlgorithm
from tabu_search import TabuSearch


class HRH:
    def __init__(self, capacity, items,POPULATION_SIZE = 50,MAX_GENERATIONS = 250,MAX_NO_CHANGE = 50 ,TOURNAMENT_SIZE = 20 ,MUTATION_RATE = 0.3 ,CROSSOVER_RATE = 0.6):
        """
        Creates an instance that can run the tabu search algorithm .
        :param capacity: The capacity of a bin.
        :param items: The items that have to be packed in bins.
        """
        self.POPULATION_SIZE = POPULATION_SIZE
        self.MAX_GENERATIONS = MAX_GENERATIONS
        self.MAX_NO_CHANGE = MAX_NO_CHANGE
        self.TOURNAMENT_SIZE = TOURNAMENT_SIZE
        self.MUTATION_RATE = MUTATION_RATE
        self.CROSSOVER_RATE = CROSSOVER_RAT
        self.bin_capacity = capacity
        self.items = items

    def run(self):
        result1 = GeneticAlgorithm(self.bin_capacity, self.items,self.POPULATION_SIZE,self.MAX_GENERATIONS,self.MAX_NO_CHANGE,self.TOURNAMENT_SIZE,self.MUTATION_RATE,self.CROSSOVER_RATE)
        total_iterationsAG, stagnationAG = result1.run()

        result2 = TabuSearch(self.bin_capacity, self.items)
        total_iterationsTB, stagnationTB, combinationTB = result2.run2(result1)

        return result1,result2,total_iterationsAG, stagnationAG, total_iterationsTB, stagnationTB, combinationTB

