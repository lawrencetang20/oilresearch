import matplotlib.pyplot as plt
from setup import matching, statista_data, investing_com_data, bloomberg_data, treasury_data, datastream_data
from data_functions import getNextLowestDate


def getAverage(matching, statista, investing_com, bloomberg, treasury, datastream):
  average = [round(sum((statista[i], investing_com[i], bloomberg[i]), datastream[i])/4,2) for i in range(len(matching))]
  return average

def plotAverage(matching, average):
  date1 = getNextLowestDate('02/24/22', matching)
  date2 = getNextLowestDate('12/5/22', matching)
  date3 = getNextLowestDate('10/12/23', matching)
  date4 = getNextLowestDate('11/16/23', matching)
  plt.figure(figsize=(12, 6))
  plt.plot(matching, average)
  plt.title('Urals Discounts')
  plt.xlabel('Date')
  plt.ylabel('Price Difference')
  plt.axvline(x=date1, color='red', linestyle='--')
  plt.axvline(x=date2, color='red', linestyle='--')
  plt.axvline(x=date3, color='red', linestyle='--')
  plt.axvline(x=date4, color='red', linestyle='--')
  plt.xticks(matching[::30], rotation=45)
  plt.tight_layout()
  plt.savefig('../saved_pngs/average.png')
  print('png saved')
  plt.show()

average = getAverage(matching, statista_data, investing_com_data, bloomberg_data, treasury_data, datastream_data)

if __name__ == "__main__":
  plotAverage(matching, average)
