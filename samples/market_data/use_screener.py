"""Demonstrates how to use the ScreenerClient service from the Alpaca API.

This Python script demonstrates how to use the Alpaca API to fetch and print data
about the most active stocks and market movers. It shows how to initialize the
ScreenerClient, create a MostActivesRequest or MarketMoversRequest object with
the desired parameters, and retrieve the data using the get_most_actives or
get_market_movers methods.

Note:
-----
It requires a valid API key and secret key, which are read from a configuration
file named 'config.ini'.

Example usage:
    python use_screener.py
"""

from configparser import ConfigParser
from alpaca.data.requests import MostActivesRequest
from alpaca.data.requests import MarketMoversRequest
from alpaca.data.enums import MostActivesBy  
from alpaca.data.enums import MarketType
from alpaca.data.historical.screener import ScreenerClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('.config/config.ini')

# Get the specified credentials.
api_key = config.get('alpaca', 'api_key')
secret_key = config.get('alpaca', 'api_secret')

# Initialize the ScreenerClient.
screener_client = ScreenerClient(
    api_key=api_key,
    secret_key=secret_key
)

# Initialize the MostActivesRequest. We want to get the top 20 most 
# active stocks by volume.
most_actives_request = MostActivesRequest(
    top=20,
    by=MostActivesBy.VOLUME
)

# Now let's get the data.
most_actives_data = screener_client.get_most_actives(most_actives_request)
print(most_actives_data)

# Let's define the request to get the top 20 gainers.
market_movers_request = MarketMoversRequest(
    top=20,
    market_type=MarketType.STOCKS
)

# Now let's get the data.
market_movers_data = screener_client.get_market_movers(market_movers_request)
print(market_movers_data.gainers)
print(market_movers_data.losers)
