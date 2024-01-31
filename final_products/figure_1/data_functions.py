import csv

def part_a_data(csvname):

  return

def part_b_data(csvname):

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
