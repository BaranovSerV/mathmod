from linear_systems import gauss_zeydel

import numpy as np

A = np.array(
    [[104, -4, 6, 2],
     [9, 95, 1, 0],
     [-10, -5, 100, 2],
     [-2, 0, 5, 64]])

b = np.array([-826, -452, 90, -304])

print(gauss_zeydel(A, b))