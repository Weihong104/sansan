# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:40:19 2024

@author: USER
"""

class Father:
    def display(self,name):
        self.name = name
        print("Father name is ", self.name)
        
class Mother:
    def display(self,name):
        self.name = name
        print("Mother name is ", self.name)       
        
class Child(Father,Mother):
    pass

class Son(Father):
    pass


print(Child.__name__,'繼承二個父類')
for item in Child.__bases__:
    print(item)
    
    
john = Son()
john.display("Tom")

print(Son.__bases__)

# 變更子類的繼承

Son.__bases__ = (Mother,)

john.display("Mary")

print(Son.__bases__)


    

