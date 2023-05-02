import pandas as pd
import numpy as np
import pyupbit as pu
import datetime

def get_ohlc(symbol, start_date=None, end_date=None):
    symbol = "KRW-"+symbol
    start_date = int(start_date.replace('-', ''))
    end_date = int(end_date.replace('-', ''))
    count = end_date - start_date
    df = pu.get_ohlcv(symbol, to = str(end_date), count=count)
    df.index = [datetime.datetime.strptime(datewithtime.strftime('%Y-%m-%d'), '%Y-%m-%d') for datewithtime in df.index]
    df = df.rename(columns={'open': 'Open', 'high': 'High', 'low':'Low', 'close':'Close', 'volume':'Volume'})
    df['Adj Close'] = df['Close']
    df = df.drop('value', axis=1)
    return df

def get_price(symbol, start_date=None, end_date=None):
    df = get_ohlc(symbol, start_date=start_date, end_date=end_date)
    df.rename(columns={'Close':symbol}, inplace=True)
    return df[[symbol]]