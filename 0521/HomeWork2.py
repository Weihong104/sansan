# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:12:27 2024

@author: USER
"""

import random
black = [10,17,41]
white = [5,12,31]

number = list()

for i in white:
    number.append(i)
    
while len(number) != 6:
    n = random.randint(1,50)
    if black.count(n) == 0:
        while number.count(n) != 0:
            n = random.randint(1,50)
            
        number.append(n)    
        
print(number)        