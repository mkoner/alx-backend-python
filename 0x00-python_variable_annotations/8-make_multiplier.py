#!/usr/bin/env python3
'''
Module for variable annotations in Python
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Function that accepts a string and int/float and returns the
    a tuple of the string and square of int/float with annotations
    '''
    def f(n: float) -> float:
        """ multiplies a float by multiplier """
        return n * multiplier

    return f
