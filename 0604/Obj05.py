# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:37:37 2024

@author: USER
"""

# 封裝

class Account():
    def __init__(self,number,name,money):
        self.__number = number  # 屬性私有化
        self.__name = name
        self.__balance = money
        
    def deposite(self,money):
        if money > 0 :
            self.__interest(money)
            self.__balance += money
        else:
            raise RuntimeError("不可以為負數")
            
    def withDraw(self,money):
        if self.__balance >= money:
            self.__balance -= money
            
    def showMoney(self):
        return self.__balance
    
    def __interest(self,money):
        if money >= 30000:
            inter = money * 0.003
            self.__balance += inter
    
    
ac = Account('123-456-789','王小明',1000)    
ac2 = Account('987-654-321','陳美麗',30000)

ac.deposite(10000)
print(ac.showMoney())

print(ac.showMoney())








        