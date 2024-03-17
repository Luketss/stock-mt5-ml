import yfinance as yf

petra = "PETR4.SA"


class Yahoo:
    def __init__(self):
        pass

    def get_stock_history(self, stock_code):
        ticker = yf.Ticker(stock_code)
        hist = ticker.history(period="1mo")
        return hist


if __name__ == "__main__":
    yahoo = Yahoo()
