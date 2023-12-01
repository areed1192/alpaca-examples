"""Demonstrates how to use the TradingClient to get corporate announcements.

This script shows an example of using the TradingClient class from the alpaca.trading.client
module to interact with the Alpaca API. It retrieves corporate announcements using the
provided API key and secret key from a configuration file. The retrieved corporate
announcements are then printed to the console.

Note:
-----
It requires a valid API key and secret key, which are read from a configuration
file named 'config.ini'.

Example usage:
    python use_corporate_announcements.py
"""
from datetime import date
from configparser import ConfigParser
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import CorporateActionType
from alpaca.trading.requests import GetCorporateAnnouncementsRequest


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

# Let's grab the corporate announcements for Microsoft.
# We'll only grab the dividends from 2023-09-01 to 2023-11-30.
request = GetCorporateAnnouncementsRequest(
    ca_types=[CorporateActionType.DIVIDEND],
    since=date(year=2023, month=9, day=1),
    until=date(year=2023, month=11, day=30),
    symbol="MSFT"
)

# Make the request and print the data.
ca_data = trading_client.get_corporate_announcements(filter=request)
print(ca_data)

# Let's grab a specific corporate announcement, by just taking the ID from the
# first corporate announcement in the list.
ca_data = trading_client.get_corporate_announcement_by_id(
    corporate_announcment_id=ca_data[0].id
)
print(ca_data)
