from typing import Callable

import numpy as np

def quadratic_spline_with_an_additional_condition(
    x_array: list[float], 
    y_array: list[float], 
    dfa: Callable[[float], float]
) -> list[tuple[float, float, float]]:
    """
    Вычисляет коэффициенты квадратичного сплайна с дополнительным условием
    первой производной в начальной точке.

    :param x_array: Список узлов интерполяции (x-координаты)
    :param y_array: Список значений функции в узлах (y-координаты)
    :param dfa: Значение первой производной в начальной точке x_array[0]
    :return: Список коэффициентов [(a0, b0, c0), (a1, b1, c1), ...] для каждого интервала
    """
    n_intervals = len(x_array) - 1  
    n = 3 * n_intervals  
    
    A = np.zeros((n, n))
    F = np.zeros(n)      

    j = 0  
    for i in range(n_intervals):
        A[j, 3 * i] = 1
        A[j, 3 * i + 1] = x_array[i]
        A[j, 3 * i + 2] = x_array[i] ** 2
        F[j] = y_array[i]
        j += 1

        A[j, 3 * i] = 1
        A[j, 3 * i + 1] = x_array[i + 1]
        A[j, 3 * i + 2] = x_array[i + 1] ** 2
        F[j] = y_array[i + 1]
        j += 1

    for i in range(n_intervals - 1):
        A[j, 3 * i + 1] = 1
        A[j, 3 * i + 2] = 2 * x_array[i + 1]
        A[j, 3 * (i + 1) + 1] = -1
        A[j, 3 * (i + 1) + 2] = -2 * x_array[i + 1]
        F[j] = 0
        j += 1

    A[j, 1] = 1
    A[j, 2] = 2 * x_array[0]
    F[j] = dfa

    coeffs = np.linalg.solve(A, F)

    splines = []
    for i in range(n_intervals):
        a = coeffs[3 * i]
        b = coeffs[3 * i + 1]
        c = coeffs[3 * i + 2]
        splines.append((a, b, c))
    
    return splines
