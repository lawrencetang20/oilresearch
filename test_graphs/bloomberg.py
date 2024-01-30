import csv
import matplotlib.pyplot as plt
import mplcursors

"""

INSTALLATIONS
pip install mplcursors
pip install matplotlib

"""

csvname = '../excel_csv/figure_4/bloomberg_urals_brent.csv'

prices = []
dates = []

with open(csvname, newline = '') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    prices.append(float(row['Discount']))
    dates.append(row['\ufeffDates'])

plt.plot(dates, prices)
plt.title('Price Difference between Urals and Brent')
plt.xlabel('Date')
plt.ylabel('Price Difference')
plt.xticks(dates[::30], rotation=45)
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