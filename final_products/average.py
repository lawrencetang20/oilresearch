import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from setup import matching, statista_data, investing_com_data, bloomberg_data, treasury_data, datastream_data
from setup import investing_total, statista_total, bloomberg_total, treasury_total, datastream_total
from data_functions import getNextLowestDate


def getAverage(matching, statista, investing_com, bloomberg, treasury, datastream):
  average = [round(sum((statista[i], investing_com[i], bloomberg[i], datastream[i]))/4,3) for i in range(len(matching))]
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
  plt.ylabel('Price Difference ($/bbl)')
  plt.axvline(x=date1, color='red', linestyle='--')
  plt.axvline(x=date2, color='red', linestyle='--')
  # plt.axvline(x=date3, color='red', linestyle='--')
  plt.axvline(x=date4, color='red', linestyle='--')
  plt.xticks(matching[::30], rotation=45)
  plt.tight_layout()
  plt.savefig('../saved_pngs/average_matching_no_treasury.png')
  print('png saved')
  plt.show()

def plotAverageExtended(investing_total, statista_total, bloomberg_total, treasury_total, datastream_total):
  dates_investing, prices_investing = investing_total
  dates_statista, prices_statista = statista_total
  dates_bloomberg, prices_bloomberg = bloomberg_total
  dates_treasury, prices_treasury = treasury_total
  dates_datastream, prices_datastream = datastream_total


  datasets = [
    (dates_statista, prices_statista, 'Statista'),
    (dates_investing, prices_investing, 'Investing.com'),
    (dates_bloomberg, prices_bloomberg, 'Bloomberg'),
    (dates_datastream, prices_datastream, 'Datastream'),
  ]

  average_series_data = {}

  for dates, prices, label in datasets:
    for date, price in zip(dates, prices):
      date = datetime.strptime(date, '%m/%d/%y')
      if date not in average_series_data:
        average_series_data[date] = [price]
      else:
        average_series_data[date].append(price)

  average_dates = []
  average_prices = []

  for date, prices_list in average_series_data.items():
    average_dates.append(date)
    average_prices.append(sum(prices_list) / len(prices_list))

  average_df = pd.DataFrame({'Date': average_dates, 'Average': average_prices})
  average_df.sort_values(by='Date', inplace=True)
  average_df.set_index('Date', inplace=True)

  plt.figure(figsize=(12, 6))
  plt.plot(average_df.index, average_df['Average'], label='Average')
  plt.axvline(x=pd.to_datetime('02/24/22', format='%m/%d/%y'), color='red', linestyle='--', label='Vertical Line')
  plt.axvline(x=pd.to_datetime('12/5/22', format='%m/%d/%y'), color='red', linestyle='--', label='Vertical Line')
  # plt.axvline(x=pd.to_datetime('10/12/23', format='%m/%d/%y'), color='red', linestyle='--', label='Vertical Line')
  plt.axvline(x=pd.to_datetime('11/16/23', format='%m/%d/%y'), color='red', linestyle='--', label='Vertical Line')
  plt.title('Urals Discounts Average')
  plt.xlabel('Date')
  plt.ylabel('Price Difference ($/bbl)')
  plt.tight_layout()
  plt.savefig('../saved_pngs/average_extended_no_treasury.png')
  print('png saved')
  plt.show()

average = getAverage(matching, statista_data, investing_com_data, bloomberg_data, treasury_data, datastream_data)

if __name__ == "__main__":
  plotAverage(matching, average)
  plotAverageExtended(investing_total, statista_total, bloomberg_total, treasury_total, datastream_total)
