import numpy as np


def ode_system_explicit_euler(A, Y0, N, a, b):
    h = (b - a) / N
    
    Y1 = np.zeros((N, Y0.shape[0]))
    Y1[0] = Y0
    
    for i in range(1, N):
        Y1[i] = Y1[i-1] + h * np.dot(A, Y1[i-1])
    return Y1