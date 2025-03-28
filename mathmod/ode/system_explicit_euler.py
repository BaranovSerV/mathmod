import numpy as np


def ode_system_explicit_euler(A, Y0, N, a, b):
    """ 
    Решает систему обыкновенных дифференциальных уравнений (ОДУ) явным методом Эйлера.
    
    :param A: Матрица системы ОДУ размера (n, n), где n — количество уравнений.
    :type A: np.ndarray
    :param Y0: Начальное условие системы — одномерный массив размера N,
    задающий начальные значения для каждого уравнения.
    :type Y0: np.ndarray
    :param N: Количество шагов интегрирования. 
    :type N: int
    :param a: Начало интервала интегрирования.
    :type a: float
    :param b: Конец интервала интегрирования.
    :type b: float

    :return: Двумерный массив размера (N, N), где каждая строка содержит решение
        системы на соответствующем временном шаге. Первая строка соответствует
        начальному условию Y0.
    :rtype: np.ndarray
    """
    h = (b - a) / N
    
    Y1 = np.zeros((N, Y0.shape[0]))
    Y1[0] = Y0
    
    for i in range(1, N):
        Y1[i] = Y1[i-1] + h * np.dot(A, Y1[i-1])
    return Y1