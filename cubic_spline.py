import numpy as np
from slae import solve_slae
from coefficients import find_coefficients


def cubic_spline(x, y, t, h, int_points):
    N = x.shape[0]
    S_x = np.zeros((int_points + 1, 1))
    i = 0
    lmbd, mu, xi_x = find_coefficients(x, h)
    b, c, d = solve_slae(x, h, lmbd, mu, xi_x, 1)
    for j in range(0, int_points + 1):
        t_c = t[0] + (t[N - 1] - t[0]) / int_points * (j - 1)
        while t_c > t[i + 1]:
            i = i + 1

        S_x[j] = x[i] + b[i] * (t_c - t[i]) + c[i] * pow((t_c - t[i]), 2) + d[i] * pow((t_c - t[i]), 3)

    S_y = np.zeros((int_points + 1, 1))
    i = 0
    lmbd, mu, xi_y = find_coefficients(y, h)
    b, c, d = solve_slae(y, h, lmbd, mu, xi_y, 0)
    for j in range(0, int_points + 1):
        t_c = t[0] + (t[N - 1] - t[0]) / int_points * (j - 1)
        while t_c > t[i + 1]:
            i = i + 1
        S_y[j] = y[i] + b[i] * (t_c - t[i]) + c[i] * pow((t_c - t[i]), 2) + d[i] * pow((t_c - t[i]), 3)

    return S_x, S_y
