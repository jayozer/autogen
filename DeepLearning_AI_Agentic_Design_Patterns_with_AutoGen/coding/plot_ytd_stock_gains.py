# filename: plot_ytd_stock_gains.py

import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Define the stock tickers
stocks = ['NVDA', 'TSLA']

# Define the start and end dates for the YTD
start_date = "2024-01-01"
end_date = "2024-07-13"

# Download the stock data
data = yf.download(stocks, start=start_date, end=end_date)['Adj Close']

# Calculate YTD gains
ytd_gains = (data / data.iloc[0] - 1) * 100

# Plot the data
plt.figure(figsize=(10, 6))
for stock in stocks:
    plt.plot(ytd_gains.index, ytd_gains[stock], label=stock)

plt.title('Year-to-Date (YTD) Stock Gains for NVDA and TSLA')
plt.xlabel('Date')
plt.ylabel('YTD Gain (%)')
plt.legend()
plt.grid(True)
plt.savefig('ytd_stock_gains.png')

print("The plot has been saved as ytd_stock_gains.png")