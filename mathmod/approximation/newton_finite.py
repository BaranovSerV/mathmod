import numpy as np
from scipy.special import factorial

def finite_differences(x_list, y_list):
    """
    Вычисляет конечные разности для набора точек (x_list, y_list).

    :param x_list: Список значений аргумента x.
    :param y_list: Список значений функции f(x) в точках x_list.
    :return: Первый ряд таблицы конечных разностей (разности для x_0).
    """
    n = len(x_list)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_list

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = diff_table[i + 1, j - 1] - diff_table[i, j - 1]
    
    return diff_table[0]


def newton_finite(x, x_list, coeffs, h):
    """
    Вычисляет значение интерполяционного многочлена Ньютона в точке x.

    :param x: Точка, в которой вычисляется значение многочлена.
    :param x_list: Список значений аргумента x.
    :param coeffs: Коэффициенты из таблицы конечных разностей.
    :param h: Шаг сетки (разность между соседними значениями x_list).
    :return: Значение интерполяционного многочлена Ньютона в точке x.
    """
    n = len(x_list)
    result = coeffs[0]
    product = 1

    for i in range(1, n):
        product *= (x - x_list[i - 1])
        result += coeffs[i] * product / (factorial(i) * h ** i)
    
    return result