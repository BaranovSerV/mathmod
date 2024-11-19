def newton(f, df, x, eps=1e-6):
    """

    :param f:
    :param df:
    :param x:
    :param eps:
    :return:
    """
    x_next = x - f(x)/df(x)
    i = 0
    while abs(x_next - x) > eps:
        x = x_next
        x_next = x - f(x)/df(x)
        i += 1
    return x_next, i


def simplified_newton(f, df, x0, eps=1e-6):
    x00 = x0
    x1 = x0 - f(x0)/df(x00)
    i = 0
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - f(x0)/df(x00)
        i += 1
    return x1, i


def false_position(f, a, b, eps=1e-6):
    i = 0
    c_before = 0
    c = (a * f(b) - b * f(a)) / (f(a) - f(b))
    error = abs(c - c_before)

    while error > eps:
        c_after = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(a) * f(b) >= 0:
            return ('Указан неверный участок локализации!')

        elif f(c_after) * f(a) < 0:
            error = abs(c_after - b)
            b = c_after
            i += 1

        elif f(c_after) * f(b) < 0:
            error = abs(c_after - a)
            a = c_after
            i += 1
    return c_after, i


def secant(f, x__minus_1, x_n, eps=1e-6):
    i = 0
    x_plus_1 = x_n - (x__minus_1 - x_n) / (f(x__minus_1) - f(x_n)) * f(x_n)

    while abs(x_plus_1 - x_n) > eps:
        x__minus_1 = x_n
        x_n = x_plus_1
        x_plus_1 = x_n - (x_n - x__minus_1) / (f(x_n) - f(x__minus_1)) * f(x_n)
        i += 1
    return x_plus_1, i

