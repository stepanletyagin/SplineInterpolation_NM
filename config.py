import math
import numpy as np

data = np.loadtxt('var17_z1.dat')
# data = np.loadtxt('var17_z2.dat')


def circle():
    # t = np.linspace(0, 2 * math.pi, num=49)
    t = np.linspace(0, math.pi, num=49) #for task_2
    x = np.zeros(len(t))
    y = np.zeros(len(t))
    for i in range(0, len(t)):
        x[i] = math.cos(t[i])
        y[i] = math.sin(t[i])
    return x, y


def cardioid():
    t = np.linspace(0, 2 * math.pi, num=49)
    x = np.zeros(len(t))
    y = np.zeros(len(t))
    for i in range(0, len(t)):
        x[i] = 2 * math.cos(t[i]) - math.cos(2 * t[i])
        y[i] = 2 * math.sin(t[i]) - math.sin(2 * t[i])
    return x, y


def astroid():
    t = np.linspace(0, 2 * math.pi, num=49)
    x = np.zeros(len(t))
    y = np.zeros(len(t))
    for i in range(0, len(t)):
        x[i] = pow(math.cos(t[i]), 3)
        y[i] = pow(math.sin(t[i]), 3)
    return x, y
