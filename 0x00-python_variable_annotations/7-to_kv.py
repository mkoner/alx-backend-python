#!/usr/bin/env python3
'''
Module for variable annotations in Python
'''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Function that accepts a string and int/float and returns the
    a tuple of the string and square of int/float with annotations
    '''
    return (k, v * v)
