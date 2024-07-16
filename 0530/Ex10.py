# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:23:00 2024

@author: USER
"""

import traceback

def divfun(num1,num2):
    try:
        result = divmod(num1,num2)        
        print(result)
        
    finally:
        print("計算完成")
        
        
        
        
try:        
    divfun(10,2)        
    divfun(20,0)
except Exception as e:
    print()
    print(e.__traceback__.tb_lineno)
    print(e)
    print(e.__traceback__.tb_frame.f_globals['__file__'])
    print(traceback.format_exc())