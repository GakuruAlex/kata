def to_camel_case(text):
    """_ converts dash/underscore delimited words into camel casing_

    Args:
        text (_str_): _parameter_
    Returns:
        text (_str_): _converted text_
    """
    text = text.replace("-"," ").replace("_"," ").split(" ") #Remove dash/underscore and split to list
    text[1:] = [text[n].title() for n,word in enumerate(text) if n > 0] #Convert first letter in words after the first to uppercase
    text = "".join(text)
    return text

def to_camel_case_2(text):
    """_ converts dash/underscore delimited words into camel casing_

    Args:
        text (_str_): _parameter_
    Returns:
        text (_str_): _converted text_
    """
    text = text.replace("-"," ").replace("")