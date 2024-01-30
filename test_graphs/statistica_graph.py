import csv
import matplotlib.pyplot as plt
import mplcursors

"""

INSTALLATIONS
pip install mplcursors
pip install matplotlib


April 17, 2023

October 12, 2023

November 16, 2023

"""

csvname = '../excel_csv/figure_4/statista_data.csv'

prices = []
dates = []

with open(csvname, newline = '') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    prices.append(float(row['Discount']))
    dates.append(row['\ufeffDate'])


plt.plot(dates, prices)
plt.title('Price Difference between Urals and Brent')
plt.xlabel('Date')
plt.ylabel('Price Difference')
plt.xticks(dates[::30], rotation=45)
plt.axvline(dates.index('04/17/23'), color='red', linestyle= '--')
plt.axvline(dates.index('10/12/23'), color='red', linestyle= '--')
plt.axvline(dates.index('11/16/23'), color='red', linestyle= '--')
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