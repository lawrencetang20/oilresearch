import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from setup import matching, statista_data, investing_com_data, bloomberg_data, treasury_data, datastream_data
from setup import investing_total, statista_total, bloomberg_total, treasury_total, datastream_total
from data_functions import getNextLowestDate

def plotSeries(matching, statista, investing_com, bloomberg, treasury, datastream):
  date1 = getNextLowestDate('02/24/22', matching)
  date2 = getNextLowestDate('12/5/22', matching)
  date3 = getNextLowestDate('10/12/23', matching)
  date4 = getNextLowestDate('11/16/23', matching)
  plt.figure(figsize=(12, 6))
  plt.plot(matching, statista, label='Statista')
  plt.plot(matching, investing_com, label='Investing.com')
  plt.plot(matching, bloomberg, label='Bloomberg')
  plt.plot(matching, datastream, label = 'Datastream')  
  plt.plot(matching, treasury, label = 'Treasury')
  plt.title('Urals Discounts')
  plt.xlabel('Date')
  plt.ylabel('Price Difference ($/bbl)')
  plt.axvline(x=date1, color='red', linestyle='--')
  plt.axvline(x=date2, color='red', linestyle='--')
  # plt.axvline(x=date3, color='red', linestyle='--')
  plt.axvline(x=date4, color='red', linestyle='--')
  plt.xticks(matching[::30], rotation=45)
  plt.legend(loc='upper right')
  plt.tight_layout()
  plt.savefig('../../saved_pngs/figure_4/series_matching.png')
  print('png saved')
  plt.show()

def plotSeriesExtended(investing_total, statista_total, bloomberg_total, treasury_total, datastream_total, no_treasury):
  dates_investing, prices_investing = investing_total
  dates_statista, prices_statista = statista_total
  dates_bloomberg, prices_bloomberg = bloomberg_total
  dates_treasury, prices_treasury = treasury_total
  dates_datastream, prices_datastream = datastream_total

  if not no_treasury:
    datasets = [
      (dates_statista, prices_statista, 'Statista'),
      (dates_investing, prices_investing, 'Investing.com'),
      (dates_bloomberg, prices_bloomberg, 'Bloomberg'),
      (dates_datastream, prices_datastream, 'Datastream'),
      (dates_treasury, prices_treasury, 'Treasury'),
    ]
  else:
    datasets = [
      (dates_statista, prices_statista, 'Statista'),
      (dates_investing, prices_investing, 'Investing.com'),
      (dates_bloomberg, prices_bloomberg, 'Bloomberg'),
      (dates_datastream, prices_datastream, 'Datastream'),
    ]

  common_index = pd.to_datetime(datasets[0][0], format='%m/%d/%y')

  plt.figure(figsize=(12, 6))

  for dates, prices, label in datasets[1:]:
    dates = [datetime.strptime(date, '%m/%d/%y') for date in dates]
    common_index = common_index.union(pd.to_datetime(dates, format='%m/%d/%y'))

  for dates, prices, label in datasets:
    dates = [datetime.strptime(date, '%m/%d/%y') for date in dates]
    series_data = pd.Series(index=dates, data=prices)

    series_resampled = series_data.reindex(common_index).interpolate(method='linear')
    series_resampled = series_resampled.ffill().bfill()

    dates_resampled = series_resampled.index
    prices_resampled = series_resampled.values

    max_original_date = max(series_data.index)
    if max_original_date in dates_resampled:
      index = dates_resampled.get_loc(max_original_date)
      dates_resampled = dates_resampled[:index + 1]
      prices_resampled = prices_resampled[:index + 1]

    plt.plot(dates_resampled, prices_resampled, label=label)
    print(f"{label} ends on: {max_original_date}")
    plt.legend(loc='upper right')

  plt.axvline(x=pd.to_datetime('02/24/22', format='%m/%d/%y'), color='red', linestyle='--', label='Vertical Line')
  plt.axvline(x=pd.to_datetime('12/5/22', format='%m/%d/%y'), color='red', linestyle='--', label='Vertical Line')
  # plt.axvline(x=pd.to_datetime('10/12/23', format='%m/%d/%y'), color='red', linestyle='--', label='Vertical Line')
  plt.axvline(x=pd.to_datetime('11/16/23', format='%m/%d/%y'), color='red', linestyle='--', label='Vertical Line')
  plt.title('Urals Discounts')
  plt.xlabel('Date')
  plt.ylabel('Price Difference ($/bbl)')
  plt.tight_layout()
  if not no_treasury:
    plt.savefig('../../saved_pngs/figure_4/series_extended_with_treasury.png')
    print('png saved')
  else:
    plt.savefig('../../saved_pngs/figure_4/series_extended_no_treasury.png')
    print('png saved')
  
  plt.show()

if __name__ == "__main__":
  plotSeries(matching, statista_data, investing_com_data, bloomberg_data, treasury_data, datastream_data)
  ## MAKE TRUE INSTEAD OF FALSE IN ORDER TO DO NO TREASURY
  plotSeriesExtended(investing_total, statista_total, bloomberg_total, treasury_total, datastream_total, False)