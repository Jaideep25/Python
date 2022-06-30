# the illustration of lim x->0 sin(x)/x = 1

import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-20,20,500)

y = np.sin(x)/x # y = sin(x)/x

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the functions, with labels
plt.plot(x,y, 'b-', label='y=sin(x)/x')
plt.plot(x,2*y, 'c-', label='y=2sin(x)/x')
plt.plot(x,-y, 'm-', label='y=-sin(x)/x')

plt.legend(loc='upper left')

# show the plot
plt.show()
