# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:24:26 2024

@author: USER
"""

class Mother():
    def display(self,pay):
        self.price = pay
        if self.price >= 30000:
            self.price *= 0.9
        print( '= {:,}'.format(self.price))    
        
        
        
class Daughter(Mother):
    def display(self,pay):
        self.price = pay        
        super().display(pay)
        if self.price >= 30000:
            self.price *= 0.8
            
        print('8折={:,}'.format(self.price))    
        
        
Mary = Mother()
print("40000 打 9 折=")        
Mary.display(40000)

Cherry = Daughter()
print("40000 打 9 折 =")
Cherry.display(40000)