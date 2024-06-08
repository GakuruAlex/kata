def is_valid_walk(walk):
    """_Determine whether a given path is valid_

    Args:
        walk (_list_): _Parameter for suggested walk path_

    Returns:
        _bool_: _True or False based on path validity_
    """
    walks_count = {}
    opposites ={"n":"s","s":"n","e":"w","w":"e"}
    if len(walk) != 10:
        return False
    else:
        poss_walks = set(walk)
        if len(poss_walks) % 2 != 0:
            return False
        else:
            for w in poss_walks:
                walks_count[w] = walk.count(w)
            for w in walks_count.keys():
                try:
                    if walks_count[w] == walks_count[opposites[w]]:
                        return True
                    else:
                        return False
                except KeyError:
                    return False