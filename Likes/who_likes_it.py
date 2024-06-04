
def likes(names):
    """_Displays a text for likes a particular post. Using if elif block_

    Args:
        names (_list_): _names of people who like a post_
    Returns:
        string of text to display
    """
    length = len(names)
    if not names:
        return(f"no one likes this")
    else:
        if length == 1:
            return(f"{names[0]} likes this")
        elif length == 2:
            return(f"{' and '.join(names)} like this")
        elif length == 3:
            return(f"{names[0]},{' and '.join(names[1:3])} like this")
        else:
            return(f"{names[0]},{names[1]} and {length - 2} others like this")



def dict_likes(names):
    """_Display likes text given a list of people who liked a post using dictionary and format_

    Args:
        names (_list_): _names of people who like a post_
    Returns:
        a text to display
    """
    length = len(names)
    
    return{
        0: "no one likes this",
        1:"{} likes this",
        2:"{} and {} like this",
        3:"{}, {} and {} like this",
        4:"{}, {} and {n} others like this"
    }[min(4, length)].format(*names, n = length - 2)