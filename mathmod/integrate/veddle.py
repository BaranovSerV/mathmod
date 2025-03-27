from typing import Callable


def veddle(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Вычисляет определенный интеграл формулой Вэддла.

        
    param f: (Callable[[float], float]): Интегрируемая функция
    param a: (float): Нижний предел интегрирования
    param b: (float): Верхний предел интегрирования
    param n: (int): Количество интервалов 

    return:
        float: Приближенное значение определенного интеграла
    Точность метода: 8
    """
    h = (b - a) / n
    integral=0
    
    for i in range(0, n):
        x = a + i * h
        integral += 41 * f(x) + 216 * f(x + h / 6) + 27 * f(x + h / 3)
    
    for i in range(1, n + 1):
        x = a + i * h
        integral += 41 * f(x) + 216 * f(x - h / 6) + 27 * f(x - h / 3)
    
    for i in range(1, n + 1):
        x=a + (i - 1 / 2) * h
        integral += 272 * f(x)
    
    integral *= h / 840
    
    return integral
