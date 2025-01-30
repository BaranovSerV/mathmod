from typing import Callable


def newton(
    f: Callable, 
    df: Callable, 
    x: float, epsilon=1e-6
) -> tuple[float, int]:
    """
    Метод Ньютона (касательных) для нахождения корня уравнения f(x) = 0.

    :param f: Функция, корень которой нужно найти.
    :param df: Производная функции f.
    :param x: Начальное приближение.
    :param epsilon: Заданная точность (по умолчанию 1e-6).
    :return: Приближённое значение корня и количество итераций.
    """

    x_next = x - f(x) / df(x)
    i = 0
    while abs(x_next - x) > epsilon:
        x = x_next
        x_next = x - f(x) / df(x)
        i += 1
    return x_next, i
