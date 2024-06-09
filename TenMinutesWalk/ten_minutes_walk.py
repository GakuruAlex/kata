def is_valid_walk(walk):
    """_Determine whether a given path is valid_

    Args:
        walk (_list_): _Parameter for suggested walk path_

    Returns:
        _bool_: _True or False based on path validity_
    """
    walks_count = {}
    bool_walks = []
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
                        bool_walks.append(True)
                    else:
                        bool_walks.append(False)
                except KeyError:
                    return False
            return False not in bool_walks
        

#optimal soln
def is_valid_walk_soln(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
