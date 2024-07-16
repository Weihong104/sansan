# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:28:10 2024

@author: USER
"""

n1,n2 = eval(input('input number ,:'))

try:
    result = n1 / n2
except Exception as e:
    print(e)

else:
    print("Result:",result)

print('Finish')    