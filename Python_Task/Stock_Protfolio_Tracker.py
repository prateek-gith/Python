import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] += quantity
        else:
            self.stocks[symbol] = {'quantity': quantity}

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
        else:
            print(f"{symbol} is not in the portfolio.")

    def track_performance(self):
        total_value = 0
        for symbol, data in self.stocks.items():
            stock = yf.Ticker(symbol)
            current_price = stock.history(period="1d")['Close'].iloc[0]
            value = current_price * data['quantity']
            print(f"{symbol}: Quantity={data['quantity']}, Current Price={current_price}, Value={value}")
            total_value += value
        print(f"Total Portfolio Value: {total_value}")

# Example usage:
portfolio = StockPortfolio()

# Add stocks to the portfolio
portfolio.add_stock("AAPL", 10)
portfolio.add_stock("GOOGL", 5)

# Track performance
portfolio.track_performance()

# Remove a stock
portfolio.remove_stock("AAPL")

# Track performance after removing a stock
portfolio.track_performance()
