# Alpaca API Examples

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Example Files](#example-files)
- [Support These Projects](#support-these-projects)

## Overview

Alpaca is a technology company that offers various services related to stock and crypto trading. They
provide simple, modern API-first solutions for individuals and businesses to connect applications and
build algorithms to buy and sell stocks or crypto.

Alpaca-py provides an interface for interacting with the API products Alpaca offers. These API products
are provided as various REST, WebSocket and SSE endpoints that allow you to do everything from
streaming market data to creating your own investment apps.

## Setup

**Setup - Requirements Install:**

For this particular project, you only need to install the dependencies, to use the project. The dependencies
are listed in the `requirements.txt` file and can be installed by running the following command:

```console
pip install -r requirements.txt
```

After running that command, the dependencies should be installed.

## Example Files

**Market Data:**

- `use_crypto.py`
  - Demonstrates how to use the CryptoHistoricalData service from the Alpaca API.
- `use_news.py`
  - Demonstrates how to use the NewsRequest service from the Alpaca API.
- `use_screener.py`
  - Demonstrates how to use the ScreenerClient service from the Alpaca API.
- `use_stocks.py`
  - Demonstrates how to use the StockHistoricalData service from the Alpaca API.

**Trading:**

- `use_accounts.py`
  - Demonstrates how to use the TradingClient to get the account and account configurations.
- `use_assets.py`
  - Demonstrates how to use the TradingClient to get asset information.
- `use_corporate_accouncements.py`
  - Demonstrates how to use the TradingClient to get corporate announcements.
- `use_orders.py`
  - Demonstrates how to use the TradingClient to create, submit, delete, query, and replace orders.

## Support These Projects

**Patreon:**
Help support this project and future projects by donating to my [Patreon Page](https://www.patreon.com/sigmacoding). I'm
always looking to add more content for individuals like yourself, unfortuantely some of the APIs I would require me to
pay monthly fees.

**YouTube:**
If you'd like to watch more of my content, feel free to visit my YouTube channel [Sigma Coding](https://www.youtube.com/c/SigmaCoding).
