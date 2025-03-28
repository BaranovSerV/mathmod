import numpy as np


def ode_system_implicit_euler(
    A: np.ndarray, 
    Y0: np.ndarray, 
    N: int, 
    a: float, 
    b: float
) -> np.ndarray:
    """ 
    Решает систему обыкновенных дифференциальных уравнений (ОДУ) неявным методом Эйлера.
    
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
    Y = np.zeros((N, Y0.shape[0]))
    Y[0] = Y0
    for i in range(1, N):
        Y[i] = np.linalg.solve(np.eye(A.shape[0]) - h * A, Y[i-1])
    return Y