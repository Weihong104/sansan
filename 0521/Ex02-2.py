# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:59:13 2024

@author: USER
"""

import random

number = list()
for i in range(5,101,5):
    number.append(i)
    
print(number)


for i in range(5):
    n = number.pop(random.randint(0,len(number)-1))    
    print(n)