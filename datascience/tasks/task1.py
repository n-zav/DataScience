def print_array():
    """
    outputs array=[['a','b','c'],['d','e','f']] in one line
    """
    array = [['a', 'b', 'c'], ['d', 'e', 'f']]
    output = []
    for i in array:
        output.append(' '.join(i))

    return output
