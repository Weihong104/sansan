# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:38:11 2024

@author: USER
"""

a = 100
b = a
print(id(a))
print(id(b))

a = 199

print(id(a))

item = [10,20,30,40]

data = item

print(id(item))
print(id(data))

item[0] = 199

print(data)

print(id(data))



