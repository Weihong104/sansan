# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:56:23 2024

@author: USER
"""

try:
    result = 10 / 0
    print(result)
    
except Exception as e:
    print(e)

finally:
    print("一定會執行")    
    
print("程式執行完畢")
          
          