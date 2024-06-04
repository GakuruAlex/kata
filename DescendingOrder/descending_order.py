def descending_order(number):
    """_Rearrange digits of a non negative number in descending order_

    Args:
        number (_int_): _A non negative integer_
        
    Returns:
        number (_int__): _Highest possible number__
    
    """
    number = list(str(number))
    number.sort(reverse=True)
    number = int("".join([num for num in number]))
    return number