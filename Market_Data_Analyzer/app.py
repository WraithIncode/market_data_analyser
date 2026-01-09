# Import necessary modules, including custom ones from the 'src' directory

import src.metrics as mt
import src.visualization as vis
import src.downloader as dw
import os
import sys
import matplotlib.pyplot as plt

# Add 'src' directory to system path for module imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

print("--- Market Data Downloader & Analyzer ---")

# Prompt user for ticker symbol and convert to uppercase
print("Note: For Indian stocks use .NS (NSE) or .BO (BSE). Example: RELIANCE.NS")
ticker_symbol = input("Enter the ticker symbol (e.g., AAPL): ").strip().upper()

if not ticker_symbol:
    print("Error: Ticker symbol cannot be empty.")
    sys.exit(1)

# Download data starting from a default date or user-specified date
start_date = input(
    "Enter the start date (YYYY-MM-DD) [default: 2025-01-01]: ").strip()
current_start_date = start_date if start_date else "2025-01-01"

print(f"Downloading data for {ticker_symbol}...")
try:
    data = dw.download_data({ticker_symbol}, start_date=current_start_date)
except Exception as e:
    print(f"Error downloading data: {e}")
    sys.exit(1)

if data.empty:
    print(
        f"No data found for {ticker_symbol} starting from {current_start_date}.")
    sys.exit(0)

# Calculate daily returns, volatility metrics and annualized returns
try:
    day_returns = mt.daily_returns(data)
    daily_vol = mt.daily_volatility(day_returns)

    if not daily_vol.empty:
        daily_vol_float = daily_vol.iloc[0]
        annual_returns = mt.annual_returns(daily_vol)
        annual_returns_float = annual_returns.iloc[0]

        # Visualize and print results
        print("\n--- Results ---")
        print(f"Daily volatility: {daily_vol_float*100:.2f}%")
        print(f"Annual returns: {annual_returns_float*100:.2f}%")

        vis.plot(data['Close'], title=f"{ticker_symbol} Closing Prices")
        plt.show()
        vis.plot(day_returns, title=f"{ticker_symbol} Daily Returns")
        plt.show()
    else:
        print("Not enough data to calculate metrics.")

except Exception as e:
    print(f"An error occurred during analysis: {e}")
