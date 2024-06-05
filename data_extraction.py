import yfinance as yf
import pandas as pd
import s3fs 
import json
from datetime import datetime

def stock_data():
    # Define the stock ticker, start and end dates
    ticker = "AAPL"  # Example: Apple Inc.
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    filename = "s3://kicchu-ki-bucket/AAPL_stock_data.csv"

    data = yf.download(ticker, start=start_date, end=end_date)

    data.to_csv(filename)


