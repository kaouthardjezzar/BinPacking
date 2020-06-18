from genetic_algorithm import GeneticAlgorithm
import math
import threading

class myThread (threading.Thread):
   def __init__(self, threadID,ga):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.ga = ga
   def run(self):
      self.ga.run()
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
        #divide the population into islands
        ga = GeneticAlgorithm(self.bin_capacity, self.items,self.POPULATION_SIZE)
        population = ga.population
        N = len(population)
        ITEM_PER_ISLAND=int(math.ceil(N/self.NUMBER_OF_ISLANDS))
        func = lambda i: int((i + 1) * ITEM_PER_ISLAND) if (i + 1) * ITEM_PER_ISLAND < N else N
        islands = [GeneticAlgorithm(self.bin_capacity, self.items,POPULATION_SIZE=ITEM_PER_ISLAND,population=population[i*ITEM_PER_ISLAND: func(i)]) for i in range(self.NUMBER_OF_ISLANDS)]

        #log some information
        print("\nnumber of islands ", len(islands))
        print("size of the population ",len(population))

        best_solutions=[]
        threads=[]
        #executing the algorithm
        for i in range(self.NUMBER_OF_ISLANDS):
            #creating the islands
            ga = islands[i]
            t = myThread(i,ga)
            threads.append(t)
            t.start()

        print("waiting fot the threads .......")
        for t in threads:
            t.join()    
            best_solutions.append(t.ga.best_solution.generate_solution(self.items))   
            print("solution in island ", t.ga.best_solution in islands[i].population)
        return best_solutions




