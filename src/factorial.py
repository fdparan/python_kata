# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:54:52 2015

@author: francisparan
"""

from functools import reduce

def factorial(num):
    if num < 0:
        raise ValueError('factorial() not defined for negative values')

    return reduce(lambda x, y: x*y, range(1, num+1), 1)

