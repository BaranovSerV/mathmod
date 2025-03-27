from typing import Callable


def ode_teylor(
    f: Callable[[float, float], float], 
    df_t: Callable[[float, float], float], 
    df_y: Callable[[float, float], float], 
    y: float, 
    t: float, 
    h: float
) -> float:
    """
    Решает задачу Коши для ОДУ первого порядка методом Тейлора второго порядка.

    :param f: Функция правой части ОДУ f(t, y), задающая уравнение dy/dt = f(t, y).
    :type f: Callable[[float, float], float]
    :param df_t: Частная производная df/dt, выражающая зависимость f от t.
    :type df_t: Callable[[float, float], float]
    :param df_y: Частная производная df/dy, выражающая зависимость f от y.
    :type df_y: Callable[[float, float], float]
    :param y: Начальное значение функции y в момент времени t.
    :type y: float
    :param t: Текущий момент времени.
    :type t: float
    :param h: Шаг интегрирования.
    :type h: float

    :return: Значение y в следующий момент времени t + h, вычисленное методом Тейлора второго порядка.
    :rtype: float
    """
    return y + h * f(t, y) + (h ** 2 / 2) * (df_t(t, y) + df_y(t, y) * f(t, y))
