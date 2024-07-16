# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Dancer:
    def __init__(self,name,hp,mp):
        self.__name = name
        self.__hp = hp
        self.__mp = mp
        
    def fight(self):
        print("使出迴旋踢")
        
    def song(self):
        print("YoYoYo")
        
    def setHp(self,hp):
        self.__hp = hp
        
    def setMp(self,mp):
        self.__mp = mp
        
    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp
    
    def getMp(self):
        return self.__mp
    
    
class SworksMan:
    
    def __init__(self,name,hp,mp):
        self.__name = name
        self.__hp = hp
        self.__mp = mp
        
    def fight(self):
        print("使出西洋劍")
        
    def Deathblow(self):
        print("使出屠龍刀快斬")
        
    def setHp(self,hp):
        self.__hp = hp
        
    def setMp(self,mp):
        self.__mp = mp
        
    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp
    
    def getMp(self):
        return self.__mp    
    
class Adviser:
    
    def __init__(self,name,hp,mp):
        self.__name = name
        self.__hp = hp
        self.__mp = mp
        
    def fight(self):
        print("使出西洋劍")
        
    def Deathblow(self):
        print("使出屠龍刀快斬")
        
    def setHp(self,hp):
        self.__hp = hp
        
    def setMp(self,mp):
        self.__mp = mp
        
    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp
    
    def getMp(self):
        return self.__mp    
    
        
        