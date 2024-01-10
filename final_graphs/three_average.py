from three_series import matching, statistica, investing_com, bloomberg

def getAverage(matching, statistica, investing_com, bloomberg):
  average = [round(sum((statistica[i], investing_com[i], bloomberg[i]))/3,2) for i in range(len(matching))]
  return average

def

