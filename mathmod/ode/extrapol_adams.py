from typing import Callable


def ode_exstrapol_adams(
    f: Callable[[float, float], float], 
    y: float, 
    t: float, 
    y_minus: float, 
    t_minus: float,
    h: float
) -> float:
    """
    Решает задачу Коши для ОДУ первого порядка методом экстраполяции Адамса второго порядка.

    :param f: Функция правой части ОДУ f(t, y), задающая уравнение dy/dt = f(t, y).
    :type f: Callable[[float, float], float]
    :param y: Текущее значение функции y.
    :type y: float
    :param t: Текущий момент времени.
    :type t: float
    :param y_minus: Значение y на предыдущем шаге (t - h).
    :type y_minus: float
    :param t_minus: Значение t на предыдущем шаге (t - h).
    :type t_minus: float
    :param h: Шаг интегрирования.
    :type h: float

    :return: Значение y в следующий момент времени t + h.
    :rtype: float
    """
    return y + h / 2 * (3 * f(t, y) - f(t_minus, y_minus))
