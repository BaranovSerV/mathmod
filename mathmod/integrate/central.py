from typing import Callable


def central(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Вычисляет определенный интеграл методом левых прямоугольников.

    
    param f: (Callable[[float], float]): Интегрируемая функция
    param a: (float): Нижний предел интегрирования
    param b: (float): Верхний предел интегрирования
    param n: (int): Количество прямоугольников (интервалов)

    return:
        float: Приближенное значение определенного интеграла
    Точность метода: 2
    """
    h = (b - a) / n
    I = 0
    for i in range(n):

        I += f(a + h / 2 + i * h)
    return I * h
