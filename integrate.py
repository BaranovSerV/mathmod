def right_rectangles(f, a, b, n):
    h = (b-a)/n
    S = 0
    for i in range(1, n+1):
        S += f(a+i*h)
    return h*S


def left_rectangles(f, a, b, n):
    h = (b-a)/n
    S = 0
    for i in range(n):
        S += f(a+i*h)
    return h*S


def trapezoidal(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        integral += f(a + i * h)

    integral *= h
    return integral


def  central(a, k, func):
    h = 10**(-k)
    return (func(a + h) - func(a-h)) / (2 * h)