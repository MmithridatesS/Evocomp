from itertools import accumulate
from math import floor
from os import popen
from typing import Callable, List
from Sequences.Genotype import Genotype
from Utilities.Probability import Probability
from Sequences.BinarySequence import BinarySequence


class Selection(Probability):
    def __init__(self,space: List, phenotype: Callable, goal: str):
        assert isinstance(space, List[Genotype]), 'the given list should contain pairs' 
        super().__init__(Selection.get_sample(space, phenotype, goal))
    
    @staticmethod
    def get_sample(genelist,phenotype, goal):
        if goal == 'maxima':
            probratio = Probability.get_relative([phenotype(x) for x in genelist])
        elif goal == 'minima':
            probratio = Probability.get_relative([1/phenotype(x) for x in genelist])
        return zip(genelist, probratio)
    
    
    
    def roulette_wheel(self) -> List:
        res = []
        for i in range(len(self.__genotype)):
            res.append(self.pick()[0])    
        return res
        
    def roulette_wheel_stochastic_remainder(self)-> List:   
        space, prob = zip(*self._samplespace)
        res = []
        length = len(self._samplespace)
        pop = [floor(p*length) for p in prob]
        for i in range(length):
            for j in range(pop[i]):
                res.append(self._samplespace[i])       
        if len(res) < len:
            for i in range(length - len(res)):
                res.append(self.pick(True))
        if len(res) > length:
            for i in range(len(res) - length):
                res.remove(min(res, key = lambda x : x[1]) )

    
    def accratio(self):
        accumulateiveratio = Probability.get_relativeaccumulate([self.__phenotype(x) for x in self.__genotype], self.__goal)
        sample = Probability(zip(self.__genotype, accumulateiveratio))
        


    def tournaument():
        pass
