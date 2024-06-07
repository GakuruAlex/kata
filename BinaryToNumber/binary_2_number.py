from math import fsum
from memory_profiler import profile


def binary_array_to_number_2(arr):
    arr.reverse()
    return sum([x * pow(2, i) for i, x in enumerate(arr)])


def binary_array_to_number(arr):
    sum = 0
    arr.reverse()
    for i,x in enumerate(arr):
        sum +=  x * pow(2, i)
    return sum


def binary_array_to_number_3(arr):
    arr.reverse()
    return fsum([m * pow(2, n) for n, m in enumerate(arr)])