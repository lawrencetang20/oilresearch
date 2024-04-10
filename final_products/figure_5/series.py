from setup import points
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize, LinearSegmentedColormap
from matplotlib.cm import ScalarMappable
import numpy as np

def regressionPlot(data):
  x_values = [point[0] for point in data]
  y_values = [point[1] for point in data]
  labels = [point[3] for point in data]
  dates = [point[2] for point in data]

  date_values = [int(date.split('-')[1]) for date in dates]

  fig, ax = plt.subplots(figsize=(12, 6))

  pre_colors = plt.cm.Reds(np.linspace(0.8, 0.2, 256))  
  post_colors = plt.cm.Blues(np.linspace(0.2, 0.8, 256))  

  norm = Normalize(vmin=min(date_values), vmax=max(date_values))
  scalar_map = ScalarMappable(norm=norm, cmap=None)

  for i, label in enumerate(labels):
    if label == 'Pre':
      color = pre_colors[int((date_values[i] - min(date_values)) / (max(date_values) - min(date_values)) * 255)]
    elif label == 'Post':
      color = post_colors[int((date_values[i] - min(date_values)) / (max(date_values) - min(date_values)) * 255)]
    ax.scatter(x_values[i], y_values[i], color=color)

  # plt.xlim(0, 20)

  ax.set_xlabel('Extraction (million barrels per day)')
  ax.set_ylabel('Price ($ per barrel)')

  # Create colorbars for 'Pre' and 'Post' gradients
  pre_cbar = plt.colorbar(ScalarMappable(norm=norm, cmap=plt.cm.Reds), pad=0.02, ax=ax, orientation='vertical')
  post_cbar = plt.colorbar(ScalarMappable(norm=norm, cmap=plt.cm.Blues), pad=0.02, ax=ax, orientation='vertical')
  pre_tick_labels = ['', '2016', '', '', '', '', '', '', '2007']
  post_tick_labels = ['', '2016', '', '', '', '', '', '', '2022']
  pre_cbar.set_ticklabels(pre_tick_labels)
  post_cbar.set_ticklabels(post_tick_labels)

  pre_cbar.set_label('Pre Opec')
  post_cbar.set_label('Post Opec')

  coeffs = np.polyfit(x_values, y_values, 1)
  slope = coeffs[0]
  intercept = coeffs[1]
  regression_line = [slope * x + intercept for x in x_values]
  ax.plot(x_values, regression_line, color='black', label='Regression Line')

  plt.tight_layout()
  plt.savefig('../../saved_pngs/figure_5/regression.png')
  print('png saved')
  plt.show()

if __name__ == "__main__":
  regressionPlot(points)