from typing import Callable


def milne(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Вычисляет определенный интеграл формулой Милна.

    param f: (Callable[[float], float]): Интегрируемая функция
    param a: (float): Нижний предел интегрирования
    param b: (float): Верхний предел интегрирования
    param n: (int): Количество интервалов 

    return:
        float: Приближенное значение определенного интеграла
    Точность метода: 6
    """
    h = (b - a) / n
    integral=0
    
    for i in range(1,n+1):
        x = a + i * h

        integral += 7 * f(x) + 32 * f(x-h / 4)
    

    for i in range(n):
        x = a + i * h
        integral += 7 * f(x) + 32 * f(x + h / 4)
    
    for i in range(1 ,n + 1):
        x=a+(i- 1 / 2) * h
        integral += 12 * f(x)
    
    integral *= h / 90
    
    return integral
