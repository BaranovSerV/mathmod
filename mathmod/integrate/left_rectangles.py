from typing import Callable


def left_rectangles(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Вычисляет определенный интеграл методом левых прямоугольников.

    Аргументы:
        f (Callable[[float], float]): Интегрируемая функция
        a (float): Нижний предел интегрирования
        b (float): Верхний предел интегрирования
        n (int): Количество прямоугольников (интервалов)

    Возвращает:
        float: Приближенное значение определенного интеграла
    """
    h = (b-a)/n
    S = 0
    for i in range(n):
        S += f(a+i*h)
    return h*S


