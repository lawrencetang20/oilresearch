import matplotlib.pyplot as plt
from setup import matching, statistica, investing_com, bloomberg

def plotSeries(matching, statistica, investing_com, bloomberg):
  plt.plot(matching, statistica, label='Statistica')
  plt.plot(matching, investing_com, label='Investing.com')
  plt.plot(matching, bloomberg, label='Bloomberg')
  plt.title('Urals Discounts')
  plt.xlabel('Date')
  plt.ylabel('Price Difference')
  plt.xticks(matching[::30], rotation=45)
  plt.legend()
  plt.tight_layout()
  plt.savefig('../saved_pngs/three_series.png')
  plt.show()


if __name__ == "__main__":
  plotSeries(matching, statistica, investing_com, bloomberg)
