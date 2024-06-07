from math import fsum

def get_sum(a, b):
    sum = 0
    a, b = min(a, b), max(a, b)
    for i in range(a, b+1):
        sum += i
    return sum

def get_sum_1(a, b):
    return fsum([x for x in range(min(a, b), max(a, b)+ 1)])

def get_sum_2(a, b):
    sum = 0
    for i in range(min(a, b),max(a, b)+1):
        sum += i
    return sum

def get_sum_3(a, b):
    sum = 0
    nums = [x for x in range(min(a, b), max(a, b)+1)]
    for num in nums:
        sum += num
    return sum

def get_sum_4(a, b):
    a, b = min(a, b), max(a, b)
    return fsum([x for x in range(a, b+1)])



def get_sum_6(a, b):
    a, b = min(a, b), max(a, b)
    nums = [x for x in range(a, b + 1)]
    return fsum(nums)

def get_sum_7(a,b):
    return sum(range(min(a, b), max(a, b) + 1))


