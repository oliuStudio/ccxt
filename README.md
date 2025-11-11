# CCXT - Modified Version with Lighter Exchange Support

A modified version of the CCXT cryptocurrency trading library with additional support for Lighter Exchange.

## Installation

You can install this package directly from GitHub:

```bash
pip install git+https://github.com/oliuStudio/ccxt.git
```

## Features

- All standard CCXT functionality
- Additional support for Lighter Exchange
- Compatible with Python 3.8+

## Usage

```python
import ccxt

# Create exchange instance
exchange = ccxt.lighter({
    'apiKey': 'your_api_key',
    'secret': 'your_secret',
    'sandbox': True,  # Use sandbox for testing
})

# Fetch markets
markets = exchange.load_markets()
print(markets)
```

## License

MIT License
