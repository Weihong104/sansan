# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:17:22 2024

@author: USER
"""

msg = "姓名：{}年齡：{}".format('Bill',19)

print(msg)


msg = "姓名：{0}年齡：{1}，別名：{0}".format("聯成",30)

print(msg)

msg = "現金：{:,}元".format(10000000)
print(msg)

msg = "姓名：{:10s}利率：{:.2f}".format('Bill',3.1415926)

print(msg)


msg = "姓名：{:>10s}利率：{:.2f}".format('Bill',3.1415926)

print(msg)

msg = "姓名：{:^10s}利率：{:.2f}".format('Bill',3.1415926)

print(msg)

msg = "姓名：{0:^10s}利率：{1:.2f}".format('Bill',3.1415926)

print(msg)