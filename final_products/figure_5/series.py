from setup import points
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
import numpy as np

def regressionPlot(data):
  x_values = [point[0] for point in data]
  y_values = [point[1] for point in data]
  labels = [point[3] for point in data]
  dates = [point[2] for point in data]

  date_values = [int(date.split('-')[1]) for date in dates]

  fig, ax = plt.subplots(figsize=(12, 6))
  norm = Normalize(vmin=min(date_values), vmax=max(date_values))
  cmap = plt.get_cmap('coolwarm')
  cmap = cmap.reversed()
  scalar_map = ScalarMappable(norm=norm, cmap=cmap)

  for i, label in enumerate(labels):
    color = scalar_map.to_rgba(date_values[i])
    if label == 'Post':
      ax.scatter(x_values[i], y_values[i], color=color, label=label)
    elif label == 'Pre':
      ax.scatter(x_values[i], y_values[i], color=color, label=label)

  coeffs = np.polyfit(x_values, y_values, 1)
  slope = coeffs[0]
  intercept = coeffs[1]
  regression_line = [slope * x + intercept for x in x_values]
  ax.plot(x_values, regression_line, color='black', label='Regression Line')

  ax.set_xlabel('Extraction (million barrels per day)')
  ax.set_ylabel('Price ($ per barrel)')
  ax.set_title('Scatter Plot of Points')

  cbar = plt.colorbar(ScalarMappable(norm=norm, cmap=cmap), pad=0.02)
  cbar.set_ticks([])
  
  plt.tight_layout()
  plt.savefig('../../saved_pngs/figure_5/regression.png')
  print('png saved')
  plt.show()


if __name__ == "__main__":
  regressionPlot(points)