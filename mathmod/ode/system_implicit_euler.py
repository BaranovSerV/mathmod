import numpy as np


def ode_system_implicit_euler(A, Y0, N, a, b):
    h=(b - a) / N
    Y = np.zeros((N, Y0.shape[0]))
    Y[0] = Y0
    for i in range(1, N):
        Y[i] = np.linalg.solve(np.eye(A.shape[0]) - h * A, Y[i-1])
    return Y