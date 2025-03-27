import numpy as np

def devided_differences(array_x: list[float], array_y: list[float]) -> np.ndarray:
    """
    Вычисляет коэффициенты интерполяционного многочлена Ньютона с разделёнными разностями.

    :param array_x: Список значений x (узлы интерполяции).
    :param array_y: Список значений функции f(x) в узлах интерполяции.
    :return: Коэффициенты интерполяционного многочлена.
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


def newton_devided(x: float, array_x: list[float], coeffs: list[float]) -> float:
    """
    Вычисляет значение интерполяционного многочлена Ньютона в точке x
    с использованием метода разделённых разностей.

    :param x: Точка, в которой вычисляется значение многочлена.
    :param array_x: Список узлов интерполяции.
    :param coeffs: Коэффициенты, вычисленные методом разделённых разностей.
    :return: Значение интерполяционного многочлена в точке x.
    """
    n = len(array_x)
    P = coeffs[0]
    omega = 1

    for i in range(1, n):
        omega *= (x - array_x[i - 1])
        P += coeffs[i] * omega

    return P
