from twelvedata import TDClient
import pandas as pd
import matplotlib.pyplot as plt 
import mplfinance as mpf
import pandas as pd 
import matplotlib.dates as mpdates
from supersecretapi import supersecretapi
def update_stock():
    td = TDClient(apikey=supersecretapi()) #get your own api! :P
    ts = td.time_series(symbol="AAPL",
                        interval="1day",
                        timezone="America/Argentina/Buenos_Aires",
                        start_date="2020-11-02",
                        end_date="2021-01-09",
                        outputsize=5000).as_pandas()
    ts = ts.sort_values("datetime")#I Spend too much time sorting the DataFrame and not saving it hahaha
    print(ts)
    ts.to_csv("AAPL.csv")
    return ts

"""
Use existing date column as index:
https://queirozf.com/entries/pandas-time-series-examples-datetimeindex-periodindex-and-timedeltaindex
"""

def to_data_index(ts):
    datetime_series = pd.to_datetime(ts['datetime'])
    datetime_index = pd.DatetimeIndex(datetime_series.values)
    tss=ts.set_index(datetime_index)
    tss.drop('datetime',axis=1,inplace=True)
    return tss

#ts = pd.read_csv("AAPL.csv",parse_dates=True)
ts = update_stock()
print(ts)
print(type(ts))
#tss = to_data_index(ts)
#print(tss)
mpf.plot(ts,volume=True,type="candle",mav=4)
#update_stock()

