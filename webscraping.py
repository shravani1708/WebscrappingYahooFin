import requests
from bs4 import BeautifulSoup 
import json
stocks={'AMZN','DWAC','META','AAPL'}
stockinfo=[]
def getdata(company):
    headers= {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    url=f'https://finance.yahoo.com/quote/{company}'  
    res =requests.get(url,headers=headers) 
    soup=BeautifulSoup(res.text,'html.parser')
    stock={
        'company':company , 
        'price':soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        'change':soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
    }
    return stock
for item in stocks:
    stockinfo.append(getdata(item))
n=len(stockinfo)
for i in range(n):
    print(item,'=',stockinfo[i])
print('Success')
