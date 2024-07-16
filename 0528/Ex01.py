# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def factorial(data,start):
    result = start
    for item in data:
        result *= item
        
    return result


#
res = factorial(data=[3,5,7,9,11],start=1)    

print("RESULT:{:,}".format(res))