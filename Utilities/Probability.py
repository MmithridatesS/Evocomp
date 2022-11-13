from operator import truediv
from timeit import timeit
from typing import List
import random
from xmlrpc.client import Boolean
from Utilities.Tools import Utilities



class Probability:
    def __init__(self, samplespace: List, uniform = False):
        assert isinstance(samplespace, List), 'expected type: List as samplespace'
        if uniform:
            p = 1/len(samplespace)
            self._samplespace = [(i, p) for i in samplespace]
        else:
            self._samplespace = sorted(samplespace, key=lambda x: x[1], reverse=True)

        self._accprobability = Utilities.accumulate(list(zip(*self._samplespace))[1])
    
    
    def __str__(self):
        return f'sample space: {self._samplespace} \naccumulate probability: {self._accprobability}'
    
    def get_samplespace(self):
        return self._samplespace

    def pick(self, with_probability = False):
        idx, r = [0], random.uniform(0,1)
        for i in range(len(self._samplespace)):
            if self._accprobability[i]>r: 
                idx[0] = i
                break
        if with_probability:
            return self._samplespace[idx[0]]
        else: 
            return self._samplespace[idx[0]][0]
            
    @staticmethod
    def static_pick(p: float) -> Boolean:
        if random.uniform(0,1) <= p:
            return True
        return False
    
    @staticmethod
    def get_space(sample: List, p: float, method: str) :
        l = len(sample)
        assert l>0, 'given list contains no items'
        if method == 'recursive':
            recursive_array = []
            for i in range(l - 1):
                recursive_array.append(((1 - p) ** i) * p)
            recursive_array.append((1 - p) ** (l - 1))
        return Probability(list(zip(sample, recursive_array)))
        

    @staticmethod
    def recprob_toss(p: float, l: int) -> List[Boolean]:
        assert (p < 1 and p > 0), 'p between 0 and 1 expected'
        assert l > 0, 'cant have a list with negative or zero items'
        if l == 1:
            return [True]
        res = []
        for i in range(l - 1):
            res.append(Probability.pick(((1 - p) ** i) * p))
        res.append(Probability.pick((1 - p) ** (l - 1)))
        return res        
    
    @staticmethod
    def get_relativeaccumulate(lst) -> List:   
        return Utilities.accumulate([x/sum(lst) for x in lst])
    
    @staticmethod
    def get_relative(lst):
        return [x/sum(lst) for x in lst]