import data_functions as data
from setup import start, end, link, investing_urals, statista, bloomberg

"""
calculates the average Urals discount in

the four weeks leading up to (and including) October 12, 2023,
the period from October 13 to (and including) November 16, 2023,
the period since November 16.

dates:
09/14/23 to 10/12/23
10/13/23 to 11/16/23
11/17/23 to today


"""



dates_investing, prices_investing = data.investingData(investing_urals, data.investingAPI(link))
dates_statista, prices_statista = data.statistaData(statista)
dates_bloomberg, prices_bloomberg = data.bloombergData(bloomberg)

def getAverage(start_date, end_date, dates, prices):
  low = data.getNextHighestDate(start_date, dates)
  high = data.getNextLowestDate(end_date, dates)

  return round(sum(prices[low:high+1])/(high-low+1), 2)

def period(start, end):
  pI = getAverage(start, end, dates_investing, prices_investing)
  pS = getAverage(start, end, dates_statista, prices_statista)
  pB = getAverage(start, end, dates_bloomberg, prices_bloomberg)
  print('In the order of Investing, Statista, Bloomberg')
  print(pI, pS, pB)  

if __name__ == "__main__":
  print('\n')

  print('Period 1:')
  period('09/14/23', '10/12/23')
  print('\n')

  print('Period 2:')
  period('10/13/23', '11/16/23')
  print('\n')

  print('Period 3')
  period('11/17/23', '01/10/24')
  print('\n')
