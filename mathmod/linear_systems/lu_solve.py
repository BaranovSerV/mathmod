import numpy as np

def lu_solve(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Решение системы линейных уравнений Ax = b методом LU-разложения.

    :param A: Квадратная матрица (n x n)
    :param b: Вектор правой части (размер n)
    :return: Вектор решения x
    """
    L, U = lu_decomposition(A)
    n = len(b)
    # Прямой ход: решаем Ly = b
    y = np.zeros_like(b, dtype=np.float64)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Обратный ход: решаем Ux = y
    x = np.zeros_like(b, dtype=np.float64)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x


