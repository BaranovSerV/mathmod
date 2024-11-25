from typing import Callable

def right_rectangles(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Вычисляет определенный интеграл методом правых прямоугольников.

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
    for i in range(1, n+1):
        S += f(a+i*h)
    return h*S


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


def central(a: float, k: int, func: Callable[[float], float]) -> float:
    """
    Вычисляет приближенное значение производной методом центральных разностей.

    Аргументы:
        a (float): Точка, в которой вычисляется производная
        k (int): Параметр точности (определяет шаг как 10^(-k))
        func (Callable[[float], float]): Функция, производную которой нужно найти

    Возвращает:
        float: Приближенное значение производной в точке a
    """
    h = 10**(-k)
    return (func(a + h) - func(a-h)) / (2 * h)