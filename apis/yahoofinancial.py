from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt

# tech_stocks = ['AAPL', 'MSFT', 'INTC']
# yahoo_financials_tech = YahooFinancials(tech_stocks)
# print(yahoo_financials_tech.get_historical_price_data("2018-08-01", "2018-08-10", "weekly"))

start_date = "2022-02-01"
end_date = "2023-12-24"

oil_names = ['BZ=F', 'CL=F']
oils = YahooFinancials(oil_names)
response = oils.get_historical_price_data(start_date, end_date, "daily")

brent = response['BZ=F']
urals = response['CL=F']

# dates
dates = [price_data['formatted_date'] for price_data in brent['prices']]

# open prices
brent_prices = [round(price_data['open'], 3) for price_data in brent['prices']]
urals_prices = [round(price_data['open'], 3) for price_data in urals['prices']]

difference = [urals_prices[i] - brent_prices[i] for i in range(len(brent_prices))]

plt.figure(figsize=(10, 6))
plt.plot(dates, difference, label='Urals - Brent Price Difference')
plt.axhline(0, color='black', linestyle='--', linewidth=1, label='Zero Difference')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Price Difference')
plt.title('Urals - Brent Price Difference Over Time')
plt.xticks([])

# Adding a legend
plt.legend()


# Display the plot
plt.tight_layout()
plt.show()