from setup import EU_volume, india_volume, others_volume, turkey_volume, china_volume, US_UK_volume, dates
import matplotlib.pyplot as plt

def stackedPlot(EU, india, others, turkey, china, US_UK, dates):
  categories = ['EU', 'US/UK', 'China', 'India', 'Turkey', 'Others']

  plt.figure(figsize=(12, 6))
  plt.stackplot(dates, EU, US_UK, china, india, turkey, others, labels=categories, baseline='zero', alpha=0.5)
  plt.ylabel('Volume (million barrels per day)')
  plt.xticks(range(0, len(dates), 30), [dates[i] for i in range(0, len(dates), 30)], rotation=45)
  plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0)
  plt.tight_layout()
  plt.savefig('../../saved_pngs/figure_3/figure_3.png')
  print('png saved')
  plt.show()

if __name__ == "__main__":
  stackedPlot(EU_volume, india_volume, others_volume, turkey_volume, china_volume, US_UK_volume, dates)