# -*- coding: utf-8 -*-
"""
作業
亂數產生5~100之間可以被5整除的數
產生用5個變數去儲存不可重複
"""
import random

# 初始化五個變數
a, b, c, d, e = 0, 0, 0, 0, 0

# 使用 while 循環生成五個不重複的符合條件的隨機數字
while True:
    num = random.randrange(5, 101, 5)  # 生成5到100之間的可以被5整除的隨機數字
    if num % 5 == 0:
        if a != num and b != num and c != num and d != num and e != num:
            if a == 0:
                a = num
            elif b == 0:
                b = num
            elif c == 0:
                c = num
            elif d == 0:
                d = num
            elif e == 0:
                e = num
        if a != 0 and b != 0 and c != 0 and d != 0 and e != 0:
            break  # 當五個變數都不為零時退出循環

# 打印結果
print(a)
print(b)
print(c)
print(d)
print(e)