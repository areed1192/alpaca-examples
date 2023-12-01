"""Demonstrates how to use the StockHistoricalData service from the Alpaca API.

This script showcases the usage of the StockHistoricalDataClient class from the
Alpaca API to retrieve historical stock data and latest stock information. It
demonstrates how to make requests for stock quotes, stock bars, and the latest
bar for a specific stock.

The script reads API credentials from a configuration file, initializes the
StockHistoricalDataClient, and makes requests using the StockQuotesRequest,
StockBarsRequest, and StockLatestBarRequest classes. The retrieved data is
then printed to the console.

Note:
-----
It requires a valid API key and secret key, which are read from a configuration
file named 'config.ini'. The code contains commented-out print statements that
demonstrate different ways to access and display the retrieved data.

Example usage:
    python use_stocks.py
"""

from datetime import datetime
from configparser import ConfigParser
from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import StockBarsRequest
from alpaca.data.requests import StockQuotesRequest
from alpaca.data.requests import StockLatestBarRequest
from alpaca.data.historical import StockHistoricalDataClient


# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read(".config/config.ini")

# Get the specified credentials.
api_key = config.get("alpaca", "api_key")
secret_key = config.get("alpaca", "api_secret")

# Initialize the StockHistoricalDataClient.
stock_data_client = StockHistoricalDataClient(
    api_key=api_key,
    secret_key=secret_key
)

# Now let's define a request using the StockQuotesRequest class.
# We'll get the quotes for the stock 'AAPL' from 2023-11-01 to 2023-11-10.
# We'll also limit the number of quotes to 1000 otherwise we could be waiting
# for a while to get the data.
request = StockQuotesRequest(
    symbol_or_symbols=["AAPL"],
    start=datetime(year=2023, month=11, day=1).date(),
    end=datetime(year=2023, month=11, day=10).date(),
    limit=1000,
)

# Now let's get the data.
data = stock_data_client.get_stock_quotes(request_params=request)

# # Let's print the data.
# print(data)

# # I can also return it as a dataframe.
# print(data.df)

# # This returns it as a dictionary.
# print(data.dict())

# Let's define a new request but this time we will request bars.
# We'll get the bars for the stock 'AAPL' from 2023-11-01 to 2023-11-10.
# We'll limit the number of bars to 1000 and we'll set the timeframe to 1 hour.
request = StockBarsRequest(
    symbol_or_symbols=["AAPL"],
    start=datetime(year=2023, month=11, day=1).date(),
    end=datetime(year=2023, month=11, day=10).date(),
    limit=1000,
    timeframe=TimeFrame.Hour,
)

# Now let's get the data.
data = stock_data_client.get_stock_bars(request_params=request)

# # Let's print the data.
# print(data.df)

# Now let's get the latest '1 minute' bar for the stock 'AAPL'.
request = StockLatestBarRequest(symbol_or_symbols=["AAPL"])

# Make the request
latest_bar = stock_data_client.get_stock_latest_bar(request_params=request)

# Let's print the data, keep in mind you get just a dict back.
print(latest_bar)
