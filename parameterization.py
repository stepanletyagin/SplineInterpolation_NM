import numpy as np
import math


def param(x, y):
    N = x.shape[0]
    t = np.zeros(N)
    h = np.zeros(N - 1)
    for i in range(1, N):
        h[i - 1] = math.sqrt(pow((x[i] - x[i - 1]), 2) + pow((y[i] - y[i - 1]), 2))
        t[i] = t[i - 1] + h[i - 1]
    return h, t
