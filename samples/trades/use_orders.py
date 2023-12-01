"""Demonstrates how to use the TradingClient to create, submit, delete, query, and replace orders.

This script shows an example of using the TradingClient class from the alpaca.trading.client
module to interact with the Alpaca API. It creates an order request, submits the order,
queries the order, replaces the order, and finally deletes the order.

Note:
-----
It requires a valid API key and secret key, which are read from a configuration
file named 'config.ini'.

Example usage:
    python use_orders.py
"""
from configparser import ConfigParser
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import OrderRequest
from alpaca.trading.enums import OrderSide
from alpaca.trading.enums import OrderType
from alpaca.trading.enums import OrderClass
from alpaca.trading.enums import TimeInForce

# Day (DAY)
# Good 'Til Canceled (GTC)
# Fill or Kill (FOK) 
# Immediate or Cancel (IOC)
# Submit On Market Open (OPG)
# Submit On Market Close (CLS)

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('.config/config.ini')

# Get the specified credentials.
api_key = config.get('alpaca', 'api_key')
secret_key = config.get('alpaca', 'api_secret')

# Initialize the TradingClient.
trading_client = TradingClient(
    api_key=api_key,
    secret_key=secret_key,
    paper=True
)

# Let's define a new order request.
order_request = OrderRequest(
    symbol="MSFT",
    qty=10.0,
    side=OrderSide.BUY,
    type=OrderType.MARKET,
    order_class=OrderClass.SIMPLE,
    time_in_force=TimeInForce.DAY,
    extended_hours=False
)

# Now we can submit the order.
order_submission_response = trading_client.submit_order(order_data=order_request)
print(order_submission_response)
