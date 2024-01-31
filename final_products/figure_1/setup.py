import data_functions as data

start = 'Jan 2018'
end = 'May 2023'

part_a = '../../excel_csv/figure_1/figure_1_a.csv'
part_b = '../../excel_csv/figure_1/figure_1_b.csv'

part_a_dates, part_a_values = data.part_a_data(part_a)
part_b_dates, part_b_values = data.part_b_data(part_b)

start_index = part_b_dates.index(start)
end_index = part_b_dates.index(end)

part_b_dates = part_b_dates[start_index: end_index+1]
part_b_values = part_b_values[start_index: end_index+1]
part_b_values = [float(value)/1000 for value in part_b_values] # make MBPD not TBPD
