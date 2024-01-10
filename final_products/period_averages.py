import data_functions as data
from setup import start, end, link, investing_urals, statistica, bloomberg

"""
calculates the average Urals discount in

the four weeks leading up to (and including) October 12, 2023,
the period from October 13 to (and including) November 16, 2023,
the period since November 16.

dates:
09/14/22 to 10/12/23
10/13/23 to 11/16/23
11/17/23 to today


"""



dates_investing, prices_investing = data.investingData(investing_urals, data.investingAPI(link))
dates_statistica, prices_statistica = data.statisticaData(statistica)
dates_bloomberg, prices_bloomberg = data.bloombergData(bloomberg)


if __name__ == "__main__":
  print(dates_investing)