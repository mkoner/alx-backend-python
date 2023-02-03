#!/usr/bin/env python3
'''
Module for variable annotations in Python
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Function that accepts a mixed list of floats and ints
    and returns the sum as float with annotations
    '''
    sum: float = 0
    for elm in mxd_lst:
        sum += elm
    return sum
