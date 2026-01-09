import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime


def download_data(ticker_symbol, start_date="2020-01-01", end=datetime.now()):
    data = yf.download(ticker_symbol, start=start_date, end=end
                       ).drop(columns=["High", "Low", "Open", "Volume"])
    return data
