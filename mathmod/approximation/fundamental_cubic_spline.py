import numpy as np

def compute_fundamental_cubic_spline_coeffs(x_array, y_array, y_derivative_start, y_derivative_end):
    """
    Вычисляет коэффициенты фундаментального кубического сплайна с заданными граничными условиями на производные.

    :param x_array: Массив узлов интерполяции (значения x).
    :param y_array: Массив значений функции в узлах интерполяции (значения y).
    :param y_derivative_start: Значение производной в начальном узле x_0.
    :param y_derivative_end: Значение производной в конечном узле x_n.
    :return: Массив коэффициентов s, представляющих производные кубического сплайна в узлах x_array.
    """
    n = len(x_array) - 1
    h = np.diff(x_array)  

    A = np.zeros((n + 1, n + 1))
    b = np.zeros(n + 1)

    A[0, 0] = 1
    b[0] = y_derivative_start

    for i in range(1, n):
        A[i, i - 1] = 1 / h[i - 1]
        A[i, i] = 2 * (1 / h[i - 1] + 1 / h[i])
        A[i, i + 1] = 1 / h[i]
        b[i] = 3 * ((1 / (h[i - 1] ** 2)) * (y_array[i] - y_array[i - 1]) + (1 / (h[i] ** 2)) * (y_array[i + 1] - y_array[i]))
    
    A[n, n] = 1
    b[n] = y_derivative_end

    spline_coeffs = np.linalg.solve(A, b)

    return spline_coeffs


def fundamental_cubic_spline(x_array, y_array, spline_coeffs, x_values):
    """
    Вычисляет значения кубического сплайна в заданных точках x_values.

    :param x_array: Массив узлов интерполяции (значения x).
    :param y_array: Массив значений функции в узлах интерполяции (значения y).
    :param spline_coeffs: Массив коэффициентов s, вычисленный с помощью compute_fundamental_cubic_spline_coeffs.
    :param x_values: Массив точек, в которых необходимо вычислить значения сплайна.
    :return: Массив значений кубического сплайна в точках x_values.
    """
    n = len(x_array) - 1
    h = np.diff(x_array)
    spline_values = np.zeros_like(x_values)

    for i in range(n):
        mask = (x_values >= x_array[i]) & (x_values <= x_array[i + 1])
        dx = x_values[mask] - x_array[i]

        a = y_array[i]
        b = spline_coeffs[i]
        c = (3 * (y_array[i + 1] - y_array[i]) / h[i] ** 2) - (2 * spline_coeffs[i] + spline_coeffs[i + 1]) / h[i]
        d = (-2 * (y_array[i + 1] - y_array[i]) / h[i] ** 3) + (spline_coeffs[i] + spline_coeffs[i + 1]) / h[i] ** 2

        spline_values[mask] = a + b * dx + c * dx ** 2 + d * dx ** 3
    
    return spline_values