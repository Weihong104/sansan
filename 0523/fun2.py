# -*- coding: utf-8 -*-
"""
Created on Thu May 23 21:10:42 2024

@author: USER
"""
# 有參數的函式，也稱位置函式
def area(w,h):
    return w*h

def loopfor(start,end):
    total = 0
    
    for i in range(start,end+1):
        total += i
        
    return total


print(area(4,3))    
print(loopfor(1,10))
print(loopfor(2,30))

