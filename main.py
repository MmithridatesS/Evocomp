from typing import List
import numpy as np
import random
from Utilities.Probability import Probability
from Utilities.Tools import Utilities
from Utilities.Selection import Selection
from Sequences.Chromosome import Chromosome
from Sequences.BinarySequence import BinarySequence

import math


class TS:
    __instances: List = []
    __instancesCount: int = 0

    def __init__(self, grid_size):
        if grid_size < 1:
            raise ValueError('grid size negative...')
        self.__grid = np.zeros((grid_size, grid_size))
        self.__gridSize = grid_size

    def generate(self, num):
        # assert num > grid
        if (num > self.__gridSize ** 2):
            raise ValueError('Entring number is more than the capacity of the grid')

        self.__instancesCount = num
        self.__instances = list(
            zip(random.sample(range(self.__gridSize), num), random.sample(range(self.__gridSize), num)))
        for x in range(len(self.__instances)):
            self.__grid[self.__instances[x][0]][self.__instances[x][1]] = 1

    def get_grid(self):
        return self.__grid

    def get_instances(self):
        return self.__instances

    def get_instancescount(self):
        return self.__instancesCount


class Simulation:
    def __init__(self, board: TS, iterations: int, numchr: int, **kwargs):
        self.__method = kwargs['method']
        self.__iterations = iterations
        self.__numchr = numchr
        self.__grid = board.get_grid()
        self.__initialchromosome = Chromosome(board.get_instances(), board.get_instancesCount())
        self.__activeChromosomes = self.__initialchromosome.random_instance(self.__numchr)
        self.__state: dict = {
            'initialRoute': self.__initialchromosome,
            'bestRoute': self.__initialchromosome,
            'initialDistance': "%0.5f" % self.__initialchromosome.fitness_score(),
            'bestDistance': float("%0.5f" % min(self.__activeChromosomes.values())),
            'worstDistance': float("%0.5f" % max(self.__activeChromosomes.values())),
            'fitnessScoreSum': sum(self.__activeChromosomes.values())
        }

    def process(self):

        # Selection:

        # crossover

        # mutation

        # fitness ranking

        pass

    def selection_prob(self):
        p_bv = {}
        if self.__method == 1:
            for key, value in self.__activeChromosomes.items():
                if (Probability.toss_uniform(1 - (value / self.__state['fitnessScoreSum']))):
                    p_bv[key] = value
            return p_bv

        elif self.__method == 2:
            for key, value in self.__activeChromosomes.items():
                print(value, self.__state['worstDistance'])
                if (Probability.toss_uniform(1 - ((self.__state['worstDistance'] - value) / self.__state['worstDistance']))):
                    p_bv[key] = value
            return p_bv

    def get_activechromosomes(self):
        return self.__activeChromosomes

    def get_state(self):
        print(self.__state)


def main():
    p = Probability(['a','b','c'], True)
    print(p.pick())

if __name__ == "__main__":
    main()
