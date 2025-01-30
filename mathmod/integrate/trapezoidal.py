from typing import Callable


def trapezoidal(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Вычисляет определенный интеграл методом трапеций.

    Аргументы:
        f (Callable[[float], float]): Интегрируемая функция
        a (float): Нижний предел интегрирования
        b (float): Верхний предел интегрирования
        n (int): Количество трапеций (интервалов)

    Возвращает:
        float: Приближенное значение определенного интеграла
    """
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        integral += f(a + i * h)

    integral *= h
    return integral
