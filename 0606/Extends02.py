# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:34:40 2024

@author: USER
"""

# 基礎類別   父類
class Father: 
    def car(self):
        print("bmw")
        
    def house(self):
        print("7期")
        
        
        
class Mother:
    def car(self):
        print("保時捷")        
        
    def land(self):
        print("14期")
        
#衍生類別  子類        
class Son(Mother,Father):
    pass        


son = Son()
son.car()
son.house()