#!/usr/bin/bash
def multiply_by_2(a_dictionary):
    new_diction = a_dictionary.copy()
    for key in new_diction:
        new_diction[key] *= 2
    return new_diction
