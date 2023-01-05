from termcolor import colored
import yfinance as yf
import time
import stockstats
import pandas as pd
import os

def get_price(stock_name):
    ticker = stock_name
    stock = yf.Ticker(ticker)
    price = stock.info['regularMarketPrice']
    return price

def get_rsi(stock_name):
    ticker = stock_name
    stock = stockstats.StockDataFrame.retype(pd.read_csv(f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1=0&period2=9999999999&interval=1d&events=history"))
    rsi = stock["rsi_14"]
    return f"{rsi[-1]:.2f}"
    
# Run the loop indefinitely
while True:
    list_stocks = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'V', 'PG', 'MCD', 'INTC', 'CSCO' ]
    
    for i in list_stocks:
        price = get_price(i)
        rsi = get_rsi(i)
        print([ i + " " + str(price) + " " + str(rsi) ])
        if (float(rsi) < 30):
            print(colored(" >> BUY : " + i,'green'))
            os.system('say "BUY BUY BUY BUY BUY"')
            
        elif (float(rsi) > 70):
            print(colored(" >> SELL : " + i,'red'))
            os.system('say "SELL SELL SELL SELL SELL"')
    
    time.sleep(60)


