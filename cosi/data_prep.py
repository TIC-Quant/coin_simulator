import pandas as pd
import numpy as np
import requests, json
import pyupbit


def get_price(symbol, start_date=None, end_date=None, decimal_duex=True):
    '''
    :param symbol: Symbol or ticker of equity by finance.yahoo.com
    :param start_date: The first date of period
    :param end_date: The last date of period
    :param decimal_duex: Set false not to round up
    :return: Historical close prices
    '''
    df = get_ohlc(symbol, start_date=start_date, end_date=end_date, decimal_duex=decimal_duex)
    df.rename(columns={'close':symbol}, inplace=True)
    return df[[symbol]]


def get_ohlc(symbol, start_date=None, end_date=None, decimal_duex=True):
    '''
    :param symbol: Symbol or ticker of equity by finance.yahoo.com
    :param start_date: The first date of period
    :param end_date: The last date of period
    :param decimal_duex: Set false not to round up
    :return: historical open, high, low, close prices and trade volume
    '''
    if isinstance(symbol, list):
        symbol = symbol[0]
    end_date = pd.to_datetime(end_date).date() if end_date else pd.Timestamp.today().date()
    start_date = pd.to_datetime(start_date).date() if start_date else months_before(end_date, 12)
    df = _get_daily_price(symbol, start=start_date, end=end_date)
    __decimal_formatter(decimal_duex)
    return df

def __decimal_formatter(duex):
    if duex:
        pd.options.display.float_format = '{:,.2f}'.format
    else:
        pd.options.display.float_format = '{:,.6f}'.format

def _get_daily_price(symbol, start, end):
    delta = end - start
    df = pyupbit.get_ohlcv(symbol, count=delta.days)   
    return df

def months_before(date, n):
    '''
    Get date n months before given date
    :param date: Base date
    :param n: N months
    :return: Date
    '''
    d = pd.to_datetime(date) - pd.DateOffset(months=n)
    if d.weekday() > 4:
        adj = d.weekday() - 4
        d += pd.DateOffset(days=adj)
    else:
        d = d
    return d.date()


if __name__ == '__main__':
    df = get_price('KRX-BTC')