import numpy as np


def three_diag(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Метод прогонки для решения СЛАУ с трехдиагональной матрицей A.

    :param A: трехдиагональная матрица (размер n x n)
    :param b: правая часть (вектор размер n)
    :return: решение системы (вектор размер n)
    """
    n = len(A)

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
