# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:19:55 2024

@author: USER
"""

class Parent:
    def show1(self):
        print("Parent show1")
        
    def show2(self):
        print("Parent show2")
        
class Son(Parent):
    def display(self):
        print("Son Display")        
        
class Daughter(Parent):
    def show2(self):
        print("Daughter Show2")        
        
    def display(self):
        print("Daughter Display")
        
class GrandChild(Son,Daughter):
    def message(self):
        print('Child')
        

bill = GrandChild()

bill.show1()
bill.show2()        
bill.display()
bill.message()
        