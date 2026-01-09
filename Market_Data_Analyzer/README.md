# Market Data Downloader & Analyzer

A Python-based tool to analyze historical market data, compute returns and volatility, and visualize asset performance.

## Features
- **Data Collection**: Downloads daily adjusted close prices using `yfinance`.
- **Metrics**: Calculates Daily Returns, Daily Volatility, and Annualized Volatility.
- **Visualization**: Plots closing prices and daily returns.
- **Interfaces**: 
  - **CLI**: Simple command-line interface.
  - **Streamlit**: Interactive web dashboard.

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Command Line Interface (CLI)
Run the script directly in your terminal:
```bash
python app.py
```
Follow the prompts to enter the ticker symbol and start date.

### 2. Streamlit Web App
Run the interactive dashboard:
```bash
streamlit run streamlit_app.py
```

### Ticker Symbology
Enter the ticker symbol compatible with Yahoo Finance.
- **US Stocks**: `AAPL`, `GOOGL`, `TSLA`
- **Indian Stocks (NSE)**: Add `.NS` suffix (e.g., `RELIANCE.NS`, `TCS.NS`)
- **Indian Stocks (BSE)**: Add `.BO` suffix (e.g., `RELIANCE.BO`)

## Project Structure
- `app.py`: CLI entry point.
- `streamlit_app.py`: Streamlit application.
- `src/`: Core logic modules (`downloader`, `metrics`, `visualization`).
