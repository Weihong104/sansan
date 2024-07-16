# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:12:53 2024

@author: USER
"""

data = [10,20,30]
try:
   
    print(data[10])
    
    print(data[0])
    print(10/0) 
    print(data[2])
except Exception as err:
    print(err)    
    
print("Finish")    