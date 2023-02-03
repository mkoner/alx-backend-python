#!/usr/bin/env python3
'''
Module for variable annotations in Python
'''

from typing import Iterable, Sequence, Tuple, List


Lst = Iterable[Sequence]
SeqInt = Tuple[Sequence, int]


def element_length(lst: Lst) -> List[SeqInt]:
    '''Length'''
    return [(i, len(i)) for i in lst]
