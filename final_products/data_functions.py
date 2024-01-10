
import requests
import csv
import matplotlib.pyplot as plt
import mplcursors
from datetime import datetime, timedelta

def investingAPI(url):
  response = requests.get(url)
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
    brent_dates.append(formatted_date[:len(formatted_date)-4]+formatted_date[len(formatted_date)-2:])

  brent_prices.reverse()
  brent_dates.reverse()
  
  return brent_prices, brent_dates

def investingData(csvname, brent):
  brent_prices, brent_dates = brent

  urals_prices = []
  urals_dates = []

  with open(csvname, newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      urals_prices.append(float(row['Discount']))
      unformat = row['\ufeffDate']
      formatted = datetime.strptime(unformat, '%m/%d/%y').strftime('%m/%d/%y')
      urals_dates.append(formatted)

  urals_prices.reverse()
  urals_dates.reverse()

  common_dates = [date for date in urals_dates if date in brent_dates]

  price_difference = [round(urals_prices[urals_dates.index(date)] - brent_prices[brent_dates.index(date)], 2) for date in common_dates]
  rolling_average = [0 for _ in range(len(price_difference))]

  for i in range(len(price_difference)):
    start = i
    end = min(len(price_difference)-1, i+4)
    rolling_average[i] = round(sum(price_difference[start:end+1])/(end+1-start),2)

  return(common_dates, rolling_average)

def statisticaData(csvname):
  prices_statistica = []
  dates_statistica = []

  with open(csvname, newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      prices_statistica.append(float(row['Discount']))
      dates_statistica.append(row['\ufeffDate'])
  
  return dates_statistica, prices_statistica

def bloombergData(csvname):
  prices_bloomberg = []
  dates_bloomberg = []

  with open(csvname, newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      prices_bloomberg.append(float(row['Discount']))
      unformat = row['\ufeffDate']
      formatted = datetime.strptime(unformat, '%m/%d/%y').strftime('%m/%d/%y')
      dates_bloomberg.append(formatted)
  
  return dates_bloomberg, prices_bloomberg

def getMatchingData(investing_data, statistica_data, bloomberg_data):
  dates_investing, prices_investing = investing_data
  dates_statistica, prices_statistica = statistica_data
  dates_bloomberg, prices_bloomberg = bloomberg_data

  matching = [date for date in dates_investing if date in dates_statistica and date in dates_bloomberg]

  statistica = [prices_statistica[dates_statistica.index(date)] for date in matching]
  investing_com = [prices_investing[dates_investing.index(date)] for date in matching]
  bloomberg = [prices_bloomberg[dates_bloomberg.index(date)] for date in matching]

  return matching, statistica, investing_com, bloomberg

def getNextHighestDate(exact_date, dates):
  try:
    return dates.index(exact_date)
  except ValueError:
    base_datetime = datetime.strptime(exact_date, '%m/%d/%y')
    filtered_dates = [datetime.strptime(date, '%m/%d/%y') for date in dates if datetime.strptime(date, '%m/%d/%y') > base_datetime]
    next_highest_date = min(filtered_dates) if filtered_dates else None
    next_highest_date_str = next_highest_date.strftime('%m/%d/%y') if next_highest_date else None
    
    return dates.index(next_highest_date_str)

def getNextLowestDate(exact_date, dates):
  try:
    return dates.index(exact_date)
  except ValueError:
    base_datetime = datetime.strptime(exact_date, '%m/%d/%y')
    filtered_dates = [datetime.strptime(date, '%m/%d/%y') for date in dates if datetime.strptime(date, '%m/%d/%y') < base_datetime]
    next_lowest_date = max(filtered_dates) if filtered_dates else None
    next_lowest_date_str = next_lowest_date.strftime('%m/%d/%y') if next_lowest_date else None
    
    return dates.index(next_lowest_date_str)