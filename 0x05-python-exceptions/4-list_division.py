#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ function to divide list_1 by list_2

    Arguments:
        my_list_1: the first list
        my_list_2: the second list

    Returns:
        the new result list
    """
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            result.append(0)
            print("wrong type")
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except IndexError:
            result.append(0)
            print("out of range")
        finally:
            pass
    return result
