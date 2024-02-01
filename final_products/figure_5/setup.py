import data_functions as data

start_oil = 'Jan 2007'
end_oil = 'Dec 2022'
start_urals = 'Jan-07'
end_urals = 'Dec-22'

oil_extraction = '../../excel_csv/figure_5/oil_extraction.csv'
urals = '../../excel_csv/figure_5/urals_monthly.csv'

oil_extraction_dates, oil_extraction_values = data.oil_extraction(oil_extraction)

start_index = oil_extraction_dates.index(start_oil)
end_index = oil_extraction_dates.index(end_oil)

oil_extraction_dates = oil_extraction_dates[start_index: end_index+1]
oil_extraction_values = oil_extraction_values[start_index: end_index+1]
oil_extraction_values = [float(value)/1000 for value in oil_extraction_values] # make MBPD not TBPD

urals_dates, urals_values = data.urals_monthly(urals)

start_index = urals_dates.index(start_urals)
end_index = urals_dates.index(end_urals)

urals_dates = urals_dates[start_index: end_index+1]
urals_values = urals_values[start_index: end_index+1]