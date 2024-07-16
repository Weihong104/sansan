# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:39:24 2024

@author: USER
"""

def divfun(num1,num2):
    try:
        result = divmod(num1,num2)        
        print(result)
        
    except Exception as e:
        print("函式處理")
        raise Exception(e)  # 丟出一個例外
        
        
try:
    divfun(10,0)
except Exception as e:
    # print("主程式")
    # print(e)  
    pass

print("程式再執行")      