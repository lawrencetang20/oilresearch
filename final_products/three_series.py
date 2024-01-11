import matplotlib.pyplot as plt
from setup import matching, statista_data, investing_com_data, bloomberg_data
from data_functions import getNextLowestDate

def plotSeries(matching, statista, investing_com, bloomberg):
  date1 = getNextLowestDate('02/24/22', matching)
  date2 = getNextLowestDate('12/5/22', matching)
  date3 = getNextLowestDate('10/12/23', matching)
  date4 = getNextLowestDate('11/16/23', matching)
  plt.figure(figsize=(12, 6))
  plt.plot(matching, statista, label='Statista')
  plt.plot(matching, investing_com, label='Investing.com')
  plt.plot(matching, bloomberg, label='Bloomberg')
  plt.title('Urals Discounts')
  plt.xlabel('Date')
  plt.ylabel('Price Difference')
  plt.axvline(x=date1, color='red', linestyle='--')
  plt.axvline(x=date2, color='red', linestyle='--')
  plt.axvline(x=date3, color='red', linestyle='--')
  plt.axvline(x=date4, color='red', linestyle='--')
  plt.xticks(matching[::30], rotation=45)
  plt.legend(loc='upper right')
  plt.tight_layout()
  plt.savefig('../saved_pngs/three_series.png')
  print('png saved')
  plt.show()


if __name__ == "__main__":
  plotSeries(matching, statista_data, investing_com_data, bloomberg_data)
