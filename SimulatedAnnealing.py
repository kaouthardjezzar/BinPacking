from heuristics import FirstFit
import numpy as np
from item import Item
from bin import Bin
import copy

class SA(object):
    def __init__(self,alpha,capacity, items,t_init,t_target,iter_nb):
        self.alpha = alpha
        self.items = items
        self.capacity = capacity
        self.bins = [Bin(capacity)]
        self.t_init = t_init
        self.t_target = t_target
        self.iter_nb = iter_nb


    def run_for_hrh(self,bins):
        self.bins = copy.deepcopy(bins)
        # Initialize temperature
        t = self.t_init
        # Average to temprature to separate 
        t_average = (self.t_init + self.t_target) / 2
        # iterate
        while t > self.t_target:
            for i in range(self.iter_nb):
                if t > t_average:
                    neighbour = self._get_neighbour_01()
                else:
                    neighbour = self._get_neighbour_11()
                delta = self._objective_function(neighbour) - self._objective_function(self.bins)
                if delta > 0:
                    self.bins = copy.deepcopy(neighbour)
                else:
                    u = np.random.random()
                    if (u < np.exp(delta/t)):
                        self.bins = copy.deepcopy(neighbour)
            t = self.alpha * t


    def run(self):
        # Initial solution generated with first fit method
        for item in self.items:
            self.bins = FirstFit.apply(item, self.bins)
        # Initialize temperature
        t = self.t_init
        # Average to temprature to separate 
        t_average = (self.t_init + self.t_target) / 2
        # iterate
        while t > self.t_target:
            for i in range(self.iter_nb):
                if t > t_average:
                    neighbour = self._get_neighbour_01()
                else:
                    neighbour = self._get_neighbour_11()
                delta = self._objective_function(neighbour) - self._objective_function(self.bins)
                if delta > 0:
                    self.bins = copy.deepcopy(neighbour)
                else:
                    u = np.random.random()
                    if (u < np.exp(delta/t)):
                        self.bins = copy.deepcopy(neighbour)
            t = self.alpha * t


    # move a random element from a random bin and to another random bin 
    def _get_neighbour_01(self):
        neighbour = copy.deepcopy(self.bins)
        b_index = np.random.randint(low=0,high=len(neighbour))
        bin_to_remove_from = neighbour[b_index]
        i_index = np.random.randint(low=0,high=len(bin_to_remove_from.items))
        item_to_move = bin_to_remove_from.items[i_index]
        del bin_to_remove_from.items[i_index]
        neighbour[b_index] = bin_to_remove_from
        while True:
            bin = neighbour[np.random.randint(low=0,high=len(neighbour))]
            if bin.can_add_item(item_to_move):
                bin.add_item(item_to_move)
                break
        if len(bin_to_remove_from.items) == 0:
            del neighbour[b_index]
        return neighbour

    # swap two random elements from two random bins
    def _get_neighbour_11(self):
        neighbour = copy.deepcopy(self.bins)
        while True:
            b_index1, b_index2 = np.random.randint(low=0,high=len(self.bins),size=2)
            bin1 = neighbour[b_index1]
            bin2 = neighbour[b_index2]
            i_index1 = np.random.randint(low=0,high=len(bin1.items))
            i_index2 = np.random.randint(low=0,high=len(bin2.items))
            item1 = bin1.items[i_index1] 
            item2 = bin2.items[i_index2] 
            if (bin1.filled_space() - item1.size + item2.size <= self.capacity) and (bin2.filled_space() - item2.size + item1.size <= self.capacity) :
                break
        bin1.items[i_index1] = item2
        bin2.items[i_index2] = item1
        neighbour[b_index1] = bin1
        neighbour[b_index2] = bin2
        return neighbour

    def _objective_function(self,bins):
        S = 0
        for bin in bins:
            s = 0
            for item in bin.items:
                s += item.size
            S = ( S + s ** 2 ) / self.capacity
        return S



# test neighbour functions
'''
items = [Item(10),Item(10),Item(1),Item(2)]
sa = SA(0.9,12,items)
sa.run()
neighbour = sa._get_neighbour_11()
print("===Original===")
for bin in sa.bins:
    print(bin)
print("===Neighbour===")
for bin in neighbour:
    print(bin)
'''