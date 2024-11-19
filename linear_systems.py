import numpy as np
from scipy.linalg import norm

from utils import is_symmetric_positive_definite, lu_decomposition, is_diagonally_dominant


def gauss_zeydel(A: np.ndarray, b: np.ndarray, epsilon: float = 1e-6, norma: int = 1):
    """
     Решение СЛАУ итерационным методом Гаусса-Зейделя.
    :param A: матрица левой части
    :param b: массив правой части
    :param epsilon: погрешность
    :param norma: норма для остановки
    :return: Вектор решения (размером n) и количество итераций
    """
    A = A.copy()
    b = b.copy()

    if not is_diagonally_dominant(A):
        raise ValueError("Отсутствует диагональное преобладание матрицы!")

    n = len(b)
    x = np.zeros_like(b)
    iteration_count = 0

    while True:
        x_new = np.copy(x)

        for i in range(n):
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]
        if norm(x_new - x, norma) <= epsilon:
            break
        x = x_new
        iteration_count += 1
    return x, iteration_count


def jacobi(A: np.ndarray, b: np.ndarray, epsilon=1e-6, norma=1) -> tuple:
    """
    Решение СЛАУ методом Якоби.
    :param A: Матрица коэффициентов системы
    :param b: Вектор свободных членов
    :param epsilon: Заданная точность
    :param norma: Норма для оценки погрешности (например, 1, 2, np.inf)
    :return: Решение системы (вектор x) и количество итераций
    """
    n = len(b)
    x = np.zeros_like(b)  # Начальное приближение
    iteration_count = 0

    # Разделяем A на диагональную, верхнюю и нижнюю части
    D = np.diag(A)  # Диагональные элементы
    R = A - np.diagflat(D)  # Остальная часть матрицы

    while True:
        x_new = (b - np.dot(R, x)) / D  # Основная формула метода Якоби

        # Проверяем условие выхода
        if norm(x_new - x, norma) <= epsilon:
            break

        x = x_new
        iteration_count += 1

    return x_new, iteration_count


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


def lu(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Решение СЛАУ:
    Метод LU - разложения
    :param A:
    :param b:
    :return:
    """

    A = A.copy()
    b = b.copy()

    L, U = lu_decomposition(A)
    n = len(b)
    # Решаем Ly = b
    y = np.zeros_like(b)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Решаем Ux = y
    x = np.zeros_like(b)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x


def gauss_single_division(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Решение СЛАУ:
    Метод Гаусса - схема единственного деления
    :param A:
    :param b:
    :return:
    """
    A = A.copy()
    b = b.copy()
    n = len(b)

    # Прямой ход
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    return x
