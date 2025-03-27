from typing import Callable


def ode_euler(
    f: Callable[[float, float], float], 
    y: float, 
    t: float, 
    h: float
) -> float:
    """
    Решает задачу Коши для ОДУ первого порядка методом Эйлера.

    :param f: Функция правой части ОДУ f(t, y), задающая уравнение dy/dt = f(t, y).
    :type f: Callable[[float, float], float]
    :param t: Текущий момент времени.
    :type t: float
    :param y: Текущее значение функции y.
    :type y: float
    :param h: Шаг интегрирования.
    :type h: float

    :return: Значение y в следующий момент времени t + h.
    :rtype: float
    """
    return y + h * f(t, y)
