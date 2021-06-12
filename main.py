import numpy as np
import matplotlib.pyplot as plt
from parameterization import param
from cubic_spline import cubic_spline

data = np.loadtxt('var17_z1.dat')
x = data[:, 0]
y = data[:, 1]

h, t = param(x, y)

S_x, S_y = cubic_spline(x, y, t, h, 2000)

fig_orig = plt.figure()
plt.plot(x, y, 'ro')
plt.plot(S_x, S_y)
plt.grid()
plt.show()
fig_orig.savefig('saved_figure.jpg')


