# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:37:37 2024

@author: USER
"""

class Account():
    def __init__(self,number,name,money):
        self.number = number
        self.name = name
        self.balance = money
        
    def deposite(self,money):
        if money > 0 :
            self.balance += money
        else:
            raise RuntimeError("不可以為負數")
            
    def withDraw(self,money):
        if self.balance >= money:
            self.balance -= money
            
    def showMoney(self):
        return self.balance
    
    
ac = Account('123-456-789','王小明',1000)    
ac2 = Account('987-654-321','陳美麗',30000)


ac.deposite(10000)
print(ac.showMoney())

# ac2.deposite(-1000)
# print(ac2.showMoney())

ac.balance = 999999999

print(ac.showMoney())








        