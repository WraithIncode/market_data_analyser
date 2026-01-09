import numpy as np


def daily_returns(data):
    daily_returns = (data['Close'].pct_change())
    return daily_returns


def daily_volatility(x):
    std_pct_change = (x.std())
    return std_pct_change


def annual_returns(y):
    annual_returns = (y * np.sqrt(252))
    return annual_returns
