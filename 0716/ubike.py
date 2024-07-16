# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:12:03 2024

@author: USER
"""

import db

import requests

import json

url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=100"


data = requests.get(url).text


sql = "insert into students(name,memo) value(%s,%s)"
db.cursor.execute(sql,('John',data))
db.conn.commit()



bike = json.loads(data)

for row in bike:
    sql = "select * from bike where station='{}'".format(row['sna'])
    db.cursor.execute(sql)
    
   
    if db.cursor.rowcount == 0:
        sql ="insert into bike(station,rent,space,address) value(%s,%s,%s,%s)"
        db.cursor.execute(sql,(row['sna'],row['sbi'],row['bemp'],row['ar']))
        db.conn.commit()
        
db.conn.close()        



