from typing import Callable


def right_rectangles(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Вычисляет определенный интеграл методом правых прямоугольников.


    param f: (Callable[[float], float]): Интегрируемая функция
    param a: (float): Нижний предел интегрирования
    param b: (float): Верхний предел интегрирования
    param n: (int): Количество прямоугольников (интервалов)

    return:
        float: Приближенное значение определенного интеграла
    Точность метода: 1
    """
    h = (b - a) / n
    S = 0
    for i in range(1, n + 1):
        S += f(a + i * h)
    return h * S


