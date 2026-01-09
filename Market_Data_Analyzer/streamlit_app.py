# Import necessary modules
import streamlit as st
import src.metrics as mt
import src.visualization as vis
import src.downloader as dw
import os
import sys
from datetime import datetime

# Add 'src' directory to system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Page Configuration
st.set_page_config(
    page_title="Market Data Analyzer",
    layout="wide"
)

# Header
st.title("Market Data Downloader & Analyzer")
st.markdown("Analyze stock market data with volatility and return metrics.")
st.markdown("---")

# Layout: Inputs
col1, col2 = st.columns(2)

with col1:
    ticker_symbol = st.text_input(
        "Enter Ticker Symbol (e.g., AAPL):",
        "AAPL",
        help="Use suffix .NS for NSE or .BO for BSE (e.g., RELIANCE.NS, TCS.BO)"
    ).strip().upper()

with col2:
    start_date = st.date_input("Start Date:", datetime(2025, 1, 1))

# Validation & Execution
if st.button("Calculate Metrics", type="primary"):
    if not ticker_symbol:
        st.error("Please enter a valid ticker symbol.")
    else:
        with st.spinner(f"Downloading data for {ticker_symbol}..."):
            try:
                # Convert date object to string YYYY-MM-DD
                start_date_str = start_date.strftime("%Y-%m-%d")
                data = dw.download_data(
                    ticker_symbol, start_date=start_date_str)

                if data.empty:
                    st.error(
                        f"No data found for {ticker_symbol} from {start_date_str}.")
                else:
                    # Calculations
                    day_returns = mt.daily_returns(data)
                    daily_vol = mt.daily_volatility(day_returns)

                    if daily_vol.empty:
                        st.warning("Not enough data to calculate volatility.")
                    else:
                        daily_vol_float = daily_vol.iloc[0]
                        annual_returns = mt.annual_returns(daily_vol)
                        annual_returns_float = annual_returns.iloc[0]

                        # Display Metrics
                        st.markdown("### Key Metrics")
                        m_col1, m_col2 = st.columns(2)
                        m_col1.metric("Daily Volatility",
                                      f"{daily_vol_float*100:.2f}%")
                        m_col2.metric("Annual Returns",
                                      f"{annual_returns_float*100:.2f}%")

                        st.markdown("---")

                        # Visualization
                        st.markdown("### Charts")
                        fig1 = vis.plot(
                            data['Close'], title=f"{ticker_symbol} Closing Prices")
                        st.pyplot(fig1)
                        fig2 = vis.plot(
                            day_returns, title=f"{ticker_symbol} Daily Returns")
                        st.pyplot(fig2)

            except Exception as e:
                st.error(f"An error occurred: {e}")
