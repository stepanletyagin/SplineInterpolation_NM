import numpy as np
from coefficients import find_coefficients


def cubic_cpline_cbcr(data ,h, t, int_points):
    N = data.shape[0]
    lmbd, mu, xi = find_coefficients(data, h)

    gamma_0 = h[1] / h[0]
    gamma_N = h[N - 3] / h[N - 2]
    xi_0 = xi[0] / 3 + 2 * gamma_0 * (data[1] - data[0]) / h[0]
    xi_N = xi[N - 2] / 3 + 2 * gamma_N * (data[N - 1] - data[N - 2]) / h[N - 2]

    B = np.zeros((N, 1))
    for i in range(0, N - 2):
        B[i] = xi[i]

    B[N - 2] = xi_0
    B[N - 1] = xi_N

    A = np.zeros((N, N))
    for i in range(0, N - 2):
        A[i, i] = lmbd[i]
        A[i, i + 1] = 2
        A[i, i + 2] = mu[i]

    A[N - 2, 0] = gamma_0
    A[N - 2, 1] = (1 + gamma_0)
    A[N - 1, N - 2] = (1 + gamma_N)
    A[N - 1, N - 1] = gamma_N

    b = np.linalg.solve(A, B)
    d = np.zeros((N - 1, 1))
    c = np.zeros((N - 1, 1))
    for i in range(0, N - 1):
        d[i] = 2 * (data[i] - data[i + 1]) / pow(h[i], 3) + (b[i + 1] + b[i]) / pow(h[i], 2)
        c[i] = 3 * (data[i + 1] - data[i]) / pow(h[i], 2) - (b[i + 1] + 2 * b[i]) / h[i]

    S = np.zeros((int_points + 1, 1))
    i = 0
    for j in range(0, int_points + 1):
        t_c = t[0] + (t[N - 1] - t[0]) / int_points * (j - 1)
        while (t_c > t[i + 1]):
            i = i + 1
        S[j] = data[i] + b[i] * (t_c - t[i]) + c[i] * pow((t_c - t[i]), 2) + d[i] * pow((t_c - t[i]), 3)

    return S



