import matplotlib.pyplot as plt
from setup import matching, statistica_data, investing_com_data, bloomberg_data

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
  print('png saved')
  plt.show()


if __name__ == "__main__":
  plotSeries(matching, statistica_data, investing_com_data, bloomberg_data)
