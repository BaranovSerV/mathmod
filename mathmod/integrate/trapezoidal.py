from typing import Callable


def trapezoidal(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Вычисляет определенный интеграл методом трапеций.


    param f: (Callable[[float], float]): Интегрируемая функция
    param a: (float): Нижний предел интегрирования
    param b: (float): Верхний предел интегрирования
    param n: (int): Количество трапеций (интервалов)

    return:
        float: Приближенное значение определенного интеграла
    Точность метода: 2
    """
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        integral += f(a + i * h)

    integral *= h
    return integral
