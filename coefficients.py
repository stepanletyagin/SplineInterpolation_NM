import numpy as np


def find_coefficients(data, h):
    N = data.shape[0]
    lmbd = np.zeros(N - 1)
    mu = np.zeros(N - 1)
    xi = np.zeros(N - 1)
    for i in range(0, N - 2):
        lmbd[i] = h[i + 1] / (h[i + 1] + h[i])
        mu[i] = h[i] / (h[i + 1] + h[i])
        xi[i] = 3 * (lmbd[i] * (data[i + 1] - data[i]) / h[i] + mu[i] * (data[i + 2] - data[i + 1]) / h[i + 1])

    return lmbd, mu, xi
