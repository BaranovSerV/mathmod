from linear_systems import three_diag, jacobi, gauss_zeydel, relaxation_method

import numpy as np

A = np.array(
    [[5, -1, 0, 0],
     [2, 4.6, -1, 0],
     [0, 2, 3.6, -0.8],
     [0, 0, 3, 4.4]])

b = np.array([2, 3.3, 2.6, 7.2])

print(jacobi(A,b, norma=np.inf))

print(gauss_zeydel(A,b, norma=np.inf))

print(relaxation_method(A,b, omega=0.9, norma=np.inf))
