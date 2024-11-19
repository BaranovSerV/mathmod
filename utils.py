import numpy as np


def lu_decomposition(A: np.ndarray):
    """
    Решение СЛАУ методом LU-разложения.

    :param A: матрица левой части
    :param b: массив правой части
    :return: вектор решения (размером n)
    """
    n = len(A)
    L = np.zeros_like(A)
    U = np.zeros_like(A)

    for i in range(n):
        # Вычисляем элементы верхней треугольной матрицы U
        for k in range(i, n):
            sum1 = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum1

        # Вычисляем элементы нижней треугольной матрицы L
        for k in range(i, n):
            if i == k:
                L[i][i] = 1  # Диагональные элементы L равны 1
            else:
                sum2 = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum2) / U[i][i]

    return L, U


def is_symmetric_positive_definite(A: np.ndarray) -> bool:
    """
    Проверяет, является ли матрица симметрично положительно определённой.

    :param A: Квадратная матрица
    :return: True, если матрица симметрично положительно определённая, иначе False
    """
    if not np.allclose(A, A.T):
        return False
    try:
        np.linalg.cholesky(A)
        return True
    except np.linalg.LinAlgError:
        return False


def is_diagonally_dominant(A: np.ndarray) -> bool:
    """

    :param A: Квадратная матрица
    :return: True, если присутствует диагональное преобладание, иначе False
    """
    for i in range(A.shape[0]):
        if np.abs(A[i, i]) <= np.sum(np.abs(A[i, :])) - np.abs(A[i, i]):
            return False
    return True