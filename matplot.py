import matplotlib as mpl  
from mpl_toolkits.mplot3d import Axes3D  
import numpy as np  
import matplotlib.pyplot as plt  
  
mpl.rcParams['legend.fontsize'] = 10  
  
fig = plt.figure()  
ax = fig.gca(projection='3d')  
theta1 = np.linspace(-4 * np.pi, 4 * np.pi, 100)  
z = np.linspace(-2, 2, 100)  
r = z**2 + 1  
x = r * np.sin(theta1)  
y = r * np.cos(theta1)  
ax.plot3D(x, y, z, label='parametric curve', color = 'red')  
ax.legend()  
  
plt.show()  