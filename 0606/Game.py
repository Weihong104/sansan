# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:15:15 2024

@author: USER
"""

from Role import Dancer,SworksMan
import random


def changeRole(me,you):
    print(me.getName(),end='')
    me.fight()
    blood = random.randint(0,10)
    youblood = you.getHp() - blood
    you.setHp(youblood)
    
    print("{}損失{}血量，目前的血量：{}".format(you.getName(),blood,youblood))    



if __name__ == '__main__':
    
    dancer = Dancer('大喬',150,300)
    
    man = SworksMan('劉備',150,150)
    
    while (dancer.getHp() > 0 and man.getHp() > 0):
        num = random.randint(1,50)
        
        if num % 2 == 0:
            changeRole(dancer,man)
        else:
            changeRole(man,dancer)           
        
    if dancer.getHp() > 0:
        print(dancer.getName(),"Win")
    else:
        print(man.getName(),"Win")
        
            
    