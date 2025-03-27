from typing import Callable


def ode_improved_euler(
    f: Callable[[float], float], 
    y: float, 
    t: float, 
    h: float
) -> float:
    """
    Решает задачу Коши для ОДУ первого порядка усовершенствованным методом Эйлера второго порядка.

    :param f: Функция правой части ОДУ f(t, y), задающая уравнение dy/dt = f(t, y).
    :type f: Callable[[float, float], float]
    :param y: Начальное значение функции y в момент времени t.
    :type y: float
    :param t: Текущий момент времени.
    :type t: float
    :param h: Шаг интегрирования.
    :type h: float

    :return: Значение y в следующий момент времени t + h.
    :rtype: float
    """
    return y + h * f(t + h / 2, y + h / 2 * f(t, y))