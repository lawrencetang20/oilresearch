import data_functions as data
import pandas as pd

start = '2022-01-01'
end = '2024-01-17'
link = f'http://api.scraperlink.com/investpy/?email=tangla@mit.edu&type=historical_data&product=commodities&from_date={start}&to_date={end}&time_frame=Daily&name=brent'

investing_urals = '../excel_csv/crudeoil.csv'
statista = '../excel_csv/statista_data.csv'
bloomberg = '../excel_csv/bloomberg_urals_brent.csv'
treasury = '../excel_csv/treasury.csv'
datastream = '../excel_csv/datastream.csv'

investing_total = data.investingData(investing_urals, data.investingAPI(link))
statista_total = data.statistaData(statista)
bloomberg_total = data.bloombergData(bloomberg)
treasury_total = data.treasuryData(treasury)
datastream_total = data.datastreamData(datastream)

matching, statista_data, investing_com_data, bloomberg_data, treasury_data, datastream_data = data.getMatchingData(investing_total, statista_total, bloomberg_total, treasury_total, datastream_total)

if __name__ == "__main__":
  df = pd.DataFrame({
    'Matching': matching,
    'Statista': statista_data,
    'Investing.com': investing_com_data,
    'Bloomberg': bloomberg_data,
    'Treasury': treasury_data,
    'Datastream': datastream_data
  })

  df.to_csv('../excel_csv/matching_dates.csv', index=False)