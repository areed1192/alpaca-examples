from configparser import ConfigParser
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

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

# search for crypto assets
request_crypto = GetAssetsRequest(
    asset_class=AssetClass.CRYPTO,
)

# search for stocks assets
request_stocks = GetAssetsRequest(
    asset_class=AssetClass.US_EQUITY,
)

# get all crypto assets
assets = trading_client.get_all_assets(request_crypto)
print(assets)

# get all stocks assets
assets = trading_client.get_all_assets(request_stocks)
print(assets)

# Grab a specific asset
asset = trading_client.get_asset(symbol_or_asset_id="MSFT")
print(asset)
