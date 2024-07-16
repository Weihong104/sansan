# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:16:20 2024

@author: USER
"""

# 串列表達式

data = list()

for i in range(1,11):
    data.append(i)
    
print(data)    

level = [ i for i in range(1,11) ]

print(level)

number = [i for i in range(1,11) if i % 3 == 0 ]
print(number)