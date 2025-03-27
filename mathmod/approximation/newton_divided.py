import numpy as np


def divided_differences(array_x: list[float], array_y: list[float]):
    """
    Функция получения коэффициентов для интерполяции метод Ньютона с разделенными
    разностями.
    """
    n = len(array_x)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = array_y

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = (
                (diff_table[i + 1, j - 1] - diff_table[i, j - 1]) / (array_x[i + j] - array_x[i])
            )
    return diff_table[0]


def newton_divided(x: float, array_x: list[float], coeffs: list[float]):
    n = len(array_x)
    P = coeffs[0]
    omega = 1

    for i in range(1, n):
        omega *= (x - array_x[i - 1])

        P += coeffs[i] * omega

    return P



