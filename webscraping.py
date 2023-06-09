import requests
import yfinance as yf
from bs4 import BeautifulSoup 
import json
stock=input("Enter the stock name")
stockinfo=[]
def getdata(company):
    headers= {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    url=f'https://finance.yahoo.com/quote/{company}'  
    res =requests.get(url,headers=headers) 
    soup=BeautifulSoup(res.text,'html.parser')
    info={
        'company':company , 
        'price':soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        'change':soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
    }
    return info
data=getdata(stock)
st_data=yf.Ticker(stock)
st_data=st_data.history(period="max")
st_data
st_data.plot.line(y="Close", use_index=True)
print(data)
print('Success')

