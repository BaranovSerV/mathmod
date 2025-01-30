def simple_iteration_method(phi, x0, epsilon=1e-6):
    """
    Метод простой итерации для решения нелинейного уравнения.
    
    :param phi: функция, задающая итерационный процесс phi(x).
    :param x0: начальное приближение.
    :param epsilon: точность решения (по умолчанию 1e-6).
    
    :return: Кортеж из двух значений: корень уравнения и количество итераций, выполненных для нахождения решения.
    """

    i = 0
    x_prev = x0
    while True:
        x_next = phi(x_prev)
        
        if abs(x_next - x_prev) < epsilon:
            return x_next, i
        
        i += 1 
        x_prev = x_next
