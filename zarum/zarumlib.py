import os
from tradingview_ta import TA_Handler, Interval
import subprocess
from terminaltables import AsciiTable
from twelvedata import TDClient
import pandas as pd
import matplotlib.pyplot as plt 
import mplfinance as mpf
import pandas as pd 
import matplotlib.dates as mpdates
from supersecretapi import supersecretapi
def update_stock(stock=str): #Gets the stock data from Twelvedata
    td = TDClient(apikey=supersecretapi()) #get your own api! :P
    ts = td.time_series(symbol=stock,
                        interval="1day",
                        timezone="America/Argentina/Buenos_Aires",
                        start_date="2020-11-02",
                        end_date="2021-01-09",
                        outputsize=5000).as_pandas()
    ts = ts.sort_values("datetime")#I Spend too much time sorting the DataFrame and not saving it hahaha
    print(ts)
    ts.to_csv("data/%s.csv" % stock)
    return ts

def to_data_index(ts): #Transform pandas.DataFrame to one with time index
    """
    Use existing date column as index:
    https://queirozf.com/entries/pandas-time-series-examples-datetimeindex-periodindex-and-timedeltaindex
    """
    datetime_series = pd.to_datetime(ts['datetime'])
    datetime_index = pd.DatetimeIndex(datetime_series.values)
    tss=ts.set_index(datetime_index)
    tss.drop('datetime',axis=1,inplace=True)
    return tss

def loop_simples_de_coleta(argumento,errormsg,classe): #Get input with some safeguard
	if classe == "int":
		while True:
			try:
				resposta = int(input(argumento))
				return resposta
			except:
				print(errormsg)
	elif classe == "str":
		while True:
			try:
				resposta = input(argumento)
				return resposta
			except:
				print(errormsg)
	elif classe == "bool":
		while True:
			try:
				resposta = bool(int(input(argumento)))
				return resposta
			except:
				print(errormsg)
	elif classe == "float":
		while True:
			try:
				resposta = float(input(argumento))
				return resposta
			except:
				print(errormsg)

def get_stock(): #Get sell/buy indicators from tradingview_ta for one stock, with user input and print the result
    handler = TA_Handler()
    symbol = loop_simples_de_coleta(config[3],config[0],config[2])
    handler.set_symbol_as(symbol)
    exchange = loop_simples_de_coleta(config[4],config[0],config[2])
    handler.set_exchange_as_crypto_or_stock(exchange)
    handler.set_screener_as_stock("america")
    r ="Interval." + str(interval_options())
    handler.set_interval_as(r)
    stock = handler.get_analysis().summary
    stock_table = []
    for i in stock.items():
        stock_table.append(i)
    stock_table.insert(0,["Company: " + symbol.upper(),"Result"])
    stock_table = AsciiTable(stock_table)
    print(stock_table.table)

def receive_input(lista=list,valor=int): #Compares user input to values on one list and return correspondent str
    for i in lista:
        if i[-1] == valor:
            return i[0]
        else:
            continue

def get_list_stock(lista=list): #Get sell/buy indicators for multiple stocks from a list, and print the results 
    handler = TA_Handler()
    for i in range(len(lista)):
        handler.set_symbol_as(lista[i][0])
        handler.set_exchange_as_crypto_or_stock("NASDAQ")
        handler.set_screener_as_stock("america")
        handler.set_interval_as(Interval.INTERVAL_1_HOUR)
        stock = handler.get_analysis().summary
        stock_table = []
        for b in stock.items():
            stock_table.append(b)
        stock_table.insert(0,["Company: " + lista[i][0].upper(),"Result"])
        stock_table = AsciiTable(stock_table)
        print(stock_table.table)


def stock_pref_list(): #Open a file with a list of stocks and return a list of stocks
    stock_pref_listado = []
    with open("stocks_watchlist","r") as stock_list:
        for stock in stock_list:
            stock_pref_listado.append(stock.split())
    return stock_pref_listado

def interval_options(): #Offer rudimentary menu with time options and return time as str
    #try to implement some get function to auto populate the list.
    interval_options = [["Option", "#"],[Interval.INTERVAL_1_MINUTE,1],
 [Interval.INTERVAL_5_MINUTES,2],
 [Interval.INTERVAL_15_MINUTES,3],
 [Interval.INTERVAL_1_HOUR,4],
 [Interval.INTERVAL_4_HOURS,5],
 [Interval.INTERVAL_1_DAY,6],
 [Interval.INTERVAL_1_WEEK,7],
 [Interval.INTERVAL_1_MONTH,8],["Voltar",0]]

    table_interval = AsciiTable(interval_options)
    print(table_interval.table)
    interval_resp = loop_simples_de_coleta(configleng[5],configleng[0],configleng[2])
    r = receive_input(interval_options,interval_resp)
    return r

def update_multiple_stocks(lista=list):
    for element in lista:
        update_stock(element[0])#Think to change to list of list of strings to list of strings

configleng = ["Try once again\n","int","str","Stock Symbol:     ","Market Symbol:    ","Time Interval:    "]

if __name__ == "__main__":
   ##get_list_stock(stock_pref_list())
   # #ts = pd.read_csv("AAPL.csv",parse_dates=True)
    ts = update_multiple_stocks(stock_pref_list())
   #print(stock_pref_list())
   # #tss = to_data_index(ts)
   # #print(tss)
   # mpf.plot(ts,volume=True,type="candle",mav=4)
   # #update_stock()
