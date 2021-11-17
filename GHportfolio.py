from os import name
import numpy as np
import pandas as pd
import datetime

weekdays = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
date = datetime.datetime.now()
weekday = weekdays[datetime.datetime.weekday(date)]
weeknumber = datetime.date.isocalendar(date) 
t = date.strftime("%S")
#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

def price(ticker, perio, holdings):
    data = yf.download(tickers=ticker, period=perio, interval='1m')
    a = data['Open']
    prices = a[1]
    print(ticker, '$',prices, "Total holdings:",holdings*prices)
    return prices

#Look up the ticker symbol for the stock, currency you want on yahoo finance and  put in your holdings

totBTC = 1
priceBTC = price('BTC-USD',"5m", totBTC)

totETH = 1
priceETH = price("ETH-USD","5m",totETH)




#Holdings
totvalue = priceBTC*totBTC+priceETH*totETH

print("Currency","Price","Holdings","Value")
print("BTC", priceBTC,totBTC,priceBTC*totBTC,priceBTC*totBTC/totvalue)
print("ETH", priceETH,totETH,priceETH*totETH,priceETH*totETH/totvalue)

print("Total value:",totvalue,"USD")

