# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 20:53:47 2024

@author: USER
"""
import requests
import xml.sax
import io

class bikeHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.station=''
        self.rent=''
        self.space=''
    def startElement(self, tag, attr):
        self.tag=tag
    def characters(self, content):
        if self.tag=='sna':
            self.station==content
        if self.tag=='sbi':
            self.rent=content
        if self.tag=='bemp':
            self.space=content
    def endElement(self, tag):
        if self.tag=='sna':
            print('站名:',self.station)
        if self.tag=='sbi':
            print('可借:',self.rent)
        if self.tag=='bemp':
            print('可停:',self.space)



if __name__=='__main__':
    url='https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/xml?size=100'
    parser=xml.sax.make_parser()#建立空的解析器
    ubike=bikeHandler()
    parser.setContentHandler(ubike)
    data=requests.get(url)
    data.encoding='utf-8'
    data=data.text
    f=io.StringIO(data)
    parser.parse(f)
