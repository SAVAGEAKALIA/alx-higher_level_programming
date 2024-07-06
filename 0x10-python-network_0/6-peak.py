#!/usr/bin/python3
""" Script to calculate peak """


def find_peak(list_of_integers):
    """
    Function  definition
    Find the peak through the lowest tim complexity method
    """

    num_list = list_of_integers

    if len(num_list) == 0:
        return None

    if len(num_list) == 1:
        return num_list[0]
    if len(num_list) == 2:
        return max(num_list)

    middle_index = len(num_list) // 2

    right = middle_index + 1
    left = middle_index - 1

    if num_list[middle_index] > num_list[middle_index - 1] \
            and \
            num_list[middle_index] > num_list[middle_index + 1]:
        return num_list[middle_index]

    elif num_list[right] > num_list[middle_index]:
        return find_peak(num_list[right:])

    else:
        for element in num_list[:left]:
            if element > num_list[left]:
                num_list[left] = element
            else:
                continue
        return num_list[left]

