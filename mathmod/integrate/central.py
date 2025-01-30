from typing import Callable


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
