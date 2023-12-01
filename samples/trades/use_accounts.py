from configparser import ConfigParser
from alpaca.trading.client import TradingClient

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

# Let's grab the account
account = trading_client.get_account()
print(account.model_dump())

# Let's grab the account configurations
account_configurations = trading_client.get_account_configurations()
print(account_configurations.model_dump())
