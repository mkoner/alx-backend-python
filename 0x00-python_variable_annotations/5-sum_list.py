#!/usr/bin/env python3
'''
Module for variable annotations in Python
'''


def sum_list(input_list: list[float]) -> float:
    '''
    Function that accepts a list of floats and returns the 
    sum as float with annotations
    '''
    sum: float = 0
    for elm in input_list:
        sum += elm
    return sum
