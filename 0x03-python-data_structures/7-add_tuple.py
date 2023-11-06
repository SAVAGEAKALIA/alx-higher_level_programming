#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a1 = tuple_a[:2]
    tuple_b1 = tuple_b[:2]

    if len(tuple_a1) < 2:
        if len(tuple_a1) == 1:
            tuple_a1 = (tuple_a1[0], 0)
        else:
            tuple_a1 = (0, 0)
    if len(tuple_b1) < 2:
        if len(tuple_b1) == 1:
            tuple_b1 = (tuple_b1[0], 0)
        else:
            tuple_b1 = (0, 0)

    # Calculate the sum of the first and second elements of the tuples
    result = (tuple_a1[0] + tuple_b1[0], tuple_a1[1] + tuple_b1[1])


    return result
