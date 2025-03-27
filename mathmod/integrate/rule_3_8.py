from typing import Callable


def rule_3_8(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Вычисляет определенный интеграл правилом 3/8.

    param f: (Callable[[float], float]): Интегрируемая функция
    param a: (float): Нижний предел интегрирования
    param b: (float): Верхний предел интегрирования
    param n: (int): Количество интервалов 

    return:
        float: Приближенное значение определенного интеграла
    Точность метода: 4
    """
    h = (b - a) / n
    I = 0

    for i in range(1, n + 1):
        x = a + i * h

        I += 3 * f(x - h / 3) + f(x)

    for i in range(n):
        x = a + i * h

        I += 3 * f(x + h / 3) + f(x)


    I *= h / 8
    return I
