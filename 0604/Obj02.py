# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:56:29 2024

@author: USER
"""

class Clothes:
    def __init__(self,color,size):
        self.color = color
        self.size = size
        
    def setColor(self,color):
        self.color = color
        
    def setSize(self,size):
        self.size = size
        
        
    def display(self):
        print("顏色：",self.color)
        print("尺寸：",self.size)
        
    def water(self):
        print("顏色：{}，防潑水！".format(self.color))
        
if __name__ == '__main__':        
    c1 = Clothes("白色","M")    
    c1.water()
    c1.display()
    c1.setColor("黑色")    
    c1.water()

        
    