
import yfinance as yf
import pandas as pd

TICKERS = ["SPY","QQQ","IWM","TLT","IEF","SHY","GLD"]

def load_prices(start="2010-01-01"):
    data = yf.download(TICKERS, start=start)
    return data["Adj Close"]

def compute_returns(prices):
    return prices.pct_change().dropna()
