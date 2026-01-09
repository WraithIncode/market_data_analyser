import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime


import requests


def download_data(ticker_symbol, start_date="2020-01-01", end=None):
    if end is None:
        end = datetime.now()
    if isinstance(ticker_symbol, set):
        ticker_symbol = list(ticker_symbol)

    # Create a session with a custom User-Agent to mimic a browser
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    })

    # Note: yfinance's download method might not directly accept a session in all versions,
    # but using a single ticker string with Ticker module is often more robust.
    # However, since we might pass a list, we stick to download but rely on the upgraded version.
    # If this fails, we can resort to individual Ticker calls.
    # Let's try to pass the session implicitly if supported, but currently yfinance
    # handles this internally better in newer versions.
    # We will stick to the standard download but ensure single ticker is passed as string if it's length 1

    if isinstance(ticker_symbol, list) and len(ticker_symbol) == 1:
        ticker_symbol = ticker_symbol[0]

    data = yf.download(ticker_symbol, start=start_date,
                       end=end, progress=False)

    # Drop columns if they exist
    cols_to_drop = ["High", "Low", "Open", "Volume"]
    existing_cols = [c for c in cols_to_drop if c in data.columns or (isinstance(
        data.columns, pd.MultiIndex) and c in data.columns.get_level_values(0))]

    if existing_cols:
        data = data.drop(columns=existing_cols)

    return data
