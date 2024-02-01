from setup import points
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

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

  ax.set_xlabel('Extraction (million barrels per day)')
  ax.set_ylabel('Price ($ per barrel)')
  ax.set_title('Scatter Plot of Points')

  cbar_ax = fig.add_axes([0.95, 0.15, 0.05, 0.7])  # [left, bottom, width, height]
  cbar = plt.colorbar(ScalarMappable(norm=norm, cmap=cmap), cax=cbar_ax)
  cbar.set_label('Month')

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  regressionPlot(points)