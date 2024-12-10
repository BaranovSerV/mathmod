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

def linear_spline(x_vals, y_vals):
    """
    Создает функцию линейного сплайна для заданных точек.
    
    :param x_vals: Список x-координат узлов интерполяции.
    :param y_vals: Список y-координат узлов интерполяции.
    :return: Функция линейного сплайна.
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("Длина x_vals и y_vals должна совпадать.")
    if len(x_vals) < 2:
        raise ValueError("Для линейной интерполяции требуется хотя бы 2 точки.")

    def spline(x):
        # Проверяем, что x в пределах диапазона
        if x < x_vals[0] or x > x_vals[-1]:
            raise ValueError("x вне диапазона интерполяции.")
        
        # Ищем соответствующий интервал
        for i in range(len(x_vals) - 1):
            if x_vals[i] <= x <= x_vals[i + 1]:
                # Формула линейной интерполяции
                t = (x - x_vals[i]) / (x_vals[i + 1] - x_vals[i])
                return (1 - t) * y_vals[i] + t * y_vals[i + 1]
        return None

    return spline

    



