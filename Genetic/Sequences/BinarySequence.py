import numpy as np
import string
import math
import random
from typing import Callable, List
from Sequences.Genotype import Genotype


class BinarySequence(Genotype):
    def __init__(self, binary_sequence: string):
        #testing required for valid generation
        assert isinstance(binary_sequence, str), 'binary sequence should be instance of sring'
        self.__sequence = binary_sequence
    def __str__(self):
        return 'Sequence: ' + self.__sequence + '\n phenotype: ' + str(self.get_phenotype())

    def __eq__(self, binary_sequence):
        return self.__sequence == binary_sequence.get_sequence() and self.__phenotype == binary_sequence.get_phenotype()

    # expression of the binary sequence
    def get_phenotype(self):
        return self.__phenotype

    # getters
    def get_sequence(self):
        return self.__sequence

    def get_phenotype(self):
        return self.__phenotype

    def get_length(self):
        return len(self.__sequence)

    # mutation and crossover
    def mutate(self, p):
        chr = [int(a) for a in list(self.__sequence)]
        arr = [np.random.choice([0, -1], p=[1 - p, p]) for x in chr]
        return BinarySequence(''.join([str(abs(x)) for x in np.add(chr, arr)]))

    def crossover(self, sequence, index):
        assert isinstance(sequence, BinarySequence)
        return [BinarySequence(self.__sequence[0:index] + sequence.get_sequence()[index:]),
                           BinarySequence(sequence.get_sequence()[0:index] + self.__sequence[index:])]
    @staticmethod
    def generate_random(len: int, phenotype: Callable):
        assert len != 0,'cant assign a binary sequence of length 0'
        return BinarySequence(str(bin(random.randint(0, 2 ** len - 1)))[2:].zfill(len))

    @staticmethod
    def calculate_length(boundry, percision):
        assert percision < 1 and percision > 0
        assert isinstance(boundry, tuple)
        assert boundry[1] > boundry[0]
        return math.ceil(math.log2((boundry[1] - boundry[0]) / percision + 1))

