# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:54:24 2024

@author: USER
"""
# 原始方式

# score = [70,60,50,100,60,70]
# found = False
# for i in score:
#     if i > 100:
#         found = True
#         print("找到有大於100分的數字")
#         break

# if not found:
#     print("數字都是正常")
    
    
#改進方式    
score = [70,60,50,110,60,70]

for i in score:
    if i > 100:
        print("有數字大於100")
        break
else:
    print("所有數字皆正常")    
