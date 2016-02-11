# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:54:52 2015

@author: francisparan
"""

def factorial(num):
    if num < 0:
        raise ValueError('factorial() not defined for negative values')

    result = 1
    for n in range(result, num+1):
        result *= n
    return result


