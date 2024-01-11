import sys
sys.path.append('/Users/lawrencetang/Desktop/Internships:Research/UROP/oilresearch')

from final_products import data_functions as data
import matplotlib.pyplot as plt

print("here")

bloomberg_brent = '../excel_csv/bloomberg_brent.csv'
start = '2022-01-01'
end = '2024-01-10'
link = f'http://api.scraperlink.com/investpy/?email=tangla@mit.edu&type=historical_data&product=commodities&from_date={start}&to_date={end}&time_frame=Daily&name=crude'


bloomberg_data = data.bloombergData(bloomberg_brent)
investing_data = data.investingAPI(link)

dates_investing, prices_investing = investing_data
dates_bloomberg, prices_bloomberg = bloomberg_data

matching = [date for date in dates_investing if date in dates_bloomberg]

investing_com = [prices_investing[dates_investing.index(date)] for date in matching]
bloomberg = [prices_bloomberg[dates_bloomberg.index(date)] for date in matching]
price_difference = [ic - bb for ic, bb in zip(investing_com, bloomberg)]


plt.plot(matching, investing_com, label='Investing.com')
plt.plot(matching, bloomberg, label='Bloomberg')
plt.plot(matching, price_difference, label='Investing.com - Bloomberg')

plt.title('Brent Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(matching[::30], rotation=45)
plt.legend()
plt.tight_layout()
plt.show()