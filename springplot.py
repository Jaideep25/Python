# Import libraries

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
# Define Dataset

x = np.random.randint(100,size=(80))
y = np.random.randint(150, size=(80))
z = np.random.randint(200, size=(80))
 
# Creating figure

fig = plt.figure(figsize = (16, 9))
ax = plt.axes(projection ="3d")
  
# Creat color map

color_map = plt.get_cmap('spring')
 
# Create scatter plot and colorbar

scatter_plot = ax.scatter3D(x, y, z,
                            c=(x+y+z),
                            cmap = color_map)
 
plt.colorbar(scatter_plot)
 
# Show plot

plt.show()
