import requests
import csv
import matplotlib.pyplot as plt
import mplcursors
from datetime import datetime

"""

INSTALLATIONS
pip install mplcursors
pip install investpy
pip install requests
pip install matplotlib

api used: https://api.scraperlink.com/investpy/

commodities:
- country= (if not using 'id')
* id=, or name=
Example: http://api.scraperlink.com/investpy/?email=your@email.com&type=historical_data&product=commodities&from_date=2022-11-08&to_date=2022-11-09&time_frame=Daily&name=gold

https://www.investing.com/commodities/crude-oil-urals-spot-futures-historical-data

name=brent for brent oil futures

"""

start = '2022-01-01'
end = '2023-12-22'
csvname = '../excel_csv/figure_4/crudeoil.csv'

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
  start = max(i,0)
  end = min(len(price_difference)-1, i+4)
  rolling_average[i] = sum(price_difference[start:end+1])/(end+1-start)

plt.plot(common_dates, rolling_average)
plt.title('Price Difference between Urals and Brent')
plt.xlabel('Date')
plt.ylabel('Price Difference')
plt.xticks(common_dates[::30], rotation=45)
plt.tight_layout()

while(True):
  print('Do you want to trace data points (Y/N then press enter)? If type exit, then program will terminate.')
  x = input()
  if x == 'Y':
    on = True
    break
  elif x == 'N':
    on = False
    break
  elif x == 'exit':
    quit()
    
cursor = mplcursors.cursor(hover=on)
plt.show()
