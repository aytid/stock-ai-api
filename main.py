from fastapi import FastAPI
from stock_data import get_stock_history
from lstm_model import predict_stock

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Stock AI API running"}


@app.get("/stock/{ticker}")
def stock_history(ticker: str):

    data = get_stock_history(ticker)

    return {
        "ticker": ticker,
        "history": data
    }


@app.get("/predict/{ticker}")
def predict(ticker: str):

    price = predict_stock(ticker)

    return {
        "ticker": ticker,
        "predicted_price": price
    }