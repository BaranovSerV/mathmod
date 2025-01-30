import numpy as np


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

    # if not is_diagonally_dominant(A):
        # raise ValueError("Отсутствует диагональное преобладание матрицы!")

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


