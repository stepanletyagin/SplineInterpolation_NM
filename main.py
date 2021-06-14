import matplotlib.pyplot as plt
from parameterization import param
from cubic_spline import cubic_spline
from config import *
from cubic_spline_open_curve import cubic_cpline_cbcr

# x, y = circle()
# x, y = cardioid()
# x, y = astroid()
x = data[:, 0]
y = data[:, 1]

h, t = param(x, y)

#Task_1
S_x, S_y = cubic_spline(x, y, t, h, 2000)

#Task_2
# S_x = cubic_cpline_cbcr(x, h, t, 2000)
# S_y = cubic_cpline_cbcr(y, h, t, 2000)

fig_orig = plt.figure(figsize=(12, 12))
plt.plot(x, y, 'r*')
plt.plot(S_x, S_y, 'b')
plt.grid()
plt.show()
# fig_orig.savefig('saved_figure_task1.jpg')


