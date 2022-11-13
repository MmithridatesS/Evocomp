import timeit
from typing import Callable, List
import math


class Utilities:
    @staticmethod
    
    
    def time(fun: Callable):
        def wrapper():
            s = timeit.timeit()
            fun()
            e = timeit.timeit()
            print(e - s)
        return wrapper

    @staticmethod
    # makes zero matrix of k rows and l columns
    def zeros(k, l):
        res = []
        for i in range(k):
            res.append([])
            for j in range(l):
                res[i].append(0)
        return res

    @staticmethod  # function to calculate euclidean distance between p1 and p2
    def euclidean_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    @staticmethod
    def listsplit(l: List, n: int) -> List:
        lst = []
        i = 0
        while len(l) - i > n:
            lst.append(l[i:i + n])
            i = i + n
        lst.append(l[i:])
        return lst
    @staticmethod
    def accumulate(lst):
        acc = 0
        ls = []
        for i in range(len(lst)):
            ls.append(round(acc+lst[i], 3))
            acc += lst[i]
        return ls


