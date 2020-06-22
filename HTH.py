from genetic_algorithm_elite import GeneticAlgorithm
import math
import threading
from queue import Queue
import random
import time
from datetime import datetime


exchange_locks = []
threads=[]
random.seed(0)
jobs_done=0
best_solutions = []

class myThread (threading.Thread):
   def __init__(self, threadID,ga,Queue=None,Lock=None,name="Thread"):
      threading.Thread.__init__(self)
      #print("started ", name)
      self.threadID = threadID
      self.ga = ga
      self.lock=Lock
      self.queue = Queue
      self.name = name
   def run(self,iterations=1):
      global jobs_done
      # while running add here some Locks to synchronize threads
      for i in range(iterations):
        #print("iteration ",i," thread  ", self.threadID)
        start_time = datetime.now()
        self.ga.run()
        execution_time = datetime.now() - start_time
        best_solutions.append((self.ga.best_solution,execution_time))
        self.ga.shuffle()
        #print("done with that...")
        if i < iterations-1:
           #print("migrating...")
           self.migrate(random.randint(0,len(threads)-1))
      #print(self.name, "done")
      jobs_done+=1
        
      
   def send_to_thread(self,thread,data):
      thread.lock.acquire()
      thread.queue.put(data)
      thread.lock.release()

   def migrate(self,thread_num):
      thread_to_receive = threads[thread_num]
      if thread_to_receive == self:
         thread_to_receive = threads[(thread_num + 1) % len(threads)]
      
      mask = [random.random() >= 0.5 for i in self.ga.population]
      members_to_migrate=[self.ga.population[i] for i in range(len(self.ga.population)) if mask[i] ]
      for p in members_to_migrate:
         self.ga.population.remove(p)
      ts = int(datetime.now().timestamp())
      #print("best solution in population :",ts,members_to_migrate in self.ga.population)
      self.ga.update_individuals(self.ga.population)
      #print("migrating :",self,members_to_migrate)
      self.send_to_thread(thread_to_receive,\
         members_to_migrate)
      time.sleep(0.01)
      self.lock.acquire()
      while not self.queue.empty():
         #print("receiving data")
         new_population_member= self.queue.get()
         self.ga.population+=new_population_member
         self.ga.update_individuals(self.ga.population)
         #print("recieving : ",self,new_population_member)
      self.lock.release()



class HTH:
   
   def __init__(self, capacity, items,nbislands,popsize,maxgen,maxnoch,toursize,mutrt,crossvort):
      """
      Creates an instance that can run the tabu search algorithm .
      :param capacity: The capacity of a bin.
      :param items: The items that have to be packed in bins.
      """
      self.bin_capacity = capacity
      self.items = items
      self.NUMBER_OF_ISLANDS = nbislands
      self.POPULATION_SIZE = popsize
      self.MAX_GENERATIONS = maxgen
      self.MAX_NO_CHANGE = maxnoch
      self.TOURNAMENT_SIZE = toursize
      self.MUTATION_RATE = mutrt
      self.CROSSOVER_RATE = crossvort
          

   def run(self):
      global threads, jobs_done
      #divide the population into islands
      ga = GeneticAlgorithm(self.bin_capacity, self.items,self.POPULATION_SIZE)
      population = ga.population
      N = len(population)
      ITEM_PER_ISLAND=int(math.ceil(N/self.NUMBER_OF_ISLANDS))
      func = lambda i: int((i + 1) * ITEM_PER_ISLAND) if (i + 1) * ITEM_PER_ISLAND < N else N
      islands = [GeneticAlgorithm(self.bin_capacity, self.items,ITEM_PER_ISLAND,self.MAX_GENERATIONS ,self.MAX_NO_CHANGE,self.TOURNAMENT_SIZE,self.MUTATION_RATE + random.randint(0,9) * 0.01 * [-1,1][random.randrange(2)],self.CROSSOVER_RATE + random.randint(0,3) * 0.1 * [-1,1][random.randrange(2)] + random.randint(0,9) * 0.01 * [-1,1][random.randrange(2)],population=population[i*ITEM_PER_ISLAND: func(i)]) for i in range(self.NUMBER_OF_ISLANDS)]

      #log some information
      #print("\nnumber of islands ", len(islands))
      #print("size of the population ",len(population))
      
      #executing the algorithm
      for i in range(self.NUMBER_OF_ISLANDS):
         #creating the islands
         ga = islands[i]
         q = Queue()
         l=threading.Lock()
         name = "Thread-" + str(int(datetime.now().timestamp()))
         t = myThread(i,ga,Queue=q,Lock=l,name=name)
         threads.append(t)
         t.start()

      #print("waiting fot the threads .......")
      while jobs_done < self.NUMBER_OF_ISLANDS:
         time.sleep(0.01)
      #print("we have ",len(threads), " threads") 
      for index,t in enumerate(threads):
         #print("dealing with thread:",index)
         t.join()    
         #best_solutions.append((index,t.ga.best_solution.generate_solution(self.items)))   
         #print("solution in island ",index,t.name, t.ga.best_solution in islands[i].population)
      del threads[:]
      threads=[]
      jobs_done=0
      #print("we have ",len(threads), " threads")
      return best_solutions




