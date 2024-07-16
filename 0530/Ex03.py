# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:04:08 2024

@author: USER
"""

data = [10,20,30]
try:
    print(10/0)
    print(data[10])
    
    print(data[0])
    
    print(data[2])
except (IndexError , ZeroDivisionError) as err:
    print(err)    
    
print("Finish")    