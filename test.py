from interpolate import lagrange
from matplotlib import pyplot as plt
import numpy as np  

list_x = [-1, -0.7, -0.43, -0.14, -0.14, 0.43, 0.71, 1, 1.29, 1.57, 1.86, 2.14, 2.43, 2.71, 3]
list_y = [-2.25, -0.77, 0.21, 0.44, 0.64, 0.03, -0.22, -0.84, -1.2, -1.03, -0.37, 0.61, 2.67, 5.04, 8.90]

L = lagrange(list_x, list_y)

x = np.linspace(-3, 3, 100)
y = [L(x_i) for x_i in x] 

plt.plot(x, y)
plt.scatter(list_x, list_y)
plt.grid(True) 
plt.show()