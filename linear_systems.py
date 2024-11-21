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

def relaxation_method(A, b, omega=1.0, epsilon=1e-6, norma=1):
    """
    Решение СЛАУ методом релаксации (SOR).
    
    :param A: Матрица коэффициентов (n x n).
    :param b: Вектор правой части (n).
    :param omega: Параметр релаксации (по умолчанию 1.0 — метод Зейделя).
    :param tol: Точность решения (по умолчанию 1e-6).
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


def three_diag(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Метод прогонки для решения СЛАУ с трехдиагональной матрицей A.

    :param A: трехдиагональная матрица (размер n x n)
    :param b: правая часть (вектор размер n)
    :return: решение системы (вектор размер n)
    """
    n = len(A)

    # Извлекаем диагонали
    a = np.zeros(n) 
    d = np.zeros(n)  
    c = np.zeros(n)  

    for i in range(n):
        d[i] = A[i, i]
        if i > 0:
            a[i] = A[i, i - 1]
        if i < n - 1:
            c[i] = A[i, i + 1]

    # Прямой ход
    alpha = np.zeros(n)
    beta = np.zeros(n)

    alpha[0] = -c[0] / d[0]
    beta[0] = b[0] / d[0]

    for i in range(1, n):
        denominator = d[i] + a[i] * alpha[i - 1]
        alpha[i] = -c[i] / denominator if i < n - 1 else 0  # Последний alpha не используется
        beta[i] = (b[i] - a[i] * beta[i - 1]) / denominator

    # Обратный ход
    x = np.zeros(n)
    x[-1] = beta[-1]

    for i in range(n - 2, -1, -1):
        x[i] = alpha[i] * x[i + 1] + beta[i]

    return x

def gauss_partial_pivot(a, b):
    n = len(b)
    a = np.copy(a)
    b = np.copy(b)

    for i in range(n):
        # Находим строку с максимальным элементом в i-ом столбце от i до n
        max_row = np.argmax(abs(a[i:, i])) + i
        
        # Меняем местами строки
        if i != max_row:
            a[[i, max_row]] = a[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        
        for j in range(i + 1, n):
            factor = a[j, i] / a[i, i]
            a[j, i:] -= factor * a[i, i:]
            b[j] -= factor * b[i]
    
    # Обратный ход для получения решения
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(a[i, i + 1:], x[i + 1:])) / a[i, i]
    
    return x

    