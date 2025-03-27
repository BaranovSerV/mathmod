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


def lu_decomposition(A: np.ndarray):
    """
    LU-разложение матрицы A на матрицы L и U.
    A = LU, где L - нижняя треугольная матрица, U - верхняя треугольная матрица.

    :param A: Квадратная матрица (n x n)
    :return: матрицы L и U
    """
    n = len(A)
    L = np.eye(n, dtype=np.float64) 
    U = np.zeros_like(A, dtype=np.float64)  
    for i in range(n):
        # Вычисляем элементы верхней треугольной матрицы U
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))

        # Вычисляем элементы нижней треугольной матрицы L
        for j in range(i + 1, n):
            L[j, i] =  (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]
    return L, U



