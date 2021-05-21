#!/usr/bin/python3
""" text_indentation function """


def text_indentation(text):
    """ function to print a text with 2 new lines after ., ? and :

    Arguments:
        text: the given string
    Returns:
        nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.' + '\n\n')
    text = text.replace('?', '?' + '\n\n')
    text = text.replace(':', ':' + '\n\n')
    new_string = [x.strip() for x in text.split('\n')]
    new_string = '\n'.join(new_string)
    print(new_string, end="")
