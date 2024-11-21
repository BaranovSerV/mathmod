import numpy as np


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