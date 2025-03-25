from typing import Callable


def simplified_newton(
    f: Callable, 
    df: Callable, 
    x0: float, 
    epsilon: float = 1e-6
) -> tuple[float, int]:
    """
    Упрощённый метод Ньютона для нахождения корня уравнения f(x) = 0.

    :param f: Функция, корень которой нужно найти.
    :param df: Производная функции f.
    :param x0: Начальное приближение.
    :param epsilon: Заданная точность (по умолчанию 1e-6).
    :return: Приближённое значение корня и количество итераций.
    """

    x00 = x0
    x1 = x0 - f(x0) / df(x00)
    i = 0
    while abs(x1 - x0) > epsilon:
        x0 = x1
        x1 = x0 - f(x0) / df(x00)
        i += 1
    return x1, i
