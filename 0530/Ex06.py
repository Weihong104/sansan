# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:42:55 2024

@author: USER
"""

data = [1,2,3]

num1,num2 = eval(input("輸入二個數字，用,隔開："))

try:
    result = num1 / num2
    print(result)
    print(data[0])
    print(data[10])
    
except IndexError as e:
    print("索引值Error")    
    print("請檢查！！")
except:
    print("其他錯誤")    
    
print("程式執行完畢")    
    
    