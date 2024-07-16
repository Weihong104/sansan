# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:03:24 2024

@author: USER
"""

fruits = {'apple':100,'banana':49,'orange':69}

print(fruits['banana'])
#print(fruits['charrey'])
print(fruits.get('charrey'))
print(fruits.get('orange'))
print(fruits.get('charrey',0))
print(fruits.get('charrey','找不到key'))
