from typing import Callable

def simpson(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Вычисляет определенный интеграл формулой Симпсона.


    param f: (Callable[[float], float]): Интегрируемая функция
    param a: (float): Нижний предел интегрирования
    param b: (float): Верхний предел интегрирования
    param n: (int): Количество интервалов 

    return:
        float: Приближенное значение определенного интеграла
    Точность метода: 4
    """
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:

            integral += 2 * f(x)
        else:

            integral += 4 * f(x)

    integral *= h / 3
    
    return integral
