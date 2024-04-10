import matplotlib.pyplot as plt
import pandas as pd
from setup import dates, revenues, averages

def displayPlot(date, revenue, average):
  df = pd.DataFrame({
    'Date': date,
    'Revenue': revenue,
    'Average': average
  })

  plt.figure(figsize=(12, 6))
  plt.bar(df['Date'], df['Revenue'], color='blue')
  plt.plot(df['Date'], df['Average'], color='orange', linestyle='-', linewidth=3)
  plt.ylabel('Revenue (billions $)')

  plt.xticks(rotation=90)

  plt.tight_layout()

  plt.savefig('../../saved_pngs/figure_7/bar_chart.png')
  print('png saved')
  plt.show()

if __name__ == "__main__":
  displayPlot(dates, revenues, averages)