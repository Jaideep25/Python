import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-np.pi,np.pi,100)

p = np.sin(x) # y = sin(x)
q = np.sin(2*x) # y = sin(2x)
r = np.sin(3*x) # y = sin(3x)


# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the functions, with labels
plt.plot(x,p, 'b-', label='y=sin(x)')
plt.plot(x,q, 'c-', label='y=sin(2x)')
plt.plot(x,r, 'm-', label='y=sin(3x)')

plt.legend(loc='upper left')

# show the plot
plt.show()
