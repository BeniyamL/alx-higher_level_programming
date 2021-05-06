#!/usr/bin/python3
def best_score(a_dictionary):
    """function that finds the biggest integer value

    Arguments:
        a_dictionary: the given dictionary

    Returns:
        the key with bigest value
    """
    if a_dictionary is None:
        return None
    max_val = max(a_dictionary.values(), default=None)
    for k, v in a_dictionary.items():
        if max_val == v:
            return k
    return None
