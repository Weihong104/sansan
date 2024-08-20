# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:38:50 2024

@author: USER
"""
import requests
from bs4 import BeautifulSoup

header = {
    
'cookie':
'GUC=AQEBCAFmv01m6UIapAPg&s=AQAAAMkiP12n&g=Zr4Ekg; A1=d=AQABBL8dQ2YCEByCyoJP6UUdU2hwxRgSrLQFEgEBCAFNv2bpZr3Lb2UB_eMBAAcIvx1DZhgSrLQ&S=AQAAAg0YXGpG1FgFMv9UOAmdaiU; A3=d=AQABBL8dQ2YCEByCyoJP6UUdU2hwxRgSrLQFEgEBCAFNv2bpZr3Lb2UB_eMBAAcIvx1DZhgSrLQ&S=AQAAAg0YXGpG1FgFMv9UOAmdaiU; A1S=d=AQABBL8dQ2YCEByCyoJP6UUdU2hwxRgSrLQFEgEBCAFNv2bpZr3Lb2UB_eMBAAcIvx1DZhgSrLQ&S=AQAAAg0YXGpG1FgFMv9UOAmdaiU; cmp=t=1723729031&j=0&u=1---; gpp=DBAA; gpp_sid=-1; axids=gam=y-8uX0jN1E2uLR1TPm7rkyHDRnpayVeHc9~A&dv360=eS1qRjJNQW9SRTJ1RVcwbnpBMU9ZY1BFOG5uSkdaalVtNn5B&ydsp=y-gUi0k2lE2uIIYJAXI1RZEeYbPNo2unDj~A&tbla=y-DNsZqJRE2uLjXSY5DU3uWJ6uhkQ0dhaz~A; tbla_id=3d793f72-9844-4932-b860-77bab8236a24-tuctd3ca342; ms=c2=sME&c2_expire=1726321040113&co_servername=sME&co_servername_expire=1723815440113; _ga=GA1.3.450811619.1723729040; __BWtransf=c1723729040172x457d6d315; __BWtransf=c1723729040172x457d6d315; __BWfp=c1723729040172x457d6d315; __BWfp=c1723729040172x457d6d315; _gid=GA1.3.1106255223.1723729041; _bwgaid=450811619.1723729040; _ga_X0K6L55LH7=GS1.3.1723729040.1.1.1723729120.60.0.0; GUCS=AV23lrg-; _gat=1; __BW_1146-13B0J47T10CC4DR=1723729040.1723729120.-1',
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

    
    }
    
    
param = {
    'p': 'iPhone15'
    
    }    
    
    
url = "https://tw.buy.yahoo.com/search/product"


data = requests.get(url,headers=header,params=param)

data.encoding = 'utf-8'

data = data.text

print(data)

