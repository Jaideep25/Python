# Import Library

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Plotting 3D axis figures

fig = plt.figure(figsize = (8, 6))
ax = plt.axes(projection = '3d')
  
# Define Data

z = np.linspace(0,15,150)
x = np.sin(z)
y = np.cos(z)

# Plot 3D scatter 

ax.scatter3D(x, y, z)

# zlim() method

ax.set_zlim(-1.5, 4)

# Display

plt.show()
