from typing import Callable


def ode_modified_euler(
    f: Callable[[float, float], float], 
    y: float, 
    t: float, 
    h: float
) -> float:
    """
    Решает задачу Коши для ОДУ модифицированным методом Эйлера 2-го порядка.

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
    def y_temp(t, y):
        return y + h * f(t, y)

    return y + h / 2 * (f(t, y) + f(t + h, y_temp(t, y)))
