import csv

def oil_extraction(csvname):

  dates = []
  crude_oil_data = []

  with open(csvname, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if len(row) >= 2:
        if row[0] == 'API':
          dates = row[1:]
        elif row[0] == 'INTL.57-1-RUS-TBPD.M':
          crude_oil_data = row[1:]

  return dates, crude_oil_data

def urals_monthly(csvname):
  
  urals_value = []
  dates = []

  with open(csvname, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    next(csv_reader)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
      # Extract date and price from each row and append to respective lists
      date = row[0]
      price = float(row[1])  # Convert price to float
      dates.append(date)
      urals_value.append(price)
  
  return dates, urals_value