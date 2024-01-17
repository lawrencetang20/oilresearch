import data_functions as data
import pandas as pd

start = '2022-01-01'
end = '2024-01-10'
link = f'http://api.scraperlink.com/investpy/?email=tangla@mit.edu&type=historical_data&product=commodities&from_date={start}&to_date={end}&time_frame=Daily&name=brent'

investing_urals = '../excel_csv/crudeoil.csv'
statista = '../excel_csv/statista_data.csv'
bloomberg = '../excel_csv/bloomberg_urals_brent.csv'
treasury = '../excel_csv/treasury.csv'
datastream = '../excel_csv/datastream.csv'

matching, statista_data, investing_com_data, bloomberg_data, treasury_data, datastream_data = data.getMatchingData(data.investingData(investing_urals, data.investingAPI(link)), data.statistaData(statista), data.bloombergData(bloomberg), data.treasuryData(treasury), data.datastreamData(datastream))

if __name__ == "__main__":
  df = pd.DataFrame({
    'Matching': matching,
    'Statista': statista_data,
    'Investing.com': investing_com_data,
    'Bloomberg': bloomberg_data,
    'Treasury': treasury_data,
    'Datastream': datastream_data
  })

  df.to_csv('../excel_csv/python_data.csv', index=False)