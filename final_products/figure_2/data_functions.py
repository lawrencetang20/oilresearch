import csv

def extractData(csvname):
  others_volume = []
  turkey_volume = []
  india_volume = []
  china_volume = []
  US_UK_volume = []
  EU_volume = []

  dates = []

  with open(csvname, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      match row['destination']:
        case 'EU':
          EU_volume.append(float(row['volume']))
          dates.append(row['date'])
        case 'India':
          india_volume.append(float(row['volume']))
        case 'Others':
          others_volume.append(float(row['volume']))
        case 'Turkey':
          turkey_volume.append(float(row['volume']))
        case 'China':
          china_volume.append(float(row['volume']))
        case 'US/UK':
          US_UK_volume.append(float(row['volume']))
        case _:
          print(row)
          
  return EU_volume, india_volume, others_volume, turkey_volume, china_volume, US_UK_volume, dates