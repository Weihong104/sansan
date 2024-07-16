# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

number = list()

while len(number) != 5:
    n = random.randrange(5,101,5)
    if number.count(n) == 0:
        number.append(n)
        
print(number)        