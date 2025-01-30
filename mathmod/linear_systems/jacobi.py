import numpy as np

def jacobi(A: np.ndarray, b: np.ndarray, epsilon=1e-6, norma=1):
    """
    Решение СЛАУ методом Якоби.
    :param A: Матрица коэффициентов системы
    :param b: Вектор свободных членов
    :param epsilon: Заданная точность
    :param norma: Норма для оценки погрешности (например, 1, 2, np.inf)
    :return: Решение системы (вектор x) и количество итераций
    """
    iteration_count = 0
    n = len(b)
    x = np.zeros_like(b, dtype=np.float64)  # Начальное приближение (нулевой вектор)
    x_new = np.zeros_like(x)
    
    while True:
        iteration_count += 1
        for i in range(n):
            s = sum(A[i, j] * x[j] for j in range(n) if j != i)  
            x_new[i] = (b[i] - s) / A[i, i]
        
        if np.linalg.norm(x_new - x, norma) < epsilon:
            return x_new, iteration_count
        
        x = x_new.copy()
