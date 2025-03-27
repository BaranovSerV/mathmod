from typing import Callable


def false_position(
    f: Callable, 
    a: float, 
    b: float, 
    epsilon=1e-6
) -> tuple[float, int]:
    """
    Метод ложного положения для нахождения корня нелинейного уравнения. 
    Работает для отрезка [a, b], на котором f(a) * f(b) < 0.

    :param f: Функция, корень которой нужно найти.
    :param a: Левая граница отрезка.
    :param b: Правая граница отрезка.
    :param epsilon: Заданная точность (по умолчанию 1e-6).

    :return: Приближённое значение корня и количество итераций.
    """

    i = 0
    c_before = 0
    c = (a * f(b) - b * f(a)) / (f(a) - f(b))
    error = abs(c - c_before)

    while error > epsilon:
        c_after = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(a) * f(b) >= 0:
            raise 

        elif f(c_after) * f(a) < 0:
            error = abs(c_after - b)
            b = c_after
            i += 1

        elif f(c_after) * f(b) < 0:
            error = abs(c_after - a)
            a = c_after
            i += 1
    return c_after, i
