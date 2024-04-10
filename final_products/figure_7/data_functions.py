import csv

def getData(csv_file_path):

  dates = []
  revenues = []
  averages = []

  with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader, None)
      
    for row in csv_reader:
      dates.append(row[0])
      revenues.append(float(row[1]))
      averages.append(float(row[2]))
  
  return dates, revenues, averages