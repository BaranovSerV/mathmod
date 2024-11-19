def newton(f, df, x, epsilon=1e-6):
    """
    Метод Ньютона (касательных) для нахождения корня уравнения f(x) = 0.

    :param f: Функция, корень которой нужно найти.
    :param df: Производная функции f.
    :param x: Начальное приближение.
    :param epsilon: Заданная точность (по умолчанию 1e-6).
    :return: Приближённое значение корня и количество итераций.
    """
    x_next = x - f(x) / df(x)
    i = 0
    while abs(x_next - x) > epsilon:
        x = x_next
        x_next = x - f(x) / df(x)
        i += 1
    return x_next, i


def simplified_newton(f, df, x0, epsilon=1e-6):
    """
    Упрощённый метод Ньютона для нахождения корня уравнения f(x) = 0.

    :param f: Функция, корень которой нужно найти.
    :param df: Производная функции f.
    :param x0: Начальное приближение.
    :param epsilon: Заданная точность (по умолчанию 1e-6).
    :return: Приближённое значение корня и количество итераций.
    """
    x00 = x0
    x1 = x0 - f(x0) / df(x00)
    i = 0
    while abs(x1 - x0) > epsilon:
        x0 = x1
        x1 = x0 - f(x0) / df(x00)
        i += 1
    return x1, i


def false_position(f, a, b, epsilon=1e-6):
    """
    Метод ложного положения для нахождения корня уравнения f(x) = 0.
    Работает для отрезка [a, b], на котором f(a) * f(b) < 0.

    :param f: Функция, корень которой нужно найти.
    :param a: Левая граница отрезка.
    :param b: Правая граница отрезка.
    :param epsilon: Заданная точность (по умолчанию 1e-6).
    :return: Приближённое значение корня и количество итераций.
    """
    i = 0
    c_before = 0
    c = (a * f(b) - b * f(a)) / (f(a) - f(b))
    error = abs(c - c_before)

    while error > epsilon:
        c_after = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(a) * f(b) >= 0:
            return "Указан неверный участок локализации!"

        elif f(c_after) * f(a) < 0:
            error = abs(c_after - b)
            b = c_after
            i += 1

        elif f(c_after) * f(b) < 0:
            error = abs(c_after - a)
            a = c_after
            i += 1
    return c_after, i


def secant(f, x__minus_1, x_n, epsilon=1e-6):
    """
    Метод секущих для нахождения корня уравнения f(x) = 0.
    Не требует аналитической производной.

    :param f: Функция, корень которой нужно найти.
    :param x__minus_1: Предыдущее приближение (x_(n-1)).
    :param x_n: Текущее приближение (x_n).
    :param epsilon: Заданная точность (по умолчанию 1e-6).
    :return: Приближённое значение корня и количество итераций.
    """
    i = 0
    x_plus_1 = x_n - (x__minus_1 - x_n) / (f(x__minus_1) - f(x_n)) * f(x_n)

    while abs(x_plus_1 - x_n) > epsilon:
        x__minus_1 = x_n
        x_n = x_plus_1
        x_plus_1 = x_n - (x_n - x__minus_1) / (f(x_n) - f(x__minus_1)) * f(x_n)
        i += 1
    return x_plus_1, i
