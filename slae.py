import numpy as np


def solve_slae(data, h, lmbd, mu, xi, flag):
    N = data.shape[0]
    B = np.zeros((N, 1))
    for i in range(0, N - 2):
        B[i] = xi[i]

    A = np.zeros((N, N))
    for i in range(0, N - 2):
        A[i, i] = lmbd[i]
        A[i, i + 1] = 2
        A[i, i + 2] = mu[i]

    if (flag == 1):
        A[N - 2, 0] = 1
        A[N - 1, 1] = 1
        A[N - 2, N - 2] = 1
        A[N - 1, N - 1] = 1
    else:
        A[N - 2, 0] = -1
        A[N - 1, 1] = -1
        A[N - 2, N - 2] = 1
        A[N - 1, N - 1] = 1

    b = np.linalg.solve(A, B)
    d = np.zeros((N - 1, 1))
    c = np.zeros((N - 1, 1))

    for i in range(1, N - 1):
        d[i] = 2 * (data[i] - data[i + 1]) / pow(h[i], 3) + (b[i + 1] + b[i]) / pow(h[i], 2)
        c[i] = 3 * (data[i + 1] - data[i]) / pow(h[i], 2) - (b[i + 1] + 2 * b[i]) / h[i]

    return b, c, d
