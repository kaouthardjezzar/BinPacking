from genetic_algorithm import GeneticAlgorithm
from SimulatedAnnealing import SA

class HRH_RS:
    def __init__(self , capacity, items,POPULATION_SIZE = 50,MAX_GENERATIONS = 250,MAX_NO_CHANGE = 50 ,TOURNAMENT_SIZE = 20 ,MUTATION_RATE = 0.3 ,CROSSOVER_RATE = 0.6, alpha = 0.5,t_init = 500 ,t_target = 5,iter_nb = 10):
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
        self.CROSSOVER_RATE = CROSSOVER_RATE

        self.alpha = alpha
        self.t_init = t_init
        self.t_target = t_target
        self.iter_nb = iter_nb

        self.bin_capacity = capacity
        self.items = items

    def run(self):
        result1 = GeneticAlgorithm(self.bin_capacity, self.items, self.POPULATION_SIZE,self.MAX_GENERATIONS,self.MAX_NO_CHANGE,self.TOURNAMENT_SIZE,self.MUTATION_RATE,self.CROSSOVER_RATE)
        total_iterationsAG, stagnationAG = result1.run()

        sa = SA(self.alpha,self.bin_capacity, self.items,self.t_init, self.t_target, self.iter_nb)
        sa.run_for_hrh(result1.best_solution.generate_solution(self.items))

        return sa

