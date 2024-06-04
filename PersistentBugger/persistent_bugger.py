from math import prod

def persistence(num):
    """_Recursively multiply digits of a number until you get a single digit number_

    Args:
        num (_int_): _a positive parameter_
    Returns:
        count (__int__): _number of times you multiply the digits of mul to get single digit_
    """
    count = 0
    while num // 10 != 0:
        num = prod([int(x) for x in str(num)], start = 1)
        count += 1
    return count