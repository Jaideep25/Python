# Import libraries

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
# Define Data

x = np.arange(0, 20, 0.2)
y =  np.sin(x)
z1 = np.cos(x)
z2 = np.exp(8)
 
# Create Figure

fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
 
# Create Plot

ax.scatter3D(x, y, z1, marker='<', s=20, label='Triangle')
ax.scatter3D(x, y, z2, marker='o', s=20, label='Circle' )

# Add legend

ax.legend(loc=1)
 
# Show plot

plt.show()
