from genetic_algorithm import GeneticAlgorithm
import math



class HTH:
    NUMBER_OF_ISLANDS=3
    POPULATION_SIZE = 100
    def __init__(self, capacity, items):
        """
        Creates an instance that can run the tabu search algorithm .
        :param capacity: The capacity of a bin.
        :param items: The items that have to be packed in bins.
        """
        self.bin_capacity = capacity
        self.items = items

    def run(self):
        #divide the population
        ga = GeneticAlgorithm(self.bin_capacity, self.items,self.POPULATION_SIZE)
        population = ga.population
        N = len(population)
        ITEM_PER_ISLAND=int(math.ceil(N/self.NUMBER_OF_ISLANDS))
        func = lambda i: int((i + 1) * ITEM_PER_ISLAND) if (i + 1) * ITEM_PER_ISLAND < N else N
        islands = [population[i*ITEM_PER_ISLAND: func(i)] for i in range(self.NUMBER_OF_ISLANDS)]
        print("number of islands ", len(islands))
        print("size of the population ",len(population))
        for i in range(self.NUMBER_OF_ISLANDS):
            ga = GeneticAlgorithm(self.bin_capacity, self.items,population_size=ITEM_PER_ISLAND,population=islands[i])
            total_iterationsAG, stagnationAG = ga.run()
            #print("island {}".format(i),ga.best_solution.generate_solution(self.items) )
            print("solution in island ", ga.best_solution in islands[i])
        return "done"




