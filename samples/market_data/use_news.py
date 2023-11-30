"""Demonstrates how to use the CryptoHistoricalData service from the Alpaca API."""

from configparser import ConfigParser
from alpaca.data.requests import NewsRequest
from alpaca.data.historical.news import NewsClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('.config/config.ini')

# Get the specified credentials.
api_key = config.get('alpaca', 'api_key')
secret_key = config.get('alpaca', 'api_secret')

# Initialize the NewsClient.
news_data_client = NewsClient(
    api_key=api_key,
    secret_key=secret_key
)

# Initialize the NewsRequest. We want to get the news for Microsoft.
# We can only get a max of 50 articles.
request = NewsRequest(
    symbols='MSFT',
    limit=50
)

# Now let's get the data.
news_data = news_data_client.get_news(request)
print(news_data)

# If there are more articles, we can get them by using the next_page_token.
# We can get the next page by using the same request but with the next_page_token.
# We can keep doing this until there are no more articles.
while next_page_token := news_data.next_page_token:
    request = NewsRequest(
        symbols='MSFT',
        limit=50,
        page_token=next_page_token
    )
    news_data = news_data_client.get_news(request)
    print(news_data)
