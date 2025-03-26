import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
data = yf.download("BMW.DE", start="2020-01-01", end="2025-03-26")
data.to_csv("bmw_stock.csv")

data = pd.read_csv("bmw_stock.csv", header=3, names=['Date', 'Close', 'High', 'Low', 'Open', 'Volume'])
data.dropna(inplace=True)


data["Date"] = pd.to_datetime(data["Date"])
monthly_avg = data.groupby(data["Date"].dt.to_period("M"))["Close"].mean()


monthly_avg.plot(title="BMW Stock Price Trends")
plt.xlabel("Month")
plt.ylabel("Average Close Price (€)")
plt.show()