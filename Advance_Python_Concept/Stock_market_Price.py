import requests

API_KEY = 'YOUR_API_KEY'

def get_stock_price(symbol):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if 'Global Quote' in data:
            price = float(data['Global Quote']['05. price'])
            return price
        else:
            print(f"No stock data found for symbol: {symbol}")
            return None

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Example usage for multiple symbols
if __name__ == "__main__":
    symbols = ['AAPL', 'MSFT', 'GOOGL', 'TSLA']

    for symbol in symbols:
        stock_price = get_stock_price(symbol)
        if stock_price is not None:
            print(f"Current price of {symbol}: ${stock_price:.2f}")
        else:
            print(f"Failed to retrieve stock price for {symbol}")



    """
    1.Sign up for an API key: Visit the Alpha Vantage website to sign up and get your API key. This key is necessary to authenticate your requests.

    2.Install requests library: If you haven't already, install the requests library using pip: pip install requests
    
    
    
   What Is The Mean of :  price = data['Global Quote']['05. price']

    The line price = data['Global Quote']['05. price'] in the context of fetching stock market data from the Alpha Vantage API refers to accessing the current price of a stock from the JSON response returned by the API.

    Here a breakdown of how this works:

    API Response Structure: When you make a request to Alpha Vantage's API with the GLOBAL_QUOTE function for a specific stock symbol, the response JSON typically contains nested data structures.

    JSON Response Example:

    json
    Copy code
    {
        "Global Quote": {
            "01. symbol": "AAPL",
            "02. open": "149.8000",
            "03. high": "150.6800",
            "04. low": "149.3600",
            "05. price": "150.1900",
            "06. volume": "122175551",
            "07. latest trading day": "2024-07-20",
            "08. previous close": "149.9800",
            "09. change": "0.2100",
            "10. change percent": "0.1401%"
        }
    }
    Accessing the Price:

    In the JSON response, "Global Quote" is a key that contains another dictionary.
    Within "Global Quote", "05. price" is a key that holds the current price of the stock as a string (formatted to two decimal places).
    Extracting the Price:

    data['Global Quote']['05. price'] accesses the value associated with the key "05. price" within the "Global Quote" dictionary.
    Since this value is a string representing the stock price, you might want to convert it to a float if numerical operations are needed (float(data['Global Quote']['05. price'])).
    """