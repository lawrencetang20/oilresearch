from setup import part_b_dates, part_b_values
import matplotlib.pyplot as plt

def plotMonthly(dates, values):
  plt.figure(figsize=(10, 6))
  plt.plot(dates, values, linestyle='-')
  plt.ylim(6, 12)
  plt.ylabel('Extraction (million barrels per day)')
  plt.title('Monthly')
  plt.xticks(range(0, len(dates), 6), [dates[i] for i in range(0, len(dates), 6)], rotation=45, ha='right')
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()
  plt.savefig('../../saved_pngs/figure_1/figure_1_part_b.png')
  print('png saved')
  plt.show()

if __name__ == "__main__":
  plotMonthly(part_b_dates, part_b_values)