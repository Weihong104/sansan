# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:59:40 2024

@author: USER
"""

#無參數的函式
def Hello():
    print("你好")
    print("Hello")
    
    
def loopfor():
    for i in range(5):
        print(i)
        
def sumNumber():
    total = 0
    for i in range(1,11):
        total += i
        
    return total    



        
        
Hello()
Hello()
loopfor()        

number = sumNumber()
print(number)
print(sumNumber())

print(Hello())


