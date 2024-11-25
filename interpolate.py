from typing import Callable
import numpy as np

def lagrange(list_x: list[float], list_y: list[float]) -> Callable:
    """
    Функция для вычисления коэффициентов полинома Лагранжа.

    Аргументы:
        list_x (list[float]): Список значений x.
        list_y (list[float]): Список значений y.

    Возвращает:
        Callable: Функция, которая вычисляет значение полинома Лагранжа.
    """
    def L(x: float) -> float:
        result = 0.0
        for i in range(len(list_x)):
            basis = np.prod([(x - list_x[j]) / (list_x[i] - list_x[j]) 
                           for j in range(len(list_x)) if j != i])
            result += list_y[i] * basis
        return result
    return L



def mnk(list_x: list[float], list_y: list[float]) -> Callable:
    """
    Функция для вычисления коэффициентов полинома МНК.

    Аргументы:    
        list_x (list[float]): Список значений x.
        list_y (list[float]): Список значений y.

    Возвращает:
        Callable: Функция, которая вычисляет значение полинома МНК. 
    """
    
    pass


    



