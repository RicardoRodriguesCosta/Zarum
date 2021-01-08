from tradingview_ta import TA_Handler, Interval
import subprocess
from terminaltables import AsciiTable

def loop_simples_de_coleta(argumento,errormsg,classe):
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


config = ["Try once again\n","int","str","Stock Symbol:     ","Market Symbol:    ","Time Interval:    "]

def get_stock():
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

def receive_input(lista=list,valor=int):
    for i in lista:
        if i[-1] == valor:
            return i[0]
        else:
            continue

def get_list_stock(lista=list):
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


def stock_pref_list():
    stock_pref_listado = []
    with open("stocks.txt","r") as stock_list:
        for stock in stock_list:
            stock_pref_listado.append(stock.split())
    return stock_pref_listado

def interval_options():#try to implement some get function to auto populate the list.
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
    interval_resp = loop_simples_de_coleta(config[5],config[0],config[2])
    r = receive_input(interval_options,interval_resp)
    return r

if __name__ == "__main__":
    get_list_stock(stock_pref_list())
