# Import libraries

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
# Define Data

z = [3, 6, 9, 12, 15]
x = [2, 4, 6, 8, 10]
y = [5, 10, 15, 20, 25]
 
# Create Figure

fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
 
# Create Plot

ax.scatter3D(x, y, z, s=100, color='green',   depthshade=True)

# Add axis

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Show plot

plt.show()
