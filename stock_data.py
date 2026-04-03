import yfinance as yf

def get_stock_history(ticker):

    stock = yf.Ticker(ticker)

    df = stock.history(period="1y")

    df.reset_index(inplace=True)

    data = []

    for _, row in df.iterrows():
        data.append({
            "date": str(row["Date"]),
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"])
        })

    return data