# filename: stock_prices_YTD_plot_doma_hippo.py

from functions import get_stock_prices, plot_stock_prices
import datetime

# Step 1: Get today's date and set the start date to the beginning of the year
today = datetime.date(2024, 7, 13)
start_date = datetime.date(2024, 1, 1)
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = today.strftime('%Y-%m-%d')

# Step 2: Retrieve the stock prices for DOMA and HIPPO
stock_symbols = ['DOMA', 'HIPPO']
stock_prices = get_stock_prices(stock_symbols, start_date_str, end_date_str)

# Step 3: Plot the stock prices and save to a file
plot_stock_prices(stock_prices, 'stock_prices_YTD_plot_doma_hippo.png')

print("The stock prices YTD plot for DOMA and HIPPO has been saved as 'stock_prices_YTD_plot_doma_hippo.png'.")