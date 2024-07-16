# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:15:39 2024

@author: USER
"""
import random

ans = random.randint(1, 100)
guess = 0

count = 1
while ans != guess:
    
    guess = int(input("請輸入1~100之間的整數："))
    if guess > ans:
        print("請猜小一點")
    elif guess < ans:
        print("請猜大一點")
        
    count += 1    
    if count == 4:
        break
    
        
if ans == guess:        
    print("猜對了")        
else:
    print("已滿 3 次不能再猜了")    