"""Demonstrates how to use the CryptoHistoricalData service from the Alpaca API.

This script showcases the usage of the CryptoHistoricalData service from the Alpaca
API. It demonstrates how to retrieve historical data, such as bars, trades, and
orderbook snapshots, for a specified cryptocurrency symbol within a given time range.

The script utilizes the CryptoHistoricalDataClient class from the Alpaca Python SDK
to interact with the Alpaca API. It requires a valid API key and secret key, which
are read from a configuration file named 'config.ini'.
"""

from datetime import datetime
from configparser import ConfigParser
from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.requests import CryptoTradesRequest
from alpaca.data.requests import CryptoSnapshotRequest
from alpaca.data.requests import CryptoLatestOrderbookRequest
from alpaca.data.historical import CryptoHistoricalDataClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('.config/config.ini')

# Get the specified credentials.
api_key = config.get('alpaca', 'api_key')
secret_key = config.get('alpaca', 'api_secret')

# Initialize the CryptoHistoricalDataClient.
crypto_data_client = CryptoHistoricalDataClient(
    api_key=api_key,
    secret_key=secret_key
)

# Now let's define a request using the CryptoBarsRequest class.
# We'll get the bars for the stock 'BTC/USD' from 2023-11-01 to 2023-11-10.
# Limit the number of bars to 1000 and set the timeframe to 1 hour.
request = CryptoBarsRequest(
    symbol_or_symbols=['BTC/USD'],
    start=datetime(year=2023, month=11, day=1).date(),
    end=datetime(year=2023, month=11, day=10).date(),
    timeframe=TimeFrame.Hour,
    limit=1000
)

# Now let's get the data.
bar_data = crypto_data_client.get_crypto_bars(request_params=request)

# Let's print the data.
print(bar_data)

# Just like with the StockHistoricalDataClient, I can return the data as a
# dataframe.
print(bar_data.df)

# Let's define the request to grab the latest orderbook for the stock 'BTC/USD'.
request = CryptoLatestOrderbookRequest(
    symbol_or_symbols=['BTC/USD']
)

# Send the request and print the data.
book_data = crypto_data_client.get_crypto_latest_orderbook(request_params=request)
print(book_data)

# Let's define the request to grab the trades for the stock 'BTC/USD'.
request = CryptoTradesRequest(
    symbol_or_symbols=['BTC/USD'],
    start=datetime(year=2023, month=11, day=1).date(),
    end=datetime(year=2023, month=11, day=10).date(),
    limit=1000
)

# Send the request and print the data.
trade_data = crypto_data_client.get_crypto_trades(request_params=request)
print(trade_data)

# Let's define the request to grab the snapshot for the stock 'BTC/USD'.
# Snapshots contain latest trade, latest quote, latest minute bar, latest
# daily bar and previous daily bar data for the queried symbols.
request = CryptoSnapshotRequest(
    symbol_or_symbols=['BTC/USD']
)

snapshot_data = crypto_data_client.get_crypto_snapshot(request_params=request)
print(snapshot_data)
