# scrape_indian_stocks.py
import yfinance as yf
import pandas as pd
import os

# Top 15 Indian companies (tickers on NSE)
tickers = [
    "RELIANCE.NS",  # Reliance
    "TCS.NS",       # Tata Consultancy Services
    "INFY.NS",      # Infosys
    "HDFCBANK.NS",  # HDFC Bank
    "ICICIBANK.NS", # ICICI Bank
    "HINDUNILVR.NS",# Hindustan Unilever
    "SBIN.NS",      # State Bank of India
    "BHARTIARTL.NS",# Bharti Airtel
    "KOTAKBANK.NS", # Kotak Mahindra Bank
    "LT.NS",        # Larsen & Toubro
    "AXISBANK.NS",  # Axis Bank
    "MARUTI.NS",    # Maruti Suzuki
    "HCLTECH.NS",   # HCL Technologies
    "ITC.NS",       # ITC
    "ONGC.NS"       # Oil & Natural Gas
]

# Create data folder
os.makedirs("data", exist_ok=True)

# Download data
for ticker in tickers:
    print(f"Downloading {ticker}...")
    df = yf.download(ticker, start="2022-01-01", end="2025-08-27")
    df.to_csv(f"data/{ticker.replace('.NS','')}.csv")
    print(f"{ticker} saved to data/{ticker.replace('.NS','')}.csv")

print("All done!")
