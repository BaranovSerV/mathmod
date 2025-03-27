from typing import Callable


def secant(
    f: Callable, 
    x_minus_1: float, 
    x_n: float, epsilon=1e-6
) -> tuple[float, int]:
    """
    Метод секущих для нахождения корня уравнения f(x) = 0.
    Не требует аналитической производной.

    :param f: Функция, корень которой нужно найти.
    :param x_minus_1: Предыдущее приближение.
    :param x_n: Текущее приближение.
    :param epsilon: Заданная точность (по умолчанию 1e-6).

    :return: Приближённое значение корня и количество итераций.
    """

    i = 0
    x_plus_1 = x_n - (x_minus_1 - x_n) / (f(x_minus_1) - f(x_n)) * f(x_n)

    while abs(x_plus_1 - x_n) > epsilon:
        x_minus_1 = x_n
        x_n = x_plus_1
        x_plus_1 = x_n - (x_n - x_minus_1) / (f(x_n) - f(x_minus_1)) * f(x_n)
        i += 1
    return x_plus_1, i
