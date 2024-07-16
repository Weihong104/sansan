# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:20:45 2024

@author: USER
"""

def total(*value):
    t = 0
    
    for i in value:
        t += i
        
    return t

print(total())    

print(total(1,2,3,4))

print(total(10,20))

def school(*people,name):
    print('校名：',name)
    print('學校資料：',people)
    
#school(600,100,5,'很有愛學校')        會error 因為需要關鍵字引數
school(600,100,5,name='很有愛學校')    
    