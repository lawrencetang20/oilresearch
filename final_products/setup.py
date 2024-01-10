import data_functions as data

start = '2022-01-01'
end = '2024-01-01'
link = f'http://api.scraperlink.com/investpy/?email=tangla@mit.edu&type=historical_data&product=commodities&from_date={start}&to_date={end}&time_frame=Daily&name=crude'

investing_urals = '../excel_csv/crudeoil.csv'
statistica = '../excel_csv/statistica_data.csv'
bloomberg = '../excel_csv/bloomberg_urals_brent.csv'

matching, statistica, investing_com, bloomberg = data.getMatchingData(data.investingData(investing_urals, data.investingAPI(link)), data.statisticaData(statistica), data.bloombergData(bloomberg))