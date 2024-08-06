# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 19:07:24 2024

@author: USER
"""

import requests
import io
import xml.sax

class BusHandler(xml.sax.ContentHandler):
    def startElement(self,tag,attr):
        if tag=='Route':
            print(attr['nameZh'])
            print(attr['ddesc'])
            print(attr['departureZh'])
            print()
            
if __name__=='__main__':
    url='https://ibus.tbkc.gov.tw/xmlbus/StaticData/GetRoute.xml'
    parser=xml.sax.make_parser()#建立空的解析器
    bus=BusHandler()
    parser.setContentHandler(bus)
    data=requests.get(url)
    data.encoding='utf-8'
    data=data.text
    busData=io.StringIO(data)
    
    parser.parse(busData)