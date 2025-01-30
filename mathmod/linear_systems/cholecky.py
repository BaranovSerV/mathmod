import numpy as np


def cholecky(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Решение СЛАУ методом Холецкого (LLT - разложения)
    
    :param A: матрица левой части
    :param b: массив правой части
    :return: Вектор решения (размером n)
    """

    # Проверка симметрично положительно определённой матрицы
    if not is_symmetric_positive_definite(A):
        raise ValueError("Матрица должна быть симметрично положительно определённой!")
    A = A.copy()
    b = b.copy()

    n = A.shape[0]
    L = np.zeros_like(A)

    for i in range(n):
        for j in range(i + 1):
            sum_k = sum(L[i, k] * L[j, k] for k in range(j))

            if i == j:
                L[i, j] = np.sqrt(A[i, i] - sum_k)
            else:
                L[i, j] = (A[i, j] - sum_k) / L[j, j]
    # L y = b
    y = np.zeros_like(b)
    for i in range(len(b)):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    # L^T x = y
    x = np.zeros_like(b)
    for i in range(len(b) - 1, -1, -1):
        x[i] = (y[i] - np.dot(L[i + 1:, i], x[i + 1:])) / L[i, i]

    return x

