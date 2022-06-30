# Import libraries

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Define Function

def function_z(x,y):
    return 100 - (x**2 + y**2)

# Define Data

x_val = np.linspace(-3, 3, 30)
y_val = np.linspace(-3, 3, 30)

X, Y = np.meshgrid(x_val, y_val)

# Call function

z = function_z(X, Y)

# Create figure

fig = plt.figure(figsize =(10,6))
ax = plt.axes(projection='3d')

# Create surface plot

ax.plot_surface(X, Y, z, color='#ff4500');

# Display

plt.show()
