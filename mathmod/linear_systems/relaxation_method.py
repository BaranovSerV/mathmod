import numpy as np


def relaxation_method(A, b, omega=1.0, epsilon=1e-6, norma=1):
    """
    Решение СЛАУ методом релаксации (SOR).
    
    :param A: Матрица коэффициентов (n x n).
    :param b: Вектор правой части (n).
    :param omega: Параметр релаксации (по умолчанию 1.0 — метод Зейделя).
    :param epsilon: Точность решения (по умолчанию 1e-6).
    :return: Приближенное решение x.
    """
    iteration_count = 0
    n = len(b)
    x = np.zeros_like(b, dtype=np.float64)  

    while True:
        x_new = np.copy(x)  
        iteration_count += 1
        
        for i in range(n):
            s1 = sum(A[i, j] * x_new[j] for j in range(i))      
            s2 = sum(A[i, j] * x[j] for j in range(i + 1, n)) 
            
            x_new[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (b[i] - s1 - s2)
        
        if np.linalg.norm(x_new - x, norma) < epsilon:
            return x_new, iteration_count
        
        x = x_new

