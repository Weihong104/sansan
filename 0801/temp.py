# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json
url='https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=1000'

data= requests.get(url).text

bike=json.loads(data)

for item in bike:
    print(item['sna'])
    print(item['sbi'])
    print(item['bemp'])
    print()



