from pickletools import genops
from Sequences.BinarySequence import BinarySequence
from Sequences.Genotype import Genotype
from Sequences.RealCoded import RealCoded
from Utilities.Probability import Probability
from Utilities.Tools import Utilities
from Utilities.Selection import Selection
import random
from typing import Callable, List

type_list = ['binarycoded', 'realcoded']

class Population:
    def __init__(self,type,space: List[Genotype] = [], goal = 'maxima', phenofunc = lambda x: int(x, base=2) ):
        self.__space = space
        self.__goal = goal
        self.__phenofunc = phenofunc
        try: 
            type_list[type]
        except KeyError: 
            raise ValueError('given type name is not valid')
    def __str__(self):
        return 'Sequence space: ' + str([x.get_sequence() for x in self.__space])

    
    
    def __sub__(self, population):
        if isinstance(population, Population):
            cs = self.__space
            ps = population.get_space()
            for i in range(len(ps)):
                cs.remove(ps[i])
            return Population(cs)
        if isinstance(population, Genotype): 
            self.__space.remove(population)
            return self
    #should be tested manually
    def __add__(self, population):
        if isinstance(population, Population):
            return Population(self.__space + population.get_space())
        if isinstance(population, Genotype):
            self.__space.append(population)
            return self
    def get_space(self):
        return self.__space

    def get_length(self):
        if len(self.__space) != 0:
            return len(self.__space[0].get_sequence())

    # mutation and crossover on a population
    def mutate(self, probability: float):
        return Population([x.mutate(probability) for x in self.__space])

    def crossover(self, probability: float, randfunc):
        seed = Utilities.listsplit(random.sample(self.__space,len(self.__space)), 2)
        crossover_population = Population()
        for i in range(len(seed)):
            if len(seed[i]) != 2:
                crossover_population = crossover_population + Population(seed[i])
            else:
                if Probability.static_pick(probability):
                    crossover_population = crossover_population + seed[i][0].crossover(seed[i][1], randfunc())
        return crossover_population

    @staticmethod
    def generate(len, goal, phenotype):
        
        #real should be added 
        
        
        
        pass
    
    
    
    def select(self, method, goal): 
        methods = {
            'roulette_wheel': Selection.roulette_wheel,
            'roulette_wheel_stochastic_remainder': Selection.roulette_wheel_stochastic_remainder,
            'tournaument' : Selection.tournaument
        }
        s = Selection(self.__space, goal)
        print(s)
        try:
            return Population(methods[method](s))
        except KeyError:
            raise ValueError('invalid selection method')
        
        



