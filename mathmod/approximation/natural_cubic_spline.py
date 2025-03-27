import numpy as np

def compute_natural_cubic_spline_coeffs(
    x_array: list[float], 
    y_array: list[float]
):
    """
    Вычисляет коэффициенты кубического сплайна для набора точек (x, y) 
    с натуральными граничными условиями.

    :param x_array: Узлы интерполяции (список значений x).
    :param y_array: Значения функции в узлах интерполяции (список значений y).
    :return: Коэффициенты s, описывающие производные кубического сплайна в узлах x_array.
    """
    n = len(x_array) - 1
    h = np.diff(x_array)
    A = np.zeros((n + 1, n + 1))
    b = np.zeros(n + 1)

    # Условия на границах для натурального сплайна
    A[0, 0] = - 4 / h[0]
    A[0, 1] = - 2 / h[0]
    b[0] = - 6 * (y_array[1] - y_array[0]) / h[0] ** 2

    for i in range(1, n):
        A[i, i - 1] = 1 / h[i - 1]
        A[i, i] = 2 * (1 / h[i - 1] + 1 / h[i])
        A[i, i + 1] = 1 / h[i]
        b[i] = 3 * ((1 / (h[i - 1] ** 2)) * (y_array[i] - y_array[i - 1]) + (1 / (h[i] ** 2)) * (y_array[i + 1] - y_array[i]))
    
    A[n, n] =  4 / h[n - 1]
    A[n, n - 1] = 2 / h[n - 1]
    b[n] = 6 * (y_array[n] - y_array[n - 1]) / h[n - 1] ** 2

    s = np.linalg.solve(A, b)

    return s

def natural_cubic_spline(
    x_array: list[float], 
    y_array: list[float], 
    s: list[float], 
    x_values: list[float]
):
    """
    Вычисляет значения натурального кубического сплайна для заданных точек x_values.

    :param x_array: Узлы интерполяции (список значений x).
    :param y_array: Значения функции в узлах интерполяции (список значений y).
    :param s: Коэффициенты производных, вычисленные функцией compute_natural_cubic_spline_coeffs.
    :param x_values: Точки, в которых требуется вычислить значения сплайна.
    :return: Массив значений сплайна в точках x_values.
    """
    n = len(x_array) - 1
    h = np.diff(x_array)
    S = np.zeros_like(x_values)

    for i in range(n):
        mask = (x_values >= x_array[i]) & (x_values <= x_array[i + 1])
        dx = x_values[mask] - x_array[i]

        a = y_array[i]
        b = s[i]
        c = (3 * (y_array[i + 1] - y_array[i]) / h[i] ** 2) - (2 * s[i] + s[i + 1]) / h[i]
        d = (-2 * (y_array[i + 1] - y_array[i]) / h[i] ** 3) + (s[i] + s[i + 1]) / h[i] ** 2

        S[mask] = a + b * dx + c * dx ** 2 + d * dx ** 3
    
    return S
