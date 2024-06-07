def count_bits(n):
    """_Calculate the number of bits that are equal to one in the binary representation of a number_

    Args:
        n (_int_): _parameter_

    Returns:
        _int_: _number of bits equal to one_
    """
    return bin(n).count("1")