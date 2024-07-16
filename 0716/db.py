# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='iu',
    password='0987654321',
    database='myiu',
    auth_plugin='mysql_native_password'
    
    )

cursor = conn.cursor(buffered=True)