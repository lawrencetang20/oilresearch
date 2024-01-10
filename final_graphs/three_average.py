import matplotlib.pyplot as plt
from three_series import matching, statistica, investing_com, bloomberg

def getAverage(matching, statistica, investing_com, bloomberg):
  average = [round(sum((statistica[i], investing_com[i], bloomberg[i]))/3,2) for i in range(len(matching))]
  return average

def plotAverage(matching, average):
  plt.plot(matching, average)
  plt.title('Urals Discounts')
  plt.xlabel('Date')
  plt.ylabel('Price Difference')
  plt.xticks(matching[::30], rotation=45)
  plt.tight_layout()
  plt.show()

average = getAverage(matching, statistica, investing_com, bloomberg)
plotAverage(matching, average)
