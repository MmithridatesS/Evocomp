from typing import List
from copy import deepcopy
import random
from Sequences.Genotype import Genotype
from Utilities import Tools

class Chromosome(Genotype):
    def __init__(self, chromosome:List, instance_count:int) -> None:
        self.__chromosome = chromosome
        self.__instanceCount = instance_count
        pass
    def mutate(self,maxnum):
        chrom = deepcopy(self.__chromosome)
        assert maxnum > 1, 'Negative mutations not expected'
        assert maxnum <= self.__tsGrid.get_instancesCount()-1, 'More mutations than instances'
        elems = random.sample(self.__chromosome,k=maxnum)
        elemarg = sorted([self.__chromosome.index(x) for x in elems])
        for i in range(len(elems)):
            chrom[elemarg[i]] = elems[i]
        return chrom
    def crossover(chromosome1,chromosome2,idx):
        assert len(chromosome1) == len(chromosome2), 'chromosoes of the same length expected'
        res = []
        ch = chromosome1[:idx]
        chr = deepcopy(chromosome2)
        for i in range(len(ch)):
            chr.remove(ch[i])
        res.append(ch + chr)
        ch = chromosome1[idx:]
        chr = deepcopy(chromosome2)
        for i in range(len(ch)):
            chr.remove(ch[i])
        res.append(chr+ch)
        ch = chromosome2[:idx]
        chr = deepcopy(chromosome1)
        for i in range(len(ch)):
            chr.remove(ch[i])
        res.append(ch + chr)
        ch = chromosome2[idx:]
        chr = deepcopy(chromosome1)
        for i in range(len(ch)):
            chr.remove(ch[i])
        res.append(chr+ch)
        return res
    def random_instance(self,ln):
        res ={}
        for i in range(ln):
            chr: Chromosome = Chromosome(random.sample(self.__chromosome,self.__instanceCount),self.__instanceCount)
            res[chr] = chr.fitness_score()
        return res
    def fitness_score(self):
        sum = 0
        for i in range(len(self.__chromosome)-1):
            sum = sum + Tools.euclidean_distance(self.__chromosome[i],self.__chromosome[i+1])
        return sum

    def get_instancesCount(self):
        return self.__instanceCount
    def get_instance(self):
        return self.__chromosome
