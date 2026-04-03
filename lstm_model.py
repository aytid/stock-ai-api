import yfinance as yf
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model


model = load_model("stock_lstm_model.h5")


def predict_stock(ticker):

    df = yf.download(ticker, period="2y")

    data = df[['Close']]

    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(data)

    last_60_days = scaled_data[-60:]

    X = np.array([last_60_days])

    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    prediction = model.predict(X)

    prediction = scaler.inverse_transform(prediction)

    return float(prediction[0][0])