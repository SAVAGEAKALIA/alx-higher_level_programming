#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for i in my_list:
        num = i % 2 == 0
        result.append(num)

    return result
