from tradingview_ta import TA_Handler, Interval

tesla = TA_Handler()
tesla.set_symbol_as("TSLA")
tesla.set_exchange_as_crypto_or_stock("NASDAQ")
tesla.set_screener_as_stock("america")
tesla.set_interval_as(Interval.INTERVAL_1_DAY)
print(tesla.get_analysis().summary)


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


t = "Try once again\n"
i = "int"
s = "str"
h = "Stock Symbol:     "
j = "Market Symbol:    "

handler = TA_Handler()
symbol = loop_simples_de_coleta(h,t,s)
#symbol = input("Stock Symbol:     ")
handler.set_symbol_as(symbol)
exchange = loop_simples_de_coleta(j,t,s)
#exchange = input("Market Symbol:    ")
handler.set_exchange_as_crypto_or_stock(exchange)
handler.set_screener_as_stock("america")
handler.set_interval_as(Interval.INTERVAL_1_MINUTE)
print(handler.get_analysis().summary)

