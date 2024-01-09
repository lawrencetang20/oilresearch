
import requests
import csv
import matplotlib.pyplot as plt
import mplcursors
from datetime import datetime

start = '2022-01-01'
end = '2023-12-22'
csvname = 'excel_csv/crudeoil.csv'

response = requests.get(f'http://api.scraperlink.com/investpy/?email=tangla@mit.edu&type=historical_data&product=commodities&from_date={start}&to_date={end}&time_frame=Daily&name=crude')

# check if app connected, 200 if connected
if response.status_code == 200:
  print("API connected")

brent_data = response.json()

brent_prices = [float(entry['last_close']) for entry in brent_data['data']]
dates = [entry['rowDate'] for entry in brent_data['data']]

brent_dates = []

for date_str in dates:
  date_object = datetime.strptime(date_str, '%b %d, %Y')
  formatted_date = date_object.strftime('%m/%d/%Y')
  brent_dates.append(formatted_date)

urals_prices = []
urals_dates = []

with open(csvname, newline = '') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    urals_prices.append(float(row['Price']))
    urals_dates.append(row['\ufeff"Date"'])

brent_prices.reverse()
brent_dates.reverse()
urals_prices.reverse()
urals_dates.reverse()

common_dates = [date for date in urals_dates if date in brent_dates]

price_difference = [round(urals_prices[urals_dates.index(date)] - brent_prices[brent_dates.index(date)], 2) for date in common_dates]
rolling_average = [0 for i in range(len(price_difference))]

for i in range(len(price_difference)):
  start = max(i-4,0)
  end = min(len(price_difference)-1, i)
  rolling_average[i] = sum(price_difference[start:end+1])/(end+1-start)

shortened_dates = [date[:len(date)-4]+date[len(date)-2:] for date in common_dates]

csvname = 'excel_csv/statistica_data.csv'

prices = []
dates = []

with open(csvname, newline = '') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    prices.append(float(row['Discount']))
    dates.append(row['\ufeffDate'])

matching = [date for date in shortened_dates if date in dates]

statistica = [prices[dates.index(date)] for date in matching]
investing_com = [price_difference[shortened_dates.index(date)] for date in matching]

disparity = [investing_com[i]-statistica[i] for i in range(len(matching))]

plt.plot(matching, statistica, label='Statistica')
plt.plot(matching, investing_com, label='Investing.com')
plt.title('Price Difference between Urals and Brent')
plt.xlabel('Date')
plt.ylabel('Price Difference')
plt.xticks(matching[::30], rotation=45)

plt.axvline(matching.index('04/17/23'), color='red', linestyle= '--')
plt.axvline(matching.index('10/12/23'), color='red', linestyle= '--')
plt.axvline(matching.index('11/16/23'), color='red', linestyle= '--')

plt.legend()
plt.tight_layout()

plt.figure()
plt.plot(matching, disparity)
plt.title('Difference between statistica and investing')
plt.xlabel('Date')
plt.ylabel('Price Difference')
plt.xticks(matching[::30], rotation=45)


plt.show()