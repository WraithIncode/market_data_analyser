import yfinance as yf
from datetime import datetime
import pandas as pd


def download_data(ticker_symbol, start_date="2020-01-01", end=datetime.now()):
    print(f"Downloading for {ticker_symbol} from {start_date} to {end}")
    try:
        raw_data = yf.download(ticker_symbol, start=start_date, end=end)
        print("Raw data columns:", raw_data.columns)
        print("Raw data head:", raw_data.head())

        data = raw_data.drop(columns=["High", "Low", "Open", "Volume"])
        return data
    except Exception as e:
        print(f"Error in download_data: {e}")
        return pd.DataFrame()


ticker = "AAPL"
ticker_set = {ticker}
start_date = "2025-01-01"

print(f"--- Attempting download with set: {ticker_set} ---")
data_set = download_data(ticker_set, start_date=start_date)
if data_set.empty:
    print("Result: Data is empty.")
else:
    print("Result: Data is NOT empty.")
    print(data_set.head())

print(f"\n--- Attempting download with string: {ticker} ---")
data_str = download_data(ticker, start_date=start_date)
if data_str.empty:
    print("Result: Data is empty.")
else:
    print("Result: Data is NOT empty.")
    print(data_str.head())
