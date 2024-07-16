# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:25:25 2024

@author: USER
"""

class Father:
    def company(self):
        print("老爸的公司：輝達")
    def showMoney(self):
        print("三兆美金")
        
        
class Son(Father):
    pass

class Daughter(Father):
    # 重新定義父類別的方法
    def company(self):
        print("女兒在超微上班")
    def boyfriend(self):
        print("男友在Intel上班")
        
        
son = Son()
son.company()
son.showMoney()

daughter = Daughter()
daughter.company()
daughter.showMoney()        