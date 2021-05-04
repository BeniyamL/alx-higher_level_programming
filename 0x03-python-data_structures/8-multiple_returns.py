#!/usr/bin/python3
def multiple_returns(sentence):
    """
    multiple_returns - return length and first character of a string
    @sentence: the given string
    @Return : the length and first character of a string
    """
    l = len(sentence)
    if l == 0:
        return (0, None)
    frstchar = sentence[0]
    return (l, frstchar)
