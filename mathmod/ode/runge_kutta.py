from typing import Callable


def ode_runge_kutta_third(
    f: Callable[[float], float], 
    y: float, 
    t: float, 
    h: float
) -> float:
    """
    Решает задачу Коши для ОДУ первого порядка методом Рунге-Кутты третьего порядка.

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
    def k1(f: Callable[[float], float], t: float, y: float) -> float:
        return f(t, y)

    def k2(f: Callable[[float], float], t: float, y: float, h: float) -> float:
        return f(t + h / 2, y + h / 2 * k1(f, t, y))

    def k3(f: Callable[[float], float], t: float, y: float, h: float) -> float:
        return f(t + h, y - h * k1(f, t, y) + 2 * h * k2(f, t, y, h))
    
    return y + h / 6 * (k1(f, t, y) + 4 * k2(f, t, y, h) + k3(f, t, y, h))



def ode_runge_kutta_fourth(    
    f: Callable[[float, float], float], 
    y: float, 
    t: float, 
    h: float
) -> float:
    """
    Решает задачу Коши для ОДУ первого порядка методом Рунге-Кутты четвёртого порядка.

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
    def k1(f, t, y):
        return f(t, y)
    
    def k2(f, t, y, h):
        return f(t + h / 2, y + h / 2 * k1(f, t, y))
    
    def k3(f, t, y, h):
        return f(t + h / 2, y + h / 2 * k2(f, t, y, h))
    
    def k4(f, t, y, h):
        return f(t + h, y + h * k3(f, t, y, h))
    
    return y + h / 6 * (k1(f, t, y) + 2 * k2(f, t, y, h) + 2 * k3(f, t, y, h) + k4(f, t, y, h))