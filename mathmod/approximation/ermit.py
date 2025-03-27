def polinomial_ermit(
    x: float, 
    x_i: float,
    x_minus_1, 
    y_i: float, 
    y_minus_1: float, 
    y_dir_i: float, 
    y_dir_minus_1: float
):
    """
    Вычисление значения интерполяционного многочлена Эрмита.

    param x:
        Точка, в которой вычисляется значение многочлена Эрмита.
    param x_i:
        Координата правого узла интерполяции (x_i > x_minus_1).
    param x_minus_1:
        Координата левого узла интерполяции (x_minus_1 < x_i).
    param y_i:
        Значение функции в правом узле интерполяции (f(x_i)).
    param y_minus_1: 
        Значение функции в левом узле интерполяции (f(x_minus_1)).
    param y_dir_i:
        Значение производной функции в правом узле интерполяции (f'(x_i)).
    param y_dir_minus_1:
        Значение производной функции в левом узле интерполяции (f'(x_minus_1)).

    return:
        float
        Значение интерполяционного многочлена Эрмита в точке x.
    """
    h_i = x_i - x_minus_1

    P_3 = (y_minus_1 * (x - x_i) ** 2 * (2 * (x - x_minus_1) + h_i) / h_i ** 3 +
           y_i * (x - x_minus_1) ** 2 * (2 * (x_i - x) + h_i) / h_i ** 3 + 
           y_dir_minus_1 * (x - x_minus_1) * (x - x_i) ** 2 / h_i ** 2 + 
           y_dir_i * (x - x_minus_1) ** 2 * (x - x_i) / h_i ** 2
    )
    
    return P_3



